# Hledání

Tři typy hledání podle velikosti datové sady a podle toho, kam uživatel po hledání jde.

Související: [Filtrování](filtrovani.md) · [Prázdné stavy](prazdne-stavy.md) ·
[Datové tabulky](../komponenty/datove-tabulky.md)

---

## Rychlé rozhodnutí

1. Hledání vede na **samostatnou stránku výsledků** = basic search. Dotaz se spustí až akcí uživatele.
2. Malá datová sada (jedna stránka, web, tabulka) a výsledky se ukážou hned pod polem = **active
   search**. Dotaz běží po každém znaku.
3. Hledání v tom, co patří přihlášenému uživateli, s možností rozšířit záběr = **focused search**.
4. **Label k vyhledávacímu poli nedávej.** Ikona lupy plus placeholder stačí.
5. Vždycky zobraz **počet výsledků**, i když je nula. Při scope filtru i počet pro každý scope.
6. Nula výsledků **není slepá ulička**: nabídni návaznou akci.
7. Když hledání trvá, dej indikátor. U náročného hledání progress bar s odhadem.
8. Scope filtr musí mít možnost „All" nebo „Any" a ta musí být **vybraná defaultně**.
9. Nepoužívej hledání, když je dat málo nebo se informace najde v jednom pohledu.

---

## Kontext

Carbon úvodem konstatuje, že očekávání uživatelů od hledání jsou vysoká, protože vyhledávač je často
primární vstupní bod na internet, a že **konzistence je kritická**. Volba metody závisí na velikosti
prohledávané datové sady a na tom, kde v produktu hledání je.

Většina hledání podle Carbonu začíná široce a záběr se zužuje aplikací filtrů.

**ZDROJ:** Carbon, Search pattern, Overview. https://carbondesignsystem.com/patterns/search-pattern/

## Anatomie

1. **Scope filtr** (volitelný): omezí hledání na sekci nebo kategorii obsahu.
2. **Ikona hledání**: signalizuje vyhledávací pole. Lupa je univerzální způsob, jak hledání označit.
3. **Placeholder**: užitečný a krátký text napovídající, co lze hledat. Carbonův příklad:
   „Search for networks or devices."
4. **Textové pole**: kam uživatel zadává dotaz.

**ZDROJ:** Carbon, Search pattern, Anatomy. https://carbondesignsystem.com/patterns/search-pattern/

## Tři typy

| Typ | Kdy použít | Použití |
|---|---|---|
| Basic | Uživatel provede hledání a bude přesměrovaný na samostatnou stránku výsledků | Globální hledání, nebo jakékoliv hledání směrující na samostatnou stránku výsledků |
| Active | Nejlepší pro malé datové sady (jedna stránka, web, tabulka). Když uživatel těží z průběžné zpětné vazby na svůj dotaz a když server unese značnou zátěž z hledání | Aktivně hledá v databázi a vypisuje nejlepší výsledky v panelu nebo na aktuální stránce: katalog, malý web, malá datová sada v tabulce, podmnožina informací uvnitř stránky |
| Focused | Když je hledání zaměřené na úkoly nebo informace specifické pro přihlášeného uživatele. Omezuje zátěž serveru zúžením záběru a přitom nabízí sílu širokého hledání | Přiřazené úkoly, produktové katalogy, osobní repozitáře, obsah vytvořený přihlášeným uživatelem |

**ZDROJ:** Carbon, Search pattern, Types of search.
https://carbondesignsystem.com/patterns/search-pattern/

### Basic search

Nespustí dotaz nad datovou sadou, dokud uživatel hledání nespustí.

**Kdy podle Carbonu:**

| Situace | Důvod |
|---|---|
| Hledání je drahé | Hledání ve velkém objemu informací může být náročné na prostředky, zvlášť když hledá hodně uživatelů zároveň. Aktivní hledání po každém zadaném nebo smazaném znaku je nepraktické |
| Hledání je pomalé | U masivního objemu se aktivní hledání stane příliš pomalým. Delší zpracování po každém znaku působí, že web nebo aplikace nereaguje |
| Informace je uživateli neznámá | Když uživatel hledá v aplikaci nebo webu, který nezná, samostatná stránka výsledků mu dá lepší představu o struktuře dat a dostupných zdrojích |

