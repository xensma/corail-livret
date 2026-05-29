# Download Gwadatrip's actual hero images for the 10 excursions
$photos = @(
  @{ id="catamaran-iles-des-saintes"; url="https://images.unsplash.com/photo-1473186578172-c141e6798cf4?auto=format&fit=crop&w=1600&q=80" }
  @{ id="plongee-reserve-cousteau";    url="https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1600&q=80" }
  @{ id="saloon-boat-saint-francois";  url="https://images.unsplash.com/photo-1559827260-dc66d52bef19?auto=format&fit=crop&w=1600&q=80" }
  @{ id="jetski-petite-terre";         url="https://images.unsplash.com/photo-1520942702018-0862200e6873?auto=format&fit=crop&w=1600&q=80" }
  @{ id="observation-baleines";        url="https://images.unsplash.com/photo-1568430462989-44163eb1752f?auto=format&fit=crop&w=1600&q=80" }
  @{ id="canyoning-saut-acomat";       url="https://images.unsplash.com/photo-1433086966358-54859d0ed716?auto=format&fit=crop&w=1600&q=80" }
  @{ id="kayak-mangrove";              url="https://images.unsplash.com/photo-1502920917128-1aa500764cbd?auto=format&fit=crop&w=1600&q=80" }
  @{ id="ascension-soufriere";         url="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1600&q=80" }
  @{ id="chutes-du-carbet";            url="https://images.unsplash.com/photo-1432405972618-c60b0225b8f9?auto=format&fit=crop&w=1600&q=80" }
  @{ id="snorkeling-ilet-gosier";      url="https://images.unsplash.com/photo-1559827260-dc66d52bef19?auto=format&fit=crop&w=1600&q=80" }
)
$dest = "C:\Users\Xensma\corail-livret\public\photos\activities"
New-Item -ItemType Directory -Path $dest -Force | Out-Null
foreach ($p in $photos) {
  $out = "$dest\$($p.id).jpg"
  try {
    Invoke-WebRequest -Uri $p.url -OutFile $out -UseBasicParsing -TimeoutSec 30
    Write-Host "OK $($p.id).jpg ($(([System.IO.FileInfo]$out).Length / 1KB) KB)"
  } catch { Write-Host "FAIL $($p.id): $_" }
}
