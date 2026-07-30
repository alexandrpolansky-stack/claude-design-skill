# Tagy

Čtyři varianty, které se liší **funkcí, ne vzhledem**. Nejčastější chyba je použít jednu variantu na
účel jiné.

Související: [Filtrování](../vzory/filtrovani.md) ·
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md) ·
[Přetečení a truncation](../vzory/preteceni-a-truncation.md) ·
[Stavové indikátory](../vzory/stavove-indikatory.md)

---

## Rychlé rozhodnutí

1. Jen kategorizace nebo label bez interakce = **read-only tag**.
2. Uživatel ho může zavřít nebo odebrat (filtr, vlastní label) = **dismissible tag**.
3. Uživatel ho zapíná a vypíná jako volbu = **selectable tag**.
4. Kliknutí odkryje další nebo přetékající tagy = **operational tag**.
5. **Tag nikdy nepoužívej jako odkaz na jinou stránku ani na spuštění nového tabu.**
6. **Nedávej tagu víc funkcí.**
7. Titulek pod 20 znaků, když to jde. Přetečení zkrať výpustkou, **nezalamuj na víc řádků**.
8. Skupina tagů: 8 px mezi nimi ze všech stran. Vodorovně max **šest** tagů na řádek.
9. Když by výběr tagů přesáhl **pět řádků** zalomení, použij multiselect dropdown.
10. Read-only tag **není v tab orderu** a focus nedostane.

---

## Kdy tagy použít

**PRAVIDLO:** Použij tagy, když je obsah namapovaný do **víc kategorií** a uživatel potřebuje způsob,
jak mezi nimi rozlišovat.
**ZDROJ:** Carbon, Tag usage, When to use.
https://carbondesignsystem.com/components/tag/usage/

Carbonův výčet konkrétních použití:

- Kategorizace, labelování nebo read-only situace.
- Metoda filtrování dat na stránce, v komponentě, nebo ve spojení s hledáním.
- V chat flow k rozhodnutí a posunutí konverzace.
- Vytváření uživatelských vlastních labelů a jejich odebírání.
- Zobrazení přetečení víc tagů, například v popoveru, modalu nebo detailním pohledu.

## Kdy tagy nepoužít

**PRAVIDLO:** **Nepoužívej tagy jako odkazy**, které tě přesměrují na úplně jinou stránku nebo vyhodí ze
současné zkušenosti do samostatného tabu. **Vyhýbej se tagům s víc funkcemi**, ať předejdeš zmatení
a snížíš nechtěné kliky.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Tag usage, When not to use, verbatim: „Do not use tags as links that direct you to an
entirely different page or launch you from a current experience to a separate tab. Avoid using tags with
multiple functions to prevent confusion and reduce accidental clicks."
https://carbondesignsystem.com/components/tag/usage/
Carbon zákaz odkazu opakuje ještě u operational tagu.

## Čtyři varianty

| Varianta | Účel | Interakce |
|---|---|---|
| Read-only | Bez interaktivní funkce, běžně na kategorizaci a labelování | Žádná. Jen kurzor na hover |
| Dismissible | Lze zavřít, zamknout nebo odebrat. Typicky filtrování a uživatelský obsah | Klikatelná je **oblast okolo zavíracího křížku** |
| Selectable | Lze vybrat nebo odvybrat. Často jako výběr filtrující data v kontextu stránky. Taky v chat flow k rozhodnutí | Klikatelný je **celý kontejner**, klik znovu odvybere |
| Operational | Při interakci odkryje další nebo přetékající tagy (popover, modal, detailní pohled drobenky) | Klikatelný je **celý kontejner** |

**Vizuální rozlišení funkcí, které Carbon dělá:** selectable a operational tagy mají **rámeček
kontejneru**, aby bylo na první pohled vidět, že mají zvýšenou interaktivitu a fungují jinak.

**ZDROJ:** Carbon, Tag usage, Variants a Anatomy.
https://carbondesignsystem.com/components/tag/usage/

## Anatomie

Všechny čtyři varianty mají: **kontejner, textový titulek** a volitelně **dekorativní ikonu**.
Dismissible má navíc **zavírací křížek**. Selectable a operational mají **rámeček**.

**Dekorativní ikona** jde **před** titulek. Je volitelná a často podporuje titulek vizuálně. Carbon
doporučuje **nepoužívat ji u malé velikosti tagu**, kde je kompaktní odsazení, protože by mohlo vzniknout
vizuální napětí mezi některými tvary ikon a tagy s rámečkem.

**ZDROJ:** Carbon, Tag usage, Anatomy a Modifiers, Decorative icons.
https://carbondesignsystem.com/components/tag/usage/

## Velikosti

