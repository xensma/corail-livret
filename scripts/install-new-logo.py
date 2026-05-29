#!/usr/bin/env python3
"""Replace /brand/logo-corail.png with the new high-res transparent logo,
   resized to a web-friendly width while preserving aspect ratio."""
import pathlib
from PIL import Image

SRC = pathlib.Path(r"C:\Users\Xensma\Pictures\séléction photos pour post insta\Logo hight definition (2) transparent.png")
DST = pathlib.Path(r"C:\Users\Xensma\corail-livret\public\brand\logo-corail.png")

# Backup existing file once
backup = DST.with_name("logo-corail.legacy.png")
if not backup.exists() and DST.exists():
    backup.write_bytes(DST.read_bytes())
    print(f"  Backup: {backup}")

img = Image.open(SRC)
print(f"  Source: {img.size[0]}x{img.size[1]} mode={img.mode}")

# Resize to max width 1200px while keeping aspect ratio. The vertical/stacked
# logo (~1.52:1) ends up around 1200x789. Plenty of resolution at 2x density.
TARGET_W = 1200
ratio = TARGET_W / img.size[0]
new_h = int(round(img.size[1] * ratio))
img_resized = img.resize((TARGET_W, new_h), Image.LANCZOS)

# Ensure RGBA so transparency survives.
if img_resized.mode != "RGBA":
    img_resized = img_resized.convert("RGBA")

img_resized.save(DST, format="PNG", optimize=True)
size = DST.stat().st_size
print(f"  Saved : {DST} -> {TARGET_W}x{new_h} mode={img_resized.mode} ({size} bytes)")
