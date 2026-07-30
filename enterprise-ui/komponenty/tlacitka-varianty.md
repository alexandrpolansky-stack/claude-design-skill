# Tlačítka: varianty, skupiny, zarovnání

Taxonomie pěti variant, jejich role v toku a pravidla pro skládání do skupin.

**Tvrdá pravidla o tlačítkách (kolik jich smí být, kontrast, terč, stavy, destruktivní akce) jsou
v [Tlačítka: varianty, hierarchie, stavy, destruktivní akce](../../ux-design/pravidla/tlacitka.md).
Ta nota má tvrdší zdroje (WCAG, Fitts, měření) a v konfliktu vyhrává.** Tahle nota doplňuje jen to,
co tam není: pojmenovanou taxonomii variant, doporučené kombinace ve skupinách a zarovnání.

Související: [Volba komponenty](../zaklady/volba-komponenty.md) ·
[Běžné akce](../vzory/bezne-akce.md) · [Dialogy a panely](../vzory/dialogy-a-panely.md) ·
[Prázdné stavy](../vzory/prazdne-stavy.md) · [2x grid a breakpointy](../zaklady/2x-grid-a-breakpointy.md)

---

## Rychlé rozhodnutí

1. **Tlačítko není navigace.** Když akce vede uživatele na jinou stránku, použij **odkaz**.
2. **Primární tlačítko jednou na obrazovku.** Výjimka: dočasný tok spuštěný z obsahu stránky (viz níže).
3. **Sekundární tlačítko nikdy samostatně** a nikdy na pozitivní akci. Je to „Zrušit" nebo „Zpět"
   v páru s primárním.
4. **Na plné stránce je primární tlačítko vlevo** a nalevo od sekundárního. **V průvodci a dialogu
   vpravo** a napravo od sekundárního.
5. **Víc než tři akce = menu button**, ne čtyři tlačítka vedle sebe.
6. **Tlačítka ve skupině mají stejnou šířku**, danou nejdelším labelem. Ghost do toho nepočítej.
7. **Nemíchej velikosti tlačítek v jedné skupině.**
8. **Icon-only tlačítko vždycky s tooltipem.** Bez výjimky, i u „samozřejmé" ikony.
9. **Danger nikdy jako icon-only.**
10. **Label tlačítka se při přetečení zalomí na druhý řádek.** Nikdy nezkracuj výpustkou.
11. **Ne každá stránka potřebuje primární tlačítko.**

---

## Pět variant a jejich funkce

Carbon je explicitní v tom, že varianta není vzhled, ale **signál funkce**, a že rozhodnutí musí být
konzistentní napříč produktem.

| Varianta | Funkce podle Carbonu |
|---|---|
| **Primary** | Hlavní výzva k akci na stránce. Má se objevit **jen jednou na obrazovku** (nepočítá se hlavička aplikace, modál a side panel) |
| **Secondary** | Sekundární akce. **Použitelná jen spolu s primárním tlačítkem.** V páru nese negativní akci sady, například „Zrušit" nebo „Zpět". **Ne samostatně a ne na pozitivní akci** |
| **Tertiary** | Méně výrazné, někdy **nezávislé** akce. Funguje samostatně i v páru s primárním. Hodí se na podúlohy na stránce, kde už je primární tlačítko pro hlavní a finální akci |
| **Ghost** | Nejmenší důraz, často spolu s primárním. V progresivním toku: primární dopředu, sekundární „Zpět", ghost „Zrušit" |
| **Danger** | Akce s možným **destruktivním dopadem na uživatelova data** (smazat, odebrat). Má tři styly: primary, tertiary, ghost |

**ZDROJ:** Carbon, Button usage, Variants, verbatim k primárnímu: „Primary buttons should only appear
once per screen (not including the application header, modal dialog, or side panel)." A k sekundárnímu:
„Do not use a secondary button in isolation and do not use a secondary button for a positive action."
https://carbondesignsystem.com/components/button/usage/

### Kdy tlačítko vůbec nepoužívat