| Velikost | Kdy |
|---|---|
| Small | Kondenzované nebo inline prostory |
| Medium | **Výchozí a nejčastější** |
| Large | Když je tag **primárním úkolem stránky nebo hlavním bodem**, když je hodně místa, nebo když je vedle jiných komponent, které jsou taky 32 px vysoké |

**ZDROJ:** Carbon, Tag usage, Sizing.
https://carbondesignsystem.com/components/tag/usage/

## Umístění a zarovnání

**PRAVIDLO:** Svisle zarovnej **kontejner tagu** k ostatním komponentám nebo textu vedle. **Nezavěšuj
kontejnery tagů do mezer mřížky**, abys svisle zarovnal titulky tagů s ostatním textem na stránce. Když
jsou tagy ve skupinách, doporučuje se **8 px mezery mezi nimi nahoře, dole, vlevo a vpravo**.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Tag usage, Placement, verbatim: „Do not hang tag containers into grid gutters to
vertically align the tag's titles with other text on the page."
https://carbondesignsystem.com/components/tag/usage/

## Titulek

- **Stručný a informativní.**
- Popsat tag **pár slovy**, nebo **pod 20 znaků**, když to jde.
- Dlouhý obsah v titulku dávej **jen když je to nutné**, například u uživatelsky definovaných názvů
  kategorií nebo systémově generovaných řetězců textu.

**Přetečení:** titulek lze zkrátit výpustkou. Na hover celý titulek v tooltipu prohlížeče, **na focus
z klávesnice v tooltipu**. Zkrácení nastav **na začátku, v prostředku nebo na konci** podle toho, co se
pro daný případ hodí nejlíp.

**PRAVIDLO:** **Vyhýbej se zalamování dlouhých titulků na víc řádků** uvnitř kontejneru tagu.
**PROČ:** Carbon dává dva důvody: zkreslí to tvar tagu a integritu tradičního tvaru tagu, který má být
kompaktní. A může to vytvořit misalignment s ostatními tagy, když jsou ve skupině.
**TŘÍDA:** B
**ZDROJ:** Carbon, Tag usage, Overflow content.
https://carbondesignsystem.com/components/tag/usage/
Detail: [Přetečení a truncation](../vzory/preteceni-a-truncation.md)

## Read-only tag

Používá se ke kategorizaci a labelování, **bez interaktivní funkce**. Má několik barevných voleb a může
používat volitelné dekorativní ikony k odlišení víc kategorií.

**PRAVIDLO:** Když má tvůj návrh tagy jako labely nebo na kategorizaci, použij **modifikátory jako barvy
nebo ikony**, které to odlišení pomůžou označit.
**ZDROJ:** Carbon, Tag usage, Read-only tag.
https://carbondesignsystem.com/components/tag/usage/

**Klávesnice:** read-only tagy **nejsou v tab orderu**, nejsou interaktivní a **focus nedostanou**.
Zdroj: https://carbondesignsystem.com/components/tag/accessibility/

## Dismissible tag

- Běžně se používá **se komponentou hledání** na hledání nebo filtrování klíčových slov na stránce nebo
  v jejích sekcích.
- Lze ho použít i jako **uživatelsky vytvořený label** aplikovaný na instance, který se dá později
  odebrat.
- **PRAVIDLO: nepoužívej dismissible tag, když má být trvale přítomný**, protože ho uživatel může zavřít
  nebo zrušit.
- **Klikatelná je jen oblast okolo zavíracího křížku**, ne celý tag.
- Vývojářská poznámka Carbonu: **nepřidávej `onClick` funkci na dismissible tag**, interakce se má
  rezervovat jen pro zavírací ikonu.

**ZDROJ:** Carbon, Tag usage, Dismissible tag a Tag accessibility.
https://carbondesignsystem.com/components/tag/usage/

## Selectable tag

- Uživatel je může vybírat a odvybírat. Použití: formulář obsahující jen tagy jako metodu výběru, chat
  k rozhodnutí a posunutí konverzace, výběr filtrující obsah na stránce nebo v komponentě.
- **Může být alternativou tradičních formulářových komponent**, ale jen tehdy, když **celý formulář
  konzistentně používá tagy jako svůj styl výběru**.
- Lze použít na multi-select i single-select.
- **Musí vždycky zůstat ve vysokém kontrastu**, aby byl rozdíl mezi vybraným a nevybraným tagem
  zřetelný.

**Pravidla pro skupiny:**

| Počet tagů | Rozvržení |
|---|---|
| **Šest nebo méně** | Vodorovné zarovnání na jednom řádku, kvůli lepšímu skenování |
| Hodně tagů | Vodorovné zarovnání **není doporučené**, tagy se mají zalamovat na další řádek |
| **Přes pět řádků** zalomení | **Použij jinou komponentu**, Carbon jmenuje multiselect dropdown |

