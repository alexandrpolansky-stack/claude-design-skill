# Kontext: gastro (restaurace, bar, kavárna)

**Tenhle sektor je v knihovně evidenčně obrácený.** U [luxury](luxury.md) je regulace skoro nulová
a všechno je volba. Tady je to naopak: regulatorní vrstva je nejkonkrétnější z celého privátního
sektoru (alergeny mají vlastní nařízení a v prodeji na dálku vlastní článek), zatímco positioning
a vizuální vrstva je stejně slabě podložená jako v luxury. K tomu je gastro jediný sektor, kde
existuje samostatná výzkumná tradice o designu MENU, měřená eye-trackingem a field experimenty.
Vznikla ale na papírovém dvoustránkovém menu, ne na webu, a metaanalýza téhle tradice sama říká, že
její efekty jsou v poli řádově menší než v laboratoři (viz pravidlo o diskontu níže).

**Zároveň je to nejzaneřáděnější informační prostředí v celé knihovně.** Konzultantská "menu
psychologie" recykluje tvrzení, která nikdy nikdo neměřil, a při průzkumu se nezávisle na sobě
našly **dvě kompletně vyfabrikované citace studií**, které v SEO obsahu kolují jako fakt (obě jsou
vypsané v sekci Co v tomhle sektoru NENÍ). Sem se nepřebírá nic bez dohledání primárního textu.
Nota je proto delší než sesterské a značná část její hodnoty je v tom, co vyvrací.

**Kdo je čtenář.** Dvě situace, ne dvě demografie. Buď člověk s úkolem (je otevřeno? kde to je?
kolik to stojí? mají něco bez lepku?), který rozhodnutí "jdeme někam" už udělal a hledá údaj. Nebo
člověk, který vybírá zážitek a čte web jako ukázku toho, jaký bude večer. Ten první potřebuje
údaje, ten druhý důvod. Většina reálných briefů obsahuje oba, jen v jiném poměru. Existuje k tomu
i naměřená segmentace: v choice-based conjointu na restauračních profilech vyšly dva segmenty,
"visually oriented" a "price-rating oriented" (Liu, Wei, Kalgotra, Çobanoğlu, 2022, International
Journal of Hospitality Management 104, 103248, N=746 plus dolování 92 934 obrázků z OpenTable;
metadata ověřena, abstrakt jen sekundárně).

**Dopad chyby.** Rozdělený na tři nesouměřitelné vrstvy, a to je pro tenhle sektor určující:
- **Utilitní chyba** (chybí hodiny, adresa, menu není čitelné na mobilu) je nejčastější a přitom
  neměřitelná. Host, který nenajde, jde jinam a nikdy se neozve.
- **Positioning chyba** (web vypadá levněji, než podnik je) je asymetrická a nezachytí ji žádná
  metrika, přesně jako v [luxury](luxury.md).
- **Alergenová chyba** je jediný případ v celé knihovně, kdy designové rozhodnutí může někoho
  poslat do nemocnice, a je zároveň pokutovatelná. Tahle vrstva nemá s vkusem nic společného
  a nesmí se s ním míchat.

**Regulace vs volba.** Nejkonkrétnější regulatorní vrstva ze všech privátních sektorů v knihovně,
ale se dvěma dírami, které se v praxi pravidelně pletou:
1. Povinnost informovat o alergenech platí v provozovně **vždy** (nařízení 1169/2011, čl. 44). Na
   web se přenáší až ve chvíli, kdy web přijímá objednávku (čl. 14 odst. 2).
2. European Accessibility Act na gastro dopadá jen přes transakci **a** jen nad velikost
   mikropodniku. Většina jednotlivých restaurací, barů a kaváren je z něj vyjmutá. To je proti tomu,
   jak je EAA popsaný v [e-commerce notě](e-commerce.md), a proti tomu, co tvrdí většina gastro
   marketingového obsahu. Detail v pravidlech níže.

**Vrstvení, které platí i tady.** Strukturu a pozice neodchyluj (menu, hodiny, adresa, rezervace).
Regulatorní parametry ber jako mantinel. Odchyluj povrch: fotografii, paletu, písmo, motion. Na
destinačním konci osy je prostor na povrchu velký, na utilitním malý, protože tam povrch soutěží
s hustotou údajů.

Legenda tříd: A = tvrdá opora (měření), B = publikovaná konvence nebo regulace, C = řemeslná praxe
či pozorování bez opory. C se nikdy nepovyšuje na A, ani když se tak v praxi cituje.

Sesterské noty: [luxury.md](luxury.md), [e-commerce.md](e-commerce.md), [finance.md](finance.md),
[dev-tools-saas.md](dev-tools-saas.md), [vlada.md](vlada.md), [zdravotnictvi.md](zdravotnictvi.md),
[deti.md](deti.md), [seniori.md](seniori.md).

---

## Proč je to jedna nota a ne dvě

Rozptyl uvnitř gastra je větší než u ostatních osmi sektorů. Krajní body jsou tak daleko od sebe,
že se nabízí je rozdělit. Rozdělené nejsou, ze čtyř důvodů:

1. **Regulatorní vrstva je na celé ose stejná.** Alergeny, EAA, kalorie a reklama na alkohol platí
   pro luxusní bar i pro polední menu identicky. Ve dvou notách by se duplikovala a jedna kopie by
   zastarala dřív než druhá. Přesně tenhle failure mode repo už jednou zaplatilo: gridlines byly
   opravené ve skillu a ne v knihovně a půl roku radily opak (viz [CLAUDE.md](../../CLAUDE.md)).
2. **Je to osa, ne dvě kategorie.** Vinný bar s poledním menu, bistro, které je v jedenáct kantýna
   a v osm destinace, hotelová restaurace. Dvě noty by nutily ke klasifikaci, kterou zadání
   neumožňuje.
3. **V repu už je precedens.** [deti.md](deti.md) drží tři věková pásma, která se od sebe liší
   silněji než casual a fine dining, v jedné notě, a segmentaci řeší jako první pravidlo. Tady je to
   stejná konstrukce.
4. **Pravidla se na ose nepřepínají, mění se jim parametry.** Jen dvě z pravidel níže se skutečně
   obracejí (viditelnost ceny a hustota údajů v prvním zorném poli). Zbytek platí po celé ose,
   s jinou intenzitou.

Osa má v téhle notě jméno **destinace ↔ sousedská utilita**:

| | Destinace | Sousedská utilita |
|---|---|---|
| Co web prodává | důvod přijít, atmosféru | dostupnost a orientaci |
| Metrika | positioning, ne konverze | najde host údaj a přijde |
| Hustota v prvním pohledu | jeden obraz, málo slov | údaje hned, žádné tajemství |
| Cena na webu | může chybět záměrně | patří tam |
| Odkud vede k jiné notě | [luxury.md](luxury.md) | [e-commerce.md](e-commerce.md) při objednávce |

