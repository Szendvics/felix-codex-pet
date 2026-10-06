#!/usr/bin/env python3
"""Pack the classic Felix frames into a Codex pet and validate the result."""

import bisect
import hashlib
import itertools
import json
from pathlib import Path
import subprocess
import sys

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
CELL = (192, 208)
SCALE = 1.5
GROUND = 190
# Original sheets have different cell sizes. Keep one scale for every pose.
GRIDS = {302: (2, 6), 303: (2, 6), 315: (6, 4), 319: (3, 3),
         322: (2, 6), 324: (4, 5), 325: (4, 5)}
# State, source sheet, source frames, vertical offsets, Codex frame durations.
# The archive reverses 302/303's direction labels; the pixels face left/right.
ROWS = [
    ("idle", 325, [2, 3, 4, 5, 6, 3], [0]*6, [280, 110, 110, 140, 140, 320]),
    ("running-right", 303, [0, 2, 3, 5, 6, 8, 9, 11], [0]*8, [120]*7+[220]),
    ("running-left", 302, [0, 2, 3, 5, 6, 8, 9, 11], [0]*8, [120]*7+[220]),
    ("waving", 325, [7, 9, 10, 13], [0]*4, [140]*3+[280]),
    ("jumping", 319, [2, 3, 4, 3, 0], [0, -16, -32, -16, 0], [140]*4+[280]),
    ("failed", 322, [0, 1, 2, 4, 6, 8, 10, 11], [0]*8, [140]*7+[240]),
    ("waiting", 325, [2, 3, 4, 5, 6, 3], [0]*6, [150]*5+[260]),
    ("running", 324, [6, 7, 8, 9, 10, 7], [0]*6, [120]*5+[220]),
    ("review", 315, [4, 6, 8, 12, 19, 21], [0]*6, [150]*5+[280]),
]
LABELS = ["Idle", "Drag right", "Drag left", "Wave", "Jump", "Failed",
          "Needs input", "Working", "Review"]


def source_frames():
    for entry in json.loads((ROOT / "source/sources.json").read_text()):
        path = ROOT / entry["path"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError(f"Source checksum mismatch: {path}")
    sheets = {}
    for ident, (cols, rows) in GRIDS.items():
        with Image.open(ROOT / f"source/fig_{ident}.png") as image:
            image = image.convert("RGBA")
        if image.width % cols or image.height % rows:
            raise ValueError(f"Invalid source grid: {ident}")
        w, h = image.width // cols, image.height // rows
        frames = [image.crop((x*w, y*h, (x+1)*w, (y+1)*h))
                  for y in range(rows) for x in range(cols)]
        # A shared baseline preserves the original motion within each sheet.
        baseline = max(frame.getbbox()[3] for frame in frames if frame.getbbox())
        sheets[ident] = (frames, baseline)
    return sheets


def render(frame, baseline, dy):
    scaled = frame.resize((round(frame.width*SCALE), round(frame.height*SCALE)),
                          Image.Resampling.NEAREST)
    x = (CELL[0] - scaled.width) // 2
    y = GROUND - round(baseline*SCALE) + dy
    bbox = scaled.getbbox()
    if bbox is None or not (4 <= x+bbox[0] < x+bbox[2] <= CELL[0]-4
                           and 4 <= y+bbox[1] < y+bbox[3] <= CELL[1]-4):
        raise ValueError("A pose is empty or clips the cell padding")
    cell = Image.new("RGBA", CELL)
    cell.alpha_composite(scaled, (x, y))
    return cell


def build():
    sheets = source_frames()
    atlas = Image.new("RGBA", (CELL[0]*8, CELL[1]*9))
    animations = []
    for row, (state, ident, indices, offsets, durations) in enumerate(ROWS):
        frames, baseline = sheets[ident]
        if not len(indices) == len(offsets) == len(durations):
            raise ValueError(f"Mismatched animation schedule: {state}")
        cells = [render(frames[i], baseline, dy) for i, dy in zip(indices, offsets)]
        if len({cell.tobytes() for cell in cells}) < 2:
            raise ValueError(f"Static animation: {state}")
        for column, cell in enumerate(cells):
            atlas.alpha_composite(cell, (column*CELL[0], row*CELL[1]))
        animations.append(cells)

    package = ROOT / "felix"
    package.mkdir(exist_ok=True)
    atlas.save(package / "spritesheet.webp", lossless=True, exact=True)
    (package / "pet.json").write_text(json.dumps({
        "id": "felix", "displayName": "Felix",
        "description": "The classic desktop cat, with his original animations.",
        "spritesheetPath": "spritesheet.webp",
    }, indent=2) + "\n")

    qa = ROOT / "qa"
    qa.mkdir(exist_ok=True)
    subprocess.run([sys.executable, str(ROOT / "tools/validate_atlas.py"),
                    str(package / "spritesheet.webp"), "--json-out",
                    str(qa / "validation.json")], check=True)
    contact = Image.new("RGB", (CELL[0]*8+140, CELL[1]*9), "#9297a1")
    contact.paste(atlas, (140, 0), atlas)
    draw = ImageDraw.Draw(contact)
    for row, label in enumerate(LABELS):
        draw.text((12, row*CELL[1]+90), label, fill="black")
    contact.save(qa / "contact-sheet.png")

    preview = []
    schedules = [list(itertools.accumulate(row[4])) for row in ROWS]
    for tick in range(0, 3000, 40):
        board = Image.new("RGB", (CELL[0]*3, (CELL[1]+28)*3), "#20242c")
        draw = ImageDraw.Draw(board)
        for row, cells in enumerate(animations):
            x, y = (row % 3)*CELL[0], (row // 3)*(CELL[1]+28)
            column = bisect.bisect_right(schedules[row], tick % schedules[row][-1])
            board.paste(cells[column], (x, y+20), cells[column])
            draw.text((x+12, y+8), LABELS[row], fill="white")
        preview.append(board)
    preview[0].save(ROOT / "preview.gif", save_all=True, append_images=preview[1:],
                    duration=40, loop=0, optimize=False)
    print(f"Built and validated {package}")


if __name__ == "__main__":
    build()
