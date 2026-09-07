# Datové tabulky

Nejsložitější komponenta enterprise UI. Kdy tabulku použít, jak ji vrstvit funkcemi a co do ní nepatří.

Související: [Volba komponenty](../zaklady/volba-komponenty.md) · [Stránkování](strankovani.md) ·
[Filtrování](../vzory/filtrovani.md) · [Hledání](../vzory/hledani.md) ·
[Přetečení a truncation](../vzory/preteceni-a-truncation.md)

---

## Rychlé rozhodnutí

1. Data ve sloupcích, uživatel mezi nimi porovnává nebo se k jednomu záznamu naviguje = tabulka.
2. Jen čtení párů termín a hodnota, bez řazení = **structured list**, ne tabulka.
3. Komplexnější zobrazení nebo interakce, než tabulka zvládne = **není to tabulka**.
4. Tabulka **není** náhrada tabulkového procesoru.
5. **Nevnořuj tabulku do tabulky** ani do malých kontejnerů, kde se obsah tísní nebo musí zkracovat.
6. Výška řádku hlavičky **musí** být stejná jako výška řádků tabulky.
7. Hover na řádku nechej **vždy zapnutý**, i když řádek není klikatelný.
8. Toolbar: max **pět akcí**, víc přes overflow menu nebo combo button.
9. Overflow menu na řádku s méně než třemi volbami = **nedávej menu, dej ikonová tlačítka inline**.
10. Načítání = **skeleton, ne spinner**.
11. Stránkování **pod** tabulku, bez odsazení, nikdy nad ni.
12. XL výšku řádku použij **jen** tehdy, když čekáš dvě řádky obsahu v jednom řádku.

---

## Kdy tabulku použít a kdy ne

**Použij:** k organizaci a zobrazení dat. Když se uživatel musí nanavigovat ke konkrétnímu kusu dat,
aby dokončil úkol. Na zobrazení všech zdrojů uživatele.

**Nepoužívej:** když je potřeba komplexnější zobrazení dat nebo komplexnější interakce. Jako náhradu
tabulkového procesoru.

**ZDROJ:** Carbon, Data table usage, When to use / When not to use, verbatim: „As a replacement for
a spreadsheet application." https://carbondesignsystem.com/components/data-table/usage/

## Tři varianty

| Varianta | Co dělá |
|---|---|
| Default | Jen hlavička a řádky. Dostupná v pěti výškách řádku |
| With selection | Výběr jednotlivých řádků. Single-select přes radio button, multi-select přes checkbox. Uživatel může provést jednu akci nebo dávkové akce nad vybranými položkami |
| With expansion | Prezentuje velké množství dat v malém prostoru. Uživatel rozbaluje a sbaluje panely řádků, aby odkryl a skryl další informaci |

Kombinace expandable plus selectable je možná. **Rozbalovací ikona je vždy první a nalevo od ikony
výběru.**

**ZDROJ:** Carbon, Data table usage, Variants.
https://carbondesignsystem.com/components/data-table/usage/

## Anatomie

1. **Titulek a popis:** titulek tabulky a volitelný popis.
2. **Toolbar:** globální ovládání tabulky včetně hledání a nastavení.
3. **Hlavička sloupce:** titulek pro záhlaví řádku s volitelným řazením.
4. **Řádek:** lze konfigurovat na různé typy dat. Řádky mohou být vybíratelné, rozbalovací a upravené
   na alternující zebra pozadí.
5. **Lišta stránkování:** volitelná komponenta, která nechá uživatele navigovat data po stránkách,
   když je dat příliš mnoho, aby se zobrazila naráz.

**ZDROJ:** Carbon, Data table usage, Anatomy.
https://carbondesignsystem.com/components/data-table/usage/

## Výšky řádku a párování

Pět výšek: extra small, small, medium, large, extra large. Konkrétní hodnoty (třída **B**, Carbonova
volba):

