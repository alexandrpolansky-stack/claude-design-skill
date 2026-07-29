# Portfolio a work grid: hierarchie dlaždic a barva jako wayfinding

Nota řeší strukturu portfolio/case-study sekce (work grid, projektová galerie) — jak dát
mřížce projektů hierarchii a jak barva celé sekce nese víc než dekoraci. Otevři ji při stavbě
portfolia, agenturního webu nebo case-study přehledu, kdy hrozí, že grid vyjde jako uniformní
řada stejně velkých karet bez důrazu.

Sesterská nota: [Vizuální craft](vizualni-craft.md) (obecný rámec pojmenování pólu a
sebevědomého rozhodnutí, ze kterého tahle nota vychází).

**Zdroj jiného typu než zbytek knihovny.** Obě pravidla vychází z přímého pozorování tří
nezávisle nominovaných Awwwards webů (`warmnfuzzy.tv`, `forms.world`, `davidspaeth.com`),
otevřených živě přes Playwright 29. 7. 2026, ne z publikované studie nebo eseje praktika.
Malý vzorek (n=3), ale shoda napříč nezávislými weby je stejný typ argumentu jako shoda
napříč design systémy v jiných notách — jen s menším n. Označeno jako třída C.

## Použitelná pravidla

### Vlajková dlaždice: hierarchie, ne uniformní mřížka

**PRAVIDLO:** V portfolio/work gridu dej nejsilnějšímu nebo nejnovějšímu projektu výrazně
větší dlaždici než ostatním (asymetrická masonry mřížka), ne stejnou velikost všem. Obsah
dlaždic zámerně míchej typy (fotka, ilustrace/render, plochá barva s logem) — nenuť každou
dlaždici, aby byla "hero image".
**KDY PLATÍ:** portfolio, case-study přehled, agenturní work stránka s 5+ položkami.
**PROČ:** Uniformní mřížka bez hierarchie nutí diváka hodnotit všechny projekty stejně a nic
nevede oko k tomu nejdůležitějšímu. Warmnfuzzy.tv dává první, největší dlaždici svému aktuálně
nejsilnějšímu projektu (Velociti Elite 3, cca 60 % šířky prvního řádku) a zbytek řádku dělí na
menší dlaždice; ve druhém řádku míchá produktovou fotku, plochou brandovou barvu s logem
(ego life) a fotku billboardu v ulici (Elephant Valley) — tři různé režimy obsahu vedle sebe.
**TŘÍDA:** C (přímé pozorování 1 webu, screenshot 29. 7. 2026)
**ZDROJ:** živý screenshot warmnfuzzy.tv/work, 29. 7. 2026
**KDY NEPLATÍ:** portfolio, kde jsou všechny položky záměrně rovnocenné (např. klientská
case-study knihovna pro interní použití, ne marketingová prezentace) — tam uniformní mřížka
komunikuje nestrannost, což je žádoucí.

### Barva na celou sekci jako wayfinding a osobnost

**PRAVIDLO:** U vícestránkového/vícesekčního webu neomezuj brandovou barvu na malý akcent
(viz [Vizuální craft](vizualni-craft.md) pravidlo o vzácném akcentu) — u klíčových
sekcí/stránek (work, kontakt, kampaň) ji použij jako fullscreen pozadí celé sekce. Barva pak
funguje zároveň jako wayfinding (uživatel pozná, že je jinde) i jako moment osobnosti.
**KDY PLATÍ:** web s víc než jednou hlavní sekcí/stránkou (portfolio + work + kontakt), kde
má každá nést trochu jinou náladu, ale zůstat v jednom brandu.
**PROČ:** Warmnfuzzy.tv drží homepage v bílo-černé s barvou jen jako drobný akcent (viz
pravidlo o vzácném akcentu ve `vizualni-craft.md`), ale work stránka je celá v brandové
mustard žluté (`#f7dd47`, stejný odstín jako `theme-color` meta tag). Kontrast mezi
"vzácný akcent" na homepage a "plná barva" na work stránce je čitelný signál, že jde
o jinou část webu, ne jen dekorace.
**TŘÍDA:** C (přímé pozorování 1 webu, screenshot + CSS 29. 7. 2026)
**ZDROJ:** živý screenshot warmnfuzzy.tv (homepage vs. /work), CSS custom property
`theme-color: rgb(247, 221, 71)`, 29. 7. 2026
**KDY NEPLATÍ:** brand s jednou pevnou barvou napříč celým systémem (finance, zdravotnictví,
státní správa) — tam by barevná sekce působila nekonzistentně, ne jako wayfinding.

## Jak rozhodnout v praxi

1. Než postavíš grid, urči nejsilnější/nejnovější projekt — dostane výrazně větší dlaždici.
2. Namíchej typy obsahu dlaždic (foto/ilustrace/plochá barva+logo), nenuť jednotný vzhled.
3. Pokud má web víc hlavních sekcí, zvaž fullscreen brandovou barvu jako odlišení sekce,
   ne jen coby akcent.
4. Obojí drž jako VĚDOMÉ rozhodnutí (viz [Vizuální craft](vizualni-craft.md)), ne default.
