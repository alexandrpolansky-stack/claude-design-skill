# Taby

Kdy taby a kdy něco jiného. Tři varianty, zarovnání na mřížku a rozdíl mezi automatickým a manuálním
tablistem.

Související: [Volba komponenty](../zaklady/volba-komponenty.md) ·
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md) ·
[Navigace v hierarchii](navigace-v-hierarchii.md)

---

## Rychlé rozhodnutí

1. Skupiny souvisejícího obsahu ve stejném kontextu = taby.
2. Přepínání formátů **stejného** obsahu nebo filtrování stejného obsahu = **content switcher**.
3. Krokový lineární proces = **progress indicator**.
4. Uživatel potřebuje obsah **porovnávat** = **ani jedno**, zobraz vedle sebe.
5. V komponentě (modal, karta) používej **line taby**, ne contained.
6. **Nepoužívej vertikální taby jako navigaci.**
7. Vždy je jeden tab vybraný. Minimum dva taby (u zavíratelných jeden).
8. Label jedno až dvě slova. Na malých šířkách taby **scrollují, nezalamují se ani nestohují**.
9. Grid aware zarovnání jen do čtyř tabů a jen u contained.
10. Panel se dlouho načítá = **manuální** tablist, a musíš to anotovat do návrhu.

---

## Kdy taby a kdy ne

**Kdy:** k seskupení odlišného, ale souvisejícího obsahu, aby uživatel mohl přepínat pohledy bez
opuštění stránky. Carbonovo zdůvodnění: **snižuje to kognitivní zátěž**. Lze je použít na celostránkové
rozvržení, nebo v komponentách jako modaly, karty nebo boční panely. Typický obsah: formuláře,
nastavení, dashboardy, aby uživatel nemusel odejít ze svého flow.

**Kdy ne, tři situace:**

| Situace | Použij místo toho |
|---|---|
| Přepínání mezi různými formáty stejného obsahu, nebo filtrování stejného obsahu | **Content switcher.** Carbon dodává, že se často používá **spolu** s taby, ale typicky slouží na **nižší hierarchii**, na organizaci souvisejícího obsahu **uvnitř** obsahu tabu |
| Uživatel potřebuje projít krok za krokem lineárním procesem | **Progress indicator.** Taby organizují informaci hierarchicky, ale zůstávají flexibilní v tom, jak lze obsah navrhnout a konzumovat |
| Uživatel potřebuje **porovnávat** informaci mezi skupinami | **Ani taby.** Vedlo by to k tomu, že bude klikat tam a zpět, aby úkol dokončil |

**ZDROJ:** Carbon, Tabs usage, When to use / When not to use.
https://carbondesignsystem.com/components/tabs/usage/

**Content switcher versus taby, Carbonova definice rozdílu:** content switcher nechá uživatele
**porovnávat a přepínat mezi alternativními pohledy** na podobný nebo související obsah. Obsah
seskupený do tabů je součástí stejného většího kontextu, ale **obsah se nepřekrývá**.

**Progress indicator versus taby:** obsah progress indikátoru se pohybuje v **logické posloupnosti** a
ukazuje další kroky, aby vedl uživatele k dokončení úkolu. Taby organizují obsah do skupin, kterými
uživatel prochází, a **nepodporují progresivní úkoly**.

## Tři varianty

| Varianta | Charakteristika |
|---|---|
| Line | Samostatný tab, který lze i vnořit do komponent. Běžně používaný **v komponentách**, nebo pro obsah zabírající celou stránku, nespojený s jinými komponentami. **Vysoce flexibilní**, lze ho položit na pozadí i na vrstvu |
| Contained | **Zdůrazněný** tab, běžně používaný pro definované obsahové oblasti, typicky podstránky. **Vždy připojený k panelu**, který používá stejnou vrstvu jako vybraný tab |
| Vertical | Tablist se svislou orientací k probírání obsahu |

**Rozdíl v hierarchii:** protože contained taby stojí na vrstvách, jejich obsah má tendenci **vystoupit
proti pozadí a udržet vysokou vizuální hierarchii**, zatímco line taby se snadněji **splynou s obsahem**.

**Carbonovo varování u contained:** kvůli vrstvicímu modelu si dávej pozor na vrstvy použité uvnitř tabů,
aby obsah nebyl vizuálně příliš složitý, zvlášť v menších oblastech.

**ZDROJ:** Carbon, Tabs usage, Variants, Line tabs, Contained tabs.
https://carbondesignsystem.com/components/tabs/usage/

## Struktura

