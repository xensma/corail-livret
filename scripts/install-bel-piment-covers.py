#!/usr/bin/env python3
"""Install new Bel'Escale + Piment Bleu cover photos (resize to 1600px wide,
   back up the Airbnb originals)."""
import pathlib
from PIL import Image

TARGET_W = 1600
JOBS = [
    {
        "src":     pathlib.Path(r"C:\Users\Xensma\Downloads\Bel Escale.jpg"),
        "dst_dir": pathlib.Path(r"C:\Users\Xensma\corail-livret\public\photos\villas\bel-escale"),
        "backup":  "cover.legacy-airbnb.jpg",
    },
    {
        "src":     pathlib.Path(r"C:\Users\Xensma\Downloads\piment bleu.jpg"),
        "dst_dir": pathlib.Path(r"C:\Users\Xensma\corail-livret\public\photos\villas\piment-bleu"),
        "backup":  "cover.legacy-pdf.jpg",
    },
]

for j in JOBS:
    dst = j["dst_dir"] / "cover.jpg"
    backup = j["dst_dir"] / j["backup"]
    if dst.exists() and not backup.exists():
        dst.rename(backup)
        print(f"  backup {dst.name} -> {backup.name}")
    img = Image.open(j["src"])
    w, h = img.size
    if w > TARGET_W:
        nh = int(round(h * TARGET_W / w))
        img = img.resize((TARGET_W, nh), Image.LANCZOS)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save(dst, format="JPEG", quality=85, optimize=True)
    print(f"  OK {j['dst_dir'].name}/cover.jpg: {img.size[0]}x{img.size[1]} ({dst.stat().st_size} bytes)")
