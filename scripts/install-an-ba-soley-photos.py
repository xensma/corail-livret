#!/usr/bin/env python3
"""Install curated An Ba Soley La photos: pick 10 best from the 89 hi-res
   AIRBNB_COMPRESSEES folder, resize to max 1600px wide, replace existing."""
import pathlib
from PIL import Image

SRC = pathlib.Path(r"C:\Users\Xensma\Pictures\final hd\AIRBNB_COMPRESSEES")
DST = pathlib.Path(r"C:\Users\Xensma\corail-livret\public\photos\villas\an-ba-soley-la")
BACKUP = DST / "_legacy"

# Curated selection: cover = #22 (wide pool head-on with orange/yellow chairs + bar lounge visible),
# gallery = 9 more for full visual story.
SELECTION = [
    (22, "cover.jpg"),         # HERO: wide pool view facing villa
    (18, "gallery-01.jpg"),    # terrace under awning, pool + loungers
    (20, "gallery-02.jpg"),    # dining area + pool side view
    (11, "gallery-03.jpg"),    # pool top-down with sun loungers
    (1,  "gallery-04.jpg"),    # aerial property view
    (14, "gallery-05.jpg"),    # pool with orange/yellow chairs
    (2,  "gallery-06.jpg"),    # high aerial of villa+pool
    (15, "gallery-07.jpg"),    # pétanque court
    (13, "gallery-08.jpg"),    # pool calm
    (17, "gallery-09.jpg"),    # exterior profile
]

# Backup existing files before replacing
BACKUP.mkdir(parents=True, exist_ok=True)
for f in DST.iterdir():
    if f.is_file() and not f.name.startswith("_"):
        target = BACKUP / f.name
        if not target.exists():
            f.rename(target)
            print(f"  backup {f.name}")

# Install new ones
TARGET_W = 1600
for n, name in SELECTION:
    src_file = SRC / f"An Ba Soley La-{n}_airbnb.jpg"
    if not src_file.exists():
        print(f"  MISSING {src_file.name}")
        continue
    img = Image.open(src_file)
    w, h = img.size
    if w > TARGET_W:
        nh = int(round(h * TARGET_W / w))
        img = img.resize((TARGET_W, nh), Image.LANCZOS)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    out = DST / name
    img.save(out, format="JPEG", quality=85, optimize=True)
    print(f"  OK {name}: {img.size[0]}x{img.size[1]} ({out.stat().st_size} bytes)")

print("\nDone.")
