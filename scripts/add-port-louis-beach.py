#!/usr/bin/env python3
"""Insert Anse du Souffleur (Port Louis) beach into beaches.json
   between Plage Sainte-Anne and Grande Anse Deshaies."""
import json
import pathlib

BEACHES_PATH = pathlib.Path(r"C:\Users\Xensma\corail-livret\src\data\saint-francois\beaches.json")

with BEACHES_PATH.open(encoding="utf-8") as f:
    beaches = json.load(f)

new_beach = {
    "id": "anse-souffleur-port-louis",
    "name": "Anse du Souffleur (Port-Louis)",
    "tagline": "Sable blanc, eau lagon, l'une des plus belles du Nord Grande-Terre",
    "description": "Longue plage de sable blanc bordée de raisiniers et cocotiers, à Port-Louis. Eau translucide et peu profonde, idéale pour les enfants. Snacks créoles et restos de plage le long du front de mer. Compter 50 min de route depuis Saint-François.",
    "coordinates": {
        "lat": 16.4203,
        "lng": -61.5275,
    },
    "facilities": [
        "Parking",
        "Snack-bars créoles",
        "Restaurants de plage",
        "Ombre raisiniers",
    ],
    "safety": "Eau calme, baignade familiale. Pas de surveillance.",
    "bestTime": "Toute la journée — magnifique en fin d'après-midi",
    "photo": "/photos/beaches/anse-souffleur-port-louis.webp",
    "i18n": {
        "en": {
            "name": "Anse du Souffleur (Port-Louis)",
            "tagline": "White sand, lagoon water — one of the finest in northern Grande-Terre",
            "description": "Long white-sand beach lined with sea grapes and coconut palms, in Port-Louis. Translucent shallow water, perfect for kids. Creole snack bars and beach restaurants along the seafront. About a 50-minute drive from Saint-François.",
            "facilities": [
                "Parking",
                "Creole snack bars",
                "Beach restaurants",
                "Sea-grape shade",
            ],
            "safety": "Calm water, family-friendly swimming. Unsupervised.",
            "bestTime": "All day — gorgeous in late afternoon",
        }
    },
}

# Insert before Grande Anse Deshaies (last entry currently)
insert_idx = next(i for i, b in enumerate(beaches) if b["id"] == "grande-anse-deshaies")
beaches.insert(insert_idx, new_beach)

with BEACHES_PATH.open("w", encoding="utf-8") as f:
    json.dump(beaches, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"OK — beaches.json now has {len(beaches)} entries")
print(f"  Inserted '{new_beach['id']}' at index {insert_idx}")
for i, b in enumerate(beaches):
    marker = "  ->" if b["id"] == new_beach["id"] else "    "
    print(f"{marker} [{i}] {b['id']} | {b['name']}")
