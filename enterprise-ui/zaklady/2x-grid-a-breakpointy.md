# Mřížka, breakpointy a chování panelů

Jak postavit rozvržení produktové aplikace tak, aby drželo rytmus napříč šířkami obrazovky. Otevři,
když řešíš, kolik sloupců, jak široké okraje, jak se má layout chovat při zvětšení okna a co udělá
vysunutý panel s obsahem.

Doplňuje [Osmibodovou mřížku](../../ux-design/zakony-principy/osmibodova-mrizka.md) (proč násobky
osmi) a [Layout theory](../../ux-design/layout/layout-theory.md) (whitespace, margin, padding).
Tahle nota přidává to, co tam není: sloupcový systém, breakpointy a chování panelů.

---

## Mini unit: základní jednotka je 8 px

**PRAVIDLO:** Všechny rozměry, odsazení a mezery odvozuj z násobků 8 px. Fixní škála: 8, 16, 24, 32,
48, 64, 80. Odsazení uvnitř kontejneru je 16 px na standardních breakpointech.
**KDY PLATÍ:** Celá aplikace, včetně vnitřního odsazení komponent.
**PROČ:** Jedna jednotka odvozuje všechna čísla ze sebe, takže vzniknou klíčové linie i tam, kde je
nikdo záměrně nekreslil. Když se dvě komponenty drží stejné škály, mřížkový efekt vznikne sám.
**TŘÍDA:** B
**ZDROJ:** Carbon, 2x Grid: „The basic unit of 2x Grid geometry is the 8-pixel square mini unit."
Padding: „Padding is always a fixed multiple of mini units: 16 pixels at all standard breakpoints."
https://carbondesignsystem.com/elements/2x-grid/overview/
**KDY NEPLATÍ:** Optická korekce jednotlivého prvku (zarovnání ikony, kompenzace vizuální váhy
kulatého tvaru). Tam je 1 px legitimní. Viz
[vizuální craft](../../ux-design/pravidla/vizualni-craft.md).

## Princip 2x: děl nebo znásob dvěma

**PRAVIDLO:** Fluidní mřížku staví dělení na polovinu (1, 2, 4, 8, 16 sloupců). Fixní mřížku staví
násobení (vezmi základní rozměr dlaždice a znásob ho dvěma, čtyřmi).
**KDY PLATÍ:** Návrh sloupcového systému nebo dlaždicového gridu.
**PROČ:** Obě cesty vedou na stejná čísla na hranici breakpointu, takže se dají v jednom layoutu
kombinovat bez konfliktu. Sloupcová a dlaždicová část stránky pak sedí na stejných linkách.
**TŘÍDA:** B
**ZDROJ:** Carbon, 2x Grid fundamentals: „The core concept of the 2x Grid is to divide or multiply by
two... Fluid grids are built by division, whereas fixed grids are built with multiplication. On
breakpoint boundaries, these sizes match."
https://carbondesignsystem.com/elements/2x-grid/overview/
**KDY NEPLATÍ:** Layout postavený na zlatém řezu nebo jiné proporci. To není chyba, jen jiný systém,
viz [Grids a golden ratio](../../ux-design/layout/grids-a-golden-ratio.md). Nemíchej je v jednom
projektu.

## Breakpointy

Konkrétní hodnoty Carbonu. Přebírám je jako referenci proto, že jsou vzájemně konzistentní
(šířka sloupce vždy vychází na násobek mini unitu), ne proto, že by byly jediné správné.

| Breakpoint | Od (px / rem) | Sloupců | Šířka sloupce | Padding | Vnější margin |
|---|---|---|---|---|---|
| Small | 320 / 20 | 4 | 25 % | 16 px | 0 |
| Medium | 672 / 42 | 8 | 12,5 % | 16 px | 16 px |
| Large | 1056 / 66 | 16 | 6,25 % | 16 px | 16 px |
| X-Large | 1312 / 82 | 16 | 6,25 % | 16 px | 16 px |
| Max | 1584 / 99 | 16 | 6,25 % | 16 px | 24 px |

**PRAVIDLO:** Testuj návrh i kód přímo na hranicích breakpointů, ne uprostřed rozsahu. Počet sloupců
je v rámci breakpointu konstantní, mění se šířka sloupce.
**TŘÍDA:** B
**ZDROJ:** Carbon, 2x Grid, tabulka breakpointů plus „For best results, test designs and code at each
of these standard breakpoints." https://carbondesignsystem.com/elements/2x-grid/overview/
**KDY NEPLATÍ:** Aplikace s garantovanou minimální šířkou (interní nástroj na firemních monitorech).
Tam malé breakpointy neřeš, ale WCAG 1.4.10 Reflow (AA) platí i tak, takže obsah se musí dát zobrazit
při 320 CSS px bez horizontálního scrollu.

