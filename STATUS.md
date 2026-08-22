# Stav znalosti a co doplnit

Snímek k 23. 8. 2026 (po doplnění tichých selhání layoutu do `enterprise-ui/vzory/`). Účel: aby bylo vidět,
kde je znalost tenká, a nemuselo se to hádat. Když něco doplníš, uprav i tenhle soubor.

## Souhrn

| | |
|---|---|
| Not v knihovně celkem | 88 |
| `neuro-design/` | 1 (master dokument, 5 modulů) |
| `ux-design/` | 51 (31 původních + 11 v `pravidla/` + 9 v `kontext/`) |
| `enterprise-ui/` | 29 (6 `zaklady/` + 13 `vzory/` + 10 `komponenty/`) |
| `web-dev/` | 4 |
| `sheets/` | 3 (znalostní báze, výzkumný destilát, Apps Script vrstva) |
| Pravidel s třídou důkazu (`ux-design/pravidla/`) | ~131 v 11 notách |
| Sektorových pravidel (`ux-design/kontext/`) | ~87 v 9 notách |
| Pravidel s třídou důkazu (`enterprise-ui/`) | 155 v 29 notách, 355 blocích ZDROJ |
| Obrázků v repu | 32 |
| Odkazů na obrázky, které ve zdroji nejsou | 24, všechny v notách označených **[archiv]** (bylo 99) |
| Not pod 120 slov (kostra) | 5, z toho 3 označené **[archiv]** a 2 **[stub]** |
| Not označených **[archiv]** | 8 |

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

### Doplněno 23. 8. 2026: tichá selhání layoutu

Tři noty, které do sekce nepřišly z Carbonu, ale z praxe a ze specifikace, a tvoří spolu jednu
rodinu: **chování, které mlčky neproběhne**. Stylopis projde validací, devtools ukáže spočítanou
hodnotu, a nestane se nic. Symptom přitom vypadá jako jiná chyba, takže se hledá na špatném místě.

| Nota | Co mlčí |
|---|---|
| `vzory/stabilita-layoutu.md` | Automatický layout tabulky se přeměří z právě načtených řádků, takže filtr překreslí celou mřížku |
| `vzory/preteceni-a-truncation.md`, dvě sekce | Zkrácení na nereplacovaném inline boxu se zahodí; položka flexu nebo gridu se bez `min-width: 0` nesmrskne pod obsah |
| `vzory/prekryvy-a-vrstveni.md` | `z-index` neuteče ze stacking contextu, `position: fixed` uvnitř transformovaného předka není vůči viewportu, `sticky` umře pod předkem s `overflow` |

**Proč je tahle rodina cennější než další import.** Evidenčně je to většinou **třída A**, protože
jde o chování dané specifikací, ne o doporučení design systému. Carbon takové věci nepopisuje ze
své podstaty: říká, jak má komponenta vypadat, ne co se stane, když ji někdo napíše. Zdroje jsou
MDN a vlastní praxe, ne druhá ruka.

**Metodická věc, která se osvědčila:** ke každé pasti patří **sonda do konzole**, protože čtení
stylopisu na tyhle chyby nestačí. Vada je v kombinaci předka a potomka, ne v jedné deklaraci.
A ke každé sondě patří ověření sondy: nasadit si vlastní rozbitý případ a zkontrolovat, že ho
najde. Prázdný výsledek z nefunkční sondy je tiché selhání o patro výš.

## 0b. Audit a zatřídění původního importu (23. 8. 2026)

Knihovna byla fakticky dvě knihovny v jednom repu: 49 not s třídou důkazu (`pravidla/`,
`kontext/`, `enterprise-ui/`) a 35 not z původního importu studijních poznámek, bez tříd,
bez nadpisů a z velké části bez příchozích odkazů. Audit prošel obsah všech 35, ne jen jejich
velikost.

**Zavedeny tři vrstvy důvěryhodnosti.** V konfliktu vyhrává vyšší: (1) `pravidla/` a `kontext/`,
(2) `enterprise-ui/`, (3) zbytek `ux-design/` a `web-dev/`. Pravidlo je zapsané v `_index.md`
i v `skills/design-advisor/SKILL.md`, protože skill je místo, kde se rozhoduje.

