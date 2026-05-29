#!/usr/bin/env python3
"""Prepare restaurants.json for dynamic per-villa 'Proches de la villa':
  - Strip villa-specific `distanceKm` / `walkMinutes` from every resto
    (they were computed against Kisara only; now computed at render time).
  - Move the 4 hand-curated 'proches' items into 'marina' so they still
    appear when a villa is far away from them.
  - Update the 'marina' label to acknowledge Crystal Beach / abords.
  - Empty `proches.items`. The render layer will fill it dynamically
    per villa by picking the N closest restos (Haversine) across all
    other categories.
"""
import json
import pathlib

PATH = pathlib.Path(r"C:\Users\Xensma\corail-livret\src\data\saint-francois\restaurants.json")

with PATH.open(encoding="utf-8") as f:
    data = json.load(f)

# 1. Strip villa-specific fields from all items
for cat in data.values():
    for item in cat.get("items", []):
        item.pop("distanceKm", None)
        item.pop("walkMinutes", None)

# 2. Move current proches items into marina (they are between marina and Crystal Beach geographically)
current_proches = data["proches"]["items"]
print(f"Moving {len(current_proches)} proches items into 'marina':")
for r in current_proches:
    print(f"  - {r['id']} | {r['name']}")
data["marina"]["items"] = current_proches + data["marina"]["items"]

# 3. Relabel marina to include Crystal Beach
data["marina"]["label"] = "Saint-François : Marina, centre-ville & Crystal Beach"
data["marina"]["label_en"] = "Saint-François: Marina, town centre & Crystal Beach"

# 4. Empty proches.items (render layer will compute per-villa)
data["proches"]["items"] = []

with PATH.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"\nOK - restaurants.json ready for dynamic proches.")
print(f"  marina now has {len(data['marina']['items'])} items.")
print(f"  proches.items emptied (rendered dynamically).")