## Fluidní, fixní, hybridní: podle toho, co uživatel chce vidět

**PRAVIDLO:** Rozhodni podle uživatelova cíle při zvětšení okna. Chce vidět **víc položek** (katalog,
seznam dlaždic): škáluj počet, tedy fixní dlaždice, které se zabalují. Chce vidět **víc z každé
položky** (dashboard, editor, dataviz): škáluj rozměr, tedy fluidní sloupce s pevným počtem.
**KDY PLATÍ:** Každá stránka s dynamickým obsahem.
**PROČ:** Když to obrátíš, uživatel roztáhne okno a nedostane nic navíc, jen víc bílé plochy nebo
naopak zbytečně natažené řádky textu.
**TŘÍDA:** B
**ZDROJ:** Carbon, Grid behaviors: „If a user's goal is to see more items, scale column count by
tiling fixed boxes. If a user wants to see more content within each item, scale boxes and use fixed
column counts." https://carbondesignsystem.com/elements/2x-grid/overview/
**KDY NEPLATÍ:** Nic, co má garantovanou délku řádku textu. Tam platí přednostně
45 až 75 znaků na řádek, viz [typografie](../../ux-design/pravidla/typografie.md).

**Hybridní chování běžných částí UI** (jedna dimenze fixní, druhá fluidní):

| Prvek | Šířka | Výška |
|---|---|---|
| Hlavička, toolbar | fluidní podle mřížky | fixní v mini unitech |
| Boční panel | fixní | fluidní podle okna |
| Menu, dropdown | fixní | fluidní podle obsahu |
| Datová tabulka | fluidní podle mřížky | fluidní podle obsahu |

## Poměry stran pro dlaždice a obrázky

**PRAVIDLO:** Rozměry dlaždic a mediálních boxů drž na jednom z poměrů 1:1, 2:1, 2:3, 3:2, 4:3, 16:9.
Minimální výška dlaždice odpovídá poměru 2:1.
**KDY PLATÍ:** Dlaždicové gridy, karty, náhledy, obrázková pole.
**PROČ:** Omezená množina poměrů udělá z náhodné sady dlaždic soustavu. Bez ní se rozdíly ve výškách
čtou jako chyba.
**TŘÍDA:** C jako estetické tvrzení, B jako konvence. Měření k tomu Carbon nemá, uvádí „heighten the
perception of unity".
**ZDROJ:** Carbon, Sizing scale, Aspect ratio. https://carbondesignsystem.com/elements/2x-grid/overview/
Minimální poměr dlaždice 2:1: https://carbondesignsystem.com/components/tile/usage/
**KDY NEPLATÍ:** Obsah s principiálně neznámou výškou (uživatelský text). Tam rezervuj minimální
výšku a nech ho růst, viz [Přetečení a truncation](../vzory/preteceni-a-truncation.md).

## Klíčové linie jsou test hotového layoutu

**PRAVIDLO:** V hotovém rozvržení musí být vidět svislé i vodorovné linie, na kterých se zarovnává
víc než jeden prvek. Když žádná taková linie neexistuje, layout je jen sada kontejnerů.
**KDY PLATÍ:** Kontrola před předáním návrhu.
**PROČ:** Zarovnání na společnou linku nese oko z prvku na prvek. Vodorovné zarovnání je stejně
důležité jako svislé, což se v praxi zanedbává.
**TŘÍDA:** C (estetické tvrzení bez měření), ale je to nejlevnější dostupná kontrola kvality.
**ZDROJ:** Carbon, Key lines: „ensure the overall layout has visible key lines: vertical and
horizontal lines on which multiple objects align... Horizontal and vertical alignment are equally
critical." https://carbondesignsystem.com/elements/2x-grid/overview/
**KDY NEPLATÍ:** Záměrně asymetrická expresivní kompozice. Tam je porušení linky výrazový prostředek,
ale musí být jediné a zjevně chtěné.

## Mezery mezi sloupci: tři režimy

Carbon má tři režimy mezer mezi sloupci: **wide**, **narrow** a **condensed**. Konkrétní hodnoty
uvádí u komponent, ne v přehledu mřížky.

