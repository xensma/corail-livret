#!/usr/bin/env python3
"""For Corail Livret — Kisara villa:
  1. Update La Rhumerie du Pirate coordinates to the precise Google Maps values
     and add a `mapsUrl` field.
  2. Compute the Haversine distance from the villa to every restaurant and store
     it on each item (`distanceKm` rounded to 2 decimals, `walkMinutes` rounded
     up using 13 min/km — realistic for tropical heat on real-world routes).
  3. Sort the `proches` category by ascending distance so closest is first.
  4. Print a report of all restos by category with their computed distance.
"""
import json
import math
import pathlib

RESTOS_PATH = pathlib.Path(r"C:\Users\Xensma\corail-livret\src\data\saint-francois\restaurants.json")
VILLA_PATH = pathlib.Path(r"C:\Users\Xensma\corail-livret\src\data\villas\kisara.json")

# ---------------------------------------------------------------- helpers
def haversine_km(a, b):
    """Great-circle distance in km between two (lat, lng) pairs."""
    lat1, lng1 = math.radians(a[0]), math.radians(a[1])
    lat2, lng2 = math.radians(b[0]), math.radians(b[1])
    dlat = lat2 - lat1
    dlng = lng2 - lng1
    h = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(h))


# ---------------------------------------------------------------- load
with VILLA_PATH.open(encoding="utf-8") as f:
    villa = json.load(f)
villa_coords = (
    villa["location"]["coordinates"]["lat"],
    villa["location"]["coordinates"]["lng"],
)
print(f"Villa Kisara coords: {villa_coords}")

with RESTOS_PATH.open(encoding="utf-8") as f:
    data = json.load(f)

# ---------------------------------------------------------------- patch La Rhumerie du Pirate
for cat_key, cat in data.items():
    for item in cat.get("items", []):
        if item["id"] == "rhumerie-pirate":
            old = item["coordinates"]
            item["coordinates"] = {"lat": 16.259209, "lng": -61.256480}
            item["mapsUrl"] = "https://maps.app.goo.gl/TL2bYNaEVXnozp8R7"
            print(
                f"\nLa Rhumerie du Pirate:"
                f"\n  coords {old['lat']},{old['lng']} -> {item['coordinates']['lat']},{item['coordinates']['lng']}"
                f"\n  mapsUrl added"
            )

# ---------------------------------------------------------------- compute distance for every resto
for cat_key, cat in data.items():
    for item in cat.get("items", []):
        coords = item.get("coordinates")
        if not coords:
            continue
        d = haversine_km(villa_coords, (coords["lat"], coords["lng"]))
        item["distanceKm"] = round(d, 2)
        # 13 min/km -> ~4.6 km/h, realistic walking pace in tropical climate w/
        # real road routing (straight-line distance underestimates by ~25%).
        item["walkMinutes"] = max(1, math.ceil(d * 13))

# ---------------------------------------------------------------- sort proches by distance
data["proches"]["items"].sort(key=lambda r: r["distanceKm"])

# ---------------------------------------------------------------- save
with RESTOS_PATH.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")

# ---------------------------------------------------------------- report
print("\n=== Distances villa Kisara -> restos (km, walk min) ===")
for cat_key in ["proches", "marina", "sainte-anne", "pointe-chateaux", "le-moule", "traiteurs"]:
    cat = data[cat_key]
    print(f"\n[{cat_key}] {cat['label']}")
    items = sorted(cat["items"], key=lambda r: r.get("distanceKm", 999))
    for it in items:
        d = it.get("distanceKm")
        w = it.get("walkMinutes")
        print(f"  {d:>5.2f} km · {w:>3} min walk · {it['name']}")

print(f"\nOK — restaurants.json saved.")
