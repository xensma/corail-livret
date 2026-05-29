#!/usr/bin/env python3
"""Extract embedded images from the 4 reference PDFs."""
import pathlib, pypdf, io
from PIL import Image

DOWNLOADS = pathlib.Path(r"C:\Users\Xensma\Downloads")
ROOT = pathlib.Path(r"C:\Users\Xensma\corail-livret\public\photos\villas")

MAP = {
    "Livret d'accueil Villa Piment Bleu.pdf": "piment-bleu",
    "Livret d'accueil Villa Tiki Reva.pdf":   "tiki-reva",
    "Livret d'accueil Villa Rêve Indigo.pdf": "reve-indigo",
    "Savannah.pdf":                           "savannah",
}

MIN_KB = 30  # skip tiny logo/icon images
TARGET_W = 1600

for pdfname, slug in MAP.items():
    src = DOWNLOADS / pdfname
    if not src.exists():
        print(f"MISSING {src}"); continue
    dst_dir = ROOT / slug
    dst_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n== {slug} ==")
    reader = pypdf.PdfReader(src)
    saved = 0
    for pi, page in enumerate(reader.pages):
        try:
            imgs = page.images
        except Exception as e:
            print(f"  p{pi+1} error listing: {e}"); continue
        for ii, img in enumerate(imgs):
            data = img.data
            if len(data) < MIN_KB * 1024:
                continue
            try:
                pil = Image.open(io.BytesIO(data))
                w, h = pil.size
                if w < 600 or h < 400:  # skip tiny
                    continue
                # Resize down to TARGET_W max width
                if w > TARGET_W:
                    nh = int(round(h * TARGET_W / w))
                    pil = pil.resize((TARGET_W, nh), Image.LANCZOS)
                if pil.mode in ("RGBA", "P"):
                    pil = pil.convert("RGB")
                saved += 1
                fname = "cover.jpg" if saved == 1 else f"gallery-{saved-1:02d}.jpg"
                out = dst_dir / fname
                pil.save(out, format="JPEG", quality=85, optimize=True)
                print(f"  p{pi+1} img{ii+1} {pil.size} -> {fname} ({out.stat().st_size} bytes)")
                if saved >= 13:
                    break
            except Exception as e:
                print(f"  p{pi+1} img{ii+1} decode err: {e}")
        if saved >= 13:
            break
