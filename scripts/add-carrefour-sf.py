#!/usr/bin/env python3
"""Restore Carrefour Market Saint-François to services.json.
   Insert it right after Super U so the two supermarkets group near each other
   (Monoprix stays at index 0)."""
import json
import pathlib

SERVICES_PATH = pathlib.Path(r"C:\Users\Xensma\corail-livret\src\data\saint-francois\services.json")

with SERVICES_PATH.open(encoding="utf-8") as f:
    services = json.load(f)

carrefour = {
    "id": "carrefour-market-sf",
    "name": "Carrefour Market Saint-François",
    "category": "Supermarché",
    "address": "Rue de la République, Saint-François",
    "coordinates": {
        "lat": 16.2528,
        "lng": -61.2769,
    },
    "phone": "+590590889090",
    "hours": "Lun-Sam 8h-20h, Dim 8h-13h",
    "website": "https://www.carrefour.fr/magasin/market-saint-francois",
    "i18n": {
        "en": {
            "category": "Supermarket",
            "hours": "Mon-Sat 8am-8pm, Sun 8am-1pm",
        }
    },
}

# Find Super U index, insert Carrefour right after it
insert_idx = next(i for i, s in enumerate(services) if s["id"] == "super-u") + 1
services.insert(insert_idx, carrefour)

with SERVICES_PATH.open("w", encoding="utf-8") as f:
    json.dump(services, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"OK - services.json now has {len(services)} entries")
print(f"  Inserted '{carrefour['id']}' at index {insert_idx}")
for i, s in enumerate(services):
    marker = "  ->" if s["id"] == carrefour["id"] else "    "
    print(f"{marker} [{i}] {s['id']} | {s['name']} ({s['category']})")