**Osa sama je PRACOVNÍ HYPOTÉZA, ne zjištění.** Konceptuální oporu má dělení v rozlišení hedonické
a utilitární hodnoty spotřeby (Babin, Darden, Griffin, 1994, Journal of Consumer Research 20(4),
644-656, škála PSV; korroborace v Journal of Business Research 126 (2021), 578-590). Je to
publikovaný a replikovaný konstrukt, **ale jeho doména je nákupní chování v retailu, ne design
gastro webu**. Žádná studie tuhle osu na gastro weby nemapuje a nehledala se. Třída C, nepřenášej
z ní žádná čísla, a až se najde měření, přepiš ji nebo zahoď. Rozhodnutí "jedna nota" stojí na
argumentech 1 až 4 výše, které jsou pevné (duplikace regulace, precedens v repu); samotné POJMENOVÁNÍ
osy pevné není.

---

## Pravidla

### Umísti klienta na osu, nestav "web pro restauraci"

**PRAVIDLO:** Než padne první rozhodnutí o layoutu, zjisti a zapiš, kde na ose destinace ↔
sousedská utilita klient stojí a čím to podložíš (cenová hladina, jak host přichází, jestli se
rezervuje, jestli je podnik cílem cesty nebo tím, co je nejblíž). Podle toho se rozhoduje hustota
prvního pohledu a viditelnost ceny. Web optimalizovaný pro průměr osy neslouží ani jednomu konci.
**KDY PLATÍ:** Na začátku každého gastro projektu, před wireframem.
**PROČ:** Krajní body osy vedou k opačným rozhodnutím o téže obrazovce a obě jsou ve svém kontextu
správná. Dva reálné pražské podniky, oba dobře udělané, oba ověřené naživo 29. 7. 2026:
- Craft cocktail bar ve Starém Městě (`beyondthebar.cz`): první obrazovka je jeden atmosférický obraz a pět textových
  odkazů (Menu, Spirit list, Instagram, Visit us, Contact), z praktických prvků jen běžící hodiny
  "Prague 18:30". Menu na webu je šest signature koktejlů se surovinami a **bez cen**, s explicitní
  větou "Full menu available only at the bar." Adresa, hodiny, mail a telefon na webu jsou, ale až
  v sekci Find Us na konci jednostránky. Žádná online rezervace.
- Kavárna v Karlíně (`mujsalekkavy.cz`): nad fotkou je nejdřív řada odkazů na sesterské podniky, pak pět kategorií menu,
  pak adresa, hodiny a telefon v jedné řádce, pak Mapa, Rezervace, Dárkové poukazy, Email, Kariéra
  a nakonec sociální sítě. Nula tajemství, všechno v prvním bloku.
**TŘÍDA:** C. Osa je odvozená (viz sekce výše), příklady jsou vlastní pozorování s n=2.
**ZDROJ:** Vlastní analýza dvou živých webů přes headless prohlížeč, 29. 7. 2026 (struktura ověřena
ze snapshotu DOM a přístupnostního stromu, ne z popisu). Konceptuální rámec Babin, Darden, Griffin
(1994). Metoda odpovídá postupu použitému ve [vizualni-craft.md](../pravidla/vizualni-craft.md).
**KDY NEPLATÍ:** Když klient obojí kombinuje v čase (denní kantýna, večerní destinace). Pak se osa
neurčuje pro podnik, ale pro vstupní bod: polední menu je utilita, večerní prezentace destinace,
a je legitimní mít pro každý jinou stránku.

### Diskontuj laboratorní nálezy o menu na třetinu

**PRAVIDLO:** Když stojí doporučení o menu na laboratorním testu s fingovaným menu, neber jeho
velikost efektu do klientského slibu. Ber ho jako směr a čekej v provozu řádově třetinu. Pravidlo
platí i na pravidla o menu v téhle notě.
**KDY PLATÍ:** Vždy, když se z výzkumu o menu dělá odhad dopadu.
**PROČ:** Metaanalýza designu menu (53 studií, 61 intervencí, 16 522 účastníků, 279 velikostí
efektu) našla celkový efekt d=0,39 (95% CI 0,34-0,45), ale s prudkým gradientem podle realističnosti
designu: laboratoř 0,45 (0,38-0,52) proti poli 0,18 (0,12-0,24), a fingované menu 0,48 proti
reálnému menu 0,16 (0,06-0,26), obojí p<0,001. Heterogenita I²=95 %. Nejsilnější dimenzí byly
vlastnosti samotné menu karty (0,85), zatímco **dimenze popisu položky, pod kterou spadá i vizuální
informace včetně fotek, měla ze šesti nejmenší efekt a na skutečný nákup vyšla nesignifikantně**.
**TŘÍDA:** A.
**ZDROJ:** Ip & Chark (2023), International Journal of Hospitality Management 108, 103353,
random-effects meta-analýza, plný text čten. Mírný publikační bias (LFK 1,37).
**KDY NEPLATÍ:** Metaanalýza fotografii neizoluje jako vlastní moderátor, takže z ní **nelze**
odvodit číslo pro fotku samotnou. A diskont není důvod výzkum ignorovat: směry efektů drží, jen
velikosti ne.

### Cenu na webu ukaž, i na horní polovině osy

**PRAVIDLO:** Default je cena viditelná v menu na webu. Skrytí ceny je vědomé positioning
rozhodnutí, které se zapíše a odůvodní, ne úspora práce.
**KDY PLATÍ:** Celá osa kromě explicitně destinačního positioningu s vlastním odůvodněním.
**PROČ:** V měření priorit při volbě restaurace byla cena v menu na **prvním místě ve všech třech
testovaných segmentech** (full-service, quick-casual, quick-service). Není to jen věc fast foodu.
Druhé místo se přitom mezi segmenty lišilo, cena ne.
**TŘÍDA:** A ve své doméně, C jako přenos.
**ZDROJ:** Chua, Karim, Lee, Han (2020), International Journal of Environmental Research and Public
Health 17(17), 6276, N=539, Klang Valley (Malajsie), papírový dotazník, respondenti řadili 9 kritérií
od 1 do 9, plný text čten. **Limit, který autoři sami uvádějí:** jediná metropolitní oblast
v Malajsii, tedy omezená generalizovatelnost. Dvě vlastní výhrady: měří deklarovanou důležitost, ne
chování, a **fine dining jako samostatný segment v datech není** ("full-service" není totéž).
**KDY NEPLATÍ:** Destinační konec osy, kde je potlačení ceny součástí positioningu. Platí tam
[luxury pravidlo o prodejním tlaku](luxury.md): je to byznys rozhodnutí, ne vizuální. Kdo cenu
skryje, ať ví, že platí kritériem, které je jinak na prvním místě.

### Praktické údaje nejsou patička

