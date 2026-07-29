# Typografie: pravidla s třídou důkazu

Evidence-based vrstva typografie: délka řádku, spacing, škálování textu a hierarchie,
s třídou důkazu u každého pravidla. Otevři, když nastavuješ sazbu textu (šířky sloupců,
line-height, velikosti) nebo když někdo zdůvodňuje typografická rozhodnutí psychologickým
"magickým číslem". Základy anatomie písma drží
[Typography: základy a anatomie](../typography/typography-zaklady-anatomie.md), volbu
písma [Serif a Sans Serif](../typography/serif-a-sans-serif.md) a
[Font pairing](../typography/font-pairing.md). Kontrast textu (4,5:1 a jeho skutečný
původ) drží [Kontrast a barva](kontrast-a-barva.md).

## Třídy důkazu

| Třída | Význam |
|---|---|
| A | doloženo výzkumem, ideálně replikovaným |
| B | publikovaná konvence nebo regulace (zákon, norma, design systém); závazné nebo interoperabilní, ale není to důkaz o percepci |
| C | autorita nebo tradované tvrzení bez dohledatelné opory |

---

### Délka řádku 45 až 75 znaků

**PRAVIDLO:** Drž délku řádku souvislého textu mezi 45 a 75 znaky včetně mezer, ideál
kolem 66; ve vícesloupcové sazbě 40 až 50 znaků. V CSS nejjednodušeji `max-width: 65ch`
na textovém bloku.

**KDY PLATÍ:** Souvislý čtený text: články, dokumentace, delší popisy. Je to jediné tvrdé
měřitelné číslo z knižního typografického kánonu.

**PROČ:** Tradiční mechanismus: příliš krátký řádek nutí oko skákat na nový řádek moc
často a trhá čtení, příliš dlouhý ztěžuje návrat na začátek dalšího řádku. Měřený důkaz
pro konkrétní čísla ale audit nenašel; síla pravidla stojí na nezávislé shodě knižního
kánonu (Bringhurst: 45-75, ideál 66) s webovou praxí (Practical UI: 40-80). Dva zdroje
s různou historií a publikem konvergují na stejném rozsahu, aniž jeden cituje druhého.

**TŘÍDA:** C (autorita/kánon), se vzácnou vlastností nezávislé konvergence. Nevydávat
za změřený práh.

**ZDROJ:** Bringhurst, The Elements of Typographic Style (45-75 znaků, ideál 66;
vícesloupec 40-50) · Practical UI (40-80 znaků).

**KDY NEPLATÍ:** Headliny, UI mikrotexty, tabulky, popisky, kód. A uvnitř rozsahu nikdo
nedoložil, že 66 je měřitelně lepší než 55 nebo 72; ideál ber jako kotvu, ne jako cíl
optimalizace.

---

### Text musí přežít uživatelský override spacingu

**PRAVIDLO:** Stavěj text tak, aby se nic neořízlo, nepřekrylo a neztratilo, když si
uživatel vynutí: line-height 1,5násobek velikosti fontu, mezery za odstavci 2násobek,
letter-spacing 0,12násobek a word-spacing 0,16násobek. Nejlevnější cesta ke splnění:
tělo textu rovnou sázej s line-height minimálně 1,5, nefixuj výšky kontejnerů podle
aktuálního obsahu a nepoužívej ořezávání textu.

**KDY PLATÍ:** WCAG 1.4.12 Text Spacing, úroveň AA, nové ve verzi 2.1. Pozor na přesné
znění: SC nevyžaduje, abys s těmito hodnotami sázel, vyžaduje, aby je design přežil.
Prakticky ale vylučuje layouty závislé na pevném line-height pod 1,5.

**PROČ:** Lidé s dyslexií a slabozrakostí si spacing přenastavují (custom stylesheety,
rozšíření, čtecí nástroje). Design, který se při overridu rozbije nebo ořízne obsah,
jim text reálně odepře, i když "v defaultu vypadá dobře".

**TŘÍDA:** B (regulatorní/normativní).

**ZDROJ:** W3C, Understanding SC 1.4.12, https://www.w3.org/WAI/WCAG21/Understanding/text-spacing.html