| Velikost | Výška |
|---|---|
| XS | 24 px |
| SM | 32 px |
| MD | 40 px |
| LG | 48 px |
| XL | 64 px |

**PRAVIDLO:** Řádek hlavičky **vždy** odpovídá výšce řádků tabulky. **Nemíchej** je.
**XL výšku doporučuj jen tehdy, když se očekávají dvě řádky obsahu v jednom řádku.**
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Data table, Style, Rows, dvě věty, verbatim: „The column header row should
always match the row size of the table." a „Extra large row heights are only recommended if your
data is expected to have two lines of content in a single row."
https://carbondesignsystem.com/components/data-table/style/

Citace se opravovala 5. 9. 2026, protože ji `scripts/verify-citations.py` nenašel. Tvrzení
se nezměnilo, přestěhovalo se ze stránky `usage` na `style`, „2 lines" se přepsalo na „two lines"
a **mezi ty dvě věty přibyla třetí**, o centrování textu v řádku. Proto jsou tady dva oddělené
citáty a ne jeden souvislý: slepit dvě věty, mezi kterými na stránce stojí třetí, je citace,
která nikdy nebyla. Ověřeno proti živé stránce z téhož dne, ne z paměti.

**Párování toolbaru s výškou řádku** (Carbon má jen dvě výšky toolbaru na pět výšek řádku):

| Toolbar | Páruje se s |
|---|---|
| Vysoký (48 px) | XL a LG řádky |
| Nízký (32 px) | SM a XS řádky |

**Stránkování** má tři velikosti (LG, MD, SM), takže nejde spárovat 1:1 s pěti výškami řádku. Carbonovo
řešení: u XL řádků použij LG stránkování, u XS řádků SM stránkování.
Zdroj: https://carbondesignsystem.com/components/pagination/usage/

**Sloupce:** šířka se může lišit podle obsahu, vyžaduje se jen minimální mezera mezi sloupci.
**Tabulka vyžaduje tři nebo víc sloupců.** Carbon tedy sám žádné konkrétní šířky nepředepisuje,
předepisuje jen ten odstup.
**ZDROJ:** Carbon, Data table, Style, Structure, verbatim: „Column widths can vary by content and
only require a minimum spacing between columns. Tables require three or more columns."
https://carbondesignsystem.com/components/data-table/style/

**Pozor, tohle platí o jednom vykreslení.** Když se sada řádků mění za běhu (filtr, přepínač
rozsahu, stránkování), znamená „šířka podle obsahu" jinou mřížku pro každou sadu, takže uživatel
přepne filtr a dostane k tomu posun všech sloupců. Co s tím:
[Stabilita layoutu při změně dat](../vzory/stabilita-layoutu.md).

### Šířka sloupců se odvozuje z obsahu, ne z jejich počtu

**PRAVIDLO:** Šířku sloupce určuje to, co v něm stojí. Sloupec s krátkým obsahem je úzký, sloupec
s prózou široký. **Nedělej všechny sloupce stejně široké.**
**KDY PLATÍ:** Vždy. Nejtvrději u tabulek, které míchají krátké tvary (chip, stav, datum, částka)
s prózou (jméno, které psal člověk).
**PROČ:** Rovný podíl dá úzkému obsahu víc místa, než potřebuje, a širokému míň, takže se ořezává
právě ten sloupec, který nese nejvíc informace. Zároveň to od sebe hodnoty vzdálí a řádek se hůř
čte vcelku.
**TŘÍDA:** B
**ZDROJ:** GitLab Pajamas, Table, Content, Columns, verbatim: „Size columns according to the data
they contain rather than making them all an even width. For example, columns of small content
should be narrow, while columns of paragraphs should be relatively wide. Allow the browser to lay
out the tables according to the viewport size." https://design.gitlab.com/components/table/

