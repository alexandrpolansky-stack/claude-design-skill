# Frontend / UX build-time pravidla

Destilát pro moment, kdy se reálně píše UI kód. Imperativy, žádná teorie.
Hloubka a odůvodnění: [knihovna](../_index.md).

**Tenhle soubor je zdroj.** Zkrácená path-scoped varianta pro Claude Code je
[frontend-ux.md](frontend-ux.md) a je z něj odvozená: když měníš pravidlo, oprav obě místa, jinak
se rozejdou (už se to jednou stalo, viz [STATUS.md](../STATUS.md)).

## UX zákony (aplikuj vždy)
- Fitts: klíčové akce velké a snadno cílitelné; primární CTA velké.
- Hick: omezuj počet voleb; neukazuj 10 tlačítek, kde stačí 2-3.
- Miller (7±2): seskupuj do chunků po 5-9 (menu, formuláře, navigace).
- Jakob: chovej se jako známé weby; neděs uživatele nestandardní navigací.
- Tesler: složitost přesuň na systém (předvyplnění, autodetekce), ne na uživatele.
- Postel: buď liberální ke vstupu, vždy dej jasnou zpětnou vazbu.

Zdroj: [UX Laws](../ux-design/zakony-principy/ux-laws.md).

## Hierarchie a layout
- 8pt grid pro spacing (násobky 8/4), konzistentní mezery.
- Gestalt: blízkost = skupina; seskupuj whitespacem, ne čarami/rámečky.
- Velkorysý whitespace, obsah musí dýchat. Méně je víc.

Zdroj: [Osmibodová mřížka](../ux-design/zakony-principy/osmibodova-mrizka.md), [Layout Theory](../ux-design/layout/layout-theory.md).

## Barvy
- 60-30-10: dominantní / sekundární / akcent. Akcent jen pro CTA a zvýraznění.
- Sémantika (success/warning/error) konzistentně a nikdy jen barvou (přidej ikonu/popisek).

Zdroj: [Pravidlo 60-30-10](../ux-design/color/pravidlo-60-30-10.md), [Color Theory](../ux-design/color/color-theory.md).

## Typografie
- Jasná hierarchie H1>H2>H3>body, modulární škála (např. faktor 1.25).
- Line-height ~140-150 % pro tělo textu. Max ~2 fonty (nadpis + tělo).
- Min. velikost těla ~16px.

Zdroj: [Typografie](../ux-design/pravidla/typografie.md) (tvrdá čísla se třídou důkazu),
názvosloví [Typografie: základy a anatomie](../ux-design/typography/typography-zaklady-anatomie.md).

## Afordance a feedback
- Tlačítka vypadají jako tlačítka; interaktivní prvky jsou rozpoznatelné.
- Na každou akci viditelná zpětná vazba (stav, animace, hláška).
- Žádné „Norman doors": z prvku musí být jasné, co dělá.

Zdroj: [GENERAL UX KNOWLEDGE](../ux-design/ux-zaklady/general-ux-knowledge.md).

## Přístupnost (nepodkročitelné)
- Kontrast min. 4.5:1 (běžný text), 3:1 (velký text a UI prvky). Cíl WCAG 2.1.
- Viditelný focus stav, plná ovladatelnost klávesnicí.

## Implementační pasti, které mlčky nezaberou
- Zkracování textu funguje jen na blokovém boxu. Na `<span>` s `display: inline` se `overflow`
  i `text-overflow` zahodí bez chyby.
- Položka flexu nebo gridu se bez `min-width: 0` nesmrskne pod svůj obsah, takže se nezkrátí.
  V gridu totéž řeší `minmax(0, 1fr)` místo `1fr`.
- `z-index` neuteče ze stacking contextu. Zakládá ho i `opacity` pod 1, `filter`,
  `backdrop-filter`, `transform`, `will-change`, `contain` a `container-type`. Modál a popover
  renderuj do top layeru (`showModal()`, Popover API), ne do kontejneru.
- `position: fixed` uvnitř předka s `transform`, `perspective` nebo `filter` se pozicuje vůči
  tomu předkovi, ne vůči viewportu.
- `position: sticky` umře pod jakýmkoli předkem s `overflow` jiným než `visible`, a bez nenulového
  `top` se chová jako `relative`.
- Tabulka, jejíž řádky mění filtr, potřebuje deklarované šířky a fixní layout, jinak se s každou
  změnou dat překreslí celá mřížka.

Zdroj: [Přetečení a zkracování](../enterprise-ui/vzory/preteceni-a-truncation.md),
[Překryvy a vrstvení](../enterprise-ui/vzory/prekryvy-a-vrstveni.md),
[Stabilita layoutu](../enterprise-ui/vzory/stabilita-layoutu.md). Všechno třída A ze specifikace.

## Proces (u větší stavby)
- Než stavím: kdo je uživatel, jaký je jeho cíl, jaký je hlavní flow.
  Postup: [Step By Step UX-UI](../ux-design/proces/step-by-step-ux-ui.md).
- Hotový příklad design systému s konkrétními tokeny:
  [Design system DRIVE](../ux-design/priklady-ds/design-system-drive.md).
