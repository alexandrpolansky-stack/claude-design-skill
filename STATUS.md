# Stav znalosti a co doplnit

Snímek k 30. 7. 2026 (po importu principů z IBM Carbonu do `enterprise-ui/`). Účel: aby bylo vidět,
kde je znalost tenká, a nemuselo se to hádat. Když něco doplníš, uprav i tenhle soubor.

## Souhrn

| | |
|---|---|
| Not v knihovně celkem | 86 |
| `neuro-design/` | 1 (master dokument, 5 modulů) |
| `ux-design/` | 51 (31 původních + 11 v `pravidla/` + 9 v `kontext/`) |
| `enterprise-ui/` | 27 (6 `zaklady/` + 11 `vzory/` + 10 `komponenty/`) |
| `web-dev/` | 4 |
| `sheets/` | 3 (znalostní báze, výzkumný destilát, Apps Script vrstva) |
| Pravidel s třídou důkazu (`ux-design/pravidla/`) | ~131 v 11 notách |
| Sektorových pravidel (`ux-design/kontext/`) | ~87 v 9 notách |
| Pravidel s třídou důkazu (`enterprise-ui/`) | 144 v 27 notách, 347 blocích ZDROJ |
| Obrázků v repu | 32 |
| Odkazů na obrázky, které ve zdroji nejsou | 97 (78 ux-design + 17 web-dev + 2 ostatní) |
| Not pod 120 slov (kostra) | 6 |

## 0. Enterprise UI z IBM Carbonu (30. 7. 2026)

Nová sekce `enterprise-ui/`, 27 not, 144 pravidel se třídou důkazu. Zdroj: lokální kopie
dokumentace IBM Carbon Design System (stránky `usage` a `accessibility`, čteno 30. 7. 2026).
Účel sekce: dosud v knihovně nebyla znalost o tom, jak stavět **produktovou aplikaci** (dashboard,
CRUD, administrace), jen o vizuální stránce webu.

**Co se přebralo a co ne.** Zadání bylo explicitní: principy a vzory, ne design. Nepřebrané
záměrně: Carbon tokeny, hex hodnoty, IBM Plex, elevation škály, ikonová knihovna, vizuály „AI
presence". Odůvodnění je napsané přímo v [`enterprise-ui/zaklady/vrstvy-a-vzory.md`](enterprise-ui/zaklady/vrstvy-a-vzory.md):
kdo zkopíruje tokeny, postaví produkt, který vypadá jako IBM, a to není cíl. Každý blok ZDROJ
nese verbatim anglický citát z Carbonu plus URL, aby se za rok dalo poznat, co je Carbonovo
tvrzení a co moje syntéza (ta je označená třídou **C**).

**Doložené rozpory s knihovnou, ponechané jako rozpory** (stejný princip jako gridlines fix,
sekce 5). V každém případě vyhrává knihovna, protože má tvrdší zdroje, a nota to říká v místě:

| Téma | Carbon | Knihovna | Kdo vyhrává |
|---|---|---|---|
| Placeholder | mírnější postoj | zakazuje úplně (GOV.UK, WCAG 1.4.3) | knihovna |
| Načasování validace | on blur | on submit (GOV.UK) | knihovna jako výchozí, Carbon legitimní u enterprise s vlastním výzkumem |
| Značení povinných polí | označ menšinu | označ nepovinná (GOV.UK) | tentýž princip „označ menšinu", jen na jiný typ formuláře |
| Skeleton screens | doporučuje, odvolává se na NN/g | Viget 2017 (N=136) je proti | knihovna, a navíc: Carbonova citace míří na článek o indikátorech obecně, ne na srovnání skeleton vs. spinner. **Carbonovo tvrzení nepodpírá jeho vlastní zdroj** |
| „Please" ve zprávách | povoluje při obtěžování uživatele | zakazuje v chybových hláškách (GOV.UK) | striktnější pravidlo u chyb |

Navíc zdokumentovaná **nekonzistence uvnitř Carbonu**: u stavových indikátorů říká vizuální
sekce „aspoň tři ze čtyř prvků", přístupnostní sekce „aspoň dva z barvy/tvaru/symbolu". Ani jedno
není podané jako přesné, v notě je bezpečné čtení.