**PRAVIDLO:** **Nepoužívej tlačítka jako navigační prvky.** Když je žádaná akce dostat uživatele na
novou stránku, použij **odkaz**.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, When not to use, verbatim: „Do not use buttons as navigational
elements. Instead, use links when the desired action is to take the user to a new page."
https://carbondesignsystem.com/components/button/usage/

**Praktický důsledek:** rozhoduje, co se stane, ne jak to má vypadat. „Zobrazit detail" jako přechod
na jinou URL je odkaz, i když ho vizuálně nakreslíš jako tlačítko. Screen reader oznámí roli a ta
musí odpovídat.

---

## Sedm velikostí

| Velikost | Kdy podle Carbonu |
|---|---|
| Extra small | Když je **omezený vertikální prostor** nebo stísněný layout |
| Small | Když je tlačítko párované s **32px small** vstupním polem |
| Medium | Když je tlačítko párované s **40px medium** vstupním polem |
| **Large (productive)** | **Nejběžnější velikost v softwarových produktech.** Páruje se s 14px tělem textu |
| Large (expressive) | Větší expresivní typo dává rovnováhu k **16px tělu textu**. Používá web IBM.com v bannerech |
| Extra large | Když tlačítko **doráží k okraji větší komponenty**: modál, side panel, úzký tearsheet |
| 2XL | Když tlačítko doráží k okraji **komponenty na celou obrazovku**, například velký tearsheet |

**PRAVIDLO:** **Nemíchej různé velikosti tlačítek v jedné skupině.**
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Button sizes, verbatim: „We do not recommend mixing different button
sizes in button groups." https://carbondesignsystem.com/components/button/usage/

**Jak to čti pro vlastní produkt:** Carbon má sedm velikostí proto, že tlačítko se páruje s výškou
vstupního pole a s velikostí písma vedle sebe. Nepřebírej sedm stupňů, přeber **pravidlo párování**:
výška tlačítka se řídí tím, s čím stojí v jedné řadě. Konkrétní hodnoty jsou v Carbonových tokenech,
ty záměrně nepřebíráme. Viz [Vrstvy a vzory](../zaklady/vrstvy-a-vzory.md).

---

## Důraz (emphasis)

**Klíčové pozorování Carbonu:** nemusíš tlačítka použít v pořadí, které jejich labely napovídají.
Sekundární tlačítko má menší vizuální prominenci než primární, ale je **tonálně těžké**. Když layout
potřebuje víc akcí (toolbary, seznamy dat, dashboardy), je lepší volba **tertiary nebo ghost**.

Dvě best practices, které Carbon jmenuje:

1. **Jedno tlačítko s vysokým důrazem.** Layout by měl obsahovat jedno tlačítko s vysokým důrazem,
   které dává jasně najevo, že ostatní jsou v hierarchii méně důležitá.
2. **Víc úrovní důrazu.** Tlačítko s vysokým důrazem může doplnit střední a nízký důraz.
   **Seskupuj jen akce, které mají mezi sebou vztah.**

**ZDROJ:** Carbon, Button usage, Emphasis.
https://carbondesignsystem.com/components/button/usage/

**Souvislost s domácím pravidlem:** [`ux-design/pravidla/tlacitka.md`](../../ux-design/pravidla/tlacitka.md)
říká „nejvýš jedno primární tlačítko na vizuálně oddělenou sekci" a „nejvýš tři akcentní na pohled".
Carbon je na úrovni stránky **striktnější** (jedno na obrazovku), ale vyjímá hlavičku aplikace, modál
a side panel, což je fakticky totéž rozdělení na oblasti. **Bezpečné čtení: jedno primární na
oblast, a když jich je na obrazovce víc než jedna, zkontroluj, že spolu vizuálně nesoutěží.**

---

## Zarovnání

Carbon říká, že tlačítka jsou v tomhle unikátní: jejich zarovnání závisí na tom, **kde se objeví**
a jestli jsou uvnitř jiné komponenty.

