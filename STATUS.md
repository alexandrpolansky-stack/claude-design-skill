# Stav znalosti a co doplnit

Snímek k 29. 7. 2026 (v0.2.0, po fázi 2 projektu design-rule-system). Účel: aby bylo vidět,
kde je znalost tenká, a nemuselo se to hádat. Když něco doplníš, uprav i tenhle soubor.

## Souhrn

| | |
|---|---|
| Not v knihovně celkem | 58 |
| `neuro-design/` | 1 (master dokument, 5 modulů) |
| `ux-design/` | 50 (31 původních + 11 v `pravidla/` + 8 v `kontext/`) |
| `web-dev/` | 4 |
| `sheets/` | 3 (znalostní báze, výzkumný destilát, Apps Script vrstva) |
| Pravidel s třídou důkazu (`ux-design/pravidla/`) | ~131 v 11 notách |
| Sektorových pravidel (`ux-design/kontext/`) | ~66 v 8 notách |
| Obrázků v repu | 32 |
| Odkazů na obrázky, které ve zdroji nejsou | 97 (78 ux-design + 17 web-dev + 2 ostatní) |
| Not pod 120 slov (kostra) | 6 |

## 0. Fáze 2: evidence-based pravidla a sektorový kontext (29. 7. 2026)

Osm paralelních agentů (mix Opus/Fable podle náročnosti rozhodování) napsalo `ux-design/pravidla/`
a `ux-design/kontext/` z podkladu fáze 1 (research zdrojů, uložený mimo repo ve vaultu
`Brain/projects/design-rule-system/`). Každé pravidlo nese třídu důkazu A/B/C a explicitní
KDY NEPLATÍ, přesně podle formátu v [CLAUDE.md](CLAUDE.md).

**Opraveno u toho i existující obsah** (stejný princip jako gridlines fix, viz sekce 4):
- `ux-design/zakony-principy/ux-laws.md` – callouty u Fitts, Hick a Miller. Populární verze
  (větší tlačítko = míň chyb, kratší menu = rychlejší rozhodnutí, max 7±2 položek) jsou
  vyvrácené konkrétní citovanou evidencí, teorie zůstala se zpřesněným rozsahem platnosti.
- `ux-design/zakony-principy/efekty.md` – aesthetic-usability effect: jádro (Tractinsky 1997,
  replikace nepřítelem hypotézy) zůstalo jako A, ale „forgiveness" tvrzení (hezký design = lidé
  promíjí chyby) je označené jako nepodložené, s odkazem na tři studie, které jdou proti.

**Nejcennější jednotlivé nálezy:**
- NHS tvrzení „zaoblené rohy jsou klikatelnější" je forenzně vyvrácené (nezdrojovaný commit,
  nula review komentářů, fráze má v celé organizaci nhsuk jediný výskyt). Viz `tvar-a-radius.md`.
- WCAG kontrast 4,5:1 má SLABŠÍ evidenční základ než aesthetic-usability effect, přestože vypadá
  vědečtěji. Viz `kontrast-a-barva.md`, sekce „Ironie".
- Bezokrajové flat UI má měřený náklad: +22 % času, +25 % fixací, úspěšnost 86 %→50 % (NN/g,
  Moran 2017, p<0,005). Viz `anti-slop.md`.
- Vztah rychlosti čekací animace a vnímaného čekání je konvexní, ne lineární (Ding & Kyung 2025,
  6 experimentů, N≈7000). „Rychlejší je vždy lepší" neplatí. Viz `pohyb.md`.
- Skeleton screens nemají žádnou doloženou oporu, jediná kontrolovaná studie je má nejhorší ze
  všech testovaných variant. Viz `formulare-a-stavy.md`.
- Vizuál je u zdravotnictví a malých poskytovatelů bez brandu prahová podmínka, ne diferenciátor
  (Sillence 2004, Robins 2010), zatímco u financí je nejsilnější kredibilitní páka v celém datasetu
  (Fogg 2002: 54,6 % zmínek design look). Viz `kontext/zdravotnictvi.md`, `kontext/finance.md`.