**PRAVIDLO:** Adresa, otevírací doba a telefon patří na místo, kde je host najde bez hledání, a to
i na destinačním konci osy. Adresu proklikni do mapové aplikace, telefon do `tel:`. Telefon
neschovávej a nenahrazuj formulářem.
**KDY PLATÍ:** Každý gastro web. Intenzita se po ose mění, existence ne.
**PROČ:** Publikovaná konvence to říká přímo: "Include hours of operation and time zones", "Clearly
display contact phone numbers... Don't hide or remove phone numbers", "Link address(es) so they open
a map application where users can get directions." Google to má ve strukturovaných datech pro
LocalBusiness jako povinné `address` a `name` a doporučené `menu`, `openingHoursSpecification`,
`priceRange`, `telephone`, `geo`. A hledání pobočky měřitelně selhává i dnes: v opakovaných vlnách
testů lokátorů vyšla úspěšnost 63 % (2001) a 97 % (2018), ale hladce dořešených úkolů bylo jen
57 % a potíže se objevily ve 40 % případů.
**TŘÍDA:** B pro konvenci, A pro měření lokátorů. Přenos na gastro je C.
**ZDROJ:** Kaley, NN/g (2019), Contact Us Page Guidelines, 20 profesionálů, 40 webů, kontext B2B.
Harley, NN/g (2018), Store Finders and Locators, 4 vlny, celkem 46 účastníků, 28 desktop a 28 mobil
webů, **restaurace ve vzorku byly**. Nielsen, NN/g (2001), lokátory 10 velkých firem. Google
LocalBusiness structured data (developers.google.com).
**KDY NEPLATÍ:** Kolující číslo "80 % lidí jde přímo do vyhledávače nebo do map" je z téhož
zdroje, **ale pro úkol najít pobočku vlastní banky**, ne restauraci, a NN/g pro ten podnález
neuvádí N. Na gastro se nepřenáší, i když je to intuitivně pravděpodobné. Kolik návštěv reálně
přichází přes Google Business Profile místo homepage, žádný publikovaný benchmark neříká, změřit se
to dá jen na konkrétním profilu.

### Alergenová povinnost se zapíná objednávkovým tlačítkem

**PRAVIDLO:** Informační web bez transakce nemusí alergeny řešit. Ve chvíli, kdy na webu nebo
v aplikaci vzniká objednávka, musí být informace o alergenech dostupná **před dokončením
objednávky**, na materiálu, který ten prodej nese, nebo jiným jasně určeným způsobem, a bez
příplatku. Nestačí ji poslat s jídlem.
**KDY PLATÍ:** Každý web nebo aplikace, kde host objednává jídlo nebo pití k odběru či rozvozu.
**PROČ:** Nařízení 1169/2011 dělá u nebalených pokrmů povinný jediný údaj, a to alergeny (čl. 44
odst. 1 písm. a) odkazem na čl. 9 odst. 1 písm. c), tedy 14 skupin z přílohy II). Restaurace,
kantýna a kavárna jsou "zařízení společného stravování" podle definice v čl. 2 odst. 2 písm. d).
A čl. 14 odst. 2 tuhle povinnost výslovně protahuje do prodeje na dálku: "In the case of
non-prepacked foods offered for sale by means of distance communication, the particulars required
under Article 44 shall be made available in accordance with paragraph 1 of this Article." Odstavec 1
písm. a) žádá dostupnost "before the purchase is concluded" a na "material supporting the distance
selling", odstavec 1 písm. b) pak znovu při doručení.
**TŘÍDA:** B (regulace, právně vynutitelná).
**ZDROJ:** Nařízení (EU) č. 1169/2011, čl. 2 odst. 2 písm. d), čl. 9 odst. 1 písm. c), čl. 14
odst. 1 a 2, čl. 44 odst. 1 a 2, znění ověřeno proti EUR-Lex (anglická verze). České provedení:
§ 9a zákona č. 110/1997 Sb. a § 7 odst. 3 vyhlášky č. 417/2016 Sb., dozor SZPI.
**KDY NEPLATÍ:** Web, který jen informuje a neuzavírá objednávku. Tam povinnost leží na provozovně,
ne na stránce. Bar z příkladu výše má v koktejlech mléčné složky (jogurt, mléko, custard) a alergeny
na webu neuvádí, což je při neexistenci online objednávky v pořádku.

### "Zeptejte se obsluhy" nefunguje jako předprodejní kanál

**PRAVIDLO:** Českou variantu "Informaci o výskytu konkrétních alergenů v pokrmu žádejte u obsluhy"
nekopíruj do objednávkového flow na webu jako splnění povinnosti. Když ji použiješ, musí vedle ní
stát konkrétní, jasně určený a bezplatný kanál, kterým host odpověď dostane **před** odesláním
objednávky, ne až u výdeje.
**KDY PLATÍ:** Objednávkové a rozvozové rozhraní.
**PROČ:** Vyhláška nabízí čtyři písemné způsoby: podle čl. 21 nařízení (výčet u položky), větou
"žádejte u obsluhy" včetně následného předání informace, zařízením pro vizuální komunikaci, nebo
kódy a symboly vysvětlenými v nabídce. Všechny čtyři jsou napsané pro provoz, kde obsluha fyzicky
je. V objednávkovém formuláři obsluha v momentě rozhodnutí není. Praktický důsledek pro design: buď
alergeny u položek (nejlépe kódy s legendou, což vyhláška výslovně dovoluje), nebo prominentní
telefon či chat s uvedenou dostupností.
**TŘÍDA:** B pro požadavek dostupnosti před dokončením objednávky, **C pro odvození**, že věta
"žádejte u obsluhy" sama nestačí. Nařízení připouští "other appropriate means clearly identified by
the food business operator" a nikde neříká, že telefon uvedený na stránce nestačí. Tohle je výklad,
ne citace. U ostrého klientského závazku to chce právníka, ne tuhle notu.
**ZDROJ:** § 7 odst. 3 písm. a) až d) vyhlášky č. 417/2016 Sb., znění ověřeno u dvou nezávislých
zdrojů. Nařízení 1169/2011 čl. 14 odst. 1 písm. a).
**KDY NEPLATÍ:** V provozovně je "žádejte u obsluhy" plně dostačující, legální a běžný způsob.
Pravidlo se týká jen digitálního objednávání.

### EAA dopadá na gastro jen přes transakci a jen nad mikropodnik

