# Přetečení obsahu a zkracování

Kde smíš text zkrátit výpustkou, kde ne, a kdy místo zkrácení nabídnout „Zobrazit více".

Související: [Datové tabulky](../komponenty/datove-tabulky.md) · [Tagy](../komponenty/tagy.md) ·
[Navigace v hierarchii](../komponenty/navigace-v-hierarchii.md) ·
[Načítání a čekání](nacitani-a-cekani.md)

---

## Rychlé rozhodnutí

1. Zkracuj: drobenka, stránkování, dlouhé URL, odstavec popisu, dlouhý název položky.
2. **Nezkracuj: nadpisy stránek, titulky, labely, chybové hlášky, validační hlášky, notifikace.**
3. Zkrácený text **vždycky** doprovoď tooltipem prohlížeče na hover, který ukáže celý řetězec.
   Jediná výjimka: konec zkráceného odstavce.
4. Před výpustkou musí zůstat **aspoň čtyři nezkrácené znaky** a výpustka musí zastupovat **tři nebo
   víc** znaků.
5. Samotná výpustka bez textu = potřebuje **overflow menu** na hover, ne tooltip.
6. Hodně přetékajícího obsahu = tlačítko „Zobrazit více", ne scroll, gradient nebo fade.
7. Label tlačítka nezkracuj nikdy, ať se zalomí.
8. Checkbox label nezkracuj, radši přeformuluj, nebo ať se zalomí.

---

## Definice

Přetékající obsah je text (odstavec nebo řetězec), který přesahuje požadovaný prostor. Platí to
i pro řadu komponent, které přesahují daný prostor. Přetékající obsah se typicky zmenšuje, aby se
vešel, nebo aby se snížila repetitivnost. Dva způsoby, jak označit, že obsah pokračuje jinde nebo pod
ohybem: **zkrácení** a tlačítko **„Zobrazit více"**.

**ZDROJ:** Carbon, Overflow content pattern, úvod.
https://carbondesignsystem.com/patterns/overflow-content/

## Kde zkracovat a kde ne

| Zkracuj | Nezkracuj |
|---|---|
| Drobenka | Nadpisy stránek |
| Stránkování | Titulky |
| Dlouhé URL odkazy | Labely |
| Odstavec textu (například popis) | Chybové hlášky |
| Zkrácení dlouhého názvu položky (vytvořeného uživatelem nebo platformou) | Validační hlášky |
| | Notifikace |

**ZDROJ:** Carbon, Overflow content, Usage, verbatim: „Truncation should **not** be used on page
headers, titles, labels, error messages, validation messages, or notifications."
https://carbondesignsystem.com/patterns/overflow-content/

**Proč zákaz u hlášek:** to Carbon explicitně nezdůvodňuje, ale je to konzistentní s pravidlem
knihovny, že chybová hláška musí obsahovat popis problému **i** instrukci k opravě. Zkrácená hláška
jednu z těch dvou částí ztratí. Viz
[formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).

## Mechanika zkracování

**PRAVIDLO:** Zkrácené položky reprezentuje výpustka `...` a ta má zastupovat **tři nebo víc**
zkrácených znaků. V zkráceném řetězci musí zůstat **aspoň čtyři nezkrácené znaky**. Zkrácené položky
**vždycky** obsahují tooltip prohlížeče na hover, který ukáže celý řetězec, jméno nebo frázi. **Jediná
situace, kdy tooltip prohlížeče potřeba není, je konec zkráceného odstavce.**
**KDY PLATÍ:** Každé zkrácení.
**TŘÍDA:** B
**ZDROJ:** Carbon, Overflow content, Truncation, verbatim: „Truncated items are represented by an
ellipsis `...` and should represent three or more truncated characters in a text string. There must be
at least four characters of non-truncated content in a truncated string. Truncated items always include
a browser tooltip on hover to show the entire string, name, or phrase that the ellipsis is
representing." https://carbondesignsystem.com/patterns/overflow-content/
**KDY NEPLATÍ:** Konec zkráceného odstavce, kde tooltip potřeba není.

## Tři typy zkrácení

| Typ | Kdy | Před | Po |
|---|---|---|---|
| Front-line | Na začátku řetězce, aby naznačil, že text pokračuje z předchozího místa | `123456789` | `...56789` |
| Mid-line | Když má víc řetězců různý začátek nebo konec, ale **naprosto stejný prostředek**. Nebo když je potřeba zkrátit frázi, jejíž konec zkrátit nelze | `123400005678` `987600004321` | `1234...5678` `9876...4321` |
| End-line | Na konci řetězce nebo odstavce, aby naznačil, že obsah pokračuje jinde, že vzor v posloupnosti pokračuje, nebo aby zkrátil dlouhý řetězec | `123456789` | `12345...` |