**Chování:**

- **Nedávné dotazy:** když uživatel klikne nebo tabne do pole, ukaž menu s nedávnými dotazy tohohle
  uživatele, s trendujícími dotazy, nebo s obojím. Jak začne psát, menu vystřídají návrhy podle dotazu.
- **Type-ahead návrhy:** generují se z průběžné analýzy vzorců hledání a **zatěžují server minimálně**.
  Uživatel bez závazku vidí náhled výsledků, návrhy dalších termínů, nebo najde přímo to, co chtěl.
  Objeví se, jak začne psát.
- **Stránka výsledků:** uživatel na ní má mít možnost zvolit filtry a zúžit výsledky. Když chceš
  nabídnout filtry ještě před hledáním, použij scope filtr.

Carbon k designu stránky výsledků říká, že závisí na potřebách produktu, a konkrétnější vodítko slibuje
až do budoucna.

### Active search

Rychlý způsob hledání v aplikaci nebo datové sadě. Dotaz běží **po každém zadaném znaku** a výsledky
jsou hned pod polem. Carbon to popisuje jako filtrování datové sady klíčovými slovy.

**Skládá se z:** vyhledávacího pole, ikony hledání a křížku, který funguje jako smazat nebo zrušit.
**Nemá tlačítko Search ani Go**, protože hledání běží aktivně a uživatel se nikam nepřesměrovává.

**Kdy podle Carbonu:**

| Situace | Důvod |
|---|---|
| Data jsou omezená | Hledání pravděpodobně vrátí přesný výsledek. Malý web, tabulka s omezenými daty. Nebo katalog položek (produktový katalog, knihovna) |
| Uživatel ví, co hledá | Když uživatel aplikaci zná, hledáním typicky hledá zdroj, o kterém ví, že existuje. Aktivní výsledky v panelu ho pustí přímo na stránku nebo zdroj |
| Filtruje se katalog na stránce | Když produkt zobrazuje katalog na stránce, aktivní hledání zúží možnosti podle dotazu |

**Chování:**

- Placeholder má být **konkrétnější než u basic search** a má zůstat viditelný, dokud uživatel nezačne
  psát.
- Volitelně můžeš do panelu výsledků přidat položku „See all results", která se pak chová jako
  basic search.
- U katalogu nebo knihovny zužuj výsledky na stránce, jak uživatel píše.
- Nedávné dotazy uživatele mají být v panelu pod polem a **jak začne psát, vystřídají je odpovídající
  výsledky**.
- U malé množiny na celé stránce: před spuštěním hledání zobraz všechny položky, jak uživatel začne
  psát, zobrazuj jen ty, které odpovídají.

### Focused search

Kombinace basic a active search. Uživatel aktivně vidí výsledky ze svojí stránky, produktu nebo
záběru, a **pod nimi má možnost záběr rozšířit** na všechna dostupná data. Ideální pro uživatele
konkrétního nástroje, který je součástí katalogu nebo balíku produktů.

**Kdy podle Carbonu:**

| Situace | Důvod |
|---|---|
| V rámci balíku produktů | Aktivně nabídne výsledky vztažené k přihlášenému uživateli. Omezí prostředky potřebné na hledání a přitom dá možnost rozšířit záběr na celý produktový katalog nebo databázi |
| V rámci složky nebo datové sady | Uživatel může hledání zúžit i rozšířit v rámci datové struktury. Když panel výsledků nedodá, co potřebuje, může hledat jinde bez toho, aby odešel z pole |

**Chování:**

- Když uživatel vybere podkategorii z panelu výsledků, hledání se chová jako basic search
  s aplikovaným filtrem. **Vybraný filtr má persistovat i pro další hledání**, dokud ho uživatel
  nezruší nebo nezačne novou session.
