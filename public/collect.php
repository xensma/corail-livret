<?php
// ─────────────────────────────────────────────────────────────────────────────
// Corail Conciergerie — Collecteur d'analytics maison (first-party).
// Reçoit un événement (page vue / clic sortant / événement nommé) et l'enregistre
// dans MySQL. SANS cookie, SANS stocker l'IP (visiteur = hash quotidien anonyme).
//
// Règle d'or : ne JAMAIS renvoyer d'erreur au client. Le livret ne doit jamais
// casser ni ralentir à cause de l'analytics → on répond 204 quoi qu'il arrive.
//
// Config (identifiants MySQL + sel) : fichier au-dessus du docroot, hors dépôt :
//   /home/mama4664/corail-db-config.php   (voir corail-db-config.sample.php)
// ─────────────────────────────────────────────────────────────────────────────

header('Cache-Control: no-store');

function done() { http_response_code(204); exit; }

// POST uniquement
if (($_SERVER['REQUEST_METHOD'] ?? 'GET') !== 'POST') { done(); }

// Filtre anti-bot basique (en plus du déclenchement JS qui élimine déjà la majorité)
$ua = $_SERVER['HTTP_USER_AGENT'] ?? '';
if ($ua === '' || preg_match('~bot|crawl|spider|slurp|bing|yandex|preview|monitor|curl|wget|python|headless|lighthouse~i', $ua)) { done(); }

// Corps JSON (taille bornée)
$raw = file_get_contents('php://input');
if ($raw === false || strlen($raw) > 4000) { done(); }
$d = json_decode($raw, true);
if (!is_array($d)) { done(); }

// Normalisation + validation
function field($v, $max) {
  $v = is_string($v) ? trim($v) : '';
  return function_exists('mb_substr') ? mb_substr($v, 0, $max, 'UTF-8') : substr($v, 0, $max);
}
$type = field($d['t'] ?? '', 16);
if (!in_array($type, ['pageview', 'outbound', 'event'], true)) { done(); }
$name   = field($d['n'] ?? '', 120);
$path   = field($d['p'] ?? '', 255) ?: '/';
$villa  = field($d['v'] ?? '', 80);
$locale = field($d['l'] ?? '', 5);
$url    = field($d['u'] ?? '', 512);
$ref    = field($d['r'] ?? '', 255);

// Config hors dépôt
$cfgPath = __DIR__ . '/../corail-db-config.php';
if (!is_file($cfgPath)) { done(); }
$cfg = require $cfgPath;
if (!is_array($cfg)) { done(); }

// Visiteur unique anonyme : hash quotidien (l'IP/UA ne sont JAMAIS stockés)
$ip      = $_SERVER['REMOTE_ADDR'] ?? '';
$day     = gmdate('Y-m-d');
$salt    = $cfg['salt'] ?? 'corail';
$visitor = substr(hash('sha256', $day . '|' . $ip . '|' . $ua . '|' . $salt), 0, 16);

try {
  $dsn = 'mysql:host=' . ($cfg['host'] ?? 'localhost') . ';dbname=' . ($cfg['db'] ?? '') . ';charset=utf8mb4';
  $pdo = new PDO($dsn, $cfg['user'] ?? '', $cfg['pass'] ?? '', [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_TIMEOUT => 3,
  ]);
  // Table créée à la volée (idempotent) → pas de script SQL à lancer à la main
  $pdo->exec(
    'CREATE TABLE IF NOT EXISTS events (
      id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
      ts DATETIME NOT NULL,
      day DATE NOT NULL,
      type VARCHAR(16) NOT NULL,
      name VARCHAR(120) NULL,
      path VARCHAR(255) NOT NULL,
      villa VARCHAR(80) NULL,
      locale VARCHAR(5) NULL,
      url VARCHAR(512) NULL,
      referrer VARCHAR(255) NULL,
      visitor CHAR(16) NOT NULL,
      KEY idx_day (day),
      KEY idx_villa (villa),
      KEY idx_type (type)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4'
  );
  $st = $pdo->prepare(
    'INSERT INTO events (ts, day, type, name, path, villa, locale, url, referrer, visitor)
     VALUES (UTC_TIMESTAMP(), :day, :type, :name, :path, :villa, :locale, :url, :ref, :visitor)'
  );
  $st->execute([
    ':day' => $day, ':type' => $type,
    ':name' => ($name !== '' ? $name : null),
    ':path' => $path,
    ':villa' => ($villa !== '' ? $villa : null),
    ':locale' => ($locale !== '' ? $locale : null),
    ':url' => ($url !== '' ? $url : null),
    ':ref' => ($ref !== '' ? $ref : null),
    ':visitor' => $visitor,
  ]);
} catch (Throwable $e) {
  // silencieux — on ne révèle rien et on ne casse rien
}

done();