**PRAVIDLO:** Nepřenášej na gastro klienta tvrzení "od 6/2025 musí web v EU splňovat WCAG 2.1 AA".
Ověř dvě podmínky: (1) uzavírá se na webu spotřebitelská smlouva (objednávka, placená rezervace,
prodej voucheru), a (2) není klient mikropodnik, tedy má 10 a více osob nebo přesahuje 2 mil. EUR
obratu či bilanční sumy. Když jedna z nich neplatí, WCAG je pořád správný default, ale ne právní
povinnost, a takhle se to klientovi říká.
**KDY PLATÍ:** Vždy, když se v nabídce nebo v argumentaci objeví EAA.
**PROČ:** Slovo "restaurant" se v celém textu směrnice nevyskytuje ani jednou, na gastro tedy dopadá
výhradně derivativně přes "e-commerce services". Ty jsou definované jako služby poskytované na
dálku přes weby a mobilní služby "with a view to concluding a consumer contract" (čl. 3 bod 30).
Čistě informační web restaurace smlouvu neuzavírá. A především: **čl. 4 odst. 5 mikropodniky
poskytující služby z požadavků vyjímá úplně**, s odůvodněním v recitálu 70 (náklad na dodržení je
u nich neproporčně velký a i samotné posuzování neproporcionality by bylo zátěží). Většina
jednotlivých restaurací, barů a kaváren tuhle definici splňuje. Řetězec ne.
**TŘÍDA:** B (regulace).
**ZDROJ:** Směrnice (EU) 2019/882, čl. 2 odst. 2 (výčet služeb, "provided to consumers after
28 June 2025"), čl. 3 bod 23 (mikropodnik: "fewer than 10 persons" a obrat nebo bilance do 2 mil.
EUR), čl. 3 bod 30 (definice e-commerce services), čl. 4 odst. 5 (výjimka), recitál 70. Znění
ověřeno proti EUR-Lex dvěma nezávislými průchody. České provedení: zákon č. 424/2023 Sb., § 2
odst. 3 písm. a) vyjímá služby poskytované mikropodnikem, § 3 odst. 1 písm. p) definuje mikropodnik
odkazem na čl. 2 odst. 3 přílohy I nařízení Komise (EU) č. 651/2014, § 29 stanoví účinnost
28. 6. 2025.
**KDY NEPLATÍ:** Řetězec, franšíza nad prahem a hotelová skupina jsou v režimu naplno. **Otevřená
otázka:** jestli samotná bezplatná rezervace bez platby je "concluding a consumer contract",
verbatim text směrnice neřeší a judikatura k tomu nebyla dohledána, takže to je NEOVĚŘENO.
A výjimka je výjimka z právní povinnosti, ne z toho, že část hostů má brýle, artritidu nebo mobil
na slunci. Prahy 4,5:1 a 24×24 px se drží stejně, jen se za ně neargumentuje pokutou. Viz
[kontrast-a-barva.md](../pravidla/kontrast-a-barva.md) a [tlacitka.md](../pravidla/tlacitka.md).

### Vyfocené menu je neopravitelná vada, PDF je měkčí případ

**PRAVIDLO:** Menu na webu sázej jako HTML text. Nikdy ne obrázek s vyfoceným nebo naskenovaným
lístkem. PDF jen jako doplněk ke stažení vedle HTML verze, ne místo ní, a nikdy jako odkaz do cizí
sdílené složky.
**KDY PLATÍ:** Každé menu na webu, po celé ose.
**PROČ:** Rozdíl mezi obrázkem a PDF je věcný, ne stupňovitý:
- **Obrázek menu porušuje současně kritérium úrovně A a AA.** 1.1.1 Non-text Content (A): "All
  non-text content that is presented to the user has a text alternative that serves the equivalent
  purpose." 1.4.5 Images of Text (AA): "If the technologies being used can achieve the visual
  presentation, text is used to convey information rather than images of text." A 1.1.1 se dá
  splnit textovou alternativou, takže obrázek smí zůstat. **1.4.5 se tím splnit nedá**, žádá
  skutečný text, a výjimka "essential" je určená na logotypy a ukázky písma, ne na jídelní lístek.
  Obrázkové menu je tedy na AA nesplnitelné, dokud nepřejde na text.
- **PDF přístupné být může** (tagované, PDF/UA podle ISO 14289-1:2014), takže tvrzení "PDF nemůže
  být přístupné" je nepřesné. V praxi ale skoro nikdy tagované není: v peer-reviewed auditu 20 000
  PDF splnilo všech šest kritérií "less than 3.2%" a "a large majority (74.9%) fail to meet any
  criteria at all". A fixní stránkový layout naráží na reflow: EN 301 549 klauzule 10.1.4.10 žádá
  i u newebového dokumentu zobrazení "without requiring scrolling in two dimensions" na ekvivalentu
  320 CSS px.
- **Reálný nález z živého webu:** kavárna z prvního pravidla má **všech pět kategorií menu jako PDF
  v Google Drive** (ověřeno 29. 7. 2026, cíl odkazu je `msk_kava_cz_web.pdf` v Drive prohlížeči).
  Host kvůli ceně kávy opustí web, čeká na JS viewer cizí služby a dostane dokument, který na
  telefonu nejde pořádně přečíst.
**TŘÍDA:** B pro WCAG kritéria a EN 301 549 (ověřeno proti W3C a proti textu normy; obě kritéria
jsou z WCAG 2.0 a platí i v 2.1 a 2.2). A pro nepřístupnost PDF v praxi, ale v jiné doméně. C pro
tvrzení, že je to v gastru časté (n=1 živé pozorování).
**ZDROJ:** W3C WCAG, SC 1.1.1 (A) a SC 1.4.5 (AA). EN 301 549 V3.2.1 klauzule 10 (aplikuje WCAG na
stahované dokumenty verbatim) a 10.1.4.10 Reflow. Kumar & Wang (2024), Uncovering the New
Accessibility Crisis in Scholarly PDFs, ACM ASSETS 2024, DOI 10.1145/3663548.3675634, 20 000 PDF
z let 2014-2023, šest kritérií, triangulováno checkerem, manuálním hodnocením a testy se screen
readery. GOV.UK: Williams, N. (2018), Why GOV.UK content should be published in HTML and not PDF,
gds.blog.gov.uk, což je **konvence, ne měření**.
**KDY NEPLATÍ:** Sezónní degustační menu, které existuje jako tiskovina, je legitimní publikovat
i jako PDF, pokud je vedle něj HTML verze. U mikropodniku to není právní porušení (viz pravidlo
o EAA), zůstává to ale vada použitelnosti. **A nepodkládej to SEO argumentem:** Google PDF
indexuje, je na jeho seznamu indexovatelných typů, crawluje prvních 64 MB a u obrázků použije OCR.
Obhajitelné je jen to, že PDF je samostatná URL bez navigace, bez rich resultu a bez kontroly nad
titulkem a snippetem.

### Menu se čte jako kniha, ne po zlatém trojúhelníku

