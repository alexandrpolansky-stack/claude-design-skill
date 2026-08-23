# Theming a dark mode

Jak postavit téma tak, aby přepnutí do tmavého režimu nerozbilo hloubku, kontrast ani značku.
Knihovna k tomu dosud měla tři roztroušená pravidla, tahle nota je spojuje a doplňuje vrstvu,
která chyběla: sémantické tokeny a to, co prohlížeč dělá sám.

Související: [Hloubka a stíny](hloubka-a-stiny.md) · [Kontrast a barva](kontrast-a-barva.md) ·
[Anti-slop](anti-slop.md) · [Stroke a hranice](stroke-a-hranice.md) ·
[Formuláře a stavy](formulare-a-stavy.md)

## Rychlé rozhodnutí

1. **Nikdy neinvertuj.** Tmavé téma není světlé s obrácenou luminancí.
2. **Pojmenuj tokeny podle role, ne podle barvy.** `surface-raised`, ne `gray-100`.
3. **Nastav `color-scheme` na `:root`.** Bez toho zůstanou scrollbary, formulářové prvky a canvas
   ve světlém, ať máš CSS jakékoliv.
4. **`prefers-color-scheme: light` znamená taky „uživatel si nevybral".** Nejde je rozlišit.
5. **Přepínač má tři stavy:** světlé, tmavé, podle systému. Výchozí je systém.
6. **Změř kontrast v obou režimech.** Brand barva, která projde na bílé, na tmavé typicky propadne.
7. **V tmavém tématu nese hloubku světlejší plocha, ne stín.**
8. **Logo, ilustrace a grafy potřebují vlastní variantu.** Průhledné PNG s tmavou kresbou zmizí.

## Režim, téma a značka nejsou totéž

| Pojem | Co to je | Kolik jich je |
|---|---|---|
| **Režim** | Světlý nebo tmavý | Dva, plus „podle systému" jako volba |
| **Téma** | Konkrétní sada hodnot pro režim | Nejméně dvě, u produktu klidně čtyři (high contrast) |
| **Značka** | Barvy, které se nemění podle režimu | Jedna, ale s variantami pro kontrast |

Nejčastější chyba je slít je dohromady a mít jednu paletu s `if dark`. Pak se každá nová komponenta
řeší znovu.

## Sémantická vrstva tokenů

