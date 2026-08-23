# Stav pohledu v URL

Co z rozhraní patří do adresy a co ne, aby šel pohled sdílet odkazem a aby tlačítko zpět dělalo to,
co uživatel čeká. Zavírá mezeru, kterou si jmenuje [Hromadné akce](hromadne-akce.md).

**Platí i mimo produktové aplikace.** Je to chování prohlížeče a očekávání uživatele, ne konvence
Carbonu. Filtr v e-shopu a záložka na marketingovém webu mají stejný problém.

Související: [Filtrování](filtrovani.md) · [Stránkování](../komponenty/strankovani.md) ·
[Taby](../komponenty/taby.md) · [Hledání](hledani.md) · [Hromadné akce](hromadne-akce.md)

## Rychlé rozhodnutí

1. **Do URL patří všechno, co mění, co uživatel vidí.** Filtr, hledaný výraz, řazení, stránka,
   aktivní tab, rozbalený panel.
2. **Do URL nepatří to, co je uživatelovo a pomíjivé.** Výběr řádků, otevřený modál, pozice kurzoru,
   rozpracovaný text ve formuláři.
3. **Změna, kterou uživatel vyvolal vědomě, je `pushState`.** Vrátí se k ní tlačítkem zpět.
4. **Průběžná změna během psaní nebo tažení je `replaceState`.** Jinak zaplní historii.
5. **Výchozí hodnotu do URL nepiš.** `?page=1` a `?sort=default` jsou šum.
6. **Pohled musí jít otevřít z prázdné relace.** Odkaz poslaný kolegovi nesmí záviset na tom,
   co má v prohlížeči uložené.
7. **Neplatnou hodnotu v adrese nesmíš spolknout ani spadnout na ni.** Vrať se k výchozí a řekni to.

## Co do adresy patří a co ne

| Stav | Do URL | Proč |
|---|---|---|
| Filtr a faseta | **Ano** | Bez toho nejde poslat „koukni na tohle" |
| Hledaný výraz | **Ano** | Totéž, plus zpět z detailu musí vrátit výsledky |
| Řazení | **Ano** | Mění pořadí, tedy to, co uživatel vidí |
| Stránka | **Ano** | Zpět z detailu má vrátit tutéž stránku |
| Aktivní tab | **Ano** | Odkaz na konkrétní záložku je běžné očekávání |
| Rozbalený panel nebo sekce | **Ano, když je jich málo** | U dlouhého seznamu accordionů je to nečitelné |
| Časový rozsah v dashboardu | **Ano** | Jinak je snímek nesdělitelný |
| **Výběr řádků** | **Ne** | Je to uživatelův pracovní stav, ne pohled. Viz níže |
| Otevřený modál | **Většinou ne** | Výjimka: modál, který je vlastně stránka (detail položky) |
| Rozpracovaný formulář | **Ne** | Patří do konceptu, ne do adresy |
| Pozice scrollu | **Ne** | Řeší `scrollRestoration`, viz níže |
| Cokoliv citlivého | **Nikdy** | Adresa se loguje na serveru, v proxy i v historii |

**TŘÍDA:** C pro celé rozdělení. Je to řemeslná syntéza, nedohledal jsem k tomu měření ani
normativní text. Vercel to má jako holý imperativ bez odůvodnění, viz Zdroj.

**Poslední řádek je bezpečnostní, ne designový.** Do query stringu nepatří token, e-mail ani rodné
číslo, protože adresa přežije v serverových logách a v historii prohlížeče. Když filtr filtruje
podle osobního údaje, posílej identifikátor, ne hodnotu.

## Výběr řádků do adresy nepatří

**PRAVIDLO:** Vybrané řádky neukládej do URL.
**KDY PLATÍ:** Vždy, i když je výběr malý.
**PROČ:** Tři důvody a stačí jeden. Za prvé, výběr se ruší při změně filtru (viz
[Hromadné akce](hromadne-akce.md)), takže by adresa nesla stav, který sama vzápětí zneplatní.
Za druhé, sdílený odkaz by příjemci předvybral cizí položky, což je u hromadného mazání past.
Za třetí, výběr nad filtrem může být 4 812 položek a ty se do adresy nevejdou.
**TŘÍDA:** C.
**KDY NEPLATÍ:** Pohled, který je z podstaty o konkrétní množině a nemá dávkové akce, například
srovnávač produktů. Tam je ale výběr obsahem pohledu, ne pracovním stavem.

