<?php
// ─────────────────────────────────────────────────────────────────────────────
// Corail Conciergerie — Tableau de bord analytics (PROTÉGÉ par .htaccess Basic Auth,
// mêmes identifiants que la page d'accueil). Lecture seule de la table `events`.
// ─────────────────────────────────────────────────────────────────────────────
header('Content-Type: text/html; charset=utf-8');

$cfgPath = __DIR__ . '/../corail-db-config.php';
$err = null; $pdo = null;
if (!is_file($cfgPath)) {
  $err = "Configuration manquante : place le fichier corail-db-config.php au-dessus du docroot.";
} else {
  $cfg = require $cfgPath;
  try {
    $dsn = 'mysql:host=' . ($cfg['host'] ?? 'localhost') . ';dbname=' . ($cfg['db'] ?? '') . ';charset=utf8mb4';
    $pdo = new PDO($dsn, $cfg['user'] ?? '', $cfg['pass'] ?? '', [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
  } catch (Throwable $e) { $err = "Connexion à la base impossible. Vérifie corail-db-config.php."; }
}

$days  = isset($_GET['days']) ? max(1, min(365, (int)$_GET['days'])) : 30;
$since = gmdate('Y-m-d', time() - ($days - 1) * 86400);

function qall($pdo, $sql, $args = []) { $st = $pdo->prepare($sql); $st->execute($args); return $st->fetchAll(PDO::FETCH_ASSOC); }
function one($pdo, $sql, $args = []) { $r = qall($pdo, $sql, $args); return (int)($r[0]['c'] ?? 0); }
function h($s) { return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); }

$kpi = ['pv' => 0, 'visitors' => 0, 'outbound' => 0, 'events' => 0];
$perVilla = []; $topOut = []; $byEvent = []; $daily = [];
if ($pdo && !$err) {
  try {
    $kpi['pv']       = one($pdo, "SELECT COUNT(*) c FROM events WHERE type='pageview' AND day>=?", [$since]);
    $kpi['visitors'] = one($pdo, "SELECT COUNT(DISTINCT visitor) c FROM events WHERE day>=?", [$since]);
    $kpi['outbound'] = one($pdo, "SELECT COUNT(*) c FROM events WHERE type='outbound' AND day>=?", [$since]);
    $kpi['events']   = one($pdo, "SELECT COUNT(*) c FROM events WHERE type='event' AND day>=?", [$since]);
    $perVilla = qall($pdo, "SELECT COALESCE(villa,'(accueil)') villa, COUNT(*) pv, COUNT(DISTINCT visitor) v
                            FROM events WHERE type='pageview' AND day>=? GROUP BY villa ORDER BY pv DESC", [$since]);
    $topOut   = qall($pdo, "SELECT url, COUNT(*) c FROM events WHERE type='outbound' AND day>=? AND url IS NOT NULL
                            GROUP BY url ORDER BY c DESC LIMIT 25", [$since]);
    $byEvent  = qall($pdo, "SELECT name, COUNT(*) c FROM events WHERE type='event' AND day>=? AND name IS NOT NULL
                            GROUP BY name ORDER BY c DESC", [$since]);
    $daily    = qall($pdo, "SELECT day, COUNT(*) c FROM events WHERE type='pageview' AND day>=? GROUP BY day ORDER BY day", [$since]);
  } catch (Throwable $e) {
    $err = "Aucune donnée pour l'instant (la table sera créée au premier événement reçu).";
  }
}
$maxDaily = 1; foreach ($daily as $r) { $maxDaily = max($maxDaily, (int)$r['c']); }
function shorten($u, $n = 60) {
  $len = function_exists('mb_strlen') ? mb_strlen($u) : strlen($u);
  if ($len <= $n) return $u;
  return (function_exists('mb_substr') ? mb_substr($u, 0, $n) : substr($u, 0, $n)) . '…';
}
?>
<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Stats — Corail Conciergerie</title>
<style>
  :root { --turq:#5BA8A2; --turqd:#3E7C77; --ink:#1F2A2E; --cream:#F5F2ED; --sand:#D9CDB4; --accent:#E08A5B; }
  * { box-sizing:border-box; }
  body { margin:0; font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif; background:var(--cream); color:var(--ink); }
  .wrap { max-width:1000px; margin:0 auto; padding:24px 18px 60px; }
  header { display:flex; align-items:baseline; justify-content:space-between; flex-wrap:wrap; gap:10px; margin-bottom:8px; }
  h1 { font-size:22px; margin:0; }
  h1 small { color:var(--turqd); font-weight:600; font-size:13px; text-transform:uppercase; letter-spacing:.12em; display:block; }
  .period a { display:inline-block; padding:6px 12px; margin-left:6px; border-radius:999px; text-decoration:none; font-size:13px; color:var(--ink); background:#fff; border:1px solid #0001; }
  .period a.on { background:var(--turq); color:#fff; }
  .note { background:#fff; border:1px solid var(--sand); border-radius:12px; padding:14px 16px; margin:14px 0; color:#000a; }
  .kpis { display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin:18px 0; }
  .kpi { background:#fff; border:1px solid #0001; border-radius:14px; padding:16px; }
  .kpi b { display:block; font-size:30px; line-height:1.1; }
  .kpi span { font-size:12px; text-transform:uppercase; letter-spacing:.08em; color:#0008; }
  .card { background:#fff; border:1px solid #0001; border-radius:14px; padding:18px; margin:16px 0; }
  .card h2 { font-size:15px; margin:0 0 12px; text-transform:uppercase; letter-spacing:.08em; color:var(--turqd); }
  table { width:100%; border-collapse:collapse; font-size:14px; }
  th,td { text-align:left; padding:7px 8px; border-bottom:1px solid #0001; }
  th { font-size:11px; text-transform:uppercase; letter-spacing:.06em; color:#0007; }
  td.num,th.num { text-align:right; font-variant-numeric:tabular-nums; }
  td a { color:var(--turqd); text-decoration:none; word-break:break-all; }
  .chart { display:flex; align-items:flex-end; gap:3px; height:120px; }
  .chart .bar { flex:1; background:var(--turq); border-radius:3px 3px 0 0; min-height:2px; position:relative; }
  .chart .bar:hover::after { content:attr(data-l); position:absolute; bottom:100%; left:50%; transform:translateX(-50%); white-space:nowrap; background:var(--ink); color:#fff; font-size:11px; padding:2px 6px; border-radius:4px; margin-bottom:4px; }
  .muted { color:#0007; font-size:13px; }
  @media (max-width:640px){ .kpis{grid-template-columns:repeat(2,1fr);} }
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1><small>Corail Conciergerie</small>Statistiques des livrets</h1>
    <div class="period">
      <?php foreach ([7,30,90] as $d): ?>
        <a class="<?= $d===$days?'on':'' ?>" href="?days=<?= $d ?>"><?= $d ?> j</a>
      <?php endforeach; ?>
    </div>
  </header>
  <p class="muted">Période : <?= h($days) ?> derniers jours (depuis le <?= h($since) ?>). Sans cookie, données anonymisées.</p>

  <?php if ($err): ?>
    <div class="note">⚠ <?= h($err) ?></div>
  <?php endif; ?>

  <div class="kpis">
    <div class="kpi"><b><?= number_format($kpi['pv'],0,',',' ') ?></b><span>Pages vues</span></div>
    <div class="kpi"><b><?= number_format($kpi['visitors'],0,',',' ') ?></b><span>Visiteurs uniques</span></div>
    <div class="kpi"><b><?= number_format($kpi['outbound'],0,',',' ') ?></b><span>Clics sortants</span></div>
    <div class="kpi"><b><?= number_format($kpi['events'],0,',',' ') ?></b><span>Événements</span></div>
  </div>

  <?php if ($daily): ?>
  <div class="card">
    <h2>Pages vues par jour</h2>
    <div class="chart">
      <?php foreach ($daily as $r): $hgt = round(((int)$r['c'] / $maxDaily) * 116) + 2; ?>
        <div class="bar" style="height:<?= $hgt ?>px" data-l="<?= h($r['day']) ?> · <?= h($r['c']) ?>"></div>
      <?php endforeach; ?>
    </div>
  </div>
  <?php endif; ?>

  <div class="card">
    <h2>Par villa</h2>
    <?php if ($perVilla): ?>
    <table>
      <tr><th>Villa</th><th class="num">Pages vues</th><th class="num">Visiteurs</th></tr>
      <?php foreach ($perVilla as $r): ?>
        <tr><td><?= h($r['villa']) ?></td><td class="num"><?= h($r['pv']) ?></td><td class="num"><?= h($r['v']) ?></td></tr>
      <?php endforeach; ?>
    </table>
    <?php else: ?><p class="muted">Pas encore de données.</p><?php endif; ?>
  </div>

  <div class="card">
    <h2>Top liens cliqués (excursions, restos, cartes, WhatsApp…)</h2>
    <?php if ($topOut): ?>
    <table>
      <tr><th>Lien</th><th class="num">Clics</th></tr>
      <?php foreach ($topOut as $r): ?>
        <tr><td><a href="<?= h($r['url']) ?>" target="_blank" rel="noopener"><?= h(shorten($r['url'])) ?></a></td><td class="num"><?= h($r['c']) ?></td></tr>
      <?php endforeach; ?>
    </table>
    <?php else: ?><p class="muted">Aucun clic sortant enregistré pour l'instant.</p><?php endif; ?>
  </div>

  <div class="card">
    <h2>Événements (PDF, WhatsApp, appel…)</h2>
    <?php if ($byEvent): ?>
    <table>
      <tr><th>Événement</th><th class="num">Nombre</th></tr>
      <?php foreach ($byEvent as $r): ?>
        <tr><td><?= h($r['name']) ?></td><td class="num"><?= h($r['c']) ?></td></tr>
      <?php endforeach; ?>
    </table>
    <?php else: ?><p class="muted">Aucun événement enregistré pour l'instant.</p><?php endif; ?>
  </div>
</div>
</body>
</html>
