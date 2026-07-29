# Knihovna designové znalosti (MOC)

Vstupní bod do celé knihovny. Princip: tahle mapa je levný index, ze kterého se vytáhne jen
relevantní nota. Nenačítat všechno.

Značka **[stub]** = nota je zatím kostra, hodí se doplnit. Stav a mezery: [STATUS.md](STATUS.md).

## Sekce

| Sekce | Not | O čem |
|---|---|---|
| [neuro-design/](neuro-design/) | 1 | Kognitivní ergonomie, eye-tracking, algoritmy vizuální váhy. Nejhutnější dokument v knihovně. |
| [ux-design/](ux-design/) | 31 | UX zákony, proces, barvy, typografie, layout, trendy, etika, hotový design systém. |
| [web-dev/](web-dev/) | 4 | HTML/CSS základy, vkládání CSS, stylizace textu, práce s obrázky. |
| [sheets/](sheets/) | 3 | Google Sheets reporty: rozhodovací rámec, brand tokeny, Apps Script vrstva. |

---

## Neuro-design (začni tady u větší stavby)

- [Neuro-design master document](neuro-design/neuro-design-master.md) — kognitivní ergonomie a architektura datových rozhraní. Pět modulů: biologie vizuální percepce (F/Z-pattern, kognitivní zátěž), matematika mřížek a Gestalt, algoritmy sémantického škálování (výpočet vizuální váhy prvku), persuasive design a vedení pozornosti, diagnostika chyb a fail-safe protokoly. Psané přímo jako instrukční rámec pro generování a evaluaci UI.

## UX základy

- [GENERAL UX KNOWLEDGE](ux-design/ux-zaklady/general-ux-knowledge.md) — Don Norman, afordance, viditelnost, zpětná vazba, mapování, role v UX týmu, tech terminologie.
- [Design Research Methods](ux-design/ux-zaklady/design-research-methods.md) — metody UX výzkumu.
- [Content strategy a UX writing](ux-design/ux-zaklady/content-strategy-ux-writing.md) — think like an editor, obsahová strategie.
- [Define the problem](ux-design/ux-zaklady/define-the-problem.md) — definice problému před návrhem řešení.
- [Design Process](ux-design/ux-zaklady/design-process.md) — celkový designový proces.
- [Understand who your users are](ux-design/ux-zaklady/understand-your-users.md) — kdo jsou uživatelé, persony.
- [Discovery](ux-design/ux-zaklady/discovery.md) — fáze objevování problému a kontextu.
- [Etika v UX](ux-design/ux-zaklady/etika-v-ux.md) — etika, dark patterns naopak.
- [UX experience](ux-design/ux-zaklady/ux-experience.md) — z čeho se skládá uživatelský zážitek. **[stub]**

## Zákony a principy (nejvíc akční pro stavbu)

- [UX Laws](ux-design/zakony-principy/ux-laws.md) — Fitts, Hick, Jakob, Miller (7±2), Tesler, Postel, Parkinson, Gestalt zákony.
- [Osmibodová mřížka](ux-design/zakony-principy/osmibodova-mrizka.md) — 8pt grid pro konzistentní spacing.
- [Efekty](ux-design/zakony-principy/efekty.md) — kognitivní efekty v UX.
- [Principy a Pravidla](ux-design/zakony-principy/principy-a-pravidla.md) — návrhové principy a pravidla.

## Proces

- [Step By Step UX-UI WEB, APP Design](ux-design/proces/step-by-step-ux-ui.md) — celý postup: user flow, wireframy, AIDA, prototyp, usability a A/B testing, iterace.

## Barvy

- [Color Theory](ux-design/color/color-theory.md) — teorie barev, barevné kruhy, schémata.
- [Color Psychology](ux-design/color/color-psychology.md) — psychologie barev a emoce.
- [Color Grading](ux-design/color/color-grading.md) — ladění barev.
- [Pravidlo 60-30-10](ux-design/color/pravidlo-60-30-10.md) — poměr primární/sekundární/akcentní barvy.

## Typografie

- [Typography — základy, anatomie](ux-design/typography/typography-zaklady-anatomie.md) — anatomie písma, základy.
- [Serif a Sans Serif](ux-design/typography/serif-a-sans-serif.md) — kdy patkové vs. bezpatkové.
- [Práce s fontem](ux-design/typography/prace-s-fontem.md) — praktická práce s fonty.
- [Font pairing](ux-design/typography/font-pairing.md) — párování fontů. **[stub]**

## Layout

- [Layout Theory](ux-design/layout/layout-theory.md) — whitespace, margin, padding, rozložení.
- [Grids a Golden ratio](ux-design/layout/grids-a-golden-ratio.md) — mřížky a zlatý řez.

## Web-dev (implementace)

- [HTML a CSS](web-dev/html-a-css.md) — základy HTML a CSS, box model, selektory. Největší nota v sekci.
- [Stylizace textu](web-dev/stylizace-textu.md) — práce s textem v CSS.
- [Inserting CSS](web-dev/inserting-css.md) — způsoby vkládání CSS.
- [Using best images possible](web-dev/using-best-images.md) — volba a příprava obrázků.

## Google Sheets

- [Znalostní báze](sheets/znalostni-baze.md) — rozhodovací rámec otázka→graf, brand tokeny, archetypy reportů, A/B slop→profi, kritéria kvality.
- [NotebookLM destilát](sheets/notebooklm-destilat.md) — surovější výzkumný podklad včetně URL zdrojů.
- [Apps Script vrstva](sheets/apps-script-vrstva.md) — styling přes Apps Script a clasp.

## Příklad hotového design systému

- [Design system DRIVE](ux-design/priklady-ds/design-system-drive.md) — kompletní DS s konkrétními tokeny: paleta s hex kódy, typografická škála, WCAG kontrasty, komponenty (tlačítka, karty, mikrointerakce). Nejrozsáhlejší nota v knihovně, reálná ukázka převedení designu do specifikací.

## Trendy

- [Grafické trendy](ux-design/trendy/graficke-trendy.md) **[stub]** · [Trendy v typografii](ux-design/trendy/trendy-v-typografii.md) **[stub]**

## Další

- [Logo Design](ux-design/logo-foto/logo-design.md) — návrh loga.
- [Photography](ux-design/logo-foto/photography.md) — základy fotografie pro design.

## Destiláty pro moment psaní kódu

Nepatří do knihovny, jsou to imperativy vytažené z toho, co je výše:

- [rules/frontend-ux.md](rules/frontend-ux.md) — path-scoped pravidlo (`.tsx`, `.css`), ke zkopírování do `~/.claude/rules/`.
- [rules/frontend-ux-detailed.md](rules/frontend-ux-detailed.md) — stejné imperativy s odkazy do knihovny.

## Zdroje k učení

- [Kurzy](ux-design/zdroje/kurzy.md) — grafické a UX kurzy.
- [Videa](ux-design/zdroje/videa.md) — UX/UI a barevné tutoriály. **[stub]**
