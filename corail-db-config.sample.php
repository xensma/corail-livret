<?php
// ─────────────────────────────────────────────────────────────────────────────
// MODÈLE de configuration de la base analytics.
//
// ▶ À FAIRE (une seule fois) :
//   1. Dans cPanel O2switch → « Bases de données MySQL » : crée une base
//      (ex. mama4664_corail_stats), un utilisateur, un mot de passe, et donne
//      à l'utilisateur TOUS les privilèges sur cette base.
//   2. Copie ce fichier, renomme-le « corail-db-config.php », remplis les
//      valeurs ci-dessous, puis dépose-le dans  /home/mama4664/  (c.-à-d.
//      JUSTE AU-DESSUS du dossier du site, PAS dans le site).
//      → Il ne sera ni déployé, ni accessible par le web.
//   3. Génère un « sel » aléatoire long (n'importe quelle longue chaîne) :
//      il sert à anonymiser les visiteurs. Ne le change plus ensuite.
// ─────────────────────────────────────────────────────────────────────────────

return [
  'host' => 'localhost',
  'db'   => 'mama4664_corail_stats',   // ← nom EXACT de ta base cPanel
  'user' => 'mama4664_corail',         // ← utilisateur MySQL
  'pass' => 'REMPLACE_PAR_TON_MDP',    // ← mot de passe MySQL
  'salt' => 'REMPLACE_PAR_UNE_LONGUE_CHAINE_ALEATOIRE_SECRETE',
];