**PRAVIDLO:** Nerozmisťuj položky v menu podle "zlatého trojúhelníku" ani podle "sweet spotu"
uprostřed nebo vpravo nahoře. Předpokládej lineární čtení odshora dolů, po sloupcích a kategoriích,
jako v knize.
**KDY PLATÍ:** Návrh menu, papírového i webového.
**PROČ:** Eye-tracking na dvoustránkovém menu žádný frekvenční sweet spot nenašel. Mezi čtyřmi
z pěti sledovaných oblastí nebyl v počtu fixací rozdíl (F(3,96)=0,97, p=0,413). Naopak se ukázal
"sour spot": oblast, na kterou se skoro nekoukalo, a informace o restauraci na konci menu měly
u všech 25 účastníků dohromady 9 fixací. Knižní sekvence 1→2→3→4→5 vyhrála nad křížovým vzorem
z oborového tisku měřitelně (Levenshteinova vzdálenost 0,377 vs 0,523, t(24)=−6,62, p<0,0001)
a 13 z 25 lidí (52 %) mělo prvních pět fixací identických. Zlatý trojúhelník sám za sebou žádné
měření nemá, jen okruh vzájemných citací v oborovém tisku.
**TŘÍDA:** A pro knižní vzor. Tvrzení "zlatý trojúhelník je změřený" je C a **aktivně vyvrácené**.
**ZDROJ:** Yang, S. S. (2012), International Journal of Hospitality Management 31(3), 1021-1029,
N=27 rekrutovaných / 25 analyzovaných, eye tracker 60 fps, dvoustránkové papírové menu, plný text
čten. Yang v úvodu trasuje původ oborové konvence a uzavírá: "its pattern has not been empirically
validated nor has its underlying reasoning been explained." Nezávisle totéž konstatují Dayan
a Bar-Hillel (2011): "These recommendations, however, were never backed by research, and none, to
the best of our knowledge, exists."
**KDY NEPLATÍ:** Studie měřila pohyb očí, **ne nákupní chování**, a autorka sama upozorňuje, že
není jasné, jestli je delší fixace příčina nebo následek volby. Testovaný byl jediný formát
(dvoustránkové papírové menu), takže na scrollovaný web ani na jednosloupcový mobilní výpis se to
přenáší jako odhad. Stabilita mezi lidmi navíc vychází slabě: plná sekvence byla u každého unikátní,
shoda se objevuje až při zkrácení na šest a méně fixací.

### Kraj kategorie je exponované místo, ale nepřepočítávej to na procenta prodeje

