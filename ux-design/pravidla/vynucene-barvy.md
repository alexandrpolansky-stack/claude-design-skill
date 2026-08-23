# Vynucené barvy (forced colors)

Režim, ve kterém prohlížeč zahodí tvoje barvy a nahradí je uživatelskou paletou. Nejznámější případ
je Windows High Contrast Mode. Není to varianta tmavého režimu ani přístupnostní doplněk, je to
**třetí barevný režim s vlastními pravidly**, ve kterém přestane platit několik jiných pravidel
téhle knihovny.

Související: [Hloubka a stíny](hloubka-a-stiny.md) · [Stroke a hranice](stroke-a-hranice.md) ·
[Theming a dark mode](theming-a-dark-mode.md) · [Kontrast a barva](kontrast-a-barva.md) ·
[Tlačítka](tlacitka.md)

## Rychlé rozhodnutí

1. **Nebojuj s tím.** Uživatel si paletu zvolil, protože jinak nevidí. Tvoje barvy jsou ta méně
   důležitá strana.
2. **Testuj to, co nese význam:** hranice ovládacích prvků, focus ring, stavy, ikony, grafy.
3. **Kde hloubku nese stín, přidej v tomhle režimu hranici.** `box-shadow` je vynucen na `none`.
4. **Kde význam nese gradient nebo obrázek na pozadí, přidej text nebo tvar.** Nepodařené pozadí
   zmizí taky.
5. **Barvy, které prohlížeč nepřebíjí, ber ze systémových klíčových slov,** ne z vlastní palety.
6. **`forced-color-adjust: none` je poslední možnost,** ne způsob, jak si udržet vzhled.
7. **Ikona jen jako barevná plocha bez tvaru zmizí.** Platí i pro stavové tečky.

## Co to je a kdy nastane

**PRAVIDLO:** Počítej s tím, že prohlížeč může tvoje barvy nahradit uživatelskou paletou, a navrhni
rozhraní tak, aby v tu chvíli nepřestalo nést význam.
**KDY PLATÍ:** Každé rozhraní. Není to nic okrajového: režim zapínají lidé se sníženým viděním,
se světloplachostí a s migrénami, a v podnikovém prostředí bývá vynucený politikou.
**PROČ:** V tomhle režimu už nerozhoduješ o barvě ty. Rozhoduješ jen o tom, jestli rozhraní zůstane
srozumitelné, když barvu ztratíš.
**TŘÍDA:** A pro mechanismus.
**ZDROJ:** MDN, `forced-colors`, verbatim: „used to detect if the user agent has enabled a forced
colors mode where it enforces a user-chosen limited color palette on the page. An example of a forced
colors mode is Windows High Contrast mode." Hodnoty jsou `none` a `active`.
https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors Čteno 23. 8. 2026.
**KDY NEPLATÍ:** Nikdy, ale míra práce se liší. U textového obsahu se typicky nestane nic. U rozhraní,
které nese význam barvou, tvarem plochy a stínem, se rozpadne hodně.

```css
@media (forced-colors: active) {
  /* sem patří náhrady, ne kosmetika */
}
```

## Co prohlížeč přebije

**PRAVIDLO:** U těchhle vlastností se tvoje hodnota zahodí. Nepočítej s nimi jako s nositelem
významu.

| Vlastnost | Co se stane |
|---|---|
| `color`, `background-color` | Nahrazeno systémovou barvou |
| `border-color`, `outline-color` | Nahrazeno systémovou barvou |
| `text-decoration-color`, `text-emphasis-color` | Nahrazeno |
| `column-rule-color`, `-webkit-tap-highlight-color` | Nahrazeno |
| SVG `fill` a `stroke` | Nahrazeno |
| **`box-shadow`** | **Vynuceno na `none`** |
| **`text-shadow`** | **Vynuceno na `none`** |
| **`background-image`** | **Vynuceno na `none` u všeho, co není `url()`**, tedy gradienty pryč |
| `color-scheme` | Vynuceno na `light dark` |
| `scrollbar-color` | Vynuceno na `auto` |

