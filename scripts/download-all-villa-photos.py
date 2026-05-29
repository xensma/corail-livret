#!/usr/bin/env python3
"""Download photos for the 4 villas listed on corailconciergerie.com."""
import pathlib
import urllib.request
import urllib.error

BASE = "https://www.corailconciergerie.com/assets/images"
ROOT = pathlib.Path(r"C:\Users\Xensma\corail-livret\public\photos\villas")

VILLAS = {
    "luminescence": {
        "hero": "hero/luminescence-hero.jpg",
        "gallery": [
            "villas/jpg/luminescence/luminescence1.jpg",
            "villas/jpg/luminescence/luminescence7.jpg",
            "villas/jpg/luminescence/luminescence9.jpg",
            "villas/jpg/luminescence/luminescence22.jpg",
            "villas/jpg/luminescence/luminescence21.jpg",
            "villas/jpg/luminescence/luminescence17.jpg",
            "villas/jpg/luminescence/luminescence5.jpg",
            "villas/jpg/luminescence/luminescence14.jpg",
            "villas/jpg/luminescence/luminescence27.jpg",
            "villas/jpg/luminescence/luminescence10.jpg",
            "villas/jpg/luminescence/luminescence29.jpg",
            "villas/jpg/luminescence/luminescence31.jpg",
        ],
    },
    "mango": {
        "hero": "hero/mango-hero.jpg",
        "gallery": [
            "villas/jpg/mango/mango1.jpg",
            "villas/jpg/mango/mango2.jpg",
            "villas/jpg/mango/mango7.jpg",
            "villas/jpg/mango/mango8.jpg",
            "villas/jpg/mango/mango10.jpg",
            "villas/jpg/mango/mango11.jpg",
            "villas/jpg/mango/mango14.jpg",
            "villas/jpg/mango/mango15.jpg",
            "villas/jpg/mango/mango16.jpg",
            "villas/jpg/mango/mango17.jpg",
            "villas/jpg/mango/mango19.jpg",
            "villas/jpg/mango/mango20.jpg",
        ],
    },
    "verdea": {
        "hero": "hero/verdea-hero.jpg",
        "gallery": [
            "villas/jpg/verdea/verdea1.jpg",
            "villas/jpg/verdea/verdea3.jpg",
            "villas/jpg/verdea/verdea4.jpg",
            "villas/jpg/verdea/verdea7.jpg",
            "villas/jpg/verdea/verdea8.jpg",
            "villas/jpg/verdea/verdea9.jpg",
            "villas/jpg/verdea/verdea10.jpg",
            "villas/jpg/verdea/verdea11.jpg",
            "villas/jpg/verdea/verdea12.jpg",
            "villas/jpg/verdea/verdea13.jpg",
            "villas/jpg/verdea/verdea14.jpg",
            "villas/jpg/verdea/verdea15.jpg",
        ],
    },
    "prairies-turquoises": {
        "hero": "hero/prairies-hero.jpg",
        "gallery": [
            "villas/jpg/prairies/pt2.jpg",
            "villas/jpg/prairies/pt3.jpg",
            "villas/jpg/prairies/pt4.jpg",
            "villas/jpg/prairies/pt5.jpg",
            "villas/jpg/prairies/pt6.jpg",
            "villas/jpg/prairies/pt7.jpg",
            "villas/jpg/prairies/pt8.jpg",
            "villas/jpg/prairies/pt9.jpg",
            "villas/jpg/prairies/pt10.jpg",
        ],
    },
}

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

for slug, cfg in VILLAS.items():
    dest_dir = ROOT / slug
    dest_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n== {slug} ==")
    items = [(cfg["hero"], "cover.jpg")] + [
        (rel, f"gallery-{i+1:02d}.jpg") for i, rel in enumerate(cfg["gallery"])
    ]
    for src_rel, dst_name in items:
        url = f"{BASE}/{src_rel}"
        dst = dest_dir / dst_name
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=15) as r, dst.open("wb") as f:
                f.write(r.read())
            print(f"  OK {dst.name} - {dst.stat().st_size} bytes")
        except urllib.error.HTTPError as e:
            print(f"  HTTP {e.code} for {url}")
        except Exception as e:
            print(f"  FAIL {url}: {e}")
