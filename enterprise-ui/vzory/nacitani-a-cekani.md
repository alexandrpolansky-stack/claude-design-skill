# Načítání a čekání

Který indikátor při jakém čekání, a kde se Carbon rozchází s doloženou evidencí v téhle knihovně.

**Přečti si nejdřív** [Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md), sekce
Loading stavy. Tam jsou prahy čekání (0,1 / 1 / 10 s), pravidlo o krokování progress baru
(peer-reviewed, třída A) a **doložený nález proti skeleton screenům**. Tahle nota přidává Carbonovu
typologii komponent a přiznává, kde Carbon tvrdí opak.

Související: [Prázdné stavy](prazdne-stavy.md) · [Dialogy a panely](dialogy-a-panely.md) ·
[Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md)

---

## Rychlé rozhodnutí

1. Pod 1 s: nic. Pod 3 s podle Carbonu taky nic (viz níže).
2. Jeden prvek nebo tlačítko: **inline loading**, tlačítko disabled po dobu běhu.
3. Celá stránka nebo sekce: **loading indikátor s overlayem**, obsah nedostupný.
4. Postup lze vyčíslit: **determinovaný progress bar**.
5. Postup vyčíslit nelze, ale běží dlouho: **nedeterminovaný progress bar**.
6. Uživatel musí mezi kroky zasáhnout: **progress indicator**, ne progress bar.
7. První načtení obsahu se známým tvarem: skeleton. **Ale pozor, viz spor níže.**
8. Nad pár minut: přidej notifikaci, nespoléhej na indikátor.
9. Nikdy neběž víc indikátorů zároveň.
10. Konec načítání musí být oznámený i čtečce, ne jen zmizením spinneru.

---

## Spor o skeleton screeny: knihovna versus Carbon

**Carbon tvrdí**, že skeleton stavy a další načítací indikátory zvyšují uživatelskou spokojenost,
a odkazuje na NN/g. Verbatim: „According to research conducted by the Nielsen Norman Group, skeleton
states and other loading indicators improve user satisfaction."
Zdroj: https://carbondesignsystem.com/patterns/loading-pattern/, odkazuje na
https://www.nngroup.com/articles/progress-indicators/

**Knihovna má proti tomu doložený nález.** Jediná dohledaná kontrolovaná studie, která skeleton
srovnává se spinnerem a s prázdnou obrazovkou při **stejné délce čekání**, má skeleton nejhorší ve
všech měřených metrikách (Viget 2017, N = 136). Detail včetně čísel je ve
[formulářích a stavech](../../ux-design/pravidla/formulare-a-stavy.md).

**Jak to rozhodnout:** platí pravidlo knihovny. Skeleton používej, když chceš předem sdělit tvar
obsahu a layout je stabilní, ne s odůvodněním, že je prokazatelně rychlejší. Carbonův odkaz na NN/g
míří na článek o **progress indikátorech obecně**, ne na srovnání skeletonu se spinnerem, takže jeho
tvrzení o skeletonech tou citací není doložené. To je moje ověření Carbonovy citace, ne Carbonovo
tvrzení.

**Carbonova pravidla o skeletonech, která platí bez ohledu na ten spor** (jsou to konstrukční
omezení, ne tvrzení o rychlosti):

- Skeleton dávej **jen** na kontejnerové komponenty (dlaždice, structured list) nebo datové
  komponenty (tabulky, karty).
- Akční komponenty (tlačítka, vstupy, checkboxy, toggly) skeleton ve většině případů **nepotřebují**.
- **Nikdy** nezobrazuj jako skeleton: toasty, overflow menu, položky dropdownu, modaly, loadery.
  Prvky **uvnitř** modalu skeleton mít mohou, modal sám ne.
- Skeleton má být na obrazovce jen několik sekund a zmizí, jak se komponenty a obsah naplní.

**ZDROJ:** Carbon, Loading pattern, Skeleton states, verbatim: „Never represent toast notifications,
overflow menus, dropdown items, modals, and loaders with skeleton states. Elements inside a modal may
have a skeleton state, but the modal itself should not."
https://carbondesignsystem.com/patterns/loading-pattern/

**A jedno pravidlo z knihovny navíc:** skeleton nesmí po načtení přeskládat layout. Stejné rozměry,
stejný počet prvků. Viz [formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).

## Loading indikátor (spinner)

