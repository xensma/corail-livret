# Corail Conciergerie — Livrets d'accueil

Site statique Astro hébergeant les livrets d'accueil digitaux des 15 villas et résidences gérées par Corail Conciergerie à Saint-François, Guadeloupe.

**URL de prod** : https://livrets.corailconciergerie.com

## Stack

- **Astro 4** (statique, SSG)
- **Tailwind CSS** (utility-first + charte Corail : turquoise #72C9C2, crème #F5F2ED)
- **i18n FR / EN** custom
- **Données JSON** (1 fichier par villa + données partagées Saint-François)
- **Hébergement** : O2switch (cPanel + Let's Encrypt SSL)

## Structure

```
src/
├── components/        # Astro components (Hero, RestaurantCard, NavMenu, etc.)
├── data/
│   ├── villas/        # 1 JSON par villa (kisara.json, la-rhumiere.json, etc.)
│   └── saint-francois/  # restaurants, plages, activités, services partagés
├── i18n/ui.ts         # strings FR/EN
├── layouts/
└── pages/
    ├── index.astro    # homepage FR
    ├── [slug].astro   # 1 page par villa FR
    └── en/            # versions EN
public/
├── brand/             # logos, favicon
└── photos/
    ├── villas/        # par slug
    ├── restos/
    ├── beaches/
    └── activities/
scripts/               # one-off (génération, migration)
```

## Dev local

```bash
npm install
npm run dev
# → http://localhost:4321
```

## Build prod

```bash
npm run build
# → dist/ contient le site statique à uploader sur O2switch
```

## Ajouter une villa

1. Créer `src/data/villas/<slug>.json` (cf. `kisara.json` pour le template)
2. Créer `src/pages/<slug>.astro` (4 lignes, copier `kisara.astro`)
3. Créer `src/pages/en/<slug>.astro`
4. Ajouter dans `src/pages/index.astro` et `src/pages/en/index.astro`
5. Photos dans `public/photos/villas/<slug>/cover.jpg` + `gallery-XX.jpg`

## Logique métier

### Sélection "Proches de la villa" (restaurants)

Pour chaque villa, les 4 restos affichés sont choisis selon (dans l'ordre) :

1. **`prochesOverride: [resto-id-list]`** dans le JSON — liste curée (ex. La Rhumière, Verdéa)
2. **`prochesMode: 'dynamic'`** — Haversine sur coords villa (ex. Prairies Turquoises)
3. **Fallback** : `restaurants.proches.items` (= 4 Crystal Beach Kisara) pour les villas proches géographiquement

Le rendu déduplique automatiquement : un resto en "proches" n'apparaît pas dans une autre catégorie.

### Villa vs Appartement

`propertyType: 'apartment'` (sinon défaut "villa") :

- Titre section devient "Bien utiliser votre **appartement**"
- Section piscine devient "**Piscines de la résidence**" (au lieu de "Votre piscine")
- Section piscine masquée totalement si `pool: null` (cas Savannah)

## Déploiement O2switch

Le site se build localement (`npm run build`) et le contenu de `dist/` est uploadé dans le Document Root du sous-domaine :

```
/home/mama4664/livrets.corailconciergerie.com.mama4664.odns.fr/
```

Méthodes possibles :
- Git push auto (si activé dans cPanel "Git Version Control")
- FTP / SFTP manuel
- Script auto à venir

## Contacts

- Claire (concierge) : +590 690 51 84 68 — contact@corailconciergerie.com
- Maxence (propriétaire / dev) : +33 6 60 46 80 28