**Praktický důsledek u mid-line:** to je typ, na který se v enterprise UI zapomíná. ID záznamů,
cesty k souborům, hashe a názvy instancí mají často shodný prostředek a rozdíl je na obou koncích.
End-line zkrácení je tam k ničemu, protože všechny řetězce vypadají stejně.

**Implementační poznámka Carbonu:** front-line a end-line se dají udělat CSS (utilita `text-truncate`
plus atribut `title` pro tooltip, a nastavená `width` kontejneru nebo textového prvku, aby se dalo
spočítat, kde zkrácení začne). **Mid-line vlastní CSS třídu nemá, potřebuje JavaScript.**

**ZDROJ:** Carbon, Overflow content, Variations a Code.
https://carbondesignsystem.com/patterns/overflow-content/

## Samotná výpustka

**PRAVIDLO:** Výpustka může zastupovat kondenzovaný obsah i sama za sebe. Tenhle typ zkrácení
vyžaduje na hover **overflow menu**, nikoliv tooltip prohlížeče.
**KDY PLATÍ:** Zkrácená drobenka, zkrácené stránkování.
**PROČ:** Zastoupený obsah nejsou znaky jednoho řetězce, ale víc samostatných položek, ke kterým
uživatel potřebuje přístup, ne jen jejich přečtení.
**TŘÍDA:** B
**ZDROJ:** Carbon, Overflow content, Ellipses alone, verbatim: „An ellipsis on its own may also
represent condensed content. This type of truncation requires an overflow menu on hover instead of
a browser tooltip." https://carbondesignsystem.com/patterns/overflow-content/
Konkrétní chování u drobenky (první a poslední dvě položky vidět, zbytek do overflow menu, nikdy
nezalamovat na druhý řádek): [Navigace v hierarchii](../komponenty/navigace-v-hierarchii.md).

## „Zobrazit více"

**PRAVIDLO:** Tlačítko „Zobrazit více" použij, když je přetékajícího obsahu **významné množství**.
Dá uživateli možnost vidět obsah po strávitelnějších kusech, ne všechno naráz. „Zobrazit více" se
používá **místo scrollování, gradientů nebo fade efektů**, protože je výraznější a akční. Když je
potřeba, může existovat i „Zobrazit méně". V případech, kdy jde o výkon, se to samé dá podat jako
„Načíst více".
**KDY PLATÍ:** Dlouhé seznamy, dlouhý textový obsah.
**TŘÍDA:** B
**ZDROJ:** Carbon, Overflow content, „Show more" buttons, verbatim: „A 'Show more' button is used in
place of scrolling, gradients, or fades as they are more prominent and actionable."
https://carbondesignsystem.com/patterns/overflow-content/
**Souvislost:** „Load more" má i souvislost s postupným načítáním dat po dávkách, viz
[Načítání a čekání](nacitani-a-cekani.md).

## Přetečení podle komponenty

Souhrn toho, co jednotlivé komponenty Carbonu o svém přetečení říkají. Detaily jsou v příslušných
notách.

