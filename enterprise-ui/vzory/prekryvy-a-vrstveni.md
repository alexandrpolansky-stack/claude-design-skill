# Překryvy a vrstvení

Proč překryv nevyleze nad sousedy, nedrží se při scrollu, nebo se pozicuje vůči něčemu jinému, než
čekáš. Otevři při stavbě čehokoli, co se překrývá s obsahem: modál, boční panel, dropdown, tooltip,
lepivá hlavička, plovoucí toolbar.

Související: [Dialogy a panely](dialogy-a-panely.md) ·
[Tooltip a toggletip](../komponenty/tooltip-a-toggletip.md) ·
[Výběr ze seznamu](../komponenty/vyber-ze-seznamu.md) · [Notifikace](notifikace.md) ·
[Stabilita layoutu](stabilita-layoutu.md) ·
[Hloubka a stíny](../../ux-design/pravidla/hloubka-a-stiny.md)

---

## Rychlé rozhodnutí

1. **Modál a popover nedávej do kontejneru.** Renderuj je do **top layeru** (`<dialog>` plus
   `showModal()`, nebo Popover API). Tím celý problém se z-indexem odpadá, místo aby se řešil.
2. **Když překryv neleze nad sousedy, nezvedej z-index.** Když nefunguje `10`, nepomůže `9999`.
   Hledej předka, který založil stacking context.
3. **Stacking context zakládá i to, co vypadá nevinně:** `opacity: 0.99`, `filter`, `backdrop-filter`,
   `transform`, `will-change`, `contain`, `container-type`. Sklíčkový header s rozostřením a karta
   s container query jsou přesně ty případy.
4. **`position: fixed` uvnitř předka s `transform`, `perspective` nebo `filter`** se pozicuje vůči
   **tomu předkovi**, ne vůči viewportu.
5. **`position: sticky` umře, když má kterýkoli předek `overflow` jiný než `visible`.** Nehlásí to nic.
6. **Sticky bez nenulového insetu se chová jako `relative`.** Chybějící `top` je nejčastější příčina
   „sticky nefunguje".
7. **z-index ber ze škály definované na jednom místě**, ne ad hoc u komponenty.

---

## Proč „zvýším z-index" nefunguje

Stacking context se v nadřazeném kontextu chová jako **jeden nedělitelný blok**. Když ho předek
založí, je jedno, jaké číslo dá dítě: celý ten blok se v rodičově kontextu zařadí podle **rodičova**
z-indexu, a dítě z něj nemá jak vylézt.

**ZDROJ:** MDN, Stacking context, verbatim: „Stacking contexts are treated atomically as a single
unit in the parent stacking context." A dál: „Importantly, the `z-index` values of its child stacking
contexts only have meaning within its parent's stacking context."
https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Stacking_context
**TŘÍDA:** A (chování dané specifikací, ne názor)

**Praktický důsledek:** `z-index: 9999` na dropdownu uvnitř karty s `transform: translateY(0)`
nedělá nic. Symptom vypadá jako „menu se schovává pod další kartu", příčina je o dvě patra výš
a v úplně jiné vlastnosti, takže se hledá na špatném místě.

## Co zakládá stacking context

Úplný seznam z MDN, seskupený podle toho, jak často to člověk napíše bez úmyslu vrstvit:

| Skupina | Vlastnost a hodnota |
|---|---|
| **Kořen** | `<html>` |
| **Pozice** | `position: absolute` nebo `relative` **a zároveň** `z-index` jiný než `auto` · `position: fixed` nebo `sticky` (samo o sobě, bez z-indexu) |
| **Položka flexu nebo gridu** | `z-index` jiný než `auto` |
| **Průhlednost a míchání** | `opacity` menší než `1` · `mix-blend-mode` jiný než `normal` |
| **Vizuální efekty** (hodnota jiná než `none`) | `transform`, `scale`, `rotate`, `translate`, `filter`, `backdrop-filter`, `perspective`, `clip-path`, `mask` / `mask-image` / `mask-border` |
| **Izolace a containment** | `isolation: isolate` · `contain: layout` nebo `paint` (tedy i `contain: strict` a `contain: content`) · `container-type: size` nebo `inline-size` |
| **Optimalizace** | `will-change` s jakoukoli vlastností, která by kontext založila na neinicialní hodnotě |
| **Top layer** | prvek v top layeru a jeho `::backdrop` |
| **Animace** | prvek, u kterého se vlastnost zakládající kontext (třeba `opacity`) animovala přes `@keyframes` s `animation-fill-mode: forwards` |

