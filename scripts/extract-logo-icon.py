"""Extract icon-only from HD logo, remove white background -> transparent PNG."""
from PIL import Image
from pathlib import Path

SRC = Path(r"C:\Users\Xensma\corail-livret\public\brand\logo-corail-hd.jpg")
OUT_DIR = Path(r"C:\Users\Xensma\corail-livret\public\brand")

img = Image.open(SRC).convert("RGBA")
w, h = img.size
print(f"HD logo: {w}x{h}")

# Crop top portion (where the coral motif is — roughly upper 42% to exclude the text)
icon_box = (0, 0, w, int(h * 0.42))
icon = img.crop(icon_box)

# Remove near-white background (alpha = 0 for whites)
data = icon.getdata()
new_data = []
for r, g, b, a in data:
    # If pixel is near-white, make it transparent
    if r > 240 and g > 240 and b > 240:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append((r, g, b, a))
icon.putdata(new_data)

# Auto-trim transparent borders
bbox = icon.getbbox()
if bbox:
    icon = icon.crop(bbox)
    print(f"Trimmed icon: {icon.size}")

# Resize to a reasonable size (max 512px wide for clarity)
icon.thumbnail((512, 512), Image.LANCZOS)
icon.save(OUT_DIR / "logo-icon.png", "PNG", optimize=True)
print(f"Saved logo-icon.png ({icon.size})")

# Also create a darker turquoise variant for light backgrounds
# (here we keep turquoise as-is, it works on both)
