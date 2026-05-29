#!/usr/bin/env python3
"""Generate the 8 villa JSON data files from a single source-of-truth dictionary.

Practical info (gate codes, WiFi, trash location, landline) is extracted from the
PDFs the user shared. Everything else (restaurants list, beach list, activities,
Corail services) is shared across all villas — handled by data files outside
this generator.

Structure mirrors src/data/villas/kisara.json so the existing KisaraPage.astro
component renders any villa unchanged.
"""
import json, pathlib, copy

OUT = pathlib.Path(r"C:\Users\Xensma\corail-livret\src\data\villas")
OUT.mkdir(parents=True, exist_ok=True)
KISARA = json.loads((OUT / "kisara.json").read_text(encoding="utf-8"))

# -------------------------------------------------------------- shared
def shared_contacts():
    return copy.deepcopy(KISARA["contacts"])

def shared_bebettes():
    return copy.deepcopy(KISARA["bebettes"])

def shared_bebettes_en():
    return copy.deepcopy(KISARA["i18n"]["en"]["bebettes"])

def shared_trash(verre_loc):
    return {
        "ordures": "Containers gris dans le local poubelles à la sortie de la résidence. Sacs poubelle fermés. Évacuation tous les jours conseillée (chaleur).",
        "tri": "Container jaune dans le local : bouteilles plastique, papier/carton, fer/aluminium.",
        "verre": f"Conteneurs verts : {verre_loc}.",
    }
def shared_trash_en(verre_loc_en):
    return {
        "ordures": "Grey containers in the bin room at the residence exit. Closed bin bags. Daily disposal recommended (heat).",
        "tri": "Yellow container in the bin room: plastic bottles, paper/cardboard, metal/aluminium.",
        "verre": f"Green glass containers: {verre_loc_en}.",
    }

def shared_appliances(extras_fr=None):
    base = {
        "wifi": "WiFi fibre optique haut débit dans toute la villa.",
        "tv": "Box TV Orange (sélectionner source HDMI 1). Bouquet chaînes locales et internationales.",
        "coffee": "Cafetière filtre (filtres papier taille 4) + machine Nespresso (capsules dans les supermarchés).",
        "ac": "Climatisation dans chaque chambre — utiliser uniquement quand la pièce est occupée, portes/fenêtres fermées. La nuit : régler sur 26 °C, ventilation auto.",
        "water": "Eau potable + réserve 1 250 L et suppresseur → autonomie ~48h en cas de coupure réseau. Robinet extérieur du cabanon = indicateur réseau ville.",
        "septic": "Fosse septique : pas de lingettes, tampons, serviettes hygiéniques, ni javel/huile/produits chimiques.",
    }
    if extras_fr:
        base.update(extras_fr)
    return base

def shared_appliances_en(extras_en=None):
    base = {
        "wifi": "High-speed fibre WiFi throughout the villa.",
        "tv": "Orange TV box (HDMI 1 source). Local and international channels.",
        "coffee": "Filter coffee maker (size 4 paper filters) + Nespresso machine (capsules in supermarkets).",
        "ac": "AC in each bedroom — use only when occupied, doors/windows closed. At night: 26 °C, auto fan.",
        "water": "Drinkable water + 1,250 L reserve and pressure pump → ~48h autonomy during mains cuts. Outdoor garden shed tap = mains indicator.",
        "septic": "Septic tank: no wipes, tampons, sanitary pads, bleach, oil or harsh chemicals.",
    }
    if extras_en:
        base.update(extras_en)
    return base

def shared_pool():
    return {
        "alarm": "⚠ Surveillance enfants OBLIGATOIRE. Alarme avec aimant (logo plongeur) : voyant rouge = désactivée, vert = surveillance. La surveillance se réactive automatiquement ~15 min après la fin de baignade calme.",
        "rules": "Pas de crème solaire dans l'eau (douche avant baignade), pas de verre, pas d'objets coupants. L'accès au local technique est interdit.",
        "maintenance": "Nettoyage assuré par notre prestataire. Une épuisette est disponible. En cas de souci, contactez votre concierge.",
    }
def shared_pool_en():
    return {
        "alarm": "⚠ Adult supervision REQUIRED. Alarm with magnet (diver logo): red light = disarmed, green = active. Auto-rearms ~15 min after calm water returns.",
        "rules": "No sunscreen in the water (shower before), no glass, no sharp objects. Technical room is off-limits.",
        "maintenance": "Servicing by our provider. A skimmer net is available. Contact your concierge for any issue.",
    }