## `pushState` versus `replaceState`

**PRAVIDLO:** Vědomou změnu pohledu zapiš `pushState`, průběžnou `replaceState`.

| Akce uživatele | Metoda | Proč |
|---|---|---|
| Použití filtru tlačítkem, přepnutí tabu, změna stránky | `pushState` | Uživatel to udělal záměrně a čeká, že zpět to vrátí |
| Psaní do vyhledávacího pole | `replaceState` | Jinak vznikne záznam na každý stisk klávesy |
| Tažení posuvníku rozsahu | `replaceState` během tažení, `pushState` po puštění | Historie má nést výsledek, ne průběh |
| Zápis výchozího stavu při načtení | `replaceState` | Nemá vzniknout druhý záznam pro tutéž stránku |

**KDY PLATÍ:** Každá aplikace, která mění pohled bez načtení stránky.
**PROČ:** Uživatel má tlačítko zpět naučené jako „vrať mi předchozí pohled". Když každé písmeno
v hledání založí záznam, tlačítko zpět přestane fungovat jako výstup ze stránky a uživatel se
z aplikace nedostane jinak než přidržením tlačítka.
**TŘÍDA:** A pro mechanismus obou metod, C pro přiřazení akcí.
**ZDROJ:** MDN, Working with the History API, verbatim: „The `pushState()` method adds a new entry to
the session history, while the `replaceState()` method updates the session history entry for the
current page." K reakci na navigaci: „When the browser navigates to this history entry, the browser
fires a `popstate` event, which contains the state object associated with that entry."
https://developer.mozilla.org/en-US/docs/Web/API/History_API/Working_with_the_History_API
Čteno 23. 8. 2026.
**KDY NEPLATÍ:** Klasická vícestránková aplikace, kde navigaci obstarává server. Tam se řeší jen to,
co je v adrese, ne jak se tam dostalo.

**Na `popstate` musíš reagovat.** Zápis do adresy bez obsluhy zpětné navigace je horší než žádný
zápis: adresa se změní, obsah ne, a uživatel vidí pohled, který neodpovídá tomu, co má v řádku.

## Tlačítko zpět

**PRAVIDLO:** Po zpět musí být pohled **vizuálně tentýž**, ze kterého uživatel odešel: stejný filtr,
stejná stránka, stejné řazení, stejná pozice ve výpisu.
**KDY PLATÍ:** Nejostřeji na cestě seznam, detail, zpět. To je nejčastější cesta v produktové aplikaci.
**PROČ:** Když se uživatel vrátí z detailu na první stránku nevyfiltrovaného seznamu, přijde
o kontext, který si sám vytvořil, a musí ho postavit znovu. U seznamu s deseti filtry to je konec práce.
**TŘÍDA:** C.
**KDY NEPLATÍ:** Návrat na krok, který už neplatí (smazaná položka, vypršelá relace). Tam ukaž stav,
který vysvětluje, co se stalo, ne prázdnou tabulku. Viz [Prázdné stavy](prazdne-stavy.md).

**Pozice ve výpisu je zvláštní případ.** Prohlížeč ji obnovuje sám, ale u obsahu načteného až po
navigaci nemá co obnovit.
**ZDROJ:** MDN, `History.scrollRestoration`, verbatim k hodnotám: `auto` je „The location on the page
to which the user has scrolled will be restored", `manual` je „The location on the page is not
restored. The user will have to scroll to the location manually."
https://developer.mozilla.org/en-US/docs/Web/API/History/scrollRestoration Čteno 23. 8. 2026.
Sáhni po `manual` jen tehdy, když si obnovu pozice řešíš sám po dotažení dat. Jinak ji nech na `auto`.

## Sdílitelnost pohledu

**PRAVIDLO:** Otevření adresy v prázdné relaci (jiný prohlížeč, anonymní okno) musí dát **tentýž
pohled**, kromě dat, na která příjemce nemá oprávnění.
**KDY PLATÍ:** Každý pohled, jehož adresa se mění.
**PROČ:** To je celý důvod, proč se stav do adresy dává. Když se část stavu drží v `localStorage`
nebo v paměti, odkaz je nepravdivý a lidé si posílají snímky obrazovky místo odkazů.
**TŘÍDA:** C.
**KDY NEPLATÍ:** Osobní nastavení, které pohled nemění (hustota, oblíbené sloupce). To do adresy
nepatří a v úložišti prohlížeče je správně.

