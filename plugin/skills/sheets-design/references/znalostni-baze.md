
# Sheets design — znalostní báze (spojený destilát)

> [!important] Domácí pravidlo přebíjí obecný výzkum: GRIDLINES ZŮSTÁVAJÍ VIDITELNÉ
> Obecný dataviz výzkum níže (Tufte, data-ink ratio) doporučuje gridlines skrývat.
> Pro TrustSoft tabulky to NEPLATÍ. Existující reporty (Access Overview a spol.)
> gridlines mají; nový list, který je skryje, vypadá cize a nesedne k ostatním.
> Nikdy nevolej `hide_gridlines` / `setHiddenGridlines(true)` na TrustSoft listech.
> Zbytek doporučení (whitespace místo tlustých borderů, max 1 px linky) platí dál.


> Autoritativní podklad pro `sheets-design` skill. Spojuje NotebookLM extrakci (kola 1-3, viz [NotebookLM destilát](notebooklm-destilat.md)) a web research (IBM Carbon, ColorBrewer, Datawrapper, FT Visual Vocabulary, Cleveland-McGill, NN/G, US data-design standards, Ben Collins, Stephen Few).
> Provenience: **[oba]** = NotebookLM i web nezávisle souhlasí (vysoká jistota) · **[NLM]** = jen NotebookLM · **[web]** = jen web research (má URL).

## 0. Princip
Cíl: Sheet vypadá jako **report / aplikace, ne jako tabulka**. Kvalita = kázeň v mřížce a mazání všeho, co nenese informaci (data-ink ratio, Tufte [web]), ne dekorace. Barva, ohraničení, font navíc = šum. Sheet nefingujeme jako HTML/Figmu, ale dotáhneme dokumentový dojem. [oba]

## 0b. TrustSoft identita (DEFAULT paleta + font) — zdroj pravdy: `panovec 6/references/design-system.md`
Sheet reporty se defaultně stylují do TrustSoft brandu (soulad s prezentačním skillem Panovec). Tohle přebíjí generickou paletu níže; obecná pravidla (60-30-10, kontrast, počet barev) platí dál jako mantinely.

**Font:** Work Sans (v Sheets dostupný jako Google Font).

**Paleta (role):**
| token | hex | role |
|---|---|---|
| navy | `#202C39` | hlavičky, struktura, text, tmavá pozadí |
| green | `#8EC641` | JEDINÝ akcent (klíčová data, ikony, fills) |
| dkGreen | `#35601A` | zelená pro TEXT na světlém (akcentní green je moc světlá → nízký kontrast) |
| surface / bg / hi | `#F2F7FD` / `#F8FCFD` / `#EFF5E3` | light card / pozadí / soft green highlight |
| grey ramp n50-n800 | `#F5F7FA` `#E2E8EF` `#C7D0DA` `#8B97A4` `#5A6672` `#38424E` | neutrály (zebra, linky, muted) |
| coral / amber | `#EA6044` / `#F0C602` | JEN funkčně: chyba / varování |
| gray999 | `#707070` | muted/"before" text (nikdy grey-blue) |
| aws / azure | `#FF9900` / `#0078D4` | OPT-IN only, nikdy defaultně |

**Zamčený table styling (mapuje se 1:1 na Sheets):** navy hlavička + bílý bold; zebra white / `n50`; tenké `n100` linky; muted sloupec `gray999`; highlight sloupec `hi` fill + navy bold. Čísla doprava bez balastních desetin. **Gridlines viditelné** (domácí pravidlo, viz callout nahoře), freeze hlavičky.

**Brand mantinely:** RULE #0 = čitelnost, nikdy tone-on-tone, na tmavém pozadí text jen bílá/green. Green dosage = max jedna velká zelená masa (jinak přehoď na navy/grey). Jeden akcent (green), modrá není akcent. Bez em-dashů (spaced en-dash pro rozsahy). Ikona nikdy nesplývá s kruhem (bílá ikona na barevném / navy na světlém).

## 1. Rozhodovací rámec: co použít kdy
Vybírej podle **byznys otázky**, ne podle toho co je hezké. Přesnost vnímání (Cleveland-McGill, od nejpřesnějšího): poloha na společné škále > poloha nezarovnaná > délka/úhel > plocha > objem > sytost barvy. Důsledek: **bar/column > pie > heatmapa** v přesnosti čtení. [web]