| Režim | Mezera | Kdy podle Carbonu |
|---|---|---|
| Wide (výchozí) | 32 px (margin okolo boxu se rovná jeho paddingu, dohromady 32) | „gives the most breathing room between the data table and the other components or content" |
| Narrow | 16 px, komponenta zasahuje do mezery | u tabulky „will hang the component into the gutter and create a desirable type alignment between the data table's title and other type on the page" |
| Condensed | 1 px | fluidní formuláře; „Fluid forms are architectural and remain cohesive by never allowing vertical or horizontal space between inputs" |

**PRAVIDLO:** U condensed režimu dávej pozor na nezamýšlený vztah mezi nesouvisejícími bloky. Carbon
řešení jmenuje: hybridní mřížka nebo odlišná barva plochy.
**TŘÍDA:** B
**ZDROJ:** Carbon, celkový gutter 32 px: „The margin around each grid box matches its padding, for
a total gutter of 32 pixels." https://carbondesignsystem.com/elements/2x-grid/overview/ ·
Popis režimů u tabulky včetně varování verbatim: „The data table can be used on a condensed grid, but
care should be taken to avoid any unintentional relationships with other UI elements. Use a hybrid
grid or a dissimilar background color to avoid the components blending in to each other."
https://carbondesignsystem.com/components/data-table/usage/ ·
Hodnoty 32 / 16 / 1 px a přiřazení k formulářům:
https://carbondesignsystem.com/components/form/usage/
**KDY NEPLATÍ:** Fluidní formulář, kde je nulová mezera záměrná. Carbon k němu dodává, že narrow
režim (16 px) se ve formulářích typicky nepoužívá, protože dostává text do mezery.

## Chování panelů

Boční a horní panely jsou to, co v produktové aplikaci nejčastěji rozbije mřížku. Tři chování:

| Typ | Šířka | Co udělá s obsahem |
|---|---|---|
| Flexibilní | Sbalený a rozbalený stav, pevná šířka v rozbaleném | Při rozbalení stlačí obsah i mřížku, nebo obsah vytlačí za hranu okna |
| Fixní | Stálá, nelze sbalit, stojí mimo responzivní mřížku | Trvale zabírá šířku, mřížka se počítá ze zbytku |
| Plovoucí | Nad obsahem | Mřížku neovlivní, ale zakrývá obsah, takže musí být zavíratelný |

**PRAVIDLO:** Rozhodni dopředu, jestli panel obsah stlačuje, nebo ho zakrývá. Plovoucí panel, který
nelze zavřít, je chyba. Svislé panely jdou vždy do plné výšky okna.
**KDY PLATÍ:** Levá navigace, pravý detailní panel, filtrační drawer.
**PROČ:** Když panel stlačí mřížku, změní se počet sloupců pro obsah a musíš to navrhnout pro oba
stavy. Když to nikdo nerozhodne, sbalení panelu rozláme layout.
**TŘÍDA:** B
**ZDROJ:** Carbon, Grid influencers, Panel behavior: „All vertical panels expand to fill the full
height of the browser window" a u plovoucích „must be dismissible by the user".
https://carbondesignsystem.com/elements/2x-grid/overview/
**KDY NEPLATÍ:** Nic, ale u malých breakpointů se z flexibilního panelu typicky stává plovoucí, což
je legitimní změna typu.

---

## Co tahle nota neřeší

- Proč zrovna 8 a ne jiné číslo. To je
  [Osmibodová mřížka](../../ux-design/zakony-principy/osmibodova-mrizka.md).
- Whitespace jako výrazový prostředek a vztah margin/padding.
  [Layout theory](../../ux-design/layout/layout-theory.md).
- Délku řádku a typografickou škálu. [Typografie](../../ux-design/pravidla/typografie.md).
- **Implementaci CSS gridu knihovna nepokrývá.** `web-dev/html-a-css.md` je úvod do HTML a CSS
  a grid ani flexbox v něm nejsou. Jediná gridová mechanika, kterou knihovna má, je `minmax(0, 1fr)`
  proti nesmrštitelné stopě, viz [Přetečení a zkracování](../vzory/preteceni-a-truncation.md).

## Zdroj

IBM Carbon Design System, 2x Grid Overview, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/elements/2x-grid/overview/
Čísla breakpointů a sizing škály jsou Carbonova konkrétní volba (třída **B**), ne norma. Přebírám je
jako vnitřně konzistentní referenci. Tvrzení o vnímané jednotě a klíčových linkách jsou třída **C**,
Carbon k nim neuvádí měření.