**ZDROJ:** MDN, Stacking context, sekce „The stacking context", úplný výčet.
https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Stacking_context
**TŘÍDA:** A

**Které z toho překvapí v praxi:**

- **`opacity` menší než 1.** Karta ztlumená na `0.95` v disabled stavu uvězní všechno, co z ní má
  vylézt. Viz [Disabled vs. read-only](disabled-vs-read-only.md).
- **`backdrop-filter`.** Poloprůhledná hlavička s rozostřením pozadí je dnes běžný vzor a zakládá
  kontext pro celý svůj obsah.
- **`container-type: inline-size`.** Přidáš container query, aby byla komponenta responzivní, a
  rozbiješ jí dropdown. Ty dvě věci spolu na první pohled nesouvisí vůbec.
- **`will-change`.** Přidává se kvůli výkonu, obvykle bez vědomí, že mění vrstvení.
- **`contain`.** Totéž, přidává se kvůli výkonu.

## Top layer: řešení, ne obcházení

**PRAVIDLO:** Překryv, který má být nad **vším** v dokumentu (modál, popover, menu vyvolané
z komponenty), nerenderuj do stromu vedle spouštěče a neřeš mu z-index. Pošli ho do **top layeru**.
**KDY PLATÍ:** Modální dialog, popover, menu, které přesahuje svůj kontejner.
**PROČ:** Top layer je vrstva prohlížeče nad všemi vrstvami dokumentu, takže otázka „který předek
mi zakládá kontext" přestane existovat.
**TŘÍDA:** A
**ZDROJ:** MDN, Top layer, verbatim: „The top layer is a specific layer that spans the entire width
and height of the viewport and sits on top of all other layers displayed in a web document."
https://developer.mozilla.org/en-US/docs/Glossary/Top_layer

Co se do top layeru dostane podle MDN:

| Způsob | Prvek |
|---|---|
| `HTMLDialogElement.showModal()` | `<dialog>` zobrazený jako modální |
| `HTMLElement.showPopover()` | prvek s popoverem |
| `Element.requestFullscreen()` | prvek na celou obrazovku |
| otevření nabídky | picker u customizable `<select>` |

**Pozor na jednu věc:** prvek v top layeru **sám zakládá stacking context**, stejně jako jeho
`::backdrop`. To je v pořádku a je to žádoucí, jen to znamená, že vrstvení uvnitř modálu je zase
vlastní svět.

**Starší cesta** je portál, tedy vyrenderovat překryv jako dítě `<body>`. Řeší to sice předky, ale
ne bez ceny: přijdeš o dědění stylů z místa spouštěče a musíš si sám pohlídat focus a to, aby obsah
pod modálem přestal být dostupný. Top layer je řešení téhož problému, které tohle nese s sebou.

## `position: fixed` a jeho containing block

**PRAVIDLO:** `position: fixed` **není** vždycky vůči viewportu. Když má **kterýkoli předek**
`transform`, `perspective` nebo `filter` s jinou hodnotou než `none`, stane se ten předek
containing blockem a fixed prvek se pozicuje vůči **němu**.
**KDY PLATÍ:** Vždy. Týká se i `will-change: transform`.
**TŘÍDA:** A
**ZDROJ:** MDN, `position`, verbatim: „the element's containing block is the initial containing
block established by the viewport, unless any ancestor has `transform`, `perspective`, or `filter`
property set to something other than `none` [...] which then causes that ancestor to take the place
of the elements containing block."
https://developer.mozilla.org/en-US/docs/Web/CSS/position

