#!/usr/bin/env python3
"""Download a curated subset of Villa La Rhumière photos from corailconciergerie.com
   into corail-livret/public/photos/villas/la-rhumiere/."""
import pathlib
import urllib.request
import urllib.error

DST_DIR = pathlib.Path(r"C:\Users\Xensma\corail-livret\public\photos\villas\la-rhumiere")
DST_DIR.mkdir(parents=True, exist_ok=True)

BASE = "https://www.corailconciergerie.com/assets/images"

# Cover (hero) + a few interior/exterior shots
photos = [
    ("hero/larhumiere-hero.jpg", "cover.jpg"),
    ("villas/jpg/larhumiere/larhumiere1.jpg", "pool-01.jpg"),
    ("villas/jpg/larhumiere/larhumiere4.jpg", "exterior-01.jpg"),
    ("villas/jpg/larhumiere/larhumiere6.jpg", "interior-01.jpg"),
    ("villas/jpg/larhumiere/larhumiere7.jpg", "interior-02.jpg"),
    ("villas/jpg/larhumiere/larhumiere8.jpg", "interior-03.jpg"),
    ("villas/jpg/larhumiere/larhumiere13.jpg", "bedroom-01.jpg"),
    ("villas/jpg/larhumiere/larhumiere17.jpg", "bedroom-02.jpg"),
    ("villas/jpg/larhumiere/larhumiere19.jpg", "bathroom-01.jpg"),
    ("villas/jpg/larhumiere/larhumiere23.jpg", "garden-01.jpg"),
    ("villas/jpg/larhumiere/larhumiere25.jpg", "garden-02.jpg"),
]

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
for src_rel, dst_name in photos:
    url = f"{BASE}/{src_rel}"
    dst = DST_DIR / dst_name
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as r, dst.open("wb") as f:
            f.write(r.read())
        print(f"  OK {dst.name}  {dst.stat().st_size} bytes")
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code} for {url}")
    except Exception as e:
        print(f"  FAIL {url}: {e}")

print(f"\nFiles in {DST_DIR}:")
for f in sorted(DST_DIR.iterdir()):
    print(f"  {f.name} - {f.stat().st_size} bytes")