- Komponenta má **dvě zóny: vybranou a nevybranou**.
- **Jeden tab je vždy vybraný defaultně**, typicky první.
- **Vždy aspoň dva taby** v nezavíratelné skupině, **aspoň jeden** v zavíratelné.
- Ikony jsou volitelné.

**ZDROJ:** Carbon, Tabs usage, Formatting.
https://carbondesignsystem.com/components/tabs/usage/

## Zarovnání

Dva druhy šířky:

| Zarovnání | Jak funguje | Kdo ho může použít |
|---|---|---|
| Auto-width (výchozí) | Každý tab má jinou velikost podle počtu znaků labelu, ale konzistentní padding na každé straně. **První label, vybraný defaultně, se zarovná na mřížku.** Kde taby končí, se bude lišit a nemusí to skončit na mřížce | Line i contained |
| Grid aware | Taby zabírají sadu sloupců **jako skupina, každý tab stejně široký**. Label prvního tabu se zarovná s prvním použitým sloupcem, poslední tab **vždy končí na hraně sloupce**. Taby mezi tím poplynou a nemusí být na mřížce, ale **vždy budou stejně široké** | **Jen contained** |

**Grid aware používej, když** (všechny čtyři podmínky):

1. Jsou **čtyři taby nebo méně**.
2. Tablist se vejde na mřížku bez tísnění labelů.
3. Labely jsou krátké a stručné.
4. Ostatní prvky na stránce se mohou zarovnat na tablist.

**Obecné pravidlo zarovnání labelu:** stejně jako u tlačítek závisí zarovnání na tom, kde se taby
objevují a jestli jsou uvnitř jiné komponenty. **První label u line i contained tabů se zarovná
s mřížkou a s textem pod nimi.** Když jsou taby uvnitř komponenty (karta), řiď se mřížkou, kterou
používáš uvnitř té komponenty, a zarovnej label s textem v komponentě. Labely vertikálních tabů se taky
zarovnávají na mřížku, takže všechny labely v tablistu budou na stejném sloupci.

**ZDROJ:** Carbon, Tabs usage, Alignment.
https://carbondesignsystem.com/components/tabs/usage/
Detail mřížky: [2x grid a breakpointy](../zaklady/2x-grid-a-breakpointy.md).

### Taby uvnitř komponenty

**PRAVIDLO:** Když používáš line taby uvnitř komponenty (například modalu), **první label se vždy zarovná
na ostatní obsah v tom prostoru**. **Nepoužívej tam contained taby.** Hrany line tabu mohou podle
odsazení kontejneru sahat až k hranám prostoru. Lze přidat **navazující linku** od konce posledního
tabu k hraně obsahové oblasti, což přidá hierarchickou jasnost a vyváží taby s ostatním obsahem.
**KDY PLATÍ:** Taby uvnitř modalu, karty, panelu.
**TŘÍDA:** B
**ZDROJ:** Carbon, Tabs usage, Alignment within a component.
https://carbondesignsystem.com/components/tabs/usage/
**Pozor:** Carbon zároveň doporučuje **nedávat taby do dialogu vůbec**, protože skrývají informaci. Viz
[Dialogy a panely](../vzory/dialogy-a-panely.md). Když tam taby dáváš, je to proti doporučení vzoru.

## Labely

- **Krátké, jasné a konkrétní. Jedno až dvě slova**, protože se snadněji skenují.
- Vertikální taby dovolí v tabu víc znaků, ale **drž se co nejstručněji**, aby nebylo potřeba zkrácení
  a aby zbylo místo na labely v jiných jazycích.
- Textový label má **jasně komunikovat pohled, který uživatel uvidí**, a obsah v něm.
- **Sekundární label** mohou mít **jen contained taby zarovnané na mřížku**. **Nepoužívej sekundární
  labely u line tabů, auto-width contained tabů ani u vertikálních.**

**ZDROJ:** Carbon, Tabs usage, Content a Modifiers, Secondary labels.
https://carbondesignsystem.com/components/tabs/usage/

## Přetečení

| Varianta | Chování |
|---|---|
| Line a contained | **Nepotřebují zkrácení**, protože dovolují horizontální scrollování. Taby samy rostou a zmenšují se |
| Vertical | Když je label moc dlouhý, **přeteče na dva řádky a pak se zkrátí výpustkou**. Na hover celý titulek v tooltipu prohlížeče, **na focus v Carbonovém tooltipu** |

**ZDROJ:** Carbon, Tabs usage, Overflow content.
https://carbondesignsystem.com/components/tabs/usage/
Detail: [Přetečení a truncation](../vzory/preteceni-a-truncation.md).

## Responzivní chování

