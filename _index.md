# Knihovna designové znalosti (MOC)

Vstupní bod do celé knihovny. Princip: tahle mapa je levný index, ze kterého se vytáhne jen
relevantní nota. Nenačítat všechno.

Značka **[stub]** = nota je zatím kostra, hodí se doplnit. Stav a mezery: [STATUS.md](STATUS.md).

## Sekce

| Sekce | Not | O čem |
|---|---|---|
| [neuro-design/](neuro-design/) | 1 | Kognitivní ergonomie, eye-tracking, algoritmy vizuální váhy. Nejhutnější dokument v knihovně. |
| [ux-design/](ux-design/) | 48 | UX zákony, proces, barvy, typografie, layout, trendy, etika, hotový design systém, evidence-based pravidla, kontext podle sektoru. |
| [web-dev/](web-dev/) | 4 | HTML/CSS základy, vkládání CSS, stylizace textu, práce s obrázky. |
| [sheets/](sheets/) | 3 | Google Sheets reporty: rozhodovací rámec, brand tokeny, Apps Script vrstva. |

---

## Neuro-design (začni tady u větší stavby)

- [Neuro-design master document](neuro-design/neuro-design-master.md) – kognitivní ergonomie a architektura datových rozhraní. Pět modulů: biologie vizuální percepce (F/Z-pattern, kognitivní zátěž), matematika mřížek a Gestalt, algoritmy sémantického škálování (výpočet vizuální váhy prvku), persuasive design a vedení pozornosti, diagnostika chyb a fail-safe protokoly. Psané přímo jako instrukční rámec pro generování a evaluaci UI.

## UX základy

- [GENERAL UX KNOWLEDGE](ux-design/ux-zaklady/general-ux-knowledge.md) – Don Norman, afordance, viditelnost, zpětná vazba, mapování, role v UX týmu, tech terminologie.
- [Design Research Methods](ux-design/ux-zaklady/design-research-methods.md) – metody UX výzkumu.
- [Content strategy a UX writing](ux-design/ux-zaklady/content-strategy-ux-writing.md) – think like an editor, obsahová strategie.
- [Define the problem](ux-design/ux-zaklady/define-the-problem.md) – definice problému před návrhem řešení.
- [Design Process](ux-design/ux-zaklady/design-process.md) – celkový designový proces.
- [Understand who your users are](ux-design/ux-zaklady/understand-your-users.md) – kdo jsou uživatelé, persony.
- [Discovery](ux-design/ux-zaklady/discovery.md) – fáze objevování problému a kontextu.
- [Etika v UX](ux-design/ux-zaklady/etika-v-ux.md) – etika, dark patterns naopak.
- [UX experience](ux-design/ux-zaklady/ux-experience.md) – z čeho se skládá uživatelský zážitek. **[stub]**

## Zákony a principy (nejvíc akční pro stavbu)

- [UX Laws](ux-design/zakony-principy/ux-laws.md) – Fitts, Hick, Jakob, Miller, Tesler, Postel, Parkinson, Gestalt zákony. Fitts, Hick i Miller mají u sebe opravný callout: populární verze (větší tlačítko = míň chyb, kratší menu = rychlejší rozhodnutí, max 7±2 položek) je vyvrácená auditem 2026, teorie zůstala, jen s přesnějším rozsahem platnosti.
- [Osmibodová mřížka](ux-design/zakony-principy/osmibodova-mrizka.md) – 8pt grid pro konzistentní spacing.
- [Efekty](ux-design/zakony-principy/efekty.md) – kognitivní efekty v UX.
- [Principy a Pravidla](ux-design/zakony-principy/principy-a-pravidla.md) – návrhové principy a pravidla.

## Pravidla (evidence-based, s třídou důkazu)

Vzniklo z fáze 2 projektu design-rule-system (29. 7. 2026). Každé pravidlo má šest povinných
částí: PRAVIDLO, KDY PLATÍ, PROČ, TŘÍDA (A tvrdá opora / B publikovaná konvence nebo regulace /
C řemeslná praxe), ZDROJ, KDY NEPLATÍ. Otevři, když stavíš konkrétní komponentu a chceš vědět,
proč zrovna tahle hodnota, ne jiná.