**PRAVIDLO:** Když se rozchází čitelnost uvnitř jedné tabulky a shoda s tabulkou na jiné obrazovce,
vyhrává ta jedna tabulka.
**KDY PLATÍ:** Při sjednocování víc seznamů v jednom produktu.
**PROČ:** Sjednocení je prostředek, ne cíl. Sloupec zúžený kvůli tomu, aby seděl na jinou stránku,
platí za shodu ořezanou hodnotou, kterou čte uživatel právě tady.
**TŘÍDA:** B
**ZDROJ:** GitLab Pajamas, Table, Appearance, verbatim: „As general rule, consider that alignment
within a table is more important than consistency from table to table."
https://design.gitlab.com/components/table/

**Rozpor mezi dvěma zdroji třídy B, a je vědomý.** GitLab v téže větě říká „allow the browser to
lay out the tables according to the viewport size", tedy auto layout. To jde proti
[stabilitě layoutu](../vzory/stabilita-layoutu.md), která u tabulky s měnící se sadou řádků žádá
deklarované šířky. Rozhoduje účel: GitLab míří na to, ODKUD se šířka bere (z obsahu), stabilita na
to, KDY se přepočítává (nikdy za běhu). Splnit jde obojí, viz metoda níž.

**Odvozená metoda: procenta s podlahou.** Třída **C**, tohle už není citace, je to způsob, jak ta
dvě pravidla splnit naráz.

1. Změř nejdelší **skutečnou** hodnotu každého sloupce, ne reprezentativní. Hlavičku počítej jako
   obsah, když je širší než hodnoty pod ní. Přičti mezeru mezi sloupci.
2. Ta čísla jsou podlahy. Podíl sloupce je jeho podlaha dělená součtem podlah té tabulky,
   `min-width` tabulky je ten součet.
3. Nad `min-width` rostou všechny sloupce společně a poměr drží. Pod ním se nic nesmršťuje, obal
   scrolluje vodorovně.
4. Prózový sloupec je jediný, který se smí ořezat, takže dostane zbytek a jeho podlaha je volba,
   ne měření.

**Co to řeší:** šířka je z obsahu (GitLab), je deklarovaná, takže filtr nepřekreslí mřížku
(stabilita), a nic kromě prózy se neořezává, protože každý sloupec je při `min-width` přesně tak
široký jako jeho nejdelší hodnota.

**Sjednocení mezi obrazovkami z toho vypadne samo, když jsou podlahy sdílené podle TYPU obsahu**
(identifikátor, chip, stav, počet, datum, částka), ne měřené zvlášť v každé tabulce. Datum je pak
stejně široké všude, protože je to totéž datum. Není to zvláštní pravidlo navíc, je to důsledek
prvního.

**Jak ta čísla naměřit, když do běžící aplikace nevidíš.** Třída **C**, je to postup, ne pravidlo.
Postav měřicí lavici: statická stránka, která načte stylesheety a font produktu, vloží do skutečné
tabulky skutečné markup buňky a nechá ji na `width: max-content`. Šířka obsahu je box buňky mínus
její vlastní padding. Nepotřebuje běžící aplikaci, přihlášení ani data.

Dvě podmínky, jinak lavice lže:

1. **Nejdřív ji zkalibruj** proti hodnotám, které někdo naměřil přímo v aplikaci. Dokud lavice
   nereprodukuje známá čísla, neměříš totéž prostředí. Šest hodnot do 0,8 px je dost.
2. **Měř markup komponenty, ne holý řetězec.** Tentýž text v `<span class="svc-tag">` vyšel o 9,5 px
   šířeji než v holé buňce, datum v buňce s tabulkovými číslicemi o 6,8 px, datum s časem o 12,4 px.
   Kdo měří řetězec, dostane podlahu systematicky nízkou, a ořezání se pak objeví až u uživatele.

