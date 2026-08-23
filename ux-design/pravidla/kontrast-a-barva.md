# Kontrast a barva: pravidla s třídou důkazu

Pravidla pro kontrast, barvu jako nositele informace a sémantiku stavů. Otevři, když
nastavuješ barvy textu a UI prvků, stavové barvy (chyba, varování, úspěch) nebo obhajuješ
kontrastní hodnoty před někým, kdo se ptá "proč zrovna tohle číslo". Každé pravidlo nese
třídu důkazu, protože právě tady se nejvíc lže sebejistotou: čísla vypadají jako věda,
i když jsou to normy a konvence.

Teorii barev a harmonií drží [Color Theory](../color/color-theory.md), poměry palety
[Pravidlo 60-30-10](../color/pravidlo-60-30-10.md), evidence-based typografii
[Typografie](typografie.md). Ukázku konkrétních kontrastních párů má
[Design system DRIVE](../priklady-ds/design-system-drive.md).

## Třídy důkazu

| Třída | Význam |
|---|---|
| A | doloženo výzkumem, ideálně replikovaným |
| B | publikovaná konvence nebo regulace (zákon, norma, design systém); závazné nebo interoperabilní, ale není to důkaz o percepci |
| C | autorita nebo tradované tvrzení bez dohledatelné opory |

## Ironie, kterou si zapamatuj předem

Pravidlo, které vypadá nejtvrději a nejnumeričtěji (kontrast 4,5:1), má SLABŠÍ evidenční
základ než pravidlo, které vypadá jako folklór (aesthetic-usability effect). Poměr 4,5:1
je derivace z norem CRT éry krát faktor bez zdroje. Jádro aesthetic-usability effectu je
naopak replikované studiemi, které ho původně chtěly vyvrátit. Kdo cituje 4,5:1 jako
"vědecky ověřenou hranici čitelnosti", opakuje chybu, kterou dělá i samotná dokumentace
WCAG. Poctivé zařazení: 4,5:1 je regulatorní mantinel (třída B), jádro aesthetic-usability
je empirie (třída A) a jeho populární verze je folklór (třída C). Detaily u obou pravidel níž.

---

### Kontrast textu minimálně 4,5:1

**PRAVIDLO:** Drž kontrast běžného textu proti pozadí minimálně 4,5:1; velký text (od 18 pt
/ 24 px, tučný od 14 pt / ~18,7 px) minimálně 3:1; AAA úroveň je 7:1 (SC 1.4.6). Měř nástrojem
podle vzorce WCAG `(L1 + 0.05) / (L2 + 0.05)`, ne odhadem. A ber to takhle: 4,5:1 používáme
jako regulatorní a interoperabilní baseline, protože je testovatelný, právně ukotvený
a nástrojově podporovaný. Není to percepční práh čitelnosti. U světlého textu na tmavém
pozadí, u tenkých řezů a u malých velikostí ber 4,5:1 jako NEDOSTATEČNOU podmínku a přidej
rezervu. Nikdy netvrď, že jde o vědecky ověřenou hranici.

**KDY PLATÍ:** Veškerý čitelný text (WCAG 1.4.3, úroveň AA, od verze 2.0). Právně vynutitelné:
European Accessibility Act 2019/882 váže od 28.6.2025 i privátní sektor (e-commerce, banking)
přes EN 301 549 ≈ WCAG 2.1 AA; v ČR zákon č. 99/2019 Sb. pro veřejný sektor; v USA Section 508
a ADA Title II.