**Když příjemce nemá oprávnění**, ukaž stav „nemáš přístup" s vysvětlením a akcí, ne prázdný seznam
a ne přesměrování na domovskou stránku. Prázdný seznam se čte jako „nic tu není", což je jiná
informace. Viz [Prázdné stavy](prazdne-stavy.md), typ „chybí oprávnění".

## Tvar adresy

**PRAVIDLO:** Výchozí hodnoty vynechávej, parametry pojmenuj podle domény, ne podle komponenty,
a pořadí drž stabilní.
**KDY PLATÍ:** Vždy.
**PROČ:** Adresa je taky rozhraní. `?stav=aktivni&role=admin` řekne příjemci, co uvidí, ještě než
klikne. `?f1=2&f2=7&p=1&s=0` neřekne nic a při každé změně se přeskládá, takže dvě adresy pro tentýž
pohled vypadají různě a nedají se porovnat ani nacachovat.
**TŘÍDA:** C.
**KDY NEPLATÍ:** Velmi složité filtry, kde by čitelný zápis adresu neúnosně natáhl. Tam se ukládá
pojmenovaný pohled na serveru a v adrese je jeho identifikátor. To je ale jiný vzor, ne zkratka.

**Neplatná hodnota v adrese** je běžný stav, ne chyba programátora: adresy se upravují ručně,
zastarávají a přežijí změnu produktu. Vrať se k výchozí hodnotě, pohled zobraz a **řekni, že se to
stalo** („Filtr `role=superadmin` už neexistuje, zobrazuji vše"). Tiché ignorování je horší,
protože uživatel uvidí jiná data, než pro která dostal odkaz.

## Přístupnost

Změna pohledu bez načtení stránky je pro čtečku neviditelná, dokud jí to někdo neřekne.

**PRAVIDLO:** Po použití filtru nebo změně stránky oznam výsledek do live region („Zobrazeno 24
z 4 812") a **focus nepřesouvej**, když uživatel zůstává na tomtéž místě.
**TŘÍDA:** A pro požadavek (WCAG 4.1.3 Status Messages, Level AA), C pro znění.
**ZDROJ:** WCAG 2.2 SC 4.1.3. https://www.w3.org/WAI/WCAG22/quickref/ Drátování je v
[Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md).

Titulek stránky (`<title>`) měň spolu s adresou. Je to první věc, kterou čtečka po navigaci přečte,
a zároveň to, co se uloží do záložek a historie.

## Co tahle nota neřeší

- **Konkrétní knihovnu na synchronizaci stavu s adresou.** Princip je nezávislý na frameworku.
- **Serverové renderování a cachování podle query stringu.** To je výkonové téma, ne designové.
- **Pojmenované uložené pohledy** („Moje otevřené tikety") jako produktová funkce. Zmíněné jen jako
  východisko pro složité filtry.
- **Hluboké odkazy do nativní aplikace.** Jiná doména.
- **Kolik filtrů je moc.** Viz [Filtrování](filtrovani.md).

## Zdroj

- MDN, [Working with the History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API/Working_with_the_History_API)
  a [`History.scrollRestoration`](https://developer.mozilla.org/en-US/docs/Web/API/History/scrollRestoration).
  Obojí čteno 23. 8. 2026.
- WCAG 2.2, SC 4.1.3 Status Messages, Level AA. https://www.w3.org/WAI/WCAG22/quickref/
- Podnět a osnova: [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines),
  MIT, kategorie „Navigation & State", verbatim: „URL reflects state - filters, tabs, pagination,
  expanded panels in query params" a „Deep-link all stateful UI". Odůvodnění a hranice, tedy co do
  adresy nepatří, tam nejsou a jsou doplněné knihovnou.

**Většina pravidel je třída C.** Mechanika History API a požadavek na oznámení stavu jsou A, zbytek
je řemeslná syntéza. Kdyby se k tomu našlo měření, nota se má přepsat, ne doplnit.