- [Tlačítka](ux-design/pravidla/tlacitka.md) – kolik primárních tlačítek, jak přiřadit variantu, pět stavů, focus ring, destruktivní akce a tvrdé mantinely velikosti (Fitts, SMALLER-OF model, WCAG 2.5.8).
- [Tvar a radius](ux-design/pravidla/tvar-a-radius.md) – border-radius: Material 3 škála jako výchozí systém, optická kulatost vnořených prvků, a forenzní důkaz, že „zaoblené je klikatelnější" je nepodložený folklór (NHS commit bez citace).
- [Stroke a hranice](ux-design/pravidla/stroke-a-hranice.md) – kdy border vs. stín vs. whitespace, WCAG 3:1 pro viditelnost hranic komponent, 1px oddělovače, focus ring na zaoblených prvcích.
- [Hloubka a stíny](ux-design/pravidla/hloubka-a-stiny.md) – kdy hloubku nést barvou plochy a kdy stínem, ověřené elevation škály (Carbon, Material 3), proč stín nikdy nesmí nést hranici ovládacího prvku.
- [Pohyb](ux-design/pravidla/pohyb.md) – trvání a easing s ověřenými tokeny, přerušitelnost, prefers-reduced-motion, WCAG 2.2.2/2.3.3, a proč vztah rychlosti čekací animace k vnímanému čekání je konvexní, ne lineární (Ding & Kyung 2025, N≈7000).
- [Kontrast a barva](ux-design/pravidla/kontrast-a-barva.md) – proč 4,5:1 je regulatorní baseline, ne percepční práh (a proč má slabší evidenci než aesthetic-usability effect), WCAG 1.4.11, USWDS magic number, sémantika stavů.
- [Typografie](ux-design/pravidla/typografie.md) – délka řádku 45-75 znaků, WCAG text spacing a resize 200 %, škála jako nástroj konzistence, proč Miller/Cowan neplatí na hierarchii nadpisů.
- [Formuláře a stavy](ux-design/pravidla/formulare-a-stavy.md) – label vs. placeholder, kdy validovat, text chybové hlášky, multi-step a Cowanovo 3-5, prázdné a chybové stavy, proč skeleton screen nemá doloženou oporu.
- [Anti-slop](ux-design/pravidla/anti-slop.md) – markery generického vzhledu s třídou důkazu, včetně naměřeného nálezu, že bezokrajové flat UI stojí uživatele o 22 % víc času (NN/g, Moran 2017).

## Kontext a sektor (proč web pro úřad nevypadá jako web pro zubaře)

Osm sektorů, každý s vlastní tabulkou parametr → hodnota → třída důkazu. Otevři podle klienta,
pro kterého stavíš.

- [Vláda a veřejná správa](ux-design/kontext/vlada.md) – právní mantinely (zákon 99/2019 Sb., Section 508, ADA Title II), konkrétní WCAG prahy, identita provozovatele před vizuálem.
- [Zdravotnictví](ux-design/kontext/zdravotnictvi.md) – vizuál jako prahová zkouška, NHS čitelnost a tón, forenzní rozbor „zaoblené je klikatelnější" folklóru.
- [Finance a fintech](ux-design/kontext/finance.md) – vizuál jako nejsilnější páka kredibility (54,6 % zmínek u Fogg 2002), FCA Consumer Duty, EAA pro banking.
- [Luxury](ux-design/kontext/luxury.md) – nejslabší evidenčně podložený sektor v knihovně, poctivě přiznané.
- [Dev tools a SaaS](ux-design/kontext/dev-tools-saas.md) – proč „Linear look" není evidence, proč nestylované primitivy (Radix) vizuální pravidla záměrně nemají.
- [E-commerce](ux-design/kontext/e-commerce.md) – nejvyšší výchozí nedůvěra ze všech sektorů, jak citovat Baymard bez čísel o konverzi.
- [Děti](ux-design/kontext/deti.md) – tři věková pásma, velikosti písma z testování s dětmi, Children's Code jako privacy rámec.
- [Senioři](ux-design/kontext/seniori.md) – nejtvrdší čísla v knihovně (43 % pomalejší, 45 % problém s taby), řešením je WCAG AA, ne oddělený senior mód.