| Otázka / potřeba | Nástroj | Proč | Kdy NE |
|---|---|---|---|
| Jediná klíčová metrika, hned | **KPI karta** vlevo nahoře | okamžité sdělení bez dekódování mřížky, nízká kognitivní zátěž [oba] | když je potřeba kontext/vývoj |
| Srovnání velikostí kategorií | **Sloupcový/pruhový** | mozek přesně čte délky ve 2D [oba] | plynulý čas s desítkami bodů |
| Trend v čase (spojitá data) | **Čárový** | Gestalt jednotné spojení vede oko, sděluje směr [oba] | nespojité nezávislé kategorie |
| Podíl na celku, málo kategorií | **Pie/donut jen ≤5** (ideál 2-4) | oko špatně čte úhly/plochy [oba] | podobně velké nebo >5 → bar |
| Porovnat desítky přesných hodnot | **Tabulka + filtry** | detail, přesnost | exec „big picture" (Hick: pomalé) [NLM] |
| Extrémy/anomálie v obří matici | **Heatmapa (color scale)** | vizuální izolace (Von Restorff), focal point [NLM] | když jsou primární přesné hodnoty |
| Rozložení | histogram / boxplot / dot | [web] | |
| Vztah dvou proměnných | scatter / bubble | [web] | |
| Odchylka od reference/nuly | diverging bar | [web] | |
| Pořadí | ordered bar / lollipop / slope | [web] | |
| Cíl vs skutečnost kompaktně | **bullet graph** (Few) | náhrada gauge, zlomek místa; v Sheets aproximace stacked bar + reference line [web] | |

**Flat 2D vždy > 3D.** 3D = foreshortening + ztráta ploché základny, nutí číst plochu místo polohy; NN/G: nepoužívat. [oba]

## 2. Barvy
**Tři typy palet** [web]: kategoriální (různé hue = skupiny), sekvenční (1 hue přes lightness, low→high), divergentní (2 sekvenční sbíhající se ve světlém středu = odchylka od reference).

Pravidla:
- **60-30-10** [oba]: 60 % neutrál base (tiché plátno, např. `#F8F9FA`), 30 % primární/sekundární (identita), 10 % akcent/CTA (focal point). Přesně 3 „role" barev + 2 sémantické (červená/zelená).
- **Počet kategorií 3-6**, tvrdý strop vnímání 6-8 (subitizace); nad limit seskup nebo dej nedůležité do šedé. [oba] Carbon dovolí max 14 jen s texturami/markery. [web]
- **„Fewer hues, more shades"** (Economist/FT): 2-3 hue + odstíny > duha. [oba]
- **Šedá je pracovní barva** (chybějící data, kontext, nedůležité); ládit teplotu k paletě. [web]
- **Akcent (CTA):** ~90 % saturace/jas, **vyhnout se hue H40-H120** (žlutozelené padnou pod 3:1 na světlém pozadí). [NLM]
- **Sémantika stavů + colorblind:** stav vždy i textem/ikonou, nikdy jen barvou; preferuj **modrá/červená > zelená/červená** (deuteranopie). [oba]
- **Kontrast:** grafika/velké KPI 3:1, tělo textu 4.5:1. Světlá žlutá/oranžová na bílém často pod 3:1. [oba]
- **Tlumené vs syté podle publika** [NLM]: tlumené (wellness/HR/korporát) snižují stres a únavu; sytá/ostrá pro gamifikovaný e-commerce. Ostrá červená = panika → chybu řešit tlumenou červenou.

**Hotové palety (HEX):**
- IBM Carbon kategoriální (14, ber první 3-6): `#6929c4 #1192e8 #005d5d #9f1853 #fa4d56 #570408 #198038 #002d9c #ee538b #b28600 #009d9a #012749 #8a3800 #a56eff`. [web]
- Okabe-Ito colorblind-safe (8): `#E69F00 #56B4E9 #009E73 #F0E442 #0072B2 #D55E00 #CC79A7 #000000`. [web]
- US gov sekvenční (blue): `#081627 #112E51 #205493 #2E78D2 #6DA1E0 #97BCE9 #C1D7F2`; divergentní: `#112E51 #97BCE9 #C1D7F2 #FFBEA9 #853A22`. [web]
- ColorBrewer colorblind/print (Set2, Dark2, Paired) → generuj na colorbrewer2.org. [web]
- Tlumená „wellness" [NLM]: base `#F8F9FA`, text `#212529`, primární zelená `#A3B899`, sekundární modrá `#829AB1`, akcent zlatá `#E9C46A`, úspěch `#85DD7C`, varování `#F4A261`, chyba `#D9534F`. „Calm": pozadí `#1b2250` + bílá.