**Nalezené a opravené rozpory.** Tohle je hlavní důvod, proč audit nebyl kosmetika:

| Kde | Co bylo špatně | Oprava |
|---|---|---|
| `typography/font-pairing.md` | radila „3-4 fonty na design", a **`pravidla/anti-slop.md` na ni odkazovala jako na svůj zdroj** u pravidla „dvě rodiny jsou strop" | Nota přepsána, aby souhlasila. Override blok vysvětluje původní chybu, `anti-slop.md` má upřesněný odkaz |
| `typography/serif-a-sans-serif.md` | „Sans Serif je starší než Serif, byl vytvořen pro počítače" | Faktická chyba, opravena calloutem. Bezpatkové je z 19. století, patkové o staletí starší |
| `typography/prace-s-fontem.md` | podlaha velikosti písma **8 px** | Callout s odkazem na `pravidla/typografie.md` a `kontext/seniori.md`, kde je 16 px podlaha na mobilu |
| `zdroje/kurzy.md` | osobní cesta `C:\Users\...`, což `CLAUDE.md` zakazuje | Odstraněna |

Rozpor u fontů je druhý případ stejného druhu jako gridlines (viz sekce 5), tentokrát horší:
pravidlo se třídou citovalo jako oporu notu, která tvrdila opak.

**Zatříděno, ne smazáno.** Sedm not dostalo značku **[archiv]** a banner přímo v souboru:
`trendy/` obojí (obsah byl jen v chybějících obrázcích), `color/color-grading.md` (postprodukce
videa v Premiere, mimo rozsah), `logo-foto/photography.md` (ovládání fotoaparátu, ne práce
s fotografií v designu), `zdroje/` obojí a `ux-zaklady/ux-experience.md` (osobní zápisky).
Nic se nemazalo: kontrola příchozích odkazů ukázala, že i zdánlivě prázdné noty jsou odkazované
(`graficke-trendy.md` z `anti-slop.md`, `photography.md` z `kontext/gastro.md`), takže mazání by
rozbilo odkazy v evidence-classed notách.

**Doplněno 26 chybějících nadpisů.** Ani jedna nota z původního importu neměla H1 titulek a větu
o tom, k čemu je. Doplněno u všech, spolu s řádkem `Související:`, což zároveň spravilo sirotky.

| | Před | Po |
|---|---|---|
| Not bez příchozího odkazu | 14 | 6, z toho 5 označených **[archiv]** |
| Not bez H1 nadpisu | 26 | 0 |
| Známých rozporů mezi vrstvami | 3 neodhalené | 0 |

**Metodická poznámka, která stojí za zapamatování:** první verze tohohle auditu měla špatná data,
protože hledala příchozí odkazy grepem na zkrácené jméno souboru (`serif-a-sans` nenajde
`serif-a-sans-serif.md`). Podle těch dat vycházelo, že `layout-theory.md` je nepoužívaná, přitom
na ni odkazuje sedm not. **Příchozí odkazy se musí počítat rozpuštěním relativní cesty na skutečný
soubor, ne shodou podřetězců.**

### Druhá část úklidu (23. 8. 2026)

**Mrtvé obrázky vyřešené, z 99 zbylo 24.** Postupováno podle pravidla v `CLAUDE.md`: chybějící
ukázka se nahradí popisem toho, co měla ukázat. Kde text ukázku nepotřeboval, odkaz odešel; kde ji
nesl (slovník anatomie písma), vznikly z popisků skutečné definice. `web-dev/html-a-css.md` přišel
o 16 odkazů a 14 osiřelých titulků typu „Ukázka kódu:", které bez obrázku nic neznamenaly.
**Zbylých 24 je záměrně**: leží v notách označených **[archiv]**, kde banner vysvětluje, že obsah
byl právě v těch obrázcích. Mazat je by ten důkaz zahodilo.