**PRAVIDLO:** Když je potřeba položku zvýraznit, dej ji na začátek nebo konec seznamu v kategorii,
ne do středu. Nikdy z toho ale klientovi neslibuj konkrétní nárůst prodeje.
**KDY PLATÍ:** Řazení položek uvnitř kategorie menu.
**PROČ:** V laboratorním i provozním testu se položky z krajů kategorie objednávaly častěji než ze
středu: 56 % vs 44 % (p<0,001) při 904 pozorováních v lab podmínkách a 55 % (p<0,05) na reálných
objednávkách v kavárně. Efekt přežívá i v novějších a robustnějších designech, ale mění cíl:
v předregistrovaném field experimentu v univerzitní kantýně (7 968 prodejů, 50 dní) snížilo umístění
vegetariánské volby nahoru podíl masitých jídel o 5,3 až 7,2 procentního bodu, ale **podíl
vegetariánských jídel se signifikantně nezvýšil**. A ve field experimentu, kde se přehodil obsah
celých stran menu, se neprojevilo nic.
**TŘÍDA:** A pro existenci efektu, C pro jakoukoli konkrétní velikost u konkrétní položky.
**ZDROJ:** Dayan & Bar-Hillel (2011), Judgment and Decision Making 6(4), 333-342, open access, plný
text čten (studie 1: N=240, 4 verze menu, bez cen, 904 pozorování; studie 2: kavárna v Tel Avivu,
~950 objednávek, 15+15 dní). Replikace a protievidence: Bianchi et al. (2023), Int J Behav Nutr Phys
Act 20:60, pětiramenný RCT, N=9 003, simulovaná delivery platforma; Andersson & Nelander (2021),
Games 12(1):2, předregistrovaný field experiment; Kincaid & Corsun (2003), IJCHM 15(4), 226-231,
nulový výsledek ("The data revealed no significant differences in item sales from time 1 to time 2");
Bucher et al. (2016), Br J Nutr 115(12), systematický přehled 18 studií, kde meta-analýza nešla:
"It was not possible to quantify and directly compare the effect sizes."
**KDY NEPLATÍ:** Autoři sami nemají vysvětlení mechanismu ("We cannot offer a satisfying
explanation") a upozorňují, že směr efektu je opačný než ve zbytku literatury o pozičních efektech,
kde obvykle vyhrává střed. Formulace z abstraktu "až dvakrát populárnější" je maximum jedné položky,
ne průměr, a v sekundárních zdrojích se přebírá jako průměr. Nepoužívej ji.

### Nezkracuj menu na sedm položek kvůli paradoxu volby

**PRAVIDLO:** Počet položek v kategorii řeš podle provozu a kuchyně, ne podle "sedmi položek" nebo
"paradoxu volby". Když klient chce menu zkrátit, ať to má jiný důvod (skladové zásoby, konzistence,
rychlost výdeje).
**KDY PLATÍ:** Každá diskuse o délce menu odůvodněná kognitivní zátěží.
**PROČ:** Metaanalýza 63 podmínek z 50 experimentů, N=5 036, našla pro choice overload efekt
prakticky nulový: d=0,02, 95% CI −0,09 až 0,12, se závěrem "The overall effect size in the
meta-analysis was virtually zero". Dostatečné podmínky, kdy k zahlcení dojde, se identifikovat
nepodařilo. Heuristika "7 položek" navíc bývá odvozená z Millerova 7±2, což je práce o rozsahu
pracovní paměti, nikoli o volbě z viditelného seznamu. Z vytištěného menu si člověk pamatovat nic
nemusí, a přesně tenhle argument vznášejí i Yang (2012) a Dayan s Bar-Hillelem.
**TŘÍDA:** A pro nulový efekt choice overload. "7 položek na kategorii" je C, primární měření
NENALEZENO.
**ZDROJ:** Scheibehenne, Greifeneder, Todd (2010), Journal of Consumer Research 37(3), 409-425,
63 podmínek z 50 publikovaných i nepublikovaných experimentů, plný text čten. K Millerovi
a k jeho zneužívání viz opravný callout v [ux-laws.md](../zakony-principy/ux-laws.md).
**KDY NEPLATÍ:** Mezistudiová variance v metaanalýze reálná je (τ²=0,12), takže tvrzení není "delší
menu je vždy stejně dobré", ale "krátit menu kvůli zahlcení nemá oporu". A není to argument proti
kategorizaci: struktura a hierarchie jsou o něčem jiném než o počtu položek.

### Fotka pomáhá jen u jednoznačně pojmenovaného jídla

**PRAVIDLO:** Fotografii dávej k položkám s běžným popisným názvem. U autorských, cizojazyčných
nebo nejednoznačných názvů ji dávej jen tehdy, když z ní jde poznat, co to je. Nedoplňuj fotku
mechanicky ke všemu.
**KDY PLATÍ:** Menu s fotkami, na webu i na tiskovině.
**PROČ:** Fotka u položky zvyšuje postoj, ochotu platit a nákupní záměr, ale jen u běžných popisných
názvů. U nejednoznačných názvů to platí jen pro část populace, a **lidé s vizuálním kognitivním
stylem hodnotili nejednoznačně pojmenované jídlo S fotkou horší než bez fotky.** Fotka tedy není
monotónně pozitivní prvek. K tomu platí diskont z pravidla výše: dimenze popisu položky včetně
vizuální informace vyšla v metaanalýze na skutečný nákup nesignifikantně.
**TŘÍDA:** A pro směr efektu. Velikost efektu NEOVĚŘENA a neuvádí se.
**ZDROJ:** Hou, Yang, Sun (2017), International Journal of Hospitality Management 60, 94-103,
DOI 10.1016/j.ijhm.2016.10.008, primární experimenty (interakce fotka × typ názvu × styl zpracování
informací). Abstrakt ověřen ze dvou zdrojů, citace ověřena přes Crossref, **plný text nezískán
(403), takže N ani velikosti efektu neuvádět**.
**KDY NEPLATÍ:** Na destinačním konci osy, kde je součástí positioningu menu bez fotek. Pro tvrzení
"čím dražší podnik, tím méně fotek" žádné měření neexistuje, je to pozorování odvětvové konvence.

### Profesionální estetika bije UGC estetiku, když je cílem rezervace

**PRAVIDLO:** Když má fotografie vést k rezervaci nebo návštěvě, plať profesionální. UGC nebo
instagramový styl neobhajuj tím, že je "autentičtější a proto přesvědčivější". Když UGC použít
chceš, obklop ho pozitivními recenzemi a větším počtem profesionálních snímků.
**KDY PLATÍ:** Volba fotografického vstupu do webu a na profily.
**PROČ:** Ve čtyřech kontrolovaných experimentech (celkem N=1 282) činila profesionální estetika
destinaci vizuálně přitažlivější a to zvyšovalo booking intentions, proti amatérské estetice.
Negativní efekt amatérské estetiky se zmírňoval u rizikově averzních zákazníků, v přítomnosti
pozitivních recenzí a při větším počtu profesionálních fotek. Nejcitovanější studie o zákaznických
fotkách, která se používá jako protiargument, **profesionální fotografii vůbec nesrovnává** (je to
korelační dotazník, N=980), takže z ní nejde tvrdit, že UGC vyhrává.
**TŘÍDA:** A ve své doméně (recenzní weby a turismus), B jako přenos na gastro.
**ZDROJ:** Marder, Erz, Angell, Plangger (2021), Journal of Travel Research 60(1), 31-46,
DOI 10.1177/0047287519895125, čtyři experimenty, N=1 282, abstrakt ověřen ze dvou nezávislých
zdrojů. **Plný text nezískán (403), takže N per experiment a zda byly ve stimulech i fotky jídla je
NEOVĚŘENO.** Protistrana: Safeer, Abrar, Zhou (2025), PLOS One, N=980, korelační dotazník bez
srovnávací skupiny.
**KDY NEPLATÍ:** Doména studie je ubytování a recenzní weby, ne jídlo. Přímý experiment srovnávající
UGC a profesionální fotografii na jídle nebo restauraci NENALEZEN. A pravidlo je o estetické úrovni,
ne o tom, kdo držel foťák: dobře nasvícená fotka od majitele je profesionální estetika.

### Pozadí soutěží s jídlem o pozornost, není aditivní

**PRAVIDLO:** Na produktové fotografii jídla drž pozadí a dressing tiché. Když chceš atmosféru,
udělej z ní samostatný snímek, ne kulisu k jídlu. A nesázej dlouhou galerii podobných záběrů téhož.
**KDY PLATÍ:** Fotografická direkce pro menu, homepage a sociální sítě.
**PROČ:** V eye-trackingu bez zadaného úkolu platilo, že čím komplexnější a salientnější prostírání
a dekorace v pozadí, tím **menší** vizuální pozornost dostalo samotné jídlo. Ambientní dressing tedy
není přičítání, je to soutěž. Druhá vrstva: opakované prohlížení a hodnocení obrázků jídla vyvolá
nasycení a **snižuje** chuť na podobná jídla, protože zvažování jídla spouští spontánní simulaci
chuti a ta sama k nasycení stačí. "Víc food pornu = víc chuti" tedy není monotónní.
**TŘÍDA:** A pro směr obou efektů. Čísla neuvádět, primární texty nezískány.
**ZDROJ:** Zhang & Seo (2015), Food Quality and Preference 41, 172-179,
DOI 10.1016/j.foodqual.2014.12.004, primární eye-tracking, free-viewing; citace a nález ověřeny,
**primární text neviděn, N NEOVĚŘENO**. Larson, Redden, Elder (2014), Journal of Consumer Psychology
24(2), 188-194, primární experimenty, abstrakt ověřen, **plný text neviděn**. Kontext: Spence,
Okajima, Cheok, Petit, Michel (2016), Brain and Cognition 110, 53-63, je **REVIEW, ne měření**, plný
text čten, a zvýšenou salivaci z obrazů jídla podmiňuje: "at least if the food images are combined
with other food-related sensory cues".
**KDY NEPLATÍ:** Na destinačním konci osy je atmosférická fotografie často hlavní obsah a pravidlo
se na ni nevztahuje, protože tam jídlo o pozornost soutěžit nemá. Kontrolované srovnání ambientní
proti produktové fotografii, a už vůbec ne segmentované podle cenové hladiny, NENALEZENO.

### Kalorie u anglického klienta patří i na web

**PRAVIDLO:** Když klient provozuje stravovací zařízení v Anglii a má 250 a více zaměstnanců, musí
být energetická hodnota v kcal u položky nejen na fyzickém menu, ale i tam, kde se jídlo nabízí na
webu nebo v mobilní aplikaci, jako součást popisu položky. Zahrň to do návrhu položky menu od
začátku, ne jako dodatek.
**KDY PLATÍ:** Anglie, 250+ zaměstnanců. Ne EU, ne Česko.
**PROČ:** Regulace to výslovně vztahuje na weby a aplikace, ne jen na tiskoviny: reg. 5 odst. 1
písm. b) ukládá poskytnout informaci k zobrazení, když je jídlo nabízeno "on a website or through
a mobile application", a reg. 6 odst. 2 žádá zobrazení "as part of the description of each item of
food". Prakticky to mění vzhled řádku menu: k názvu, popisu a ceně přibývá čtvrtý údaj, který se
nedá schovat do detailu.
**TŘÍDA:** B (regulace).
**ZDROJ:** The Calorie Labelling (Out of Home Sector) (England) Regulations 2021, SI 2021/909,
reg. 1 odst. 3 (účinnost 6. 4. 2022), reg. 4 odst. 2 písm. c) (výjimka pro nápoje nad 1,2 %
alkoholu), reg. 5 odst. 1 písm. b), reg. 6 odst. 2, reg. 7 odst. 1 (práh 250 zaměstnanců). Znění
ověřeno proti legislation.gov.uk.
**KDY NEPLATÍ:** V EU ani v Česku obdobná povinnost pro nebalené pokrmy není, tam je povinný jediný
údaj a to alergeny. Nápoje nad 1,2 % alkoholu jsou vyjmuté i v Anglii. Pod 250 zaměstnanců je to
dobrovolné.

