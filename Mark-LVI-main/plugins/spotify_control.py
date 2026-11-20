"""
Spotify controls for MARK LVI / JARVIS.

Drop-in plugin. It does not modify the UI, API-key configuration, or backend.
OAuth uses Authorization Code with PKCE and a loopback-only callback.
The Spotify client ID is read from SPOTIFY_CLIENT_ID or from:
  ~/.config/mark-lvi/spotify_client_id
Tokens stay on this computer, outside the repository.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import random
import secrets
import threading
import time
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import requests


PLUGIN = {
    "name": "spotify_control",
    "description": (
        "Control the user's own Spotify account. Use for Spotify requests only: "
        "connect or disconnect Spotify, check connection status, play music, "
        "play a requested song or playlist, play saved songs from the user's "
        "Spotify library, pause, stop, resume, skip to next or previous, list "
        "playlists, create a playlist, add a song to a playlist, or rename a "
        "playlist. For 'play music' with no song or playlist specified, play a "
        "shuffled selection of the user's saved Spotify tracks. For a named "
        "song, search Spotify and play the best matching result. For a named "
        "playlist, play that playlist. Do not use this tool for other music "
        "services or for general music recommendations."
    ),
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "command": {
                "type": "STRING",
                "description": (
                    "One of: connect, disconnect, status, play, pause, stop, "
                    "resume, next, previous, playlists, create_playlist, "
                    "add_to_playlist, rename_playlist."
                ),
            },
            "track": {
                "type": "STRING",
                "description": "Song title and optionally artist. Used for play or add_to_playlist.",
            },
            "playlist": {
                "type": "STRING",
                "description": "Playlist name. Used for play, add_to_playlist, or rename_playlist.",
            },
            "new_name": {
                "type": "STRING",
                "description": "New playlist name. Used for create_playlist or rename_playlist.",
            },
            "public": {
                "type": "BOOLEAN",
                "description": "Whether a newly created playlist should be public. Defaults to false.",
            },
        },
        "required": ["command"],
    },
}


AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
API_ROOT = "https://api.spotify.com/v1"
REDIRECT_URI = "http://127.0.0.1:8888/callback"
SCOPES = " ".join([
    "user-read-private",
    "user-library-read",
    "user-read-playback-state",
    "user-modify-playback-state",
    "playlist-read-private",
    "playlist-modify-private",
    "playlist-modify-public",
])

_CONNECT_LOCK = threading.Lock()
_TOKEN_LOCK = threading.RLock()


class SpotifyError(RuntimeError):
    pass


def _config_dir() -> Path:
    root = Path(os.environ.get("XDG_CONFIG_HOME", str(Path.home() / ".config")))
    return root / "mark-lvi"


def _token_file() -> Path:
    return _config_dir() / "spotify_token.json"


def _client_id() -> str:
    value = os.environ.get("SPOTIFY_CLIENT_ID", "").strip()
    if value:
        return value
    try:
        return (_config_dir() / "spotify_client_id").read_text(encoding="utf-8").strip()
    except OSError:
        return ""


def _log(player, message: str) -> None:
    if player is not None:
        try:
            player.write_log("SPOTIFY: " + message)
        except Exception:
            pass


def _load_tokens() -> dict:
    try:
        data = json.loads(_token_file().read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def _save_tokens(data: dict) -> None:
    folder = _config_dir()
    folder.mkdir(parents=True, exist_ok=True, mode=0o700)
    path = _token_file()
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, indent=2), encoding="utf-8")
    try:
        os.chmod(temporary, 0o600)
    except OSError:
        pass
    temporary.replace(path)
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass


def _delete_tokens() -> None:
    try:
        _token_file().unlink()
    except FileNotFoundError:
        pass


def _token_request(data: dict) -> dict:
    try:
        response = requests.post(TOKEN_URL, data=data, timeout=15)
    except requests.RequestException as exc:
        raise SpotifyError("Could not reach Spotify's login service: " + str(exc)) from exc
    if response.status_code >= 400:
        try:
            detail = response.json().get("error_description") or response.json().get("error")
        except Exception:
            detail = response.text[:200]
        raise SpotifyError("Spotify login failed: " + str(detail or response.status_code))
    try:
        return response.json()
    except ValueError as exc:
        raise SpotifyError("Spotify returned an unreadable login response.") from exc


def _refresh_access_token() -> str:
    with _TOKEN_LOCK:
        tokens = _load_tokens()
        refresh_token = tokens.get("refresh_token")
        client_id = _client_id()
        if not refresh_token or not client_id:
            raise SpotifyError("Spotify is not connected. Say 'connect Spotify' first.")
        fresh = _token_request({
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": client_id,
        })
        tokens["access_token"] = fresh["access_token"]
        tokens["expires_at"] = time.time() + int(fresh.get("expires_in", 3600))
        if fresh.get("refresh_token"):
            tokens["refresh_token"] = fresh["refresh_token"]
        if fresh.get("scope"):
            tokens["scope"] = fresh["scope"]
        _save_tokens(tokens)
        return tokens["access_token"]


def _access_token(force_refresh: bool = False) -> str:
    with _TOKEN_LOCK:
        tokens = _load_tokens()
        access = tokens.get("access_token")
        expires_at = float(tokens.get("expires_at") or 0)
        if not force_refresh and access and expires_at > time.time() + 60:
            return access
    return _refresh_access_token()


class _OAuthServer(HTTPServer):
    oauth_result = None


class _OAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlsplit(self.path)
        if parsed.path != "/callback":
            self.send_error(404)
            return
        query = urllib.parse.parse_qs(parsed.query)
        self.server.oauth_result = {
            "code": (query.get("code") or [None])[0],
            "state": (query.get("state") or [None])[0],
            "error": (query.get("error") or [None])[0],
        }
        if self.server.oauth_result["error"]:
            title = "Spotify connection was not approved"
            message = "You can close this page and return to JARVIS."
        else:
            title = "Spotify connected"
            message = "Authorization received. You can close this page and return to JARVIS."
        body = (
            "<!doctype html><html><head><meta charset='utf-8'>"
            "<title>" + title + "</title></head>"
            "<body style='font-family:Arial;background:#10131a;color:#f4f4f4;"
            "display:grid;place-items:center;min-height:90vh;text-align:center'>"
            "<main><h2>" + title + "</h2><p>" + message + "</p></main></body></html>"
        ).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, _format, *_args):
        return


def _connect_worker(player=None) -> None:
    server = None
    try:
        client_id = _client_id()
        if not client_id:
            raise SpotifyError(
                "Spotify Client ID is missing. Save it in "
                "~/.config/mark-lvi/spotify_client_id, then say 'connect Spotify' again."
            )

        try:
            server = _OAuthServer(("127.0.0.1", 8888), _OAuthHandler)
        except OSError as exc:
            raise SpotifyError(
                "Could not open the local Spotify callback on 127.0.0.1:8888. "
                "Close any other app using that port and try again."
            ) from exc

        server.timeout = 0.5
        state = secrets.token_urlsafe(24)
        verifier = secrets.token_urlsafe(64)
        challenge = base64.urlsafe_b64encode(
            hashlib.sha256(verifier.encode("ascii")).digest()
        ).decode("ascii").rstrip("=")

        auth_query = urllib.parse.urlencode({
            "response_type": "code",
            "client_id": client_id,
            "scope": SCOPES,
            "redirect_uri": REDIRECT_URI,
            "state": state,
            "code_challenge_method": "S256",
            "code_challenge": challenge,
        })
        login_url = AUTH_URL + "?" + auth_query
        _log(player, "Opening Spotify authorization in your browser.")
        webbrowser.open(login_url, new=1, autoraise=True)

        deadline = time.time() + 180
        while time.time() < deadline and server.oauth_result is None:
            server.handle_request()

        result = server.oauth_result
        if result is None:
            raise SpotifyError("Spotify authorization timed out. Say 'connect Spotify' to try again.")
        if result.get("state") != state:
            raise SpotifyError("Spotify authorization state did not match. Please reconnect.")
        if result.get("error"):
            raise SpotifyError("Spotify authorization was declined: " + str(result["error"]))
        if not result.get("code"):
            raise SpotifyError("Spotify did not return an authorization code.")

        token_data = _token_request({
            "grant_type": "authorization_code",
            "code": result["code"],
            "redirect_uri": REDIRECT_URI,
            "client_id": client_id,
            "code_verifier": verifier,
        })
        token_data["expires_at"] = time.time() + int(token_data.get("expires_in", 3600))
        _save_tokens(token_data)
        _log(player, "Spotify connected. Your account token is stored on this computer.")
    except Exception as exc:
        _log(player, str(exc))
    finally:
        if server is not None:
            try:
                server.server_close()
            except Exception:
                pass
        _CONNECT_LOCK.release()


def _api(method: str, path: str, params=None, body=None) -> dict:
    url = API_ROOT + path
    for attempt in range(2):
        token = _access_token(force_refresh=(attempt == 1))
        try:
            response = requests.request(
                method,
                url,
                headers={"Authorization": "Bearer " + token},
                params=params,
                json=body,
                timeout=15,
            )
        except requests.RequestException as exc:
            raise SpotifyError("Spotify API request failed: " + str(exc)) from exc

        if response.status_code == 401 and attempt == 0:
            continue
        if response.status_code == 429:
            retry = response.headers.get("Retry-After", "a short time")
            raise SpotifyError("Spotify is rate-limiting requests. Try again in " + retry + " seconds.")
        if response.status_code == 403:
            raise SpotifyError(
                "Spotify refused this action. Check that this Spotify account is on the app's "
                "allowed-users list, that the requested permissions were approved, and that "
                "the account has Premium for playback controls."
            )
        if response.status_code == 404:
            raise SpotifyError(
                "Spotify could not find an active playback device or the requested item. "
                "Open Spotify on a device and try again."
            )
        if response.status_code >= 400:
            try:
                detail = response.json().get("error", {}).get("message")
            except Exception:
                detail = response.text[:200]
            raise SpotifyError("Spotify API error: " + str(detail or response.status_code))
        if not response.content:
            return {}
        try:
            data = response.json()
            return data if isinstance(data, dict) else {"data": data}
        except ValueError:
            return {}
    raise SpotifyError("Spotify authorization expired. Say 'connect Spotify' again.")


def _playback_device() -> str:
    data = _api("GET", "/me/player/devices")
    devices = data.get("devices") or []
    if not devices:
        raise SpotifyError(
            "No Spotify playback device is available. Open the Spotify app or web player "
            "on your PC or phone, then try again."
        )
    active = next((d for d in devices if d.get("is_active") and d.get("id")), None)
    selected = active or next((d for d in devices if d.get("id") and not d.get("is_restricted")), None)
    if not selected:
        raise SpotifyError("Spotify has no controllable playback device. Open Spotify and try again.")
    return selected["id"]


def _start_playback(payload: dict) -> None:
    device_id = _playback_device()
    _api("PUT", "/me/player/play", params={"device_id": device_id}, body=payload)


def _get_saved_tracks(limit: int = 50) -> list[dict]:
    data = _api("GET", "/me/tracks", params={"limit": limit, "offset": 0})
    tracks = []
    for entry in data.get("items") or []:
        track = entry.get("track") or {}
        if track.get("uri") and not track.get("is_local"):
            tracks.append(track)
    return tracks


def _find_saved_track(query: str) -> dict | None:
    wanted = query.casefold().strip()
    for track in _get_saved_tracks(50):
        title = (track.get("name") or "").casefold()
        artists = " ".join(a.get("name", "") for a in track.get("artists", [])).casefold()
        if wanted == title or wanted in title or (wanted and wanted in artists):
            return track
    return None


def _search_track(query: str) -> dict:
    data = _api("GET", "/search", params={"q": query, "type": "track", "limit": 5})
    items = (data.get("tracks") or {}).get("items") or []
    if not items:
        raise SpotifyError("I could not find that song on Spotify: " + query)
    return items[0]


def _get_playlists() -> list[dict]:
    found = []
    for offset in (0, 50, 100):
        data = _api("GET", "/me/playlists", params={"limit": 50, "offset": offset})
        batch = data.get("items") or []
        found.extend(batch)
        if not data.get("next") or not batch:
            break
    return found


def _find_playlist(name: str) -> dict:
    wanted = name.casefold().strip()
    if not wanted:
        raise SpotifyError("Tell me the playlist name.")
    playlists = _get_playlists()
    exact = next((p for p in playlists if (p.get("name") or "").casefold() == wanted), None)
    match = exact or next((p for p in playlists if wanted in (p.get("name") or "").casefold()), None)
    if not match:
        raise SpotifyError("I could not find a Spotify playlist named " + name + ".")
    return match


def _track_label(track: dict) -> str:
    artists = ", ".join(a.get("name", "") for a in track.get("artists", []))
    return (track.get("name") or "Unknown track") + ((" by " + artists) if artists else "")


def _play(command_args: dict) -> str:
    playlist_name = (command_args.get("playlist") or "").strip()
    track_name = (command_args.get("track") or "").strip()

    if playlist_name:
        playlist = _find_playlist(playlist_name)
        uri = playlist.get("uri")
        if not uri:
            raise SpotifyError("Spotify did not return a playable playlist URI.")
        _start_playback({"context_uri": uri})
        return "Playing your Spotify playlist, " + playlist.get("name", playlist_name) + "."

    if track_name:
        track = _find_saved_track(track_name)
        if track is None:
            track = _search_track(track_name)
        _start_playback({"uris": [track["uri"]]})
        return "Playing " + _track_label(track) + " on Spotify."

    tracks = _get_saved_tracks(50)
    if not tracks:
        raise SpotifyError("Your Spotify saved-tracks library is empty.")
    random.shuffle(tracks)
    selected = tracks[:min(50, len(tracks))]
    _start_playback({"uris": [t["uri"] for t in selected]})
    return "Playing a shuffled selection of " + str(len(selected)) + " songs from your Spotify library."


def _playlist_names() -> str:
    playlists = _get_playlists()
    if not playlists:
        return "You do not have any Spotify playlists yet."
    names = [p.get("name", "Untitled playlist") for p in playlists[:25]]
    suffix = " and more" if len(playlists) > 25 else ""
    return "Your Spotify playlists are: " + "; ".join(names) + suffix + "."


def run(parameters: dict, player=None, session_memory=None) -> str:
    command = str(parameters.get("command", "")).strip().lower()
    track_name = str(parameters.get("track", "") or "").strip()
    playlist_name = str(parameters.get("playlist", "") or "").strip()
    new_name = str(parameters.get("new_name", "") or "").strip()

    try:
        if command == "connect":
            if not _CONNECT_LOCK.acquire(blocking=False):
                return "Spotify connection is already waiting for authorization in your browser."
            thread = threading.Thread(target=_connect_worker, args=(player,), daemon=True)
            thread.start()
            return "Opening Spotify authorization in your browser. Approve access there, then return to JARVIS."

        if command == "disconnect":
            _delete_tokens()
            return "Spotify has been disconnected from this computer."

        if command == "status":
            profile = _api("GET", "/me")
            label = profile.get("display_name") or profile.get("id") or "your Spotify account"
            return "Spotify is connected as " + str(label) + "."

        if command == "play":
            return _play(parameters)

        if command in ("pause", "stop"):
            _api("PUT", "/me/player/pause")
            return "Spotify playback paused."

        if command == "resume":
            _api("PUT", "/me/player/play")
            return "Spotify playback resumed."

        if command == "next":
            _api("POST", "/me/player/next")
            return "Skipped to the next Spotify track."

        if command == "previous":
            _api("POST", "/me/player/previous")
            return "Returned to the previous Spotify track."

        if command == "playlists":
            return _playlist_names()

        if command == "create_playlist":
            if not new_name:
                raise SpotifyError("Tell me the name for the new playlist.")
            is_public = bool(parameters.get("public", False))
            created = _api("POST", "/me/playlists", body={"name": new_name, "public": is_public})
            return "Created the " + ("public" if is_public else "private") + " Spotify playlist, " + created.get("name", new_name) + "."

        if command == "add_to_playlist":
            if not track_name:
                raise SpotifyError("Tell me which song to add.")
            playlist = _find_playlist(playlist_name)
            track = _find_saved_track(track_name)
            if track is None:
                track = _search_track(track_name)
            _api("POST", "/playlists/" + playlist["id"] + "/items", body={"uris": [track["uri"]]})
            return "Added " + _track_label(track) + " to " + playlist.get("name", playlist_name) + "."

        if command == "rename_playlist":
            if not new_name:
                raise SpotifyError("Tell me the new playlist name.")
            playlist = _find_playlist(playlist_name)
            _api("PUT", "/playlists/" + playlist["id"], body={"name": new_name})
            return "Renamed the Spotify playlist to " + new_name + "."

        return (
            "Spotify command not recognized. Try connect, status, play, pause, resume, "
            "next, previous, playlists, create playlist, add song to playlist, or rename playlist."
        )
    except SpotifyError as exc:
        return "Spotify: " + str(exc)
    except Exception as exc:
        _log(player, "Spotify plugin error: " + str(exc))
        return "Spotify encountered an unexpected error: " + str(exc)