**Co to je:** signalizuje, že akce běží. **Na rozdíl od progress baru nenese žádnou informaci
o postupu.** Když proces zabere víc než chvilku, použij progress indikátor.

**Kdy použít podle Carbonu:**

| Situace | Detail |
|---|---|
| Akce dočasně vyřadí aplikaci | Použij indikátor **plus celoobrazovkový overlay** |
| Zpracování zabere víc než pár sekund | Když načítání vyžaduje plné prostředky aplikace a potrvá delší než chvilku, celoobrazovkový indikátor |
| Ukládají se nebo odesílají data od uživatele | Indikátor dá aplikaci dokončit zpracování, než uživatel pokračuje |

**Carbonův práh:** „Use a loading indicator if the expected wait time exceeds three seconds."
Zdroj: https://carbondesignsystem.com/components/loading/usage/

**Poznámka k rozporu:** knihovna má práh 1 s pro první zpětnou vazbu a 2 až 10 s pro smyčkovanou
animaci, s citací Nielsena a NN/g (viz [formuláře a
stavy](../../ux-design/pravidla/formulare-a-stavy.md)). Carbonovy 3 s jsou uvnitř toho rozmezí, takže
to není protiklad, jen konkrétnější volba. Pro pravidlo „pod 1 s nic" platí knihovna.

**Kdy loading indikátor nepoužít podle Carbonu:**

- Na postupné zobrazování obsahu (tam skeleton).
- Když je k pokračování potřeba interakce uživatele (tam tooltip, progress indicator, notifikace).
- U celoobrazovkových načtení Carbon **preferuje skeleton** před indikátorem.
- Nikdy neběž víc indikátorů zároveň, přehltí to uživatele.

**Dvě velikosti a jejich role:**

| Velikost | Kde |
|---|---|
| Velký (výchozí) | Celoobrazovkové převzetí, sekce stránky, modaly, jednotlivé dlaždice. Typicky **s overlayem**, aby uživatel nemohl interagovat s načítanými prvky |
| Malý | Kontextové a lokalizované načítání uvnitř konkrétního prvku, typicky inline. Bez overlayů, umísti do nebo vedle spouštěcího prvku |

**Umístění:** celoobrazovkově doprostřed viewportu s poloprůhledným overlayem. V komponentě
(modal, dlaždice, panel) doprostřed toho prostoru, taky s overlayem.