| Zarovnání | Kde |
|---|---|
| **Vlevo** | Výzvy k akci v bannerech, formuláře uvnitř stránky, vnořená tlačítka v komponentách jako dlaždice |
| **Vpravo** | Inline notifikace, tlačítka inline u polí, datové tabulky, progresivní formuláře, průvodci, dialogy s jedním tlačítkem |
| **Na celou šířku** | Dialogy, side panel, malé dlaždice |

**ZDROJ:** Carbon, Button usage, Alignment.
https://carbondesignsystem.com/components/button/usage/

**Odůvodnění, které Carbon dává k plné stránce:** „When the browser window is large and the user is
scrolling to read, it's best to have the primary button where the user's attention has been focused
all along." Naopak v průvodci, kde uživatel prochází sérií kroků, primární akce tradičně sedí vpravo
dole.

### Pořadí ve skupině (Carbon si tohle pravidlo změnil)

**PRAVIDLO:** Na plné stránce je primární tlačítko **zarovnané vlevo a stojí nalevo** od
sekundárního nebo tertiary. V průvodcích a dialogových okénkách je **zarovnané vpravo a stojí
napravo** od sekundárního nebo tertiary.
**KDY PLATÍ:** Vždy, u horizontálně řazených skupin.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Horizontally arranged groups. Carbon k tomu má explicitní poznámku,
verbatim: „This guidance has changed. Previously we advocated maintaining the primary button position
to the right of the secondary button when the button group was left-aligned. After talking to teams
and doing more research, we've revised our position."
https://carbondesignsystem.com/components/button/usage/

**Proč to zmiňuju:** starší produkty postavené na Carbonu mají levo zarovnanou skupinu s primárním
tlačítkem **napravo**. Není to chyba implementace, je to stará verze pravidla. Když sjednocuješ
existující produkt, čekej oba vzory a rozhodni jeden.

### Fixed, fluid a hanging

| Pojem | Co znamená |
|---|---|
| **Fixed width** | Šířku určuje label. Carbon k tomu má fixní vnitřní odsazení: 16px vlevo, **64px vpravo** od labelu |
| **Fluid width** | Plovoucí primární, sekundární nebo tertiary tlačítko zabírá **určený počet sloupců** responzivní mřížky |
| **Hanging** | Zarovnaný je **label tlačítka na mřížku**, ne kontejner |
| **Non-hanging** | Zarovnaný je **kontejner tlačítka na mřížku**. Platí pro tlačítka s viditelným kontejnerem |

**PRAVIDLO:** **Fluid tlačítka jsou vždycky lepší než fixed width** v layoutu. Když je to možné, nastav
pozici kontejneru tlačítka relativně k responzivní mřížce a **srovnej šířku tlačítka se šířkou
ostatních prvků na stránce**.
**KDY PLATÍ:** V layoutu stránky. Pro tertiary Carbon fluid nedoporučuje.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Fluid width button, verbatim: „Fluid width buttons are always
preferable to fixed width default buttons in a layout."
https://carbondesignsystem.com/components/button/usage/

**Kde fluid nesmí být vlevo:** Carbon má obecné pravidlo, že **fluid tlačítka nejsou nikdy zarovnaná
vlevo** v layoutu ani v kontejneru. Jsou zarovnaná vpravo, nebo zabírají celou šířku kontejneru.

**Hanging přes gutter:** hanging zarovnání se používá k **seskupení sekcí mezi komponentami
a tlačítky, které se navzájem přímo ovlivňují**. Carbon k tomu nabízí narrow gutter mode (16px),
nebo alternativu: chovat se ke skupině tlačítek jako k **jednomu objektu** na mřížce, kde každé
tlačítko zabírá 50 % kontejneru a mezi nimi je programový 16px gutter. Detail gutter módů
v [2x grid a breakpointy](../zaklady/2x-grid-a-breakpointy.md).

---

## Skupiny tlačítek

**Kdy skupina a kdy menu:**

| Počet akcí | Řešení |
|---|---|
| 2 nebo 3 | **Skupina tlačítek** |
| 4 a víc | **Menu button**, aby akce nezabíraly tolik místa |
| Hodně běžných akcí nebo funkcí | **Toolbar** |

