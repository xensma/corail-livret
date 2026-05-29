#!/usr/bin/env python3
"""Revert La Rhumerie du Pirate restaurant — I mistakenly attached Villa La
Rhumière's coords (16.259209, -61.256480) to it. Restore the original
approximate coords and drop the mapsUrl that belongs to the villa, not the
restaurant."""
import json
import pathlib

PATH = pathlib.Path(r"C:\Users\Xensma\corail-livret\src\data\saint-francois\restaurants.json")

with PATH.open(encoding="utf-8") as f:
    data = json.load(f)

for cat_key, cat in data.items():
    for item in cat.get("items", []):
        if item["id"] == "rhumerie-pirate":
            item["coordinates"] = {"lat": 16.2562, "lng": -61.231}  # original
            item.pop("mapsUrl", None)
            print(f"Reverted {item['id']} -> coords {item['coordinates']}")

with PATH.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