### Obsah reklamy na alkohol omezuje zákon, ne vkus

**PRAVIDLO:** U barového a nápojového webu nepiš a nefoť: nabádání k nestřídmosti, ironizování
abstinence, spojení alkoholu s výkonem nebo řízením, spojení se společenským nebo sexuálním
úspěchem, léčivé či povzbuzující účinky, a nezdůrazňuj obsah alkoholu jako přednost. Nepoužívej
vizuální prvky ani motivy oslovující lidi pod 18 let.
**KDY PLATÍ:** Web, sociální sítě a kampaňové materiály barů, pivovarů a nápojových značek v ČR.
**PROČ:** Není to etiketa, ale zákonný výčet zakázaných obsahů reklamy na alkoholické nápoje.
Dopadá přímo na copy a na volbu fotografie, tedy na věci, o kterých rozhoduje designér, ne právník.
Nejčastější reálná kolize je "spojení se společenským úspěchem", protože přesně to většina barové
fotografie dělá.
**TŘÍDA:** B (regulace).
**ZDROJ:** § 4 zákona č. 40/1995 Sb., o regulaci reklamy. **Verbatim primární znění NEZÍSKÁNO**
(e-Sbírka i zakonyprolidi.cz nedostupné pro automatický fetch, esipa za registrací). Substance
ověřena u dvou nezávislých zdrojů, které paragraf reprodukují shodně. Před ostrým klientským
závazkem si znění dohledej v e-Sbírce.
**KDY NEPLATÍ:** Zákon nevyžaduje elektronické ověření věku (age gate) pro samotnou reklamu, takže
ho nestav jako povinnost. Vlastní pravidla má prodej alkoholu na dálku, ta jsou jinde než v zákoně
o reklamě a tahle nota je nepokrývá.

### V rezervačním formuláři patří newsletter zvlášť a nezaškrtnutý

**PRAVIDLO:** Rezervační formulář drž na nezbytných polích (jméno, počet osob, čas, jeden kontakt).
Souhlas s marketingem dej jako oddělený, nepředzaškrtnutý prvek, ne jako součást obecných podmínek,
a nabídni stejně snadné odvolání.
**KDY PLATÍ:** Každý rezervační a objednávkový formulář v EU.
**PROČ:** Rezervační data jdou pod plnění smlouvy, ale jen ta nezbytná: "your organisation cannot
proceed with the execution of the contract or service without the personal data in question." Na
marketing se ten základ nevztahuje: "this legal basis does not apply... if you wish to process an
individual's personal data for marketing purposes, fraud prevention, targeted advertising or any
other purposes related to your organisation's business model." Souhlas musí být "a clear affirmative
action (without pre-ticked boxes and made separately from applicable general conditions)"
a odvolatelný "as easily as it was to provide it". Předzaškrtnuté políčko je tedy dark pattern
a zároveň porušení.
**TŘÍDA:** B pro citované vodítko, C pro konkrétní layout formuláře.
**ZDROJ:** EDPB, SME Data Protection Guide, sekce Process personal data lawfully, verbatim citace
ověřeny. Gastro-specifické vodítko od EDPB, ICO ani národního DPA NENALEZENO, tohle je aplikace
obecného pravidla. K formulářům obecně viz
[formulare-a-stavy.md](../pravidla/formulare-a-stavy.md), k dark patterns
[etika-v-ux.md](../ux-zaklady/etika-v-ux.md).
**KDY NEPLATÍ:** Publikovaná konvence ani měření pro samotný rezervační flow (počet kroků, kdy si
říct o telefon versus mail, co má být v potvrzení) NEEXISTUJE. Prošly se Baymard, NN/g, GOV.UK
Design System, USWDS a Carbon, žádný booking pattern tam není. Jakékoli konkrétní doporučení
v tomhle je C. Obecná opora pro kvalitu formuláře je Seckler, Heinz, Bargas-Avila, Opwis, Tuch
(2014), CHI '14, 1275-1284, kontrolovaný eye-tracking, N=65, ale je generická, ne gastro.

---

## Co v tomhle sektoru NENÍ

Seznam je stejně důležitý jako pravidla. V gastru dvojnásob, protože tady se nejen tradují nedoložené
konvence, ale **kolují i citace studií, které vůbec neexistují**:

| Tvrzení | Stav |
|---|---|
| "Parsa & Njite (2014), IJCHM 26(7), 1056-1076, 271 menu, price anchoring zvedl účet o 6,8 %" | **FABRIKACE.** Obsah daného čísla IJCHM vytažen z Emeraldu, sedm položek, žádný takový článek. Šíří to AI-generovaný SEO obsah |
| "Yue, Tong & Prinyawiwatkul (2019), fotky v menu a vnímaná kvalita" | **FABRIKACE.** Crossref 0 výsledků, OpenAlex u reálného autora Prinyawiwatkula nic o fotkách v menu |
| Zlatý trojúhelník / sweet spot v menu | konvence oborového tisku bez měření, **aktivně vyvrácená** eye-trackingem (Yang 2012) |
| Price anchoring v menu (drahá položka nahoře zvedá útratu) | primární měření v restauračním kontextu NENALEZENO |
| "Foto u položky = +30 % prodeje" | konzultantské tvrzení bez metodiky, N ani kontrolní podmínky. Třída C |
| "7 položek na kategorii" | primární měření NENALEZENO, a choice overload má metaanalyticky d=0,02 |
| "PDF zhoršuje použitelnost o 300 %" | Nielsenův **vlastní** "rough estimate, based on watching users" z roku 2001, bez N a metodiky. Není to měření |
| "Menu v PDF Google neindexuje" | **NEPRAVDA.** PDF je na Googlově seznamu indexovatelných typů, crawluje 64 MB, u obrázků OCR |
| "PDF nemůže být přístupné" | nepřesné, PDF/UA (ISO 14289-1:2014) existuje. Přesně: v praxi tagované není a fixní layout naráží na reflow |
| Dark patterns v delivery appkách podle Di Geronimo et al. (CHI 2020, 95 %, 1 787 nálezů, 7,4 na appku) | **CHYBNÉ PŘIŘAZENÍ.** Korpus 240 appek obsahoval Photography, Family, Shopping, Social, Music and Audio, Entertainment a Communication. **Žádnou food, drink ani delivery kategorii.** V gastro textech se to cituje běžně a je to špatně |
| "80 % lidí jde na lokální podnik přímo přes vyhledávač nebo mapy" | měřeno na úkolu najít pobočku **vlastní banky**, ne restauraci, a NN/g pro ten podnález neuvádí N |
| "77 % hostů navštíví web před jídlem, 68 % web odradil" | marketingový průzkum agentury, která prodává gastro marketing, a **filtr vzorku obsahuje jen lidi, kteří web navštívit chtějí**. Sampling bias zabudovaný v definici vzorku |
| Prevalence PDF nebo obrázkových menu na gastro webech | žádná studie ani vendor report to nekvantifikuje. NENALEZENO |
| Měření vztahu mezi cenovou hladinou podniku a přítomností fotek v menu | NENALEZENO |
| Kontrolované srovnání ambientní proti produktové fotografii jídla | NENALEZENO |
| Restauračně specifická usability studie od NN/g | NEEXISTUJE. Jediný restaurační článek je metafora bez dat |
| Publikovaný rezervační pattern v design systému | NEEXISTUJE (GOV.UK, USWDS, Carbon, Baymard) |
| Ověřitelný zdroj pro "gastro vyhledávání je převážně mobilní" | NENALEZENO. Všechna kolující čísla vedou na vendor blogy nebo na studii z roku 2012 zaplacenou prodejci mobilní reklamy |

**Zvláštní varování k celé "food and menu psychology" literatuře.** Velká část populárního obsahu
v téhle oblasti stojí na Cornell Food and Brand Lab a jeho vedoucím, u kterého Cornell shledal
vědecké pochybení a který má 18 stažených článků. Žádná studie citovaná v téhle notě na něm nestojí,
ověřeno. Ale kdo notu rozšiřuje, ať u každého "menu psychology" nálezu zkontroluje autora
a retrakce. Konkrétní stažený článek o popisných názvech jídel se dohledat nepodařilo, takže tvrzení
"popisný název jídla zvedne prodej" **není** označené jako stažené, jen jako nedohledané v primárním
textu.

**Baymard pro gastro existuje, ale platí stejné pravidlo jako u e-commerce.** Má dedikovanou linii
Food Delivery & Takeout a benchmark osmi mobilních webů a appek, moderované think-aloud
a eye-tracking, což je skutečné měření. Benchmark skóre je ale expertní bodování proti vlastním
guidelines, ne experiment, a Baymard sám na třech svých stránkách udává pro tentýž benchmark tři
různé počty guidelines (320+, 398, 420+). Detail v [e-commerce notě](e-commerce.md).

Nepřenášej sem ani sektorová čísla o kredibilitě z [financí](finance.md) nebo
[zdravotnictví](zdravotnictvi.md). Gastro v tom datasetu není.

## Neověřené a k dohledání příště

Tohle se v průzkumu (7/2026) otevřelo, ale **nedoověřilo do stavu, kdy z toho jde napsat pravidlo**.
Záměrně tu není pravidlo nastojato, jen zápis, kde se má příště začít.

- **Formát ceny v menu ($ symbol, zaokrouhlení, .99).** Existuje relevantní studie: Yang, Kimes,
  Sessarego (2009), International Journal of Hospitality Management 28(1), 157-160, obědové účty
  v St. Andrew's Café (Culinary Institute of America), tři formáty ($00.00, 00, slovy). Podle
  abstraktu a sekundárních zdrojů byly monetární signály ($ nebo slovo "dollars") spojené s **nižšími**
  výdaji než čistě číselný formát, mezi číselným a slovním rozdíl nebyl, a prezentace ceny celkově
  **nebyla signifikantním prediktorem** v tomhle upscale prostředí. To jde proti populární radě
  "odstraň dolarový symbol a lidé utratí víc". **Plný text NEOVĚŘEN**, N a velikosti efektu neznámé,
  pravidlo se z toho zatím psát nemá. Nedohledal se ani žádný gastro-specifický výzkum k zakončení
  ceny na .99 versus zaokrouhlení, ani k rozdílu mezi fine dining a fast casual v cenové prezentaci.
- **Kotvení ceny v menu.** Primární měření NENALEZENO, viz tabulka výše a fabrikovaná citace.
- **Zarovnání ceny a leader dots** (tvrzení, že cena na pravém okraji s tečkovanou linkou vede
  k porovnávání podle ceny a nižší útratě). Nedohledáno, pravděpodobně konzultantská rada.
- **Menu bez cen a degustační menu s jednou cenou.** Nehledáno do hloubky.
- **Prevalence PDF a obrázkových menu na českých gastro webech.** Nikdo to nemeasuruje. Levný
  vlastní krok: audit vzorku 30 až 50 pražských podniků, zapsat datum a metodu, uložit jako
  pozorování třídy C. Stejná metoda jako vizuální audit v [luxury.md](luxury.md).
- **Jestli bezplatná rezervace bez platby zakládá "consumer contract" podle EAA.** Verbatim text
  směrnice to neřeší, judikatura nedohledána.
- **Verbatim znění § 4 zákona č. 40/1995 Sb.** Substance ověřena dvěma nezávislými zdroji, primární
  text ne (e-Sbírka a zakonyprolidi.cz nešly automaticky načíst).

## Souvisí

- [Kontext: luxury](luxury.md), destinační konec osy: whitespace, restraint, potlačený prodejní tlak
- [Kontext: e-commerce](e-commerce.md), jakmile web přijímá objednávku a platbu
- [Kontext: senioři](seniori.md), povinné čtení u delivery a rezervačního rozhraní. Jediná nalezená
  usability studie delivery aplikací (Juliá-Nehme & Rosell, IJHCI, N=12, průměrný věk 70,9) našla
  SUS pod prahem 68 a 22 až 23 bariér na aplikaci, nejvíc u přidání první položky do košíku
- [Kontext: vláda](vlada.md), rozpis regulatorních rámců a WCAG parametrů
- [Kontrast a barva](../pravidla/kontrast-a-barva.md) a [Tlačítka](../pravidla/tlacitka.md),
  konkrétní prahy, které platí i tam, kde EAA nedopadá
- [Photography](../logo-foto/photography.md), obecná práce s fotografií
- [Vizuální craft](../pravidla/vizualni-craft.md), art direction a metoda živé analýzy referencí
- [Etika v UX](../ux-zaklady/etika-v-ux.md), předzaškrtnuté souhlasy a nátlak v objednávkovém flow