**PROČ:** Tady pozor, mechanismus je slabší, než jak ho WCAG prezentuje. Derivace podle
Understanding SC 1.4.3: základ 3:1 pochází z ANSI-HFES-100-1988 a ISO 9241-3 (normy z CRT éry),
vynásobený faktorem 1,5 kvůli vizu 20/40 ("A user with 20/40 would thus require a contrast
ratio of 3 * 1.5 = 4.5 to 1"). Faktor 1,5 nemá oporu: WCAG cituje Arditi & Faye (2004), kde
jediný výskyt čísla 1,5 je "intercept of 1.50" regrese log CS na log MAR, tedy intercept,
ne multiplikátor. Bruce Bailey (účastník pracovní skupiny AGWG) to přiznal přímo v issue
w3c/wcag#1705: "I concur that Aries Arditi never suggested 4.5:1" a "It is a rational basis,
just not maybe a great one." Volbu 4,5 místo 5:1 navíc spoluurčila dostupnost šedé trojice
#000/#767676/#fff v 8bitové paletě. A protože ISO 9241-3 definuje uživatele jako "20/40 vision
or better", násobení 1,5 kvůli 20/40 počítá stejnou populaci dvakrát (Somers, tamtéž).
Známé slabiny vzorce: ignoruje prostorovou frekvenci (kromě hrubé výjimky pro velký text)
a polaritu (světlé na tmavém vychází stejně jako tmavé na světlém, i když se čte jinak);
konstanta 0,05 není ve specifikaci nikde vysvětlená. Ignorování hue je naopak vědomé
rozhodnutí s citací (Knoblauch et al. 1991), takže kritika "ignoruje barvu" je nejslabší.
APCA jako navrhovaná náhrada polaritu a velikost modeluje, ale TAKY nemá publikovanou
validaci (w3c/silver#574: "Published citations are decoupled from assertions"); WCAG 3.0
Working Draft ji nezmiňuje. Verdikt je symetrický: obě strany jsou model plus expertní
úsudek, ani jedna není validovaný měřený práh.

**TŘÍDA:** B (regulatorní/normativní). Vydávat za třídu A je přesně ta chyba, proti které
tahle nota existuje.

**ZDROJ:** W3C, Understanding SC 1.4.3, https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html
· forenzní diskuse derivace: https://github.com/w3c/wcag/issues/1705
· APCA validace: https://github.com/w3c/silver/issues/574

**KDY NEPLATÍ:** Logotypy a čistě dekorativní text (výjimka přímo v SC), disabled prvky.
A hlavně neplatí jako záruka: splnění 4,5:1 u tenkého světlého textu na tmavém pozadí
nebo u malých velikostí neznamená čitelný text. Jako podmínka dostatečnosti pravidlo padá,
platí jen jako podmínka nutná.

---

### Kontrast 3:1 pro UI komponenty a grafiku

**PRAVIDLO:** Rámečky inputů, ikony nesoucí význam, focus indikátory, přepínače a části
grafů potřebné k pochopení drž minimálně 3:1 proti sousedním barvám. Žádné jemné šedé
na šedé u interaktivních prvků.

**KDY PLATÍ:** WCAG 1.4.11 Non-text Contrast, úroveň AA, nové ve verzi 2.1. Platí pro
vizuální informaci nutnou k identifikaci komponenty a jejího stavu a pro grafické objekty
nutné k pochopení obsahu.

**PROČ:** Stejná normová rodina jako 3:1 základ u textu. Prakticky vylučuje bezokrajové
"invisible UI": input, který se pozná jen podle placeholder textu, a focus ring, který
je vidět jen na kalibrovaném monitoru designéra.

**TŘÍDA:** B (regulatorní/normativní).

**ZDROJ:** W3C, Understanding SC 1.4.11, https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html

**KDY NEPLATÍ:** Disabled komponenty, čistá dekorace, vzhled plně řízený prohlížečem
a nezměněný autorem (výjimky v SC).

---

### Minimální velikost cíle 24×24 CSS px

**PRAVIDLO:** Každý klikatelný nebo tapnutelný cíl dělej minimálně 24×24 CSS px, nebo
zajisti výjimku podle SC (nejčastěji spacing: kružnice o průměru 24 px se středem v cíli
se nesmí protínat se sousedním cílem). AAA cíl je 44×44 px (SC 2.5.5).

**KDY PLATÍ:** WCAG 2.5.8 Target Size (Minimum), úroveň AA, NOVÉ ve verzi 2.2 (5.10.2023).
Pozor na časté nedorozumění: bývá chybně uváděno jako AAA z verze 2.1; je to AA a je to
ve 2.2. Přímo limituje zavírací křížky, inline ikonky a hustá ovládání.

**PROČ:** Číslo 24 je normativní konsenzus, ale mechanismus pod ním je doložený: u dotyku
prstem existuje podlaha absolutní přesnosti nezávislá na rychlosti (Bi, Li, Zhai, FFitts law,
CHI 2013, N=12, R² ≥ 0,91). Malý cíl nejde vykoupit zpomalením uživatele, jediný fix je
zvětšit terč.

**TŘÍDA:** B (číslo 24), mechanismus podlahy přesnosti je třída A.

**ZDROJ:** W3C, Understanding SC 2.5.8, https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
· Bi, Li, Zhai (2013). FFitts law: modeling finger touch with Fitts' law. CHI 2013.

**KDY NEPLATÍ:** Pět výjimek přímo v SC: dostatečný rozestup (spacing), existence
ekvivalentního většího cíle na stejné stránce, odkaz inline ve větě, default vzhled
user agentu, essential (velikost je nezbytná pro funkci nebo právně vyžadovaná).

---

### USWDS magic number: kontrast zaručený konstrukcí palety

**PRAVIDLO:** Když stavíš paletu, kalibruj odstíny na "grade" 0-100 podle luminance
(systém USWDS) a kontrastní požadavky převeď na aritmetiku: rozdíl grade 40+ zaručuje
AA pro velký text, 50+ AA pro běžný text, 70+ AAA. Pak nemusíš měřit každý pár zvlášť,
kontrast je zaručený konstrukcí.

**KDY PLATÍ:** Paleta postavená na USWDS tokenech, nebo vlastní paleta kalibrovaná stejnou
metodou. Doplněk či alternativa k párovému měření z pravidla 4,5:1, užitečné hlavně
u větších systémů barev, kde se páry kombinují volně.

**PROČ:** Kontrastní poměr je funkce luminance obou barev. Když každý token nese grade
odvozený z luminance, minimální rozdíl grade implikuje minimální kontrastní poměr,
a kontrola se přesouvá z runtime (změř každou kombinaci) do návrhu palety (drž rozdíly).

**TŘÍDA:** B (publikovaná konvence design systému s právní kotvou Section 508; USWDS je
jediný z prozkoumaných systémů s publikovanou test maticí komponent proti WCAG).

**ZDROJ:** USWDS Design tokens: Color, https://designsystem.digital.gov/design-tokens/color/overview/

**KDY NEPLATÍ:** Na libovolné paletě bez kalibrace. Rozdíl "40" mezi odstíny, jejichž
grade nikdo neodvodil z luminance, nezaručuje vůbec nic. A dědí všechny slabiny vzorce
WCAG (viz pravidlo 4,5:1), je to jeho přebalení, ne oprava.

---

### Barva nikdy jako jediný nositel informace

**PRAVIDLO:** Každou informaci vyjádřenou barvou vyjádři současně druhým kanálem: textem,
ikonou, tvarem, podtržením nebo pozicí. Návrh začni nebo zkontroluj v černobílé
(USWDS: "Start in black and white"). Platí pro stavy, chyby, odkazy v textu, povinná pole,
série v grafu i rozdíl vybráno/nevybráno.

**KDY PLATÍ:** Téměř univerzálně. Tohle je nejblíž bezvýjimečnému pravidlu v celé téhle
notě: shodují se na něm regulace (WCAG 1.4.1 Use of Color, úroveň A) i všechny prozkoumané
design systémy (USWDS, GOV.UK, NHS, Carbon, Atlassian a další). Když se shodne tolik
organizací s různými zájmy, je to nejsilnější typ konvence, jaký existuje.

**PROČ:** Barva je nejméně spolehlivý vizuální kanál. Barvosleposti má ~8 % mužů a ~0,5 %
žen (demografický argument USWDS); k tomu monochromatické a e-ink displeje, tisk, přímé
slunce a noční barevné filtry. Kanál, který u části publika prostě chybí, nesmí nést
informaci sám.

**TŘÍDA:** B (regulace plus shoda napříč všemi zdroji). Míra shody je tady výjimečná.

**ZDROJ:** W3C, Understanding SC 1.4.1, https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html
· USWDS accessibility guidance, https://designsystem.digital.gov/documentation/accessibility/
· GOV.UK Design System, button: "Do not only rely on the red colour of a warning button",
https://design-system.service.gov.uk/components/button/

**KDY NEPLATÍ:** Jen u čisté dekorace, která žádnou informaci nenese. Pro informaci
nesoucí prvky výjimka nenalezena v žádném prozkoumaném zdroji.

---

### Sémantické barvy jen pro sémantiku, stav vždy s textem nebo ikonou

**PRAVIDLO:** Stav (chyba, varování, úspěch, info) komunikuj vždy kombinací barva + text
nebo ikona, nikdy barvou samotnou (speciální případ předchozího pravidla). A obráceně:
sémantické barvy vyhraď stavům. Červená a oranžová nikdy na běžné CTA (oranžové "Uložit"
je chyba, Atlassian to má jako pojmenovaný anti-pattern). Destruktivní akce = danger barva
+ explicitní sloveso ("Smazat projekt", ne "OK") + potvrzovací krok.

**KDY PLATÍ:** Formuláře, alerty, notifikace, tlačítka, stavové odznaky. Shoda napříč
prozkoumanými systémy (GOV.UK, NHS, Atlassian, Carbon). Carbon navíc rozlišuje: destruktivní
akce jako primární krok workflow = primary danger, jako jedna z několika voleb =
tertiary/ghost danger.

**PROČ:** Dva mechanismy. Barva bez textu padá na barvosleposti a na tom, že význam barev
je naučená konvence, ne percepce. A sémantická barva na nesémantickém prvku signál
rozmělňuje: warning button funguje jen dokud je vzácný (NHS: "They are only effective if
used very sparingly. Most services should not need one.").

**TŘÍDA:** B (shoda publikovaných konvencí).

**ZDROJ:** GOV.UK Design System, button, https://design-system.service.gov.uk/components/button/
· NHS service manual, buttons, https://service-manual.nhs.uk/design-system/components/buttons
· Atlassian Design System (color): "Don't use warning or danger for CTAs that aren't
warning or danger" · IBM Carbon Design System, button.

**KDY NEPLATÍ:** Výjimka nenalezena. Nejslabší místo pravidla je volba konkrétních odstínů:
červená = chyba je kulturní konvence západního softwaru, ne percepční zákon, takže se
opírej o konzistenci uvnitř produktu, ne o "univerzální význam červené".

---

### Aesthetic-Usability Effect: jádro platí, populární verze ne

**PRAVIDLO:** Počítej s tím, že vzhled silně ovlivňuje, jak lidé použitelnost HODNOTÍ,
hlavně při prvním kontaktu a v jednorázovém testu. Nikdy z toho ale neodvozuj, že hezký
design je použitelnější nebo že promíjí chyby. Konkrétně: (1) neinterpretuj vysoká
subjektivní skóre z jednorázového testu na hezkém prototypu jako důkaz použitelnosti;
(2) neprodávej vizuální polish jako náhradu opravy usability problémů.

**KDY PLATÍ:** Jádro (estetika koreluje s VNÍMANOU použitelností před použitím) je dobře
replikované napříč kulturami: první dojmy, krátké expozice, subjektivní škály, srovnávání
prototypů.

**PROČ:** Původ: Kurosu & Kashimura (1995), 26 layoutů bankomatu, r = 0,59. Pozor,
"inherent usability" tam NEBYLA měřená použitelnost, ale soulad s design guidelines; nikdo
bankomat nepoužil (a kolující N=252 účastníků se nepodařilo ověřit, necitovat). Nejsilnější
evidence: Tractinsky (1997) studii chtěl VYVRÁTIT ("my main objective was to demonstrate
that K&K's findings were either wrong... or at best qualified by cultural factors"),
tři studie s N = 104/81/108 a postupně tvrdší metodou, a korelace vyšly "if anything...
even higher". To je vzácný vzor: replikace nepřítelem hypotézy. Pořád jde ale o pre-use
vnímání, ne o výkon.

Populární verze "hezký design = uživatelé promíjejí usability chyby" podložená NENÍ.
Článek NN/g (nngroup.com/articles/aesthetic-usability-effect/) tvrdí gradaci "minor ano,
large ne" a celý seznam referencí má dvě položky: Kurosu & Kashimura 1995 a Norman 2004
(populární kniha). Primární studie interakci neobsahovala, nebylo co promíjet. Proti
populární verzi jdou minimálně tři studie: Hassenzahl (2004) usability problémy se propsaly
do hodnocení a krása je nezachránila; Sonderegger & Sauer (2010, Applied Ergonomics, N=60)
atraktivní zařízení časy úkolů ZKRÁTILO, zatímco Sauer & Sonderegger (2010, BIT, N=60)
estetika časy PRODLOUŽILA, tedy stejná skupina, stejný rok, opačné znaménko efektu na
výkon; Sonderegger et al. (2012, Ergonomics, N=60, 2 týdny) efekt na vnímanou použitelnost
s délkou používání vyprchává. Moshagen & Thielsch (2012, N=1673): estetika a vnímaná
použitelnost jsou psychometricky oddělené konstrukty. Meta-analýza tématu neexistuje
(hledáno 7/2026, nenalezena).

**TŘÍDA:** A pro jádro (vliv na hodnocení, replikováno) / C pro populární verzi
(promíjení chyb, gradace minor/large).

**ZDROJ:** Kurosu & Kashimura (1995), CHI '95 Companion, DOI 10.1145/223355.223680
· Tractinsky (1997), CHI '97, s. 115-122 · Hassenzahl (2004), Human-Computer Interaction 19(4)
· Sonderegger & Sauer (2010), Applied Ergonomics 41(3) · Sauer & Sonderegger (2010),
Behaviour & Information Technology · Sonderegger et al. (2012), Ergonomics 55(7)
· Moshagen & Thielsch (2012), BIT · kriticky k NN/g: https://www.nngroup.com/articles/aesthetic-usability-effect/

**KDY NEPLATÍ:** Po delším reálném používání (efekt slábne s expozicí), na objektivní
výkon (nekonzistentní znaménko efektu) a na toleranci chyb (nepodloženo). Jádro navíc
neříká nic o tom, KTERÉ vizuální volby estetiku zvyšují.

**Souvislost:** Měření kontrastu zvlášť ve světlém a tmavém tématu je v [Theming a dark mode](theming-a-dark-mode.md).