**Text:** volitelný. U velkého indikátoru Carbon doporučuje krátkou stavovou zprávu pod ním
(„Loading data..."), ale poznamenává, že label v komponentě defaultně není.

**ZDROJ:** Carbon, Loading usage. https://carbondesignsystem.com/components/loading/usage/

## Inline loading

**Kdy:** akce, která nejde provést okamžitě a zabere krátkou chvíli. Nebo když se načítá nebo
obnovuje malé množství dat (typicky stav). Carbon jmenuje typické akce: create, update, delete
s významnějším zpracováním dat. Umístění: v tabulce, po kliknutí na tlačítko, v modalu.

**Kdy ne:** celostránkové načtení (tam skeleton). A **nikdy nespouštěj inline loading na víc
položkách nebo akcích zároveň**, kromě prvního načtení nebo obnovení stránky.

**Čtyři stavy a co s labelem:**

| Stav | Label |
|---|---|
| Inactive | Bez vizuálního indikátoru |
| Active | Popisuje probíhající akci („Ukládám...") |
| Finished | **Musí se změnit** („Uloženo"). Úspěšný stav je aktivní 1,5 s, pak se volá `onSuccess` |
| Error | Musí se změnit na informaci o chybě nebo selhání. Komponenta zneaktivní a **musí přijít inline notifikace nebo obsluha chyby ve formuláři** |

**Funkci `onSuccess`** Carbon používá na: znovunačtení dat, zavření modalu, reset formuláře. Když
funkci nezadáš, úspěšný stav zůstane na obrazovce **navždy**.

**Interakce:** interaktivní prvky spojené s tlačítkem musí být po dobu načítání disabled, aby
uživatel nemohl akci vyvolat znovu.

**Umístění:** když inline loading dočasně nahradí obsah, musí být na stejném místě a se stejným
zarovnáním jako obsah, který nahradil.

**ZDROJ:** Carbon, Inline loading usage. https://carbondesignsystem.com/components/inline-loading/usage/

## Progress bar

**Rozhodnutí determinovaný versus nedeterminovaný:**

| Varianta | Kdy | Chování |
|---|---|---|
| Determinovaný | Postup lze spočítat proti konkrétnímu cíli (stahování souboru známé velikosti) | Plní se od 0 do 100 %, **nikdy neklesá ani neresetuje** |
| Nedeterminovaný | Postup je neznámý nebo dobu čekání nelze spočítat | Pruh se rychle a opakovaně pohybuje zleva doprava. **Carbon rezervuje pohyb tam a zpět pro skeletony** |

**Přechod:** nedeterminovaný se **může** změnit na determinovaný, jak se posbírá dost informací.
Finální determinovaná fáze pak vizuálně oznámí dokončení.

**Kdy progress bar použít:** dlouhá operace nebo proces s významným či neznámým trváním. Když se
proces dá popsat kvantitativně (procentem). Na vizualizaci postupu systémové operace (download,
upload, načítání dat, odeslání formuláře, uložení změn).

**Kdy ne:**

- Když se čeká na zobrazení rozbaleného obsahu: **skeleton**.
- Když je k postupu potřeba manuální akce uživatele: **progress indicator**.
- Když postup určují akce uživatele (dokončené tutoriály, zabrané místo), ne akce systému.
- Když proces trvá **méně než 5 sekund**: loading indikátor.

**Tři typy operací a jejich vyčíslitelnost podle Carbonu:**

| Operace | Vyčíslitelnost |
|---|---|
| Download | Obvykle lze získat hodnotu postupu a aktualizovat v reálném čase. Podle dat ze zdroje lze odhadnout i zbývající čas |
| Upload | Podle zdroje dat a konfigurace API to reálný postup hlásit nemusí umět. I tak se snaž dát determinovanou hodnotu, kdykoliv to jde |
| Zpracování dat | Podle operace lze použít odhadovaný čas nebo počet cyklů |

**Tři statusy:** active (animovaný pruh, akce běží), success (plná šířka plus checkmark), error
(pruh se rozšíří na plnou šířku, zčervená a **zůstane vidět**, plus ikona selhání). Při chybě musí
přijít inline notifikace nebo obsluha chyby ve formuláři.

**Po dokončení** může progress bar zůstat jako potvrzení, nebo automaticky zmizet, podle situace.

**Text:**

| Prvek | Pravidlo |
|---|---|
| Label | Krátký, pár slov nebo jedna řádka. **Nikdy se během načítání nemění** a nemusí se měnit ani na konci, protože úspěch nebo chybu nese barva pruhu a ikona. Lze ho vizuálně skrýt, ale musí být definovaný pro čtečku |
| Helper text | U determinovaného typicky procento, zlomek, poměr nebo číselná hodnota. U nedeterminovaného kvantitativní hodnota **nejde**, použij obecnou frázi („Fetching assets...") nebo počet („42/256 items"). Procento má **odpočítávat nahoru** s postupem |
| Chybový status | Musí problém sdělit v chybovém helper textu |

**Umístění textu:** label **vždy nad** progress barem kvůli čitelnosti, helper text pod ním nebo
vedle. **Nedávej text do pruhu ani do dráhy**, dělá to nepořádek a nekonzistentní zarovnání. Ale
nedávej ho ani daleko, protože se ztratí kontext.

**Rozměry:** dvě výšky, 8 px a 4 px. Menší se hodí do karet, tabulek a bočních panelů. Minimální
šířka 48 px, a **maximum drž na šesti sloupcích**. Příliš dlouhý progress bar zhoršuje čitelnost.
**Nerozšiřuj ho na celou šířku okna nebo aplikace.**

**Zarovnání textu:** default (celá stránka, karty, dialogy), inline (datová tabulka), indent (boční
panely, karty na dashboardu, kde progress bar sahá k hranám).

**Interakce podle umístění:**

| Kde | Co se blokuje |
|---|---|
| Část stránky | S ostatními prvky stránky lze dál pracovat |
| Uvnitř kontejneru | Podle situace zneaktivni celý kontejner, nebo jen tu sekci, která se zpracovává. Se zbytkem kontejneru a stránky, který to neovlivňuje, musí jít pracovat |

**RTL:** rozvržení se zrcadlí, label vpravo, hodnota vlevo, pruh se plní zprava doleva. Pozor na
polohu znaku procenta, liší se podle lokalizace.

**ZDROJ:** Carbon, Progress bar usage. https://carbondesignsystem.com/components/progress-bar/usage/
Carbon k tomu cituje NN/g Progress Indicators a Response Times: The 3 Important Limits, tedy stejné
zdroje jako [formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).

## Postupné načítání (progressive loading)

**Co to je:** stránka se načítá v dávkách. Nejdřív nejjednodušší pohled, pak postupně detailnější
dávky, dokud není celý viewport hotový.

**Co do které dávky:**

| Dávka | Obsah |
|---|---|
| První | Základní struktura stránky (skeleton verze kontejnerových komponent), datový text (skeleton verze textu) a nedatový text |
| Další | Obrázky, obsah mimo viewport, interaktivní (akční) komponenty, datový text |

**Ne všechno potřebuje skeleton.** Carbon říká, že část může být do načtení vyjádřená jako prázdné
místo. Příklad: obrázek 600 × 600 px se do načtení může zobrazit jako plocha 600 × 600 px bílého
místa.

**Kdy použít:**

| Situace | Detail |
|---|---|
| Pohled se načítá pomalu | Stránky, které tahají data z víc zdrojů, typicky dashboardy |
| Uživatel změní filtry nebo fasety v tabulce | Tabulky mohou tahat z velkých datových sad, zpracování zabere chvíli |

**ZDROJ:** Carbon, Loading pattern, Progressive loading.
https://carbondesignsystem.com/patterns/loading-pattern/

## Load more

**Kdy:** rozšíření seznamu, kde je zobrazený jen zlomek možností. Nebo když se seznam plní
z databáze, aby se data načítala v postupných dávkách.

Carbon zmiňuje „Load more" i jako variantu „Show more" tam, kde je problém s výkonem.
Viz [Přetečení a truncation](preteceni-a-truncation.md).

**ZDROJ:** Carbon, Loading pattern, Load more options a Overflow content pattern.
https://carbondesignsystem.com/patterns/loading-pattern/

## Načítání ve dvou konkrétních kontextech

**V datové tabulce:** když se čeká na zobrazení informace, použij **skeleton, ne spinner**.
Zdroj: https://carbondesignsystem.com/components/data-table/usage/

**V modalu:** dokončení akce má proběhnout okamžitě. Delší čekání = spinner s overlayem nad tělem
modalu, obsah disabled, primární tlačítko disabled. Krátké čekání = inline loading na primárním
tlačítku. Když akce potřebuje víc než pár sekund, informaci o postupu zobraz **jinde na obrazovce**.
Zdroj: https://carbondesignsystem.com/components/modal/usage/
Detail: [Dialogy a panely](dialogy-a-panely.md)

## Přístupnost

**PRAVIDLO:** Čtečka musí uživatele informovat, když aplikace načítá, je zaneprázdněná, zasekne se
nebo proces selže.
**TŘÍDA:** A jako požadavek (WCAG 4.1.3 Status Messages, AA, a W3C podklad Notification of
Loading/Busy), B pro Carbonovu techniku.
**ZDROJ:** Carbon, Loading pattern, Accessibility, s odkazem na
https://www.w3.org/WAI/GL/wiki/Notification_of_Loading/Busy
https://carbondesignsystem.com/patterns/loading-pattern/

Konkrétní technika (`aria-live` assertive versus polite, oznámení dokončení, `role="progressbar"`,
`aria-busy`) je v [Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md).

---

## Co tahle nota neřeší

- Prahy čekání 0,1 / 1 / 10 s a jejich zdroj.
  [Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).
- Krokování progress baru (víc menších kroků působí rychleji, peer-reviewed). Tamtéž.
- Konvexní vztah rychlosti animace a vnímaného čekání (Ding & Kyung 2025).
  [Pohyb](../../ux-design/pravidla/pohyb.md).
- `prefers-reduced-motion` a přerušitelnost animací. Tamtéž.
- Progress indicator jako komponentu pro krokovaný proces.
  [Navigace v hierarchii](../komponenty/navigace-v-hierarchii.md).

## Zdroj

IBM Carbon Design System: Loading pattern, Loading usage, Inline loading usage, Progress bar usage.
Lokální kopie přečtená 30. 7. 2026. https://carbondesignsystem.com/patterns/loading-pattern/
Carbon cituje NN/g Progress Indicators (2001), Response Times: The 3 Important Limits (1993),
Bill Chung o skeleton stavech (Medium UX Collective, 2018) a W3C.
Třída **B**, u WCAG požadavků **A**. Carbonovo tvrzení o přínosu skeletonů je v téhle knihovně
**doloženě sporné**, viz sekce výše.
