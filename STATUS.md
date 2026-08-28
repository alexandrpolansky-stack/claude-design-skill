# Stav znalosti a co doplnit

Snímek k 23. 8. 2026 (po retenčním testu a opravách, které z něj vypadly). Účel: aby bylo vidět,
kde je znalost tenká, a nemuselo se to hádat. Když něco doplníš, uprav i tenhle soubor.

## Souhrn

| | |
|---|---|
| Not v knihovně celkem | 92 |
| `neuro-design/` | 1 (master dokument, 5 modulů) |
| `ux-design/` | 53 (31 původních + 13 v `pravidla/` + 9 v `kontext/`) |
| `enterprise-ui/` | 31 (6 `zaklady/` + 15 `vzory/` + 10 `komponenty/`) |
| `web-dev/` | 4 |
| `sheets/` | 3 (znalostní báze, výzkumný destilát, Apps Script vrstva) |
| Pravidel s třídou důkazu (`ux-design/pravidla/`) | ~148 v 13 notách |
| Sektorových pravidel (`ux-design/kontext/`) | ~87 v 9 notách |
| Pravidel s třídou důkazu (`enterprise-ui/`) | ~168 v 30 notách, ~365 blocích ZDROJ |
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

## 0c. Retenční test a co z něj vypadlo (23. 8. 2026)

**Metoda.** Čtyři čisté subagenty, každý dostal jeden reálný úkol, vstupní bod `_index.md` a zákaz
procházet složky. Úkoly: filtrovatelná tabulka uživatelů s hromadnými akcemi, modál pod stickym
headerem s `z-index: 9999`, jednostránková landing page, čtyřkrokový onboarding wizard. Očekávané
výsledky byly zapsané předem, aby se laťka po přečtení odpovědí neposouvala.

**Výsledek retrievalu: 4 ze 4.** Nikdo nesáhl do noty označené **[archiv]**, nikdo neskončil ve
`web-dev/`, opravený rozpor font-pairing versus anti-slop drží. Z-index se trefil na první pokus.
Přidávání dalších not tedy není to, co knihovnu zlepší; nálezitelnost a rozpory bolí víc.

**Šest vad, které audity minuly a test našel:**

| # | Vada | Oprava |
|---|---|---|
| 1 | `neuro-design/` a `sheets/` nebyly v pravidle o vrstvách, přestože index doporučuje neuro-design jako první čtení | `_index.md` má tabulku tří vrstev, která pokrývá všechny sekce, plus varování „ber z něj metodiku, ne čísla" |
| 2 | `SKILL.md` krok 5 posílal na `step-by-step-ux-ui.md`, která nemá konec | Krok 5 nese proces sám, nota má **[neúplné]** a poctivý popis |
| 3 | Živý mezivrstvový rozpor: `neuro-design-master.md` zdůvodňoval shlukování Millerovou sedmičkou, `pravidla/typografie.md` (třída A) to zakazuje | Blok „Jak tuhle notu číst" nahoře v notě plus inline oprava. Výzkum zůstal, override je nad ním |
| 4 | `pravidlo-60-30-10.md` radil akcent „90 % saturace, 90 % jasu", což u primárního CTA vyrábí porušení kontrastu | Override blok se dvěma variantami akcentu. `anti-slop.md` už notu neuvádí jako oporu bez výhrady |
| 5 | 128 zbytků `<mark style="background: #...">` ve 12 notách (minulý úklid řešil jen `#Tag`) | Převedeno na tučné, u nadpisů a dlouhých pasáží odstraněno bez zvýraznění |
| 6 | `formulare-a-stavy.md` si protiřečila (shrnutí „1 až 10 s", pravidlo „2 až 10 s"); práh 5 s versus 10 s proti Carbonu nepojmenovaný; `navigace-v-hierarchii.md` hlásila konflikt u validace, ne u progress indikátoru | Shrnutí srovnáno podle doslovného zdroje (NN/g), oba konflikty pojmenované v místě |

**Popisky v indexu.** Systematická vada: popisovaly téma noty, ne situaci, ve které ji otevřít.
Přepsáno 17 řádků a dva nadpisy sekcí. Konkrétní chyby, které stojí za zapamatování:

