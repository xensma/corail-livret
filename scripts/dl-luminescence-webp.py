#!/usr/bin/env python3
"""Download Luminescence photos in WEBP format from corailconciergerie.com."""
import pathlib, urllib.request

BASE = "https://www.corailconciergerie.com/assets/images"
DST = pathlib.Path(r"C:\Users\Xensma\corail-livret\public\photos\villas\luminescence")
DST.mkdir(parents=True, exist_ok=True)

items = [
    ("hero/luminescence-hero.webp", "cover.webp"),
] + [
    (f"villas/webp/luminescence/luminescence{n}.webp", f"gallery-{i+1:02d}.webp")
    for i, n in enumerate([1, 7, 9, 22, 21, 17, 5, 14, 27, 10, 29, 31])
]

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
for src, dst_name in items:
    url = f"{BASE}/{src}"
    dst = DST / dst_name
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as r, dst.open("wb") as f:
            f.write(r.read())
        print(f"  OK {dst.name} - {dst.stat().st_size} bytes")
    except Exception as e:
        print(f"  FAIL {url}: {e}")
