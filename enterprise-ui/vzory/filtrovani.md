# Filtrování

Jak nechat uživatele zúžit množinu dat zapínáním a vypínáním předem daných atributů.

Související: [Hledání](hledani.md) · [Datové tabulky](../komponenty/datove-tabulky.md) ·
[Volba komponenty](../zaklady/volba-komponenty.md) · [Tagy](../komponenty/tagy.md) ·
[Stabilita layoutu při změně dat](stabilita-layoutu.md)

---

## Rychlé rozhodnutí

1. Jedna hodnota z kategorie = chová se jako **radio button**. Víc hodnot = chová se jako **checkbox**.
2. Víc kategorií zároveň = **nikdy** do menu ani dropdownu. Svisle vlevo, nebo vodorovně nad daty.
3. Jedna kategorie nebo se čeká jedna volba = **okamžitá aplikace**.
4. Víc kategorií, nebo pomalý dotaz = **dávková aplikace** s tlačítkem „Použít filtry".
5. Výchozí stav kategorie: vše vybráno, když uživatel typicky **vylučuje**. Nic nevybráno, když
   typicky **vybírá jedno kritérium**.
6. Skrytý filtr (drawer, dropdown, menu) **musí** mít na zavřeném stavu indikátor: počet aplikovaných
   filtrů plus možnost je zrušit bez otevírání.
7. Každá kategorie musí mít zrušení všech svých filtrů najednou. Při víc kategoriích i zrušení všeho
   napříč kategoriemi.
8. Focus musí po přepnutí filtru zůstat na místě, i když se obsah přenačte.

---

## Co filtr řeší

Carbon jmenuje tři užitečnosti filtru: pomůže uživateli najít, co hledá; ukáže dostupné možnosti
v rámci určitých kritérií; a pomůže rozhodnout, když je možností hodně.

**ZDROJ:** Carbon, Filtering, Overview. https://carbondesignsystem.com/patterns/filtering/

## Pět metod výběru

| Metoda | Definice podle Carbonu |
|---|---|
| Single selection | Uživatel může zvolit jen jeden atribut, který mění výsledky |
| Multiselection | Uživatel může zvolit víc atributů |
| Multiple categories | Uživatel může volit atributy napříč víc kategoriemi dat |
| Multiple filters s dávkovou aktualizací | Uživatel vybere víc filtrů a pak provede další akci, kterou je aplikuje |
| Multiple filters s okamžitou aktualizací | Data se aktualizují při každé jednotlivé volbě |

**ZDROJ:** Carbon, Filtering, Selection methods, tabulka.
https://carbondesignsystem.com/patterns/filtering/

### Single selection

Chová se **pod kapotou jako radio button**. Typy: základní dropdown, inline dropdown, sada radio
buttonů (samostatně nebo v menu).

### Multiselect

Chová se **pod kapotou jako checkbox**. Typy: multiselect dropdown, inline multiselect dropdown,
sada checkboxů (samostatně nebo v menu).

### Víc kategorií

**Kategorie** je sada filtračních položek na stejné téma. Carbonův příklad: „size" je kategorie a
`small`, `medium`, `large`, `extra large` jsou její volby. Na jednu množinu dat se dá aplikovat víc
kategorií (velikost, barva, cenové rozmezí).

**PRAVIDLO:** Výběr napříč víc kategoriemi umísti svisle vlevo od stránky, nebo vodorovně nad množinou
dat. **Víc kategorií nikdy nedávej do menu ani dropdownu.**
**KDY PLATÍ:** Vždy, když filtruješ podle víc než jedné kategorie.
**TŘÍDA:** B
**ZDROJ:** Carbon, Filtering, Selecting multiple categories, verbatim: „Multiple category selection is
usually placed vertically on the left side of the page or horizontally at the top of the data set.
Multiple categories should never be put within a menu or dropdown."
https://carbondesignsystem.com/patterns/filtering/
**KDY NEPLATÍ:** Nikdy. Carbon výjimku nedává.

### Dávková versus okamžitá aktualizace

| Metoda | Trigger | Kdy použít podle Carbonu |
|---|---|---|
| Dávková | Typicky tlačítko „Apply filters", data se obnoví **jednou** | Uživatel dělá víc volb napříč různými kategoriemi, které trvá mentálně zpracovat. **A taky u pomalého vracení dat**, aby uživatel nemusel čekat po každé volbě |
| Okamžitá | Jednotlivá volba, filtr manipuluje daty v reálném čase | Uživatel vybírá jen z jedné kategorie, nebo se čeká, že udělá jen jednu volbu |

**ZDROJ:** Carbon, Filtering, Multiple filters with batch updates / with instant updates.
https://carbondesignsystem.com/patterns/filtering/

