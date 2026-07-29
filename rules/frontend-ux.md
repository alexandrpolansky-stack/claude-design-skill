---
paths:
  - "**/*.tsx"
  - "**/*.jsx"
  - "**/*.css"
  - "**/*.scss"
  - "**/*.html"
  - "**/*.vue"
  - "**/*.svelte"
---

# Frontend / UX build-time pravidla

Když stavím nebo upravuju UI, držím se těchhle destilovaných pravidel (imperativy).
Plný zdroj a hloubka: skill `design-advisor` v repu claude-design-skill, index `plugin/skills/design-advisor/references/INDEX.md`.

## UX zákony (aplikuj vždy)
- Fitts: klíčové akce velké a snadno cílitelné; primární CTA velké.
- Hick: omezuj počet voleb; neukazuj 10 tlačítek, kde stačí 2-3.
- Miller (7+-2): seskupuj do chunků po 5-9 (menu, formuláře, navigace).
- Jakob: chovej se jako známé weby; needěs uživatele nestandardní navigací.
- Tesler: složitost přesuň na systém (předvyplnění, autodetekce), ne na uživatele.
- Postel: buď liberální ke vstupu, vždy dej jasnou zpětnou vazbu.

## Hierarchie a layout
- 8pt grid pro spacing (násobky 8/4), konzistentní mezery.
- Gestalt: blízkost = skupina; seskupuj whitespacem, ne čarami/rámečky.
- Velkorysý whitespace, obsah musí dýchat. Méně je víc.

## Barvy
- 60-30-10: dominantní / sekundární / akcent. Akcent jen pro CTA a zvýraznění.
- Sémantika (success/warning/error) konzistentně a nikdy jen barvou (přidej ikonu/popisek).

## Typografie
- Jasná hierarchie H1>H2>H3>body, modulární škála (např. faktor 1.25).
- Line-height ~140-150 % pro tělo textu. Max ~2 fonty (nadpis + tělo).
- Min. velikost těla ~16px.

## Afordance a feedback
- Tlačítka vypadají jako tlačítka; interaktivní prvky jsou rozpoznatelné.
- Na každou akci viditelná zpětná vazba (stav, animace, hláška).
- Žádné „Norman doors": z prvku musí být jasné, co dělá.

## Přístupnost (nepodkročitelné)
- Kontrast min. 4.5:1 (běžný text), 3:1 (velký text a UI prvky). Cíl WCAG 2.1.
- Viditelný focus stav, plná ovladatelnost klávesnicí.

## Proces (u větší stavby)
- Než stavím: kdo je uživatel, jaký je jeho cíl, jaký je hlavní flow. Postup viz nota `proces/step-by-step-ux-ui.md`.
- Hotový příklad design systému s konkrétními tokeny: nota `priklady-ds/design-system-drive.md` (DRIVE).
