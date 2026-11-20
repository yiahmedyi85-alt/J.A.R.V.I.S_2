# Spotify setup for JARVIS

The Spotify integration is a drop-in plugin at `plugins/spotify_control.py`.
It does not require edits to `main.py`, `ui.py`, the dashboard, or the existing
API-key settings.

## 1. Create a Spotify developer app

1. Open the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
2. Create an app for personal development.
3. Open the app settings.
4. Add this exact Redirect URI:

   `http://127.0.0.1:8888/callback`

5. Save the app settings and copy the **Client ID**.

Use the Client ID only. This plugin uses OAuth Authorization Code with PKCE,
so it does not need or store a Spotify Client Secret.

## 2. Add your Spotify account to the app

For Spotify Development Mode, the developer account owner must have an active
Spotify Premium subscription. Development Mode apps can authorize up to five
Spotify accounts. Add the Spotify account you will connect in the app's
User Management / allowed users section.

Spotify also requires a Premium listening account for the Start/Resume Playback
endpoint. Keep Spotify open on the computer or another Spotify Connect device
when using playback commands.

## 3. Save the Client ID on this computer

The plugin checks the `SPOTIFY_CLIENT_ID` environment variable first. Otherwise,
it reads the Client ID from:

`~/.config/mark-lvi/spotify_client_id`

### Linux / macOS

Run this in a terminal, replacing the placeholder with your Client ID:

```bash
mkdir -p ~/.config/mark-lvi
printf '%s' 'PASTE_YOUR_CLIENT_ID_HERE' > ~/.config/mark-lvi/spotify_client_id
chmod 600 ~/.config/mark-lvi/spotify_client_id
```

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\.config\mark-lvi" | Out-Null
Set-Content -NoNewline "$HOME\.config\mark-lvi\spotify_client_id" "PASTE_YOUR_CLIENT_ID_HERE"
```

Do not put the Client ID or Spotify tokens in GitHub. The plugin stores OAuth
tokens locally in `~/.config/mark-lvi/spotify_token.json` and restricts file
permissions where the operating system supports it.

## 4. Connect JARVIS

1. Restart JARVIS so it discovers the new plugin.
2. Say: **Connect Spotify**.
3. Your browser opens the Spotify authorization page.
4. Sign in to the Spotify account you added to the app and approve access.
5. Return to JARVIS.

The first connection requires the computer to be able to open the local callback
at `127.0.0.1:8888`.

## 5. Voice commands

- "Play Blinding Lights"
- "Play music from my Spotify library"
- "Play my playlist [playlist name]"
- "Pause Spotify"
- "Stop Spotify" (pauses playback)
- "Resume Spotify"
- "Next song"
- "Previous song"
- "List my Spotify playlists"
- "Create a playlist called [name]"
- "Add [song] to [playlist]"
- "Rename [old playlist] to [new name]"
- "Check Spotify connection"
- "Disconnect Spotify"

For "play music" without a song or playlist name, JARVIS starts a shuffled
selection from your saved Spotify tracks. To play music, open Spotify on a
device first so Spotify Connect can expose an active playback device.

## Notes

- The plugin uses Spotify's current playlist `/items` endpoints.
- Playback control requires Spotify Premium on the listening account.
- Spotify Development Mode requires Premium for the app owner and allows up
  to five authorized Spotify users.
- Spotify access tokens are stored on this computer, not in the repository.
- Spotify's API does not expose a separate stop command, so "stop" pauses
  playback.