**PRAVIDLO:** Šířku věš na jméno sloupce, ne na jeho pozici.
**KDY PLATÍ:** Vždy, když se šířky deklarují.
**PROČ:** `col:nth-child(3)` je šířka pozice, ne sloupce. Sloupec vložený kamkoliv jinam než na konec
ji tiše přesune na cizího souseda: nic se nenahlásí, nic nespadne, a projeví se to jako useknutá
hodnota, kterou nikdo nespojí s tím vložením. Pojmenovaná třída na `<col>` cestuje se sloupcem.
Vedlejší zisk: v markupu je pak vidět, co ten sloupec je, i bez otevření stylu.
**TŘÍDA:** C, oporu jsem nenašel, je to řemeslo.

**PRAVIDLO:** Podměřený sloupec se pozná podle výšky řádku, ne podle ořezání.
**KDY PLATÍ:** U sloupců, jejichž obsah smí zalomit, tedy u textu s mezerami.
**PROČ:** Hodnota bez mezer se ořízne nebo přeteče a je to vidět na první pohled. Hodnota s mezerou
se místo toho zalomí, řádek povyroste a tabulka vypadá nepravidelně prořádkovaná. Hlásí se to jako
„nekonzistentní vzhled" a hledá se to v paddingu a v line-heightu, kde to není. Naměřeno: sloupec
o 30 px užší, než jeho nejdelší hodnota potřebovala, udělal ze 54px řádku 69px, obě v jedné tabulce.
**TŘÍDA:** C

**Kdy tuhle metodu nepoužívat:** tabulka o třech čtyřech sloupcích, jejíž sada řádků se za běhu
nemění. Tam stačí to, co říká Carbon, tedy nechat šířky na prohlížeči a hlídat jen odstup.

## Umístění

**PRAVIDLO:** Tabulku dej do hlavní obsahové oblasti stránky a dej jí **dost prostoru, aby zobrazila
data bez zkracování**. **Nedávej tabulku do tabulky** ani do menších kontejnerů, kde se informace
tísní nebo se musí zkracovat.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Data table usage, Placement, verbatim: „Avoid placing data tables inside data tables
or smaller containers where the information can feel cramped or needs truncation."
https://carbondesignsystem.com/components/data-table/usage/

**Šířka versus jiné komponenty:** tabulka může dělit vodorovný prostor s jinými komponentami, ale
Carbon doporučuje **dát tabulce na stránce nejvíc šířky**, aby uživatel viděl hustá data.

**Režimy mezer mřížky:** wide (default, nejvíc prostoru), narrow (komponenta zasahuje do mezery, což
vytvoří žádoucí zarovnání titulku tabulky s ostatní sazbou na stránce), condensed (**pozor na
nezamýšlené vztahy s jinými prvky**, řeš hybridní mřížkou nebo odlišnou barvou plochy). Detail:
[2x grid a breakpointy](../zaklady/2x-grid-a-breakpointy.md).

## Obsah

| Prvek | Pravidlo |
|---|---|
| Titulek tabulky | Musí uživateli objasnit, **co mají data společného** a jaký účel v UI mají |
| Popis | Volitelný, pod titulkem, dá víc informací o datech nebo jejich zdroji |
| Titulky sloupců | **Jedno nebo dvě slova**, která popisují data ve sloupci |
| Přetečení titulku sloupce | **Zalom na dva řádky a pak zkrať.** Celý text ukaž v tooltipu na hover |
| Kapitalizace | Sentence case u titulku, popisu i titulků sloupců |
| Primární tlačítko | Řídí se pravidly pro primární tlačítko a labely akcí |

**ZDROJ:** Carbon, Data table usage, Content.
https://carbondesignsystem.com/components/data-table/usage/
Detail kapitalizace: [UX copy v produktu](../zaklady/ux-copy-v-produktu.md).

## Funkce po jedné

Carbon staví tabulku vrstvením: základní tabulka je povinný základ, k němu se přidávají funkce
(vybíratelné řádky, rozbalovací řádky, menu na řádku, dávkové akce, menu tabulky, filtr).
Zdroj: https://carbondesignsystem.com/components/data-table/style/

### Řazení

