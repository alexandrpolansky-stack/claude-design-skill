# Stroke a hranice: border vs. stín vs. whitespace

Nota řeší, čím oddělit prvky (border, stín, rozdílné pozadí, mezera), jak tlusté
a kontrastní mají hranice být a kde je to regulované. Otevři ji, když váháš mezi
borderem a stínem, nebo když design začíná vypadat "zaneřáděně" čárami.

Poctivá poznámka k evidenci: v tomhle tématu existuje jeden tvrdý mantinel, a je
regulatorní (WCAG), ne výzkumný. Zbytek jsou publikované konvence design systémů
a řemeslná praxe. Žádná studie z auditu (2026) neměří vliv šířky nebo počtu borderů
na chování uživatele. Pravidla jsou podle toho označená, nepovyšuj je.

Sesterská nota: [Tvar a radius](tvar-a-radius.md) (border-radius a ostré vs. kulaté).

## Pravidla

### Viditelnost hranic je regulovaná: kontrast 3:1 (WCAG 1.4.11)

**PRAVIDLO:** Vizuální hranice, podle které uživatel pozná UI komponentu nebo její stav
(rámeček inputu, focus indikátor, checkbox, ikona, část grafu nutná k pochopení), musí
mít kontrast minimálně 3:1 proti sousedním barvám.
**KDY PLATÍ:** Všechny aktivní komponenty a informačně nutná grafika. Úroveň AA, nové
ve WCAG 2.1. V EU je to pro e-commerce a consumer banking právně vynutitelné (European
Accessibility Act, živý od 28. 6. 2025), pro český veřejný sektor zákon č. 99/2019 Sb.
**PROČ:** Bez kontrastní hranice slabozraký uživatel nenajde pole a nepozná focus.
Prakticky to vylučuje "invisible UI": bezokrajové inputy na světle šedém pozadí,
hairline rámečky #eee na bílé, jemně šedé icon-only tlačítko na šedé.
**TŘÍDA:** B, regulatorní mantinel (práh 3:1 je expertní konsensus W3C odvozený
z ISO/ANSI, ne naměřený percepční práh; závaznosti to neubírá)
**ZDROJ:** https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html
(SC 1.4.11 Non-text Contrast, AA, WCAG 2.1)
**KDY NEPLATÍ:** Neaktivní (disabled) komponenty, čistě dekorativní grafika, vzhled
plně určený prohlížečem bez zásahu autora. A pozor na záměnu: WCAG reguluje kontrast,
ne šířku. 1px border s kontrastem 3:1 projde, 3px border v #eee na bílé ne.

### Border je poslední volba oddělení

**PRAVIDLO:** Když potřebuješ oddělit dva prvky, zkus v tomhle pořadí: 1. whitespace
(větší mezera), 2. rozdílné pozadí, 3. jemný box shadow, 4. teprve pak border.
**KDY PLATÍ:** Karty, sekce, sidebar vs. obsah, řádky seznamu, skupiny ve formuláři.
Obzvlášť když už layout nějaké bordery má.
**PROČ:** Každý border je čára navíc, kterou oko musí zpracovat. Víc ohraničených prvků
vedle sebe = vizuální šum, design působí zaneřáděně. Mezera a pozadí oddělují bez
přidané kresby.
**TŘÍDA:** C (autorská zkušenost, Adam Wathan a Steve Schoger; bez publikovaného měření)
**ZDROJ:** Refactoring UI (Wathan & Schoger), https://www.refactoringui.com
**KDY NEPLATÍ:** Inputy a interaktivní prvky, kde border nese rozpoznatelnost a spadá
pod WCAG 1.4.11 (viz výše), tam border nenahrazuj. Husté datové tabulky, kde linky
drží řádkování. Prostředí, kde stín ani pozadí nefungují spolehlivě (e-mailové
šablony, tisk).

### Oddělovací linka: 1 px, tlumená, a jen když mezera nestačí

