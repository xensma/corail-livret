"""
Hybrid photo processing — handles both URLs and local files.

Workflow:
1. Local files dropped in C:\\Users\\Xensma\\corail-photos\\{category}\\{id}.{ext}
   are detected, optimized (900x560 max, JPG quality 85) and copied to public/photos/.
2. URL mappings in PHOTO_URLS dict are downloaded, optimized, and saved.
3. Existing public photos are kept if no new source is provided.
"""
import sys
from pathlib import Path
from PIL import Image
import urllib.request
import shutil

# ─── Configuration ──────────────────────────────────────────────────────────
INTAKE = Path(r"C:\Users\Xensma\corail-photos")
OUTPUT = Path(r"C:\Users\Xensma\corail-livret\public\photos")
TARGET_W = 1400  # max width for hero / cards
TARGET_H = 900   # max height
JPG_QUALITY = 85

# Paste URL mappings here — they take priority over local files
# Format: { "category": { "id": "https://..." } }
PHOTO_URLS = {
    "restos": {
        # "ogaiana": "https://example.com/ogaiana.jpg",
    },
    "beaches": {},
    "activities": {},
    "shops": {}
}

EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp'}


def optimize(src_path: Path, dest_path: Path):
    """Resize & re-save as JPG."""
    img = Image.open(src_path)
    if img.mode in ('RGBA', 'LA', 'P'):
        bg = Image.new('RGB', img.size, (245, 242, 237))  # corail cream
        if img.mode == 'P':
            img = img.convert('RGBA')
        bg.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
        img = bg
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    img.thumbnail((TARGET_W, TARGET_H), Image.LANCZOS)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest_path, "JPEG", quality=JPG_QUALITY, optimize=True)


def process_local(category: str):
    """Process local files in intake/{category}/."""
    src_dir = INTAKE / category
    out_dir = OUTPUT / category
    if not src_dir.exists():
        return []
    processed = []
    for src in src_dir.iterdir():
        if src.suffix.lower() not in EXTENSIONS:
            continue
        dest = out_dir / f"{src.stem}.jpg"
        try:
            optimize(src, dest)
            processed.append(f"local {category}/{dest.name} ({src.stat().st_size // 1024} KB → {dest.stat().st_size // 1024} KB)")
        except Exception as e:
            processed.append(f"FAIL {category}/{src.name}: {e}")
    return processed


def process_urls(category: str):
    """Download and optimize URLs."""
    out_dir = OUTPUT / category
    out_dir.mkdir(parents=True, exist_ok=True)
    processed = []
    for item_id, url in PHOTO_URLS.get(category, {}).items():
        try:
            tmp = out_dir / f"_tmp_{item_id}"
            urllib.request.urlretrieve(url, tmp)
            dest = out_dir / f"{item_id}.jpg"
            optimize(tmp, dest)
            tmp.unlink(missing_ok=True)
            processed.append(f"url   {category}/{dest.name} ({dest.stat().st_size // 1024} KB)")
        except Exception as e:
            processed.append(f"FAIL {category}/{item_id}: {e}")
    return processed


def main():
    print("=== Photo processing ===\n")
    total = 0
    for category in ("restos", "beaches", "activities", "shops"):
        results = process_local(category) + process_urls(category)
        if results:
            print(f"[{category}]")
            for r in results:
                print(f"  {r}")
            total += len(results)
            print()
    print(f"\nDONE — {total} photo(s) processed.")


if __name__ == "__main__":
    main()
