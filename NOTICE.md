# Sources and attribution

## Felix artwork

Original animation sheets come from the archived Felix.exe desktop companion,
preserved and extracted by [chevp/kitty-on-screen](https://github.com/chevp/kitty-on-screen)
at commit `912cb839d4806dcd0f5b95f9317b6cf414fbfd65`.
That archive credits the original Screen Mates work to codehammer.com and
adtoolsinc.com and states that its maintainer is not the original creator.

This adaptation selects, scales, positions, and retimes existing frames for the
Codex atlas. The jump includes additional vertical movement. No legacy executable
is included or run. Source URLs and SHA-256 hashes are in `source/sources.json`.

The archive does not provide an artwork redistribution license. The original
character and artwork remain the property of their respective owners. This
private, unofficial adaptation does not claim ownership of or grant a new license
to that artwork, and is not endorsed by its owners or OpenAI.

## Atlas validator

`tools/validate_atlas.py` is copied without modification from
[OpenAI's hatch-pet tools](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/hatch-pet),
commit `49f948faa9258a0c61caceaf225e179651397431`.
Its Apache License 2.0 is preserved in `tools/LICENSE.openai-skills.txt`.

## Adaptation

Codex packaging and build script: Marcell Varga <a.marcell.varga@gmail.com>.
