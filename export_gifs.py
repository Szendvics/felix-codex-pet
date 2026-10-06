#!/usr/bin/env python3
"""Export every archived sheet for manual selection; leave the pet unchanged."""

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageSequence

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "animations"
SCALE = 2
DURATION = 120  # Preview timing, not recovered Felix.exe timing.
BACKGROUND = "#aeb4bf"
# ID, columns, rows, used cells, description. Read cells left-to-right, top-to-bottom.
# The archive's captions/counts are unreliable; these grids were checked visually.
SHEETS = [
    (301, 1, 4, 4, "Landing and standing up"),
    (302, 2, 6, 12, "Walking left"),
    (303, 2, 6, 12, "Walking right"),
    (304, 2, 1, 2, "Turning right"),
    (305, 2, 1, 2, "Turning left"),
    (306, 2, 6, 12, "Sitting down, looking around, standing up"),
    (307, 2, 2, 4, "Sitting sideways"),
    (308, 4, 2, 8, "Peeking up from below"),
    (309, 4, 2, 8, "Peeking in from the side"),
    (310, 1, 5, 5, "Disappearing below the screen"),
    (311, 6, 4, 24, "Eating from the bowl"),
    (312, 2, 17, 34, "Fish A"),
    (313, 2, 11, 22, "Fish B"),
    (314, 2, 4, 8, "Fish C"),
    (315, 6, 4, 24, "Cat with a fish bowl"),
    (316, 4, 7, 26, "Going through the cat flap"),
    (317, 4, 1, 4, "Head at the screen edge"),
    (318, 4, 6, 23, "Coming out of the cat flap"),
    (319, 3, 3, 9, "Jumping, paw prints on the glass"),
    (320, 4, 3, 12, "Sitting and turning his head"),
    (321, 4, 8, 32, "Crouching with ears back and moving the tail"),
    (322, 2, 6, 12, "Turning away, sitting down, moving the tail"),
    (323, 3, 4, 12, "Watching TV"),
    (324, 4, 5, 20, "Grooming and licking a paw"),
    (325, 4, 5, 18, "Sitting and raising a paw"),
    (326, 4, 8, 32, "Moving dots A"),
    (327, 3, 5, 13, "Moving dots B"),
    (328, 7, 2, 14, "Moving dots C"),
    (1200, 1, 1, 1, "Splash screen and logo"),
]


def export():
    for entry in json.loads((ROOT / "source/sources.json").read_text()):
        if hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError(f"Source checksum mismatch: {entry['path']}")
    OUT.mkdir(exist_ok=True)
    for ident, cols, rows, count, _ in SHEETS:
        with Image.open(ROOT / f"source/fig_{ident}.png") as source:
            sheet = source.convert("RGBA")
        assert sheet.width % cols == sheet.height % rows == 0, ident
        w, h = sheet.width // cols, sheet.height // rows
        cells = [sheet.crop((x*w, y*h, (x+1)*w, (y+1)*h))
                 for y in range(rows) for x in range(cols)]
        assert all(cell.getbbox() for cell in cells[:count]), ident
        assert all(cell.getbbox() is None for cell in cells[count:]), ident
        frames = []
        for cell in cells[:count]:
            frame = Image.new("RGB", cell.size, BACKGROUND)
            frame.paste(cell, (0, 0), cell)
            frames.append(frame.resize((w*SCALE, h*SCALE), Image.Resampling.NEAREST))
        gif_path = OUT / f"fig_{ident}.gif"
        frames[0].save(gif_path, save_all=True, append_images=frames[1:],
                       duration=DURATION, loop=0, disposal=2, optimize=False)
        # Readback check: GIF may merge identical frames, but must retain their time.
        with Image.open(gif_path) as gif:
            assert gif.size == frames[0].size and gif.info["loop"] == 0, ident
            elapsed = sum(frame.info["duration"] for frame in ImageSequence.Iterator(gif))
            assert elapsed == count*DURATION, (ident, elapsed)

        cw, ch = w*SCALE+8, h*SCALE+24
        contact = Image.new("RGB", (cols*cw, rows*ch), BACKGROUND)
        draw = ImageDraw.Draw(contact)
        for index, frame in enumerate(frames):
            x, y = (index % cols)*cw, (index // cols)*ch
            contact.paste(frame, (x+4, y+20))
            draw.text((x+4, y+4), f"{ident}:{index}", fill="black")
        contact.save(OUT / f"fig_{ident}.frames.png")

    # Keep the hand-written guide; regenerate only the gallery table below it.
    readme = OUT / "README.md"
    marker = "<!-- generated gallery -->"
    guide = readme.read_text().split(marker)[0]
    table = [marker, "", "| ID · sequence | Frames | GIF |",
             "| --- | --- | --- |"]
    for ident, _, _, count, title in SHEETS:
        table.append(f"| **{ident}** · {title} | [{count} (0–{count-1})](fig_{ident}.frames.png) "
                     f"| ![{ident}: {title}](fig_{ident}.gif) |")
    readme.write_text(guide + "\n".join(table) + "\n")
    print(f"Exported and checked {len(SHEETS)} GIFs and numbered frame sheets in {OUT}")


if __name__ == "__main__":
    export()
