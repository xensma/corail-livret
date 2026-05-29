#!/usr/bin/env python3
"""Extract text + cover images from Crystal Beach 2025 PDF."""
import pathlib, io, pypdf
from PIL import Image

SRC = pathlib.Path(r"C:\Users\Xensma\Documents\site\Crystal_Beach2025.pdf")
TXT_OUT = pathlib.Path(r"C:\Users\Xensma\corail-livret\scripts\_pdf_extracts\Crystal_Beach2025.txt")
IMG_DIR = pathlib.Path(r"C:\Users\Xensma\corail-livret\public\photos\villas\crystal-beach")
TXT_OUT.parent.mkdir(parents=True, exist_ok=True)
IMG_DIR.mkdir(parents=True, exist_ok=True)

reader = pypdf.PdfReader(SRC)
print(f"Pages: {len(reader.pages)}")

# Text dump
parts = []
for i, p in enumerate(reader.pages):
    try:
        t = p.extract_text() or ""
    except Exception as e:
        t = f"[extract error p{i+1}: {e}]"
    parts.append(f"\n===== PAGE {i+1} =====\n{t}")
TXT_OUT.write_text("".join(parts), encoding="utf-8")
print(f"Text -> {TXT_OUT.name} ({TXT_OUT.stat().st_size} bytes)")

# Images: pick first decent-sized image per page, max ~15 photos
TARGET_W = 1600
saved = 0
for pi, page in enumerate(reader.pages):
    if saved >= 15:
        break
    try:
        imgs = page.images
    except Exception:
        continue
    for img in imgs:
        if len(img.data) < 40 * 1024:
            continue
        try:
            pil = Image.open(io.BytesIO(img.data))
            if pil.size[0] < 700 or pil.size[1] < 450:
                continue
            if pil.size[0] > TARGET_W:
                nh = int(round(pil.size[1] * TARGET_W / pil.size[0]))
                pil = pil.resize((TARGET_W, nh), Image.LANCZOS)
            if pil.mode in ("RGBA", "P"):
                pil = pil.convert("RGB")
            saved += 1
            name = "cover.jpg" if saved == 1 else f"gallery-{saved-1:02d}.jpg"
            out = IMG_DIR / name
            pil.save(out, format="JPEG", quality=85, optimize=True)
            print(f"  p{pi+1} -> {name} {pil.size} ({out.stat().st_size} bytes)")
            break  # one per page
        except Exception as e:
            print(f"  p{pi+1} img decode err: {e}")
print(f"Total images: {saved}")