**KDY NEPLATÍ:** Jazyky a písma, kde některá z vlastností neexistuje (výjimka přímo v SC,
např. letter-spacing v CJK písmech funguje jinak). Hodnoty 1,5/2/0,12/0,16 jsou testovací
minima pro override, ne estetické doporučení pro každý text: display headliny snesou
i těsnější sazbu, pokud override přežijí.

---

### Text musí jít zvětšit na 200 %

**PRAVIDLO:** Veškerý text musí jít zvětšit na 200 % bez ztráty obsahu a funkce.
Testuj zoomem prohlížeče na 200 %: nic se nesmí oříznout, překrýt ani zmizet a všechno
musí zůstat ovladatelné.

**KDY PLATÍ:** WCAG 1.4.4 Resize Text, úroveň AA, od verze 2.0. Souvisí s 1.4.10 Reflow
(AA, 2.1): obsah bez horizontálního scrollu při šířce 320 CSS px, což je zhruba totéž
co 200% zoom na běžném desktopu.

**PROČ:** Slabozrací uživatelé zvětšují text jako první pomoc, ještě před asistivními
technologiemi. Pevné pixelové výšky, `overflow: hidden` na textových kontejnerech
a layouty spoléhající na přesnou délku textu obsah při zvětšení ořežou.

**TŘÍDA:** B (regulatorní/normativní).

**ZDROJ:** W3C, Understanding SC 1.4.4, https://www.w3.org/WAI/WCAG21/Understanding/resize-text.html

**KDY NEPLATÍ:** Titulky ve videu a text v obrázcích (výjimka přímo v SC; text v obrázcích
je ale problém sám o sobě a řeší ho jiná kritéria).

---

### Hierarchii neomezuje žádné magické číslo

**PRAVIDLO:** Počet úrovní nadpisů a rozsah viditelné hierarchie odvozuj ze struktury
obsahu, ne z psychologických limitů paměti. Nikdy nezdůvodňuj "max 7±2 položek nebo
úrovní" Millerem ani "max 4" Cowanem; je to stejný typ chyby jako u menu, jen přenesený
na typografii.

**KDY PLATÍ:** Viditelná typografická hierarchie: úrovně nadpisů, navigace, seznamy,
obsahy dokumentů. Cokoliv, co zůstává na obrazovce, když se uživatel rozhoduje.

**PROČ:** Millerova sedmička je limit vybavování bez podnětu na jedné percepční dimenzi.
Text z roku 1956 navíc není experiment, je to přednáška bez vlastního vzorku, a Miller
sám číslo 7 nazval "pernicious, Pythagorean coincidence". Cowan (2001, ~4 chunky) přímo
vyjmenovává podmínky, za kterých je limit měřitelný: zablokované opakování a podnět
nedostupný při vybavování. Viditelná stránka porušuje obě: čtení hierarchie je rekognice
s trvalou oporou, ne recall. Misapplikaci na menu vyvrací i NN/g ("It's a common
misconception that limited short-term memory implies that menus should be similarly
limited to 7 items."). Co evidence skutečně podporuje: šířka před hloubkou (uživatelé
efektivně zvládají kolem 16 neseskupených top-level odkazů; shrnutí HFI 2003 nad studiemi
Snowberry 1983, Kiger 1984, Larson & Czerwinski 1998) a limit 3 až 5 chunků tam, kde
člověk nese informaci MEZI kroky bez opory na displeji (wizardy, opisování kódů,
srovnávání mezi taby).

**TŘÍDA:** Varování samo je třída A (audit primárních textů); pravidlo "max 7 úrovní
kvůli Millerovi" je třída C.

**ZDROJ:** Miller (1956), plný text: http://psychclassics.yorku.ca/Miller/
· Cowan (2001), Behavioral and Brain Sciences 24(1), DOI 10.1017/S0140525X01003922
· Nielsen (2009), https://www.nngroup.com/articles/short-term-memory-and-web-usability/
· Tufte, https://www.edwardtufte.com/notebook/the-magical-number-seven-plus-or-minus-two-not-relevant-for-design/
· HFI newsletter 4/2003 (Straub, Weinschenk).