**ZDROJ:** Carbon, Button usage, Button groups versus menu buttons, verbatim: „Button groups should be
used when there are either two or three actions that a user needs to consider. Any more than three
actions should be grouped meaningfully using menu buttons."
https://carbondesignsystem.com/components/button/usage/

### Doporučené kombinace

**Se primárním tlačítkem:**

| Počet | Kombinace |
|---|---|
| 2 | Primary + secondary · Primary + tertiary · Primary + ghost · Primary + danger tertiary · Danger primary + secondary · Danger primary + ghost |
| 3 | Primary + secondary + tertiary · Primary + secondary + ghost · Primary + 2× secondary · Primary + 2× tertiary · Primary + tertiary + danger tertiary |

**Bez primárního tlačítka:**

| Počet | Kombinace |
|---|---|
| 2 | 2× tertiary · Tertiary + ghost · 2× ghost |
| 3 | 3× tertiary · 2× tertiary + 1× danger tertiary |

**ZDROJ:** Carbon, Button usage, Button group combinations.
https://carbondesignsystem.com/components/button/usage/

**Doporučení Carbonu k třem a víc akcím:** kvůli vizuální váze sekundárního tlačítka doporučuje
v layoutech s **víc než třemi** výzvami k akci použít **tertiary nebo ghost**.

### Šířka ve skupině

**PRAVIDLO:** Když používáš skupinu souvisejících tlačítek (**ghost nepočítáno**), mají mít
**všechna stejnou šířku**. Šířku obvykle určuje **nejdelší label**.
**KDY PLATÍ:** Ve skupinách souvisejících tlačítek, včetně toolbaru a batch actions toolbaru.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Button width in button groups. Carbon doporučení výslovně rozšiřuje
i na toolbar a batch actions toolbar. https://carbondesignsystem.com/components/button/usage/

### Vertikálně naskládané skupiny

Vertikální skupiny jsou v produktech běžné: šetří místo v úzkých sloupcích a občas v side panelech.
Naskládaná tlačítka mohou být fluid a doražená do side panelu, nebo mít okolo 16px odstup. **Ten
16px odstup umožňuje ve vertikální skupině použít tertiary tlačítko.**

**PRAVIDLO:** Ve vertikálně naskládané skupině je **primární tlačítko vždy nahoře** a sekundární
nebo tertiary pod ním.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Vertically stacked button groups.
https://carbondesignsystem.com/components/button/usage/

### Oddělovač u fluid skupin

Mezi všemi fluid tlačítky je **1px hranice**, která přidává **rozlišení 3:1 mezi dvěma interaktivními
prvky UI**. Carbon to označuje za doporučenou funkci **kvůli přístupnosti**.

**ZDROJ:** Carbon, Button usage, Fluid button border.
https://carbondesignsystem.com/components/button/usage/
Souvislost: WCAG 1.4.11 Non-text Contrast, viz [`ux-design/pravidla/tlacitka.md`](../../ux-design/pravidla/tlacitka.md),
sekce „Co nenese text, musí mít kontrast 3:1".

---

## Primary: jedna výjimka z pravidla jednoho primárního

**PRAVIDLO:** Na stránce může být dočasně **dvě primární tlačítka**, když uživatel interakcí
s obsahem stránky spustil další tok, který má vlastní primární akci. Uživatel něco spustil
s **úmyslem soustředit se na jiný tok**, takže dvě primární tlačítka jsou přijatelná.
**KDY PLATÍ:** Jen tady. Carbon říká, že tohle je **jediný** scénář, kdy jsou dvě primární akce na
stránce doporučené.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Temporary flows with primary action, verbatim: „This is the only
scenario where having two primary actions on a page is advised." Příklad, který Carbon uvádí: datová
tabulka s primární akcí a otevřený side panel s vlastní primární akcí.
https://carbondesignsystem.com/components/button/usage/

### Ne každá stránka potřebuje primární tlačítko

**PRAVIDLO:** Když je hlavní účel stránky **interakce s jinými komponentami nebo čtení obsahu**, ne
spuštění akce, použij na podpůrné akce **tertiary a ghost** tlačítka.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Not every page needs a primary button. Příklad Carbonu: stránka,
jejímž primárním záměrem je prezentovat obsah, s filtrováním a editací jako tertiary a ghost.
https://carbondesignsystem.com/components/button/usage/