def shared_house_rules():
    return [
        "Pas de fête / événement bruyant sans accord préalable.",
        "Pas de fumée à l'intérieur. Espace fumeur sur la terrasse extérieure.",
        "Animaux non admis sauf accord écrit préalable.",
        "Respect du voisinage : silence après 22h, musique modérée.",
        "Signalez toute casse ou souci à votre concierge — on règle ensemble.",
    ]
def shared_house_rules_en():
    return [
        "No parties / loud events without prior approval.",
        "No smoking indoors. Smoking allowed on the outdoor terrace.",
        "No pets unless written approval.",
        "Respect neighbours: quiet after 10pm, moderate music.",
        "Report any breakage or issue to your concierge — we sort it together.",
    ]

def shared_departure(checkout="10h"):
    return [
        "Lancer une machine sur draps et serviettes utilisées.",
        "Vider toutes les poubelles, sortir les bacs si jour de collecte.",
        "Vider le frigo des denrées périssables.",
        "Nettoyer la grille du barbecue (si utilisé).",
        f"Fermer fenêtres, baies, clim et lumières. État des lieux à {checkout}.",
    ]
def shared_departure_en(checkout="10am"):
    return [
        "Run a load of laundry on used sheets and towels.",
        "Empty all bins, put them out if it's a collection day.",
        "Empty the fridge of perishables.",
        "Clean the BBQ grill (if used).",
        f"Close windows, doors, AC and lights. Check-out at {checkout}.",
    ]

def shared_weather():
    return {
        "alerte": "En cas d'alerte météo (juillet-octobre), suivre Météo France (www.meteofrance.gp) et la Préfecture (www.guadeloupe.gouv.fr). Stockez 3 jours d'eau et nourriture. Votre concierge reste joignable.",
        "saison": "Saison sèche : déc-avril (idéale). Saison humide : juillet-octobre (averses courtes, parfois cyclones).",
    }
def shared_weather_en():
    return {
        "alerte": "In case of weather alert (Jul-Oct), follow Météo France (meteofrance.gp) and Prefecture (guadeloupe.gouv.fr). Store 3 days of water and food. Concierge stays on hand.",
        "saison": "Dry season: Dec-April (ideal). Wet season: July-October (short showers, occasional cyclones).",
    }

def shared_amenities(features):
    """features: list of (icon, label_fr, label_en) tuples."""
    return [{"icon": i, "label": fr} for i, fr, _ in features], [{"icon": i, "label": en} for i, _, en in features]

