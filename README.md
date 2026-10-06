# Felix for Codex

The classic black-and-white desktop cat, repackaged as a Codex pet using his
original animation frames. All nine Codex states are included.

[Browse all 29 GIFs and choose the Codex state mapping](animations/README.md).
The gallery includes numbered source frames and a selection template in Hungarian.

![Felix animation preview](preview.gif)

## Install

Copy the `felix` directory into your Codex pets directory:

- Linux/macOS: `~/.codex/pets/felix/`
- Windows: `%USERPROFILE%\.codex\pets\felix\`
- Custom Codex home: `$CODEX_HOME/pets/felix/`

The destination must contain `pet.json` and `spritesheet.webp` directly.
In the desktop app, open **Settings → Pets → Refresh**, choose **Felix**, and
enter `/pet` to show him. Older versions place Pets under Appearance.

When using Windows with WSL, install in the home directory used by the app that
displays the pet. The Windows app and WSL CLI can have separate Codex homes.

## Animations

| Codex state | Felix's action |
| --- | --- |
| Idle | Same seated poses as Waiting for input (325), with Codex's idle timing |
| Drag right / left | Walking in the matching direction |
| Waving | Raising a paw |
| Jumping | Jumping and leaving paw prints on the glass (319) |
| Failed | Sitting with his back turned and moving his tail (322) |
| Waiting for input | Looking at you and moving his tail |
| Working | Eating from his bowl (311) |
| Review | Inspecting the fish bowl (315) |

This package uses the v1 atlas: 8 × 9 cells of 192 × 208 pixels, with transparent
unused cells. The app controls the pet's activity; the original desktop program's
window detection and roaming behavior are not part of the package.

Codex desktop 26.930.4958.0 uses one fixed six-frame Working row; custom pet
packages cannot choose a different Working animation on each turn.

## Rebuild and check

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python build.py
```

The build checks source checksums, frame bounds, and animation variation, then
runs OpenAI's atlas validator. It also writes `qa/contact-sheet.png`,
`qa/validation.json`, and `preview.gif` for visual inspection. On Windows, use
`.venv\Scripts\python.exe` instead.

Frame choices and timing are in `build.py`. Every pose uses the same scale;
positions preserve each source sheet's baseline. Walking directions were checked
against the actual frames because the archive labels them in reverse.

Contributor: **Marcell Varga <a.marcell.varga@gmail.com>**.

See [NOTICE.md](NOTICE.md) for original asset and validator credits.