**Proč je tohle důležité pro Clauda:** typická chyba generovaného UI je dát primární tlačítko na
každou stránku, protože „stránka má mít CTA". Na čtecí a přehledové stránce je správná odpověď
žádné primární tlačítko.

### Focus a klávesa Enter

Primární tlačítko je **výchozí akce**. Když se objeví dialog, primární tlačítko typicky **přebírá
focus**. Ve formuláři, když je focus na komponentě, která nereaguje na `Enter`, **stisk `Enter`
aktivuje primární tlačítko**.

**ZDROJ:** Carbon, Button usage, Primary button focus.
https://carbondesignsystem.com/components/button/usage/
Pozor: u destruktivních dialogů má výchozí focus jít na **Zrušit**, ne na primární akci. Viz
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md) a [Dialogy a panely](../vzory/dialogy-a-panely.md).

---

## Tertiary: tři situace, kde je to správná volba

| Situace | Proč tertiary |
|---|---|
| **Hlavička stránky** | Primární tlačítko v hlavičce je problém: obsah pod hlavičkou pravděpodobně bude mít vlastní primární akci, teď nebo v příští verzi. A tlačítko v hlavičce má i tak významnou prominenci díky **hierarchickému umístění nahoře** |
| **Skupina tlačítek** | Když je jedno primární a dvě další akce se **sdílenou důležitostí** |
| **Prázdné stavy** | U prázdného stavu na stránce, která už má definovanou primární akci, je tertiary **ideální řešení pro spuštění nového toku úloh** |

**ZDROJ:** Carbon, Button usage, Tertiary button, best practices.
https://carbondesignsystem.com/components/button/usage/
Souvislost: [Prázdné stavy](../vzory/prazdne-stavy.md).

**Výjimka u hlavičky:** když se rozhodne, že tlačítko v hlavičce stránky má být napříč všemi taby
primární, Carbon žádá **ověřit, že žádný obsah pod hlavičkou neobsahuje další primární akci**.

**Zarovnání tertiary:** má zůstat **zarovnané s obsahem stránky** a mít dostatečné odsazení ze všech
stran. **Tertiary se nemá používat ve fluid uspořádání.**

---

## Ghost: kde funguje a jak ho zarovnat

Ghost má **nejmenší prominenci** ze všech variant. Je subtilnější, což ho dělá ideálním pro
**doplňkové akce**. Funguje nejlépe, když je doražený ke kontejneru nebo horizontálně seskupený
s jinými prvky.

| Situace | Proč ghost |
|---|---|
| **Toolbar datové tabulky** | Tlačítka v toolbaru tabulky se často kreslí jako primární, ale nemusí to tak být. **Když je na stránce jiné tlačítko, které potřebuje primární styl, použij v toolbaru ghost** |
| **Produktivní karty na dashboardu** | Na dashboardu s víc produktivními kartami ghost funguje dobře, protože **přitahuje méně pozornosti než tertiary** |
| **Zrušit v progresivním toku** | Ghost funguje dobře jako „Zrušit", protože přitahuje méně pozornosti: **uživatel musí tlačítko cíleně najít a kliknout**. V tearsheetech jsou tlačítka fluid, což není vhodné použití pro tertiary |

**ZDROJ:** Carbon, Button usage, Ghost button, best practices.
https://carbondesignsystem.com/components/button/usage/
Souvislost: [Datové tabulky](datove-tabulky.md), [Dlaždice a karty](dlazdice-a-karty.md).

**Zarovnání ghost tlačítka:** funguje dobře zarovnaný **do rohu kontejneru**. Obecné pravidlo pro
vertikální zarovnání ghost tlačítka s ostatním obsahem: zajisti, aby se **jeho label zarovnal
s textem** jinde na stránce. Ghost lze rozšířit na **plnou šířku kontejneru**, ale jen u menších
kontejnerů, například side panel **480px (medium) a méně**. Aby ghost ve vertikálním uspořádání
v kontejneru vypadal zarovnaně, doporučuje Carbon, aby se **dotýkal aspoň dvou hran kontejneru**.