**Praktický důsledek:** dávková aplikace není jen otázka UX preference, je to i výkonové rozhodnutí.
Když dotaz trvá, dávkový filtr je jediná rozumná volba.

## Výchozí stav filtrů

**PRAVIDLO:** Filtry v každé kategorii začínají buď **všechny nevybrané**, nebo **všechny vybrané**.
Když se používá víc kategorií, výchozí stav se může kategorii od kategorie lišit.

Jak se rozhodnout:

| Chování uživatele | Výchozí stav |
|---|---|
| Typicky chce z výsledků **vyloučit** jedno nebo několik kritérií | Všechny filtry **vybrané** |
| Typicky chce vidět **jen** výsledky pro jedno konkrétní kritérium | Všechny filtry **nevybrané** |

**TŘÍDA:** B
**ZDROJ:** Carbon, Filtering, Filter states.
https://carbondesignsystem.com/patterns/filtering/

**Poznámka k parent checkboxu:** Carbon u multiselect dropdownu doporučuje **nepoužívat** parent
checkbox („All") ve scénářích jako filtry, kde vybrat vše a nevybrat nic znamená totéž.
Zdroj: https://carbondesignsystem.com/components/dropdown/usage/

## Indikátor na skrytém filtru

**PRAVIDLO:** Když jsou filtry schované v draweru, dropdownu nebo menu, na zavřeném stavu **musí** být
indikátor, že jsou filtry aplikované. Minimálně musí obsahovat **počet aplikovaných filtrů** a
**možnost filtry zrušit bez toho, aby se kontejner otevíral**.
**KDY PLATÍ:** Každý skrytý filtr.
**PROČ:** Bez indikátoru uživatel neví, proč vidí méně dat, než očekává.
**TŘÍDA:** B
**ZDROJ:** Carbon, Filtering, Filter states, verbatim: „At a minimum, the indicator should include the
number of filters applied and have the option to clear filters without re-opening the filter
container." https://carbondesignsystem.com/patterns/filtering/
**KDY NEPLATÍ:** Nikdy.

## Rušení filtrů

**PRAVIDLO:** Každá kategorie musí mít způsob, jak zrušit všechny své aplikované filtry najednou, bez
interakce s jednotlivými položkami. Zrušení vrátí filtry do jejich **původního výchozího stavu**.
Když je na stejnou množinu dat aplikovaných víc kategorií, musí existovat i způsob, jak zrušit
**všechny filtry napříč všemi kategoriemi** najednou.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Filtering, Resetting filters.
https://carbondesignsystem.com/patterns/filtering/
**Souvislost:** akce „Clear" má v Carbonu vlastní definici a formu (ikona close na pravé straně pole,
položky nebo hodnoty). Akce „Reset" znamená něco jiného: vrátí hodnoty do posledního **uloženého**
stavu. Viz [Běžné akce](bezne-akce.md).

## Přístupnost fasetového filtru

Dvouúrovňová obsluha: `Tab` mezi skupinami, `Enter` do faset uvnitř, šipky mezi fasetami, `Enter`
přepne. **Focus musí po přepnutí fasety zůstat na místě, i když se obsah přenačte.**
Detail a verbatim citace: [Klávesnice a focus](../zaklady/klavesnice-a-focus.md).

## Filtrování v datové tabulce

Datová tabulka má filtrování jako jednu ze svých funkcí, s vlastní variantou. Komplexní filtry patří
do toolbaru tabulky. Detail: [Datové tabulky](../komponenty/datove-tabulky.md).

Když změna filtru v tabulce trvá, patří to na postupné načítání: Carbon jmenuje změnu filtrů nebo
faset v tabulce jako jeden ze dvou hlavních důvodů pro progressive loading.
Viz [Načítání a čekání](nacitani-a-cekani.md).

---

## Co tahle nota neřeší

- Prázdný výsledek filtru. To je [Prázdné stavy](prazdne-stavy.md) a s tvrdšími zdroji
  [formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).
- Hledání jako alternativu nebo doplněk filtru. [Hledání](hledani.md).
- Tagy jako filtrační mechanismus (dismissible a selectable tagy).
  [Tagy](../komponenty/tagy.md).
- Volbu mezi dropdownem, checkboxy a radio buttony podle počtu možností.
  [Volba komponenty](../zaklady/volba-komponenty.md).

## Zdroj

IBM Carbon Design System, Filtering pattern, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/patterns/filtering/
Carbon k tomuhle vzoru cituje Patternfly Filters design guidelines (2019), Nick Babich, Best Practices
for Search Results (2017) a Think with Google, In-App Search (2016).
Vzor je krátký, Carbon k němu nemá vizuální specifikaci ani anatomii, jen rozhodovací pravidla.
Třída **B**.