## 3. Typografie
- **Bezserif** (Roboto, Inter, Lato, Noto Sans); vysoká x-height, jasné 1/l/I. [oba]
- **Velikostní škála (sjednoceno NLM pt + web px):** titul/H1 18-32 (exec KPI dashboard velký, 32; běžný report 18-22), H2 20-24, tělo 11-16 (16 nejbezpečnější), popisky/metadata 8-12, terciár minimum 12 (Light řezy ne pod 8 px). Max 3-4 úrovně, min. krok 2 px. Hierarchie **velikostí a váhou, ne barvou**. [oba]
- **Line-height 1.4-1.7×**, minimum 1.5×. Type scale ratio 1.125 (Major Second) na baseline 14 px. [web]
- **Tabulární (monospaced) číslice** pro čísla ve sloupcích (jinak `$1,111.11` vypadá menší než `$999.99`); v Sheets přes Roboto Mono nebo pravé zarovnání. [web]
- **Zarovnání:** kvantitativní čísla (peníze, %, množství) vpravo / na desetinnou; text vlevo; kvalitativní čísla (datum, ID, PSČ) vlevo; hlavička kopíruje zarovnání sloupce. [oba]
- **Čísla bez balastních desetin** — zaokrouhli na rozhodovací přesnost (`$1.46M`, ne `$1,456,234.89`). [oba]

## 4. Layout a hierarchie
- **Mřížka 12-16 sloupců, base unit 8 px.** Sidebar 240-280 px, nahoře řada 4-6 KPI karet, pod tím grafy, dole detailní tabulky. [web]
- **Vrstvení odshora podle úrovně shrnutí:** primární KPI → trendy → detail. [web]
- **F/Z-pattern + hodnota levého horního rohu:** nejdůležitější KPI vlevo nahoře, velké; vpravo dole se přehlíží (NN/G eye-tracking). [oba]
- **Whitespace = oddělovač skupin**, ne dekorace (Gestalt blízkost > tlusté čáry). [oba]
- **KPI karta, anatomie (Ben Collins):** název bez žargonu → 1věta popis → velké hlavní číslo → sekundární metrika (delta vs minulé období) → mini-trend/sparkline. [oba]
- **Miller 7±2:** max 5-9 grafů/metrik/tabulek na jeden view; zbytek za dropdown/slicer. [oba]
- **Dashboard = 1 obrazovka na monitoring** (Few); rozvržení podpoří vztahy mezi prvky. [web]
- Výška řádku tabulky: 40 px condensed / 48 regular / 56 relaxed; dělící linka max 1 px světle šedá. [web]

## 5. A/B: slop → profi (a proč B vyhrává)
| Prvek | A (slop) | B (profi) | Proč B |
|---|---|---|---|
| Paleta | duha, náhodné barvy | 60-30-10, odstíny 1 barvy | duha přetěžuje paměť a ničí hierarchii; harmonie = klid, odlišná barva jen focal point [oba] |
| Hlavička | roztroušené černé buňky | tmavý plný blok (H1) + oddělovač 3 px + whitespace | pevná struktura, vzhled aplikace ne tabulky [oba] |
| Čísla | `$1,456,234.89` | `$1.46M` / zaokrouhleno | desetiny u obřích čísel = balast, zaokrouhlení snižuje tření [oba] |
| Grafy | 3D + border + mřížka pozadí | 2D flat, bez ohraničení, průhledné pozadí | 3D zkresluje úhly; transparentnost vplyne do Drawing gridu [oba] |
| Mřížka | tlusté borders všude | tenké linky + whitespace, gridlines ponechat | non-data-ink škodí, ale gridlines v TrustSoft listech ZŮSTÁVAJÍ (domácí pravidlo) |
| Legenda | stranou grafu | přímý popisek na konci čar/segmentů | oko nemusí skákat legenda↔graf [web] |
| Chartjunk | textury, gradient, obrázky | prázdné pozadí, jen data-ink | Tufte data-ink [web] |
| Ohraničení | plné borders všude | max 1 px šedá linka nebo whitespace | méně non-data-ink [oba] |
| Číslice | proporcionální (sloupce skáčou) | tabulární + pravé zarovnání | zarovnané řády, čitelné porovnání [web] |

## 6. Archetypy reportů (podle čtenáře a otázky) [NLM]
- **(a) Exec KPI dashboard (C-level)** — otázka „jsme na tom dobře/špatně?". Oddělený Dashboard tab, dominantní KPI karty vlevo nahoře, čárové grafy pro makro-trendy. Tlumená korporát paleta, masivní H1 (32 pt), bez desetin. Proč: Hick — minimum informací s nejvyšší hodnotou, bez scrollování.
- **(b) Operativní tracker (tým)** — otázka „kde to hoří, na čem dělat dnes?". Tabulka + Dropdown/Slicer, stavové indikátory (CF Red/Amber/Green). Ostrý kontrast statusů (`#85DD7C` / `#D9534F`), hustší menší písmo (14 pt). Proč: mikro-rozhodnutí, okamžitá filtrace (Doherty), sledování anomálií.
- **(c) Finanční model** — otázka „jak dojdeme k zisku a je výpočet nezpochybnitelný?". Striktní FAST, NULOVÉ slučování buněk (zabíjí výpočetní bloky), corkscrew. Modré písmo = vstupy, černé = výpočty, červené = exporty na jiné listy. Proč: auditabilita > krása.
- **(d) Sdílený přehled (netechničtí)** — otázka „jak číst, aniž něco rozbiju?". Welcome sheet první, ochrana uzamčených buněk/listů. Square-squares mřížka + ilustrační pozadí přes Drawing. Proč: netechnický se děsí prázdné tabulky; vzhled aplikace + návod = pocit bezpečí.