---

## Danger: tři styly podle role v toku

Danger je pro akce s **destruktivním dopadem**, například „Smazat", „Odebrat", „Zastavit". Má tři
styly: **primary, tertiary, ghost**.

| Role destruktivní akce | Styl |
|---|---|
| **Vyžadovaný nebo primární krok** workflow | Danger **primary** |
| Jedna z několika akcí, ze kterých uživatel může vybírat | Nižší důraz: danger **tertiary** nebo danger **ghost** |

**ZDROJ:** Carbon, Button usage, Danger button, verbatim: „Destructive actions that are a required or
primary step in a workflow should use the primary danger button style. However, if a destructive
action is just one of several actions a user could choose from, then a lower emphasis style like the
tertiary danger button or the ghost danger button may be more appropriate."
https://carbondesignsystem.com/components/button/usage/

**Tohle je stejný princip jako v knihovně.** [`ux-design/pravidla/tlacitka.md`](../../ux-design/pravidla/tlacitka.md),
sekce „Variantu destruktivního tlačítka vyber podle role v toku", říká totéž. Knihovna k tomu navíc
přidává tvrdší pravidla: destruktivní akci nikdy nenes jen barvou, do labelu napiš, co konkrétně
zmizí. **Ta pravidla platí a Carbon je nenahrazuje.**

**PRAVIDLO:** **Danger tlačítko nemůže existovat jako icon-only.**
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Danger buttons cannot be used in an icon only form. Odůvodnění
Carbonu: danger může být kritická akce a má být na tlačítku, které nese **vyšší důraz spolu
s vizuálním labelem**. https://carbondesignsystem.com/components/button/usage/

---

## Ikony v tlačítkách

**Základní postoj Carbonu:** ikony objasňují akci a přitahují k tlačítku pozornost, ale mají se
používat **skoupě**, protože přemíra vytváří vizuální šum a snižuje použitelnost. **Když použiješ
tlačítko s ikonou v jedné části UI, neznamená to, že musíš přidat ikony ke všem ostatním tlačítkům.**

Pravidla, která Carbon jmenuje:

- Ikona je **napravo od labelu**.
- Ikona v tlačítku musí **přímo souviset s akcí**, kterou uživatel provádí.
- Ikona musí **odpovídat barevné hodnotě labelu** v tlačítku.
- Ve skupině tlačítek buď **ikona u každého tlačítka, nebo u žádného**.
- U ikon používej **výchozí variantu**, ne vyplněnou. Výjimka jsou stavové ikony, které mají vlastní
  definovanou ikonu.

**ZDROJ:** Carbon, Button usage, Button with icon.
https://carbondesignsystem.com/components/button/usage/

**Poznámka k velikostem:** Carbon uvádí 16px ikonu v tlačítkách a 20px ve large expressive. To je
konkrétní hodnota jeho vlastního systému, neber ji jako univerzální pravidlo, ale jako důkaz, že
velikost ikony se odvozuje od velikosti tlačítka a písma.

### Univerzální akce s ustálenými ikonami

Carbon definuje uzavřenou sadu akcí, u kterých je ikona natolik zavedená, že se dá vedle labelu
použít bez rizika záměny. **Důvod: aby stejná ikona neznamenala v jiném kontextu jinou akci.**

Akce, které Carbon do té sady zařadil, spolu s významem ikony:

| Akce | Ustálený význam ikony |
|---|---|
| Create / Add | plus |
| Edit | tužka |
| Copy | dva překryté listy |
| Delete | koš |
| Remove | mínus |
| Export | odchod z rámečku |
| Upload | šipka nahoru |
| Download | šipka dolů |
| Play / Start | trojúhelník |
| Pause | dvě svislé čárky |
| Stop | čtverec |
| Refresh | kruhová šipka |