# -------------------------------------------------------------- per-villa configs
# Format:
#   slug, name, tagline_fr/en, lat, lng, address, mapsUrl,
#   capacity (g/br/ba), distances (beach_name + fr_min, ...), amenities,
#   wifi (ssid, password), security (digicode, portillon, poubelles_code, special_notes_fr/en),
#   description_fr/en, welcomeMessage_fr/en,
#   stay (checkin, checkout, minNights),
#   photos_dir, photos_count, photo_ext (jpg|webp), tel
VILLAS = [
    {
        "id": "luminescence",
        "name": "Villa Luminescence",
        "tagline_fr": "Calme et élégance dans la résidence Louisiana Park",
        "tagline_en": "Calm and elegance in the Louisiana Park residence",
        "lat": 16.245176, "lng": -61.3048,
        "address": "Résidence Louisiana Park, 97118 Saint-François, Guadeloupe",
        "mapsUrl": "https://maps.app.goo.gl/F16m81yN51gdWu349",
        "neighborhood": "Résidence sécurisée Louisiana Park",
        "guests": 6, "bedrooms": 3, "bathrooms": 3,
        "distances": {
            "beach": ("Plage des Raisins Clairs", "Raisins Clairs beach", 5, "voiture", "drive"),
            "centre": ("Centre-ville Saint-François", "Saint-François town centre", 10, "voiture", "drive"),
            "marina": ("Marina de Saint-François", "Saint-François Marina", 10, "voiture", "drive"),
            "airport": ("Aéroport Pôle Caraïbes", "Pôle Caraïbes airport", 45, "voiture", "drive"),
        },
        "amenities_features": [
            ("pool", "Piscine à débordement", "Infinity pool"),
            ("pool", "Jacuzzi", "Jacuzzi"),
            ("ac", "3 chambres climatisées", "3 air-conditioned bedrooms"),
            ("shield", "Résidence Louisiana Park sécurisée", "Secure Louisiana Park residence"),
            ("wifi", "WiFi fibre optique", "Fibre WiFi"),
            ("parking", "Parking privé", "Private parking"),
            ("kitchen", "Cuisine équipée + Nespresso", "Equipped kitchen + Nespresso"),
            ("bbq", "Barbecue charbon", "Charcoal BBQ"),
        ],
        "wifi": {"ssid": "VillaLuminescence", "password": "Guadeloupe"},
        "tel": None,
        "security_codes": {"digicode": "2305 A", "portillonPieton": "2306 A", "poubelles": "2307"},
        "trash_verre_fr": "à 600m direction Saint-François, en bord de route",
        "trash_verre_en": "600m towards Saint-François, by the roadside",
        "welcome_fr": "Bienvenue à Luminescence, dans la résidence Louisiana Park. Profitez de votre piscine à débordement, du jacuzzi et de la quiétude des lieux. Nous restons à votre disposition pour toute demande.",
        "welcome_en": "Welcome to Luminescence, in the Louisiana Park residence. Enjoy your infinity pool, the jacuzzi and the peace and quiet. We remain at your service for any request.",
        "description_fr": "Villa contemporaine au cœur de la résidence privée et sécurisée Louisiana Park. Piscine à débordement, jacuzzi 5 places, 3 chambres climatisées avec salle d'eau privative, cuisine ouverte sur la terrasse. À 5 min des plages, 10 min du centre et de la marina.",
        "description_en": "Contemporary villa in the heart of the private, secure Louisiana Park residence. Infinity pool, 5-seat jacuzzi, 3 air-conditioned bedrooms each with private bathroom, open kitchen onto the terrace. 5 min from the beaches, 10 min from town and the marina.",
        "checkin": "16:00", "checkout": "10:00", "minNights": 7,
        "photos_dir": "luminescence", "photos_count": 12, "ext": "webp",
    },
    {
        "id": "piment-bleu",
        "name": "Villa Piment Bleu",
        "tagline_fr": "Architecture lumineuse dans Louisiana Park",
        "tagline_en": "Light-filled architecture in Louisiana Park",
        # Same residence as Luminescence (Louisiana Park) — coords identical
        "lat": 16.245176, "lng": -61.3048,
        "address": "Résidence Louisiana Park, 97118 Saint-François, Guadeloupe",
        "mapsUrl": "https://maps.app.goo.gl/F16m81yN51gdWu349",
        "neighborhood": "Résidence sécurisée Louisiana Park",
        "guests": 6, "bedrooms": 3, "bathrooms": 2,
        "distances": {
            "beach": ("Plage des Raisins Clairs", "Raisins Clairs beach", 5, "voiture", "drive"),
            "centre": ("Centre-ville Saint-François", "Saint-François town centre", 10, "voiture", "drive"),
            "marina": ("Marina de Saint-François", "Saint-François Marina", 10, "voiture", "drive"),
            "airport": ("Aéroport Pôle Caraïbes", "Pôle Caraïbes airport", 45, "voiture", "drive"),
        },
        "amenities_features": [
            ("pool", "Piscine privée", "Private pool"),
            ("ac", "Chambres climatisées", "Air-conditioned bedrooms"),
            ("shield", "Résidence Louisiana Park sécurisée", "Secure Louisiana Park residence"),
            ("wifi", "WiFi fibre optique", "Fibre WiFi"),
            ("parking", "Parking privé", "Private parking"),
            ("kitchen", "Cuisine équipée + Nespresso", "Equipped kitchen + Nespresso"),
            ("terrace", "Volets roulants électriques", "Electric roller shutters"),
            ("bbq", "Barbecue charbon", "Charcoal BBQ"),
        ],
        "wifi": {"ssid": "VillaPimentBleu", "password": "Guadeloupe"},
        "tel": "+590590930249",
        "security_codes": {"digicode": "2305 A", "portillonPieton": "2306 A", "poubelles": "2307"},
        "trash_verre_fr": "à 600m direction Saint-François, en bord de route",
        "trash_verre_en": "600m towards Saint-François, by the roadside",
        "welcome_fr": "Bienvenue à Piment Bleu, dans la résidence Louisiana Park. Lumière, terrasse et piscine vous attendent. À votre écoute pour toute demande pendant votre séjour.",
        "welcome_en": "Welcome to Piment Bleu, in the Louisiana Park residence. Light, terrace and pool await. We're here for any need during your stay.",
        "description_fr": "Villa au design lumineux dans la résidence privée Louisiana Park. Piscine privée, volets roulants électriques, terrasse extérieure et cuisine équipée. À 5 min des plages, 10 min du centre et de la marina.",
        "description_en": "Light-filled villa in the private Louisiana Park residence. Private pool, electric roller shutters, outdoor terrace and equipped kitchen. 5 min from the beaches, 10 min from town and the marina.",
        "checkin": "16:00", "checkout": "10:00", "minNights": 7,
        "photos_dir": "piment-bleu", "photos_count": 4, "ext": "jpg",
    },
    {
        "id": "tiki-reva",
        "name": "Villa Tiki Reva",
        "tagline_fr": "Ambiance tropicale dans Louisiana Park",
        "tagline_en": "Tropical vibes in Louisiana Park",
        "lat": 16.245176, "lng": -61.3048,
        "address": "Résidence Louisiana Park, 97118 Saint-François, Guadeloupe",
        "mapsUrl": "https://maps.app.goo.gl/F16m81yN51gdWu349",
        "neighborhood": "Résidence sécurisée Louisiana Park",
        "guests": 6, "bedrooms": 3, "bathrooms": 2,
        "distances": {
            "beach": ("Plage des Raisins Clairs", "Raisins Clairs beach", 5, "voiture", "drive"),
            "centre": ("Centre-ville Saint-François", "Saint-François town centre", 10, "voiture", "drive"),
            "marina": ("Marina de Saint-François", "Saint-François Marina", 10, "voiture", "drive"),
            "airport": ("Aéroport Pôle Caraïbes", "Pôle Caraïbes airport", 45, "voiture", "drive"),
        },
        "amenities_features": [
            ("pool", "Piscine privée", "Private pool"),
            ("ac", "Chambres climatisées", "Air-conditioned bedrooms"),
            ("shield", "Résidence Louisiana Park sécurisée", "Secure Louisiana Park residence"),
            ("wifi", "WiFi fibre optique", "Fibre WiFi"),
            ("parking", "Parking privé", "Private parking"),
            ("kitchen", "Cuisine équipée + Nespresso", "Equipped kitchen + Nespresso"),
            ("terrace", "Terrasse couverte", "Covered terrace"),
            ("bbq", "Barbecue charbon", "Charcoal BBQ"),
        ],
        "wifi": {"ssid": "Villa Tiki Reva", "password": "Guadeloupe"},
        "tel": "+590590472306",
        "security_codes": {"digicode": "2305 A", "portillonPieton": "2306 A", "poubelles": "2307"},
        "trash_verre_fr": "à 600m direction Saint-François, en bord de route",
        "trash_verre_en": "600m towards Saint-François, by the roadside",
        "welcome_fr": "Bienvenue à Tiki Reva, votre cocon tropical dans la résidence Louisiana Park. Piscine, terrasse et fraîcheur des chambres climatisées vous attendent.",
        "welcome_en": "Welcome to Tiki Reva, your tropical cocoon in the Louisiana Park residence. Pool, terrace and cool air-conditioned bedrooms await.",
        "description_fr": "Villa familiale dans la résidence privée Louisiana Park. Piscine, terrasse couverte et 3 chambres climatisées. À 5 min des plages, 10 min du centre et de la marina.",
        "description_en": "Family villa in the private Louisiana Park residence. Pool, covered terrace and 3 air-conditioned bedrooms. 5 min from the beaches, 10 min from town and the marina.",
        "checkin": "16:00", "checkout": "10:00", "minNights": 7,
        "photos_dir": "tiki-reva", "photos_count": 5, "ext": "jpg",
    },
    {
        "id": "mango",
        "name": "Villa Mango Eden Green",
        "tagline_fr": "Luxe discret à deux pas de Raisins Clairs",
        "tagline_en": "Discreet luxury steps from Raisins Clairs",
        "lat": 16.2478188, "lng": -61.2973216,
        "address": "Saint-François, Guadeloupe (proche Raisins Clairs)",
        "mapsUrl": "https://maps.app.goo.gl/RYRqW6sqY6reoMLB9",
        "neighborhood": "Quartier résidentiel proche Raisins Clairs et Manganao",
        "guests": 6, "bedrooms": 3, "bathrooms": 3,
        "distances": {
            "beach": ("Plage des Raisins Clairs", "Raisins Clairs beach", 750, "mètres", "metres"),  # use string distance
            "centre": ("Centre-ville Saint-François", "Saint-François town centre", 5, "voiture", "drive"),
            "marina": ("Marina de Saint-François", "Saint-François Marina", 5, "voiture", "drive"),
            "airport": ("Aéroport Pôle Caraïbes", "Pôle Caraïbes airport", 45, "voiture", "drive"),
        },
        "amenities_features": [
            ("pool", "Piscine sécurisée", "Secure pool"),
            ("pool", "Jacuzzi 5 places", "5-seat jacuzzi"),
            ("ac", "3 chambres climatisées", "3 air-conditioned bedrooms"),
            ("shield", "Cadre sécurisé", "Secure setting"),
            ("wifi", "WiFi fibre optique", "Fibre WiFi"),
            ("parking", "Parking privé", "Private parking"),
            ("kitchen", "Cuisine ouverte équipée", "Open equipped kitchen"),
            ("terrace", "Grande terrasse", "Large terrace"),
        ],
        "wifi": {"ssid": "VillaMango", "password": "Guadeloupe"},
        "tel": None,
        "security_codes": {"digicode": "À COMMUNIQUER", "portillonPieton": "À COMMUNIQUER", "poubelles": "À COMMUNIQUER"},
        "trash_verre_fr": "à proximité, indiqué par votre concierge à l'arrivée",
        "trash_verre_en": "nearby, shown by your concierge on arrival",
        "welcome_fr": "Bienvenue à Mango Eden Green. Profitez de la piscine sécurisée et du jacuzzi 5 places dans ce cadre 4★ à 750m de la plage des Raisins Clairs.",
        "welcome_en": "Welcome to Mango Eden Green. Enjoy the secure pool and 5-seat jacuzzi in this 4★ setting 750m from Raisins Clairs beach.",
        "description_fr": "Villa 4★ à 750m des plages des Raisins Clairs et du Manganao. Vaste salon, cuisine ouverte sur la terrasse, piscine sécurisée pour enfants et jacuzzi 5 places. 3 chambres équivalentes avec salles d'eau privatives.",
        "description_en": "4★ villa 750m from Raisins Clairs and Manganao beaches. Spacious living room, open kitchen onto the terrace, child-safe pool and 5-seat jacuzzi. 3 equivalent bedrooms each with private bathroom.",
        "checkin": "16:00", "checkout": "10:00", "minNights": 7,
        "photos_dir": "mango", "photos_count": 12, "ext": "jpg",
    },
    {
        "id": "verdea",
        "name": "Villa Verdéa",
        "tagline_fr": "La villa des Artistes — vue mer et art contemporain",
        "tagline_en": "The Artists' villa — sea view and contemporary art",
        "lat": 16.257748, "lng": -61.219787,
        "address": "Route de la Pointe des Châteaux, Saint-François",
        "mapsUrl": "https://maps.app.goo.gl/zAFpvhJpN33AkKNQ6",
        "neighborhood": "Proche Anse à la Gourde et Pointe des Châteaux",
        "guests": 6, "bedrooms": 3, "bathrooms": 3,
        "distances": {
            "beach": ("Plage de l'Anse à la Gourde", "Anse à la Gourde beach", 5, "voiture", "drive"),
            "centre": ("Centre-ville Saint-François", "Saint-François town centre", 12, "voiture", "drive"),
            "marina": ("Marina de Saint-François", "Saint-François Marina", 10, "voiture", "drive"),
            "airport": ("Aéroport Pôle Caraïbes", "Pôle Caraïbes airport", 55, "voiture", "drive"),
        },
        "amenities_features": [
            ("pool", "Piscine privée", "Private pool"),
            ("ac", "3 suites climatisées", "3 air-conditioned suites"),
            ("terrace", "Vue mer panoramique", "Panoramic sea view"),
            ("shield", "Cadre sécurisé", "Secure setting"),
            ("wifi", "WiFi fibre optique", "Fibre WiFi"),
            ("parking", "Parking privé", "Private parking"),
            ("kitchen", "Cuisine équipée", "Equipped kitchen"),
            ("bbq", "Barbecue", "Barbecue"),
        ],
        "wifi": {"ssid": "VillaVerdea", "password": "Guadeloupe"},
        "tel": None,
        "security_codes": {"digicode": "À COMMUNIQUER", "portillonPieton": "À COMMUNIQUER", "poubelles": "À COMMUNIQUER"},
        "trash_verre_fr": "indiqué par votre concierge à l'arrivée",
        "trash_verre_en": "shown by your concierge on arrival",
        "welcome_fr": "Bienvenue à Verdéa, la villa des Artistes. Profitez d'une vue mer panoramique, de l'art contemporain et de la quiétude proche de la Pointe des Châteaux.",
        "welcome_en": "Welcome to Verdéa, the Artists' villa. Enjoy panoramic sea views, contemporary art and tranquility near Pointe des Châteaux.",
        "description_fr": "Villa contemporaine neuve à Saint-François. Confort haut de gamme, art et nature. Proche de l'Anse à la Gourde et de la Pointe des Châteaux. 3 suites climatisées avec salle d'eau privative, piscine, vue mer panoramique.",
        "description_en": "Brand-new contemporary villa in Saint-François. High-end comfort, art and nature. Near Anse à la Gourde and Pointe des Châteaux. 3 air-conditioned suites each with private bathroom, pool, panoramic sea view.",
        "checkin": "16:00", "checkout": "10:00", "minNights": 7,
        "photos_dir": "verdea", "photos_count": 12, "ext": "jpg",
    },
    {
        "id": "prairies-turquoises",
        "name": "Les Prairies Turquoises",
        "tagline_fr": "Face à l'océan — 1ère ligne à Sainte-Anne",
        "tagline_en": "Facing the ocean — beachfront in Sainte-Anne",
        "lat": 16.2425822, "lng": -61.3347145,
        "address": "Sainte-Anne, Guadeloupe (première ligne océan)",
        "mapsUrl": "https://maps.app.goo.gl/jFQ1PdjQjxK85hKT6",
        "neighborhood": "Sainte-Anne, 1ère ligne océan, accès direct plage",
        "guests": 10, "bedrooms": 5, "bathrooms": 4,
        "distances": {
            "beach": ("Plage privée — accès direct", "Private beach — direct access", 0, "à pied", "walk"),
            "centre": ("Centre-ville Sainte-Anne", "Sainte-Anne town centre", 5, "voiture", "drive"),
            "marina": ("Marina de Saint-François", "Saint-François Marina", 20, "voiture", "drive"),
            "airport": ("Aéroport Pôle Caraïbes", "Pôle Caraïbes airport", 30, "voiture", "drive"),
        },
        "amenities_features": [
            ("pool", "Piscine à débordement", "Infinity pool"),
            ("ac", "5 chambres climatisées", "5 air-conditioned bedrooms"),
            ("terrace", "Vue mer permanente", "Constant sea view"),
            ("shield", "Cadre sécurisé", "Secure setting"),
            ("wifi", "WiFi fibre optique", "Fibre WiFi"),
            ("parking", "Parking privé", "Private parking"),
            ("kitchen", "Cuisine équipée", "Equipped kitchen"),
            ("bbq", "Barbecue", "Barbecue"),
        ],
        "wifi": {"ssid": "PrairiesTurquoises", "password": "Guadeloupe"},
        "tel": None,
        "security_codes": {"digicode": "À COMMUNIQUER", "portillonPieton": "À COMMUNIQUER", "poubelles": "À COMMUNIQUER"},
        "trash_verre_fr": "indiqué par votre concierge à l'arrivée",
        "trash_verre_en": "shown by your concierge on arrival",
        "welcome_fr": "Bienvenue aux Prairies Turquoises. Vue océan permanente, accès direct à la plage et levers/couchers de soleil exceptionnels. Profitez à 10 — la villa est faite pour cela.",
        "welcome_en": "Welcome to Les Prairies Turquoises. Constant ocean view, direct beach access and exceptional sunrises/sunsets. Built for 10 — make the most of it.",
        "description_fr": "Location luxe en 1ère ligne dans l'un des secteurs les plus prisés de Sainte-Anne. Accès direct à la plage. Volumes généreux, indoor-outdoor parfait, vue mer constante. Levers et couchers de soleil exceptionnels.",
        "description_en": "Beachfront luxury rental in one of Sainte-Anne's most sought-after spots. Direct beach access. Generous volumes, seamless indoor-outdoor flow, constant sea view. Exceptional sunrises and sunsets.",
        "checkin": "16:00", "checkout": "10:00", "minNights": 7,
        "photos_dir": "prairies-turquoises", "photos_count": 9, "ext": "jpg",
    },
    {
        "id": "reve-indigo",
        "name": "Villa Rêve Indigo",
        "tagline_fr": "Une parenthèse indigo à deux pas du centre",
        "tagline_en": "An indigo escape steps from the centre",
        "lat": 16.2540313, "lng": -61.2921683,
        "address": "Saint-François, Guadeloupe",
        "mapsUrl": "https://maps.app.goo.gl/5xn7Dwf5YkyVCHjz7",
        "neighborhood": "Résidence sécurisée — proche centre et plages",
        "guests": 6, "bedrooms": 3, "bathrooms": 2,
        "distances": {
            "beach": ("Plage des Raisins Clairs", "Raisins Clairs beach", 3, "voiture", "drive"),
            "centre": ("Centre-ville Saint-François", "Saint-François town centre", 5, "voiture", "drive"),
            "marina": ("Marina de Saint-François", "Saint-François Marina", 5, "voiture", "drive"),
            "airport": ("Aéroport Pôle Caraïbes", "Pôle Caraïbes airport", 45, "voiture", "drive"),
        },
        "amenities_features": [
            ("pool", "Piscine privée + balnéo", "Private pool + spa jets"),
            ("ac", "Chambres climatisées", "Air-conditioned bedrooms"),
            ("shield", "Coffre-fort, résidence sécurisée", "Safe, secure residence"),
            ("wifi", "WiFi fibre optique", "Fibre WiFi"),
            ("parking", "Parking privé", "Private parking"),
            ("kitchen", "Cuisine gaz + Nespresso", "Gas kitchen + Nespresso"),
            ("terrace", "Eau chaude solaire", "Solar hot water"),
            ("bbq", "Barbecue", "Barbecue"),
        ],
        "wifi": {"ssid": "Rêve Indigo", "password": "Guadeloupe"},
        "tel": "+590590978321",
        "security_codes": {
            "digicode": "0310",                # grand portail haut
            "portillonPieton": "1962",          # portillon piéton bas-gauche
            "poubelles": "À COMMUNIQUER",
        },
        "trash_verre_fr": "indiqué par votre concierge à l'arrivée",
        "trash_verre_en": "shown by your concierge on arrival",
        "welcome_fr": "Bienvenue à Rêve Indigo. Profitez de la piscine balnéo et de la quiétude du cadre. Un coffre-fort est à votre disposition dans le cellier (code à l'intérieur).",
        "welcome_en": "Welcome to Rêve Indigo. Enjoy the spa-jet pool and the peaceful setting. A safe is available in the utility room (code inside).",
        "description_fr": "Villa raffinée dans une résidence sécurisée de Saint-François. Piscine avec jets balnéo, eau chaude solaire, cuisine gaz, coffre-fort. 3 chambres climatisées, jardin tropical. Proche centre et plages.",
        "description_en": "Refined villa in a secure Saint-François residence. Pool with spa jets, solar hot water, gas kitchen, safe. 3 air-conditioned bedrooms, tropical garden. Near town and beaches.",
        "checkin": "16:00", "checkout": "10:00", "minNights": 7,
        "photos_dir": "reve-indigo", "photos_count": 6, "ext": "jpg",
    },
    {
        "id": "savannah",
        "name": "Résidence Savannah",
        "tagline_fr": "Appartement face à la plage, accès direct par portillon",
        "tagline_en": "Beachfront apartment, direct gate access",
        "lat": 16.2512049, "lng": -61.2659953,
        "address": "Résidence Savannah, Saint-François",
        "mapsUrl": "https://maps.app.goo.gl/ywV1j3aP4XjWQRuo6",
        "neighborhood": "Résidence sécurisée avec accès direct plage",
        "guests": 4, "bedrooms": 2, "bathrooms": 1,
        "distances": {
            "beach": ("Plage publique (accès portillon)", "Public beach (gate access)", 1, "à pied", "walk"),
            "centre": ("Centre-ville Saint-François", "Saint-François town centre", 5, "voiture", "drive"),
            "marina": ("Marina de Saint-François", "Saint-François Marina", 5, "voiture", "drive"),
            "airport": ("Aéroport Pôle Caraïbes", "Pôle Caraïbes airport", 45, "voiture", "drive"),
        },
        "amenities_features": [
            ("terrace", "Stores électriques", "Electric blinds"),
            ("ac", "Chambres climatisées (télécommande)", "AC bedrooms (remote)"),
            ("shield", "Accès plage par portillon 2845", "Beach access via gate 2845"),
            ("wifi", "WiFi fibre optique", "Fibre WiFi"),
            ("parking", "Place de parking + bip", "Parking spot + remote"),
            ("kitchen", "Cuisine équipée", "Equipped kitchen"),
            ("tv", "TV chaînes locales", "TV local channels"),
        ],
        "wifi": {"ssid": "Savannah", "password": "Guadeloupe"},
        "tel": None,
        "security_codes": {
            "digicode": "1 bip télécommande (parking)",
            "portillonPieton": "2845 (accès plage)",
            "poubelles": "À la sortie de la résidence",
        },
        "trash_verre_fr": "indiqué par votre concierge à l'arrivée",
        "trash_verre_en": "shown by your concierge on arrival",
        "welcome_fr": "Bienvenue dans la Résidence Savannah. Appartement non-fumeur, animaux non acceptés. Plage accessible via le portillon (code 2845) au bout de l'allée centrale. ⚠ Coupures d'eau possibles le soir après 18h.",
        "welcome_en": "Welcome to Résidence Savannah. Non-smoking apartment, no pets. Beach accessible via the gate (code 2845) at the end of the central path. ⚠ Water cuts possible in the evening after 6pm.",
        "description_fr": "Appartement à la résidence Savannah à Saint-François. Cuisine entièrement équipée, douche italienne, télévision chaînes locales, lave-linge, fer à repasser, machine à café. Accès direct à la plage publique par portillon privé (code 2845). Stores électriques. Coupures d'eau possibles le soir après 18h — bonne réserve recommandée.",
        "description_en": "Apartment at Résidence Savannah in Saint-François. Fully equipped kitchen, walk-in shower, local TV channels, washing machine, iron, coffee maker. Direct access to the public beach via private gate (code 2845). Electric blinds. Possible water cuts after 6pm — keep a reserve.",
        "checkin": "16:00", "checkout": "11:00", "minNights": 3,
        "photos_dir": "savannah", "photos_count": 3, "ext": "jpg",
    },
]

