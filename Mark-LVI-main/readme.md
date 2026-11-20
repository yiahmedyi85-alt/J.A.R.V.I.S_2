# âš™ï¸ MARK LVI (56)
### The Ultimate Cross-Platform Personal AI Assistant â€” By FatihMakes

> ğŸ“º **[Watch the full setup video on YouTube](https://www.youtube.com/@FatihMakes)**

A real-time voice AI that can hear, see, speak, and control your computer â€” on any OS. Supports Windows, macOS, and Linux. Built on the Gemini Live API for native audio streaming, delivering zero subscriptions and total digital autonomy.

---

## âœ¨ Overview

Mark LV gave the assistant a screen. **Mark LVI lets you choose what runs it.**

Until now this was a Gemini assistant, and only that. If you had no quota left, no
connection, or a rule that says your microphone does not leave the building, you
had no assistant. Mark LVI adds a second way to hold the conversation â€” speech
recognition, a language model and a voice, assembled from parts you pick in
âš™ â†’ **ENGINE & PROVIDERS** â€” and a way to point the assistant's own background
requests at a different model without touching the voice at all.

The local model can be on your machine (Ollama, LM Studio, llama.cpp, vLLM) or
somebody else's API (OpenAI, Groq, DeepSeek, Mistral, xAI, OpenRouter, Together).
Both are the same setting, because all of them speak the same protocol.

**None of it costs anything if you do not use it.** On a default install the
`providers/` folder is never imported â€” not at startup, not on a tool call, not
when the settings drawer opens. Measured: the decision takes **0.16 ms** and
loads nothing. The folder can be deleted, and deleting it changes nothing.

Everything the assistant already does carries over untouched. A local engine
inherits the avatar, the lip-sync, the self-echo guard, push-to-talk, the wake
word, memory, undo, the confirmation gate and every action and plugin â€” because
it enters through the same door the Live session always did.

Mark LVI also changes what the assistant is allowed to CLAIM. Every tool that
drives an application now answers with what it observed rather than with what it
attempted: `done` means it was checked, `unverified` means the request went out
and could not be confirmed â€” and the assistant says exactly that instead of
rounding it off to "done". Opening an app watches the process table for it.
Closing one asks the application politely, then checks whether it went.

It's not just an assistant â€” it's an extension of your digital life.

---

## ğŸš€ Capabilities

### Core Features
| Feature | Description |
|---|---|
| ğŸ§‘â€ğŸ¤ Holographic Avatar | An animated human head in the HUD â€” real facial geometry, lit and drawn in software, no GPU or extra packages |
| ğŸ‘„ Real Lip-Sync | ~50 mouth shapes a second from the audio's formants **and** the transcript â€” closures, spreads and rounds, not a volume meter |
| ğŸŒ Language-Free Mouth | Articulation is derived by Unicode reduction, so Latin, Cyrillic and Greek scripts all work from one rule set â€” and scripts that hide pronunciation fall back cleanly |
| ğŸ™‚ Facial Acting | Brows track the phrase, gaze saccades between fixations, natural blinking, a small nod on stressed syllables |
| ğŸ˜ Face as Status | Looks away while thinking, meets your eyes while listening, lids fall while asleep, glances down at new content |
| ğŸ§š Push-to-Talk | Hold **Ctrl+Space** and the mic opens â€” closed the rest of the time. Truly global on Windows, window-scoped elsewhere |
| ğŸ”‡ Self-Echo Guard | Never answers its own last sentence: the tail of its own voice is recognised and dropped without muting you |
| ğŸªª Runtime Self-Knowledge | Name, OS, abilities **and limits** are generated from the live system each session â€” rename it or add a plugin and it knows |
| ğŸ™ï¸ Wake Word | Local **"Hey Jarvis"** detection â€” sleeps until called, auto-sleeps after 2 min of silence, and never streams audio while asleep |
| âš¡ Instant Acknowledgment | Speaks a short, context-aware reply in **your language** the instant a longer task starts â€” no more silent waiting |
| ğŸš€ Faster Live Engine | Runs on **Gemini 3.1 Flash Live** â€” roughly 2Ã— faster time-to-first-word than the previous model |
| ğŸ§© Self-Describing Skills | Every bundled skill declares its own `TOOL` dict + handler and is auto-discovered at launch â€” adding one is a single file |
| ğŸ§  Recallable Memory | No size limit and nothing silently forgotten â€” the prompt carries what fits, the rest is looked up on demand from a local search |
| ğŸ‘ï¸ Memory Panel | See every fact JARVIS has stored about you, when it learned it, and delete any of it in one click |
| â†©ï¸ Undo | Take back what the assistant did â€” files it moved, renamed, created or wrote, and settings it changed |
| âš ï¸ Real Confirmation | Shutdown, restart and WiFi wait for a button **you** press â€” the model cannot confirm its own irreversible actions |
| ğŸ§ Audio Device Picker | Choose the microphone and speakers by name, filtered to the short list your OS shows â€” and measured, so every entry actually works |
| ğŸ”— Session Continuity | A dropped connection, a voice change or a device change no longer wipes the conversation |
| ğŸ§© Plugin System | Drop a single `.py` file into `plugins/` â€” JARVIS learns a new skill on next launch |
| ğŸ“º Video on the HUD | Plays YouTube, a local file or any video URL **where the avatar sits** â€” starts muted, sound on request |
| ğŸªœ Model Ladder | Nine Gemini models in one measured order â€” a quota, a timeout or an outage steps to the next rung instead of failing |
| ğŸ”Œ Choose Your Engine | Gemini Live, or your own STT + LLM + TTS â€” picked in the UI, no file editing |
| ğŸ  Local & Third-Party Models | Ollama Â· LM Studio Â· llama.cpp Â· vLLM Â· OpenAI Â· Groq Â· DeepSeek Â· Mistral Â· xAI Â· OpenRouter â€” one setting, because they share a protocol |
| ğŸ—£ï¸ Local Speech | Whisper on your CPU for hearing, Piper for speaking â€” **~50 languages**, neural, entirely offline |
| ğŸŒ The Voice Follows You | Whisper hears which language you spoke; the answer comes back in that language's voice, switching mid-conversation |
| ğŸ¤« Reasoning Stays Private | `` before answering, and several servers pass that through as ordinary content. Without a filter the assistant reads its own reasoning aloud: half a minute of *"the user is greeting you, you should acknowledge warmly..."* spoken in full, before the greeting. It also lands in the log, the session summary and the conversation history, where it costs context on every later turn.

It is filtered on the stream rather than with a pattern, because a tag is regularly split across two chunks â€” `"<thi"` then `"nk>"`. Tested against two hundred random chunk boundaries.

#### ğŸ›‘ "open whatsapp" opened WhatsApp four times

Gemini Live ends a turn itself. A chat API does not: every tool result is a fresh request, and if the model answers it with the same tool call again, the loop has no floor. The tool worked, returned *"Opened WhatsApp"*, and a small model asked for it again rather than replying â€” launching the application on top of the copy already running.

Two limits, because they catch different faults. A **repeated** call means the model did not understand the result it got, and re-running the tool is actively harmful â€” so it is answered from what the tool already returned and never reaches the application twice. A long chain of **different** calls is a model wandering: not harmful, not converging either, so it is capped and the model is told to answer with what it has.

### What it costs when you do not use it

| | |
|---|---|
| `providers` imported at startup | **never** |
| Deciding which engine to use | **0.16 ms** |
| Extra work on a Gemini tool call | one `stat()`, ~39 Âµs |
| Settings drawer open time | unchanged â€” the panel loads on the click |
| Tool declarations sent to Gemini | **byte-for-byte identical** â€” 56,148 characters, verified against the previous release side by side |

The first version of the settings read the config file on every call â€” measured at **143 Âµs**, paid by every request in the app whether a provider existed or not. It is cached against the file's modification time now, which also means the panel's changes take effect with no restart, and nothing has to tell the module that a setting moved.

### The things that were measured and were not what they looked like

#### â± The first thing you ever say took 8.9 seconds
Loading the speech model is 1.4s. The **first transcription after that is 8.5s**, and every one after it is 1.1s â€” it is the recogniser bringing up its kernels, not the load. That was paid by whatever the user said first, which is the worst possible moment: a person who waits eight seconds concludes it is broken and says it again, and now two turns overlap.

The warm-up now runs a throwaway recognition on a tenth of a second of silence before anyone speaks. **8.92s â†’ 1.16s**, and the warm-up itself costs 1.08s of a moment nobody is waiting for.

#### ğŸ”‡ A system voice given a script it does not have returns success and silence
Measured on an ordinary Windows 10 install: two voices, both English. A Turkish sentence came out as English phonetics â€” poor, but audible. A **Russian sentence produced zero bytes, with a success code.** Silence that reports success is the worst failure there is: the assistant looks like it ignored you, and the suspicion falls on its speakers. It is now an error that names the cause and says what to do about it.

#### ğŸˆš A whole Japanese paragraph was synthesised as one block
The sentence splitter required whitespace after the full stop. Japanese and Chinese do not put one after `ã€‚`, so nothing ever split. Two rules now: after `.!?` a space is required, or every version number becomes two sentences; after `ã€‚ï¼ï¼ŸØŸÛ”à¥¤` it is not.

#### ğŸ§® A default that only reaches new installs is not a default
The tool budget below was added as a preset value, applied when a service is **picked** in the panel. Anybody who had already set up Ollama never received it â€” measured on such an install, 20 tools and 18,039 characters on every turn instead of 14 and 11,871. Most of a fourteen-second wait for the first word.

It is a property of the endpoint now: a model on your own hardware â€” loopback or
a private address, because "your own model" often means the desktop in the next
room â€” gets the budget unless you set one yourself. A hosted endpoint never
does.

#### ğŸ§® Halving the tool count did not halve the payload
This install declares **45 tools and 56,148 characters** on every connection. Gemini carries that. A local 8B model does not â€” it picks the wrong tool, or emits JSON that will not parse.

The obvious fix is a limit on how many tools it is given. Measured, that is only half a fix: 20 tools down to 8 â€” sixty percent fewer â€” took the payload from 18,039 characters to 9,050, because the tools worth keeping are the fat ones (`file_processor` alone is 3,024 characters). There are two budgets now, one for count and one for size, and whichever bites first wins. **Gemini gets no budget and therefore every tool, in the original order.**

#### ğŸ”Œ `localhost` is not `127.0.0.1` on Windows
Windows resolves `localhost` to `::1` first; Ollama and llama.cpp bind to the IPv4 loopback only. macOS and most Linux distributions order it the other way â€” which is exactly why this ships broken, because it works on the author's machine. Every local address is normalised to `127.0.0.1`.

And a proxy set for the whole machine is **not** used to reach that same machine: `HTTP_PROXY` is commonly set globally on managed Windows and macOS, `httpx` honours it by default, and the result is a timeout that reads as "Ollama is not running" â€” sending people to reinstall a server that was working the whole time.

### The shape

#### ğŸšª The new engine speaks the old engine's language
`main.py` touches its session through exactly four methods and reads five fields off the events. That is the entire contract, so a local pipeline that implements those four is invisible to everything upstream â€” the avatar, the mouth, the echo guard, the tool dispatcher, memory, undo and every action and plugin work unchanged, with nothing added to any of them.

The alternative was inventing a neutral interface and translating each side onto it, which means rewriting eight thousand lines of code that already work so a folder you might delete can feel symmetrical. The new thing adapts to the old thing, because the old thing is the one the users have.

> **The deadlock this avoided:** `main.py` answers a tool call from *inside* its loop over `receive()`. An engine that waited there for the generation it triggers would be waiting for events only that loop can consume â€” the turn would stop dead on the first tool call and look exactly like a hung model. Every send method records, schedules, and returns.

#### ğŸ‘ï¸ An engine that cannot see is not given eyes
Each engine declares what it can do, and that declaration feeds two things that already existed: the tool list, and `_describe_limits`. A text-only model is never offered `screen_process` â€” and is *told* it cannot see, so it says so instead of describing a screen it never received. No special case anywhere; runtime self-knowledge was built for exactly this shape of problem.

#### ğŸ›‘ Something has to decide when you stopped talking
Gemini Live decides that on the server. Nothing does locally, so with **push-to-talk** the key release is the signal, and without it the engine finds it in the audio: the noise floor is measured continuously â€” fast downward, slow upward â€” speech is what stands 3.5Ã— above it, and 700 ms of quiet ends the turn. Energy, not a model: a neural detector would be better, but it would also be a second download, a second warm-up and a second thing that behaves differently on each platform.

### âš–ï¸ What local mode is, and what it is not

It is **not faster.** Gemini Live answers in roughly 0.3â€“0.6s because it has no separate recognition step, no separate synthesis step and no round trip to find the end of a turn. A local pipeline has all three, in series â€” 1.5â€“4s on ordinary hardware â€” and a turn that calls a tool costs **two** model round trips instead of one, because a stateless chat API has to be asked again with the result.

It also gives up barge-in, server-side turn detection, proactive audio and session resumption.

It keeps tools, memory, the avatar, lip-sync, undo and the confirmation gate. And it keeps working when the quota is gone, the connection is down, or the microphone is not allowed to leave the building. That is the trade, stated plainly so nobody chooses it expecting the other thing.

### ğŸ¤ It stopped saying it had done things it had not done

`open_app` answered **"Opened Spotify."** whenever its launcher returned â€” and on Windows that launcher returned the instant a *shell* started, not when an application did. A misspelling, an app that was never installed, an installer that moved: every one produced a confident success, said out loud, while nothing appeared on screen. That is worse than an error, because an error is something a user can act on and a false success sends them looking for the window.

Every tool that drives the computer now answers in one of five words, and the model is told what each may and may not be spoken as:

| | |
|---|---|
| `done` | it happened, and it was **checked** â€” never assumed from a return code |
| `unverified` | the request went out and the result could not be confirmed. Not a failure, and never to be spoken as a success |
| `failed` | it did not happen, and here is why |
| `ask` | nothing was done, because doing it would have been a guess |
| `started` | it is under way; the outcome follows separately |

The evidence is real work, not a longer sentence. Opening an application watches the process table for a new process answering to the name. Setting the volume reads it back. Setting the wallpaper reads it back. Sending on WhatsApp goes through the driver that proves the conversation is the right person's. Where nothing can be read back â€” a keystroke typed blind into Telegram â€” it says `unverified`, and the assistant tells you it cannot confirm, which is true.

> The shape came from `whatsapp_call.py` and `whatsapp_guard.py`, which reached it by hand after a real message was reporte3Î#üş|öI‚»(5fLi)³´I™£Ò¿eÅ^•€Tg¢×åö¿*·Šå^ ú*˜ŠÜÎX¤Û;¶c×E…!D¥ESwp‰?^»×êRÔ×dàv"oÂê©úKE‡Hc«X4ç*ò³D Ô:FÄ˜m	¶¤‰KÁ÷µv
1,óàóàA…_ø@i_µ»ën%—åóáLÓ3e >Ë+ªâØr:¦Ò/ú^[3î«¯déÕ'êjt.>QXÛG­zùîmWÕ`„kÿ2*î!Ñ2NÉ#_TxÜ_>ƒ…Ü]µ½¢û|øµ¼Ô*J¡^ˆÁ¦}J@ò=m6 ä|Fi¼XK¦ê4²ÊŞ^õ2£/‚š<¶µkJ—[o®K~öu|QtJ…g¤ÚÛæ+ãsSÍh½õÏ¨FÏİOZhfDQM¡ñSBÅ„æ¥òÀBŒ"ŞD%ËwVs˜§kï•úzı@%õr@ÕŸáX©Ö|èÉi+Ø÷ËçÍ2ş:×twÙ»ğº_u€RU»>¬+àbøÅ4LV`Ä^F†ùQ¼“¶WIS†\N;Â{öpà Ew¨^ÕWÄ}K<Şêf’@¤«}Çç	òz‚*²NˆJÀâ4RtKò&½OİCéN!ùï€ú¤»[!ö7İ®òSŞş)² (òWø7ù:×TƒÆºN¼0ß³Z´îú}o:9í{ŠSÆ½?Á1¼–GÆU/É4Rš0uÿÈ›Qw"Lb4íVÎÆ¡'~â›6ùñ¹YÏBøpl úâ´\I:íFóÛ‚+À­8>n&DıNwœ"ä6§ëáÌ”…½ìãÄÒ•åÚ~˜Rm 0?o‘€(µ9õÒkÛQ8gÇTëø3ã5$çºfq<ÌöhpÄÀ_@#HR&É‰¨@T:vh`VİKOCC¬LZf™ÒÆœÎ m5ŠBÕ2„€]	~vAfzhì²%R&²ƒ8NIì"RÚaÆB©Oc`ó.½)8{iäóvâTc¼æ³K`Íş@~;Ø-3Úez«ÎõhÅ8»5A,4¸×JõXyu¿K›J>ó;°ULR^À+"×ß?i‘+Öe5dL® šy«ÏÏõ¸Å»$ÎM|1l;Ö‹5ÌEM.\ÇøAÖò«°)œ)CP‡“_ÔN
S¼ÖhÎ·ˆI fyê%Æyê`r-ÌúÇzUHdv;9xÅ³ù|Y§b\"!bÿT/8*/"¤5zB$spq4Q“ßvMXœ]Yx:£¥BÃlº”	R7Ã’0äÌªJ¶Ö@
éqJ7É3F•L1BĞØPÕ]¶y_ÜÚÆ
3J®~ÕÁİòŒaß•%vás9]vXT
{Æ<0=•ËNa0”lêÁ^WFWpuº.ÿ)_w8ÏÉ°æëÛîc¸Tq½†„a"ÑÔà2„'É(æ:+ÌV¶ˆ6œw¢Ny|Ç±’|æĞ£2Ö|RsŞFˆ»1—„qrE]ìhMP¾çe.QA!©¢ˆ¿bûü‡àıÁ`æğ²FSr5`ÇhÚTÜpo…Ä1zJÄŞH|†¾3Ñmƒ¼8rPGi‘¬¨ å~Úê2´u££¦°‚Êv]"Y@¿ pM^C&Xñ”­£oĞ·5ö~]Ä‰Œ·DÎÌÌ`
û$¹•–•Q’dö?¸Ôm)(—Aq°EwgfB/!Üğ#ƒÈ  dRB&Z`%8B¢i&cc+*ä]i¬j’_tBZ …‚ñ@moDME4IÖ š&ëÒJwM|RŸtjq, OïLánìœR8Ü*Æ.‹_eš^ˆÇ„^Ç/üE{rZaÚ;_²G|S×<$p­ ÛXÓÍ€İZ^…!fkfıš¨+×Äzc|xÀzÏÒ§J&í"^c%°IqHàWznguìF{34¼³5&J_ç&#XRä´Geğ"ğø`ò·Ô—§1klGofÕÎ%i÷8»ãMDGÃ60éŸMÒÔëÛ©›´n&¬’‡ª¼–óåÛâ×[wàoHEm7İ©HŸÎ÷Åßîş/BäL1©ŸD•BQ5¥yÿhtXY€[ n\	q¼£oP.gM¸Üi0_mH2g´h¼2Lw`EªQêx5úyu62i'^>)O}ÛE-7{VKû'2{²\k²q\HkŸôAÇ™	6{âZÖj‡l O-—L]Ñƒa³±ÊGv@v§P3|c S9K®y/Ä/zŸ¨6Z\ÒBôqn?H )i?ÖÍ}—#LlVïm°°Éíl0üJvqVôß_QùJ‚À³ÔÓMuh]i'8©Œ)|wšïkåto×sÏ„l|ŒxjàMı–ƒL4-1 MºHsB']j}>Í±#u#O†âÓE‰H8ßP“"‘&ws&LQCÑSÍÄ‘œÊÈ5Ãsk˜’3WÈ"ìMgyÂö
.·çMˆxÙîßA'^¿f¼s{KœæE%[Š{TsFÊt>4Ç2ÍQRÖ‹)¢s iWÈev]%•>²Äû¦ÃJFŞ†Yw7®›éæ}$e2Æ‹^O¤å¤¦*VÃdÒïÛ\va}Bø4YF!4£¤¬İÙFHo""(êQLUA$+Y’!Fµ-øtş&^¶pªuÈ%G—.tL~Úf‹3â‰$D$À-+ÎJbïX„H>‚P=]ğ7ß-šPÔP^ñDj–±â-+#sñ9U~ˆİ
]s *^Ï!*¯<gS.&!c²SòY
4ùŠ–in¼÷ò¯9g/hQQp9Im¸lHô™‚=p=J™&FÆ(Ç.LVƒI¤-qä!	7`­{è…5i‹:iA³$ûjÃ;ÊP>ˆËU4P{®52óyÜ GYz&TÖã„úåE[*mèHÕ<”™¾7½z$Fj:¯g÷©ã
üL»y¶o‰¢Ã']ƒ[?7øÊ;b[Ø—FtbşÆ[,FMË[L5n1W§«œD£Omz?>ÄbèU
Ö±ÅÎÑÙ#œC–6K5Ú[³ÇäşdèúbóxM%íHóÜ\¨–XÕ	J Ò¹É4ÄL{ó1W"
B3d*§:·ìXh$bÂkìs\é6fGÆîHo&hÊöa±/o‰Xw@[ƒÆG¯8 &S3|±´fÃ±êvy­gpuJbIÅO1ŠØOÆ>,8LŞ‰¶X\Zà?@ë:–vq—œÊR%H½M{)·PäßNi”º4È~`{r¡¨G2Wádm•!vZH2R$‘tÄö[:k
 Aè	¸17Ot„r#ö
avzÕQ$Û@O ÑÃ7%³J æAS2C9CbaDV).GSÔmÆ$. ¶Ù³4›šYA,P“î°z;gšiÂ
%a|D$~$¾š¼2ÓKQ_ éágÙF†(2Ç:C‡y'ùpaP9ô9t§ÁZÜo—~³DûNÃ 
[N¯_>uoiŠ‰i¸+c!%p'µX&ks´î`
˜>Ü'yD9	}1T2?7d†9~N3t!<[8o‰—$#äÂ[?^ô=¥Ow¼z ïw¤—rtu¾H¶†¯KJ,}„Dx"9éÛë XIE‚MOá"Ÿ9<DF›ZR‘
uÓah&H1l|g 2õ.n§m-f+lv‡Ñ!¶.1ï@Ã&1uÊt[e~1LBâ1b^ákù_(Î&„lHo(¡%ØÑàvİ,%ir@/c–Õ„J)‹êN!ÏY:EÕõÓ44=³AùVñqdku\+AÁvJ
áJø`À½¡3b|›{UgÔQBêdö©“ô3e;0£z[eßs÷O°óŠÎ!'×Ú‘…/<1"¹ĞixQJOfàõy5øià®”Â“;8Ù®n„ ôn|æÇc8Qá¢9~¡otê@_:_3f[0¶B¡‘,:J»d‚y‹•V]äGÙ†ÔftÑÆ˜t­œI ¸;3Äû(iØ§0b§€PÖ{-lQ*OPÔ~ˆT{L¹9dE‹çqİLª$Íñb5[Mqˆ†M9à÷õ/iç*Ò5›>Á(cWC¨öÍ	Ù iOû:p?D¼	æ†^´oŸ¹Xü£³%Ëß¼zÿç«‘×f¢àl‚Ñ5!ìd0Ò	·^E¹z5Ğ˜,?2p:: ,>.
0Q|u·P^N‰FÌÅdáqö@íÒC:a;®q8·{Xx[õ¼%·R\E*ZUMX5Q—óÎŠÊT[et±Kbà)HVKÙE°Ä…!9¦vQÄ2Wş%hÑòöPŒ Ñqrdÿ»‰µOì:$9mŞ Æ<İQŞ¢mµ©$&Íí•yª9îe}YûÇhp@ ›#Có¯P¶ÀByYámf† héÄVàW"hŞe‰*©Áœq·×,ò«RÿéÖ¶Gøµ;…Éİr/k¸„éËD+9JX+Î6:-Rj3T?yYÈ"å0aboZ#7Ÿe'‹¹|~ÕşlZÍ:Ù„rÔ¾åGö \~=KsyaAcg4‚HB ßc~dÁÍy?zÃŠ{D_üt‡TmBbõ´ôÛQÌ<Á‡GA6¼ö ô¹O™VäZ`À@ÌA€ú÷ ¨[?ìşöj@ÆúJğ¾nFAH|ğK­¸ceTÔ,%qí³!“7²$_¬ÉzH"¸2â_uÒ2Izó$Òu&<l[Èæ||†rmÉ+%P{f…ı›ç}]áŞÒğ®5½3À§
ƒˆP(5t,O—D¹±],–h	lbBÖ»‘ÿêóˆ}HJƒÏh¹Ê×ÉM“0³G¯n	{HGavÚ»ác²§Ús@;	”	–ĞI&ÿY…¿š'i`«ì¶G];0‹J­R#Nœwß\åÓş¬ı—ª(bmX?gCøËtÈ…Í=ì6B¯G}¯WZ½ö\İN0KÜø]K“4ñX¯³Qñ9Z¡ş]^Ji
Ë2¦HP:t`vÚÛ´CŠ›Œ-8C6¬/æÑ3¯nbÕNĞmJŠØzj9ìæ:¤ÊGèñ
M.|„Â]˜ëYjrœ LF&è§$*YõQAãƒ¹Ó/!M2_×D9ÏB >p¾âıbÛ?L3å$o"'p‚'J¶úi&)Ì;OÀm-G¨#ƒsŠc:Z"©DmH	­áRA¦.ƒ{.šÊÌX11ãYb ÿïÃ.CXxĞ©U&\ñ0©.[òè@k®<F,è{·Iğ—şœ]º#–µ‰Xï!áêÇ6„1¬pSGpÙş—†j²'öÂoØ´¹\»”7HT3ZKè3o ]ÓèX¼Hl%ş)Ótƒ<ÿ(gQÓ*ú#Lñï)ÚHŒõ!×Ğ €“é5m<äü$ÚÈ^ó¦VÀƒb2‚ş¥©x?VÈPÅ–M×RÑÄ
ô#&r€&í1—’9bùFvIlİ$Á8g›Ş¯5bÂ¬t£ôCº›ÆšoG¯Q˜w¸ƒ«z´Ìş^ß&áŒo*ÈıúÊN:ÎEC0µäHD™Aãij%&v^Æ²×€ŸUá
¹zØˆzVÉĞE•‚ è[BË~îöë	ë&$ !ßçÀXÈ¶ºcú1`ÿ¡müŸ­ê#œ#”3Úäæá!Î•‡’pöC¥x ¼a–§l(âú©hd-ævĞğ‹Ç£Bq2 Ü’2$8[É¿;îÆÉ·Èå¬ö×óo¸Y„'0«zâ‰ƒÂº–çTt(32‰±ÆK¬-kŠln=Ä‰x¯úèÁcTá–Í‹Ë´m
‡²“ˆG´xd“°&/ÓZmrö;t/^ÊŸjnµï:'IáLR=>E!: pkMbÌ²ğGZ!¡e^…ƒˆ';IbÄ4@…U*äX¤³`ë¨eÁp‹~gmaw¾sÊudâoâegç`o¶ÿ3%È=+{*ÒB÷Ú€Fóäw5Gò7^Ñ1V³ZÂ´5W¼Dr¾NjbêÌ«Y´C‹Âè ò„×B	=½\§¯Qr<QèCK®EŠ Á‘>ëkdÖHv/Kw%³ÏÖ¡54x—à ·À5Ù.fOeW?ìáGDtÂ½x\¯Qz\W@A5…û%ê5ˆ_4ƒJ|ú7wÏË¿%…OÙ­¯}b{éäˆo¸!£Áj~Fìô¼0]`ô1ùÂşh?Ë%n]ZÆ ıºËªzi—÷ƒ­“-<dKØ4¥WÙ¥,8TëÓÜ? bqìÆ
#XİNtTï¨DÙ%"/ô±1 ¹rzœ<,em#(Ñ÷²AEÕO<-lÖ+m%ënß'çÚ(5!W72*&ã]3¾dºçõ{Íbm]@”†[-&	bùL6ĞS²º=Š?,»6f;üg‡UìÅ‹&·i¹q2FûfÈÓªğı8;Àâ‡ROüŒõê0ûùUËx(y*ó™³„r*L±rK-AI®.Wn,Ûúˆ¼ædò+FÖK¢dvRÇÙcĞeZZqzäÃ=%ÍIáÏwÑšåk=AVxwÌ!.sÅ(EªJR|DÛu®ç	[ÆYüÅĞIeJx8Ûn¡	ÊGfxËÚc¶Àµ½`q}Öd*’Y›ÔlD@4ë<Ö4ÈeF/ )˜dl~mChS-b*À†l±â55¿ÅAY¼ü ‹!Œ%Mrxóâ±°ñ³=sgKm_D–4ÕÜåtÄS
Ì>àP²ºÀ3#V>`~Wà}ÁìÙ‚#£»È¹Ú4ª]>d-FKÆ‹3iz¼…‡¥m’*:ô
jq›}j°4ñ11tG­CßçH	ß? #4 +Zm
g,ö7‡nVaS^	58W-;)jXyT%7r8")²”v%Mi@**¡{º#Ñ7ã¶Š¿NL‹z2dA§VÔ†g–ƒtÕ*	_2¢%Ëbßâ_Á±>óënVht·Ê]¥Ì;ïU¹?³ßíz™êÊ†.NOwZŸéYDvu­O…@N"=tÇgfó@{I%Àµ—.H›Û½ï¨aº*³É³#uj$Ğûş­=#x€;'¬&‡(ô!A):ëüâlÿÙ-Lé¼÷Ph;Æº|tšÌòxÓD#ØK/7¦€Ol‡nlëğÇikR|RX€rO rqOeLÿØí,yp”¤Ä3*SiQi5Gù9Ä‹>$Ä½>Z"9^ôÇöQyÀgïjKZ­Š'2‹H5Y%hUA_gğî=yYF–ü\/îL~;!G5Fã[y1RIÏ¼dQKW6‰{xOy@Cœª6',>ÇJ£j«@+î#gÑ.%©SzM;¿c‚ ¦íFLğH8(/ô,Ïá¤hÛEX‹L-hCâ*Şe4YÍ‹v§||UNMfûÅq<s7íáƒ:ŸÄ4a¹©F“l¦ÀB¿» .Ò6möm­,E6˜×7 z×@²+jÇuc	Ù·d-/³±ÖÚx.*X34'9M‚‡Oc Dœ²+Xãh?~B
aç¨aPKWV# •C{p¯cX36ÇL#À…
|_{	€FúÃƒgÓ˜?2myG¦´Zl:Ÿ=i%ã§ˆ¸Î•É¦Ş¨òÎe4`V5ö8¬	i§aşpZµ70gI:™@ø~m¯Éx/4Ê[Y¹”é-<.Ğ`1r'"f‹Xæ8Ø:z3(Ô&41	ğŠ_óyiy±:î‚/a¦Y'HÕÍ:ü,Éo?äÔgQXRM­ÇSS	oi Òr€o&X:z8bÊ"ìØ\dÕp‹eKğh´xtb­˜l8`ó&jh€èÁweno@bÇ¶‚DRpPØ½XÆOÄ=Á{ ø*gª~ıŞ%‰À
Kxox]¹ƒ.³óG—\Á¿e8ï«y7¦º´AÙgJ˜Yë¢øÈ'êİ)Ë”gÊ¯ÖÄµ¸¶ï lhÁuO?á§H`Gu ˆŠt)Hì™¯¢8 g¨îÒ‚ïO›$Yµ»C^-y´*$Oæ(z¾€3K~½ğõÉmG²]/h.’m0›:yÿMsÚg?G~¡ÒJ>…Ş¢,aN
Ù;N,@QZ…à"ğïìQ³î8M>.ONr×EB~ã¯{®WbüÁEi†&&¶ÔD1dD	‹]Ê%Y£ë¥Ğ&0T4Ÿ|©ÙE1>in"ÿÉIlNIî§h£|kO ÆW03P	,Â±ß6f=d0?8L“7@Š":S Sr¥ÂÔºôºZË÷Œd?
öä Q±áægğ¸İ764~3y Ê<{Q¶+j…ü”,“Ü/t 5ı}±<&[j›Ï •¾„ib3WÙeNªXäeÓqìGMèDS!Rj/!sª
İÈİìI‰¸T¨YŒT$Ë6+×óÕ—BDÒVíŞm³¬MV5Ş{ƒ· š¦Ø°Ò°&>tI\k(Õt§ªqÁ×äÕõË×7+©Ê.A5NÄÑzbx4<æºÜJƒ¯ê·\òWÜ »	@¸Ó¨v4®ÓG×ú:‡©W³ÔRnÃ_åsuä)ô
.í#ĞÉ\¿Çc÷€ğ»'%ãªâé°¬ÄÖ€¬«vm“¯dÕG…Ùiêög Ğª®®
V³ëK<ÃÚ¯ğôQnÖS­QT‚ì„¬İ`|>˜á…ÙòÊ×­Uö-p«‡p‘ZáïÂDˆÅ.7ì /i&âNBÊ‚#ªç>Æo…¨œkùykÜ|¼ÉÏÍ°ƒP.ª¥õcÀbƒÓê–_X…™ëÙ1yO‰>nÔWÕ~;"istÿÍx˜©ÔMkşÑŸ9A¸Ï'ÄŒº[`ŞA'kyÙ1[mA5[h³¥şivÅDìø‘x§)(è ­ñNzWùÕH×2¥³¬1GşÀf&RWöÀud¬U½3Î€µAÂTÇ–l=ú¸™÷<W ®¶¦.1—”ÉäÄ½-RÔÎawòO­°:
tC[K*Mu*á÷üÍÿLğ ­²àÑ5vÄÃêoØ	Œ?Ô;	êÜ—Ò¥ÎA_;êe1]=G´¨\´±óOÏü°N)–ÏÔş'ÍSëOûÿ}í_Ñ £-iKÉñsí[ÖÈQgW|;šX hbe¢9Oì×D­]^/S–5êä…Gˆ¨'¹vkÌQ¦HñˆE*Lj\E¦RlÔ“LˆÜØ‚ÿ:9'yLO“?f#Ğ2'ØD¹Z%#ÁòM.xAxÀ:*9'ÑÖojGqóhº»Úd;öxXÇ“,6Ø`c™Âü`¶@=#kr„WU <QB¿VAvt]Mq öR¤lGØ‘şßôSyœ.‰'Låà›VÒ[ô…\F¯KÍÜC c€å+X¥1ğ†2\ôğµ:‰ä¬ÃyêhÇŠ–kUg‡')DMgş\A88çûœ*Wl[„exn4F$$Ji)[¨5uüµw	ï0òeb"-¢W±°ñ&Ù@ğÈ	Ø:.beX>S:B†a4ÁiC‹øÙY¿lIßptJjõh<óf­y[±cpO.<˜UP•¾Zu6,h.ZÏOëafBXïµe	¸ã[·ÀS„óS'¸ÑùÏ8y:T­4ú)`éIJÍ]37u,%h|P_ˆ3Xt6X+Ò
1,ªN=u
‚˜¿HRvĞœ—b|ß[{QpG­TK—ğQ25±Z[ÀC;^H*P,eqÖNï45âãq²£èiøó=LP€[bš|‘—¹Ñ÷‰¸Ïµd–«ƒÏÀxÒµ(Ê(¿ZıTšÇ ıBW,Ôfa·‚?ºÖƒk’éÕµ˜ª—U¶­÷è¡Ì9@èF[L˜nR	zvB¦ŠhKìeGÖ¶‡;ífé“§VDc™ á¼O;OTá‚éšVµÒ¶‘„-vg¿sS>(.7Û¦:ú>3±ù6tş@ıF)ö“©×†~Æ|‹ç@¬«{GZz½ä,6Ê­F€
œF Õ4a8v1=AÙ#êxOÏµ5ª5	?B^2À>#{©8@/úUi2×€1M	è!µÊ»;rFBğp˜j´:ÉQ;	Ó­BÑs*MZˆŒá©'å¢àÖ]¤æ t=m6L 1ö{"~ä0_) 2¹ •‚.4arch
  measured in seconds on a GPU once one encrypted command had been captured;
  it is now about a hundred thousand times more expensive per guess, for 80 ms
  paid once at pairing time.
* `/login` is **rate limited** â€” six wrong keys and the address waits five
  minutes. There was no limit at all before.
* **Tokens expire.** One issued once used to work until the process ended.
* **"Revoke all devices" now ends the live sessions** it always claimed to. It
  cleared the remembered devices and left every session those devices had
  already opened working, which is the one case anybody presses it for.
* When HTTPS *is* switched on, commands are **AES-256-GCM**, not AES-CBC. CBC
  concealed a message and did nothing to stop one being changed; an attacker on
  the same network could flip bits and the assistant would act on whatever fell
  out. Over plain HTTP there is no `crypto.subtle` and so no encryption at all â€”
  the page says `NO ENC` on its own badge rather than pretending otherwise.

**And Windows was blocking it, per executable, invisibly.** This produced the
strangest report of the release: the dashboard worked when JARVIS was started
from an editor and did not work when started from its own desktop shortcut â€”
same machine, same network, same code.

The shortcut targets `pythonw.exe`, so no console window appears. An editor runs
`python.exe`. Windows Firewall rules are **per executable**, so allowing one says
nothing about the other. Worse, dismissing the "Allow access?" prompt â€” easy to
do when it appears unannounced â€” makes Windows write a **block** rule, and a
block overrides every allow rule there is, including the port rule this app
creates for itself. Measured on the machine where it went wrong: `pythonw.exe`
was blocked on the Private profile, `python.exe` only on Public, and the network
was Private. That is the entire difference between the two launch methods.

Both interpreters are allowed now, any block rule against either is found and
removed under one prompt that says what it is for, and the result is **checked
afterwards** rather than assumed. When the prompt is declined, the QR panel says
so on screen â€” the person scanning the code is looking at the HUD, not at a
terminal.

### âš¡ Nothing heavy is loaded for a feature you did not use

`pyautogui` is 394 ms and OpenCV is 224 ms, and both were paid at **every** launch by the folder scan that discovers actions and plugins â€” whether or not anyone asked for a keystroke or pointed a webcam at anything.

They are imported on first use now, across twelve files, and not one of the call sites changed: `computer_settings.py` alone has eighty-six `pyautogui.` calls and every one still reads the way it did.

| | before | after |
|---|---|---|
| discovering actions + plugins | 462 ms | **216 ms** |
| `pyautogui` / `cv2` / `pyperclip` at startup | loaded | **never** |

> The cost turned out to be a hot potato rather than a line item. Deferring it in `actions/` moved the whole 394 ms to `plugins/`, because whichever file imports first pays for everybody â€” a deferral is only a deferral when it is unanimous.

### ğŸ§® The same tools, in a third fewer characters, for a small model

The fat tool descriptions are fat on purpose: `whatsapp_guard` spends three thousand characters spelling out which phrasings mean which action, and that is what makes the model get it right. But the model that needs those three thousand characters is not the model that cannot afford them.

A declaration may now carry both â€” `description` for a model with room, and `brief` for one without â€” and the short form is used only when an engine has asked for a tool budget. **Gemini receives the full text, byte for byte.**

| | tools | characters |
|---|---|---|
| Gemini | 38 | 54,757 |
| a local model, same 38 tools | 38 | **37,230** |
| a local model on a tight budget | 12 | 11,615 |

Nothing is removed to get there. And `tier` â€” the per-file override that decides what survives a tight budget â€” was documented but never wired through the loader, so it had never once been read. It is connected now, which is why `send_message` and `file_processor` stop being cut.

### ğŸ©¹ Fixes


* **`open_app` was a command injection.** `shutil.which(name.split(".")[0])` accepted `"notepad.exe & whoami"` because `which("notepad")` succeeds, and the whole string then went to a shell unquoted. Verified before it was changed; there is no shell on any launch path now.
* **`desktop_control` asked a model to write Python and ran it.** The rules â€” "NO subprocess", "NO file deletion", "NO imports" â€” were sentences in a *prompt*, with nothing enforcing them, while the namespace handed the generated code `getattr`, the real `pathlib.Path`, `pyautogui` and `ctypes`. From inside it, `subprocess.Popen` was one line away. It was also the only tool in the project that broke the project's own architecture: every other one declares typed parameters and lets the model fill them in. Removed â€” and nothing was lost, because typing and clicking is `computer_control`, multi-step screen work is `screen_agent`, and files are `file_controller`.
* **The screen agent crashed on every machine without Pillow.** `import mss.tools` inside a function made `mss` local to that whole function, so a line five above it read a local that had not been assigned yet: *"cannot access local variable 'mss'"*. It only fired on the branch Pillow's absence selected, which is why it looked intermittent.
* **The voice changed accent at random.** Whisper reports a language for every utterance and is confident about all of them, including "ok", "hmm" and "thanks" â€” and the voice followed. `language_probability` was on the same object and was being thrown away. A switch now needs both confidence and enough words; a one-word reply keeps the language it was already speaking.
* **Chrome opened twice, on a profile with none of your sign-ins.** Asking to open a web page called `open_app` for the browser and `browser_control` after it. Both descriptions now say the second one opens the browser itself.
* **A locked Chrome profile cost 25 seconds of silence.** A profile can only be opened once, so with the browser already running the launch sat on its timeout before falling back to a profile the user was signed into nothing on â€” and said nothing about it. Whether the browser is running is a question the process table answers in 150 ms, and the answer is now reported.
* **A process whose executable path could not be read was not recognised as the assistant's own.** Self-protection compared full paths, and a path comes back empty for a process that is exiting or that the OS will not inspect â€” so a `python.exe` belonging to this very application could become a candidate for closing. The name is compared when the path cannot be, and a process that vanishes before it can be touched is no longer reported as one this tool closed.
* Search results and file contents were shown to the user with their untrusted markers still attached. Those markers are for the model.
* The activity log filled with tool status lines. It carries the conversation and problems; the running commentary belongs in the terminal.
* `computer_settings` said `Done: <action>` whether or not anything had changed. Volume, brightness and dark mode are read back now; a keystroke sent to a window the user is looking at reports what it did rather than what it achieved.
* The `model` field was declared as free text, so the **LIST button had nothing to fill in** â€” it looked like a button that did nothing.
* Changing one pipeline slot **wiped what had just been typed** into the provider above it.
* A tool result whose call had been trimmed out of the history is an orphan several servers reject outright â€” and one a model reads as something the user said. The history window never cuts through an exchange.
* A model that emits two tool calls in one turn is not asked again until **both** have answers; the second result would otherwise arrive with no call to attach to.
* A generation that fails still ends the turn. Without that the interface sits in THINKING for ever and the stall watchdog reconnects an“æGˆò¯ÆĞçŞ¯~%BrÑÖCÔQ­¹:”w‚è{•û³ıaßZùveÌŒúpR®Øi”²±s~Üç>M`·¨Ÿ”êÃºö:‘Îj´èÃnã)<VƒLEçè¨š ›Œ?{‚Æaõe ¾\÷¿¢—·²h³I­ïû-P€–b.@¶2Ú ™Ë€õIçD9¯`9]š«G’úÿ">' Î,
¯fqM R[)n@Iü*Ybõ/ OÅ>QÕf]ÆÀÛÅYZÒêoP†ÜP‰´ZÍ‰Ğ]l1û`b%NíjXë8¤w5zÉ%±Ã%W|í|çãŠ ıZíN±sñ'Áx±†À>ğ9ÁgX8V?6‚C‘¯ÜÈÉW7òñaãå.^X]ôÉ#sWù „_;iÉËã•IB°%}c‡ËËw%µÒ¾˜ÅâÁå=ÃCŠSó#õmS3Ot¹@—×£¹,¶øx²ğ[ÂœI¸ğUWâËşNBš„¨¦Iôåbï[R±†¬×uŒKˆ4»¥gi_Ê®Z[Ÿåf^h]àÉ,3SÉ£Ğ^Ä)Uù,ß÷š(ƒrTçª}vc£ËÔ7.É¶¼3„]±•çX)T–úÁ±»¹–èã©ºì}}E„=?–£6èĞmOóŞGØÛ°Ù˜ïè‰9cìÎ$4)ˆÔí‡¸*às¥­©&Î×äêSúN`SåZ^îy GP®â:î‹aî{‘I.vuL¥ÙÁ}U"º?Úñ)ÚT;M– $’ö@¢ÛœYw®øNãù.&{×¤ËÿrNU0Zš'u Ñ
û”^Es"»iÆl—Z+ÙxâÂûN	”4*"WKríÙ8ZL«¡kfË$ğŸc%NnpIjFkaRö{!ûIEÑ ÁrReMŒ€˜eNG±PKva†–§›rù‰/n7FBŒÁDRÜí>)7Ó‘(c0Ùp?jqCYàüoR17ÖV7T”sšgîI³å\+K ı s}PinÂaÉzAa$vkR{CQĞ±;ĞtÑ@É63Y%^ş6\(÷y˜3ì2¢¹*XÖ\œìŞFI¹x@¹¸`€;®GbB%—iãƒíÆ@õeC¿4TQQÂzö»õéTÓÕß¡2z¹V0{ãÆ×¥wkTpõuf‚ŸM½6*>KGğfšxJOĞP;‘tù#gW…8=6Gè>Rÿil(ø\‡®'ş_¢ÑÙ…^J¤‚³3Yxr1>$PéÈHY×w9bdH>•Cßµı±ìO*Ìcá­Âv.¿{§C;w,´àTm:?Uêpúê@Wx†30±Å½R{esn”›F>ñä^Áa"7sH7%œ–uäÄ  $uZU?rDIì(7	Šà=Gä|.1ÔÌNë17E_3RíoöfŞ}ñ´c¼C¨6´{Q±°	ŠÙír•/¤7N²Ù4(S3É|.–ÇhĞrÚÿÔõQİS$5cF—7–‡'âPQGª3WÀ}Äb†j{i« -ŠpY×0Õ+UIÔC;ûinå±\&”f>ö–˜¡6S™ b@9WüOtL_ç@yG'NÀaÓñšŠ°-ÙãICınXfQ¡	(uúÊw>ÜÇC7›&±L”¶|È.’•mewxÀ9G;'NÏ!×Á™Z‡upméS]×ò!œRböÜb4(únw%œL30o0eeq%¾4M^Í‰+c‡xk¢e!C€)w73Œ5fÍ¸
 MÕËL~v¹,ùö·"XŞç,cG¾hUthQ	Il©Ğvd7U“Ç<}‘¶´æ€w s1AåiŒdE”ŸB£JÎHß]íİ`X:~\iƒ¹{y	>Œ***ÑSµpfï%ÉqV´ eí(}Bqæî«b-#PG8—­·w½­ÄYş»rWú¯uk=Êë@W+nÅ#.‘d}Õ$ç*ÃŸÛ0©/ôj9¬&¾Osb¯dùoë¾Ö:UøJæZËi³hïW"ƒèT¥ŒºôMÂ€ Ï ¦cğ1Ó=¨Rªşªƒ¦æ°'ZÈqûZq'›Cazãm£
aªVŒ©ßb\u÷=Oäz‘,QÕDN±%À»Úëét?ôyÒáÉËAT(849²XdY¡qG}¸ª9ÊV:_A¼MĞ{K8èÚ]wÖsP3]¿A ½|`(øÔV-[™’¿n$onïõEJÛEQâ»C8Îë^Ds/!N¼9{9THL\	Ÿ§|4˜?â,Ø Ÿá¹r*½-JWo©ë`+Ü¢Ô1Õ¹¡arCú(	5¢AÔQmÁ î±ö#\<C†m$d»Ié93ZMj‹J_f±*>‡¢sRrÔppJñ´İ0Y£(33keIt/-W>·jº.˜¬r*zºt/a†g$4Ô*Wç4Aoaå(F)FU›*¨K}"â`xâÙçH [~èjE*Æ	h‘m@é­àúÃÿ»…êç½®É¸äo¿Ø'~Z\”ˆ ’)×ob|^ïPš÷%¯F¤|}%Â–®+R[šp%8—ù`'}WşôdJ4juuî9â Ì:‘HH¶6è¢z®Ç4æ ™›4íJ|M¢Ä7}(VĞPÀVózH ;´&¹æ~.åÉ†IˆkÒ¿CBïnv)¿ZBŸI,„`×Ü	ıNu£4ÖF¤´æV°qÅª=AÆî<Ü›:æì.ii@X¼áÿaõeaî%f`¾Í®ºÎvbW-Æ™ wì’š	#’Î>{a™wõM¤KLV=ÍÎwA5œ@5|\o|Y_%'7×|i 6S9`N0Ş	,ÒH¹ßñ7µ¬ğ õ¢-(ãIÇÎ`we.ÉÑE{¸mn!G×;L'1×KCuŸ•æñä¶N¯pÎ€ldŸv\’n‰ÒÔpÕŸY5K-´l9ƒ¬3(i2íØ2v…5D\}ÅmXcT©Zó„$âµ›YY#d«Gp°9 ¦×^Viğ:&+>Üa× uÉ2<6ilS`Ö/Õƒ!j¶Êƒ~¡ÄuzçxK|Y~D=×	š4v#ÒN¹ÆŞ7ñ$Â`àR)/ 6èŠ$DÌË¶ÚE|øo^`s {5|=EÜÌ7-$SE“89Ú `$†_–ïJDƒ$²4Dmp¾^³iû ½§X<PRÑrNM¨YuÄB*¼à[,6Ë#y),³²p, ¯|D%AÆæÔ.Whm]AIJ0ª%Å˜"¤wE‘İÂE{P.Ã™²gf-A,áëW!k|B>lrÚ—w0Jæ3SSOX>7Mb>äxÿUSĞŒ&cGX(¯}:ï]ÓoS	ŞëKè 5L\{|V$¡cÖô<)#"p}­SÅLa	\Rì¹FT0Q®ZaJRt,	³8<oíŞgáÉ…EDø}Ş-Sxõheô<%¿©şà.:
U€$0@6çRB	¦UOõrZAŒAk1¿Â-œ,"ÊÌIÅzm¯qUÎª4W5ebUçmT ä]Ë9#fN.\HnCòËƒ
P?8>üî6}@b½4MZf<aŸTätbÄÙ¹?/]^Wj‘QBNTm{ß' *•k›8Ú0ÅêcuoúùŠ3iS ,"óEo0!+•œd:L8{n/§8OBCQ·T&Q¨PpkXÁMæM»İ6z
qd>‘u9~+*}D378År_:ÜÏ”0Ärd§R5J>Ljóò(N#W×)Ê+h}¹-…Oø=*”<•˜	1œY<Eè=Û( l<@X€Ï9­]( e*Ro°yqn{Khe!ü1øõ<wÑ½i’ :Î&[ìYâòA2p)×<}+;˜ò»ŠfşÑrø(É2€¢l&ÉÒ ‚dÊ­ ´aÏ_İcc/+jOŸ¸<`%İUÎ(crW2º]¶"ñú>?V©q+}¤-ñ dÎt0ŒrRlDUDvH<paH[yáAß$mUº¨D²ç†½
ô$½’…şO•íByhXÜÔ‚ÒÅäà”,‹Ã‚·–?W(	]4G¿R¶Mv1”A!§O82 .L+İZú!Êlt7=sÅ<j:‘¨Úå†¨o‰`¹Œ3”qB4xnºzp9"âi‚¾C”>a,8ihFQ^õŒdŸ1mAô	“_VJº`>}-ù%T[]0rŒ,gh:Ys<%wt+0+aQ?k#u+\ÓNuqÄ>š„H¼/¨e‡d÷½7]D"9U›-}Åj5X¾CHæñ‚›ÖKX'Ø9E›Fe-|LÂw*j¨‡»)‰*ÅEH6BOH»ã*²m‘`çÅ.ßK”hfQ5˜¼ÆL+hÌÕïY|Í!ÓHÿUèP{rôRpñ³Î"ãñŒgß#l:W	;ÓJä8ŞëcıMŒ^(|VA$X­%Ùp<˜8DééÈ>!ğ^´šTåH#ÆNÅ#ßJ¿»GÈOb—t¨2gEPJG…6n}AÅõ$Í1«‚ s%RRDE$ú`9.â)®BßÿÏTq—s)ı\zyÜŠZD¡ÚŒp•(­G$ÔÆ J•|¢…´ÔûÀ'xÌıq*"(°gL<ckš ,p¿G¾eä~E7lA'FÈ	Z±S1Şn‘˜OĞnyÓK.tgtNJ_ÚV^2g1‚B6U{yTk7õüZ‡UgÅú`„wUhh9ÙmJöw1N×Ö—jMÏŠA>‰?·INDp>/xdõgØN²`*Ít3PÜ'áljÈaëN?ÖÓ
¸2|B¶:UA¤üLépm~rThÄ´–b÷PÉiV«s4èSÊHan7„¼%2û-5ÔëSÚ'”Ö·1Ùøåªç”Yy‘; +c—iQÎà‚q©F^p‰ğ¿Ÿ'ñW@;{½ã‚Q‘&Èóšêbc—s¡IFGhe‰JH4`îáßî-SgÕj oz:Ëq7½^}ùÈm÷´K(iî­b{Yˆë*V]X\ ibP3óù{+ğ$<b=Bg|ARgˆ6pi¤{İ£¤<­$aM7=­rD-Q}Eé}xfüjŞq(OĞ4lü9äÈi±‹îHE:-IR{CJ0Xy­…ÒÏ¶Çà'ai>;L…
#9[rç³3=ñw(kgAE‘Jáh~nã\Bh‹šGŒ6=qYND.<°ñâè-i2b^Ún®ÅEQjOôt´ÿŠ`Ş Öì‡M¡,uÂq¡	VæAe B"~ˆzÉ
zyùm.SusHLa’Ç9Ó„¨
­H óxbé—Ø×x­Xut3¾˜^K¡úç]º²µù¼“ÈÚô|"{g*
aİgµ^ò×)É¹ùa»¸†“q}ıZ>ûÃÕÑÃÊh_Ì˜ìbC}(,1¼Í¼J¯O7œÙÅK#CoVÉ$yRC^>î¦±Õ˜©é\c*ª¼éN|ôŞ‰D±Jü•!€x¹íí@.½×ßèÏqı>ãwlüH­gÉH(#$5Œp
ˆ¬uk’Æ¾…ßµgw¢&ÚŞ!ÍzuZ¯õ¨ódÛfÄtcmÇe¢&(J{­¡q-c^&ä$¶õšij½9D{(õ-›‹Õ×Î!ÔDJî,¶•8{‹nÈMOx+</Zr»U¸îÂ©KlÖ‚W ÏÌªü®­ëZ “]{ŒJ¶aCt§˜:"¦Íæ³IÖ7SF’ÓôPXbŠ¢	¹öùW2Û9ƒ7ûy
yÖ-4ã~´G#,v±M§£ÏP«w#ğæ„‚ŞéÄ˜êâm)T1ÚM–šòéš˜['•Úß‰ü–c<LËZ^†”íóh8AşçgeÆ AM§ ¬í¡ÇÚäB—§—2DµLûtšªÄ
…Ø=ªš«|tpa
¨b$.sF*aá•ç]¦ÖÖu1P}/·Éª@€r ¤û|•XgØŠc/çH“{ÂX\%'k1Ô0TÅÏv„#FC]xuF.˜sòåjg¤YmW3Ñ*œŸ©aşô–~æj8'\ 	ï'ÕW  0º‡)P.éì%øÁ;”9‚ uà
` úLg1Î*ÊôN9PDW, +ê×q+bG³ÏI\*Voôú‹Of%a3ß—h+D%J\cY9=†¨O³l9¥Õ#Bğ'OS%<e7à)övôú¹}TùE?Ànyâ‹SÑ9g]ñvîã&F°»4´#‰	r¿(XXF’µLg,#{|¨~€–R
e}^G ÅZCqXËêİÙµ6¾QP*mH3hš„âãÎí´9p8ÿi…Ê®ÿ;¦/1´î¤d|‰­úBzIİµş¼AÏF_-+{tù24Ía(†Õp•î¹ Ş±_TIH9é÷$Éñ„Ow4vP¨àKÕˆw!@$;R­ŞvQWà¿ƒ_ò
!â=o‰VY‚++öpV®PÊõPrn»^¼´'80ûÔ„—†ºÛóO¥8R[p  q‘åÒ}zğŞv<~+´9oè‘Ó|/Èó†Ïtx+â*dV¯g%ä’Kêã/YN²­qïc*•4fÉÉŸxiœ˜âÕÿ)4šO‘AJhSYmƒ3+csÅ­”@Ã?¦¢u“"ÇÖø×‚uêÈZïVä9)6ïpgmÔÔN*UT AvBYKO‘LÖ¢sçêZE­¿‘ùk7Ã¦ºN£ÀözOƒ³u…7…B÷\n¾¬(v;Z˜2Ô6TN‰ŠPìs÷×bawƒŞ[¥4HÖY°X‘Ók(ã>¼ÿEá|b(©êªx\{Tx¥®Ó;»o8%ì8F‹#*cé±¾BBU)Ek•7•kÓ)!.’JÁ;Yc>7ßãF‰l2bWPsT"á¨nBÇl)f[/jxº—”TZ9Cè²u¿Î„
5mDÌy‹Õ•E‰Ù)°—¶©ã½e™ŒÈ)¾™Ö…—Âì L~ë~±VNZjZfcĞœ 2i:>™FN³YM:“ø¨i>	&3M2A™Xm<Ú¥€piµoI:=ìo»ŞÀ´çQSÆ ®v%	KLaÙT48Û,92¸PX3P|¼ƒ%‚+fK3:½ÔSS5z1¿_9Æ±=û0=b–õ\u.æ=lÉW«o+E0Ã^‡TÎö#áÿaáÂG;ûÓÄ	³2:¬^Õÿ=LY’QÂµ¯wF÷sx“ü’°[†?ú*vy>-6mÜC¶s<r}I¨q(.Iî9¤WQf0æ×½'™Ê&aİ\o3¬v£zhhçMUA½õç"fDd=feT\ìÛ3äÀ¹54–Å‹]KL-Ò6ól" ;ë9 F/ÄÓÌÖ½ëÚäèhîK.²1nb‹Ezí$¹åE8±ìƒX•¿DQC&­A“§bAÇ${xô7hÁø²¥ìÖªxƒ)B]zrjfªjÎEnªÂÓÌshÿ07ç´t€ò`		#I5Š,I:ùhlz„ ´9‡quõ£3n#™@á»kğÄZ§ZmÙèúU‘F@>ê{w”•-‘*9+wY('8öî}¢Fö	BÃ^òÃÒ[KÀÄ#0Î­¤^,X5,p+³h
g†Aé9­×{f'qG*¼3ì;Şu¦PÉ~è×ÛêşHaDõ){e­|2;Ú¨GQ< E>G5oĞ§WÙ=E6Fs 4O9XÏ4Z~uT!VM
MÀ{«MXzÍ|LöŒvÆqvŒ“BÙ¦l-Nÿ­C¶ê? xê J@¬­3.ˆRRJn5ÒaˆÜSZÙj•XI¿òŞ‘±ã¹ê%osÚBïFzÕ#˜’¡N;ÿ‰é£®^˜şw.¨0£zwî2òbf+Xèoúi…oñÉ‚:hG‰½Ÿê76&cmWEHTè7iv)m•,-mXm/e|°¼ZWÕØW‘
Ãpî&òmPYÙœ»ûÅ"¯âÒ.’'¨'éc>êFo[jÜWN8S’:fØIY± ×E^Vš;‹(úĞM°èZÀ6$Hì3áŒNæ¦Ì–¹è#5/c/JKN‡Wõoş«4(!¹xuiLMV^u1$)é;®haÀFüo/5ò`v*øh—zKvQCz=êF(ec?#sœTJh×FhUZhíiM	~MÖ
”Ì5%õŞgƒ÷([pUiPp†ZNyQåYì<¡-K¦ÂA?$Yøm;=Fz3!®ˆ¼áêƒ0"riF+2WN~/ırÏ)Ip8É&hå=o3¹Av´!94¬(QrÙy›}öî4+cŸ!hŸåãèŠEìúîÆl·OrÔBJ¿;mıƒŒ•›ØØXd­>	uÀ²ßGtN|FÄ‰½òØfÓu¾pÚâï^zß£Ÿ£Ö:U˜öÉƒ¶TÙU´1›‰…ªî
òp[&øíWùÛºQ–ºúÊ$ $E\ù@ ¯óE€ó¾ºNGëeÍa;Ã£¿dŒ™1…îQx@şáŒ^+e8–Oç¶dÓÉÚ÷–ä °EÜ.îº¤n¾PÉIÏGÔ¬ ÀìÎ²>ıZoŠ¼î_Qôµ‚Kw¹¾óş®ú¯‚1‡ÒLø—hœÆ®)ù¶ß¾èmm§ÙXÅ0ê‘O²Ëˆ£¸
 ©5®Ôñ-26'ÃæëÄ$_M6Ş¬®ya×ûã­,ßù$à\³<Ì.ó0XõhÆXµÿ÷¹F&íPã‰™,Ä@¯Òh~†Qñ2¯Yªuœšö¿•NAQRú\­›zfä740yÙ Ê:5LİL\õoxŸ”p„MQåve»—:Ïé&ZæDQ.×fy[¿Jc	GP&}5#âIa‹å+©˜_ÅX”À*¸Åç{€œªXcãĞLœ«VBJ/öLÊ@Gúuz3LÇ¨.ÄÒ¸A¤ĞÉóYY”¦MıÔ®}ëš†ƒ?¶æëéD°Ñ+Ö&ÛšEÜ+ºà™€àÆ=„›ö4¸Ò@ÉŒl«óT‹]œªâ¿šEaQ¯]SÛ:`Vğ#3}=ı2SÄŠL­Lxõ|8œæwu'Ïò!•ZA ÌÊA¸Š@ò‹+Q—v½uOº… vL„rÂJs0ŞÑğA³VãÊ[İB;æY5ÿ—‘P‘…Fëøáw¬¤ ‡jv`z}û[NPXJt\*À1]JR,<äSL¦ğ’Yúü+|K52]l<íGr	Xs-&3¯E6‹µ#`£ZmgWÄUŸifÅĞO¾	Q^]fşo+Yš2vÂà9=1=(êEyvbXV
áBCß€HiX†?¶¿ŒÀqíŞsMû»nÉ¿…N>…CÕ_¼š¶Ê5- uÅĞuô:$.6‹yQ^x&±P|6ÃTÛÑÆ àcØü&û(cHç°Zw73 pï#,6?+	·[](@acQ	`Ê6(«BaèÂÆ[¼NafUmZ‚Ôq%*2C8T~bqz:v'!{·¡ñCAm•«A¢S+÷=ı8RB4EIìÜEİ8IX˜gVJ¥-hIºŒ=N}H>dãuTv,˜3?—w	f¡ı$\LÕ*MLmjÖŞ|'TîGs-³­¥7Ó	 <ÓeáQF·~àî£6ªAL[^´=m–Œg¹¯JáLn5ñZZÉ”(ÚÜ-X Ó3¨%&{h
™‡u0½6%ˆë’syD¯4ïëŸÃE™æŠV¹8UÊ¦‹—¶Btñn€·â3¾P²y›.ÕƒÕÁ­ÕTbáß“ú9İ"m³w©è“i&	O‚Ñ¯ìĞ(T‚ág/r3J•KédŠ‡’ ¨¯ûşbk	İ™SJ2Aî…!ëJTÕ+A/ÄÈ¤$ö<¢ötár@€£E·ïhŠˆ¿7ö±U)U\ıênãÙK ÀR,Ÿ´E`qÊ M…ç§<hŠL3+ÅkG1 i5psˆ¦sş@N ı¢-ç—-¶Œ0B'ì°Ït½-3q`fm?(S›¿Bcs£‹RÈ/{‘«>dr[x:ğ2IrRB0v@åÿ{¤&õF™4!Od¾xÚ ™±6¬#ÿüwDAG S‹İÜZ	@KXEa<RaI<h#OT“óJNss but its author's. **Not everyone updates games; everyone opens applications.**

Mark LV trims it to **twelve**, and every one of them does the same kind of thing: drive this machine. Applications, the browser, files, the desktop, the screen, the clock, the weather, the display. The rule is written into the project tree, so the next skill lands in the right folder without anyone having to ask.

This is not only tidiness. Every bundled skill is declared to the model on **every** connection, whether you ever use it or not. The declarations sent at startup dropped from **16,827 characters to 12,907** â€” roughly a thousand tokens off every session, and five fewer wrong tools for the model to reach for.

**Nothing was deleted.** The five moved to `plugins/`, where they still ship and still work â€” a plugin is loaded the same way, gets the same HUD and the same undo, and can be removed by deleting one file. The rule the two folders now divide on is what a skill is FOR: `actions/` drives this computer, `plugins/` is everything else. That is why the game updater, the calorie counter and the pushup counter are still here, one directory across.

### ğŸ©¹ Fixes
* An unanswering model was retried on **every** call, at 12â€“15 seconds a time, because only quota and 404 failures were ever cooled down. 503/504 now rest for 30 minutes â€” **11.2 seconds saved per call**.
* One-shot Gemini calls had **no timeout anywhere**, in any of the sixteen files that made them. Every call now carries a deadline of at least 10 seconds.
* YouTube playback failed outright with *"Requested format is not available"* â€” it was asking for a combined stream that no longer exists.
* Videos played in a **random language**, because YouTube's auto-dubs carry the same bitrate as the original track.
* The settings drawer **stuttered on first open** â€” a 2.1-second `openwakeword` import on the UI thread, not the button count it looked like.
* The settings drawer opened **underneath the video**, because `QVideoWidget` creates a native window.
* JARVIS **answered the video's soundtrack.** The microphone now follows the video's sound.
* Qt's multimedia backend printed an ffmpeg banner to the console on every play, containing the **signed streaming URL with the viewer's IP address in it**. Silenced at startup.
* **Every launch paid 201 ms for a plugin nobody had asked to use.** Discovery executes every file in `plugins/`, and `youtube_video` imported `requests` and `youtube_transcript_api` at module scope. Deferring one of them would have saved nothing â€” the transcript library imports `requests` itself. Both are now checked with `find_spec`, which answers "is it installed?" without executing anything, and loaded on first use: **plugin discovery 211 ms â†’ 39 ms**.
* A plugin that needed a file from a **newer Mark** was rejected with *"pip install core"*. The loader could not tell this project's own packages from a third-party one, so it told people to install a same-named stranger from an index â€” wrong, and a supply-chain hazard dressed up as a fix. First-party names now say the app is behind the plugin and that there is nothing to install.

> Built on the Mark LIâ€“LV foundation: the **ğŸ§‘â€ğŸ¤ Holographic Avatar**, **ğŸ‘„ Lip-Sync**, **ğŸšï¸ Push-to-Talk**, **ğŸ”‡ Self-Echo Guard**, **ğŸ§© Plugin System**, **â™¾ï¸ Unlimited Sessions**, **ğŸ¨ Live Theming** and **ğŸ™ï¸ Wake Word** are all still here.

---

## ğŸ”„ The Foundation Update â€” in every Mark from LII

These four landed across **Mark LII, LIII, LIV and LV at the same time**, after each of those releases had already shipped. They are not what any one of those versions originally introduced; they are the floor all of them now stand on, so moving up a Mark never costs you something the one below it had.

No new dependencies. No bundled asset files. No hardcoded language, and nothing that assumes one operating system.

### ğŸ§  A memory that actually remembers

The store was capped at **2,200 characters â€” the whole memory, not per entry** â€” because all of it was pasted into the system prompt on every connect, so growing the memory grew every request. When it filled, the oldest entries were deleted and one line was printed to a console nobody reads. An assistant advertised as remembering "projects, preferences and personal context" was in practice a two-page notepad that quietly forgot your sister's name after a few weeks.

Storage and prompt budget are now separate problems:

* **Nothing is deleted.** The cap is a runaway guard normal use never approaches, and if it is ever hit it says so in the activity log instead of on stdout.
* **The prompt carries a core, not a dump.** Identity in full, then the most recently updated facts, budgeted â€” measured at **971 characters on a memory holding 62 stored facts.** That is *smaller* than the old whole-store cap, so sessions now connect with fewer tokens than before.
* **The rest is fetched on demand.** A `recall_memory` tool searches the full store locally â€” no network, no second model, well under a millisecond.

The part that is easy to get wrong: **a model cannot look something up if it doesn't know the thing exists.** So the prompt also carries an **index of the keys** it had no room for. Without that, "who is AyÅŸe?" gets "I don't know" while `ayse_sister` sits on disk unread. This index interleaves categories rather than sorting by recency â€” sorting like the core, a memory with forty preferences pushed the one entry the index existed for off the end.

âš™ â†’ **ğŸ§  MEMORY** shows every stored fact, when it was learned, and an âœ• to forget it. Everything stays in `memory/long_term.json` on your machine.

### â†©ï¸ Undo â€” it can take back what it did

JARVIS moves files, renames them, writes to them and changes your settings. None of that had a way back; if it misheard you, the only remedy was to fix it by hand.

Say **"undo"** â€” in any language â€” and it reverses its own last action:

| | |
|---|---|
| **Files** | move Â· rename Â· create Â· copy Â· write Â· delete Â· organize desktop |
| **Settings** | volume Â· brightness Â· dark mode |

Three things it deliberately does *not* do:

* **It does not guess.** Settings undo reads the current value *before* changing it. Where a platform won't report that value, nothing is registered â€” an undo that restores a guess is worse than no undo.
* **It does not hoard.** Undoing a write means keeping the old contents in memory, so files over 1 MB are excluded and it says so rather than holding a 200 MB log for the session.
* **It does not delete your files to undo a copy.** The reverse of a copy is removing the copy; the reverse of "create a folder" is removing it *only while it is still empty*.

`organize_desktop` gets special treatment â€” one command that moves dozens of files, which made it the least reversible thing the assistant could do. It journals every move and puts them all back in one go, cleaning up the folders it created if they're still empty.

**Undo costs nothing at runtime.** It appends a closure to a list; nothing in it runs unless you ask.

### âš ï¸ A confirmation the model can't forge

The old gate read like this:

```python
if action in _DANGEROUS_ACTIONS:            # {"restart", "shutdown"}
    confirmed = str(params.get("confirmed", "")).lower()
```

A **tool parameter, which means the model fills it in.** Nothing stopped it sending `confirmed=yes` on the first call and nothing checked that a human had been involved. It was a convention, not a gate. And its coverage was two actions â€” so `toggle_wifi`, which cuts the assistant's own connection to the Live API and therefore *cannot be asked to undo itself*, went through with no gate at all.

The token is now issued by the interface. Shutdown, restart and WiFi put a banner on the HUD and **return immediately**; the action runs only if you press CONFIRM. Nothing blocks â€” JARVIS keeps talking while the banner is up â€” so this is **cheaper** than the old gate, which burned two tool round trips for every power command.

> The split between the two mechanisms is about reversibility, not about how alarming a word sounds. Anything undoable is done at once; only the genuinely irreversible asks. An assistant that checks with you before turning the volume down is one nobody uses.

### ğŸ§ It finally asks which microphone

Both audio streams opened with no device argument at all, so they always took whatever the OS called "default" â€” and on Windows that **moves on its own** the moment you plug in a headset in. "JARVIS can't hear me" almost always meant "JARVIS is listening to the webcam".

âš™ â†’ **ğŸ§ AUDIO DEVICES** lets you pick the microphone and the speakers by name. Two things matter more than the dropdown:

**The list is short.** `query_devices()` returns one entry per *device Ã— host API*, not per device â€” measured on an ordinary Windows machine, **41 entries for what the sound settings show as 4 microphones and 4 speakers.** The same microphone appears four times, under MME, DirectSound, WASAPI and WDM-KS, with nothing to say which is which. This is not a choice, it's a quiz. The picker takes one host API per direction, drops the "Sound Mapper" and "Primary Sound Driver" pseudo-devices that just mean "default", and deduplicates. **41 â†’ 8.**

**Every entry has been measured, not assumed.** The obvious approach is to pick the host API with the nicest names â€” WASAPI on Windows, which in shared mode **doesn't resample**, so with 16 kB in and 24 kB out against 48 kB hardware every open failed. Adding a rate check and switching to DirectSound passes that test on both sides, and PortAudio's DirectSound **output is a silent sink**: the stream opens, every write returns success in ~0 ms, and not one sample reaches the speakers.

| | write(2.0 s) took | |
|---|---|---|
| MME | **2.02 s** | consumed in real time |
| DirectSound | **0.00 s** | swallowed instantly |

No capability flag reports this. So the app measures it â€” once per host API per direction, on a background thread at startup, using silence. Two consequences worth stating plainly:

**Each direction picks its own host API.** On Windows this lands on DirectSound for the microphone and MME for the speakers â€” a split no amount of reasoning would have produced.

**The probe runs in the mode the app actually ships.** DirectSound input passes a callback stream and fails a blocking read; probing the wrong mode rejected a microphone that works perfectly.

Your choice is stored **by name, not by index** â€” indices shift whenever something is plugged in. If the saved device is gone, it falls back to the system default and says so in the log rather than failing to start.

### ğŸ”— It stops forgetting the conversation when the connection drops

**Session resumption** was switched on in the config and the handle the server sent back was **never read** â€” so every reconnect started an empty session. A dropped packet, or simply changing the voice, wiped the conversation. "Unlimited sessions" leaked through exactly this hole.

The handle is captured and replayed now. A network blip, or switching your microphone, keeps the conversation intact.

It is held in memory only, deliberately: writing it to disk would make a fresh launch continue yesterday's chat, which sounds appealing but breaks the session-summary flow â€” a conversation that never ends never produces a summary, and "yesterday we talked aboutâ€¦" line in the morning briefing silently disappears. Changing the **voice** also starts clean on purpose, since resuming restores the server's session state and would likely bring the old voice back with it.

### ğŸ©¹ Fixes that came with it

* **The assistant could die on a log line.** Status lines carry emoji and arrows (`ğŸ“¤ file_controller â†’ Moved: a.txt â†’ Documents/`). On a non-UTF-8 console â€” cp1254 on a Turkish Windows, cp1251 on a Russian one, cp932 on a Japanese one â€” printing one raises `UnicodeEncodeError`, and because this print sits *after* the tool's own `try/except`, it escaped into the receive loop and took the session down.
* **Every computer command paid for two model round trips.** `computer_settings` made an **entire second Gemini call, inside the tool**, purely to translate the request into one of its own action names â€” because the declaration only said "The action to perform", so the model rarely filled it in. When that second call failed, the fallback was `description.lower().replace(" ", "_")`, which turns the Turkish for "turn it down" into "sesi_kis" and straight to "Unknown action". The declaration now names all 56 actions and the rest is spelling tolerance handled locally by `difflib` in microseconds. When nothing matches it suggests real action names instead of dead-ending.
* An unresolvable saved audio device, or one the driver refuses to open, falls back to the system default and says so â€” on both the microphone and the speakers.
* A rejected session-resumption handle is dropped after one attempt, so an expired handle can never be replayed on every retry and prevent the reconnect it exists to protect.



---

## ğŸ—ºï¸ Mark Roadmap

| Mark | Focus |
|---|---|
| **XLIX** | Auto-start Â· clipboard intelligence Â· assistant customization |
| **L** | Session memory Â· background monitoring Â· proactive 2.0 Â· instant vision |
| **LI** | Plugin system Â· affective dialog Â· proactive audio Â· unlimited sessions |
| **LII** | Voice picker Â· live theming Â· reactive HUD Â· recallable memory Â· undo Â· real confirmation Â· audio device picker Â· session continuity |
| **LIII** | Wake word Â· Gemini 3.1 Flash Live Â· instant acknowledgment Â· self-describing action/plugin architecture |
| **LIV** | Holographic avatar Â· viseme lip-sync Â· facial acting Â· face-as-status Â· push-to-talk Â· self-echo guard Â· runtime self-knowledge & limits |
| **LV** | Video on the HUD Â· model ladder with measured fallback Â· split settings drawers Â· trimmed bundled skill list |
| **LVI** | Choose your engine Â· local & third-party models Â· Whisper + Piper in ~50 languages Â· language-following voice Â· ElevenLabs Â· tool budget for small models Â· verified outcomes instead of claimed ones Â· close an app by name Â· untrusted-content boundary Â· platform honesty on Wayland and macOS Â· hardened phone dashboard |
| *shared* | The last five above also shipped to LIII, LIV and LV at the same time â€” moving up a Mark never loses them |
| **LVII+** | Interrupt by voice Â· conversation history Â· full file access Â· security camera Â· Obsidian |

---

## âš¡ Quick Start

```bash
git clone https://github.com/FatihMakes/Mark-LVI.git
cd Mark-LVI
python setup.py        # installs deps for YOUR OS + the browser automation engine
python main.py
```

`setup.py` only ever installs what your operating system needs â€” the Windows-only libraries are skipped automatically on macOS and Linux, and vice-versa. It also checks your Python version up front, so a wrong interpreter fails with a sentence instead of a wall of pip output. Prefer to do it by hand? `pip install -r requirements.txt` works too.

> âš ï¸ **Installation Note:** If you hit a `ModuleNotFoundError` for an OS-specific package, install it with `pip install <module_name>`. The optional **wake word** engine is *not* installed here â€” grab it in one click from **âš™ â†’ WAKE WORD** inside the app.

---

## ğŸ“‹ Requirements

| Requirement | Details |
|---|---|
| **OS** | Windows 10/11, macOS, or Linux |
| **Linux display server** | Everything works on **X11**. On **Wayland** â€” the default on Ubuntu 22.04+, Fedora and current GNOME/KDE â€” the system does not permit any program to type, click, capture the screen or raise another window, so those features are unavailable and JARVIS says so at startup instead of pretending. Voice, memory, files, the web and opening applications are unaffected. Log out and pick an Xorg session to get the rest |
| **macOS permissions** | Accessibility (to type and click) and Screen Recording (to see the screen), both under System Settings â†’ Privacy & Security. Until granted, those actions silently do nothing â€” the OS reports success either way |
| **Python** | 3.11, 3.12 or 3.13 |
| **Microphone** | Required for voice interaction (and for the "Hey Jarvis" wake word) |
| **Speakers** | Required for voice replies |
| **API Key** | Free Gemini API key (entered on first launch â†’ `config/api_keys.json`). Only for the Gemini engine â€” a fully local setup needs no key and no account |
| **GPU** | **Not required, anywhere.** The avatar and HUD video are rendered in software; local speech recognition and the neural voice both run on the CPU by default |
| **YouTube on the HUD** | `yt-dlp`, installed by `setup.py`. Without it, local files and direct URLs still play and YouTube links open in the browser with an explanation |
| **Aviation Weather** | No API key or account required. The plugin uses the existing `requests` dependency and AviationWeather.gov's public API; an internet connection is required |
| **Wake word** *(optional)* | One-click download from âš™ â†’ WAKE WORD (`openwakeword`, a few MB, fully local) |
| **A different engine** *(optional)* | Nothing extra. âš™ â†’ ENGINE & PROVIDERS talks to any local or hosted model over HTTP using a library the app already has |
| **Local speech recognition** *(optional)* | `faster-whisper`, installed from the same panel. **CPU is the default** â€” a GPU is an option, never a requirement |
| **Local voice** *(optional)* | `piper-tts` for a neural voice in ~50 languages, one click from the panel â€” or nothing at all, and it uses the voices your OS already has |

---

## ğŸ—‚ï¸ Project Structure

```
Mark LVI/
â”œâ”€â”€ main.py                   # Core loop â€” Gemini Live session, audio I/O, viseme extraction, tool dispatch
â”œâ”€â”€ ui.py                     # PyQt6 HUD â€” avatar canvas, waveform, log panel, settings drawer, camera feed
â”œâ”€â”€ setup.py                  # OS-aware installer (skips wrong-OS dependencies, checks your Python)
â”œâ”€â”€ .gitignore                # Keeps your API key, TLS key and memories out of the repository
â”œâ”€â”€ providers/                # OPTIONAL â€” delete it and the assistant runs on Gemini,
â”‚                             #   exactly as it did before this folder existed.
â”‚                             #   Never imported unless a provider is configured.
â”‚   â”œâ”€â”€ base.py               # The contract: Engine / LLM / STT / TTS, caps, Live-shaped events
â”‚   â”œâ”€â”€ registry.py           # Discovery and construction â€” imports one module, on demand
â”‚   â”œâ”€â”€ schema.py             # Tool declarations: Gemini <-> OpenAI <-> Anthropic, and the budget
â”‚   â”œâ”€â”€ audio.py              # Rates and formats â€” 16 kHz in, 24 kHz out, everything between
â”‚   â”œâ”€â”€ llm_openai.py         # Every /v1/chat/completions endpoint: local servers and hosted APIs
â”‚   â”œâ”€â”€ stt_whisper.py        # Whisper on the CPU, or a transcription API
â”‚   â”œâ”€â”€ tts_piper.py          # Neural voice here, ~50 languages, follows the one you speak
â”‚   â”œâ”€â”€ tts_system.py         # Windows SAPI / macOS say / Linux espeak-ng â€” nothing to download
â”‚   â”œâ”€â”€ tts_elevenlabs.py     # One voice, every language, streamed
â”‚   â”œâ”€â”€ engine_pipeline.py    # STT -> LLM -> TTS, wearing the Live session's interface
â”‚   â”œâ”€â”€ _tests.py             # `python -m providers._tests` â€” no network, no key needed
â”‚   â””â”€â”€ voices/               # Piper voices, downloaded on demand (git-ignored)
â”œâ”€â”€ plugins/                  # OPTIONAL skills â€” delete any file and it is simply gone
â”‚   â”‚                         #   next launch. This is where anything that is NOT
â”‚   â”‚                         #   about driving the computer lives; see actions/.
â”‚   â”œâ”€â”€ _template.py          # Copy this to write a new skill â€” one file, drop in, done
â”‚   â”‚                         #   A file starting with _ is a shared driver, not a skill:
â”‚   â”‚                         #   the loader skips it, and the skills beside it import it.
â”‚   â”œâ”€â”€ aviation_weather.py   # Latest METAR/TAF for up to three ICAO stations via AviationWeather.gov
â”‚   â”œâ”€â”€ _whatsapp_core.py     # Shared WhatsApp driver â€” desktop app or Web, all three OSes
â”‚   â”œâ”€â”€ whatsapp_call.py      # Place and end WhatsApp voice / video calls
â”‚   â”œâ”€â”€ whatsapp_guard.py     # Answer, decline or auto-reply to INCOMING WhatsApp calls
â”‚   â”œâ”€â”€ telegram_remote.py    # Drive JARVIS from anywhere over Telegram
â”‚   â”œâ”€â”€ chat_takeover.py      # Reads an on-screen chat and replies in it
â”‚   â”œâ”€â”€ screen_agent.py       # Looks at the screen and works it, step by step
â”‚   â”œâ”€â”€ gmail_control.py      # Read, search, send and draft email
â”‚   â”œâ”€â”€ calendar_control.py   # Read and create calendar events
â”‚   â”œâ”€â”€ obsidian_vault.py     # Read and write notes in an Obsidian vault
â”‚   â”œâ”€â”€ document_review.py    # Review a document and report what should change
â”‚   â”œâ”€â”€ excel_writer.py       # Spreadsheet output
â”‚   â”œâ”€â”€ code_helper.py        # Write and run small programs
â”‚   â”œâ”€â”€ dev_agent.py          # Multi-file project work
â”‚   â”œâ”€â”€ image_generator.py    # Generate images
â”‚   â”œâ”€â”€ upload_video.py       # Upload the video on your Desktop to YouTube
â”‚   â”œâ”€â”€ youtube_video.py      # Search, summarise and fetch transcripts
â”‚   â”œâ”€â”€ printer_control.py    # 3D printers, over MQTT
â”‚   â”œâ”€â”€ home_assistant.py     # Smart-home devices
â”‚   â”œâ”€â”€ game_updater.py       # Update or install games through their launcher
â”‚   â”œâ”€â”€ flight_finder.py      # Flight search
â”‚   â”œâ”€â”€ shopping_list.py      # Shopping list
â”‚   â”œâ”€â”€ pomodoro.py           # Pomodoro timer
â”‚   â”œâ”€â”€ water_reminder.py     # Hydration reminders with intake tracking
â”‚   â”œâ”€â”€ quiz.py               # Spoken quizzes
â”‚   â”œâ”€â”€ spaced_repetition.py  # Flashcard review
â”‚   â”œâ”€â”€ calorie_counter.py    # Food through the webcam
â”‚   â””â”€â”€ pushup_counter.py     # Counts pushups through the webcam
â”œâ”€â”€ actions/                  # Bundled skills â€” each self-describes via a TOOL dict + handler
â”‚                             #   Everything here drives the COMPUTER, which is what decides
â”‚                             #   whether a new skill belongs in this folder at all.
â”‚   â”œâ”€â”€ web_search.py         # Gemini + DDG parallel search (news, research, price, compare)
â”‚   â”œâ”€â”€ screen_processor.py   # Screen & webcam capture for vision
â”‚   â”œâ”€â”€ background_monitor.py # User-configured topic watching â€” daily DDG check
â”‚   â”œâ”€â”€ proactive.py          # Proactive 2.0 â€” time/context/rotation-aware check-ins
â”‚   â”œâ”€â”€ reminder.py           # OS-native scheduled notifications
â”‚   â”œâ”€â”€ system_monitor.py     # CPU / RAM / GPU / temperature telemetry
â”‚   â”œâ”€â”€ computer_settings.py  # Volume, brightness, WiFi, power (per-OS)
â”‚   â”œâ”€â”€ computer_control.py   # Keyboard shortcuts, mouse, window management
â”‚   â”œâ”€â”€ open_app.py           # Application launcher (per-OS name map)
â”‚   â”œâ”€â”€ browser_control.py    # Web browser control
â”‚   â”œâ”€â”€ file_controller.py    # File system operations
â”‚   â”œâ”€â”€ file_processor.py     # Document reading and summarization
â”‚   â”œâ”€â”€ send_message.py       # Messaging integration
â”‚   â”œâ”€â”€ weather_report.py     # Live city weather data
â”‚   â”œâ”€â”€ video_player.py       # Plays video on the HUD, where the avatar normally is
â”‚   â””â”€â”€ desktop.py            # Desktop and taskbar control
â”œâ”€â”€ memory/
â”‚   â”œâ”€â”€ memory_manager.py     # Load/save long_term.json â€” sessions, monitors, identity
â”‚   â”œâ”€â”€ config_manager.py     # api_keys.json access â€” key, OS, name, voice, colour, toggles
â”‚   â””â”€â”€ long_term.json        # Persistent store â€” created on first run
â”œâ”€â”€ dashboard/                # Phone control â€” paired by QR code, one-time key
â”‚   â”œâ”€â”€ server.py             # FastAPI + uvicorn; HTTP by default, HTTPS opt-in
â”‚   â””â”€â”€ static/               # The phone page and its login screen
â”œâ”€â”€ core/
â”‚   â”œâ”€â”€ outcome.py            # What a tool tells the model: done / unverified / failed /
â”‚   â”‚                         #   ask / started, plus the untrusted-content wrapper
â”‚   â”œâ”€â”€ appidentity.py        # Which applications are running, which one the user named,
â”‚   â”‚                         #   and which processes are the assistant's own (never a target)
â”‚   â”œâ”€â”€ lazyimport.py         # Heavy third-party imports paid only if they are used
â”‚   â”œâ”€â”€ platform_support.py   # What THIS machine permits â€” Wayland, macOS permissions â€”
â”‚   â”‚                         #   reported to the user and to the model, never guessed at
â”‚   â”œâ”€â”€ gemini.py             # One place for every one-shot Gemini call â€” model ladder, timeouts,
â”‚   â”‚                         #   cooldowns, and the configured provider as one more rung
â”‚   â”œâ”€â”€ prompt.txt            # All prompt wording â€” {tokens} are filled from the live system at startup
â”‚   â”œâ”€â”€ avatar.py             # Avatar renderer â€” lighting, pose, expression, mouth (QPainter)
â”‚   â”œâ”€â”€ avatar_mesh.py        # Head geometry â€” loads the face, generates skull/neck/risers
â”‚   â”œâ”€â”€ face_model.obj        # The face itself (MediaPipe canonical model, Apache-2.0, 25 KB)
â”‚   â”œâ”€â”€ viseme.py             # Transcript â†’ mouth shapes, fused with the audio's timing
â”‚   â”œâ”€â”€ echo.py               # Tells your voice from the assistant's own echo; self-calibrating
â”‚   â”œâ”€â”€ hotkey.py             # Push-to-talk chord â€” global on Windows, windowed fallback elsewhere
â”‚   â”œâ”€â”€ undo.py               # One shared undo stack â€” actions register how to reverse themselves
â”‚   â”œâ”€â”€ confirm.py            # Irreversible-action gate â€” the token is issued by the UI, not the model
â”‚   â”œâ”€â”€ audio_devices.py      # Microphone / speaker list â€” filtered, measured, resolved by name
â”‚   â”œâ”€â”€ plugin_loader.py      # Plugin engine â€” discovery, validation, crash isolation
â”‚   â”œâ”€â”€ action_loader.py      # Bundled-action engine â€” the built-in twin of plugin_loader
â”‚   â””â”€â”€ wake_word.py          # Local "Hey Jarvis" detector â€” own thread, offline, opt-in
â””â”€â”€ config/
    â”œâ”€â”€ api_keys.json         # API key, name, voice, colour, toggles â€” created on first launch (git-ignored)
    â””â”€â”€ certs/                # Self-signed TLS pair for the phone dashboard â€” generated locally (git-ignored)
```

---

## ğŸ™ Third-Party Assets

| Asset | Source | Licence |
|---|---|---|
| `core/face_model.obj` | [MediaPipe](https://github.com/google-ai-edge/mediapipe) canonical face model â€” 468 vertices of measured human face geometry | Apache License 2.0 |
| Aviation weather reports | [AviationWeather.gov](https://aviationweather.gov/) public data API | Public data; no API key or account required |

---

## ğŸ”’ Your Data

Most data stays on your machine. There is no MARK server, no telemetry and no account. When the Aviation Weather plugin is used, the requested ICAO station codes are sent to AviationWeather.gov to retrieve the public reports; no credentials or API key are included.

| What | Where | Notes |
|---|---|---|
| Gemini API key, plugin and provider credentials | `config/api_keys.json` | **Plaintext.** Anyone with your user account can read it. Treat it like a password file. |
| Dashboard TLS certificate + private key | `config/certs/` | Generated locally, self-signed, never leaves the machine. |
| What the assistant remembers about you | `memory/long_term.json` | Delete the file to make it forget everything. |
| Requested aviation station codes | AviationWeather.gov | Sent only when the Aviation Weather plugin is used. No API key or account is required. |

All three local files are listed in `.gitignore`, so a fork or a pull request cannot leak them by accident. **If you have already committed `config/api_keys.json` anywhere public, revoke that key** at [aistudio.google.com](https://aistudio.google.com/app/apikey) and generate a new one â€” removing the file in a later commit does not remove it from the history.

Your voice is streamed to Google's Gemini Live API while a session is open; that is one of the few things that leaves your computer, and it stops when you mute or close the app. The Aviation Weather plugin makes a separate public-data request to AviationWeather.gov when you ask for METAR or TAF information.

**Mark LVI changes what that sentence can say about you.** Choose a local engine â€” Whisper on your CPU, a model served by Ollama or LM Studio, your system's own voice â€” and nothing leaves the machine at all: no audio, no transcript, no key, no account. Choose a hosted provider instead and your audio and text go to that vendor rather than to Google. The panel says which is which, and the assistant never quietly switches between them.

---

## âš ï¸ License

Personal and non-commercial use only.
Licensed under **[Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)**.

---

## ğŸ‘¤ Connect with the Creator

Engineered by a developer building a real-world JARVIS-style assistant.
â­ **Star the repository to support the journey to Mark 100.**

| Platform | Link |
|---|---|
| YouTube | [@FatihMakes](https://www.youtube.com/@FatihMakes) |
| Instagram | [@fatihmakes](https://www.instagram.com/fatihmakes) |