**PRAVIDLO:** V responzivních situacích **horizontální taby nesmí zalamovat na víc řádků ani se
stohovat**. Musí se **horizontálně scrollovat**. Vertikální taby se horizontálně nescrollují kvůli své
trvalé svislé struktuře a **vždy se stohují**.
**KDY PLATÍ:** Každá šířka obrazovky.
**TŘÍDA:** B
**ZDROJ:** Carbon, Tabs usage, Responsive behavior, verbatim: „In responsive situations, horizontal tabs
should not wrap to multiple lines or stack on top of each other; instead, they should scroll
horizontally." https://carbondesignsystem.com/components/tabs/usage/

**Scrollovatelnost:** když stránka potřebuje víc tabů, než se vejde, nebo se má přizpůsobit nové
velikosti prohlížeče, line a contained taby se stanou scrollovatelnými. **Objeví se šipky vlevo
a vpravo** pro navigaci k tabům mimo stránku.

**Breakpointy u grid aware zarovnání:**

| Breakpoint | Pravidlo |
|---|---|
| Max, XLG, LG | **Osm grid aware tabů nebo méně** |
| MD, SM | Grid aware taby se **automaticky přepnou na auto-width**, aby se na menších obrazovkách omezil zbytečný prostor |

**Vertikální taby a breakpointy:** na XL a L breakpointu zabírá vertikální tablist **4 sloupce**
z šestnáctisloupcové mřížky. Na medium breakpointu **2 sloupce**. Na small breakpointu se přepne na
**scrollovatelné contained taby**. Panel může být 8 nebo 12 sloupců široký.

## Vertikální taby

- Vlevo a svisle zarovnané taby, uživatel skenuje informaci shora dolů. Dobré na rychlé prohlížení
  a přístup k informaci, Carbon jmenuje vzor „get started".
- **Nepoužívej vertikální taby jako navigaci.**
- **Panel má zůstat stejně vysoký při přepínání tabů**, aby obsah mimo taby zůstal na stejném místě.
  Výšku tablistu a panelu má určit **tab s největším obsahem**.
- **Nepřeplňuj panel obsahem**, aby v něm nebylo nadměrné scrollování. Když potřebuješ víc místa, než
  panel dovolí, zvaž line nebo contained taby, které umožňují celostránkové rozvržení.
- Tablist i panely jsou **vždy na stejné vrstvě**.

**ZDROJ:** Carbon, Tabs usage, Vertical tabs.
https://carbondesignsystem.com/components/tabs/usage/

## Stavy

Dva hlavní: **selected** a **unselected**. Další interaktivní: **hover, focus, disabled**.

| Stav | Kdy |
|---|---|
| Selected | Uživatel klikne nebo použije šipky k aktivaci tabu |
| Unselected | Uživatel přešel na jiný tab a tento je neaktivní |
| Hover | Kurzor je nad tabem |
| Focus | Uživatel na tab kliknul, nebo navigoval klávesnicí šipkami vlevo a vpravo |
| Disabled | Uživatel nesmí s tabem interagovat kvůli oprávněním, závislostem nebo předpokladům. Disabled stav **úplně odebere interaktivní funkci**. **Stylování nepodléhá požadavku WCAG na kontrast** |

**Chování výběru:** **jen jeden tab může být vybraný najednou.** Když uživatel zvolí novou položku,
předchozí tab se automaticky odvybere. **Když uživatel z tabu odnaviguje, tab zůstane vybraný**, dokud
to uživatel nezmění.

**ZDROJ:** Carbon, Tabs usage, States.
https://carbondesignsystem.com/components/tabs/usage/
Poznámka ke kontrastu disabled stavu: [Disabled versus read-only](../vzory/disabled-vs-read-only.md).

## Automatický versus manuální tablist

**Nejdůležitější rozhodnutí u tabů, a je neviditelné ve wireframu.**

| Varianta | Chování | Kdy použít |
|---|---|---|
| Automatický | Focus a výběr jsou **synchronizované**. Šipka na tab ho zároveň vybere a panel pod ním se aktualizuje automaticky | Když se obsah panelu **načte rychle**, aby uživatel mohl rychle skenovat informace a rozhodnout se bez latence |
| Manuální | Šipky posouvají focus **bez** aktualizace panelu. Vybraný tab zůstává vybraný, focus se posune. Vybere se `Enter` nebo `Space` | Když se informace v panelu bude **načítat dlouho**. Dovolí to uživateli klávesnice nebo čtečky projít tablistem bez čekání na načtení obsahu |