- Při kliknutí nebo tabnutí do pole se ukáže menu s nedávnými dotazy uživatele, návrhy specifickými
  pro uživatele nebo session, nebo obojím. Jak začne psát, návrhy zmizí a výsledky se zužují po každém
  znaku.
- Výsledky lze **klastrovat po kategoriích** s možností „View all" v kategorii. To je ideální pro
  uživatele, který hledá napříč několika podobnými datovými sadami a neví, kde informace žije. Když
  uživatel místo dat naopak zná, nabídni scope filtr.
- Úspěšné focused search nasměruje uživatele přímo na stránku nebo zdroj. Když zvolí „See all
  results", zobraz stránku výsledků.

## Pět pravidel platných pro všechny typy

### Žádné slepé uličky

**PRAVIDLO:** Když hledání vrátí „No results", navrhni návaznou akci. Dej návrhy a užitečné zdroje,
které uživateli pomůžou najít, co hledá.
**ZDROJ:** Carbon, Search pattern, Best practices, Avoid dead ends, s odkazem na
[Empty states pattern](prazdne-stavy.md). https://carbondesignsystem.com/patterns/search-pattern/
**Souvislost:** knihovna má tohle pravidlo tvrdší a konkrétnější, včetně nálezu, že search tipy jako
jediná náplň mohou opuštění naopak zvýšit (Baymard). Viz
[formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).

### Indikátor načítání

**PRAVIDLO:** Když hledání zabere víc než chvilku, přidej indikátor. **Načítací stav má odrážet tvůj
prázdný stav** s užitečným helper textem, který signalizuje, že hledání běží. U pokročilého hledání
náročného na prostředky přidej **progress bar**: dej vědět, jak daleko hledání je a přibližně jak
dlouho to bude trvat.
**ZDROJ:** Carbon, Search pattern, Best practices, Include a loading indicator.
https://carbondesignsystem.com/patterns/search-pattern/
Detail: [Načítání a čekání](nacitani-a-cekani.md)

### Vždycky počet výsledků

**PRAVIDLO:** **Vždycky** zobraz počet výsledků hledání, včetně situace, kdy je nulový. Když nabízíš
scope filtr, zobraz i počet výsledků pro každý scope selektor.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Search pattern, Best practices, verbatim: „Always include the number of search
results, including for searches with no results. If you plan to offer a scope filter, also include the
number of results for each scope selector." https://carbondesignsystem.com/patterns/search-pattern/
**KDY NEPLATÍ:** Nikdy. Carbon to opakuje na dvou místech.

### Bez labelu

**PRAVIDLO:** Nedávej k vyhledávacímu poli label. Uživatelé vyhledávací pole očekávají a rozumí mu,
label není potřeba. Ikona lupy plus užitečný placeholder má jasně signalizovat, že pole je na hledání.
**KDY PLATÍ:** Vyhledávací pole.
**TŘÍDA:** B
**ZDROJ:** Carbon, Search pattern, Best practices, Don't include a label.
https://carbondesignsystem.com/patterns/search-pattern/
**Pozor:** to je pravidlo o **viditelném** labelu. Neviditelný label pro čtečku existovat musí. Carbon
sám vyhledávacímu poli dává neviditelný label „search" a křížku „clear search input". Viz
[Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md) a
[formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md), kde je skrytý label u search
v hlavičce jmenovaný jako legitimní výjimka.

### Lokalizace

**PRAVIDLO:** U jazyků čtených zprava doleva překlop rozvržení vyhledávacího pole. Ikona lupy je
rozpoznaná a přijímaná napříč jazyky a zeměmi.
**ZDROJ:** Carbon, Search pattern, Best practices, Localize the search field.
https://carbondesignsystem.com/patterns/search-pattern/

## Scope filtr

