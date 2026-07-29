# Stav znalosti a co doplnit

Snímek při zakládání repa (v0.1.0). Účel: aby bylo vidět, kde je znalost tenká, a nemuselo se to
hádat. Když něco doplníš, uprav i tenhle soubor.

## Souhrn

| | |
|---|---|
| Not v knihovně celkem | 39 (~31 000 slov) |
| `neuro-design/` | 1 (master dokument, 5 modulů) |
| `ux-design/` | 31 |
| `web-dev/` | 4 |
| `sheets/` | 3 (znalostní báze, výzkumný destilát, Apps Script vrstva) |
| Obrázků v repu | 32 |
| Odkazů na obrázky, které ve zdroji nejsou | 97 (78 ux-design + 17 web-dev + 2 ostatní) |
| Not pod 120 slov (kostra) | 6 |

## 1. Chybějící obrázky (největší mezera)

97 odkazů v textu ukazuje na obrázky, které nejsou ani v původním vaultu, ani nikde jinde:
zůstala po nich jen prázdná místa. V textu jsou označené jako `*[chybějící obrázek: nazev.png]*`,
takže se dají najít grepem:

```bash
grep -rn "chybějící obrázek" ux-design/ web-dev/
```

Nejvíc zasažené noty (obrázek tam nesl podstatnou část informace, takže text sám nedává smysl):

| Nota | Chybí | Dopad |
|---|---|---|
| `ux-design/typography/typography-zaklady-anatomie.md` | 11 | Anatomie písma se bez obrázku nevysvětlí. |
| `ux-design/layout/layout-theory.md` | 11 | Whitespace/margin/padding jsou popsané jako komentář k obrázkům. |
| `ux-design/layout/grids-a-golden-ratio.md` | 11 | Totéž, mřížky bez ukázky. |
| `ux-design/trendy/graficke-trendy.md` | 10 | Nota je skoro jen galerie, bez obrázků prakticky prázdná. |
| `ux-design/trendy/trendy-v-typografii.md` | 10 | Totéž. |
| `ux-design/typography/serif-a-sans-serif.md` | 7 | Srovnání řezů. |
| `ux-design/color/pravidlo-60-30-10.md`, `ux-design/typography/prace-s-fontem.md`, `ux-design/logo-foto/logo-design.md` | 4 každá | Ukázky poměrů a variant. |
| `ux-design/logo-foto/photography.md` | 3 | |
| `ux-design/ux-zaklady/content-strategy-ux-writing.md`, `ux-design/typography/font-pairing.md` | 1 každá | |
| `web-dev/html-a-css.md` | 14 | Box model, selektory a layout jsou vysvětlené na screenshotech. |
| `web-dev/inserting-css.md`, `web-dev/using-best-images.md` | 3 dohromady | |

Možnosti nápravy, od nejlevnější: **(a)** obrázek nahradit textovým popisem toho, co ukazoval
(u typografie často stačí), **(b)** vyrobit vlastní ukázku, **(c)** odkaz smazat a odstavec
přepsat, aby stál sám. U trendových not zvážit, jestli je vůbec držet.

## 2. Noty, které jsou zatím kostra

| Nota | Slov | Co dopsat |
|---|---|---|
| `ux-design/zdroje/videa.md` | 30 | Doplnit seznam, nebo sloučit do `zdroje/kurzy.md`. |
| `ux-design/trendy/trendy-v-typografii.md` | 56 | Celé; závislé i na chybějících obrázcích. |
| `ux-design/ux-zaklady/ux-experience.md` | 57 | Definice UX a složky zážitku. Překrývá se s `general-ux-knowledge.md`, možná sloučit. |
| `ux-design/trendy/graficke-trendy.md` | 67 | Celé; viz výše. |
| `ux-design/typography/font-pairing.md` | 94 | Konkrétní ověřené páry + pravidlo, proč fungují. |

## 3. Témata, která v bázi úplně chybí

Zatím není pokryté nic z tohohle, a přitom to v praxi potřebujeme:

- **Přístupnost do hloubky.** WCAG kontrast je zmíněný jako číslo, ale chybí klávesová navigace,
  screen readery, ARIA, focus management, formulářové chyby.
- **Design tokens a design systémy jako proces.** Je hotový příklad (`priklady-ds/`), ale ne
  postup, jak systém postavit, pojmenovat tokeny a udržovat.
- **Dataviz mimo Sheets.** Volba grafu, palety pro data, přesnost vnímání. Tohle
  je teď jen v `sheets-design/references/znalostni-baze.md`, přitom platí obecně -
  kandidát na vytažení do `design-advisor`.
- **Komponenty a stavy.** Tlačítka (varianty, hierarchie, velikosti), karty, navigace,
  hover/active/disabled/loading stavy. Přitom tlačítko je nejčastější věc, co se staví.
- **Landing pages a propagace.** Struktura stránky, hero, sociální důkaz, CTA hierarchie.
  Teď je k tomu jen AIDA v `proces/step-by-step-ux-ui.md`.
- **Formuláře.** Validace, chybové stavy, multi-step, label vs placeholder.
- **Prázdné a chybové stavy, loading.** Co uživatel vidí, když nejsou data.
- **Responzivita a mobil.** Breakpointy, touch targety, palec zóna.
- **Motion.** Kdy animovat, trvání, easing, `prefers-reduced-motion`.
- **Brand tokeny mimo Sheets.** Paleta a font jsou zapsané jen v `sheets-design`. Pro weby,
  komponenty, propagaci a e-maily neexistuje sdílený zdroj tokenů.

## 4. Dluhy ve struktuře

- **Duplicita destilátu.** `rules/frontend-ux.md` a `rules/frontend-ux-detailed.md` mají
  stejný obsah ve dvou souborech. Rozejdou se. Chce to jeden zdroj a druhý generovat, nebo jeden zrušit.
- **Konflikt gridlines byl v bázi, ne jen ve skillu.** Znalostní báze Sheets doporučovala gridlines
  skrývat (Tufte, data-ink), ale domácí pravidlo je nechat viditelné. Skill to měl opravené, báze ne.
  Při migraci srovnáno callout blokem a čtyřmi opravami. Poučení: když se opraví skill, opravit i bázi.
- **Jazyk.** Znalost je česky, názvy souborů anglicky/kebab-case. Zatím záměr, ale u nových not to drž,
  ať se to nerozjede.