**ZDROJ:** Carbon, Button usage, Universal actions with well-established icons. Seznam akcí je
Carbonův; **konkrétní glyfy z Carbonovy ikonové knihovny nepřebíráme**, viz
[Vrstvy a vzory](../zaklady/vrstvy-a-vzory.md). Sloupec s významem ikony je popis, ne kopie.
https://carbondesignsystem.com/components/button/usage/

**PRAVIDLO:** **Nepoužívej ikonu z téhle sady pro jinou univerzální akci.** Použití těch ikon na jiné
akce mate očekávaný výsledek.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Do not use a defined icon to represent a different universal action.
https://carbondesignsystem.com/components/button/usage/

**Ikona odkazu do nového tabu:** Carbon má samostatné pravidlo, že **akce, která uživatele vystřelí
do jiného tabu**, má mít launch ikonu, a to i když je obsah nového tabu součástí stejného produktu.
Cíl akce má být jasný z labelu a okolního kontextu. Typická místa: levá navigace, side panel, karty,
modály.

### Icon-only tlačítka

**PRAVIDLO:** Icon-only tlačítka používej **skoupě**. Carbon k tomu cituje výzkum:
„For most situations, users learn correct interpretations better with text alone than with icons
alone." (Wiedenbeck, S, 1999)
**KDY PLATÍ:** Vždy. Carbon jmenuje dva případy, kdy je icon-only doporučené:
1. Ikona je **standardizovaná a rozpoznatelná bez labelu**, nebo reprezentuje akci se silným
   vizuálním atributem (příklad Carbonu: špendlík pro připnutí).
2. **Nedostatek místa a víc akcí**, takže je potřeba toolbar s ikonovými tlačítky.
**TŘÍDA:** A pro citovaný výzkum (Wiedenbeck 1999, peer-reviewed), B pro Carbonovo rozhodovací
kritérium.
**ZDROJ:** Carbon, Button usage, Icon only buttons. Původní studie: Wiedenbeck, S (1999). The use of
icons and labels in an end-user application program: An empirical study of learning and retention.
Behavior & Information Technology, 18(2), s. 68-82.
https://carbondesignsystem.com/components/button/usage/

**PRAVIDLO:** **Icon-only tlačítko vždy vyžaduje tooltip** s textem, co by tlačítko po kliknutí
udělalo. **Bez ohledu na to, jak rozpoznatelná ikona je, a bez ohledu na to, jestli je akce
v seznamu univerzálních akcí.**
**KDY PLATÍ:** Vždy, bez výjimky.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Tooltips for icon only buttons, verbatim: „Regardless of how
recognizable an icon may or may not be, or whether that action lies within the universal actions
list, a tooltip is always required with text explaining what the icon button would do if clicked."
https://carbondesignsystem.com/components/button/usage/
Detail: [Tooltip a toggletip](tooltip-a-toggletip.md).

**Přístupnostní poznámka Carbonu:** icon-only tlačítka, která nemají trvale zobrazený textový label,
**vystavují svůj label na hover a focus**. Když se icon-only tlačítko používá k otevření menu, je to
v Carbonu **jiná komponenta** (dropdown, overflow menu), ne tlačítko. Detail:
[Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md), [Výběr ze seznamu](vyber-ze-seznamu.md).

**Icon-only varianty:** může vzít formu primary, secondary, tertiary nebo ghost, ale **nejčastěji je
stylované jako primary nebo ghost**.

---

## Label a přetečení

**PRAVIDLO:** Label je **nejdůležitější prvek tlačítka**, protože komunikuje akci, která se provede.
Použij formulku **{verb} + {noun}**, s výjimkou běžných akcí jako „Done", „Close", „Cancel", „Add"
nebo „Delete".
**KDY PLATÍ:** Vždy. Výjimky existují tam, kde by délka labelu způsobila problém v kompaktním UI
nebo negativně ovlivnila překlad, ale formulka zůstává best practice.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Button label.
https://carbondesignsystem.com/components/button/usage/
Detail včetně toho, co z toho platí v češtině: [UX copy v produktu](../zaklady/ux-copy-v-produktu.md).