- „multi-step a Cowanovo 3-5" vyrábělo přesně to nedorozumění, které nota tři odstavce vyvrací.
- `bezne-akce.md` slibovalo „save", které ve slovníku není.
- `layout-theory.md` slibovalo „padding", který v notě není ani jednou.
- „Otevři, když váháš" u `volba-komponenty.md` se sama vyfiltrovala, agent notu přeskočil, přestože
  `SKILL.md` velí otevřít ji první.
- Slova „onboarding", „wizard" a „z-index" v indexu nebyla vůbec, přestože knihovna k nim materiál má.
- Vzor, jak to má vypadat: `stabilita-layoutu.md` pojmenuje situaci („uživatel přepne filtr"), ne
  komponentu, a agent ji našel, aniž věděl, že takový problém řeší.

**Nová nota.** [Hromadné akce nad filtrovanou a stránkovanou množinou](enterprise-ui/vzory/hromadne-akce.md).
Test ukázal, že na jádro nejběžnější enterprise obrazovky knihovna neodpovídala: co znamená „vybrat
vše" nad 4 812 filtrovanými řádky, co s výběrem při přepnutí stránky, jak potvrdit smazání 200
položek, když pravidlo velí opsat název zdroje a žádný jeden název neexistuje, a jak nahlásit, že
z dávky prošlo 197 z 200. **Většina pravidel je třída C**, protože Carbon tuhle oblast nepokrývá,
a nota to říká na konci sama.

**Mezery, které test pojmenoval a které zůstávají otevřené:**

- ~~Stav filtru, stránky a výběru v URL.~~ **Zavřeno 23. 8. 2026**, viz sekce 0d.
- Oprávnění na úrovni jednotlivého řádku („nemůžu smazat sám sebe", „posledního admina").
- Výchozí počet položek na stránku. Carbon komponentu popisuje, hodnotu nedoporučuje.
- Buňka s identitou člověka (avatar plus jméno plus e-mail), nejčastější buňka seznamu uživatelů.
- Sektor „interní nástroj pro zaměstnance". Osm not v `kontext/` a ani jedna na tenhle případ.
- Struktura landing page: jaké sekce a v jakém pořadí, kolikrát opakovat CTA při scrollu.
- Animace spouštěné scrollem. `pravidla/pohyb.md` je nemá a index to teď říká.
- Onboarding jako samostatný vzor (přeskočení, dokončení později, opuštění uprostřed).
- `inert` se v knihovně nevyskytuje, přestože `prekryvy-a-vrstveni.md` požaduje zneaktivnění obsahu
  pod modálem.

## 0d. Průzkum cizích repozitářů a dvě noty z něj (23. 8. 2026)

**Co se hledalo.** Repozitáře a skilly, které by knihovně něco přidaly. Filtr byl dvojí: tvrdé
pravidlo repa (jen grafika a design) a devět mezer z retenčního testu. Hvězdičky ověřené přímo na
GitHubu, protože agregátory hlásily rozporná čísla (u jednoho repa 59,4k i 79k).

| Repozitář | Licence | Verdikt |
|---|---|---|
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | MIT, 790 hvězd | **Použito jako osnova.** Trefuje tři mezery: stav v URL, dark mode a theming, `inert`. Jsou to holé imperativy bez odůvodnění, takže posloužil jako seznam otázek a odpovědi jsou dohledané v MDN a WCAG |
| [voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md) | MIT repo, ~110k hvězd | **Ne.** Seškrábané hex hodnoty a type ramps od Stripu, Linearu a dalších. Přesně to, co se u Carbonu záměrně nebralo. MIT na repu nedává práva k vizuální identitě těch značek a nota, která učí kopírovat konkrétní značku, jde proti `anti-slop.md` |
| [Meliwat/awesome-ios-design-md](https://github.com/meliwat/awesome-ios-design-md) | 200 iOS DESIGN.md | **Ne.** Totéž plus dotyková doména, kterou má knihovna vědomě zavřenou |
| [anthropics/skills](https://github.com/anthropics/skills), frontend-design | Apache 2.0 | **Ne pro import.** Názor bez citací, neřeší dark mode, tabulky ani kontrastní čísla. Překrývá se s `anti-slop.md` a `vizualni-craft.md`, ale s měkčí oporou |
| [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) | MIT, 79,3k hvězd | **Ne pro import.** Stejný tvar: layout, typografie, motion, spacing bez zdrojů |

**Zobecnění, které stojí za zapamatování.** Po Kowalského `apple-design` (odmítnuto 23. 8. 2026,
viz sekce 0b) je tohle už třetí repo téhož tvaru: populární, dobře napsaný průvodce vkusem bez
jediného zdroje. Ekosystém je jimi zahlcený a sourcing je jediné, čím se tahle knihovna liší.
**Import nezdrojovaného skillu by tu výhodu zahodil.** Kritérium do budoucna: cizí materiál se bere
jen tehdy, když buď nese dohledatelný zdroj, nebo slouží jako seznam otázek, na které si odpovědi
dohledá knihovna sama.

**Dvě nové noty:**

- [Theming a dark mode](ux-design/pravidla/theming-a-dark-mode.md) v `pravidla/`. Zavírá mezeru,
  která byla v STATUS od začátku a kterou dosud pokrývala tři roztroušená pravidla. Sémantická
  vrstva tokenů, čtyři důvody, proč invertování nefunguje, co dělá prohlížeč sám (`color-scheme`),
  proč `prefers-color-scheme: light` nerozliší volbu od mlčení, `light-dark()`, přepínač o třech
  stavech, média, která téma nepřežijí. Mechanismy jsou třída A z MDN, prahy A z WCAG, doporučení C.
- [Stav pohledu v URL](enterprise-ui/vzory/stav-pohledu-v-url.md) ve `vzory/`. Čtvrtá nota v té
  sekci, která platí i mimo produktové aplikace. Zavírá mezeru, kterou si jmenovaly Hromadné akce.
  Tabulka patří/nepatří, proč výběr řádků do adresy nepatří, `pushState` versus `replaceState`,
  tlačítko zpět, sdílitelnost, `scrollRestoration`, neplatná hodnota v adrese.

**Co Vercel guidelines nepokrývají a co tedy zůstává otevřené:** hustota jako parametr, animace
spouštěné scrollem, dataviz palety pro tmavý režim.

### Doplněno tentýž den: univerzální před vendorským

Zadání se upřesnilo na „chceme to víc univerzální, ne zamknuté na jednu věc". To přeskládalo pořadí
kandidátů a je to správný korektiv: **31 z 91 not bylo odvozených z jednoho design systému** a celá
`enterprise-ui/komponenty/` je vázaná na to, jak Carbon skládá komponenty. Retenční test to potvrdil
sám, protože noty, které agenti trefili a použili nejvíc, byly ty mechanismové (překryvy, přetečení,
stabilita layoutu), ne komponentové.

**Kritérium pro další přidávání:** přednost má znalost o tom, jak se chová prohlížeč a člověk, před
znalostí o tom, jak jeden dodavatel skládá komponenty. To první platí všude a nezastará s verzí
design systému.

**Cloudscape (AWS, Apache 2.0, 2,6k hvězd) proto NEIMPORTOVÁN.** Je to poctivý systém pro konzole
a datově husté aplikace, ale wholesale import by ten vendorský zámek utáhl. Použit jen jako druhý
hlas tam, kde nám odporuje, viz níže.

**Nová nota:** [Vynucené barvy](ux-design/pravidla/vynucene-barvy.md). Zavírá mezeru `forced-colors`
a je to přesně ten univerzální typ: mechanismus prohlížeče, třída A z MDN, a hlavně **ruší
mechanismy čtyř jiných pravidel knihovny**. `box-shadow` je vynucen na `none` (padá hloubka
ze stínu), `background-image` na `none` u negradientních hodnot, `color-scheme` na `light dark`
(padá vlastní téma), sémantické barvy stavů splynou. Propojena s `hloubka-a-stiny`,
`stroke-a-hranice`, `kontrast-a-barva` a `theming-a-dark-mode`.

### Rozpor s Cloudscape u výběru řádků (23. 8. 2026)

Nalezen den po dopsání [Hromadných akcí](enterprise-ui/vzory/hromadne-akce.md), takže nota byla
opravena hned.

- **Původní znění, třída C:** výběr při přepnutí stránky a při řazení drž, ruš ho až při změně filtru.
- **Cloudscape, třída B**, verbatim: „Selection is overwritten by: Table sorting, Pagination,
  Preferences, and as soon as they are no longer visible on the page."
  https://cloudscape.design/patterns/resource-management/view/table-view/

**Cloudscape vyhrál** podle vlastního pravidla knihovny o vrstvách: publikovaná konvence systému,
který jede na konzoli AWS, je tvrdší opora než řemeslná úvaha. Nota teď má výchozí chování „zruš při
každé změně pohledu" a držení výběru připouští jen za podmínky, že je vidět souhrn toho, co je
vybráno mimo obrazovku. Obě strany jsou v notě citované, nic se nemazalo.

**Poučení, které stojí za zopakování:** rozpor se našel jen proto, že se hledal druhý zdroj k tématu,
které už bylo „hotové". Nota byla čerstvá a přesto špatně. Vlastní syntéza třídy C je nejrizikovější
druh obsahu v knihovně a stojí za to ji křížově ověřovat dřív než rok poté.


## 0e. Dohledání čtyř design systémů bez URL (28. 8. 2026)

Uzavřený dluh ze sekce 5: [`ux-design/pravidla/tlacitka.md`](ux-design/pravidla/tlacitka.md) citovala
Atlassian, Apple HIG, Fluent 2 a Base Web formulacemi z fáze 1 bez odkazu. Všechny čtyři jsou teď
ověřené přímo v jejich dokumentaci, s URL a doslovným anglickým zněním.

**Tři citace se potvrdily, jedna se rozpadla.**

| Systém | Co se ověřilo |
|---|---|
| Fluent 2 | „Only use one primary button in a layout for the most important action." |
| Apple HIG | „Keep the number of prominent buttons to one or two per view." plus zdůvodnění kognitivní zátěží |
| Atlassian | „Only include one primary button or call to action (CTA) in a page or area." |
| Base Web | „These are to be used sparingly as the sole action of a view.", tedy per view, ne per section |

**Co se nepotvrdilo, a jak to dopadlo.** Anti-pattern „Don't use warning or danger for CTAs that
aren't warning or danger", který podklad fáze 1 připisuje Atlassianu, neexistuje. Ověřeno **dvěma**
nezávislými cestami: na živých stránkách `components/button` ani `components/button/usage` ta věta
není, a doslovnou shodu nenajde ani hledání na webu. Přesně: na `/usage` se slovo „warning" ani
„danger" nevyskytuje vůbec, na `components/button` obě jsou, ale v popisu variant, ne jako zákaz
pro CTA. Neexistuje ta věta, ne ta slova. Třetí pokus, webový archiv, neuspěl ani jako důkaz, ani
jako vyvrácení, viz metodologie níž.

Zajímavější je druhá půlka. **Pravidlo samo Atlassian publikuje, jen na jiné stránce a jinými
slovy.** `foundations/color` definuje sémantické role významem („`warning` Use for UI that
communicates caution to prevent a mistake or error from occurring.", „`danger` Use for UI that
communicates danger or serious error states.") a přidává Do „Use the right color role for your
situation." Zákaz z toho plyne definicí. Pravidlo tedy zůstalo ve třídě B, jen s jiným zdrojem
a s výslovným zákazem citovat tu původní větu.

**Detail, který stojí za zapamatování:** explicitní Don't na té stránce míří opačným směrem („Don't
use an accent when the color has semantic meaning."), tedy zakazuje bezvýznamovou barvu tam, kde
význam patří. Naše pravidlo je jeho zrcadlo, ne jeho citát, a nota to takhle říká. Kdyby se to
nezapsalo, příští čtenář by z Atlassiana odvodil citaci, která tam zase nebude.

Poučení je stejné jako u gridlines: citace bez URL je dluh, ne detail. A přidává se k němu druhé,
konkrétnější: **když se citace nepotvrdí, hledej dál, než pravidlo odepíšeš.** První kolo ověření
vypadalo jako čistý neúspěch a skončilo by degradací pravidla na třídu C. Zdroj byl přitom o jednu
stránku vedle.

**Vedlejší nález, který zaplnil mezeru.** Nota u pravidla o disabled tlačítkách přiznávala, že
konkrétní náhradu žádný zdroj nedává a že je to odvození třídy C. Atlassian ji publikuje přímo („Use
validation or other clear on-screen directions to help people proceed."), takže ta část je teď B.
Apple k destruktivním akcím přidal „Don't assign the primary role to a button that performs
a destructive action, even if that action is the most likely choice."

**Metodologie.** Scrapling, ne WebFetch: vrací syrový markdown, takže se dá citovat doslova, a hlásí
URL po přesměrování. Tři poznatky stály za zmínku. Fluent 2 vrací na neexistující cestu HTTP 200
se soft 404, takže se URL nesmí hádat, správná cesta obsahuje segment `/core/` a dala se vyčíst
z navigačního JSONu v hydratačních propsech té 404 stránky. Apple HIG je bez JavaScriptu prázdná,
ale její obsah leží ve statickém JSONu na `developer.apple.com/tutorials/data/...`, takže prohlížeč
nebyl potřeba. A **archiv se na SPA weby nedá použít**: všech dvacet stažených snímků atlassian.design
obsahuje jen navigaci, protože obsah se dotahoval z `page-data.json`, který se do archivu nedostal.
U webů tohohle typu je archiv slepá ulička, ne záložní plán, a **nesmí se počítat jako důkazní
cesta**: soubor bez těla stránky nemůže dokládat, že v těle stránky něco není. Druhá vada téhož
setu: jen deset z dvaceti snímků je stránka Button, zbytek jsou Button group, Split button
a ikonové varianty, a stránka `/usage`, kde by ta věta nejspíš byla, v archivu není vůbec.
K tomu procesní chyba, kterou stojí za to si přiznat: **stačil jeden snímek, aby to bylo vidět.** První stažený soubor měl 928 znaků textu
a byl to čistý seznam komponent, což je hotová diagnóza. Devatenáct dalších už jen potvrdilo totéž.
Správné pořadí je jedna sonda, kontrola, že v ní vůbec je tělo stránky, a teprve pak rozstřel do
šířky. Je to stejné pravidlo jako u sond do konzole v sekci 0: ověř sondu, než uvěříš jejímu
prázdnému výsledku.

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
Fluent 2, Apple HIG a Atlassian byla v podkladu fáze 1 citovaná bez URL. **Pro
[`ux-design/pravidla/tlacitka.md`](ux-design/pravidla/tlacitka.md) to od 28. 8. 2026 neplatí**
(a pro Carbon v `enterprise-ui/` od 30. 7. 2026), tam jsou URL i doslovné znění dohledané, viz
sekce 0e. Jinde v repu pokyn platí dál, konkrétně v
[`ux-design/kontext/e-commerce.md`](ux-design/kontext/e-commerce.md).

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
- **Design-systémové citace bez URL, částečně vyřešeno 28. 8. 2026.** Fáze 1 citovala Carbon, Base
  Web, Fluent 2, Apple HIG a Atlassian bez odkazu na zdrojovou stránku. Carbon se doplnil 30. 7. 2026
  v `enterprise-ui/`, zbylé čtyři 28. 8. 2026 v [`ux-design/pravidla/tlacitka.md`](ux-design/pravidla/tlacitka.md),
  viz sekce 0e. Jedna citace se přitom rozpadla jako vymyšlená a je opravená na všech třech místech,
  kde v repu žila (`tlacitka.md`, `pravidla/kontrast-a-barva.md`, `kontext/e-commerce.md`).
  **Zbývá:** [`ux-design/kontext/e-commerce.md`](ux-design/kontext/e-commerce.md) cituje Apple HIG,
  Fluent 2, Base Web a Ant Design pořád bez URL, přestože ta URL už dohledaná jsou. Dokud se
  nepropíšou, dvě noty o týchž systémech tvrdí různou míru ověřenosti.
- **Dvě noty o tlačítkách ve dvou sekcích.** `ux-design/pravidla/tlacitka.md` (tvrdá pravidla,
  třídy A) a `enterprise-ui/komponenty/tlacitka-varianty.md` (taxonomie variant a skupin, třída B).
  Dělení je záměrné a obě noty na sebe odkazují s explicitním určením, kdo v konfliktu vyhrává,
  ale je to místo, kde se rada může rozejít. **Když měníš pravidlo o tlačítkách, otevři obě.**