**PRAVIDLO:** Volitelný scope filtr omezí hledání na sekci nebo kategorii obsahu, na rozdíl od
globálního hledání, které hledá všude. **Vybrat lze jen jednu scope kategorii najednou**, ale dropdown
musí **vždycky** obsahovat volbu „All" nebo „Any", a **ta má být vybraná defaultně**. S vybraným „All"
funguje pole jako základní globální hledání.
**KDY PLATÍ:** Kdykoliv nabízíš scope filtr.
**TŘÍDA:** B
**ZDROJ:** Carbon, Search pattern, Best practices, Add a scope filter, verbatim: „Only one scoped
category can be selected at a time, but the dropdown should always include an 'All' or 'Any' option,
and this option should be selected by default."
https://carbondesignsystem.com/patterns/search-pattern/

## Umístění vyhledávacího pole

Závisí na stavbě aplikace a na záběru hledání. Carbon rozlišuje tři úrovně:

| Úroveň | Kdy |
|---|---|
| Globální | Hledání v celém webu nebo produktu. Umístění řeší Carbonův global header pattern |
| Stránka | Hledání v obsahu konkrétní stránky |
| Komponenta | Hledání v datech komponenty, typicky datové tabulky |

**Kdy hledání nepoužívat:** když je dat málo nebo omezené množství. Když je informace jednoduchá
a najde se snadno v jednom pohledu.

**Velikosti pole:** 32 / 40 / 48 px, stejná škála jako ostatní vstupy. Velké se typicky používá na
globální úrovni, když uživatel hledá obsah v rámci pohledu stránky.

**ZDROJ:** Carbon, Search usage, Overview a Sizing.
https://carbondesignsystem.com/components/search/usage/

## Klávesová obsluha

`Tab` do pole, psaní hned, `Enter` spustí dotaz, `Esc` vymaže pole. Křížek pro vymazání je **další
tabstop** a aktivuje ho `Space` nebo `Enter`. Scope dropdown a type-ahead návrhy musí být taky
obsluhovatelné klávesnicí: u scope `Tab` na dropdown, šipky otevřou a cyklují, `Enter` vybere
a posune uživatele do vyhledávacího pole. U type-ahead šipky cyklují návrhy, `Enter` vybere, `Escape`
umožní odejít bez výběru.

Detail včetně variant se skrytým polem: [Klávesnice a focus](../zaklady/klavesnice-a-focus.md).

**Co Carbon u přístupnosti hledání přiznává jako mezeru:** návrhy a type-ahead, sdělování výsledku
a stavu hledání („25 results found", „no results found") a navigace výsledků potřebují anotaci od
designéra a Carbon k nim konkrétní dokumentaci slibuje až do budoucna.
**ZDROJ:** https://carbondesignsystem.com/components/search/accessibility/

## Hledání v datové tabulce

Datová tabulka má dvě varianty umístění:

| Varianta | Chování |
|---|---|
| Sbalené (default) | Vyvolá se ikonovým tlačítkem v toolbaru tabulky, defaultně zavřené, umístěné pod titulkem tabulky. Chová se podle vzoru **active search** |
| Otevřené | Pole je trvale otevřené, vlevo pod titulkem tabulky, roztažené až k akcím vpravo |

**ZDROJ:** Carbon, Data table usage, Searching.
https://carbondesignsystem.com/components/data-table/usage/
Detail: [Datové tabulky](../komponenty/datove-tabulky.md)

---

## Co tahle nota neřeší

- Prázdný výsledek hledání do detailu (Baymard, proč tipy nestačí).
  [Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).
- Filtrování jako samostatný mechanismus. [Filtrování](filtrovani.md).
- Design stránky výsledků. Carbon ho **nemá**, slibuje ho do budoucna.
- Globální hlavičku a umístění globálního hledání. Carbonův global header pattern v přečtené kopii
  není.

## Zdroj

IBM Carbon Design System, Search pattern a Search usage, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/patterns/search-pattern/ ·
https://carbondesignsystem.com/components/search/usage/
Carbon k tomuhle vzoru cituje Apple HIG Search Fields (2019), Nick Babich, Best Practices for Search
Results (2017) a Think with Google, In-App Search (2016). Třída **B**.
