# Downloads curated Unsplash photos for restaurants, beaches, shop
# Unsplash License: free for commercial use, no attribution required.
$ErrorActionPreference = 'Stop'

$BASE = "https://images.unsplash.com/photo-"
$PARAMS = "?w=900&h=560&fit=crop&q=80&auto=format"

$photos = @(
    # ── RESTAURANTS ──
    @{ id="ogaiana"; photo="1414235077428-338989a2e8c0" }              # bistronomique plate
    @{ id="zagaya"; photo="1559339352-11d035aa65de" }                   # plat raffiné
    @{ id="jp-o-piano"; photo="1565299624946-b28f40a0ae38" }            # cuisine raffinée
    @{ id="seaside"; photo="1559329007-40df8a9345d8" }                  # marina vue mer
    @{ id="les-salines"; photo="1551218808-94e220e084d2" }              # créole plat
    @{ id="cafe-corail"; photo="1495474472287-4d71bcdd2085" }           # café vegan healthy bowl
    @{ id="rhumarin"; photo="1532634922-8fe0b757fb13" }                 # cocktail vue mer
    @{ id="poivrier"; photo="1414235077428-338989a2e8c0" }              # gastronomique
    @{ id="metis-cafe"; photo="1551218808-94e220e084d2" }               # bistrot chic
    @{ id="quai-17"; photo="1414235077428-338989a2e8c0" }               # brasserie
    @{ id="canne-a-sucre"; photo="1559339352-11d035aa65de" }            # langouste
    @{ id="mabouya"; photo="1551218808-94e220e084d2" }                  # cave a vin
    @{ id="byron-burgers"; photo="1568901346375-23c9450c58cd" }         # burger
    @{ id="jardin-secret"; photo="1551218808-94e220e084d2" }            # tapas cocktail
    @{ id="ti-coco"; photo="1559339352-11d035aa65de" }                  # plage grillades
    @{ id="ti-francine"; photo="1565299624946-b28f40a0ae38" }           # pizza
    @{ id="le-carre"; photo="1565299624946-b28f40a0ae38" }              # pizza salades
    @{ id="la-plage"; photo="1559339352-11d035aa65de" }                 # restaurant plage
    @{ id="cocotiers"; photo="1414235077428-338989a2e8c0" }             # creole buffet
    @{ id="mango-moulin"; photo="1546833999-b9f581a1996d" }             # gastronomique
    @{ id="le-colombo"; photo="1546833999-b9f581a1996d" }               # langouste creole
    @{ id="ti-tab-kreyol"; photo="1414235077428-338989a2e8c0" }         # créole maison
    @{ id="rhumerie-pirate"; photo="1414235077428-338989a2e8c0" }       # creole
    @{ id="porte-des-indes"; photo="1565557623684-de8e9aaa9617" }       # indien tandoori
    @{ id="ti-maki"; photo="1414235077428-338989a2e8c0" }               # fusion
    @{ id="sabino"; photo="1565299624946-b28f40a0ae38" }                # pizza
    @{ id="creodelice"; photo="1414235077428-338989a2e8c0" }            # traiteur
    @{ id="delices"; photo="1414235077428-338989a2e8c0" }               # comptoirs
)

$beaches = @(
    @{ id="raisins-clairs"; photo="1559827260-dc66d52bef19" }           # turquoise lagon
    @{ id="anse-tarare"; photo="1519046904884-53103b34b206" }           # sauvage tropicale
    @{ id="plage-du-bourg"; photo="1520454974749-611b7248ffdb" }        # plage village
    @{ id="caravelle"; photo="1507525428034-b723cf961d3e" }             # iconic palm+turquoise
    @{ id="anse-a-la-gourde"; photo="1535380644094-6671ee2c14e7" }      # lagon préservé
)

$shops = @(
    @{ id="corner-shop"; photo="1502680390469-be75c86b636f" }           # surf shop / board
)

# Activities photos (extras)
$activities = @(
    @{ id="petite-terre"; photo="1583398701666-8e4abe0e7b8e" }
    @{ id="marie-galante"; photo="1559827260-dc66d52bef19" }
    @{ id="desirade"; photo="1535380644094-6671ee2c14e7" }
    @{ id="plongee-cousteau"; photo="1530053969600-caed2596d242" }
    @{ id="kitesurf"; photo="1502680390469-be75c86b636f" }
    @{ id="pointe-des-chateaux"; photo="1583298581834-0e7af0c0cc1c" }
    @{ id="marche"; photo="1488459716781-31db52582fe9" }
    @{ id="golf"; photo="1535131749006-b7f58c99034b" }
    @{ id="damoiseau"; photo="1582106245687-cbb466a9f07f" }
    @{ id="jardin-deshaies"; photo="1466692476868-aef1dfb1e735" }
)

function Download-Set($set, $folder) {
    $dir = "C:\Users\Xensma\corail-livret\public\photos\$folder"
    New-Item -ItemType Directory -Path $dir -Force | Out-Null
    foreach ($item in $set) {
        $url = "$BASE$($item.photo)$PARAMS"
        $out = "$dir\$($item.id).jpg"
        try {
            Invoke-WebRequest -Uri $url -OutFile $out -UseBasicParsing -TimeoutSec 30
            Write-Host "OK $folder/$($item.id).jpg"
        } catch {
            Write-Host "FAIL $folder/$($item.id).jpg : $_"
        }
    }
}

Download-Set $photos "restos"
Download-Set $beaches "beaches"
Download-Set $shops "shops"
Download-Set $activities "activities"

Write-Host "`nDONE."
