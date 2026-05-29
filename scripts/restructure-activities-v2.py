"""Build the real Gwadatrip catalog + add 3 new external suggestions."""
import json
from pathlib import Path

F = Path(r"C:\Users\Xensma\corail-livret\src\data\saint-francois\activities.json")
data = json.loads(F.read_text(encoding="utf-8"))

# Keep only external (suggestions) — drop all current gwadatrip
externals = [a for a in data if a.get("source") == "external"]

# REAL Gwadatrip catalog (10)
gwadatrip = [
    {
        "id": "petite-terre-no-limit", "slug": "petite-terre-no-limit",
        "name": "Petite Terre — No Limit Excursions",
        "tagline": "Réserve Naturelle de Petite Terre avec No Limit Excursions",
        "type": "Bateau", "category": "Bateau",
        "location": "Réserve Naturelle, Guadeloupe",
        "durationHours": 9, "duration": "9h00",
        "priceFrom": 150, "priceTo": 150, "currency": "EUR",
        "difficulty": "Facile", "rating": 4.9, "reviews": 487,
        "groupSize": "Max 12", "operator": "No Limit Excursions",
        "bookingUrl": "https://gwadatrip.com",
        "departurePoint": "Marina de Saint-François",
        "coordinates": {"lat": 16.2533, "lng": -61.2786},
        "description": "Journée premium dans la réserve naturelle de Petite Terre avec l'opérateur No Limit.",
        "advanceBooking": "Très demandé — réservez tôt",
        "photo": "/photos/activities/petite-terre-no-limit.webp",
        "highlight": True, "source": "gwadatrip",
        "i18n": {"en": {
            "tagline": "Petite Terre Nature Reserve with No Limit Excursions",
            "type": "Boat", "category": "Boat",
            "location": "Nature Reserve, Guadeloupe", "duration": "9am",
            "difficulty": "Easy", "groupSize": "Max 12",
            "departurePoint": "Saint-François Marina",
            "description": "Premium day in Petite Terre nature reserve with No Limit operator.",
            "advanceBooking": "Very popular — book early"
        }}
    },
    {
        "id": "petite-terre-miami-vice", "slug": "petite-terre-miami-vice",
        "name": "Petite Terre — Miami Vice",
        "tagline": "Excursion demi-journée à Petite Terre avec Miami Vice",
        "type": "Bateau", "category": "Bateau",
        "location": "Réserve Naturelle, Guadeloupe",
        "durationHours": 5, "duration": "½ journée",
        "priceFrom": 125, "priceTo": 125, "currency": "EUR",
        "difficulty": "Facile", "rating": 4.8, "reviews": 312,
        "groupSize": "Max 12", "operator": "Miami Vice",
        "bookingUrl": "https://gwadatrip.com",
        "departurePoint": "Marina de Saint-François",
        "coordinates": {"lat": 16.2533, "lng": -61.2786},
        "description": "Demi-journée intense vers Petite Terre — adapté pour ceux qui veulent profiter sans y passer la journée entière.",
        "advanceBooking": "Places limitées",
        "photo": "/photos/activities/petite-terre-miami-vice.webp",
        "highlight": False, "source": "gwadatrip",
        "i18n": {"en": {
            "tagline": "Half-day Petite Terre trip with Miami Vice",
            "type": "Boat", "category": "Boat",
            "location": "Nature Reserve, Guadeloupe", "duration": "Half day",
            "difficulty": "Easy", "groupSize": "Max 12",
            "departurePoint": "Saint-François Marina",
            "description": "Intense half-day to Petite Terre — for those who want to enjoy without spending the whole day.",
            "advanceBooking": "Limited spots"
        }}
    },
    {
        "id": "marie-galante-miami-vice", "slug": "marie-galante-miami-vice",
        "name": "Marie-Galante — Miami Vice",
        "tagline": "L'île aux 100 moulins avec Miami Vice",
        "type": "Bateau", "category": "Bateau",
        "location": "Marie-Galante, Guadeloupe",
        "durationHours": 9, "duration": "9h00",
        "priceFrom": 115, "priceTo": 115, "currency": "EUR",
        "difficulty": "Facile", "rating": 4.8, "reviews": 198,
        "groupSize": "Max 12", "operator": "Miami Vice",
        "bookingUrl": "https://gwadatrip.com",
        "departurePoint": "Marina de Saint-François",
        "coordinates": {"lat": 16.2533, "lng": -61.2786},
        "description": "Journée à Marie-Galante avec Miami Vice — distilleries, plages désertes, déjeuner créole.",
        "advanceBooking": "Départ demain disponible",
        "photo": "/photos/activities/marie-galante-miami-vice.webp",
        "highlight": False, "source": "gwadatrip",
        "i18n": {"en": {
            "tagline": "The island of 100 windmills with Miami Vice",
            "type": "Boat", "category": "Boat",
            "location": "Marie-Galante, Guadeloupe", "duration": "9am",
            "difficulty": "Easy", "groupSize": "Max 12",
            "departurePoint": "Saint-François Marina",
            "description": "Day in Marie-Galante with Miami Vice — distilleries, deserted beaches, Creole lunch.",
            "advanceBooking": "Tomorrow departure available"
        }}
    },
    {
        "id": "marie-galante-no-limit", "slug": "marie-galante-no-limit",
        "name": "Marie-Galante — No Limit Excursions",
        "tagline": "Journée authentique à Marie-Galante",
        "type": "Bateau", "category": "Bateau",
        "location": "Marie-Galante, Guadeloupe",
        "durationHours": 9, "duration": "9h00",
        "priceFrom": 110, "priceTo": 110, "currency": "EUR",
        "difficulty": "Facile", "rating": 4.9, "reviews": 256,
        "groupSize": "Max 12", "operator": "No Limit Excursions",
        "bookingUrl": "https://gwadatrip.com",
        "departurePoint": "Marina de Saint-François",
        "coordinates": {"lat": 16.2533, "lng": -61.2786},
        "description": "Journée authentique à Marie-Galante avec No Limit — atmosphère locale et conviviale.",
        "advanceBooking": "Très demandé",
        "photo": "/photos/activities/marie-galante-no-limit.webp",
        "highlight": False, "source": "gwadatrip",
        "i18n": {"en": {
            "tagline": "Authentic day in Marie-Galante",
            "type": "Boat", "category": "Boat",
            "location": "Marie-Galante, Guadeloupe", "duration": "9am",
            "difficulty": "Easy", "groupSize": "Max 12",
            "departurePoint": "Saint-François Marina",
            "description": "Authentic day in Marie-Galante with No Limit — local convivial atmosphere.",
            "advanceBooking": "Very popular"
        }}
    },
    {
        "id": "grand-cul-de-sac-marin", "slug": "grand-cul-de-sac-marin",
        "name": "Grand Cul-de-Sac Marin",
        "tagline": "Lagon préservé, mangrove et îlets de la côte nord",
        "type": "Nature", "category": "Nature",
        "location": "Lagon, Guadeloupe",
        "durationHours": 7, "duration": "7h00",
        "priceFrom": 115, "priceTo": 115, "currency": "EUR",
        "difficulty": "Facile", "rating": 4.8, "reviews": 189,
        "groupSize": "Max 12", "operator": "Partenaires Gwadatrip",
        "bookingUrl": "https://gwadatrip.com",
        "departurePoint": "Sainte-Rose ou Vieux-Bourg",
        "coordinates": {"lat": 16.3289, "lng": -61.6973},
        "description": "Journée dans le Grand Cul-de-Sac Marin — mangrove, îlets de sable blanc, snorkeling sur récif corallien.",
        "advanceBooking": "Places limitées",
        "photo": "/photos/activities/grand-cul-de-sac-marin.webp",
        "highlight": False, "source": "gwadatrip",
        "i18n": {"en": {
            "tagline": "Pristine lagoon, mangrove and northern islets",
            "type": "Nature", "category": "Nature",
            "location": "Lagoon, Guadeloupe", "duration": "7am",
            "difficulty": "Easy", "groupSize": "Max 12",
            "departurePoint": "Sainte-Rose or Vieux-Bourg",
            "description": "Day in the Grand Cul-de-Sac Marin — mangrove, white-sand islets, snorkeling on coral reef.",
            "advanceBooking": "Limited spots"
        }}
    },
    {
        "id": "jet-ski-ambiance-jet", "slug": "jet-ski-ambiance-jet",
        "name": "Jet-ski — Ambiance Jet",
        "tagline": "Sensations à Saint-François avec Ambiance Jet",
        "type": "Aventure", "category": "Aventure",
        "location": "Saint-François, Guadeloupe",
        "durationHours": 1, "duration": "1h à journée",
        "priceFrom": 130, "priceTo": 130, "currency": "EUR",
        "difficulty": "Modéré", "rating": 4.7, "reviews": 142,
        "groupSize": "1-2 / jet", "operator": "Ambiance Jet",
        "bookingUrl": "https://gwadatrip.com",
        "departurePoint": "Marina de Saint-François",
        "coordinates": {"lat": 16.2533, "lng": -61.2786},
        "description": "Location et randonnée jet-ski avec Ambiance Jet à Saint-François.",
        "advanceBooking": "Départ demain disponible",
        "photo": "/photos/activities/jet-ski-ambiance-jet.webp",
        "highlight": False, "source": "gwadatrip",
        "i18n": {"en": {
            "tagline": "Thrills in Saint-François with Ambiance Jet",
            "type": "Adventure", "category": "Adventure",
            "location": "Saint-François, Guadeloupe", "duration": "1h to full day",
            "difficulty": "Moderate", "groupSize": "1-2 / jet",
            "departurePoint": "Saint-François Marina",
            "description": "Jet-ski rental and rides with Ambiance Jet in Saint-François.",
            "advanceBooking": "Tomorrow departure available"
        }}
    },
    {
        "id": "desirade-jet-ski", "slug": "desirade-jet-ski",
        "name": "La Désirade en Jet-ski",
        "tagline": "L'expérience exclusive — La Désirade pilotée par vous-même",
        "type": "Aventure", "category": "Aventure",
        "location": "La Désirade, Guadeloupe",
        "durationHours": 6, "duration": "Journée",
        "priceFrom": 400, "priceTo": 400, "currency": "EUR",
        "difficulty": "Sportif", "rating": 4.9, "reviews": 64,
        "groupSize": "1-2 / jet", "operator": "Ambiance Jet",
        "bookingUrl": "https://gwadatrip.com",
        "departurePoint": "Marina de Saint-François",
        "coordinates": {"lat": 16.2533, "lng": -61.2786},
        "description": "Journée exceptionnelle vers La Désirade en jet-ski — réservé aux pilotes expérimentés.",
        "advanceBooking": "Très demandé — exclusif",
        "photo": "/photos/activities/desirade-jet-ski.webp",
        "highlight": True, "source": "gwadatrip",
        "i18n": {"en": {
            "name": "La Désirade by Jet-ski",
            "tagline": "The exclusive experience — La Désirade with you at the helm",
            "type": "Adventure", "category": "Adventure",
            "location": "La Désirade, Guadeloupe", "duration": "Full day",
            "difficulty": "Sporty", "groupSize": "1-2 / jet",
            "departurePoint": "Saint-François Marina",
            "description": "Exceptional day to La Désirade by jet-ski — for experienced riders only.",
            "advanceBooking": "Very popular — exclusive"
        }}
    },
    {
        "id": "paddle-kayak-mangrove", "slug": "paddle-kayak-mangrove",
        "name": "Paddle & Kayak — Mangrove",
        "tagline": "Découverte douce de la mangrove en paddle ou kayak",
        "type": "Nature", "category": "Nature",
        "location": "Grand Cul-de-Sac Marin",
        "durationHours": 4, "duration": "½ journée",
        "priceFrom": 45, "priceTo": 45, "currency": "EUR",
        "difficulty": "Facile", "rating": 4.7, "reviews": 224,
        "groupSize": "Illimité", "operator": "Partenaires Gwadatrip",
        "bookingUrl": "https://gwadatrip.com",
        "departurePoint": "Sainte-Rose",
        "coordinates": {"lat": 16.3289, "lng": -61.6973},
        "description": "Glissez en silence dans la mangrove — accessible à tous, idéal en famille.",
        "advanceBooking": "Places limitées",
        "photo": "/photos/activities/paddle-kayak-mangrove.jpg",
        "highlight": False, "source": "gwadatrip",
        "i18n": {"en": {
            "name": "Paddle & Kayak — Mangrove",
            "tagline": "Gentle discovery of the mangrove by paddleboard or kayak",
            "type": "Nature", "category": "Nature",
            "location": "Grand Cul-de-Sac Marin", "duration": "Half day",
            "difficulty": "Easy", "groupSize": "Unlimited",
            "departurePoint": "Sainte-Rose",
            "description": "Glide silently through the mangrove — accessible to all, ideal for families.",
            "advanceBooking": "Limited spots"
        }}
    },
    {
        "id": "snorkeling-karukera", "slug": "snorkeling-karukera",
        "name": "Snorkeling & Apnée — Karukera",
        "tagline": "Sortie snorkeling et apnée avec Karukera",
        "type": "Plongée", "category": "Plongée",
        "location": "Saint-François / Grand Cul-de-Sac Marin",
        "durationHours": 4, "duration": "½ journée",
        "priceFrom": 60, "priceTo": 60, "currency": "EUR",
        "difficulty": "Facile", "rating": 5.0, "reviews": 38,
        "groupSize": "Max 14", "operator": "Karukera",
        "bookingUrl": "https://gwadatrip.com",
        "departurePoint": "Selon programme",
        "coordinates": {"lat": 16.2533, "lng": -61.2786},
        "description": "Demi-journée snorkeling et apnée avec l'équipe Karukera — petits groupes, encadrement expert.",
        "advanceBooking": "Nouveauté — très demandé",
        "photo": "/photos/activities/snorkeling-karukera.webp",
        "highlight": True, "source": "gwadatrip",
        "i18n": {"en": {
            "tagline": "Snorkeling and freediving with Karukera",
            "type": "Diving", "category": "Diving",
            "location": "Saint-François / Grand Cul-de-Sac Marin", "duration": "Half day",
            "difficulty": "Easy", "groupSize": "Max 14",
            "departurePoint": "Per programme",
            "description": "Half-day snorkeling and freediving with the Karukera team — small groups, expert guidance.",
            "advanceBooking": "New — very popular"
        }}
    },
    {
        "id": "bateau-sans-permis", "slug": "bateau-sans-permis",
        "name": "Bateau sans permis — Lagon de Saint-François",
        "tagline": "Votre bateau privé sans permis dans le lagon turquoise",
        "type": "Bateau", "category": "Bateau",
        "location": "Lagon de Saint-François, Guadeloupe",
        "durationHours": 8, "duration": "9h00 – 17h00",
        "priceFrom": 150, "priceTo": 150, "currency": "EUR",
        "difficulty": "Facile", "rating": 5.0, "reviews": 89,
        "groupSize": "Max 9 pers", "operator": "Saloon Boats",
        "bookingUrl": "https://gwadatrip.com",
        "departurePoint": "Marina de Saint-François",
        "coordinates": {"lat": 16.2533, "lng": -61.2786},
        "description": "Bateau privé sans permis dans le lagon de Saint-François — barbecue à bord, glacière, baignade libre.",
        "advanceBooking": "Nouveauté — places limitées",
        "photo": "/photos/activities/bateau-sans-permis.webp",
        "highlight": False, "source": "gwadatrip",
        "i18n": {"en": {
            "name": "Licence-free boat — Saint-François Lagoon",
            "tagline": "Your private licence-free boat in the turquoise lagoon",
            "type": "Boat", "category": "Boat",
            "location": "Saint-François Lagoon, Guadeloupe", "duration": "9am – 5pm",
            "difficulty": "Easy", "groupSize": "Max 9 people",
            "departurePoint": "Saint-François Marina",
            "description": "Private licence-free boat in Saint-François lagoon — onboard BBQ, cooler, free swimming.",
            "advanceBooking": "New — limited spots"
        }}
    }
]