**Otevřené sporné body, ponechané záměrně jako spor, ne uhlazené:**
- Kdy validovat formulářové pole (on blur vs. on submit): GOV.UG a Wroblewski/Baymard si
  protiřečí, kontrolované srovnání napříč populacemi neexistuje. `formulare-a-stavy.md` to
  nechává jako dvě kontextově podmíněná pravidla, ne jako jednu odpověď.
- Elevace: Comeau odvozuje klesající opacitu stínu s rostoucí vzdáleností, Carbon ji drží
  konstantní napříč úrovněmi. Ani jedno není měření, `hloubka-a-stiny.md` to nechává jako volbu.

**Zdroje bez URL, ověřit před externím použitím:** design-systémová data pro Carbon, Base Web,
Fluent 2, Apple HIG a Atlassian byla v podkladu fáze 1 citovaná bez URL. `tlacitka.md` to
zdůvodňuje, ale kdo z toho staví klientský artefakt, ať si formulaci ověří přímo u zdroje.

**Formátová oprava napříč celým repem:** organizační pravidlo zakazuje em-dash bez výjimky.
Devět souborů (včetně `_index.md`, `README.md`, částí `sheets/`) ho obsahovalo z dřívějška,
sjednoceno na en-dash 29. 7. 2026.

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

Hotovo od fáze 2 (29. 7. 2026), zachováno jako historický záznam: Komponenty a stavy (tlačítka),
Formuláře, Prázdné a chybové stavy/loading, Motion. Viz `ux-design/pravidla/`.

Hotovo dodatečně (29. 7. 2026, po testu na dvou artefaktech): **Vizuální craft/art direction**
(klasická vs. expresivní estetika, proč zdrženlivost není nulová osobnost, rozvoj vkusu).
Diagnostikováno jako mezera po testu (viz `pravidla/tlacitka.md` sourozenecké noty pro provedení,
tahle nota řeší směr). Viz `ux-design/pravidla/vizualni-craft.md`. Zdroje jen dvě přečtené eseje
(Hobday, Kowalski) – Rauno Freiberg, Locomotive/Active Theory, Paco Coursey a Jakub Antalík
zůstávají nepřečtené, viz sekce "Co v téhle notě chybí" přímo v notě.

Rozšířeno stejný den (29. 7. 2026 večer): živá analýza 3 nezávisle nominovaných Awwwards webů
(`warmnfuzzy.tv`, `forms.world`, `davidspaeth.com`) přes nově připojený Playwright MCP —
skutečné screenshoty + CSS forenzní analýza, ne popis z paměti. Přidalo pravidlo o typografickém
párování hlasů do `vizualni-craft.md` a novou notu `ux-design/pravidla/portfolio-a-work-grid.md`
(vlajková dlaždice v portfolio gridu, barva celé sekce jako wayfinding). Obojí třída C, n=3,
zdroj je vlastní pozorování, ne publikovaná studie – viz sekce "Tři nezávislé příklady" ve
`vizualni-craft.md`. Metodologický nález k zapamatování: čistě CSS analýza bez renderu minula
reálný detail (zaoblení tlačítek na forms.world), render (screenshot) je nutný, zdroj nestačí.

Zatím není pokryté nic z tohohle, a přitom to v praxi potřebujeme:

- **Gastro jako sektor v `kontext/`, s vysokou prioritou (zadal Alex 29. 7. 2026).** Uvnitř
  jednoho oboru je obrovský rozptyl podle cenové/luxusní úrovně, mnohem větší než u ostatních
  osmi sektorů. Konkrétní příklad od Alexe: luxusní bar (`beyondthebar.cz`) potřebuje jinou
  grafiku než běžná kavárna (`mujsalekkavy.cz`), přestože obě spadají pod "gastro". Než se do
  toho půjde, rozmyslet, jestli je to jeden sektor s vnitřním rozpětím luxury↔casual (podobně
  jako obecný luxury sektor už rozpětí řeší), nebo dva samostatné sektory. Zatím NEDĚLAT žádný
  research, jen si tenhle úkol nezapomenout otevřít, až Alex řekne.