**KDY NEPLATÍ:** Paměťový limit se vrací v okamžiku, kdy hierarchie z obrazovky zmizí:
když si uživatel má zapamatovat, kde v hloubce struktury je, nebo přenést hodnoty do
dalšího kroku, počítej s 3 až 5 chunky a strukturu zploštěj nebo mu ji připomínej
(breadcrumbs, shrnutí).

Pozn.: [UX Laws](../zakony-principy/ux-laws.md) zatím uvádí populární verzi Millera
(5-9 položek v chuncích menu). Tahle nota je korekce; ux-laws čeká na přepis.

---

### Škála velikostí je nástroj konzistence, ne percepční zákon

**PRAVIDLO:** Definuj škálu velikostí a řezů předem (např. 12/14/16/20/24/32/48 px)
a vybírej jen z ní; ad hoc mezihodnoty nezaváděj. Hierarchii signalizuj kombinací
velikosti, řezu (weight) a barvy, ne jen velikostí.

**KDY PLATÍ:** Každé UI a každý dokument s víc než jednou úrovní textu. Čím víc lidí
a obrazovek, tím víc se škála vyplácí.

**PROČ:** Mechanismus je konzistence, ne percepce: škála snižuje počet arbitrárních
rozhodnutí, dělá stejné úrovně stejně vypadajícími napříč obrazovkami a hierarchii
rozpoznatelnou bez čtení. Poctivě: audit nenašel žádnou studii, která by určovala
konkrétní poměr škály; volba 1,25 vs 1,333 vs "zlatý řez" je vkus a rytmus, ne evidence.
Hodnotu má disciplína držet se jakékoliv rozumné škály, ne konkrétní čísla.

**TŘÍDA:** C (autorita a praxe design systémů: Refactoring UI, publikované type scales).

**ZDROJ:** Wathan & Schoger, Refactoring UI (definované škály; hierarchie přes weight
a barvu, ne jen velikost).

**KDY NEPLATÍ:** Škála není percepční tvrzení a nemá vlastní hodnotu: když obsah
opakovaně potřebuje mezistupeň, uprav škálu (změna systému), nedávej výjimku jednomu
místu. A škála sama hierarchii nezaručí, když se úrovně liší o jeden stupeň, který
na obrazovce není rozeznatelný.

---

### Minimální velikosti pro děti a seniory

**PRAVIDLO:** Pro děti 3-8 let používej text minimálně 14 pt (pro začínající čtenáře
vyšlo nejlépe bezpatkové písmo kolem 18 pt), pro děti 9-12 let minimálně 12 pt.
Pro seniory drž text minimálně 12 pt a přidávej rezervu v kontrastu a velikosti cílů
nad rámec minim.

**KDY PLATÍ:** Produkty cílené na tyto skupiny, nebo s významným podílem takových
uživatelů. Věkové pásmo dětí segmentuj (3-5 / 6-8 / 9-12), rozdíly mezi pásmy jsou
podle výzkumu velké.

**PROČ:** Empirie NN/g: výzkum s dětmi (N=125, tři vlny) a se seniory (N=75, 65-89 let,
proti kontrole N=20): úspěšnost úkolů 55,3 % vs 74,5 %, o 43 % pomalejší postup, chyby
2,4 vs 1,1. U publika, které pracuje s takovou penalizací, se rezerva nad regulatorní
minima vyplatí dvojnásob.

**TŘÍDA:** A s výhradou: empirický výzkum NN/g je vlastní, nerecenzovaný (self-published).

**ZDROJ:** NN/g, výzkum Children's UX (125 dětí, tři vlny) · NN/g, výzkum použitelnosti
pro seniory (N=75 vs kontrola 20).

**KDY NEPLATÍ:** Obecná populace; čísla jsou minima pro specifické skupiny, ne horní
hranice pro ostatní. A samotná velikost nestačí: u seniorů jde ruku v ruce s kontrastem
(viz [Kontrast a barva](kontrast-a-barva.md)) a velikostí cílů.
