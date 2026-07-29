
# NotebookLM destilát – zdroj pravdy pro sheets-design skill

> [!important] Domácí pravidlo přebíjí obecný výzkum: GRIDLINES ZŮSTÁVAJÍ VIDITELNÉ
> Obecný dataviz výzkum níže (Tufte, data-ink ratio) doporučuje gridlines skrývat.
> Pro TrustSoft tabulky to NEPLATÍ. Existující reporty (Access Overview a spol.)
> gridlines mají; nový list, který je skryje, vypadá cize a nesedne k ostatním.
> Nikdy nevolej `hide_gridlines` / `setHiddenGridlines(true)` na TrustSoft listech.
> Zbytek doporučení (whitespace místo tlustých borderů, max 1 px linky) platí dál.


> Notebook „Transforming Google Sheets into Professional Visual Dashboards" (~81 aktivních zdrojů).
> Tohle je **zdroj pravdy** pro obsah skillu (rozhodnutí session 2026-07-16: `.gs` styler vynechán, obsah stojí na NotebookLM extrakci).
> Sběr je iterativní. Skill se staví AŽ po dostatečné znalosti (chápat co/proč/kdy, ne jen recepty). Gate na build = Alex.

## Co ještě chybí (proto stavíme dál)
Kola 1-2 dala **recepty a čísla** (co a jak). Chybí **rozhodovací logika a zdůvodnění**: kdy použít KPI kartu vs graf vs tabulku, kdy Drawing-layer vs formát buněk vs pixel-grid, proč zrovna tahle paleta pro tenhle typ čtenáře, proč se vyhnout hue H40-H120 atd. + detailní rozbor user cases (archetypy reportů). To je kolo 3.

---

## Kolo 1 – 6 sekcí (principy → anti-patterny)

