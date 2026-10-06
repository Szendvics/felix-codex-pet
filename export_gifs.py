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
    (301, 1, 4, 4, "Talajra érkezés, felállás"),
    (302, 2, 6, 12, "Séta balra"),
    (303, 2, 6, 12, "Séta jobbra"),
    (304, 2, 1, 2, "Fordulás szemből jobbra"),
    (305, 2, 1, 2, "Fordulás szemből balra"),
    (306, 2, 6, 12, "Leülés, nézelődés, felállás"),
    (307, 2, 2, 4, "Oldalra néző ülő pózok"),
    (308, 4, 2, 8, "Kikukucskálás alulról"),
    (309, 4, 2, 8, "Kikukucskálás oldalról"),
    (310, 1, 5, 5, "Eltűnés az alsó szélen"),
    (311, 6, 4, 24, "Evés a tálból"),
    (312, 2, 17, 34, "Hal, A változat — külön kellék"),
    (313, 2, 11, 22, "Hal, B változat — külön kellék"),
    (314, 2, 4, 8, "Hal, C változat — külön kellék"),
    (315, 6, 4, 24, "Macska az akváriummal"),
    (316, 4, 7, 26, "Bebújás a macskaajtón"),
    (317, 4, 1, 4, "Apró fej / szemek a peremnél — részlet"),
    (318, 4, 6, 23, "Kibújás a macskaajtón"),
    (319, 3, 3, 9, "Felugrás, mancsnyomok az üvegen"),
    (320, 4, 3, 12, "Leülés, fejfordítás"),
    (321, 4, 8, 32, "Lelapulás, fülek hátra, farokmozgás"),
    (322, 2, 6, 12, "Hátat fordít, leül, mozgatja a farkát"),
    (323, 3, 4, 12, "Tévénézés"),
    (324, 4, 5, 20, "Mosakodás, mancsnyalogatás"),
    (325, 4, 5, 18, "Szemből ülés, mancs felemelése"),
    (326, 4, 8, 32, "Mozgó pontok — az archívumban nincs teljes macska"),
    (327, 3, 5, 13, "Mozgó pontok — az archívumban nincs teljes macska"),
    (328, 7, 2, 14, "Mozgó pontok — az archívumban nincs teljes macska"),
    (1200, 1, 1, 1, "Nyitókép / logó — állókép"),
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
    table = [marker, "", "| ID · képsor | Képkockák | GIF |",
             "| --- | --- | --- |"]
    for ident, _, _, count, title in SHEETS:
        table.append(f"| **{ident}** · {title} | [{count} db, 0–{count-1}](fig_{ident}.frames.png) "
                     f"| ![{ident} — {title}](fig_{ident}.gif) |")
    readme.write_text(guide + "\n".join(table) + "\n")
    print(f"Exported and checked {len(SHEETS)} GIFs and numbered frame sheets in {OUT}")


if __name__ == "__main__":
    export()