**TŘÍDA:** A.
**ZDROJ:** MDN, forced-colors, sekce o vynucených vlastnostech, verbatim: „the browser treats the
values of certain properties as if they have no author-level values specified. These properties have
their values forced by the browser at paint time and are selected from the set of system colors to
ensure consistent contrast for common UI elements."
https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors Čteno 23. 8. 2026.

## Čtyři pravidla knihovny, která tím přestanou platit

Tohle je hlavní důvod, proč tahle nota existuje. Nejde o exotický režim, jde o to, že **ruší
mechanismy, na kterých stojí jiná pravidla**.

| Pravidlo jinde v knihovně | Co se s ním stane | Náhrada |
|---|---|---|
| [Hloubka a stíny](hloubka-a-stiny.md): hloubku nes barvou plochy nebo stínem | **Obojí padá.** `box-shadow` je `none` a barva plochy je přepsaná | Hranice. MDN to sama uvádí jako doporučený postup |
| [Stroke a hranice](stroke-a-hranice.md): hranice komponenty musí být vidět (WCAG 3:1) | Hranice **zůstane**, ale její barvu určuje systém | Ověř, že hranice vůbec existuje. Komponenta bez `border`, která se spoléhá na kontrast ploch, zmizí |
| [Theming a dark mode](theming-a-dark-mode.md): `color-scheme` řídíš ty | `color-scheme` je vynucen na `light dark` | Nepočítej s tím, že si v tomhle režimu udržíš vlastní téma |
| [Kontrast a barva](kontrast-a-barva.md): sémantika stavů barvou | Chyba, varování a úspěch **splynou** do jedné palety | Stav musí nést i ikona nebo text. To pravidlo knihovna má, tady je jeho nejtvrdší důvod |

**Praktický důsledek:** komponenta, která je „jen světlejší obdélník se stínem", v tomhle režimu
přestane existovat jako komponenta. Uživatel uvidí text bez ohraničení.

MDN dává přímo tuhle náhradu, verbatim v komentáři vlastní ukázky: „Use a border instead, since
box-shadow is forced to 'none' in forced-colors mode".

```css
.karta {
  box-shadow: 0 1px 3px rgb(0 0 0 / 0.2);
}

@media (forced-colors: active) {
  .karta {
    border: 1px solid ButtonBorder;
  }
}
```

## Systémové barvy

**PRAVIDLO:** U vlastností, které prohlížeč **nepřebíjí**, používej systémová klíčová slova, ne
vlastní hodnoty. Jinak se paleta rozpadne na dva různé světy.
**TŘÍDA:** A.
**ZDROJ:** MDN, `<system-color>`, verbatim: „In forced colors mode, authors should use colors from
the `<system-color>` type for all properties that are not in the set of properties whose colors are
overridden. This ensures that the page consistently uses the same color palette across all
properties." https://developer.mozilla.org/en-US/docs/Web/CSS/system-color Čteno 23. 8. 2026.

| Klíčové slovo | K čemu |
|---|---|
| `Canvas` / `CanvasText` | Pozadí a text obsahu dokumentu |
| `Field` / `FieldText` | Pozadí a text vstupního pole |
| `ButtonFace` / `ButtonText` / `ButtonBorder` | Plocha, text a hranice ovládacího prvku |
| `LinkText` / `VisitedText` / `ActiveText` | Odkaz nenavštívený, navštívený, aktivní |
| `Highlight` / `HighlightText` | Pozadí a text vybrané položky |
| `SelectedItem` / `SelectedItemText` | Vybraná položka, například zaškrtnutý checkbox |
| `Mark` / `MarkText` | Zvýrazněný text (`<mark>`) |
| `GrayText` | Text vypnutého (disabled) prvku |
| `AccentColor` / `AccentColorText` | Akcentovaný ovládací prvek |

**Nejužitečnější dvojice je `ButtonBorder`.** Většina náhrad za ztracený stín a ztracenou plochu
skončí u hranice a `ButtonBorder` je to, co má uživatel nastavené pro ovládací prvky.

**`GrayText` je jediný způsob**, jak v tomhle režimu sdělit vypnutý stav. Vlastní šedá se přepíše na
běžnou barvu textu, takže disabled tlačítko bude vypadat jako aktivní. Souvisí s
[Disabled versus read-only](../../enterprise-ui/vzory/disabled-vs-read-only.md): tohle je další důvod,
proč vypnutý stav nikdy nést jen barvou.

