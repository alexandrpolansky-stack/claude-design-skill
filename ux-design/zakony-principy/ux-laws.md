# UX zákony

Fitts, Hick, Jakob, Miller, Tesler, Postel, Parkinson a Gestalt, včetně opravy tří populárních verzí.

Související: [Kognitivní efekty](efekty.md) · [Principy a heuristiky](principy-a-pravidla.md) · [Obecná UX znalost](../ux-zaklady/general-ux-knowledge.md)

## **Fittsův zákon** (Fitts Law)

> [!important] Popularizovaná verze tohoto zákona je nepřesná
> Fitts 1954 (J. Exp. Psychol. 47(6), 381-391, DOI 10.1037/h0055392) měřil **1D amplitudovou
> úlohu se stylusem na plechových terčích**, N = 52 studentů. Ne obrazovku, ne prst. Jádro
> zákona (kompromis rychlost/přesnost, vzdálenost a velikost cíle) platí, tři běžně citované
> důsledky ale ne:
>
> 1. **U 2D terče rozhoduje MENŠÍ z rozměrů, ne šířka.** MacKenzie & Buxton, CHI '92
>    (N = 12, 1170 trialů na subjekt) porovnali modely: status quo (horizontální W) r = .8097,
>    W' podél approach vektoru r = .9333, **SMALLER-OF (menší z W a H) r = .9501**, p < .001.
>    Verbatim: "a clear refutation of applying the status quo model". U tlačítka 200x24 px je
>    relevantní rozměr 24, ne 200. Rozšiřovat široké tlačítko dál do strany je podle
>    SMALLER-OF bezcenné.
> 2. **U prstu existuje absolutní podlaha přesnosti.** Bi, Li, Zhai, FFitts law, CHI 2013
>    (N = 12, R² >= 0,91): Fitts "has been insufficient in modeling small-target acquisition
>    with finger-touch". Rozptyl je součet relativní přesnosti (speed-accuracy) a **absolutní
>    přesnosti prstu, která je nezávislá na rychlosti**. Pod určitou velikost terče chybu
>    nejde vykoupit zpomalením, jediný fix je zvětšit terč.
> 3. **"Větší tlačítko = méně chyb" z Fittse nevyplývá.** Fitts modeluje ČAS při předpokládané
>    konstantní chybovosti (~4 %), samotnou chybovost nepredikuje. Jeho data: 1,2-1,3 % chyb
>    celkově, 3,6-4,1 % v nejtěžší podmínce, instrukce účastníkům byla "Emphasize accuracy
>    rather than speed."
>
> Navíc Fitts netestoval dnes citovanou lineární formu `MT = a + b·ID`. Testoval konstantní Ip
> a připouští "even though the index is not precisely constant, the hypothesis is substantially
> confirmed". Lineární forma s interceptem je pozdější konvence (Welford 1960, MacKenzie 1989).

Definice: Čas potřebný k dosažení cíle závisí na vzdálenosti k cíli a jeho velikosti
	Zkoumá lidskou motoriku
	Jde o kompromis mezi rychlostí a přesností
	**Vzdálenost** - Čím dál je tlačítko od vašeho kurzoru X palce, tím déle trvá než se k němu dostanete
	**Velikost** - Pokud je tlačítko malé, musíte před kliknutím zpomalit, abyste se trefili = vyžaduje vyšší mentální kapacitu
		• **Dobře (reverse):** Proto se tlačítko na zavření reklam používá vpravo nahoře a je malé = větší šance, že člověk klikne na reklamu = dark patterns
		• **Dobře:** Tlačítko je velké a přes celou šířku obrazovky u spodního okraje. Nemusíte mířit. Můžete na něj "plácnout" palcem rychle a bez přemýšlení, protože cíl je tak velký, že ho nelze minout.
		• **Oprava k tomu příkladu (viz callout výše):** o trefu rozhoduje VÝŠKA toho tlačítka, ne to, že je přes celou šířku (SMALLER-OF, MacKenzie & Buxton 1992). Tlačítko 375x28 px se palcem trefuje špatně, i když vypadá jako nepřehlédnutelný pruh. Šířka řeší jen horizontální míření, limit drží ten menší rozměr, a u palce k tomu přibývá podlaha přesnosti, kterou zpomalením neobejdeš.