- Sloupce lze řadit vzestupně nebo klesajícím způsobem. Ovládání je v hlavičce sloupce.
- Tři stavy: neseřazeno, seřazeno vzestupně, seřazeno klesajícím způsobem.
- **Ikona se zobrazí jen tehdy, když je řazení aktivované.** Ikonu má **jen seřazený sloupec**, ikony
  neseřazených sloupců jsou vidět **jen na hover**.

**Návrhový důsledek:** protože není trvalý vizuální indikátor řaditelnosti, designér **musí anotovat**,
že se tabulka má implementovat s řaditelnými hlavičkami. Detail:
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md).

**ZDROJ:** Carbon, Data table usage, Sorting a Data table accessibility.
https://carbondesignsystem.com/components/data-table/usage/

### Výběr

- Defaultně multi-select: uživatel vybírá checkboxem u řádku, všechny řádky checkboxem v hlavičce.
- Checkboxy v řádcích mají **dva stavy** (zaškrtnuto, nezaškrtnuto). Checkbox „vybrat vše" v hlavičce
  má **tři** (zaškrtnuto, nezaškrtnuto, indeterminate).
- Single-select varianta používá **radio button v prvním sloupci vlevo**. Akce nad vybranou položkou se
  často dávají vpravo do toolbaru, jako primární, ghost nebo ikonová tlačítka.

**ZDROJ:** Carbon, Data table usage, Selectable.
https://carbondesignsystem.com/components/data-table/usage/

### Rozbalovací řádky

**Kdy použít rozbalenou sekci:** na doplňkovou informaci nebo na data, která potřebují další čas na
dotaz.

**PRAVIDLO:** Když obsah v rozbalené oblasti začne být stísněný, **vezmi uživatele na samostatnou
stránku, boční panel nebo tabulku**, aby si informaci prohlédl a dokončil úkoly.
**TŘÍDA:** B
**ZDROJ:** Carbon, Data table usage, Expandable.
https://carbondesignsystem.com/components/data-table/usage/

**Rozbalit vše (batch expansion):** lze přidat do hlavičky, ale **není zobrazené defaultně**. Carbon
k tomu dává výkonový důvod: držením detailní informace v rozbalené sekci šetříš uživateli čas
načítání, protože odkládáš část dotazů, dokud nejsou potřeba. **Rozbalení všech řádků naráz tuhle
výhodu typicky zruší.**

### Toolbar

**PRAVIDLO:** Toolbar je vyhrazený pro **globální** akce tabulky: nastavení tabulky, komplexní filtry,
export, editace dat tabulky. Akce mohou být primární, ghost nebo ikonová tlačítka. **Do toolbaru dej
maximálně pět akcí.** Víc akcí zpřístupni přes overflow menu, combo button nebo podobnou komponentu.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Data table usage, Table toolbar, verbatim: „Include up to five actions within the
table toolbar. More actions can be made available through an overflow menu, combo button, or similar
components." https://carbondesignsystem.com/components/data-table/usage/

**Ghost tlačítko v toolbaru:** Carbon k tomu má konkrétní pravidlo. Tlačítka v toolbaru se často dělají
jako primární, ale **nemusí to tak být vždy**. Když je na stránce jiné tlačítko, které potřebuje
primární styl (typicky v hlavičce stránky), použij v toolbaru **ghost** tlačítko.
Zdroj: https://carbondesignsystem.com/components/button/usage/
Detail: [Tlačítka: varianty a volba](tlacitka-varianty.md)

### Dávkové akce

- Jak uživatel vybere položku, **nad tabulkou se zobrazí lišta dávkových akcí** se sadou možných akcí
  na všechny vybrané položky.
- Carbon k tomu dává zdůvodnění: zvyšuje to efektivitu proti opakovanému provádění stejné inline akce
  na víc položkách.
- **Když je dávkový režim aktivní, ikony jednotlivých akcí a overflow menu na řádku mají být disabled.**
- Z dávkového režimu se vyjde tlačítkem cancel na pravém konci lišty, nebo odvybráním všech položek.