**ZDROJ:** Carbon, Tag usage, Selectable tag, verbatim: „If the number of tags exceeds five lines of
wrapping, consider using a different component for your use case, like a multi-select dropdown."
https://carbondesignsystem.com/components/tag/usage/

## Operational tag

Umožní uživateli vidět komplexnější pohled na **všechny tagy** odkryté v popoveru nebo detailním pohledu
drobenky. Carbon u něj **znovu** zakazuje použití jako odkazu, který vede na jinou stránku nebo do
samostatného tabu.

**ZDROJ:** Carbon, Tag usage, Operational tag.
https://carbondesignsystem.com/components/tag/usage/

## Stavy podle varianty

| Varianta | Stavy |
|---|---|
| Read-only | enabled, disabled, skeleton |
| Dismissible a operational | enabled, hover, focus, on click, disabled, skeleton |
| Selectable | enabled, hover, focus, **selected**, disabled, skeleton |

**Disabled:** uživatel nesmí s tagem interagovat kvůli oprávněním, závislostem nebo předpokladům.
Disabled stav **úplně odebere interaktivní funkci**. **Stylování nepodléhá požadavku WCAG na kontrast.**

**ZDROJ:** Carbon, Tag usage, States.
https://carbondesignsystem.com/components/tag/usage/
Poznámka ke kontrastu disabled stavu: [Disabled versus read-only](../vzory/disabled-vs-read-only.md).

## Interakce myší podle varianty

| Varianta | Hover | Klik |
|---|---|---|
| Read-only | Jen kurzor, žádná interaktivní funkce | Nic |
| Dismissible | Kurzor nad oblastí titulku. Nad zavíracím křížkem **změna barvy pozadí ikony** plus pointer | Klik na oblast křížku tag zavře nebo odebere |
| Selectable | **Změna barvy celého pozadí** plus pointer | Klik kamkoliv tag vybere. Další klik ho odvybere |
| Operational | Změna barvy pozadí plus pointer | Klik kamkoliv odkryje víc souvisejících tagů (popover, modal, drobenka) |

**ZDROJ:** Carbon, Tag usage, Interactions a Clickable areas.
https://carbondesignsystem.com/components/tag/usage/

## Barvy tagů

Carbon k barvám říká dvě věci, které jsou přenositelné jako princip:

1. Read-only, dismissible a operational tagy mají **různé barvy**, a Carbon **doporučuje použít víc
   barev k označení různých kategorií nebo labelů**.
2. **Selectable tagy tyhle barvy nemají**, používají jádrové tokeny.

Konkrétní barevné tokeny záměrně nepřebírám. Přenositelné je pravidlo, že **výběrový tag nesmí mít
kategorii jako barvu**, protože barva už nese stav vybráno versus nevybráno.

**ZDROJ:** Carbon, Tag usage, Modifiers, Tag colors.
https://carbondesignsystem.com/components/tag/usage/
Sémantika barev a WCAG kontrast: [kontrast a barva](../../ux-design/pravidla/kontrast-a-barva.md).

## Tag versus stavový indikátor

Carbon je odděluje. Tag je na **kategorizaci, label a filtrování**. Stavový indikátor sděluje **stav
nebo závažnost** a má vlastní pravidla o povinných prvcích a kontrastu 3:1.

**Praktický důsledek** (moje formulace, třída **C**): „Aktivní / Neaktivní / Chyba" u záznamu v tabulce
je **stavový indikátor**, ne tag, i když může vypadat podobně. Řídí se pravidly ve
[stavových indikátorech](../vzory/stavove-indikatory.md), včetně požadavku na kontrast a na to, že barva
sama nestačí.

## Tag v multiselectu

Když uživatel v multiselect dropdownu vybere volby, **vlevo od textu v poli se objeví tag s celkovým
počtem** vybraných voleb a s možností všechny zrušit. Detail:
[Výběr ze seznamu](vyber-ze-seznamu.md).

---

## Co tahle nota neřeší

- Filtrování jako vzor. [Filtrování](../vzory/filtrovani.md).
- Stavové indikátory, badge a diferenciální indikátory.
  [Stavové indikátory](../vzory/stavove-indikatory.md).
- Barevné tokeny. Carbon je má na stránce `style`, záměrně je nepřebírám.
- Popover jako komponentu. Carbon ji má, v přečtené kopii samostatná stránka není.

## Zdroj

IBM Carbon Design System, Tag usage a Tag accessibility, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/components/tag/usage/
Carbon u tagu neuvádí sekci References, žádné externí zdroje k němu nemá. Třída **B**.