**Tři falešné sliby ve `web-dev/`.** `pravidla/hloubka-a-stiny.md` odkazovala na
`web-dev/html-a-css.md` „pro `box-shadow`", `enterprise-ui/zaklady/2x-grid-a-breakpointy.md`
„pro implementaci CSS gridu" a `pravidla/formulare-a-stavy.md` „pro konkrétní implementaci".
Ověřeno grepem: ta nota má **nula** výskytů `box-shadow`, `grid` i `flexbox`. Všechny tři odkazy
opraveny tak, aby říkaly pravdu, a `html-a-css.md` dostal explicitní rozsah. Mezera je přiznaná,
ne zamaskovaná.

**`rules/` sjednoceno.** Dva destiláty se rozešly (25 shodných řádků, 14 unikátních v krátké
verzi), přesně jak tenhle dokument předpovídal. `frontend-ux-detailed.md` je nově **označený jako
zdroj**, `frontend-ux.md` jako odvozená path-scoped varianta, obojí to má napsané v hlavičce.
Opraven zastaralý ukazatel na neexistující `plugin/skills/design-advisor/references/INDEX.md`
a dva překlepy. Do obou přibyla sekce o implementačních pastech, které mlčky nezaberou.

**Štěp `formulare-a-stavy.md`: rozhodnuto nedělit.** Nota má **přes 50 příchozích odkazů** z asi
dvaceti souborů a řada z nich adresuje konkrétní sekce jménem („sekce Loading stavy", „sekce
Chybové stavy"). Rozdělení by znamenalo přesměrovat všechny a u každého rozhodnout, do které
poloviny patří. Cena a riziko převyšují užitek: nota má nahoře „Rychlý průchod" a jasné `##`
sekce, které odkazy už používají jako kotvy. **Přestává to být otevřený dluh**, je to rozhodnutí.

### Třetí část: zbytky z Obsidian vaultu a kontrola ztráty obsahu (23. 8. 2026)

**Odstraněno 18 inline tagů z vaultu** (`#Research`, `#DivergentníMyšlení`, `#UsabilityTesting`
a podobně), které se mimo Obsidian renderují jako doslovný text a vypadají jako rozbitá syntaxe.
Nahrazeny běžným zvýrazněním. Ponechány čtyři, které tagy nejsou: `#N/A` jako chybová hodnota
tabulky a tři CSS ID selektory v `web-dev/html-a-css.md`.

**Devět vnitřních H1 srovnáno na H2.** Noty z vaultu měly víc nadpisů první úrovně, protože
v Obsidianu titulek nese jméno souboru. Ponechány dvě výjimky, kde druhá úroveň nese vlastní
podstrukturu, a jeden falešný nález: `# Výpočet celkové vizuální váhy prvku` v neuro-designu je
komentář uvnitř Python bloku, ne nadpis.

**Nic se nesmazalo, jen archivovalo.** Po celém úklidu proběhla kontrola ztráty obsahu: pro každý
změněný soubor se porovnal seznam řádků proti verzi v HEAD. Výsledek: **83 zmizelých řádků, všech
83 dohledaných jako záměrná úprava** (opravený odkaz, odstraněný tag, přepsaná věta, sloučený
popisek). Nula neúmyslných ztrát.

**Metodická poznámka podruhé.** První verze té kontroly použila fuzzy porovnání a nahlásila
**91 ztracených řádků v `pravidla/formulare-a-stavy.md`**, tedy v evidence-classed notě. `git diff`
přitom ukázal, že soubor má +3 řádky a jednu změněnou. Byl to falešný poplach kvůli chybě ve
skriptu. **Autoritativní je `git diff --numstat` a porovnání množin řádků, ne podobnostní metrika.**
Je to druhý případ během jednoho dne, kdy vlastní kontrolní skript lhal a málem podle něj vzniklo
špatné rozhodnutí; ten první tvrdil, že `layout-theory.md` nikdo nepoužívá.

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

## 2. Chybějící obrázky (vyřešeno 23. 8. 2026)

Bylo 99 odkazů na obrázky, které nejsou ani v původním vaultu, ani nikde jinde. **Zbývá 24
a všechny jsou záměrné.**

Postup byl podle pravidla v [CLAUDE.md](CLAUDE.md): chybějící ukázka se nahradí popisem toho, co
měla ukázat. V praxi to vyšlo na tři případy:

| Situace | Řešení | Kde |
|---|---|---|
| Text ukázku nepotřeboval, nesl informaci sám | odkaz odstraněn | `layout-theory`, `grids-a-golden-ratio`, `serif-a-sans-serif`, `prace-s-fontem`, `pravidlo-60-30-10`, `logo-design` |
| Obrázek **byl** obsah, popisek u něj byl jen jméno pojmu | z popisků vznikly skutečné definice | `typography-zaklady-anatomie`: TAIL, STEM, EAR, SHOULDER, LOOP, CLOSED COUNTER, LEG, CROSSBAR |
| Screenshoty kódu a výsledků, titulky bez nich nic neznamenaly | odkaz i osiřelý titulek odstraněn, ztráta přiznaná v hlavičce noty | `html-a-css` (16 odkazů, 14 titulků) |

**Zbylých 24 se nechává schválně.** Leží v notách označených **[archiv]** (`trendy/` obojí 20,
`photography` 3, `color-grading` 1), kde banner nahoře vysvětluje, že obsah byl právě v těch
obrázcích. Odstranit je by zahodilo důkaz, proč je nota prázdná.

Kontrola:

```bash
grep -rn "chybějící obrázek" ux-design/ web-dev/   # smí hlásit jen noty s [archiv]
```

## 3. Noty, které jsou zatím kostra

Po zatřídění 23. 8. 2026 zbývají **dvě**. Ostatní z původního seznamu se buď přepsaly, nebo dostaly
značku **[archiv]**, což je odpověď na otázku „co dopsat": nic, nejsou to stavební noty.

| Nota | Slov | Co dopsat |
|---|---|---|
| `web-dev/using-best-images.md` | 80 | Formáty a kdy který, komprese, `srcset` a responzivní obrázky. |
| `web-dev/inserting-css.md` | 81 | Zůstává jako základ; dopsat, proč se v praxi používá externí stylopis. |

Vyřešené z původního seznamu:

| Nota | Jak vyřešeno |
|---|---|
| `typography/font-pairing.md` | **Přepsána.** Původní verze navíc radila 3-4 fonty proti `anti-slop.md`, viz sekce 0b. |
| `zdroje/videa.md`, `ux-zaklady/ux-experience.md` | Označeny **[archiv]**, je to osobní materiál |
| `trendy/` obojí | Označeny **[archiv]**, obsah byl výhradně v chybějících obrázcích |

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

- ~~**Gastro jako sektor v `kontext/`.**~~ **Hotovo 29. 7. 2026**, viz sekce „Gastro sektor" výše.
  Vyřešeno jako jedna nota s osou destinace ↔ sousedská utilita, ne dva sektory.
  Zbytek k dohledání je vypsaný přímo v `ux-design/kontext/gastro.md`.
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

- ~~**Duplicita destilátu.**~~ **Vyřešeno 23. 8. 2026.** Soubory se skutečně rozešly.
  `frontend-ux-detailed.md` je označený jako zdroj, `frontend-ux.md` jako odvozená varianta,
  a obojí to nese v hlavičce s pokynem opravovat obě místa najednou.
- **Konflikt gridlines byl v bázi, ne jen ve skillu.** Znalostní báze Sheets doporučovala gridlines
  skrývat (Tufte, data-ink), ale domácí pravidlo je nechat viditelné. Skill to měl opravené, báze ne.
  Při migraci srovnáno callout blokem a čtyřmi opravami. Poučení: když se opraví skill, opravit i bázi.
- **Jazyk.** Znalost je česky, názvy souborů anglicky/kebab-case. Zatím záměr, ale u nových not to drž,
  ať se to nerozjede.
- ~~**`formulare-a-stavy.md` míchá tři témata v jednom souboru.**~~ **Rozhodnuto 23. 8. 2026
  nedělit.** Přes 50 příchozích odkazů, mnohé adresují konkrétní sekce jménem. Sekce `##` fungují
  jako kotvy a „Rychlý průchod" nahoře notu drží pohromadě. Riziko přesměrování převyšuje užitek
  z dodržení zásady „jedna nota = jedno téma".
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
