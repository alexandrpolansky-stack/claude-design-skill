# Vrstvy enterprise UI: prvky, komponenty, vzory

Vstupní nota sekce `enterprise-ui/`. Vysvětluje, proč je znalost rozdělená do třech vrstev a v jaké
vrstvě hledat odpověď na jakou otázku. Otevři ji, když stavíš produktovou aplikaci (dashboard, CRUD,
administraci, konfigurátor) a nevíš, kterou notou začít.

Související: [Volba komponenty](volba-komponenty.md) ·
[Osmibodová mřížka](../../ux-design/zakony-principy/osmibodova-mrizka.md) ·
[Design system DRIVE](../../ux-design/priklady-ds/design-system-drive.md)

---

## Odkud tahle sekce je a co v ní záměrně není

Sekce je destilát dokumentace **IBM Carbon Design System** (78 stránek: 13 vzorů, 20 komponent ve
variantách usage/style/accessibility, mřížka, obsahové pokyny). Přečteno z lokální kopie 30. 7. 2026,
kanonický zdroj je [carbondesignsystem.com](https://carbondesignsystem.com/).

**Co jsem přebral:** rozhodovací pravidla (kdy modal a kdy panel, kdy tabulka a kdy seznam),
klávesovou a focus mechaniku, obsahová pravidla, strukturu vzorů. To jsou principy, ne cizí vizuál.

**Co jsem záměrně nepřebral:** barevné tokeny, hex hodnoty, IBM Plex, konkrétní elevation stíny,
ikonovou knihovnu, „AI presence" vizuál. To je identita Carbonu, ne přenositelná znalost. Kdo
zkopíruje tokeny, postaví produkt, který vypadá jako IBM, a to není cíl. Kde je v notách číslo
(48 px, 3:1, 16 sloupců), je tam proto, že nese strukturní vztah nebo regulatorní požadavek, ne
proto, že je to Carbonový odstín.

**Třídy důkazu** používám stejné jako [`ux-design/pravidla/`](../../ux-design/pravidla/):
**A** = tvrdá opora (peer-reviewed, právní požadavek, normativní text),
**B** = publikovaná konvence (design systém, výzkumná organizace),
**C** = řemeslná praxe bez měření.
Většina obsahu téhle sekce je **B**: je to konvence velkého design systému, který ji používá
v produkci na stovkách produktů. To není totéž jako měřený nález a nikde to tak nevydávám.

---

## Tři vrstvy a co do které patří

| Vrstva | Odpovídá na | Kde v repu |
|---|---|---|
| Prvky (elements) | Jaká je geometrie, rytmus, sazba, barva | [2x grid](2x-grid-a-breakpointy.md), `ux-design/color/`, `ux-design/typography/` |
| Komponenty | Jak se chová jeden ovládací prvek, jaké má stavy a varianty | [`enterprise-ui/komponenty/`](../komponenty/) |
| Vzory (patterns) | Jak víc komponent spolu řeší jeden opakující se úkol | [`enterprise-ui/vzory/`](../vzory/) |

### Vzor je jednotka opakovaného použití, ne komponenta

**PRAVIDLO:** Když se v produktu opakuje úkol (načítání, prázdný seznam, potvrzení nevratné akce,
filtrování), hledej odpověď ve vzoru, ne v komponentě. Vzor určuje, které komponenty se použijí,
v jakém pořadí a co se stane při chybě.
**KDY PLATÍ:** Vždy, když stejná situace nastane na víc než jedné obrazovce.
**PROČ:** Komponentní knihovna zajistí, že tlačítko vypadá všude stejně. Nezajistí, že se všude
stejně potvrzuje mazání.
**TŘÍDA:** C. Tohle je moje formulace, ne Carbonovo tvrzení. Doložitelné je jen to, že Carbon vzory
jako samostatnou vrstvu dokumentuje a že jeho vzory skutečně komponenty kombinují a odkazují na ně.
**ZDROJ:** Struktura dokumentace Carbonu: 13 stránek `patterns` (dialogy, notifikace, načítání,
prázdné stavy, formuláře, filtrování, hledání, stavové indikátory, přetečení, běžné akce, disabled
a read-only stavy) vedle stránek `components` a `elements`. Každý vzor má sekci „Related components
and patterns". Příklad: https://carbondesignsystem.com/patterns/dialog-pattern/
**KDY NEPLATÍ:** Jednorázová obrazovka, která v produktu existuje jednou a nebude se opakovat.
Tam je vzor režie bez výnosu.

### Produktivní a expresivní poloha

**PRAVIDLO:** Carbon vede volbu velikostí podle toho, jestli je moment produktivní nebo expresivní.
Produktivní je běžný software: velikost „Large (productive)" je „the most common button size in
software products" a páruje se se 14px tělem textu. Expresivní poloha je pro momenty s větší sazbou
(16px tělo) a Carbon ji přiřazuje bannerům na webu, nikoliv aplikaci. Stejné dělení má u vstupů
(default versus fluid): default „in productive moments where space is at a premium", fluid
„in expressive moments".
**KDY PLATÍ:** Volba velikosti tlačítek, vstupů a sazby.
**PROČ:** Carbon zdůvodnění uvádí jen jako párování s velikostí tělového textu, ne psychologicky.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button sizes, verbatim: „Large (productive): This is the most common button size
in software products. Pairs with 14px body copy." a „Large (expressive): The larger expressive type
size within this button provides balance when paired with 16px body copy. Used by the IBM.com team
in website banners." https://carbondesignsystem.com/components/button/usage/ ·
Styling default versus fluid u dropdownu a vstupů:
https://carbondesignsystem.com/components/dropdown/usage/
**KDY NEPLATÍ:** Carbon sám u fluid stylu uvádí i neexpresivní důvody (stísněný prostor, napojení na
složitou komponentu jako toolbar), takže to není čisté dělení web versus aplikace.

### Jedna velikostní škála na obrazovku

**PRAVIDLO:** Na jedné obrazovce používej jednu výškovou třídu formulářových prvků. Když jsou
vstupy 40 px, mají 40 px i selecty, tlačítka a vyhledávání. Nemíchej velikosti v jedné skupině
tlačítek.
**KDY PLATÍ:** Každá formulářová obrazovka, toolbar, panel.
**PROČ:** Různé výšky prvků na jedné lince rozbíjejí klíčové linie mřížky, což je nejviditelnější
druh nedbalosti. Škála existuje kvůli konzistenci, ne kvůli výběru.
**TŘÍDA:** B
**ZDROJ:** Carbon uvádí u dropdownu, selectu, textového vstupu i vyhledávání shodně tři výšky
(32 / 40 / 48 px) s pokynem držet na jedné stránce jednu, a u tlačítek explicitní „nedoporučujeme
míchat velikosti ve skupině tlačítek".
https://carbondesignsystem.com/components/dropdown/usage/ ·
https://carbondesignsystem.com/components/button/usage/
**KDY NEPLATÍ:** Vnořený hustý kontext (řádek tabulky, toolbar) uvnitř volnější stránky. Tam je
menší třída záměrná a platí uvnitř toho kontejneru konzistentně.

---

## Jak sekci procházet

1. Neznáš zadání do detailu: [Volba komponenty](volba-komponenty.md), tabulka úkol → komponenta.
2. Řešíš opakující se situaci: [`vzory/`](../vzory/).
3. Řešíš chování jednoho prvku: [`komponenty/`](../komponenty/).
4. Řešíš rozvržení a breakpointy: [2x grid](2x-grid-a-breakpointy.md).
5. Píšeš texty v UI: [UX copy v produktu](ux-copy-v-produktu.md).
6. Cokoliv interaktivního: [Klávesnice a focus](klavesnice-a-focus.md) plus
   [Oznámení pro čtečky](oznameni-pro-ctecky.md). Tyhle dvě jsou povinné, ne doplňkové.

## Co tahle sekce neřeší

- Vizuální identitu, paletu a font. To je `ux-design/color/`, `ux-design/typography/` a
  [vizuální craft](../../ux-design/pravidla/vizualni-craft.md).
- Sektorový kontext (jak jinak vypadá bankovní a jak státní aplikace). To je
  [`ux-design/kontext/`](../../ux-design/kontext/).
- Evidenčně podložená mikropravidla k tlačítkům, kontrastu, pohybu a formulářům. To je
  [`ux-design/pravidla/`](../../ux-design/pravidla/), a má tvrdší zdroje než tahle sekce. Když si
  odporují, platí `pravidla/`, protože tam je třída A tam, kde tady je B.
- Implementaci v Reactu. Tahle sekce je o rozhodování, ne o API knihovny.