## **Hickův zákon** (Hicks Law)

> [!important] Popularizovaná verze tohoto zákona je nepřesná
> Hick 1952 (Q. J. Exp. Psychol. 4(1), 11-26, DOI 10.1080/17470215208416600) a Hyman 1953
> (J. Exp. Psychol. 45(3), 188-196, PMID 13052851) modelují **rozhodovací čas po jasném
> vizuálním podnětu**, ne vizuální hledání v menu. Cockburn, Gutwin, Greenberg,
> *A predictive model of menu performance*, CHI 2007 (N = 8) to říkají výslovně: aplikace
> na hledání v menu selhala, protože "**Hick and Hyman's original experiments timed decision
> time in response to clear visual stimuli**". A obecněji: "while Fitts' Law has been robustly
> applied across many experiments, attempts to model behaviour with the Hick-Hyman Law have
> been **less successful**."
>
> **Co platí místo toho:** "there is consistent empirical evidence that **novices' search time
> is LINEAR with menu length**". Pro nováčka a neznámé labely je čas hledání lineární s počtem
> položek (jejich model `Tvs = a + b·n`). Logaritmický Hick-Hyman nastupuje až u **experta**
> s prostorovou pamětí a stabilním layoutem. Landauer & Nachbar 1985, jediná studie, kde
> v menu logaritmické časy vyšly, toho dosáhla tím, že vizuální hledání záměrně eliminovala:
> totálně uspořádané labely (čísla, abecedně) a natrénovaní účastníci.
>
> **Použitelné:** u naučené, prostorově stabilní volby mezi známými alternativami roste
> rozhodovací čas logaritmicky s informačním obsahem. Praktický důsledek je žádné adaptivní
> přeskládávání menu a časté položky na predikovatelné místo; nerovnoměrné frekvence volby
> (Zipf) čas snižují.
> **Nepoužitelné:** "podle Hicka zkrať menu" a "hluboké menu je rychlejší než široké"
> (každá úroveň přidává celý cyklus hledání plus Fittsův pohyb).
>
> Vlastní N ani aparaturu Hicka a Hymana nebylo možné z primárních zdrojů ověřit (paywall),
> takže je necituj. Přehled s výhradami: Proctor & Schneider 2018, QJEP 71(6), 1281-1299.

Definice: Čas potřebný k rozhodnutí se zvyšuje s počtem a složitostí k rozhodnutí
Říká, že člověk má omezené množství paměti (RAM), pokud uživateli předložíte 10 tlačítek, musí každé tlačítko přečíst, porovnat, zanalyzovat (Pouze zjednodušené, musí se brát kontext celé stránky)
	Příklad:
		Dálkový ovladač, staré ovladače k TV měly i 50 tlačítek, najít to správné bylo velmi kognitivně náročné. Čím víc možností člověk má, tím větší je šance, že to vzdá a udělá chybu. **Dnešní Apple TV ovladače** mají už jenom například 5 tlačítek.
		**Oprava (viz callout výše):** formulace "omezené množství paměti (RAM)" plete Hicka s Millerem. Hick-Hyman není o paměti, je to vztah mezi rozhodovacím časem a informačním obsahem volby. Příklad s ovladačem je reálný, ale pomalé ho dělá vizuální HLEDÁNÍ mezi 50 nerozlišenými tlačítky, které roste lineárně s počtem, ne logaritmický rozhodovací čas. Redukce na 5 tlačítek pomáhá, jen z jiného důvodu, než říká Hick.
## **Jakubův zákon** (Jackobs Law)
Definice: Uživatelé tráví většinu času na jiných stránkách, a proto preferují, aby váš web fungoval stejně jako ty, které už znají
	Proto se vyplatí "kopírovat" ostatní weby. Nekopíruj, inspiruj se, zanech základní funkce stejně, aby byly pro uživatele intuitivní.
	Čím méně uživatel přemýšlí tím menší šance, že opustí stránku. Tím se sníží potřeba učit se nové ovládání a uživatel se může soustředit na svůj cíl.
## **Millerův zákon** (Millers Law)

