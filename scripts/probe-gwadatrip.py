"""Fetch Gwadatrip home and extract SSR JSON data + activity listings."""
import urllib.request
import re
import json
from pathlib import Path

URL = "https://gwadatrip.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8"
}

req = urllib.request.Request(URL, headers=HEADERS)
html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="replace")

print(f"HTML length: {len(html):,} bytes\n")

# Look for various SSR data patterns
markers = [
    "__NEXT_DATA__",
    "window.__NUXT__",
    "window.__INITIAL_STATE__",
    "<script type=\"application/json\"",
    "<script type=\"application/ld+json\"",
    "data-rh=",
    "<meta property=\"og:image\""
]
for m in markers:
    if m in html:
        idx = html.index(m)
        print(f"FOUND: {m} @ pos {idx}")

# Extract <script type="application/json"> blocks
json_blocks = re.findall(r'<script[^>]*type="application/(?:ld\+)?json"[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"\nJSON script blocks found: {len(json_blocks)}")
for i, block in enumerate(json_blocks):
    block = block.strip()
    print(f"  Block {i}: {len(block)} chars, starts with: {block[:120]!r}")

# Try parsing the first big JSON block
if json_blocks:
    Path(r"C:\Users\Xensma\corail-livret\scripts\gwadatrip-data.json").write_text(
        json_blocks[0], encoding="utf-8"
    )
    print(f"\nSaved first JSON block to gwadatrip-data.json")
    try:
        data = json.loads(json_blocks[0])
        print(f"  Top-level keys: {list(data.keys()) if isinstance(data, dict) else 'array'}")
    except Exception as e:
        print(f"  Parse error: {e}")

# Look for image URLs (often gives hints about the content)
imgs = re.findall(r'https://[^\s"\']+\.(?:jpg|jpeg|png|webp)', html)
unique_imgs = sorted(set(imgs))[:20]
print(f"\nFirst image URLs ({len(unique_imgs)} unique shown):")
for u in unique_imgs:
    print(f"  {u}")

# Look for og:image and meta data
og_image = re.search(r'<meta\s+property="og:image"\s+content="([^"]+)"', html)
og_title = re.search(r'<meta\s+property="og:title"\s+content="([^"]+)"', html)
og_desc = re.search(r'<meta\s+property="og:description"\s+content="([^"]+)"', html)
print(f"\nOpen Graph:")
if og_title: print(f"  og:title: {og_title.group(1)}")
if og_desc: print(f"  og:desc:  {og_desc.group(1)}")
if og_image: print(f"  og:image: {og_image.group(1)}")