## Proces

- [Step By Step UX-UI WEB, APP Design](ux-design/proces/step-by-step-ux-ui.md) – celý postup: user flow, wireframy, AIDA, prototyp, usability a A/B testing, iterace.

## Barvy

- [Color Theory](ux-design/color/color-theory.md) – teorie barev, barevné kruhy, schémata.
- [Color Psychology](ux-design/color/color-psychology.md) – psychologie barev a emoce.
- [Color Grading](ux-design/color/color-grading.md) – ladění barev.
- [Pravidlo 60-30-10](ux-design/color/pravidlo-60-30-10.md) – poměr primární/sekundární/akcentní barvy.

## Typografie

- [Typography – základy, anatomie](ux-design/typography/typography-zaklady-anatomie.md) – anatomie písma, základy.
- [Serif a Sans Serif](ux-design/typography/serif-a-sans-serif.md) – kdy patkové vs. bezpatkové.
- [Práce s fontem](ux-design/typography/prace-s-fontem.md) – praktická práce s fonty.
- [Font pairing](ux-design/typography/font-pairing.md) – párování fontů. **[stub]**

## Layout

- [Layout Theory](ux-design/layout/layout-theory.md) – whitespace, margin, padding, rozložení.
- [Grids a Golden ratio](ux-design/layout/grids-a-golden-ratio.md) – mřížky a zlatý řez.

## Web-dev (implementace)

- [HTML a CSS](web-dev/html-a-css.md) – základy HTML a CSS, box model, selektory. Největší nota v sekci.
- [Stylizace textu](web-dev/stylizace-textu.md) – práce s textem v CSS.
- [Inserting CSS](web-dev/inserting-css.md) – způsoby vkládání CSS.
- [Using best images possible](web-dev/using-best-images.md) – volba a příprava obrázků.

## Google Sheets

- [Znalostní báze](sheets/znalostni-baze.md) – rozhodovací rámec otázka→graf, brand tokeny, archetypy reportů, A/B slop→profi, kritéria kvality.
- [NotebookLM destilát](sheets/notebooklm-destilat.md) – surovější výzkumný podklad včetně URL zdrojů.
- [Apps Script vrstva](sheets/apps-script-vrstva.md) – styling přes Apps Script a clasp.

## Příklad hotového design systému

- [Design system DRIVE](ux-design/priklady-ds/design-system-drive.md) – kompletní DS s konkrétními tokeny: paleta s hex kódy, typografická škála, WCAG kontrasty, komponenty (tlačítka, karty, mikrointerakce). Nejrozsáhlejší nota v knihovně, reálná ukázka převedení designu do specifikací.

## Trendy

- [Grafické trendy](ux-design/trendy/graficke-trendy.md) **[stub]** · [Trendy v typografii](ux-design/trendy/trendy-v-typografii.md) **[stub]**

## Další

- [Logo Design](ux-design/logo-foto/logo-design.md) – návrh loga.
- [Photography](ux-design/logo-foto/photography.md) – základy fotografie pro design.

## Destiláty pro moment psaní kódu

Nepatří do knihovny, jsou to imperativy vytažené z toho, co je výše:

- [rules/frontend-ux.md](rules/frontend-ux.md) – path-scoped pravidlo (`.tsx`, `.css`), ke zkopírování do `~/.claude/rules/`.
- [rules/frontend-ux-detailed.md](rules/frontend-ux-detailed.md) – stejné imperativy s odkazy do knihovny.

## Zdroje k učení

- [Kurzy](ux-design/zdroje/kurzy.md) – grafické a UX kurzy.
- [Videa](ux-design/zdroje/videa.md) – UX/UI a barevné tutoriály. **[stub]**