**Kde to potkáš:** modál uvnitř karty, která má hover animaci přes `transform`. Vypadá to, že se
modál „otevřel do karty" místo přes obrazovku. Nebo plovoucí tlačítko ve wrapperu, který má
`filter: drop-shadow(...)`.

**Poznámka o rozsahu:** citovaná stránka jmenuje `transform`, `perspective` a `filter` a zmiňuje
`will-change: transform`. Jiné vlastnosti (`backdrop-filter`, `contain`) zakládají **stacking
context**, což je jiná věc než containing block. Nepleť si to a netvrď o nich víc, než co je
doložené.

## `position: sticky`

**PRAVIDLO:** Sticky prvek se lepí ke svému **nejbližšímu předkovi se scrollovacím mechanismem**,
který vzniká, když má `overflow` hodnotu `hidden`, `scroll`, `auto` nebo `overlay`. A to i tehdy,
když ten předek ve skutečnosti vůbec nescrolluje.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** A
**ZDROJ:** MDN, `position`, verbatim: „a sticky element 'sticks' to its nearest ancestor that has a
'scrolling mechanism' (created when `overflow` is `hidden`, `scroll`, `auto`, or `overlay`), even if
that ancestor isn't the nearest actually scrolling ancestor."
https://developer.mozilla.org/en-US/docs/Web/CSS/position

**Praktický důsledek, který stojí za celou tuhle sekci:** `overflow: hidden` se na předka píše
z úplně jiných důvodů, typicky aby ořízl zaoblený roh nebo schoval vodorovné přetečení. V tu chvíli
se lepivá hlavička tabulky přestane lepit a **nic to neohlásí**. Symptom je „sticky nefunguje",
příčina je jednořádková vlastnost o tři patra výš, napsaná kvůli zaoblení.

**Druhá nejčastější příčina:** sticky vyžaduje aspoň jednu **nenulovou inset hodnotu** (`top`,
`bottom`, `inset-block-start` a podobně). Když jsou na dané ose obě `auto`, chová se prvek na té ose
jako `relative`. Tedy tiše nic.

## Jak to najít místo hádání

Číst stylopis na tohle nestačí, protože chyba je v **kombinaci** předka a potomka, ne v jedné
deklaraci. Prohlížeč to zodpoví za jeden průchod: vezmi prvek, který se chová špatně, a nech si
vypsat všechny jeho předky, kteří zakládají stacking context, i s důvodem.

```js
function stackingAncestors(el) {
  const out = [];
  for (let p = el.parentElement; p; p = p.parentElement) {
    const s = getComputedStyle(p);
    const why = [];
    if (s.position === 'fixed' || s.position === 'sticky') why.push(`position: ${s.position}`);
    if ((s.position === 'absolute' || s.position === 'relative') && s.zIndex !== 'auto')
      why.push(`position: ${s.position} + z-index: ${s.zIndex}`);
    if (parseFloat(s.opacity) < 1) why.push(`opacity: ${s.opacity}`);
    for (const prop of ['transform', 'scale', 'rotate', 'translate', 'filter',
                        'backdropFilter', 'perspective', 'clipPath', 'maskImage']) {
      if (s[prop] && s[prop] !== 'none') why.push(prop);
    }
    if (s.mixBlendMode !== 'normal') why.push(`mix-blend-mode: ${s.mixBlendMode}`);
    if (s.isolation === 'isolate') why.push('isolation: isolate');
    if (s.willChange !== 'auto') why.push(`will-change: ${s.willChange}`);
    if (/layout|paint|strict|content/.test(s.contain)) why.push(`contain: ${s.contain}`);
    if (s.containerType && s.containerType !== 'normal')
      why.push(`container-type: ${s.containerType}`);
    if (why.length) out.push({ el: p, why });
  }
  return out;
}
// stackingAncestors($0)  v konzoli, když máš prvek vybraný v inspektoru
```

