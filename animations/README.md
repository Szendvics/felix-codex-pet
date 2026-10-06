# Felix — GIF selector

All **29 archived sequences** are available as separate GIFs below. Click a frame
count to open the numbered frame sheet if you want to use only part of a sequence.

The GIFs show each source sheet in full, read left to right and top to bottom.
Only trailing empty padding cells are omitted. Previews use 2× scaling and a gray
background for visibility. Each frame lasts **120 ms**; this is preview timing,
not timing recovered from the original program. Transitions jump back to the
start when the GIF repeats, so some need editing before they work as idle loops.

## Choose an animation for each state

| Codex state | What should it convey? | Final frame count | Codex timing |
| --- | --- | ---: | --- |
| `idle` | Calm default state with subtle, unobtrusive movement | 6 | 280, 110, 110, 140, 140, 320 ms |
| `running-right` | Moving right, with the cat facing right | 8 | 7 × 120 + 220 ms |
| `running-left` | Moving left, with the cat facing left | 8 | 7 × 120 + 220 ms |
| `waving` | Greeting or asking for attention | 4 | 3 × 140 + 280 ms |
| `jumping` | A jump: anticipation, lift, and landing | 5 | 4 × 140 + 280 ms |
| `failed` | Error, failure, or disappointment | 8 | 7 × 140 + 240 ms |
| `waiting` | Codex is waiting for your answer or approval | 6 | 5 × 150 + 260 ms |
| `running` | Codex is working: thinking or staying busy | 6 | 5 × 120 + 220 ms |
| `review` | Focused observation or inspection | 6 | 5 × 150 + 280 ms |

`running` is the **working state**; `running-left/right` cover directional movement.
The table describes each animation's purpose. The Codex app controls when it plays.
You do not need to find a GIF with the exact frame count: the selected sequence
will be adapted to the final atlas. One source can serve more than one state.

Specify a sequence ID, such as `idle=325`, or a frame range:
`idle=325:2–6` (zero-based, including both endpoints). These illustrate the format;
they do not change the current mapping. Copy and fill in this selection template:

```text
idle =
running-right =
running-left =
waving =
jumping =
failed =
waiting =
running =
review =
```

Sequences 312–314 are separate fish props; 317 contains only a head fragment.
Sequences 326–328 contain tiny moving dots in the archive, with no complete cat,
so they cannot serve as standalone pet animations. Sequence 1200 is a single
still image. Several names and counts on the source website are inaccurate;
the descriptions and counts here reflect the actual images.

Exporting does not modify the installed pet. To regenerate from the repository root:
`.venv/bin/python export_gifs.py`.

[Sources and attribution](../NOTICE.md) ·
[Codex states and timing](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/hatch-pet/references/animation-rows.md)

## All GIFs

<!-- generated gallery -->

| ID · sequence | Frames | GIF |
| --- | --- | --- |
| **301** · Landing and standing up | [4 total, 0–3](fig_301.frames.png) | ![301 — Landing and standing up](fig_301.gif) |
| **302** · Walking left | [12 total, 0–11](fig_302.frames.png) | ![302 — Walking left](fig_302.gif) |
| **303** · Walking right | [12 total, 0–11](fig_303.frames.png) | ![303 — Walking right](fig_303.gif) |
| **304** · Turning from front to right | [2 total, 0–1](fig_304.frames.png) | ![304 — Turning from front to right](fig_304.gif) |
| **305** · Turning from front to left | [2 total, 0–1](fig_305.frames.png) | ![305 — Turning from front to left](fig_305.gif) |
| **306** · Sitting down, looking around, standing up | [12 total, 0–11](fig_306.frames.png) | ![306 — Sitting down, looking around, standing up](fig_306.gif) |
| **307** · Seated poses facing sideways | [4 total, 0–3](fig_307.frames.png) | ![307 — Seated poses facing sideways](fig_307.gif) |
| **308** · Peeking up from below | [8 total, 0–7](fig_308.frames.png) | ![308 — Peeking up from below](fig_308.gif) |
| **309** · Peeking in from the side | [8 total, 0–7](fig_309.frames.png) | ![309 — Peeking in from the side](fig_309.gif) |
| **310** · Disappearing below the bottom edge | [5 total, 0–4](fig_310.frames.png) | ![310 — Disappearing below the bottom edge](fig_310.gif) |
| **311** · Eating from the bowl | [24 total, 0–23](fig_311.frames.png) | ![311 — Eating from the bowl](fig_311.gif) |
| **312** · Fish, variant A (separate prop) | [34 total, 0–33](fig_312.frames.png) | ![312 — Fish, variant A (separate prop)](fig_312.gif) |
| **313** · Fish, variant B (separate prop) | [22 total, 0–21](fig_313.frames.png) | ![313 — Fish, variant B (separate prop)](fig_313.gif) |
| **314** · Fish, variant C (separate prop) | [8 total, 0–7](fig_314.frames.png) | ![314 — Fish, variant C (separate prop)](fig_314.gif) |
| **315** · Cat with a fish bowl | [24 total, 0–23](fig_315.frames.png) | ![315 — Cat with a fish bowl](fig_315.gif) |
| **316** · Going through the cat flap | [26 total, 0–25](fig_316.frames.png) | ![316 — Going through the cat flap](fig_316.gif) |
| **317** · Small head and eyes at the edge (partial sprite) | [4 total, 0–3](fig_317.frames.png) | ![317 — Small head and eyes at the edge (partial sprite)](fig_317.gif) |
| **318** · Coming out of the cat flap | [23 total, 0–22](fig_318.frames.png) | ![318 — Coming out of the cat flap](fig_318.gif) |
| **319** · Jumping and leaving paw prints on the glass | [9 total, 0–8](fig_319.frames.png) | ![319 — Jumping and leaving paw prints on the glass](fig_319.gif) |
| **320** · Sitting down and turning the head | [12 total, 0–11](fig_320.frames.png) | ![320 — Sitting down and turning the head](fig_320.gif) |
| **321** · Crouching with ears back and moving the tail | [32 total, 0–31](fig_321.frames.png) | ![321 — Crouching with ears back and moving the tail](fig_321.gif) |
| **322** · Turning away, sitting down, moving the tail | [12 total, 0–11](fig_322.frames.png) | ![322 — Turning away, sitting down, moving the tail](fig_322.gif) |
| **323** · Watching TV | [12 total, 0–11](fig_323.frames.png) | ![323 — Watching TV](fig_323.gif) |
| **324** · Grooming and licking a paw | [20 total, 0–19](fig_324.frames.png) | ![324 — Grooming and licking a paw](fig_324.gif) |
| **325** · Sitting facing forward and raising a paw | [18 total, 0–17](fig_325.frames.png) | ![325 — Sitting facing forward and raising a paw](fig_325.gif) |
| **326** · Moving dots (no complete cat in the archive) | [32 total, 0–31](fig_326.frames.png) | ![326 — Moving dots (no complete cat in the archive)](fig_326.gif) |
| **327** · Moving dots (no complete cat in the archive) | [13 total, 0–12](fig_327.frames.png) | ![327 — Moving dots (no complete cat in the archive)](fig_327.gif) |
| **328** · Moving dots (no complete cat in the archive) | [14 total, 0–13](fig_328.frames.png) | ![328 — Moving dots (no complete cat in the archive)](fig_328.gif) |
| **1200** · Splash screen and logo (still image) | [1 total, 0–0](fig_1200.frames.png) | ![1200 — Splash screen and logo (still image)](fig_1200.gif) |