## 7. Metodiky a kdy nasadit [NLM, potvrzeno Ben Collins ve web]
- **FAST struktura listů** (Foundation / Workings / Presentation / Control) + **Calculation Blocks (corkscrew)** — robustní finanční/datové modely; ne triviální ad-hoc DB. Blok = 1 vzorec na konci s precedenty nad ním; corkscrew (otevírací = předchozí uzavírací) eliminuje kruhové odkazy.
- **FAST pravidlo palce a 24 vteřin** — vzorec delší než palec / vysvětlení nad 24 s = rozbij do víc kroků.
- **Ben Collins Onion method** — mocné hnízděné vzorce (INDEX/MATCH, složité QUERY): stav zevnitř ven, audit trail, IFERROR jako poslední obal; ne na běžné SUM/VLOOKUP.
- **Ben Collins Dashboard checklist** — stavba z prázdného listu: QUERY na surových datech → skryté Staging listy → Dashboard jen vizuálně těží; červené Separator taby drží řád. Zjednodušená struktura listů (potvrzuje i gsheets-skill repo): README/Welcome, Raw_Data, Clean_Data, Assumptions/Settings, Calculations/Staging, Summary, Dashboard.

## 8. Google Sheets: co jde a kde je strop [oba]
**Jde dobře:** skrýt gridlines (View → Show → Gridlines off; technicky jde, ale na TrustSoft listech to NEPOUŽÍVEJ, viz callout nahoře) + freeze; **vrstvení Insert → Drawing** (layout karty/oddělovače/pozadí) + **transparentní grafy** navrch (Chart → Customize → Chart style → no fill/border); `=SPARKLINE(data,{...})` do KPI karet; custom number format s barvou/šipkami pro delty; conditional formatting (color scale = heatmapa, vzorec = stav); named + protected ranges (zámek vzorců); Data validation dropdown + Slicer; **pixel-grid** (buňky ~100x100, gap 25 px, grafy 200x100) pro definované mezery; bullet efekt = stacked bar + reference line.

**Strop:** není přesná pixel-grid ani 8px systém (rozestupy přes šířky sloupců/řádků + Drawing align „na oko"); nativně žádné zaoblené rohy / měkké stíny / pill tvary (obchází se Drawing tvary nebo pixel-grid); fonty jen Google Fonts (ne všude plné tabular figures); in-line datalabels omezené (legendu jde skrýt); color scale CF má omezenou kontrolu midpointu; žádné nativní textury/markery jako colorblind pojistka; bullet/violin/sankey/waterfall nejsou nativní typy.

## 9. Kritéria kvality + jak testovat [NLM]
1. **Hustota vs whitespace:** definovaný bílý prostor kolem každého kontejneru (100x100 grid nebo 8pt mřížka, okraje 24/32 px).
2. **Kontrast WCAG 2.1:** min. 4.5:1 tělo (16 px), 3:1 velká KPI (32 px+).
3. **Miller 7±2:** max 5-9 prvků na view; zbytek za filtry.
4. **Odolnost:** plošné IFERROR proti `#REF!`/`#DIV/0!`; přetékající názvy Shrink to fit, ne rozšiřování sloupce.
5. **Slop self-check:** nese každá barva význam? >2 fonty / >6 barev? stav čitelný černobíle? **gridlines viditelné?** KPI čísla srozumitelná bez luštění?
- **Test 24 vteřin:** ukaž člověku mimo projekt, bez vysvětlení. Když do 24 s neodhalí, jakou otázku report řeší → „data puke", zjednoduš (Occam).

## 10. Zdroje (hloubka)
IBM Carbon color-palettes + accessibility (medium.com/carbondesign) · Datawrapper „Colors for data vis style guides" · FT Visual Vocabulary (github Financial-Times/chart-doctor) · colorbrewer2.org · Okabe-Ito (conceptviz.app) · NN/G „Clutter-free charts" · Cleveland-McGill (flowingdata.com) · Ben Collins „visual dashboard design" + „10 techniques" · Pencil & Paper „Enterprise data tables" · US data-design standards Colors (xdgov.github.io) · FAST Standard (fast-standard.org). Plné URL v [NotebookLM destilát](notebooklm-destilat.md) sekci web research.