**Uzavřené mezery ze sekce 4:** přístupnost do hloubky (klávesová navigace, čtečky, ARIA vzory,
focus management), komponenty mimo tlačítka (včetně původní otázky „kdy je karta klikatelná celá
vs. jen CTA uvnitř"), breakpointy a responzivní layout. Částečně uzavřený dluh
„design-systémové citace bez URL" ze sekce 5: Carbon je teď citovaný konkrétními URL, Base Web,
Fluent 2, Apple HIG a Atlassian pořád ne.

## 1. Fáze 2: evidence-based pravidla a sektorový kontext (29. 7. 2026)

Osm paralelních agentů (mix Opus/Fable podle náročnosti rozhodování) napsalo `ux-design/pravidla/`
a `ux-design/kontext/` z podkladu fáze 1 (research zdrojů, uložený mimo repo ve vaultu
`Brain/projects/design-rule-system/`). Každé pravidlo nese třídu důkazu A/B/C a explicitní
KDY NEPLATÍ, přesně podle formátu v [CLAUDE.md](CLAUDE.md).

**Opraveno u toho i existující obsah** (stejný princip jako gridlines fix, viz sekce 5):
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

## 2. Chybějící obrázky (největší mezera)

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

## 3. Noty, které jsou zatím kostra

| Nota | Slov | Co dopsat |
|---|---|---|
| `ux-design/zdroje/videa.md` | 30 | Doplnit seznam, nebo sloučit do `zdroje/kurzy.md`. |
| `ux-design/trendy/trendy-v-typografii.md` | 56 | Celé; závislé i na chybějících obrázcích. |
| `ux-design/ux-zaklady/ux-experience.md` | 57 | Definice UX a složky zážitku. Překrývá se s `general-ux-knowledge.md`, možná sloučit. |
| `ux-design/trendy/graficke-trendy.md` | 67 | Celé; viz výše. |
| `ux-design/typography/font-pairing.md` | 94 | Konkrétní ověřené páry + pravidlo, proč fungují. |

## 4. Témata, která v bázi úplně chybí

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

## Gastro sektor (29. 7. 2026, tentýž den)

Nový `ux-design/kontext/gastro.md`, jedna nota s osou destinace ↔ sousedská utilita (ne dvě
noty — regulace je na celé ose stejná, duplikace by časem rozjela, viz precedens gridlines).
21 pravidel (rozšířeno z 17, viz níže), evidenčně nejhutnější nota v `kontext/`: regulace ověřená
proti primárním textům (nařízení 1169/2011 na alergeny, EAA mikropodnik-výjimka), menu-design
výzkum (Yang 2012 eye-tracking vyvrací zlatý trojúhelník, Ip & Chark 2023 metaanalýza dává
diskontní faktor na laboratorní nálezy). Během researche odhaleny a zdokumentovány **dvě
fabrikované citace** kolující v SEO obsahu (Parsa & Njite 2014, Yue/Tong/Prinyawiwatkul 2019)
a jedno chybné přiřazení (Di Geronimo CHI 2020 dark patterns, korpus neobsahoval food/delivery
kategorii). **EAA mikropodnik-výjimka warning doplněn i do `e-commerce.md`**, křížový odkaz oběma
směry.

**Rozšíření (29. 7. 2026, po usage limit restartu):** doplňkový sub-agent dokončil research na
formát ceny v menu, který zbyl rozpracovaný. Čtyři nová pravidla: skrytí ceny snižuje vnímanou
kvalitu/hodnotu (Kim et al. 2021, proti intuici), odstranění $ symbolu samo o sobě útratu
nezvedne (Yang/Kimes/Sessarego 2009 přečten plný text — populární "+8 %" je zavádějící
zjednodušení, reálný signifikantní efekt +3,70 USD nese JAKÝKOLIV peněžní odkaz, ne symbol $),
zaokrouhlení vs. .99 má malý efekt na nákup a nulový na vnímanou kvalitu (Troll et al. 2024
preregistrovaná metaanalýza, g=0,00 na kvalitu), ceník na webu není zákonná povinnost ale NSS
judikát řekl, že "jen web" nestačí v provozovně. Plus tabulka "Co NENÍ" rozšířená o další dvě
nepodložená kolující tvrzení a warning o Wansinkových retrakcích.

Zbývá k dohledání (sekce "Neověřené a k dohledání" v notě): Naipaul & Parsa (2001) a Parsa & Njite
(2004) metodika (paywall), Ip & Chark (2023) abstrakt (Elsevier 403, bibliografie ověřená),
verbatim znění zákona 40/1995 Sb. o reklamě na alkohol, prevalence PDF/obrázkových menu na
českých webech (navržen levný vlastní audit 30-50 podniků).

Seznam, který v praxi potřebujeme. Přeškrtnuté položky jsou hotové, u každé je napsané, čím
a co z ní zbývá:

- **Gastro jako sektor v `kontext/`, s vysokou prioritou (zadal Alex 29. 7. 2026).** Uvnitř
  jednoho oboru je obrovský rozptyl podle cenové/luxusní úrovně, mnohem větší než u ostatních
  osmi sektorů. Konkrétní příklad od Alexe: luxusní bar (`beyondthebar.cz`) potřebuje jinou
  grafiku než běžná kavárna (`mujsalekkavy.cz`), přestože obě spadají pod "gastro". Než se do
  toho půjde, rozmyslet, jestli je to jeden sektor s vnitřním rozpětím luxury↔casual (podobně
  jako obecný luxury sektor už rozpětí řeší), nebo dva samostatné sektory. Zatím NEDĚLAT žádný
  research, jen si tenhle úkol nezapomenout otevřít, až Alex řekne.
- ~~**Přístupnost do hloubky nad rámec kontrastu a velikosti cíle.**~~ **Hotovo 30. 7. 2026.**
  Klávesová navigace a focus management napříč komponentami v
  `enterprise-ui/zaklady/klavesnice-a-focus.md`, čtečky a ARIA vzory (live regiony, role, vystavení
  stavu a hodnoty) v `enterprise-ui/zaklady/oznameni-pro-ctecky.md`, plus přístupnostní sekce
  v každé komponentní notě. Zbývá: nic k WCAG 2.2 jako celku (knihovna cituje jednotlivá kritéria,
  ne úplný checklist) a nic k testování s asistivní technologií.
- **Design tokens a design systémy jako proces.** Je hotový příklad (`priklady-ds/`) a teď i
  konkrétní škály (`pravidla/tvar-a-radius.md` má Material 3 radius škálu), ale ne obecný postup,
  jak si vlastní systém tokenů postavit, pojmenovat a udržovat.
- **Dataviz mimo Sheets.** Volba grafu, palety pro data, přesnost vnímání. Tohle
  je teď jen v `sheets/znalostni-baze.md`, přitom platí obecně -
  kandidát na vytažení do `design-advisor`.
- ~~**Komponenty mimo tlačítka.**~~ **Hotovo 30. 7. 2026.** `enterprise-ui/komponenty/` má deset not
  (tabulky, výběr ze seznamu, textová pole, taby, dlaždice a karty, tagy, stránkování, tooltip
  a toggletip, varianty tlačítek, drobenka a indikátor postupu) a `enterprise-ui/vzory/` jedenáct
  vzorů. Původní otázka „kdy je karta klikatelná celá vs. jen CTA uvnitř" je odpovězená
  v `enterprise-ui/komponenty/dlazdice-a-karty.md`: nejsou to dva režimy, jsou to vzájemně se
  vylučující varianty. Zbývá: menu buttons, toolbar, primární a globální navigace, tearsheet,
  file uploader, date picker, slider.
- **Landing pages a propagace jako struktura stránky.** Struktura, hero, sociální důkaz, CTA
  hierarchie napříč sekcemi. Teď je k tomu jen AIDA v `proces/step-by-step-ux-ui.md`.
- **Responzivita a mobil jako layout strategie.** Breakpointy a chování layoutu mezi velikostmi
  jsou od 30. 7. 2026 v `enterprise-ui/zaklady/2x-grid-a-breakpointy.md` (pět breakpointů, fluid
  vs. fixed, gutter módy, chování panelů) a responzivní chování jednotlivých komponent je v každé
  komponentní notě. **Zbývá mobil jako samostatná strategie:** palec zóna, dotykové gesta,
  mobilní navigační vzory. Carbon je enterprise desktop-first, tohle v něm není.
- **Brand tokeny mimo Sheets.** Paleta a font jsou zapsané jen v `sheets/`. Pro weby,
  komponenty, propagaci a e-maily neexistuje sdílený zdroj tokenů.

## 5. Dluhy ve struktuře

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
- **Design-systémové citace bez URL, částečně vyřešeno 30. 7. 2026.** Fáze 1 cituje Carbon, Base
  Web, Fluent 2, Apple HIG a Atlassian formulacemi bez odkazu na zdrojovou stránku.
  `pravidla/tlacitka.md` to přiznává. **Carbon je od 30. 7. 2026 citovaný konkrétními URL
  a verbatim citáty v `enterprise-ui/`**, takže u něj se dá tvrzení dohledat. Base Web, Fluent 2,
  Apple HIG a Atlassian pořád ne: kdo z těch pravidel staví klientský artefakt, ať si formulaci
  dohledá a ověří přímo.
- **Dvě noty o tlačítkách ve dvou sekcích.** `ux-design/pravidla/tlacitka.md` (tvrdá pravidla,
  třídy A) a `enterprise-ui/komponenty/tlacitka-varianty.md` (taxonomie variant a skupin, třída B).
  Dělení je záměrné a obě noty na sebe odkazují s explicitním určením, kdo v konfliktu vyhrává,
  ale je to místo, kde se rada může rozejít. **Když měníš pravidlo o tlačítkách, otevři obě.**
