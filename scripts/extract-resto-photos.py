"""Parse downloaded HTML files to find real photo URLs (filter out logos/icons)."""
import re
import os
from pathlib import Path

TMP = Path(os.environ['TEMP'])
sites = ['autre-version','jardin-secret','rhumarin','mabouya','poivrier']

for name in sites:
    f = TMP / f'{name}.html'
    if not f.exists():
        print(f'\n=== {name} : MISSING ({f}) ===')
        continue
    html = f.read_text(encoding='utf-8', errors='replace')
    imgs = re.findall(r'(https?://[^\s"\'<>]+\.(?:jpg|jpeg|png|webp)(?:\?[^\s"\'<>]*)?)', html, re.IGNORECASE)
    # Skip logos / icons / small thumbs
    skip_re = re.compile(r'(?i)logo|favicon|icon|sprite|svg|thumb|placeholder|gravatar|wp-includes|emoji', re.IGNORECASE)
    real = [u for u in imgs if not skip_re.search(u)]
    # Dedupe by base URL
    seen, dedup = set(), []
    for u in real:
        base = re.sub(r'\?.*$', '', u).lower()
        if base not in seen:
            seen.add(base)
            dedup.append(u)
    print(f'\n=== {name} : {len(dedup)} real images ===')
    for u in dedup[:10]:
        print(f'  {u}')