# 3 new external suggestions
new_externals = [
    {
        "id": "valombreuse", "slug": "valombreuse",
        "name": "Jardin Botanique de Valombreuse",
        "tagline": "5 hectares de fleurs tropicales et faune en liberté",
        "type": "Terre", "category": "Terre",
        "location": "Petit-Bourg, Guadeloupe",
        "durationHours": 2.5, "duration": "2h-3h",
        "priceFrom": 16.5, "priceTo": 16.5, "currency": "EUR",
        "difficulty": "Facile", "rating": 4.7, "reviews": 1280,
        "groupSize": "Visite libre", "operator": "Jardin de Valombreuse",
        "bookingUrl": "https://www.valombreuse.com",
        "officialSite": "https://www.valombreuse.com",
        "departurePoint": "Chemin de Grande Savane, Cabout, 97170 Petit-Bourg",
        "coordinates": {"lat": 16.1953, "lng": -61.6035},
        "description": "1000+ espèces botaniques, perroquets, loris, aras, flamants roses. Petit train électrique, case créole musée, restaurant, aire de jeux. Ouvert 365 j/an, 9h-18h (dernière entrée 16h30).",
        "advanceBooking": None,
        "photo": "/photos/activities/valombreuse.webp",
        "highlight": False, "source": "external",
        "i18n": {"en": {
            "name": "Valombreuse Botanical Garden",
            "tagline": "5 hectares of tropical flowers and free-roaming wildlife",
            "type": "Land", "category": "Land",
            "location": "Petit-Bourg, Guadeloupe", "duration": "2h-3h",
            "difficulty": "Easy", "groupSize": "Self-guided",
            "departurePoint": "Chemin de Grande Savane, Cabout, 97170 Petit-Bourg",
            "description": "1000+ botanical species, parrots, lorikeets, macaws, flamingos. Electric train, Creole house museum, restaurant, playground. Open daily 9am-6pm (last entry 4:30pm)."
        }}
    },
    {
        "id": "aquarium-guadeloupe", "slug": "aquarium-guadeloupe",
        "name": "Aquarium de la Guadeloupe",
        "tagline": "Le 1er aquarium des Antilles françaises — Le Gosier",
        "type": "Terre", "category": "Terre",
        "location": "Le Gosier, Guadeloupe",
        "durationHours": 2, "duration": "2h",
        "priceFrom": 14.9, "priceTo": 14.9, "currency": "EUR",
        "difficulty": "Facile", "rating": 4.5, "reviews": 2160,
        "groupSize": "Visite libre", "operator": "Aquarium de la Guadeloupe",
        "bookingUrl": "https://www.aquariumdelaguadeloupe.com",
        "officialSite": "https://www.aquariumdelaguadeloupe.com",
        "departurePoint": "Place Créole - Marina - 97190 Le Gosier",
        "coordinates": {"lat": 16.2133, "lng": -61.4934},
        "description": "Bassins lagon, mangrove, requins, tortues. Animations nourrissage le matin 10h30 et l'après-midi 16h. Ouvert 7j/7 de 9h à 19h. Tarif famille 2A+2E : 44€.",
        "advanceBooking": "Voir animations nourrissage selon jour",
        "photo": "/photos/activities/aquarium.jpg",
        "highlight": False, "source": "external",
        "i18n": {"en": {
            "name": "Guadeloupe Aquarium",
            "tagline": "The first aquarium in the French West Indies — Le Gosier",
            "type": "Land", "category": "Land",
            "location": "Le Gosier, Guadeloupe", "duration": "2h",
            "difficulty": "Easy", "groupSize": "Self-guided",
            "departurePoint": "Place Créole - Marina - 97190 Le Gosier",
            "description": "Lagoon, mangrove, shark and turtle tanks. Feeding shows at 10:30am and 4pm. Open daily 9am-7pm. Family ticket 2A+2C: €44.",
            "advanceBooking": "Check feeding show schedule"
        }}
    },
    {
        "id": "memorial-acte", "slug": "memorial-acte",
        "name": "Mémorial ACTe",
        "tagline": "Le musée mondial de la traite négrière et de l'esclavage",
        "type": "Terre", "category": "Terre",
        "location": "Pointe-à-Pitre, Guadeloupe",
        "durationHours": 2.5, "duration": "2h-3h",
        "priceFrom": 15, "priceTo": 20, "currency": "EUR",
        "difficulty": "Facile", "rating": 4.6, "reviews": 1890,
        "groupSize": "Visite libre + audioguide", "operator": "Mémorial ACTe",
        "bookingUrl": "https://memorial-acte.fr",
        "officialSite": "https://memorial-acte.fr",
        "departurePoint": "Rue Raspail, Darboussier, 97110 Pointe-à-Pitre",
        "coordinates": {"lat": 16.2403, "lng": -61.5363},
        "description": "Centre caribéen d'expressions et de mémoire de la Traite et de l'Esclavage. 7 800 m², exposition permanente sur 1 700 m². Prix Musée du Conseil de l'Europe 2017. Audioguide FR/EN/Créole. Comptez 2-3h.",
        "advanceBooking": "Mardi-Dimanche 9h-18h (dernier départ 16h30)",
        "photo": "/photos/activities/memorial-acte.jpg",
        "photoCredit": "© Wikimedia Commons",
        "highlight": False, "source": "external",
        "i18n": {"en": {
            "name": "Mémorial ACTe",
            "tagline": "The world memorial to the slave trade and slavery",
            "type": "Land", "category": "Land",
            "location": "Pointe-à-Pitre, Guadeloupe", "duration": "2h-3h",
            "difficulty": "Easy", "groupSize": "Self-guided + audioguide",
            "departurePoint": "Rue Raspail, Darboussier, 97110 Pointe-à-Pitre",
            "description": "Caribbean centre for expression and memory of the Slave Trade and Slavery. 7,800 m², permanent exhibition over 1,700 m². Council of Europe Museum Prize 2017. Audioguide FR/EN/Creole. Allow 2-3h.",
            "advanceBooking": "Tue-Sun 9am-6pm (last entry 4:30pm)"
        }}
    }
]

# Assemble: gwadatrip first, then externals (existing 7 + new 3)
data = gwadatrip + externals + new_externals

F.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Total: {len(data)} activities")
print(f"Gwadatrip: {len(gwadatrip)}")
print(f"External: {len(externals) + len(new_externals)} (7 existing + 3 new)")
for a in data:
    star = "*" if a.get("highlight") else " "
    print(f"  [{a['source'][:3]}] {star} {a['name']}")

# Also update shops.json to use Corner Shop PNG logo
SF = Path(r"C:\Users\Xensma\corail-livret\src\data\saint-francois\shops.json")
shops = json.loads(SF.read_text(encoding="utf-8"))
for s in shops:
    if s["id"] == "corner-shop":
        s["photo"] = "/photos/shops/corner-shop.png"
SF.write_text(json.dumps(shops, ensure_ascii=False, indent=2), encoding="utf-8")
print("\nCorner Shop photo updated to .png")
