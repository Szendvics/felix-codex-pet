# Felix for Codex

The classic desktop cat, with his original animations.

## Install

### Codex app

1. Run the [download command](#download-commands) for your system.
2. Open **Settings → Pets**, click **Refresh**, and select **Felix**.
3. Enter `/pet` to show him.

For the Windows app, use Windows PowerShell, even if you also use WSL.

For a manual install, [download the ZIP](https://github.com/Szendvics/felix-codex-pet/releases/latest/download/felix-codex-pet.zip),
extract it, and copy the **felix** folder to **Settings → Pets → Open folder**.

### Codex CLI

Run the [download command](#download-commands) where you run Codex. For a CLI
installed in WSL, run it inside WSL.

Start `codex`, then enter:

```text
/pets Felix
```

Terminal pets require iTerm2 3.6+ or a terminal with Kitty graphics or Sixel
support. They do not work inside tmux or Zellij.
[Official terminal pet guide](https://learn.chatgpt.com/docs/pets#choose-a-terminal-pet).

## Download commands

Run the same command to install or update Felix.

### Windows PowerShell

```powershell
$petHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
$url = 'https://github.com/Szendvics/felix-codex-pet/releases/latest/download/felix-codex-pet.zip'
Invoke-WebRequest -Uri $url -OutFile felix-codex-pet.zip -UseBasicParsing -ErrorAction Stop
Expand-Archive -LiteralPath .\felix-codex-pet.zip -DestinationPath (Join-Path $petHome 'pets') -Force
```

### macOS / Linux / WSL

Requires `curl` and `unzip`.

```sh
curl -fL https://github.com/Szendvics/felix-codex-pet/releases/latest/download/felix-codex-pet.zip -o felix-codex-pet.zip &&
unzip -o felix-codex-pet.zip -d "${CODEX_HOME:-$HOME/.codex}/pets"
```

## Animations

![Felix animation preview](preview.gif)

| App state | Felix's action |
| --- | --- |
| Idle / Needs input | Sitting, looking at you, moving his tail (325) |
| Drag right / left | Walking (303 / 302) |
| Wave | Raising a paw (325) |
| Jump | Leaving paw prints on the glass (319) |
| Failed | Sitting with his back turned, moving his tail (322) |
| Working | Eating from the bowl (311) |
| Review | Watching the fish bowl (315) |

[GIF selector](animations/README.md): all 29 sequences and numbered frames.

Codex controls when animations play. Idle uses the Needs input poses at a different
speed. Working repeats the same eating loop on every turn.

## Rebuild and check

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python build.py
```

Validates the spritesheet and creates `dist/felix-codex-pet.zip`, its SHA-256
checksum, and the previews. Edit `ROWS` in [build.py](build.py) to change the frames.
On Windows, use `python` to create the venv and `.venv\Scripts\python.exe` after that.

## Original Felix artwork

![Original Felix splash screen and logo (1200)](animations/fig_1200.gif)

[Sources and attribution](NOTICE.md)