## `forced-color-adjust`

**PRAVIDLO:** `forced-color-adjust: none` použij jen tam, kde barva **sama nese informaci, kterou
nejde vyjádřit jinak**, typicky vzorník barev, náhled fotky nebo kategoriální legenda grafu.
Nikdy ne proto, abys udržel vzhled značky.
**KDY PLATÍ:** Vždy.
**PROČ:** Vypnutím režimu na prvku vracíš odpovědnost za kontrast sobě, a to u uživatele, jehož
nastavení jsi právě obešel. Když to uděláš, musíš kontrast v tom prvku zaručit sám.
**TŘÍDA:** A pro mechanismus, C pro seznam legitimních případů.
**ZDROJ:** MDN, `forced-color-adjust`, hodnoty `auto`, `none`, `preserve-parent-color`. Verbatim:
„allows authors to opt certain elements out of forced colors mode, which then restores the control of
those values to CSS. This property should only be used to make changes that will support a user's
color and contrast requirements."
https://developer.mozilla.org/en-US/docs/Web/CSS/forced-color-adjust Čteno 23. 8. 2026.
**KDY NEPLATÍ:** Logo. To bývá první, co lidi chtějí vyjmout, ale logo v jedné barvě je pořád logo.

## Backplates

Prohlížeč kreslí za text na obrázku podklad, aby text zůstal čitelný.

**ZDROJ:** MDN, forced-colors, verbatim: „browsers will draw 'backplates' behind text to help ensure
text legibility by preserving contrast when text is placed on top of images."

**Důsledek pro návrh:** hero s textem přes fotku bude v tomhle režimu vypadat jinak, než jsi kreslil,
ale bude čitelný. To je správně a nesnaž se to potlačit. Zkontroluj jen, že se ti kvůli podkladu
nerozpadne rozvržení.

## Jak to otestovat

**PRAVIDLO:** Otestuj to, nehádej. Bez zapnutého režimu nepoznáš, co zmizelo.
**TŘÍDA:** C.

| Kde | Jak |
|---|---|
| Chrome a Edge DevTools | Rendering panel, „Emulate CSS media feature forced-colors" |
| Firefox | `about:config`, nastavit vysoký kontrast, nebo systémové nastavení |
| Windows | Nastavení, Usnadnění přístupu, Kontrastní motivy |
| Rychlá kontrola bez nástrojů | Dočasně nastav v CSS všem prvkům `box-shadow: none` a `background-image: none`. Když rozhraní přestane dávat smysl, v režimu vynucených barev taky přestane |

Poslední řádek je hrubý, ale odchytí nejčastější chybu, tedy komponentu bez hranice.

## Co tahle nota neřeší

- **Konkrétní palety Windows kontrastních motivů.** Jsou uživatelské a mění se.
- **`prefers-contrast`.** Jiná mediální feature, jiný účel (uživatel chce vyšší kontrast, ale paleta
  se nevynucuje). Knihovna k ní zatím nemá nic.
- **Vysoký kontrast v macOS a v Androidu.** Chovají se jinak a `forced-colors` na ně nemusí platit.
- **Dataviz v tomhle režimu.** Kategoriální paleta grafu je nejtěžší případ a knihovna nemá obecnou
  dataviz notu, viz [STATUS.md](../../STATUS.md).

## Zdroj

- MDN, [`forced-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors),
  [`forced-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/forced-color-adjust),
  [`<system-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/system-color).
  Vše čteno 23. 8. 2026.
- WCAG 2.2, SC 1.4.1 Use of Color a SC 1.4.11 Non-text Contrast, Level AA, jako důvod, proč stav
  nesmí být nesen jen barvou. https://www.w3.org/WAI/WCAG22/quickref/
- Microsoft Learn, [Windows High contrast mode](https://learn.microsoft.com/en-us/fluent-ui/web-components/design-system/high-contrast),
  jako dodavatelský popis režimu. Konkrétní hodnoty odtud nepřebíráme.