**Než uvěříš prázdnému výsledku, ověř sondu.** Dej si do stránky vlastní předek s `opacity: 0.99`
a zkontroluj, že ho sonda najde. Čistý výsledek ze sondy, která neumí nic najít, je jen tiché
selhání o patro výš. (Stejná hygiena jako u sondy v
[Přetečení a zkracování](preteceni-a-truncation.md).)

Na `position: fixed` je to stejný postup, jen se hledají jen tři vlastnosti:

```js
[...document.querySelectorAll('*')].filter((el) => {
  const s = getComputedStyle(el);
  return s.transform !== 'none' || s.perspective !== 'none' || s.filter !== 'none';
});
```

## z-index jako škála, ne jako číslo

**PRAVIDLO:** Definuj vrstvy **na jednom místě** jako pojmenovanou škálu a u komponent se odkazuj
na jména, ne na čísla. Konkrétní hodnoty jsou skoro jedno, důležité je **pořadí** a to, že existuje
jediné místo, kde se dá celé pořadí přečíst.
**KDY PLATÍ:** Jakmile má produkt víc než jeden typ překryvu.
**TŘÍDA:** C (vlastní syntéza z praxe, MDN ani Carbon tohle nepředepisují)

Pořadí, které dává smysl, od spodu nahoru:

| Vrstva | Co v ní je |
|---|---|
| Základ | běžný obsah stránky |
| Lepivé prvky | hlavička tabulky, plovoucí toolbar, lišta s hromadnými akcemi |
| Rozbalené ovládání | dropdown, combo box, overflow menu, tooltip |
| Modální překryv | dialog a jeho backdrop |
| Systémové zprávy | toast a notifikace, které musí být vidět i nad modálem |

**Proč jsou notifikace nahoře:** zpráva o tom, že se něco nepovedlo uložit, musí být vidět i tehdy,
když uživatel stojí v modálu. Když ji schováš pod backdrop, uživatel čeká na výsledek akce, která už
tiše selhala. Souvisí s [Notifikace](notifikace.md), kde je pravidlo, co smí zmizet samo.

**Když používáš top layer, tahle škála se scvrkne**, protože modál a popover z ní vypadnou. Zbude
pořadí uvnitř dokumentu, což je přesně ta část, kterou má smysl mít pod kontrolou.

## Co tahle nota neřeší

- **Kdy použít modál a kdy boční panel.** [Dialogy a panely](dialogy-a-panely.md).
- **Kam dát focus a jak ho udržet uvnitř překryvu.**
  [Klávesnice a focus](../zaklady/klavesnice-a-focus.md).
- **Jak má překryv vypadat**, tedy stín, hranice, hloubka.
  [Hloubka a stíny](../../ux-design/pravidla/hloubka-a-stiny.md) a
  [Stroke a hranice](../../ux-design/pravidla/stroke-a-hranice.md).
- **Jak se má překryv animovat.** [Pohyb](../../ux-design/pravidla/pohyb.md).
- **Zamčení scrollu pod modálem.** Chování napříč prohlížeči jsem neověřoval, takže o něm nepíšu.
  Otevřená otázka, ne opomenutí.
- **Kde překryv vzniká vizuálně**, tedy jestli má vyrůst ze spouštěče. To je otázka pohybu
  a prostorové návaznosti, v knihovně zatím nepokrytá.

## Zdroj

MDN Web Docs, čteno 22. 8. 2026. Všechno v téhle notě kromě poslední sekce je **třída A**, protože
popisuje chování dané specifikací, ne doporučení:

- Stacking context, úplný výčet podmínek a atomicita.
  https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Stacking_context
- `position`, containing block u `fixed` a scrollovací mechanismus u `sticky`.
  https://developer.mozilla.org/en-US/docs/Web/CSS/position
- Top layer, co to je a co se do něj dostane.
  https://developer.mozilla.org/en-US/docs/Glossary/Top_layer

Škála vrstev na konci je **třída C**, vlastní syntéza. Carbon vrstvení překryvů nepopisuje, jeho
elevation tokeny řeší vizuální hloubku, ne pořadí v z-ose.