**ZDROJ:** Carbon, Data table usage, Batch actions.
https://carbondesignsystem.com/components/data-table/usage/

### Inline akce na řádku

**PRAVIDLO:** Když overflow menu na řádku obsahuje **méně než tři** volby, nedávej menu, ale nech
akce inline jako ikonová tlačítka.
**PROČ:** Carbon: ušetří to jedno kliknutí a dostupné akce jsou vidět na první pohled.
**TŘÍDA:** B
**ZDROJ:** Carbon, Data table usage, Inline actions, verbatim: „When the overflow menu contains fewer
than three options, keep the actions inline as icon buttons instead. This approach reduces a click and
makes available actions visible at a glance."
https://carbondesignsystem.com/components/data-table/usage/

**Viditelnost overflow menu:** defaultně jsou ikony overflow menu na každém řádku **trvale viditelné**,
což uživateli signalizuje, že na řádcích lze provádět akce. Alternativně lze menu ukázat jen na hover
a focus a snížit tak vizuální šum. **Na dotykových zařízeních** tabulka detekuje, jestli zařízení
podporuje hover, a menu ponechá trvale viditelné, i když je zapnutá varianta „jen na hover".

### Hledání v tabulce

Dvě varianty: sbalená (ikonovým tlačítkem v toolbaru, defaultně zavřená, pod titulkem tabulky, chová
se podle vzoru **active search**) a otevřená (trvale, vlevo pod titulkem, roztažená až k akcím vpravo).
Detail: [Hledání](../vzory/hledani.md).

### Stránkování

Umísti **pod tabulku, naskládané, bez odsazení mezi nimi**. Nikdy nad tabulku.
Detail: [Stránkování](strankovani.md).

### Načítání

**PRAVIDLO:** Když se čeká na zobrazení informace, použij **skeleton stavy, ne spinnery**.
**ZDROJ:** Carbon, Data table usage, Loading, verbatim: „If extra load time is expected to display
information, use skeleton states instead of spinners."
https://carbondesignsystem.com/components/data-table/usage/
**Pozor:** k tvrzením o skeleton screenech má knihovna doložený nález proti. Viz
[Načítání a čekání](../vzory/nacitani-a-cekani.md). Carbonovo pravidlo „ne spinner v tabulce" ale
zůstává rozumné: spinner nad tabulkou nese nulovou informaci o tvaru přicházejících dat.

**Změna filtru nebo faset v tabulce** je jeden ze dvou Carbonových důvodů pro **progresivní načítání**,
protože tabulky tahají z velkých datových sad. Tamtéž.

### Zebra pruhy

Modifikátor pro alternující barvy řádků. Carbonovo zdůvodnění: **usnadní uživateli skenování
vodorovné informace v řádku**.
Zdroj: https://carbondesignsystem.com/components/data-table/usage/

**Poznámka k rozporu s domácím pravidlem:** v `sheets/` platí domácí pravidlo držet **gridlines
viditelné**, protože existující reporty je mají. Zebra pruhy jsou jiný mechanismus na tentýž problém
(vedení oka po řádku). Když stavíš tabulku ve webovém UI, zebra pruhy jsou legitimní volba. Když
stavíš list v Google Sheets, platí domácí pravidlo. Viz [sheets](../../sheets/znalostni-baze.md)
a [STATUS.md](../../STATUS.md), sekce dluhů.

### Hover

**PRAVIDLO:** Hover stav řádku nech **vždy zapnutý**, i když řádek není interaktivní.
**PROČ:** Carbon: pomáhá uživateli vizuálně skenovat sloupce dat v jednom řádku.
**TŘÍDA:** B
**ZDROJ:** Carbon, Data table usage, Hover, verbatim: „The data table's row hover state should always
be enabled as it can help the user visually scan the columns of data in a row even if the row is not
interactive." https://carbondesignsystem.com/components/data-table/usage/

## Tabulka v dialogu: co nedělat

