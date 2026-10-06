#!/usr/bin/env python3
"""Check CLI frame layout, cropping, and the repeating Working animation."""

import itertools
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent


def check():
    manifests = {name: json.loads((ROOT / name / "pet.json").read_text())
                 for name in ("felix", "felix-cli")}
    for name, manifest in manifests.items():
        running = manifest["animations"]["running"]
        assert running["loop"] is True, f"{name}: Working must keep looping"
        assert 0 < running["fps"] <= 60, f"{name}: unsupported CLI frame rate"
        schedule = [(index, len(list(group))*1000/running["fps"])
                    for index, group in itertools.groupby(running["frames"])]
        assert schedule == list(zip(range(56, 62), [120]*5+[220])), schedule

    assert manifests["felix-cli"]["frame"] == {"width": 192, "height": 144, "columns": 8, "rows": 13}
    with Image.open(ROOT / "felix/spritesheet.webp") as original, \
            Image.open(ROOT / "felix-cli/spritesheet.webp") as larger:
        original, larger = original.convert("RGBA"), larger.convert("RGBA")
        assert original.size == larger.size == (1536, 1872)
        for row in range(9):
            for column in range(8):
                before = original.crop((column*192, row*208, (column+1)*192, (row+1)*208))
                after = larger.crop((column*192, row*144, (column+1)*192, (row+1)*144))
                restored = Image.new("RGBA", before.size)
                restored.paste(after, (0, 46))
                assert restored.tobytes() == before.tobytes(), (row, column)
        assert larger.crop((0, 9*144, 1536, 1872)).getbbox() is None
    print("Checked CLI layout, all animation pixels, and the Working loop timing")


if __name__ == "__main__":
    check()