**PRAVIDLO:** Automatický a manuální tablist jsou ve wireframu **vizuálně nerozlišitelné**, takže
designér **musí anotovat**, která varianta se implementuje. Carbon k tomu dodává, že jde primárně
o technické rozhodnutí o potenciální latenci, takže **do diskuse mají být zapojení architekti nebo
vývojáři**.
**TŘÍDA:** B
**ZDROJ:** Carbon, Tabs usage, Automatic and manual a Tabs accessibility, Design recommendations.
https://carbondesignsystem.com/components/tabs/usage/ ·
https://carbondesignsystem.com/components/tabs/accessibility/
Carbon odkazuje na ARIA APG „Deciding when to make selection automatically follow focus".
https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/#kbd_selection_follows_focus

## Ikony

- Ikony lze použít v line i contained tabech. **Ikona je vždy připnutá vpravo** a **neobjevuje se nad,
  pod ani vlevo od labelu**.
- **Icon-only taby** lze použít u line i contained. Ikony **musí být snadno rozpoznatelné a globálně
  přijímané**. Fungují nejlépe v malých definovaných prostorech a v komponentách. **Vždy použij tooltip
  s popisem ikony na hover a focus**, aby to bylo jasné.

**ZDROJ:** Carbon, Tabs usage, Modifiers.
https://carbondesignsystem.com/components/tabs/usage/

## Zavíratelné taby

**Kdy použít:**

- K nabídnutí flexibility a škálovatelnosti ve složitých rozhraních, kde uživatel potřebuje vytvářet
  víc sekcí nebo modulů.
- Pro obsah **vytvořený nebo kurátorovaný uživatelem**.
- K zaostření na konkrétní datovou sadu nebo výsledky hledání.

**Kdy nepoužít:**

- Když taby obsahují **často používanou nebo kritickou informaci**.
- **Jako navigaci.**

**Pravidla:**

- Ikony: **použij je jen tehdy, když je budou mít všechny taby**. **Nemíchej** zavíratelné taby s ikonami
  a bez ikon.
- **Při zavírání tabu** lze použít inline varování nebo modal, když informace v tabu už nebude dostupná
  nebo bude těžko obnovitelná. Protože varování, zvlášť modaly, jsou vysoce rušivé, **použij je jen
  tehdy, když zavření způsobí chyby, nechtěná smazání nebo neuložené změny**.
- **Vyvolání nového tabu:** trigger tlačítko může vizuálně měnit tvar a velikost podle případu. **Drž
  trigger dost blízko novému tabu**, aby se akce přidání s novou položkou asociovala. Pořadí tabů může
  být vzestupné nebo klesající podle případu, ale **drž je v sekvenčním logickém pořadí**.
- **Když jsou všechny taby zavíratelné**, zajisti, aby uživatel pochopil, jak vyvolat nové taby, až
  žádné nebudou. Dej vizuální vodítka, například kontejner nebo placeholder tab, aby bylo jasné, že
  trigger tlačítko vytváří nový tab na místě, kde ho uživatel očekává.

**ZDROJ:** Carbon, Tabs usage, Dismissible tabs.
https://carbondesignsystem.com/components/tabs/usage/

## Line tab: doplněk k panelu

**Poznámka pro implementaci:** k definování panelu (obsahové oblasti pod vybraným tabem) lze použít
linku, která se táhne od tablistu ke konci panelu. **Carbon tuhle linku ve své komponentě line tabů
nemá**, tým si ji musí přidat, pokud ji chce.
**ZDROJ:** Carbon, Tabs usage, Line tabs.
https://carbondesignsystem.com/components/tabs/usage/

---

## Co tahle nota neřeší

- Jestli má být aktivní tab v adrese, řeší [Stav pohledu v URL](../vzory/stav-pohledu-v-url.md).
- Klávesovou obsluhu do detailu (jeden tabstop, wrap, dvojí tabstop na panel).
  [Klávesnice a focus](../zaklady/klavesnice-a-focus.md).
- Content switcher jako komponentu. Carbon ji má, v přečtené kopii její stránka není.
- Progress indicator jako komponentu. [Navigace v hierarchii](navigace-v-hierarchii.md).
- Levou navigaci a UI shell. Carbon je má, v přečtené kopii nejsou.
- Tokeny vrstev a barev tabů. Carbon je má na stránce `style`, záměrně je nepřebírám.

## Zdroj

IBM Carbon Design System, Tabs usage a Tabs accessibility, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/components/tabs/usage/
Carbon u tabů cituje Jakob Nielsen, Tabs, Used Right (NN/g, 2016).
https://www.nngroup.com/articles/tabs-used-right/
Třída **B**.