Carbon tabulku v dialogu nedoporučuje. Když ji tam potřebuješ:

- Drž ji **co nejjednodušší** s omezenými interakcemi.
- Výběr řádků, na které se aplikuje akce dialogu, je v pořádku.
- **Dávkové akce a dávkovou editaci uvnitř modalu nedělej.**
- U menších množin dat nebo výběrů zvaž **structured list, dropdown nebo sadu dlaždic**.

Detail a zdůvodnění: [Dialogy a panely](../vzory/dialogy-a-panely.md).

## Prázdná tabulka

**PRAVIDLO:** Prázdný stav **nahradí tabulku včetně hlavičky a zápatí**, nepřidá se k prázdné tabulce.
Přístupnostní důvod je v [Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md).
Detail rozvržení prázdného stavu v tabulce: [Prázdné stavy](../vzory/prazdne-stavy.md).

## Kdy použít něco jiného

| Alternativa | Kdy |
|---|---|
| Structured list | Jednoduchý seznam, jen čtení, párování termín a hodnota, bez řazení a bez vnořování |
| Contained list | Seznam položek v malém nebo uzavřeném prostoru, ne na celé stránce |
| Accordion | Skupiny obsahu k rozbalení, ne tabulková data |
| Tile set | Malá množina strukturovaných voleb, hlavně když je potřeba vizuál |

**ZDROJ:** Carbon, Data table usage, Similar components a Structured list usage.
https://carbondesignsystem.com/components/structured-list/usage/
Detail rozhodování: [Volba komponenty](../zaklady/volba-komponenty.md).

## Structured list

Krátká charakteristika, protože je to nejbližší alternativa tabulky.

- Zobrazuje jednoduchý seznam se značným množstvím položek ve víc řádcích. Obsah lze stohovat, aby
  v datech vznikla hierarchie.
- Řádky mohou být **read-only nebo vybíratelné**.
- **Kdy použít:** k prohlížení informace nebo k výběru položky ve skupině v nejjednodušší formě. K
  zobrazení popisu a detailní informace, představení funkcí, nebo porovnání cenových plánů.
- **Kdy nepoužít:** **vnořování se nedoporučuje**, structured list je na jednoduchá data. Když máš
  komplexní obsah, použij tabulku, která vnořování podporuje a zobrazí větší množinu obsahu.
- Vybíratelný structured list: **defaultně nic nevybráno, jen jeden řádek vybraný najednou.** Tým může
  dodat logiku na předvýběr. **Když je potřeba výběr víc řádků, použij tabulku.**
- Řádek: max **tři odstavce** textu na řádek, sentence case.
- Dvě výšky (default, condensed), dvě zarovnání (hang, flush). **Flush zarovnání není dostupné
  s výběrem.**
- Barevné pozadí řádku je dostupné **jen u hang zarovnání**.

**ZDROJ:** Carbon, Structured list usage, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/components/structured-list/usage/

---

## Co tahle nota neřeší

- Hromadné akce nad stránkovanou a filtrovanou množinou (co znamená „vybrat vše", co s výběrem při přepnutí stránky, částečné selhání dávky) jsou v [Hromadné akce](../vzory/hromadne-akce.md).
- Tokeny barev a konkrétní rozestupy tabulky. Carbon je má na stránce `style`, odkud je záměrně
  nepřebírám.
- „AI presence" vizuál tabulky. To je Carbonova identita.
- Dataviz, grafy a palety pro data. Zatím jen [sheets](../../sheets/znalostni-baze.md).
- Editovatelnou tabulku a data spreadsheet. Carbon je má v „Carbon for IBM Products", což v přečtené
  kopii není.
- Overflow menu a combo button jako komponenty. Tamtéž.

## Zdroj

IBM Carbon Design System, Data table usage, Data table style (jen strukturní části), Data table
accessibility a Structured list usage. Lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/components/data-table/usage/
Carbon u tabulky neuvádí sekci References, žádné externí zdroje k ní nemá. Třída **B**.