**PRAVIDLO:** Když už oddělovací linku použiješ, drž ji na 1 px v tlumené šedé.
Nejdřív ale ověř, jestli oddělení nezvládne samotná mezera.
**KDY PLATÍ:** Seznamy, navigace, dlouhý obsah členěný do sekcí.
**PROČ:** Silnější čára přidává vizuální váhu, kterou oddělovač nemá mít. Oddělovač je
pomůcka, ne prvek. NHS design system pracuje s tenkými linkami místo tlustých borderů
a primární oddělení nechává na whitespace.
**TŘÍDA:** B/C (konvence NHS design systemu + praxe Refactoring UI)
**ZDROJ:** https://service-manual.nhs.uk/design-system; Refactoring UI
**KDY NEPLATÍ:** Linka nutná k pochopení UI (hranice buněk editovatelné tabulky,
osa grafu) spadá pod 1.4.11 a "tlumená" má strop: musí zůstat viditelná pro slabozraké.
A mimo web: v Google Sheets reportech platí domácí pravidlo gridlines vždy viditelné,
obecná rada "linky pryč" se tam nepoužívá (viz [sheets znalostní
báze](../../sheets/znalostni-baze.md)).

### Stín jen tam, kde znamená vrstvu

**PRAVIDLO:** Stín používej jako signál elevace, tedy že prvek leží nad okolím: modál,
popover, dropdown, tažená karta. Statické dlaždice a karty v mřížce nech bez stínu,
odděl je pozadím nebo mezerou.
**KDY PLATÍ:** Rozhodování border vs. stín u karet, overlay prvků a menu.
**PROČ:** V publikovaných systémech je stín sémantický. IBM Carbon vyhrazuje elevaci
pro modály a popovery, dlaždice jsou bez elevace. Material 3 dělá hloubku primárně
tonálním rozdílem barvy a stín přidává, jen když je potřeba oddělení od pozadí.
Stín na všem = žádná informace o vrstvách.
**TŘÍDA:** B (publikované konvence IBM Carbon a Google Material 3)
**ZDROJ:** https://carbondesignsystem.com (elevation);
https://m3.material.io/styles/elevation
**KDY NEPLATÍ:** Brand postavený na měkké estetice se stíny jako dekorací: jde to, ale
stín tím ztrácí význam vrstvy a interaktivitu musíš signalizovat jinak. Naopak striktně
flat systémy stín nepoužívají vůbec a vrstvy řeší jen barvou.

### Focus ring přes box-shadow, ne outline (kvůli staršímu Safari)

**PRAVIDLO:** Custom focus indikátor kresli přes box-shadow místo outline, pokud
podporuješ Safari starší než 16.4.
**KDY PLATÍ:** Vlastní focus styly na zaoblených prvcích (tlačítka, inputy s radiusem).
**PROČ:** `outline` historicky nerespektoval `border-radius`, ring byl hranatý kolem
kulatého tlačítka. Safari to opravilo až ve verzi 16.4.
**TŘÍDA:** C (řemeslná praxe, Rauno Freiberg, Web Interface Guidelines)
**ZDROJ:** https://interfaces.rauno.me
**KDY NEPLATÍ:** Při podpoře jen aktuálních prohlížečů outline radius respektuje a má
výhody: neovlivňuje layout a s `outline-offset` se snadno odsazuje. V obou variantách
musí indikátor splnit kontrast 3:1 (WCAG 1.4.11, viz první pravidlo).

## Co nemá oporu

- **"Tenký hairline stroke a light řezy působí luxusně."** Rešerše sektoru luxury (2026)
  nenašla jedinou studii, která by to tvrdila. Žádný luxury dům (LVMH, Gucci, Hermès)
  nepublikuje design system, o který by se dalo opřít. Navíc to naráží na WCAG: tenké
  světlé řezy padají pod 1.4.3 (kontrast textu 4,5:1) a jemné linky pod 1.4.11.
  Třída C, necitovat jako pravidlo.
- **Bezokrajové "invisible UI"** (input poznáš jen podle placeholderu na světle šedé
  ploše) není minimalismus, je to nesplněné 1.4.11. Viz první pravidlo.

## Jak rozhodnout v praxi

1. Jde o interaktivní prvek nebo informačně nutnou hranici? Pak border/indikátor
   s kontrastem min. 3:1 a hotovo, o tomhle se nediskutuje.
2. Jde jen o oddělení obsahu? Zkus mezeru, pak pozadí, pak jemný stín, border poslední.
3. Stín dávej jen prvkům, které reálně leží nad okolím (modál, popover, dropdown).
4. Linky drž na 1 px a tlumené, ale ne tak tlumené, aby zmizely slabozrakým.

Související: [Tvar a radius](tvar-a-radius.md) (stejný princip: konzistence systému
místo psychologie), [Layout Theory](../layout/layout-theory.md) (whitespace, margin,
padding jako primární oddělovač).

**Souvislost:** V režimu vynucených barev určuje barvu hranice systém a hranice se stává hlavním nositelem tvaru komponenty, viz [Vynucené barvy](vynucene-barvy.md).