- **Přístupnost do hloubky nad rámec kontrastu a velikosti cíle.** WCAG kontrast (4,5:1, 3:1)
  a velikost cíle (24×24 px) jsou teď v `pravidla/kontrast-a-barva.md` a `pravidla/tlacitka.md`
  pořádně podložené. Pořád ale chybí klávesová navigace, screen readery, ARIA vzory, focus
  management napříč komponentami (ne jen focus ring na tlačítku).
- **Design tokens a design systémy jako proces.** Je hotový příklad (`priklady-ds/`) a teď i
  konkrétní škály (`pravidla/tvar-a-radius.md` má Material 3 radius škálu), ale ne obecný postup,
  jak si vlastní systém tokenů postavit, pojmenovat a udržovat.
- **Dataviz mimo Sheets.** Volba grafu, palety pro data, přesnost vnímání. Tohle
  je teď jen v `sheets/znalostni-baze.md`, přitom platí obecně -
  kandidát na vytažení do `design-advisor`.
- **Komponenty mimo tlačítka.** Karty, navigace, tabulky, modály. `pravidla/hloubka-a-stiny.md`
  a `pravidla/stroke-a-hranice.md` řeší jejich vizuální oddělení, ale ne rozhodovací pravidla
  specifická pro danou komponentu (kdy je karta klikatelná celá vs. jen CTA uvnitř, apod.).
- **Landing pages a propagace jako struktura stránky.** Struktura, hero, sociální důkaz, CTA
  hierarchie napříč sekcemi. Teď je k tomu jen AIDA v `proces/step-by-step-ux-ui.md`.
- **Responzivita a mobil jako layout strategie.** Touch target 24×24 px je pokrytý (WCAG 2.5.8),
  ale breakpointy, layout shifty mezi velikostmi a palec zóna na mobilu ne.
- **Brand tokeny mimo Sheets.** Paleta a font jsou zapsané jen v `sheets/`. Pro weby,
  komponenty, propagaci a e-maily neexistuje sdílený zdroj tokenů.

## 4. Dluhy ve struktuře

- **Duplicita destilátu.** `rules/frontend-ux.md` a `rules/frontend-ux-detailed.md` mají
  stejný obsah ve dvou souborech. Rozejdou se. Chce to jeden zdroj a druhý generovat, nebo jeden zrušit.
- **Konflikt gridlines byl v bázi, ne jen ve skillu.** Znalostní báze Sheets doporučovala gridlines
  skrývat (Tufte, data-ink), ale domácí pravidlo je nechat viditelné. Skill to měl opravené, báze ne.
  Při migraci srovnáno callout blokem a čtyřmi opravami. Poučení: když se opraví skill, opravit i bázi.
- **Jazyk.** Znalost je česky, názvy souborů anglicky/kebab-case. Zatím záměr, ale u nových not to drž,
  ať se to nerozjede.
- **`formulare-a-stavy.md` míchá tři témata v jednom souboru** (formuláře, prázdné/chybové stavy,
  loading), proti zásadě „jedna nota = jedno téma" z `CLAUDE.md`. Zatím drží pohromadě díky sekci
  Rychlý průchod nahoře. Přirozený štěp při dalším růstu: `formulare-a-validace.md` +
  `stavy-rozhrani.md`.
- **Design-systémové citace bez URL.** Fáze 1 cituje Carbon, Base Web, Fluent 2, Apple HIG
  a Atlassian formulacemi bez odkazu na zdrojovou stránku. `pravidla/tlacitka.md` to přiznává,
  ale kdo z těch pravidel staví klientský artefakt, ať si formulaci dohledá a ověří přímo.
