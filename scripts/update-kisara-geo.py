#!/usr/bin/env python3
"""Update Kisara villa with real Google Maps coordinates + maps URL."""
import json
import pathlib

PATH = pathlib.Path(r"C:\Users\Xensma\corail-livret\src\data\villas\kisara.json")

with PATH.open(encoding="utf-8") as f:
    villa = json.load(f)

villa["location"]["address"] = "705 Richeplaine, 97118 Saint-François, Guadeloupe"
villa["location"]["coordinates"] = {
    "lat": 16.2541761,
    "lng": -61.2927855,
}
villa["location"]["mapsUrl"] = "https://maps.app.goo.gl/gGd1C9DLNhY7G8CH9"

with PATH.open("w", encoding="utf-8") as f:
    json.dump(villa, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("OK - kisara.location updated:")
print(json.dumps(villa["location"], ensure_ascii=False, indent=2))
