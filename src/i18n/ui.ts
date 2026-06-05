export type Locale = 'fr' | 'en';

export const ui = {
  fr: {
    // Hero
    welcomeAbove: 'Bienvenue chez vous',
    langFR: 'FR',
    langEN: 'EN',

    // Section: Votre maison
    kVotreMaison: 'Votre maison',
    tToutSavoir: 'Tout savoir sur',
    hEquipements: 'Équipements',
    lVotreSejour: 'Votre séjour',
    lCheckin: 'Check-in',
    lCheckinPrefix: 'dès',
    lCheckout: 'Check-out',
    lCheckoutPrefix: 'avant',
    lCapacite: 'Capacité',
    lPersAbbr: 'pers',
    lChAbbr: 'ch',
    lSdbAbbr: 'sdb',
    lAProximite: 'À proximité',
    lMinutes: 'min',
    lLocalisation: 'Localisation',
    lAdresse: 'Adresse',
    btnOuvrirMaps: 'Ouvrir dans Maps →',
    lAPied: 'à pied',
    lDeLaVilla: 'de la villa',

    // Section: WiFi
    kConnexion: 'Connexion',
    tWifi: 'WiFi',
    hConnexionInternet: 'Connexion internet',
    lReseau: 'Réseau',
    lMotDePasse: 'Mot de passe',
    btnCopier: 'Copier',
    btnCopie: '✓ Copié',
    lScannerWifi: 'Scanner pour\nse connecter',

    // Section: Sécurité
    kSecurite: 'Sécurité',
    tPortailCles: 'Portail & clés',
    hPortailResidence: 'Portail résidence',
    lDigicodeVoiture: 'Digicode voiture',
    lPortillonPieton: 'Portillon piéton',
    hCles: 'Clés',

    // Section: Bien utiliser
    kAuQuotidien: 'Au quotidien',
    tBienUtiliser: 'Bien utiliser votre villa',
    tBienUtiliserApt: 'Bien utiliser votre appartement',
    tPiscinesResidence: 'Piscines de la résidence',
    lTV: 'TV & multimédia',
    lCafetiere: 'Cafetière',
    lClimatisation: 'Climatisation',
    lEauPotable: 'Eau potable',
    lFosseSeptique: 'Fosse septique',
    lKidsTitle: 'Pour les enfants',
    lKidsBadge: 'Jeux de plage pour enfants',
    lKidsGames: 'Un panier de jeux de plage — ballon, pelle, seaux, râteaux, moules et bouées — est à votre disposition.',
    lKidsCare: 'Merci de les rincer à l\'eau douce après la plage, pour les prochains petits hôtes 🌊',
    lPoolKey: '🟢 Vert = piscine protégée · 🔴 Rouge = alarme désactivée',
    lPoolCodeLabel: 'Code alarme :',
    lPoolMagnetBefore: 'Avant la baignade : passez l\'aimant (porte-clé près de la piscine) sur le symbole « Baigneur » jusqu\'au bip → le voyant passe au rouge 🔴.',
    lPoolMagnetAfter: 'En sortant de l\'eau : l\'alarme se réarme seule dès que l\'eau est calme → voyant vert 🟢. Pour accélérer, repassez l\'aimant sur le « Baigneur ».',
    lPoolCodeBefore: 'Avant la baignade : tapez le code de l\'alarme sur le clavier de la centrale → le voyant passe au rouge 🔴.',
    lPoolCodeAfter: 'En sortant de l\'eau : l\'alarme se réarme seule dès que l\'eau est calme → voyant vert 🟢. Pour accélérer, appuyez 2× sur OK.',
    lPoolBarrier: 'Barrière de sécurité « Beethoven » installée autour du bassin. Refermez et verrouillez toujours le portillon derrière vous, surtout avec des enfants.',
    lPoolWatch: 'Aucun dispositif ne remplace la surveillance : ne quittez jamais des yeux les enfants près du bassin.',
    lAlerteCyclone: 'Alerte cyclonique',

    // Section: Piscine
    kDetente: 'Détente',
    tVotrePiscine: 'Votre piscine',
    lAlarme: '⚠ Sécurité du bassin',
    lBonnesPratiques: 'Bonnes pratiques',
    lEntretien: 'Entretien',

    // Section: Tri sélectif
    kEcoTips: 'Éco-tips Guadeloupe',
    tTriSelectif: 'Tri sélectif',
    lOrdures: 'Ordures ménagères',
    lTriJaune: 'Tri (jaune)',
    lVerre: 'Verre',

    // Section: Bébettes
    kVieTropiques: 'La vie sous les tropiques',
    tBebettes: 'Nos bébettes',
    hNosAmis: 'Nos amis',
    hMoinsAimes: 'Les moins aimés',

    // Section: Règles + départ
    kSavoirVivre: 'Bon savoir-vivre',
    tReglesDepart: 'Quelques règles & jour du départ',
    hReglesMaison: 'Règles de maison',
    hJourDepart: 'Jour du départ — 10h',

    // Section: Urgences
    kEnCasDePepin: 'En cas de pépin',
    tUrgences: 'Urgences',
    hEnCasUrgence: "En cas d'urgence",
    hNumerosUtiles: 'Numéros utiles',

    // Section: Services Corail
    kPrestationsPremium: 'Nos prestations premium',
    tServicesCorail: 'Services Corail Conciergerie',
    sServicesIntro: 'Tout ce qu\'il vous faut pour vivre la meilleure expérience pendant votre séjour.',
    btnReserverWA: 'Réserver via WhatsApp →',

    // Section: Restaurants
    kSaveursLocales: 'Saveurs locales',
    tRestaurants: 'Restaurants à Saint-François',
    sRestaurants: 'Notre sélection regroupée par direction — du bistronomique étoilé à la cuisine créole familiale.',
    lSpecialite: 'Spécialité.',
    btnAppeler: 'Appeler',
    btnItineraire: 'Itinéraire',
    btnReserver: 'Réserver',

    // Section: Activités
    kAFaireAbsolument: 'Sélection Gwadatrip × Corail',
    tIncontournables: 'Les incontournables',
    sIncontournables: 'Notre sélection premium d\'excursions sur Gwadatrip — testées, sélectionnées et garanties par Corail Conciergerie. Réservation directe, annulation gratuite jusqu\'à 48h avant.',
    kEtAussi: 'Et aussi',
    tAutresExperiences: 'Autres expériences',
    lDuree: 'Durée',
    lDepart: 'Départ',
    lIncontournable: '★ Incontournable',
    lGratuit: 'Gratuit',
    lFromPrice: 'dès',
    lPerPerson: '/pers',
    lDifficulte: 'Niveau',
    lReviews: 'avis',
    lGroupSize: 'Groupe',
    btnReserverGwada: 'Réserver sur Gwadatrip →',
    btnEnSavoirPlus: 'En savoir plus →',
    lCoupDeCoeur: 'Notre coup de cœur',
    sGwadatripPower: 'Réservation sécurisée via gwadatrip.com — partenaire officiel Corail Conciergerie',
    // Section "Suggestions Corail"
    kBonsPlans: 'Bons plans Corail',
    tSuggestions: 'À faire vous-même',
    sSuggestions: "Des incontournables que vous organisez vous-même. Nous vous donnons les bonnes adresses, à vous le rythme.",
    sSuggestionsFooter: 'Liens vers les sites officiels — réservation directe selon l\'organisme.',

    // Section: Plages
    kSelEtSable: 'Le sel et le sable',
    tPlages: 'Nos plages préférées',
    sPlages: 'De la plus proche (2 min) à la plus sauvage.',
    lMeilleurMoment: 'Meilleur moment',
    lServices: 'Services',
    btnYAller: 'Y aller',
    kSargasses: 'Sargasses, soyons honnêtes',
    sSargasses: 'Selon les saisons, des algues arrivent et repartent au gré des marées — rien de grave. Les plages orientées Nord/Nord-Est restent toujours préservées (Anse à la Gourde, Salines, Souffleur, Deshaies). Saint-François et Sainte-Anne organisent un ramassage réactif.',

    // Section: Boutiques
    kLifestyle: 'Lifestyle',
    tBoutiques: 'Boutiques & surf',
    sBoutiques: 'Nos adresses repérées à Saint-François pour le shopping et la glisse.',
    lHoraires: 'Horaires',
    btnVoirSite: 'Voir le site',

    // Section: Services pratiques
    kLeQuotidien: 'Le quotidien',
    tServicesPratiques: 'Courses, pharmacie, santé',

    // Reviews + Footer
    tMerci: 'Merci.',
    kPourVotreAvis: 'Pour votre avis',
    sReviews: 'Nous serions heureux de lire votre ressenti sur votre séjour à',
    sReviewsEnd: 'Quelques minutes pour nous laisser un avis : un grand merci !',
    btnAvisGoogle: 'Avis Google',
    btnFacebook: 'Facebook',
    btnInstagram: 'Instagram',
    lGuadeloupe: 'Saint François FWI',
    sAVite: 'À très vite.',

    // ContactBar
    lVotreConciergerie: 'Votre conciergerie',
    lCorail7j7: 'Corail Conciergerie · 7j/7',
    btnWhatsApp: 'WhatsApp',
    waMessage: 'Bonjour Corail Conciergerie, je suis en séjour à',

    // Distances modes
    modeVoiture: 'voiture',
    modePied: 'à pied',

    // Index page
    indexTitle: 'Livrets d\'accueil numériques',
    indexSubtitle: 'Sélectionnez votre villa pour accéder à votre livret personnalisé.',
    indexStatusLive: 'Disponible',
    indexStatusPending: 'À venir',
    indexCTA: 'Ouvrir le livret →'
  },

  en: {
    // Hero
    welcomeAbove: 'Welcome home',
    langFR: 'FR',
    langEN: 'EN',

    // Section: Your home
    kVotreMaison: 'Your home',
    tToutSavoir: 'All about',
    hEquipements: 'Amenities',
    lVotreSejour: 'Your stay',
    lCheckin: 'Check-in',
    lCheckinPrefix: 'from',
    lCheckout: 'Check-out',
    lCheckoutPrefix: 'before',
    lCapacite: 'Capacity',
    lPersAbbr: 'guests',
    lChAbbr: 'BR',
    lSdbAbbr: 'BA',
    lAProximite: 'Nearby',
    lMinutes: 'min',
    lLocalisation: 'Location',
    lAdresse: 'Address',
    btnOuvrirMaps: 'Open in Maps →',
    lAPied: 'walk',
    lDeLaVilla: 'from the villa',

    // Section: WiFi
    kConnexion: 'Stay connected',
    tWifi: 'WiFi',
    hConnexionInternet: 'Internet connection',
    lReseau: 'Network',
    lMotDePasse: 'Password',
    btnCopier: 'Copy',
    btnCopie: '✓ Copied',
    lScannerWifi: 'Scan to\nconnect',

    // Section: Security
    kSecurite: 'Security',
    tPortailCles: 'Gate & keys',
    hPortailResidence: 'Residence gate',
    lDigicodeVoiture: 'Vehicle keypad',
    lPortillonPieton: 'Pedestrian gate',
    hCles: 'Keys',

    // Section: Daily use
    kAuQuotidien: 'Daily essentials',
    tBienUtiliser: 'Using your villa well',
    tBienUtiliserApt: 'Using your apartment well',
    tPiscinesResidence: 'Residence pools',
    lTV: 'TV & media',
    lCafetiere: 'Coffee maker',
    lClimatisation: 'Air conditioning',
    lEauPotable: 'Drinking water',
    lFosseSeptique: 'Septic tank',
    lKidsTitle: 'For the kids',
    lKidsBadge: 'Beach toys for kids',
    lKidsGames: 'A basket of beach toys — ball, shovel, buckets, rakes, sand moulds and floats — is at your disposal.',
    lKidsCare: 'Please rinse them with fresh water after the beach, for the next little guests 🌊',
    lPoolKey: '🟢 Green = pool protected · 🔴 Red = alarm off',
    lPoolCodeLabel: 'Alarm code:',
    lPoolMagnetBefore: 'Before swimming: hold the magnet (key fob near the pool) over the "Swimmer" symbol until it beeps → the light turns red 🔴.',
    lPoolMagnetAfter: 'When you get out: the alarm re-arms by itself once the water is calm → green light 🟢. To speed it up, pass the magnet over the "Swimmer" again.',
    lPoolCodeBefore: 'Before swimming: enter the alarm code on the keypad → the light turns red 🔴.',
    lPoolCodeAfter: 'When you get out: the alarm re-arms by itself once the water is calm → green light 🟢. To speed it up, press OK twice.',
    lPoolBarrier: 'A "Beethoven" safety fence surrounds the pool. Always close and latch the gate behind you, especially with children.',
    lPoolWatch: 'No device replaces supervision: never take your eyes off children near the pool.',
    lAlerteCyclone: 'Cyclone alert',

    // Section: Pool
    kDetente: 'Relax',
    tVotrePiscine: 'Your pool',
    lAlarme: '⚠ Pool safety',
    lBonnesPratiques: 'Best practices',
    lEntretien: 'Maintenance',

    // Section: Recycling
    kEcoTips: 'Eco-tips Guadeloupe',
    tTriSelectif: 'Recycling',
    lOrdures: 'Household waste',
    lTriJaune: 'Recyclables (yellow)',
    lVerre: 'Glass',

    // Section: Critters
    kVieTropiques: 'Life in the tropics',
    tBebettes: 'Our critters',
    hNosAmis: 'Our friends',
    hMoinsAimes: 'The less loved',

    // Section: Rules + departure
    kSavoirVivre: 'House etiquette',
    tReglesDepart: 'A few rules & departure day',
    hReglesMaison: 'House rules',
    hJourDepart: 'Departure day — 10am',

    // Section: Emergency
    kEnCasDePepin: 'If something happens',
    tUrgences: 'Emergencies',
    hEnCasUrgence: 'In an emergency',
    hNumerosUtiles: 'Useful numbers',

    // Section: Corail Services
    kPrestationsPremium: 'Our premium services',
    tServicesCorail: 'Corail Concierge services',
    sServicesIntro: 'Everything you need for the best possible holiday.',
    btnReserverWA: 'Book via WhatsApp →',

    // Section: Restaurants
    kSaveursLocales: 'Local flavours',
    tRestaurants: 'Restaurants in Saint-François',
    sRestaurants: 'Our hand-picked selection grouped by direction — from starred bistros to family-run Creole.',
    lSpecialite: 'Speciality.',
    btnAppeler: 'Call',
    btnItineraire: 'Directions',
    btnReserver: 'Book',

    // Section: Activities
    kAFaireAbsolument: 'A Gwadatrip × Corail selection',
    tIncontournables: 'The essentials',
    sIncontournables: 'Our hand-picked premium excursions on Gwadatrip — tested, selected and guaranteed by Corail Concierge. Direct booking, free cancellation up to 48h before.',
    kEtAussi: 'And also',
    tAutresExperiences: 'Other experiences',
    lDuree: 'Duration',
    lDepart: 'Departure',
    lIncontournable: '★ Must-do',
    lGratuit: 'Free',
    lFromPrice: 'from',
    lPerPerson: '/person',
    lDifficulte: 'Level',
    lReviews: 'reviews',
    lGroupSize: 'Group',
    btnReserverGwada: 'Book on Gwadatrip →',
    btnEnSavoirPlus: 'Learn more →',
    lCoupDeCoeur: 'Our favourite',
    sGwadatripPower: 'Secure booking via gwadatrip.com — official Corail Concierge partner',
    // Section "Corail Picks"
    kBonsPlans: 'Corail picks',
    tSuggestions: 'Explore on your own',
    sSuggestions: "Must-sees you organise yourself. We give you the best addresses, you set the pace.",
    sSuggestionsFooter: 'Links go to official sources — bookings handled by each operator.',

    // Section: Beaches
    kSelEtSable: 'Salt & sand',
    tPlages: 'Our favourite beaches',
    sPlages: 'From the closest (2 min) to the wildest.',
    lMeilleurMoment: 'Best time',
    lServices: 'Facilities',
    btnYAller: 'Go there',
    kSargasses: 'Sargassum, let\'s be honest',
    sSargasses: 'Depending on the season, seaweed comes and goes with the tides — nothing serious. North/North-East facing beaches stay clear year-round (Anse à la Gourde, Salines, Souffleur, Deshaies). Saint-François and Sainte-Anne organise reactive clean-ups.',

    // Section: Shops
    kLifestyle: 'Lifestyle',
    tBoutiques: 'Shops & surf',
    sBoutiques: 'Our picks in Saint-François for shopping and watersports.',
    lHoraires: 'Hours',
    btnVoirSite: 'Visit website',

    // Section: Daily services
    kLeQuotidien: 'Day-to-day',
    tServicesPratiques: 'Groceries, pharmacy, health',

    // Reviews + Footer
    tMerci: 'Thank you.',
    kPourVotreAvis: 'For your review',
    sReviews: 'We would love to hear your thoughts on your stay at',
    sReviewsEnd: 'A few minutes to leave us a review — a huge thank you !',
    btnAvisGoogle: 'Google review',
    btnFacebook: 'Facebook',
    btnInstagram: 'Instagram',
    lGuadeloupe: 'Saint François FWI',
    sAVite: 'See you soon.',

    // ContactBar
    lVotreConciergerie: 'Your concierge',
    lCorail7j7: 'Corail Concierge · 7 days a week',
    btnWhatsApp: 'WhatsApp',
    waMessage: 'Hello Corail, I\'m staying at',

    // Distances modes
    modeVoiture: 'drive',
    modePied: 'on foot',

    // Index page
    indexTitle: 'Digital welcome books',
    indexSubtitle: 'Select your villa to access your personalised guide.',
    indexStatusLive: 'Available',
    indexStatusPending: 'Coming soon',
    indexCTA: 'Open guide →'
  }
} as const;

export type UIKey = keyof typeof ui.fr;

export function t(locale: Locale, key: UIKey): string {
  return (ui[locale] && ui[locale][key]) || ui.fr[key];
}

/**
 * Get a translated field from a data item with optional i18n overrides.
 * Falls back to the FR field if no translation is provided.
 */
export function tField<T extends Record<string, any>>(
  item: T,
  field: keyof T & string,
  locale: Locale
): any {
  if (locale === 'fr') return item[field];
  const i18n = (item as any).i18n;
  if (i18n && i18n[locale] && i18n[locale][field] !== undefined) {
    return i18n[locale][field];
  }
  return item[field];
}
