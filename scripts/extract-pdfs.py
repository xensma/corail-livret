#!/usr/bin/env python3
"""Dump text content of 4 reference livret PDFs to local txt files for analysis."""
import pathlib
import pypdf

DOWNLOADS = pathlib.Path(r"C:\Users\Xensma\Downloads")
OUT_DIR = pathlib.Path(r"C:\Users\Xensma\corail-livret\scripts\_pdf_extracts")
OUT_DIR.mkdir(exist_ok=True)

PDFS = [
    "Livret d'accueil Villa Piment Bleu.pdf",
    "Livret d'accueil Villa Rêve Indigo.pdf",
    "Livret d'accueil Villa Tiki Reva.pdf",
    "Savannah.pdf",
]

for name in PDFS:
    src = DOWNLOADS / name
    if not src.exists():
        print(f"MISSING: {src}")
        continue
    reader = pypdf.PdfReader(src)
    out = OUT_DIR / (src.stem + ".txt")
    pages_text = []
    for i, p in enumerate(reader.pages):
        try:
            t = p.extract_text() or ""
        except Exception as e:
            t = f"[PAGE {i+1} EXTRACT ERROR: {e}]"
        pages_text.append(f"\n\n===== PAGE {i+1} =====\n{t}")
    out.write_text("".join(pages_text), encoding="utf-8")
    print(f"OK {src.name} -> {out.name} ({len(reader.pages)} pages, {out.stat().st_size} bytes)")