> [!important] Popularizovaná verze tohoto zákona je nepřesná
> **Miller 1956 není experiment.** Je to invited address (footnote 1: "first read as an Invited
> Address before the Eastern Psychological Association in Philadelphia on April 15, 1955")
> a přehled cizích dat. **Vlastní vzorek: žádný.** Plný text: psychclassics.yorku.ca/Miller/
>
> Miller sám o čísle 7, závěrečný odstavec verbatim: "I suspect that it is only a **pernicious,
> Pythagorean coincidence**." A sám zakazuje smíchat tři různé "sedmičky" do jednoho pravidla:
> "What is more natural than to think that all three of these spans are different aspects of
> a single underlying process? **And that is a fundamental mistake**, as I shall be at some
> pains to demonstrate." Rozlišuje: "Absolute judgment is limited by the amount of information.
> Immediate memory is limited by the number of items." Pointa toho papíru je chunking jako
> cesta, jak limit OBEJÍT, ne limit sám (Millerův Smith se dodrilloval na 40 binárních číslic).
>
> **Proč "max 7 položek v UI" neplatí:** Millerův limit je recall bez podnětu na jedné dimenzi
> (tón, jasnost). Menu je rekognice trvale viditelného multidimenzionálního textu. Jiná úloha,
> jiná modalita, jiná závislá proměnná. NN/g (Nielsen 2009) verbatim: "It's a common
> misconception that limited short-term memory implies that menus should be similarly limited
> to 7 items." Tufte k popularizaci: "a conclusion which can be sustained only by **not reading
> the paper**" (edwardtufte.com/notebook/the-magical-number-seven-plus-or-minus-two-not-relevant-for-design/).
>
> **Co evidence reálně podporuje:** HFI newsletter 4/2003 (Straub, Weinschenk): "users find
> roughly **16 (ungrouped) top-level links** leading into 2-3 subsequent menus the most
> efficient, learnable and least error prone." Tedy breadth > depth, širší navigace vyhrává nad
> hlubší. Citované studie: Snowberry/Parkinson/Sission 1983, Kiger 1984, Jacko/Salvendy 1996,
> Larson/Czerwinski 1998, Bernard 2002.
>
> **Kde limit paměti naopak platí:** když uživatel nese informaci MEZI kroky bez opory na
> displeji (multi-step formulář, wizard, SMS kód, srovnávání mezi taby). Tam je použitelné
> číslo 3-5 chunků, ne 7. Cowan 2001 (BBS 24(1), 87-114, DOI 10.1017/S0140525X01003922, taky
> syntéza, ne experiment) uvádí "three to five chunks... **averaging about four chunks**" a sám
> jmenuje hraniční podmínky: musí být zablokováno překódování a rehearsal a podnět nesmí být
> dostupný při výbavnosti. **Viditelné menu porušuje obě podmínky současně.**

• **Definice:** Průměrný člověk dokáže udržet v pracovní paměti pouze 7 +- 2 (okolo 9 tedy) položek
Jak s tím pracovat? V PPF jsme měli menu, kde mohl uživatel vybrat 30 položek, což je nesmysl.
Řešení je položky rozdělit logicky x graficky do bloků do tkzv. chunků, po 5-9 aby se uživatel lépe orientoval.

**Oprava (viz callout výše):** seskupení a chunkování je legitimní technika, ale číslo 5-9 z Millera nevyplývá a na počet trvale viditelných položek se limit neaplikuje. 30 položek v menu není samo sebou "nesmysl", u top-level navigace evidence podporuje spíš širší menu (řádově 16 odkazů) než dělení na sedmičky. Weinschenk, která pravidlo 3-4 v UX rozšířila, ho sama odmítá, verbatim z jejího postu 28.10.2009: "Can you really only have 4 items on a navigation bar? or 4 tabs on a screen... **No, not really. You can have more, as long as you group and chunk.**" Argument pro chunkování je tedy skenovatelnost a struktura, ne kapacita pracovní paměti.
## **Teslerův zákon** (Teslers Law)
• **Definice:** Známý také jako „Zákon zachování složitosti“. Tvrdí, že každý systém má určité množství složitosti, kterou nelze snížit
Tesler přišel s tím, že vývojáři a návrháři by měli strávit více času nad tím, aby aplikaci zjednodušili. Není možné to plně odstranit, spíše přesunout. Aby si uživatel nemusel pamatovat tisíce zkratek a podobně.
Napríklad: Platby Online - dříve jste museli vyplňovat tísíce informací dopředu a online. Nyní funguje služba jako Apple pay, která tuto funkci zjednodušila -> uživatel se může více věnovat jiným okolnostem - vývojáři proces přesunuli na sebe, vyvinuli lepší systém a přesunuli to celé pod kapotu.
- Zajímavou tečku k tomuto zákonu přidává Bruce Tognazzini, který tvrdí, že lidé se přirozeně brání snižování složitosti ve svých životech. Paradoxně to znamená, že když nějakou aplikaci extrémně zjednodušíte a ušetříte lidem čas, uživatelé ji začnou používat k řešení mnohem složitějších úkolů než dříve
## **Postelův zákon** (Postel Law)
• **Definice:** Buďte liberální v tom, co přijímáte, a konzervativní v tom, co odesíláte.
Ať se uživatel může vyjádřit více způsoby, ať je pro něj aplikace/systém co nejvíce intuitivní
Zároveň dejte uživateli jasnou a stabilní zpětnou vazbu - vytvoří návyk, buduje lepší vztah.
## **Parkinsonův zákon** (Parkinson Law)
• **Definice:** Každý úkol nabobtná tak, aby vyplnil veškerý dostupný čas určený k jeho splnění
Jinak řečeno, převedeno na praxi. Pokud máte na úklid bytu celý týden, úklid Vám zabere celý týden, pokud máte na úklid 20 minut, tak Vám zabere 20 minut.
Pokud ale na úplně stejný úkol dostanete šibeniční termín 15 minut, vaše soustředění se okamžitě zvýší, přestanete řešit detaily a úkol stihnete včas. Množství přiděleného času tedy přímo úměrně zvětšuje i vnímanou složitost a zdlouhavost úkolu.

Pokud rozhraní umožní uživateli trávit u nějakého procesu (např. nákup, registrace, vyplňování profilu) zbytečně moc času, uživatel tento čas využije – začne váhat, dělat chyby, nebo se rozptylovat. To je v digitálním prostředí nežádoucí. Designér proto musí využít Parkinsonova zákona ve prospěch uživatele tím, že **čas potřebný k úkolu drasticky zkrátí a omezí**.

Příklady:
• **Automatizace a předvyplňování:** Místo toho, aby uživatel ručně vypisoval město a stát, systém je automaticky doplní po zadání PSČ. Tím se drasticky zkrátí „čas dostupný k vyplnění“ a úkol nemá šanci nabobtnat do zdlouhavé a otravné činnosti.

• **Omezení rozptýlení (tzv. tunelování):** Během placení v e-shopu se často skryje hlavní navigace webu a všechny ostatní odkazy. Pokud by tam zůstaly, úkol (zaplatit) by se časově natáhl, protože uživatel by začal proklikávat jiné kategorie a proces by se zkomplikoval.

• **Omezené časové nabídky:** Typický marketingový tlak (odpočet času v košíku u vstupenek). Uživatel nemá čas hodinu přemýšlet a zvažovat alternativy (čímž by úkol nabobtnal), ale je nucen úkol dokončit okamžitě.

Ve zkratce: Zkrátíte-li a zjednodušíte uživateli cestu tak, aby neměl prostor úkol protahovat, ušetříte mu energii a výrazně zvýšíte šanci, že proces úspěšně dokončí.
## **Gesaltovi zákony** (Zákony vnímání)

• **Zákon blízkosti (Law of Proximity):** Objekty, které jsou blízko sebe, vnímáme jako skupinu. _Využití:_ Umožňuje vizuálně shlukovat související obsah bez nutnosti čar či rámečků!
• **Zákon podobnosti (Law of Similarity):** Podobné prvky vnímáme jako související. _Využití:_ Zajistěte, aby odkazy a navigační prvky byly vizuálně odlišné od textu a konzistentní, uživatel je pak rozpozná jako funkční skupinu
• **Zákon společné oblasti (Law of Common Region):** Prvky uvnitř jasně ohraničené oblasti jsou vnímány jako skupina.
![Zákon blízkosti 1](../_assets/zakon-blizkosti-1.png)
• **Zákon jednotného spojení (Law of Uniform Connectedness):** Prvky vizuálně spojené (např. čarou) jsou vnímány jako příbuznější než ty nespojené![Zákon jednotného spojení](../_assets/zakon-jednotneho-spojeni.png)
• **Zákon pregnantnosti (Law of Prägnanz):** Lidé interpretují složité obrázky co nejjednodušší formou, protože to vyžaduje nejméně kognitivního úsilí. _Využití:_ Design by měl upřednostňovat jednoduchost a řád, aby uživatele nezahltil

---

## Poznámka k přesnosti tří klasických zákonů

Miller, Fitts a Hick jsou výše popsaní tak, jak se běžně učí a citují, protože v té podobě
fungují jako slovník pojmů a domluvíš se s nimi s každým designérem. Kontrola primárních
zdrojů (29.7.2026) ale ukázala, že populární UI aplikace všech tří je posunutá. Opravné
callouty jsou u příslušných sekcí, tady je souhrn:

| Studie | Vlastní vzorek | Typ práce | Platnost populárního UI pravidla |
|---|---|---|---|
| Miller 1956 | žádný | přehled a přednáška | žádná, autor sám číslo 7 nazval koincidencí |
| Cowan 2001 | žádný | BBS syntéza s komentářem | žádná pro viditelné položky, silná pro paměť mezi kroky |
| Fitts 1954 | 52 studentů, 1D stylus | experiment | částečná, 2D a touch potřebují jiný rozměr W, chybovost nepredikuje |
| Hick 1952 / Hyman 1953 | nepotvrzeno | experiment | žádná pro scan neznámého menu, publikovaně vyvráceno |

Praktický dopad na tři nejčastější rozhodnutí:

1. **Kolik položek do navigace.** Neřeš to Millerem. Rozhoduj podle skenovatelnosti
   a struktury; u top-level navigace je širší lepší než hlubší.
2. **Jak velké tlačítko.** Ten menší rozměr, ne šířka. A u dotyku ber velikost jako tvrdé
   minimum, které nejde nahradit tím, že uživatel zpomalí. Konkrétní hodnoty a mantinely jsou
   v [Tlačítka](../pravidla/tlacitka.md).
3. **Jak zkrátit hledání v menu.** Stabilní pozice a rozlišitelné labely, ne mazání položek.

Zdroje (primární a klíčové sekundární):

- Miller, G. A. (1956). *The Magical Number Seven, Plus or Minus Two.* psychclassics.yorku.ca/Miller/
- Cowan, N. (2001). *Behavioral and Brain Sciences* 24(1), 87-114. DOI 10.1017/S0140525X01003922
- Fitts, P. M. (1954). *J. Exp. Psychol.* 47(6), 381-391. DOI 10.1037/h0055392
- MacKenzie, I. S., & Buxton, W. (1992). *Extending Fitts' law to two-dimensional tasks.* CHI '92
- Bi, X., Li, Y., & Zhai, S. (2013). *FFitts law.* CHI 2013
- Hick, W. E. (1952). *Q. J. Exp. Psychol.* 4(1), 11-26. DOI 10.1080/17470215208416600
- Hyman, R. (1953). *J. Exp. Psychol.* 45(3), 188-196. PMID 13052851
- Cockburn, A., Gutwin, C., & Greenberg, S. (2007). *A predictive model of menu performance.* CHI 2007
- Proctor, R. W., & Schneider, D. W. (2018). *QJEP* 71(6), 1281-1299 (přehled s výhradami)
- Straub, K., & Weinschenk, S. (2003). HFI newsletter 4/2003 (breadth vs depth v navigaci)
- Nielsen, J. (2009), nngroup.com; Tufte, E., edwardtufte.com/notebook/the-magical-number-seven-plus-or-minus-two-not-relevant-for-design/

Souvisí: [Efekty](efekty.md) (Aesthetic-Usability Effect má vlastní posun v popularizaci),
[Principy a Pravidla](principy-a-pravidla.md), [Osmibodová mřížka](osmibodova-mrizka.md).