# -------------------------------------------------------------- builder
def build(v):
    am_fr, am_en = shared_amenities(v["amenities_features"])
    photos_dir = v["photos_dir"]
    ext = v["ext"]
    cover = f"/photos/villas/{photos_dir}/cover.{ext}"
    photos = [cover] + [f"/photos/villas/{photos_dir}/gallery-{i+1:02d}.{ext}" for i in range(v["photos_count"])]

    distances_fr = {}
    distances_en = {}
    for key, (name_fr, name_en, minutes, mode_fr, mode_en) in v["distances"].items():
        distances_fr[key] = {"name": name_fr, "minutes": minutes, "mode": mode_fr}
        distances_en[key] = {"name": name_en, "mode": mode_en}

    villa = {
        "id": v["id"],
        "name": v["name"],
        "tagline": v["tagline_fr"],
        "welcomeMessage": v["welcome_fr"],
        "description": v["description_fr"],
        "capacity": {"guests": v["guests"], "bedrooms": v["bedrooms"], "bathrooms": v["bathrooms"]},
        "location": {
            "address": v["address"],
            "coordinates": {"lat": v["lat"], "lng": v["lng"]},
            "neighborhood": v["neighborhood"],
            "mapsUrl": v["mapsUrl"],
        },
        "distances": distances_fr,
        "amenities": am_fr,
        "wifi": {**v["wifi"], "security": "WPA2", "notes": "Mot de passe transmis à l'arrivée."},
        "stay": {"checkin": v["checkin"], "checkout": v["checkout"], "minNights": v["minNights"]},
        "security": {
            "portail": "Le portail de la résidence se ferme automatiquement. Télécommande/bip à proximité, ou digicode.",
            "digicode": v["security_codes"]["digicode"],
            "portillonPieton": v["security_codes"]["portillonPieton"],
            "cles": f"Clés et bip remis au check-in par votre concierge. Local poubelles à code : {v['security_codes']['poubelles']}.",
        },
        "appliances": shared_appliances(),
        "pool": shared_pool(),
        "houseRules": shared_house_rules(),
        "trashSchedule": shared_trash(v["trash_verre_fr"]),
        "bebettes": shared_bebettes(),
        "departure": shared_departure(v["checkout"].replace(":00", "h")),
        "weather": shared_weather(),
        "contacts": shared_contacts(),
        "photos": photos,
        "coverPhoto": cover,
        "i18n": {
            "en": {
                "tagline": v["tagline_en"],
                "welcomeMessage": v["welcome_en"],
                "description": v["description_en"],
                "distances": distances_en,
                "amenities": am_en,
                "wifi": {"notes": "Password provided on arrival."},
                "security": {
                    "portail": "Residence gate closes automatically. Remote nearby, or keypad.",
                    "cles": f"Keys and remote handed over at check-in by your concierge. Bin room code: {v['security_codes']['poubelles']}.",
                },
                "appliances": shared_appliances_en(),
                "pool": shared_pool_en(),
                "houseRules": shared_house_rules_en(),
                "trashSchedule": shared_trash_en(v["trash_verre_en"]),
                "bebettes": shared_bebettes_en(),
                "departure": shared_departure_en(v["checkout"].replace(":00", "am").replace("11am", "11am").replace("10am", "10am")),
                "weather": shared_weather_en(),
            }
        },
    }
    # Telephone is optional metadata not rendered yet — store as note in welcomeMessage? skip for now.
    return villa


for cfg in VILLAS:
    villa = build(cfg)
    out = OUT / f"{cfg['id']}.json"
    out.write_text(json.dumps(villa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK {out.name} - {out.stat().st_size} bytes")