**Zarovnání labelu:** v Carbonovém tlačítku je label **vždy zarovnaný vlevo, ne na střed**. Ikona
v tlačítku s labelem je **vpravo**, v icon-only tlačítku je ikona **na střed**.

**PRAVIDLO:** Když je label na dostupný prostor moc dlouhý, má **přetéct a zalomit se na druhý
řádek**. **Nezkracuj label tlačítka výpustkou.**
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Overflow content, verbatim: „We do not recommend truncating a button
label." https://carbondesignsystem.com/components/button/usage/
Souvislost: [Přetečení a truncation](../vzory/preteceni-a-truncation.md).

**RTL:** u jazyků zprava doleva se **celé tlačítko horizontálně zrcadlí**. Label je zarovnaný vpravo,
ikona vlevo.

---

## Načítání v tlačítku

Tlačítko může mít **inline loading**, který dává vizuální zpětnou vazbu, že akce probíhá. **Během
inline loadingu je tlačítko disabled.**

**ZDROJ:** Carbon, Button usage, Loading.
https://carbondesignsystem.com/components/button/usage/
Detail k prahům čekání a k tomu, kdy inline loading a kdy jiný indikátor:
[Načítání a čekání](../vzory/nacitani-a-cekani.md). Rozdíl disabled a read-only:
[Disabled vs. read-only](../vzory/disabled-vs-read-only.md).

---

## Klávesová obsluha a implementační poznámky

Tlačítko se dá **dosáhnout `Tab`** a **spustit `Space` nebo `Enter`**. Myší se dá spustit **kliknutím
kdekoli v kontejneru tlačítka**.

Tři poznámky, které Carbon dává pro vlastní implementaci:

1. Když je **odkaz „přeúčelovaný" na tlačítko**, musí být nakódovaný tak, aby ho aktivovala i klávesa
   `Space` (odkazy se výchozím chováním aktivují jen `Enter`).
2. **Toggle tlačítka** lze podpořit přepínáním `aria-pressed` mezi `"true"` a `"false"`, nebo změnou
   názvu, která odpovídá změně tvaru ikony (příklad Carbonu: „play" / „pause").
3. Carbon odkazuje na **ARIA authoring practices** pro tlačítko.

**ZDROJ:** Carbon, Button accessibility.
https://carbondesignsystem.com/components/button/accessibility/
Detail: [Klávesnice a focus](../zaklady/klavesnice-a-focus.md),
[Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md).

---

## Co tahle nota neřeší

- **Kolik tlačítek smí být na pohledu, kontrast, velikost terče, pět stavů, state layer, disabled
  antipattern, destruktivní akce jako celek.** Všechno je v
  [`ux-design/pravidla/tlacitka.md`](../../ux-design/pravidla/tlacitka.md) a má tam tvrdší zdroje.
- Konkrétní barvy, výšky, tokeny a odsazení. Carbon je má na stránce `style`, záměrně je nepřebírám.
- Carbonovu ikonovou knihovnu. Přebírám jen **seznam akcí**, u kterých je ikona ustálená.
- Menu buttons a toolbar jako komponenty. Carbon je má mimo přečtenou kopii.
- Fixed button bars a tearsheet: komponenty z IBM Products, v přečtené kopii nejsou.
- Fluid a hanging tlačítka nejsou podle Carbonu dostupná pro produkční použití. Bere se to jako
  směr, ne jako hotová specifikace.

## Zdroj

IBM Carbon Design System, Button usage a Button accessibility, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/components/button/usage/

Carbon u tlačítek uvádí čtyři externí zdroje: Mehmet Goktürk, *The Glossary of Human Computer
Interaction, Chapter 37* (Fittsův zákon, Interaction Design Foundation); Jakob Nielsen, *OK-Cancel or
Cancel-OK? The Trouble With Buttons* (NN/g, 2008); Artem Syzonenko, *Buttons on the web: placement
and order* (UX Collective, 2019); Wiedenbeck, S (1999), studie o ikonách a labelech. Z toho je
Wiedenbeck 1999 peer-reviewed (**třída A**), zbytek je publikovaná konvence (**třída B**).
Carbonova vlastní doporučení bez citace jsou **třída B**.
