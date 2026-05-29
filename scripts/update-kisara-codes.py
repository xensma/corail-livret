#!/usr/bin/env python3
"""Update Villa Kisara security codes — Kisara is in the SAME residence as
   Rêve Indigo: grand portail digicode 0310, portillon piéton 1962."""
import json, pathlib

PATH = pathlib.Path(r"C:\Users\Xensma\corail-livret\src\data\villas\kisara.json")
v = json.loads(PATH.read_text(encoding="utf-8"))

v["security"]["digicode"] = "0310"
v["security"]["portillonPieton"] = "1962"
# Update neighborhood note (same residence as Rêve Indigo)
v["location"]["neighborhood"] = "Résidence sécurisée — même que Villa Rêve Indigo"

PATH.write_text(json.dumps(v, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Kisara security codes updated:")
print(f"  digicode (grand portail): {v['security']['digicode']}")
print(f"  portillonPieton: {v['security']['portillonPieton']}")
print(f"  neighborhood: {v['location']['neighborhood']}")