**PRAVIDLO:** Komponenta nikdy nesahá na barvu přímo. Sahá na token pojmenovaný podle **role**
(`surface-base`, `surface-raised`, `text-primary`, `text-muted`, `border-subtle`, `action-primary`)
a téma tomu tokenu přiřadí hodnotu. Přepnutí režimu pak mění jednu mapu, ne komponenty.
**KDY PLATÍ:** Jakmile má produkt víc než jedno téma, tedy i „jen" světlé a tmavé.
**PROČ:** Token pojmenovaný `gray-100` v tmavém tématu buď lže, nebo se musí přebarvit na
`gray-800`, což jméno dělá nepravdivým. Jméno podle role přežije obě témata i změnu značky.
Zároveň je to jediný způsob, jak poznat, že se na dvou místech myslí totéž.
**TŘÍDA:** B. Publikovaná konvence design systémů, ne měření. Carbon, Material 3 i USWDS staví
téma na sémantické vrstvě nad surovou paletou.
**ZDROJ:** [Carbon, color usage](https://carbondesignsystem.com/elements/color/usage/), čtyři
vrstvy tématu. Konkrétní hodnoty nepřebíráme, viz pravidlo knihovny o Carbonu.
**KDY NEPLATÍ:** Jednorázová landing page s jedním režimem. Tam je token navíc režie bez užitku.

**Proč invertování nefunguje.** Kdyby stačilo obrátit luminanci, stačil by jeden filtr. Nefunguje
to ze čtyř důvodů zároveň a každý z nich se projeví jinde:

| Co se rozbije | Proč | Kde je řešení |
|---|---|---|
| **Hloubka** | Stín je tmavší plocha. Na tmavém pozadí není luminanční rozdíl, o který by se oko opřelo | [Hloubka a stíny](hloubka-a-stiny.md): výše ležící vrstva je světlejší |
| **Hranice** | Ve světlém tématu odděluje plocha, v tmavém často musí převzít práci hranice | [Stroke a hranice](stroke-a-hranice.md) |
| **Brand barva** | Sytá barva laděná na bílou má na tmavém pozadí jiný kontrastní poměr, typicky horší pro text | Sekce o kontrastu níže |
| **Obrázky a grafika** | Průhledné PNG s tmavou kresbou, mapy, screenshoty a loga zmizí nebo září | Sekce o médiích níže |

## Co dělá prohlížeč sám: `color-scheme`

**PRAVIDLO:** Na `:root` nastav `color-scheme`. Když podporuješ oba režimy, `color-scheme: light dark`.
Bez toho zůstane část rozhraní světlá bez ohledu na tvoje CSS.
**KDY PLATÍ:** Každá stránka, která má tmavý režim, i kdyby jen jako tmavou sekci.
**PROČ:** Je to jediný způsob, jak říct prohlížeči, co má udělat s tím, co ty nestyluješ.
**TŘÍDA:** A. Chování odvozené ze specifikace, ne názor.
**ZDROJ:** MDN, `color-scheme`, verbatim: „User agents change the following aspects of the UI chrome
to match the used color scheme: The color of the canvas surface. The default colors of scrollbars
and other interaction UI. The default colors of form controls. The default colors of other
browser-provided UI, such as 'spellcheck' underlines." Ovlivňuje taky „the used values of CSS system
colors". https://developer.mozilla.org/en-US/docs/Web/CSS/color-scheme Čteno 23. 8. 2026.
**KDY NEPLATÍ:** Nikdy. I stránka jen ve světlém režimu má důvod uvést `color-scheme: light`, aby ji
automatické ztmavení prohlížeče nepřebarvilo.

**Hodnota `only`** zakazuje prohlížeči téma přebít. MDN verbatim: „Forbids the user agent from
overriding the color scheme for the element. Can be used to turn off color overrides caused by
Chrome's Auto Dark Theme, by applying `color-scheme: only light;` on a specific element or `:root`."
Sáhni po ní jen tam, kde automatické ztmavení něco měřitelně rozbíjí, ne preventivně.

**`color-scheme` nestačí na tvůj obsah.** MDN to říká přímo: „Component authors must use the
`prefers-color-scheme` media feature to support the color schemes on the rest of the elements."

## `prefers-color-scheme` nerozliší volbu od mlčení

**PRAVIDLO:** Nepovažuj `prefers-color-scheme: light` za doklad, že uživatel chce světlý režim.
Znamená to „chce světlý **nebo** si nevybral". Návrh, který na tom rozlišení stojí, stojí na písku.
**KDY PLATÍ:** Vždy, zvlášť u analytiky a u rozhodnutí „kolik lidí chce dark mode".
**PROČ:** Hodnota `no-preference` v mediální feature není.
**TŘÍDA:** A.
**ZDROJ:** MDN, `prefers-color-scheme`, verbatim k hodnotě `light`: „Indicates that user has notified
that they prefer an interface that has a light theme, or has not expressed an active preference."
https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme Čteno 23. 8. 2026.
**KDY NEPLATÍ:** Vlastní přepínač, do kterého uživatel sáhl. Ten volbu doloží, systémová preference ne.

Souvislost: knihovna má v [Dev tools a SaaS](../kontext/dev-tools-saas.md) zapsané, že tvrzení
„vývojáři měřitelně preferují dark mode" **nemá oporu**. Tohle je jeden z důvodů, proč se to špatně
měří.

## `light-dark()` místo dvou bloků

**PRAVIDLO:** Když už `color-scheme: light dark` máš, definuj hodnoty tokenů funkcí `light-dark()`
místo duplikovaného `@media` bloku.
**KDY PLATÍ:** Projekty, které mohou cílit na Baseline 2024 a novější.
**PROČ:** Dvojice hodnot zůstane na jednom řádku, takže nejde přidat token do jednoho režimu
a zapomenout na druhý. To je nejčastější zdroj „v dark mode je to jedno místo divné".
**TŘÍDA:** A pro chování funkce, C pro doporučení ji upřednostnit.
**ZDROJ:** MDN, `light-dark()`, verbatim: „returns the first value if the used color scheme is
`light` or if no preference is set and the second value if the used color scheme is `dark`" a
„To enable support for the `light-dark()` color function, the `color-scheme` must have a value of
`light dark`, usually set on the `:root` pseudo-class." Baseline: newly available od května 2024.
https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/light-dark Čteno 23. 8. 2026.
**KDY NEPLATÍ:** Podpora starších prohlížečů. Pak `@media (prefers-color-scheme: dark)` s přepisem
tokenů, nikdy s přepisem komponent.

```css
:root {
  color-scheme: light dark;
  --surface-base:   light-dark(#ffffff, #16181c);
  --surface-raised: light-dark(#f5f6f8, #1e2126);
  --text-primary:   light-dark(#16181c, #e9ecef);
  --border-subtle:  light-dark(#e1e4e8, #2c3138);
}
```

Hodnoty výše jsou ukázka tvaru, ne doporučená paleta. Vlastní si změř.

## Kontrast se měří dvakrát

**PRAVIDLO:** Každý pár popředí a pozadí změř zvlášť ve světlém a zvlášť v tmavém tématu. Nepředpokládej,
že když projde jeden, projde druhý. Zvlášť to platí pro barvu značky na tlačítku a pro stavové barvy.
**KDY PLATÍ:** Vždy. Tělo textu 4,5:1, velký text a nositelé významu v UI 3:1.
**PROČ:** Kontrastní poměr není symetrický vůči inverzi. Sytá značková barva bývá laděná na bílé
pozadí a v tmavém tématu se dostane do pásma, kde na ní bílý text neprojde a proti tmavému pozadí
je zároveň málo odlišná.
**TŘÍDA:** A pro prahy, C pro tvrzení o chování značkových barev (řemeslné pozorování).
**ZDROJ:** WCAG 2.2 SC 1.4.3 Contrast (Minimum) a SC 1.4.11 Non-text Contrast, Level AA.
https://www.w3.org/WAI/WCAG22/quickref/
**KDY NEPLATÍ:** Dekorativní prvky, logo a vypnutý stav jsou z 1.4.3 vyňaté.

**Praktický důsledek:** značka typicky potřebuje dvě varianty akcentu na režim, ne jednu na produkt.
Stejná logika jako u [Pravidla 60-30-10](../color/pravidlo-60-30-10.md), kde override popisuje dvojici
„tmavší pod bílý text, jasná na rámečky".

Konkrétní past s fialovou a hnědou v tmavém režimu je v [Anti-slop](anti-slop.md), sekce
„Dark mode s fialovým nebo hnědým textem".

## Přepínač má tři stavy

**PRAVIDLO:** Nabídni **světlý, tmavý a podle systému**, s výchozí hodnotou „podle systému".
Volbu ulož a při dalším načtení aplikuj **před prvním vykreslením**.
**KDY PLATÍ:** Každý produkt s vlastním přepínačem.
**PROČ:** Dvoustavový přepínač uživatele natrvalo odpojí od systémové preference, takže mu produkt
zůstane světlý, i když si v systému večer přepne na tmavý. Aplikace až po vykreslení způsobí
záblesk světlého tématu, který je v noci fyzicky nepříjemný.
**TŘÍDA:** C. Řemeslná praxe, nedohledal jsem k tomu měření.
**KDY NEPLATÍ:** Produkt, který má z podstaty jediné téma (například nástroj na úpravu fotek, kde
by světlé pozadí zkreslovalo vnímání barev). Tam přepínač nedávej vůbec, ne ho dělat dvoustavový.

**Ikona přepínače nemá být jen symbol.** Slunce a měsíc nesou dvě různá čtení: „aktuálně je zapnuto"
versus „kliknutím přepneš na". Přidej text nebo přístupný název, který říká cílový stav.

## Barva rozhraní prohlížeče

**PRAVIDLO:** Nastav `<meta name="theme-color">` zvlášť pro světlý a tmavý režim, ať se lišta
prohlížeče na mobilu neodlepí od pozadí stránky.
**TŘÍDA:** A pro mechanismus.
**ZDROJ:** MDN, `theme-color`, verbatim: „indicates a suggested color that user agents should use to
customize the display of the page or of the surrounding user interface", a k mediální variantě: „To
set the media to which the theme color metadata applies, include the `media` attribute with a valid
media query list".
https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color
Čteno 23. 8. 2026.

```html
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#16181c" media="(prefers-color-scheme: dark)">
```

## Média, která téma nepřežijí

| Prvek | Co se stane | Co s tím |
|---|---|---|
| Logo s tmavou kresbou v průhledném PNG | Zmizí | Druhá varianta souboru, přepnutá `<picture>` s `media` |
| Screenshot světlého rozhraní | Svítí jako lampa | Rámeček a tlumené pozadí, nebo tmavá varianta snímku |
| Ilustrace s bílým pozadím | Bílý obdélník uprostřed tmavé stránky | SVG s `currentColor`, kde to jde |
| Graf a dataviz | Kategoriální paleta laděná na bílou ztratí odlišitelnost | Vlastní paleta na režim, měř odstup, ne jen kontrast |
| Mapa | Světlé dlaždice v tmavém rozhraní | Tmavý styl dlaždic od poskytovatele |

**TŘÍDA:** C, řemeslný výčet z praxe.

## Co tahle nota neřeší

- **Konkrétní paletu.** Žádné hex hodnoty kromě ukázky tvaru. Paletu si změř.
- **High contrast a `forced-colors`.** Řeší [Vynucené barvy](vynucene-barvy.md). Pozor: v tom
  režimu je `color-scheme` vynucen na `light dark`, takže vlastní téma tam neudržíš.
- **Dataviz palety pro tmavý režim.** Obecná dataviz mimo Sheets je otevřená mezera, viz
  [STATUS.md](../../STATUS.md).
- **Přepínání tématu bez záblesku v konkrétním frameworku.** Princip je „aplikuj před prvním
  vykreslením", implementace se liší podle toho, jestli renderuješ na serveru.
- **Hustotu jako parametr tématu.** Jiná mezera, viz STATUS.

## Zdroj

- MDN, [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/color-scheme),
  [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme),
  [`light-dark()`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/light-dark),
  [`theme-color`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color).
  Vše čteno 23. 8. 2026.
- WCAG 2.2, SC 1.4.3 Contrast (Minimum) a SC 1.4.11 Non-text Contrast, Level AA.
  https://www.w3.org/WAI/WCAG22/quickref/
- Sémantická vrstva tématu: [Carbon, color usage](https://carbondesignsystem.com/elements/color/usage/).
- Seznam otázek, ze kterého tahle nota vyšla:
  [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines),
  MIT, kategorie „Dark Mode & Theming". Pravidla odtud jsou holé imperativy bez odůvodnění, takže
  posloužila jako osnova a odpovědi jsou dohledané v MDN a WCAG, ne převzaté.
