"""Split activities into Gwadatrip (7) + Corail Suggestions (3) with proper sources & URLs."""
import json
from pathlib import Path

FILE = Path(r"C:\Users\Xensma\corail-livret\src\data\saint-francois\activities.json")
data = json.loads(FILE.read_text(encoding="utf-8"))

# IDs that are external (not on Gwadatrip) — move to "Suggestions" section
EXTERNAL_OVERRIDES = {
    "ascension-soufriere": {
        "photo": "/photos/activities/soufriere.webp",
        "photoCredit": "© Aurélien Brusini / Les Îles de Guadeloupe",
        "bookingUrl": "https://www.la-soufriere.com/",
        "officialSite": "https://www.la-soufriere.com/",
    },
    "chutes-du-carbet": {
        "photo": "/photos/activities/chutes-du-carbet.jpg",
        "bookingUrl": "https://www.guadeloupe-parcnational.fr/fr/des-decouvertes/les-sites/espaces-terrestres-du-parc-national/les-chutes-du-carbet",
        "officialSite": "https://www.guadeloupe-parcnational.fr/",
    },
    "plongee-reserve-cousteau": {
        "name": "Réserve Cousteau",
        "photo": "/photos/activities/reserve-cousteau.jpg",
        "bookingUrl": "https://www.reserve-cousteau.com/",
        "officialSite": "https://www.reserve-cousteau.com/",
    },
}

EXTERNAL_IDS = set(EXTERNAL_OVERRIDES.keys())

# Apply
for item in data:
    if item["id"] in EXTERNAL_IDS:
        item["source"] = "external"
        for k, v in EXTERNAL_OVERRIDES[item["id"]].items():
            item[k] = v
    else:
        item["source"] = "gwadatrip"

# Reorder: gwadatrip first, then external
data.sort(key=lambda x: (0 if x["source"] == "gwadatrip" else 1, 0 if x.get("highlight") else 1))

# Save
FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

# Summary
gw = [i for i in data if i["source"] == "gwadatrip"]
ex = [i for i in data if i["source"] == "external"]
print(f"Gwadatrip section ({len(gw)}):")
for a in gw: print(f"  - {a['name']} ({'★' if a.get('highlight') else ' '})")
print(f"\nSuggestions Corail ({len(ex)}):")
for a in ex: print(f"  - {a['name']} → {a['bookingUrl']}")