| Komponenta | Pravidlo |
|---|---|
| Tlačítko | Label **nezkracuj**, ať se zalomí na druhý řádek |
| Checkbox | Label **nezkracuj** výpustkou. Radši přeformuluj. Dlouhý label ať se zalomí na druhý řádek, a to **pod checkbox**, aby byl ovládací prvek s labelem zarovnaný nahoře. Carbon doporučuje labely pod tři slova |
| Dropdown | Vyhýbej se víc řádkům textu. Když se text nevejde na jeden řádek, přidej výpustku a **tooltip pro zobrazení celého textu**, přednostně Carbonový tooltip kvůli klávesové přístupnosti |
| Tag | Titulek lze zkrátit výpustkou. Na hover celý titulek v tooltipu prohlížeče, **na focus z klávesnice v tooltipu**. Zkrácení nastav na začátku, v prostředku nebo na konci podle situace. **Nezalamuj tag na víc řádků**, zkreslí to jeho tvar a rozbije zarovnání ve skupině |
| Tabs, horizontální | **Nepotřebují zkrácení**, protože se horizontálně scrollují a taby samy rostou a zmenšují se |
| Tabs, vertikální | Label přeteče na dva řádky a pak se zkrátí výpustkou. Na hover tooltip prohlížeče, **na focus Carbonový tooltip** |
| Tabulka, hlavička sloupce | Když je titulek moc dlouhý, **zalom na dva řádky a pak zkrať**. Celý text ukaž v tooltipu na hover |
| Structured list, hlavička sloupce | Stejné jako u tabulky |
| Progress indicator, label | Zvaž přeformulování, nebo zkrať výpustkou a dodej tooltip |
| Progress indicator, helper text | Dlouhý ať se **zalomí na druhý řádek**, což je lepší než zkrácení. Zalom ho **pod label**, aby oba držely zarovnání vlevo |
| Modal | Když je obsah delší než výška, **scrolluje jen tělo**. Vodorovně **nikdy**, použij větší modal |
| Toggletip | Scroll typicky není potřeba. Když je, scrolluje **tělo**, hlavička a zápatí zůstávají. Vodorovně ne, obsah nesmí vytéct ze stránky |
| Notifikace | Když je potřeba zpráva delší než dvě řádky, použij **actionable notifikaci** s krátkou zprávou a odkazem „Zobrazit více" na plnou zprávu (stránka nebo modal) |
| Pagination nav | Výpustka mezi stránkami značí, že v jejím menu je víc stránek. **Nikdy ji nedávej na začátek ani na konec** posloupnosti stránek |
| Text input | Když je hodnota moc dlouhá na jeden řádek, obsah se **vodorovně scrolluje** uvnitř pole při pohybu kurzoru |
| Text area | Uživatel může pole rozšířit úchytem, nebo obsah svisle scrollovat v nastavené výšce |

**ZDROJ:** Příslušné stránky `usage` jednotlivých komponent Carbonu, sekce Overflow content, lokální
kopie přečtená 30. 7. 2026. Například
https://carbondesignsystem.com/components/tag/usage/ ·
https://carbondesignsystem.com/components/checkbox/usage/ ·
https://carbondesignsystem.com/components/tabs/usage/

**Vzor, který z toho vyplývá** (moje syntéza, třída **C**): u **labelu** je zalomení lepší než
zkrácení. U **hodnoty nebo názvu** je zkrácení v pořádku, ale musí být doprovozené tooltipem. U
**hlášky** není přijatelné ani jedno, hláška se musí vejít celá.

## Tooltip na hover nestačí

**PRAVIDLO:** Když je zkrácený text dosažitelný klávesnicí (tag, tab, položka dropdownu), musí se celý
text odhalit **i na focus**, ne jen na hover. Carbon k tomu u dropdownu doporučuje svůj vlastní
tooltip místo tooltipu prohlížeče právě kvůli klávesové přístupnosti.
**KDY PLATÍ:** Každý zkrácený text na interaktivním prvku.
**TŘÍDA:** B
**ZDROJ:** Carbon, Dropdown usage, Overflow content, verbatim: „add an ellipsis (…) for overflow, and
use a tooltip to display the full text, preferably a Carbon tooltip for keyboard accessibility where
possible." https://carbondesignsystem.com/components/dropdown/usage/ ·
Carbon, Tag accessibility: „By mouse, the full title is disclosed in a browser tooltip on hover. By
keyboard, the full title is disclosed on focus in a tooltip."
https://carbondesignsystem.com/components/tag/accessibility/
**KDY NEPLATÍ:** Neinteraktivní zkrácený text (odstavec, hodnota v buňce bez interakce). Tam
klávesnice focus nedostane a tooltip prohlížeče na hover je jediná dostupná cesta. Což je zároveň
důvod, proč u takového textu zvážit, jestli má být zkrácený vůbec.

---

## Co tahle nota neřeší

- Délku řádku a čitelnost dlouhého textu.
  [Typografie](../../ux-design/pravidla/typografie.md).
- Reflow a chování při 320 CSS px (WCAG 1.4.10). To je zmíněné ve
  [2x grid a breakpointy](../zaklady/2x-grid-a-breakpointy.md), tvrdá opora je ve
  [formulářích a stavech](../../ux-design/pravidla/formulare-a-stavy.md).
- Overflow menu jako komponentu. Carbon ji má, ale v přečtené kopii samostatná stránka není.

## Zdroj

IBM Carbon Design System, Overflow content pattern, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/patterns/overflow-content/
Doplněno sekcemi Overflow content ze stránek `usage` jednotlivých komponent. Vzor je krátký a nemá
sekci References, Carbon k němu žádné externí zdroje neuvádí. Třída **B**.