### 1. Principy (proč to vypadá dobře)
- **Hierarchie:** škálování velikosti písma (H1/H2/tělo) vede oko a snižuje kognitivní zátěž.
- **60-30-10:** 60 % neutrál pozadí, 30 % primární, 10 % kontrast/CTA (vysoká saturace pro „pop").
- **Typografie:** čisté bezpatkové fonty (Roboto, Lato, Montserrat) = čitelnost na obrazovce, moderní, důvěra.
- **Whitespace:** mezery eliminují šum, obsah „dýchá", působí prémiově.
- **KPI karty:** obří čísla nahoře/vlevo sdělí výsledek okamžitě, bez luštění dat.
- **Gestalt (seskupení):** blízkost + společný podklad = vnímáno jako skupina, odpadá potřeba tlustých čar.

### 2. Konkrétní Sheets techniky (kde v UI)
- **Skrýt gridlines:** Zobrazit → Zobrazit → Mřížka (odškrtnout). Čisté plátno jako web.
- **Tmavé hlavičky:** tmavá výplň + bílý tučný text + sloučené buňky do širokého bloku.
- **KPI dlaždice:** slouč čtverec (Formát → Sloučit), metrika nahoru-doleva, bez desetin, font 35+.
- **Drawing-layer trik:** Vložit → Nákres → barevné tvary vložit jako vrstvu nad mřížku jako podklad grafů.
- **Transparentní grafy:** 2x klik → Přizpůsobit → Styl grafu → Barva pozadí = Žádná + zrušit ohraničení.
- **Podmíněné formátování:** Formát → Podmíněné formátování → barevné škály (heatmapa) nebo vlastní vzorec pro stav.
- **Named/protected ranges:** Data → Pojmenované rozsahy; Data → Chránit listy a rozsahy (zámek vzorců).
- **Dropdown/slicer:** Data → Ověření dat (dropdown); Data → Přidat průřez (interaktivní filtr grafů).

### 3. Strop Google Sheets (co neumí + čím nahradit)
- **Neumí nativně:** skutečně zaoblené rohy, měkké stíny, pill tvary.
- **Náhrada:** Vložit → Nákres (vektorové tvary se stínem, vložit nad buňky). Alt.: pixel-grid – zmenšit řádky/sloupce na čtverce (25x25 px) a „kreslit" barvou buněk přesné bloky.

### 4. Postup stavby
- **Čtenář:** začni cílovým uživatelem, jeho technická úroveň, konkrétní byznys otázky.
- **Metriky:** stáhni data, prozkoumej (QUERY, pivot), ověř že máš čím otázky zodpovědět a vytvořit KPI.
- **Layout:** oddělené listy Data / Výpočty (Workings/Staging) / Prezentace (Dashboard), oddělené prázdnými barevnými listy. Mockup nanečisto.
- **Styl:** hlavička, 60-30-10, 1-2 fonty, grafy, skryté gridlines.
- **Kontrola:** odstup, pauza, nech někoho jiného otestovat srozumitelnost a ořízni zbytečnosti.

### 5. Checklist před odevzdáním
- Welcome list s návodem, kam klikat?
- Gridlines VIDITELNÉ (domácí pravidlo přebíjí obecné doporučení výše)?
- Striktní rozdělení Vstupy / Výpočty / Prezentace do záložek?
- Buňky se vzorci zamčené proti přepisu?
- Jeden výpočet jen jednou, zbytek se odkazuje?
- Konstanty (sazby, cíle) na dedikovaném Settings listu?
- Barvy konzistentní dle palety; importovaná data vždy jednou barvou?

### 6. Anti-patterny / slop (signál → čím nahradit)
- 3D/pseudo-3D grafy → čistý flat design, 2D grafy, plné barvy.
- Tlusté černé ohraničení všude → whitespace, jemné šedé linky, zarovnání sloupců.
- Balastní desetinná místa u velkých čísel → zaokrouhlit na tisíce/miliony.
- Barevná exploze (duha) + neprofi font (Comic Sans) → profi font, odstíny jedné barvy, odlišná barva JEN pro extrém/cíl.

---

## Kolo 2 – konkrétní čísla, pojmenované metody, HEX palety

### Přesné hodnoty a rozměry
**Typografická škála (pt):** H1 32 tučně / H2 24 polotučné / H3 20 medium / podnadpis 18 regular / tělo+tlačítka 16 / popisky 14 / absolutní minimum terciár 12 pt. Light řezy nikdy pod 8 px.
- KPI „Scorecard" metrika přímo v Sheets: velikost 16.
- V datových tabulkách se drž mezi 10 a 14 (nejít pod 10, ne nad 14).

**Výška řádků a mřížka:**
- Line-height těla textu přesně 140-150 % velikosti písma.
- Oddělovací linka v hlavičce dashboardu: výška 3 px.
- Kreslící grid (Sheet Metricz postup): řádky 30 px.
- 8-point grid: kořenový text 16 px, spacing v krocích 8 px (nebo 0,5 rem).

**Pixel-grid („Square squares") trik:**
- Základní čtverec: řádky 100 px, sloupce 100 px.
- Whitespace gap mezi bloky = čtvrtina buňky = 25 px.
- Obdélníkové grafy nad mřížkou = dvojnásobek: 200 px šířka × 100 px výška.

**Barvy a 60-30-10:**
- Přesně 3 barvy: 60 % neutrál base, 30 % primární brand, 10 % CTA kontrast.
- CTA (10 %): ~90 % saturace a ~90 % jas, **vyhnout se hue H40-H120**.
- Kontrast: min. 4.5:1 běžný text, 3:1 velký text/UI, >15:1 dark mode. Opacity ikon na KPI kartách 75 %.

### Pojmenované metody krok za krokem
**FAST struktura listů (4 funkční sekce oddělené prázdnými listy):**
1. *Foundation* – vstupy (Inputs), časové příznaky (timing flags), indexační faktory.
2. *Workings* – výpočetní „motor", bloky.
3. *Presentation* – výkazy, grafy, primární vstupy, dashboard.
4. *Control* – citlivost, verzování, obsah.

**FAST Calculation Blocks (Corkscrew):** výpočet = poslední 1 řádek; nad ním zdrojové ingredience s live odkazem na data; 1 prázdný řádek nad i pod. Varianty: 4-line corkscrew, 7-line corkscrew with flag, 7-line with PPF.

**FAST pravidlo palce a vteřin:** žádný vzorec delší než šířka palce; žádný vzorec nad 24 vteřin na vysvětlení.

**Onion method (Ben Collins):** složité vnořené vzorce stav po vrstvách – základ (MATCH) v buňce (krok 1), zkopíruj do nové buňky a obal další vrstvou (krok 2), opakuj do finále (krok 4). Viditelný logický záznam, test na každé vrstvě.

**Dashboard Design Checklist (Ben Collins, postup prázdného listu):**
1. Jasný plán komu/k čemu. 2. Struktura listů s červenými oddělovači „Raw data >>". 3. Import surových dat (Supermetrics). 4. Průzkum přes pivoty. 5. Exkluzivní „Settings" list se všemi cíli/proměnnými. 6. „Staging" listy (FILTER/QUERY) speciálně pro grafy. 7. Design hlavičky v Dashboard listu. 8. První návrh + zafixuj grafy. 9. Pauza + zpětná vazba, omez „data pukes". 10. Iteruj, hlavní KPI do levého horního rohu.

### Konkrétní HEX palety
**Wellness/zotavovací (tlumená, z Designového systému):**
- Světlé pozadí (lomená bílá) `#F8F9FA` · text/tmavé pozadí `#121212` · tmavý text/světlé poz. `#212529` · text v dark mode `#E9ECEF`.
- Primární (klidná zelená) `#A3B899` · sekundární (důvěryhodná modrá) `#829AB1` · akcent/CTA (teplá zlatá) `#E9C46A`.
- Stav: úspěch `#85DD7C` · varování `#F4A261` · chyba `#D9534F`.

**Calm (noční obloha):** pozadí Cloud Burst `#1b2250` + čistě bílá = maximální klid.

**Korporátní Facebook dashboard (Ben Collins):** záhlaví Facebook modrá `#3c5a99` (horní 3. řádek).

---

## Web research (subagent, 2026-07-16) – doložené, s URL

Autoritativní zdroje: IBM Carbon, ColorBrewer, Datawrapper, FT Visual Vocabulary, Cleveland-McGill, NN/G, US data-design standards, Ben Collins, Stephen Few.

### Layout a hierarchie
- Mřížka 12-16 sloupců, base unit 8 px. Sidebar 240-280 px, nahoře řada 4-6 KPI karet, pod tím grafy, dole detailní tabulky.
- Vrstvení odshora dolů podle úrovně shrnutí: primární KPI nahoře → trendy → detail.
- F/Z-pattern: nejdůležitější KPI vlevo nahoře, velké. Vpravo dole se přehlíží (NN/G eye-tracking).
- Whitespace = oddělovač skupin, ne dekorace.
- KPI karta (Ben Collins), ustálená hierarchie: název bez žargonu → 1věta popis → velké hlavní číslo → sekundární metrika (delta vs minulé období) → mini-trend/rozpad.
- Stephen Few: dashboard = 1 obrazovka na monitoring; bullet graph místo gauge, sparkline pro kompaktnost.

### Datová vizualizace
- **Data-ink ratio (Tufte):** maximalizuj data-ink, maž non-data-ink (rámečky, pozadí, gridlines) i redundanci.
- **Cleveland-McGill přesnost vnímání** (nejlepší→nejhorší): poloha na společné škále > poloha nezarovnaná > délka/úhel > plocha > objem/zakřivení > sytost barvy. Důsledek: bar/column > pie > heatmapa v přesnosti čtení.
- **Volba grafu (FT Visual Vocabulary, 9 kategorií):** Magnitude → column/bar/lollipop · Change over time → line/column/area/slope · Part-to-whole → stacked bar, pie (jen ≤5-6), treemap, waterfall · Distribution → histogram/boxplot/dot · Correlation → scatter/bubble · Deviation → diverging bar · Ranking → ordered bar/lollipop/slope · Flow → sankey/waterfall/chord.
- **Flat 2D vždy > 3D.** 3D = foreshortening + ztráta ploché základny, nutí číst plochu místo polohy (NN/G: nepoužívat). Pie selhává nad 5-6 výsečí.

### Barvy pro data
- **3 typy palet:** kategoriální (různé hue, skupiny), sekvenční (1 hue přes lightness, low→high), divergentní (2 sekvenční sbíhající se ve světlém středu, odchylka od reference).
- **Počet kategorií:** strop vnímání 6-8 (subitizace). Praktické jádro pro Sheets: **3-6 kategorií, zbytek šedě.** Nad limit: seskup nebo do šedé.
- **"Fewer hues, more shades"** (Economist/FT): 2-3 hue + odstíny > duha.
- **Šedá je pracovní barva** (chybějící data, kontext, nedůležité). Ládit teplotu k paletě.
- **Colorblind-safe:** Okabe-Ito (8, doporučeno Nature Methods) nebo ColorBrewer Set2/Dark2/Paired. Stavy: **modrá/červená > zelená/červená** (deuteranopie).
- **Kontrast:** grafika 3:1, text 4.5:1. Světlá žlutá/oranžová na bílé často padne pod 3:1.
- **Nespoléhej jen na barvu** (Carbon): oddělovací linky, tvarové markery, textury, vždy nabídnout data table.

### Typografie
- Velikosti: body/BI 11-13 px (16 px nejbezpečnější), titul 18-22 pt, KPI label 10-12 pt, popisky 8-9 pt. Max 3-4 úrovně, min. krok 2 px.
- Line-height 1.4-1.7×, minimum 1.5×. Type scale ratio 1.125 (Major Second) na baseline 14 px.
- **Tabulární (monospaced) číslice** pro čísla ve sloupcích (jinak `$1,111.11` vypadá menší než `$999.99`). Bezserif (Inter, Roboto, Noto Sans).
- Zarovnání: kvantitativní čísla vpravo / na desetinnou; text vlevo; kvalitativní čísla (datum, ID, PSČ) vlevo. Hlavička kopíruje zarovnání sloupce.
- Výška řádku tabulky: 40 px condensed / 48 regular / 56 relaxed. Dělící linka max 1 px světle šedá.

### Anti-slop signál → náhrada
- Duha → 2-3 hue + odstíny, nedůležité šedě, max 6.
- 3D/stíny/perspektiva → flat 2D.
- Vícevýsečové/3D pie → bar; pie jen ≤5-6.
- Chartjunk (textury, gradient pozadí, obrázky) → prázdné pozadí, jen data-ink.
- Tlusté mřížky/borders všude → skryté gridlines, max 1 px šedá linka nebo whitespace.
- Balastní desetiny → zaokrouhlit na rozhodovací přesnost.
- Legenda stranou → přímý popisek na konci čar/segmentů.
- Zelená/červená stavy → modrá/červená.
- Proporcionální číslice → tabulární + pravé zarovnání.

### Konkrétní palety (HEX)
- **IBM Carbon kategoriální (14, ber první 3-6):** `#6929c4 #1192e8 #005d5d #9f1853 #fa4d56 #570408 #198038 #002d9c #ee538b #b28600 #009d9a #012749 #8a3800 #a56eff`.
- **Okabe-Ito colorblind-safe (8):** `#E69F00 #56B4E9 #009E73 #F0E442 #0072B2 #D55E00 #CC79A7 #000000`.
- **US gov (Census) kategoriální:** teal `#26C6DA`, navy `#112E51`, orange `#FF7043`, grey `#78909C`, blue `#2E78D2`, dark teal `#006C7A`, light orange `#FFBEA9`.
- **US gov sekvenční (blue):** `#081627 #112E51 #205493 #2E78D2 #6DA1E0 #97BCE9 #C1D7F2`.
- **US gov divergentní:** `#112E51 #97BCE9 #C1D7F2 #FFBEA9 #853A22`.
- **ColorBrewer** (colorblind/print filtr): Set2, Dark2 (3 kat.), Paired (4 kat.) → hex generuj na colorbrewer2.org.

### Google Sheets: co jde a kde je strop
Jde dobře: skrýt gridlines, freeze; vrstvení Insert→Drawing (layout karty/oddělovače) + transparentní grafy navrch (Chart→Customize→Chart style→no fill/border); `=SPARKLINE()` do KPI karet; custom number format s barvou/šipkami pro delty; kategoriální hex ručně (drž 3-6); bullet efekt = stacked bar + reference line; filtry Data validation dropdown + Slicer.
Strop: není přesná pixel-grid ani 8px systém (rozestupy přes šířky sloupců/řádků + Drawing align "na oko"); fonty jen Google Fonts (ne všude tabular figures); přímé in-line datalabels omezené; color scale CF má omezenou kontrolu midpointu; žádné nativní textury/markery jako colorblind pojistka; bullet/violin/sankey/waterfall nejsou nativní.

### Top zdroje (hloubkové čtení)
1. IBM Carbon color-palettes + accessibility článek (medium.com/carbondesign) – 14barevný systém, 3:1, ne-barevné pojistky.
2. Datawrapper "Colors for data vis style guides" – jak Economist/FT volí palety, "fewer hues more shades", role šedé.
3. FT Visual Vocabulary README (github Financial-Times/chart-doctor) – otázka → typ grafu.
4. colorbrewer2.org – generátor palet s colorblind/print filtry.
5. Okabe-Ito reference (conceptviz.app) – 8barevná colorblind-safe s hex.
6. NN/G "Clutter-free charts" – co mazat (3D, textury, legenda→popisek).
7. Cleveland-McGill (flowingdata.com) – proč bar > pie > heatmapa.
8. Ben Collins "visual dashboard design" + "10 techniques" – Sheets vrstvení + Drawing trik.
9. Pencil & Paper "Enterprise data tables" – row-height, zarovnání, monospaced čísla.
10. US data-design standards Colors (xdgov.github.io) – hotové 508-compliant hex sekvence.

Pozn.: Carbon/ColorBrewer/Material přesné hex jsou zčásti za JS-render/generátorem; Carbon 14 ověřeno křížově, u ColorBrewer/Material odkaz na nástroj, ne hodnoty z paměti.

---

## Kolo 3 – studie: rozhodovací logika (NotebookLM, 2026-07-16)

> Caveat: NotebookLM nechal pole ZDROJ prázdné (necitoval). Obsah ale kříží s web research výše (ten URL má), takže se dá brát jako podložený. Formát VOLBA / KDY / KDY NE / PROČ.

### 1. Rozhodovací rámec vizualizace
- **KPI karta (scorecard):** KDY jediná klíčová metrika na nejcennějším místě (vlevo nahoře). KDY NE když je potřeba kontext/vývoj v čase. PROČ okamžité sdělení bez dekódování mřížky, nízká kognitivní zátěž.
- **Datová tabulka s filtry:** KDY čtenář porovnává desítky přesných hodnot / hledá záznamy / operativní seznam. KDY NE exec dashboard na „big picture". PROČ sekvenční čtení je pomalé (Hick: čas rozhodnutí roste se složitostí).
- **Sloupcový/pruhový graf:** KDY srovnání absolutních velikostí několika kategorií. KDY NE plynulý časový vývoj s desítkami bodů. PROČ mozek přesně srovnává délky hran ve 2D.
- **Čárový graf:** KDY trend spojitých dat v čase. KDY NE nezávislé nespojité kategorie. PROČ Gestalt jednotné spojení vede oko po lince, sděluje směr bez čtení os.
- **Koláčový graf:** KDY podíl na celku u max 2-4 kategorií. KDY NE podobně velké kategorie nebo >5. PROČ oko špatně odhaduje úhly/plochy.
- **Heatmapa (barevná škála):** KDY rychlá identifikace extrémů/anomálií v obří matici. KDY NE když jsou primární přesné absolutní hodnoty. PROČ vizuální izolování (Von Restorff), focal point navede oko dřív než čtení čísel.

### 2. A/B studie prvků (A slop → B profi, proč B)
- **Paleta:** duha → 60-30-10 + odstíny jedné barvy. Duha přetěžuje vizuální paměť a ničí hierarchii; harmonie dává klid, odlišná barva zvýrazní jen focal point.
- **Hlavička:** roztroušené černé buňky → tmavý plný blok (H1) + oddělovač 3 px + whitespace. Tmavý pruh definuje strukturu, dává vzhled aplikace, ne tabulky.
- **Čísla:** `$1,456,234.89` → `$1.46M` / zaokrouhleno bez desetin. Desetiny u obřích čísel jsou balast, zaokrouhlení snižuje kognitivní tření.
- **Grafy:** 3D + border + mřížka pozadí → 2D flat, bez ohraničení, průhledné pozadí. 3D zkresluje (úhly), transparentnost umožní vplynout do Drawing gridu.
- **Mřížka:** defaultní gridlines → zcela skryté. Gridlines = vizuální šum; bez nich čisté plátno, oddělování whitespacem (Gestalt blízkost).

### 3. Barvy do hloubky
- **60-30-10:** KDY základní paleta jakéhokoliv dashboardu. KDY NE utilitární DB bez UI. PROČ balanc: 60 % neutrál (tiché plátno, např. `#F8F9FA`), 30 % sekundární (identita, např. `#829AB1`), 10 % akcent/CTA (focal point).
- **Akcent >90 % saturace, vyhnout se hue H40-H120:** KDY CTA a upozornění. KDY NE běžné panely/pozadí. PROČ žlutozelené H40-H120 mají na světlém pozadí tragický kontrast (pod 3:1 WCAG) a nedají „pop".
- **Tlumené neutrální palety:** KDY wellness/HR/stabilní korporát. KDY NE gamifikovaný e-commerce na adrenalin. PROČ tlumené snižují stres a únavu očí; ostrá červená = panika; chybu řešit tlumenou červenou (`#D9534F`).

### 4. Archetypy reportů (user cases)
- **(a) Exec KPI dashboard (C-level):** otázka „jsme na tom dobře/špatně?". Oddělený Dashboard tab, dominantní KPI karty vlevo nahoře (F-pattern/peak-end), čárové grafy pro makro-trendy. Tlumená korporát paleta, masivní H1 (Montserrat 32 pt), bez desetin. PROČ Hick: minimum informací s nejvyšší hodnotou, bez scrollování.
- **(b) Operativní tracker (tým):** otázka „kde to hoří, na čem dělat dnes?". Tabulka + Dropdown/Slicer, stavové indikátory (CF Red/Amber/Green). Ostrý kontrast statusů (úspěch `#85DD7C`, chyba `#D9534F`), hustší menší písmo (Lato 14 pt). PROČ mikro-rozhodnutí, Doherty threshold (okamžitá filtrace), sledování anomálií.
- **(c) Finanční model:** otázka „jak dojdeme k zisku a je výpočet nezpochybnitelný?". Striktní FAST (Foundation/Workings/Presentation/Control), NULOVÉ slučování buněk (zabíjí výpočetní bloky), corkscrew. Modré písmo = vstupy, černé = výpočty, červené = exporty na jiné listy. PROČ auditabilita a transparentnost > krása.
- **(d) Sdílený přehled (netechnickí):** otázka „jak číst, aniž něco rozbiju?". Welcome sheet (návod) první, ochrana uzamčených buněk/listů. Square-squares mřížka (buňky 100x100), ilustrační grafika/pozadí přes Insert→Drawing. PROČ netechnický se děsí prázdné tabulky; vzhled aplikace + uvítací list = pocit bezpečí a mapa kognitivního modelu.

### 5. Metodiky a kdy nasadit
- **FAST struktura + Calculation Blocks (corkscrew):** KDY robustní finanční/datové modely. KDY NE triviální ad-hoc DB. PROČ bojuje proti spaghetti odkazům; blok = 1 vzorec izolovaný na konci s precedenty nad ním; corkscrew (otevírací = předchozí uzavírací) eliminuje kruhové odkazy.
- **FAST pravidlo palce a 24 vteřin:** KDY psaní logického vzorce. KDY NE obří array vzorce. PROČ vzorec delší než palec / vysvětlení nad 24 s = kognitivní tření, rozbij do víc kroků.
- **Ben Collins Onion method:** KDY mocné hnízděné vzorce (INDEX/MATCH, složité QUERY). KDY NE běžné SUM/VLOOKUP. PROČ staví zevnitř ven, zanechává audit trail, chytí chybu (#N/A) ve vrstvě kde vznikla; IFERROR jako poslední obal.
- **Ben Collins Dashboard checklist (separace fází):** KDY stavba vizualizačního produktu z prázdného listu. KDY NE hrubý mockup pro ideaci. PROČ eliminuje sheet-block; QUERY na surových datech → skryté Staging listy → Dashboard jen vizuálně těží; červené Separator taby drží řád.

### 6. Kritéria kvality (měřitelné) + jak testovat
1. **Hustota vs whitespace:** definovaný bílý prostor kolem každého kontejneru (100x100 grid nebo 8pt měkká mřížka, okraje 24/32 px).
2. **Kontrast WCAG 2.1:** min. 4.5:1 tělo textu (16 px), 3:1 velká grafická KPI (32 px+).
3. **Miller 7±2:** max 5-9 grafů/metrik/tabulek na jeden view; zbytek za dropdown/slicer.
4. **Validace formátem:** plošné IFERROR proti `#REF!`/`#DIV/0!`; přetékající názvy řešit Shrink to fit, ne rozšiřováním sloupce.
- **Test:** odstup od PC (Ben Collins „step away"), ukaž člověku mimo projekt bez jediného slova vysvětlení. Když do 24 s neodhalí, jakou byznys otázku report řeší, je to „data puke" → zjednodušit (Occam).
