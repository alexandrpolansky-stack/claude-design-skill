# Kontext: e-commerce

**Kdo je čtenář.** Člověk, který přichází s výchozí nedůvěrou a obvykle uprostřed srovnávání.
V největším dostupném průzkumu kredibility (10 kategorií webů, N=2684) měla e-commerce
"general suspicion" 17,2 %, což je nejvyšší hodnota v celém datasetu. Lidé sami spontánně zmiňovali
jako signály hlavně rozpoznatelnost jména (25,9 %) a zákaznický servis (16,7 %, nad průměrem).
To znamená, že prokázání identity a dostupnosti obchodu není doplněk, je to jádro stránky.

**Dopad chyby.** Přímý a měřitelný. Nedokončený checkout, nedoručená platba, storno, chargeback.
Zároveň je to sektor s nejvíc prodávanými čísly o dopadu chyby, takže je potřeba rozlišovat, co je
naměřené a co modelové.

**Regulace vs volba.** Tvrdší než kdekoliv jinde v privátním sektoru. European Accessibility Act
2019/882 jmenuje e-commerce explicitně, je živý od 28. 6. 2025 a vyžaduje EN 301 549, tedy
prakticky WCAG 2.1 AA. Kontrast, velikost cílů, reflow a text spacing tím přestávají být předmětem
designu a stávají se vstupním parametrem. U českého veřejného zadavatele platí navíc zákon
č. 99/2019 Sb. (WCAG 2.1 AA plus publikované prohlášení o přístupnosti).

**Vrstvení.** Struktura a pozice (navigace, hledání, košík, login, souhrn objednávky) se
neodchylují. Regulatorní parametry jsou mantinel. Odchyluje se povrch.

Legenda tříd: A = tvrdá opora (měření), B = publikovaná konvence nebo regulace, C = řemeslná praxe
či pozorování bez opory.

Sesterské noty: [finance.md](finance.md) (platby a kredibilita), [vlada.md](vlada.md) (rozpis
regulatorních rámců), [luxury.md](luxury.md), [dev-tools-saas.md](dev-tools-saas.md),
[seniori.md](seniori.md), [deti.md](deti.md), [zdravotnictvi.md](zdravotnictvi.md).

---

## Pravidla

### WCAG 2.1 AA je vstup, ne cíl kvality

**PRAVIDLO:** U e-shopu v EU ber tyhle prahy jako povinný vstup: 4,5:1 na text a 3:1 na velký text
(1.4.3), 3:1 na UI komponenty, okraje inputů, ikony a focus indikátory (1.4.11), funkčnost při
320 CSS px bez horizontálního scrollu (1.4.10), `line-height` nastavitelný na 1,5násobek bez
rozbití layoutu (1.4.12), zvětšení textu na 200 % bez ztráty funkce (1.4.4), minimálně 24×24 CSS px
na klikatelný prvek (2.5.8).
**KDY PLATÍ:** Každý e-shop dostupný v EU, od 28. 6. 2025.
**PROČ:** Není to doporučení, je to standard vymahatelný na privátním sektoru. Praktický dopad na
designový prostor: 1.4.3 vylučuje světle šedý text na bílém, 1.4.11 vylučuje bezokrajové inputy
a jemné šedé ikony, 2.5.8 stanovuje minimální fyzickou velikost stepperů množství, křížků a ikon
pro odebrání z košíku.
**TŘÍDA:** B (regulace, právně vynutitelná).
**ZDROJ:** European Accessibility Act 2019/882, standard EN 301 549. Jednotlivá WCAG kritéria
ověřena proti W3C. Pozor: 2.5.8 Target Size (Minimum) je AA a NOVÉ ve WCAG 2.2 (5. 10. 2023),
ne v 2.1, což je častý zdroj nedorozumění. Verbatim text EN 301 549 clause 9 nebyl získán
primárně (etsi.org vrací 403), substance je z W3C a sekundárních zdrojů.
**KDY NEPLATÍ:** 2.5.8 má pět výjimek (spacing, equivalent, inline, user agent, essential), takže
inline odkaz uvnitř odstavce menší než 24 px porušení není. AAA prahy (7:1, 44×44 px) povinné nejsou.

### Nedůvěra je výchozí stav, důkazy identity dej do zorného pole

**PRAVIDLO:** Na produktové stránce a v checkoutu měj v dosahu bez hledání: dohledatelnou identitu
obchodu (firma, adresa, IČO), způsob a dostupnost kontaktu, a podmínky vrácení. Nespoléhej, že si
je uživatel najde v patičce.
**KDY PLATÍ:** Vždy, nejvíc u obchodu bez zavedeného jména.
**PROČ:** E-commerce má nejvyšší výchozí podezřívavost z deseti měřených kategorií (17,2 %).
Rozpoznatelnost jména (25,9 %) a zákaznický servis (16,7 %) jsou signály, které lidé spontánně
uvádějí, tedy si jich všímají sami, bez otázky. Kdo jméno nemá, musí ho nahradit ověřitelnými
detaily.
**TŘÍDA:** A.
**ZDROJ:** Fogg et al. (2002), Consumer WebWatch, N=2684, 10 kategorií webů, plný text čten.
Klíčová věta: "people assess credibility differently for different types of Web sites."
**KDY NEPLATÍ:** Metodika měří PROMINENCI, tedy co lidé sami zmíní, ne změnu chování. Neodvozuj
z procent velikost dopadu na konverzi, ta v datech není.

### Bez zavedeného jména nese vizuál větší díl kredibility

**PRAVIDLO:** U malého nebo neznámého obchodu investuj do vizuální úrovně dřív a víc než
u zavedené značky. U zavedené značky je vizuál méně nosný a prostředky patří jinam.
**KDY PLATÍ:** Rozhodování o rozpočtu a prioritách na začátku projektu.
**PROČ:** Bez rozpoznatelnosti brandu hraje vizuální design významnější roli v tom, jak se
posuzuje kredibilita. Vizuál přitom funguje jako prahová podmínka pro vyřazení, ne jako
diferenciátor pro výběr: vzhled predikoval odmítnutí, obsah a personalizace predikovaly volbu.
Prakticky to znamená, že vizuál musí přejít prahovou zkoušku, jinak se web vyřadí ještě předtím,
než se čte obsah. Investovat nad ten práh už vrací málo.
**TŘÍDA:** A ve své doméně, C jako přenos na e-shop. Obě studie jsou ze zdravotnictví.
**ZDROJ:** Robins, Holmes, Stansbury (2010), N=34, 31 zdravotnických webů, plný text čten,
verbatim: "without brand recognition, visual design plays a MORE IMPORTANT role in how credibility
is assessed". Sillence, Briggs, Fishwick, Harris (2004), CHI 2004, 15 žen, 4 týdny: "design appeal
predicted rejection (mistrust)".
**KDY NEPLATÍ:** Obojí je jiná doména a malé N. Neber to jako číslo, ale jako směr, a nepoužívej
to jako argument pro neomezený rozpočet na vizuál.

### Jedna primární akce na krok

**PRAVIDLO:** V košíku a v každém kroku checkoutu měj právě jedno primární tlačítko. Ostatní akce
(uložit na později, zpět, uplatnit kupón, změnit dopravu) dej jako sekundární nebo tertiary.
Při třech a více souběžných akcích je slouč do dropdownu.
**KDY PLATÍ:** Každá obrazovka s transakčním krokem.
**PROČ:** Víc primárních tlačítek snižuje dopad každého z nich a vytváří nejistotu, co je vlastně
další krok. Shoduje se na tom deset a více design systémů organizací s velmi různými zájmy, což
z toho dělá nejpevnější pravidlo v knihovně, i když důvody uvádějí různé (GOV.UK snížení dopadu
a nejistotu, Apple kognitivní zátěž).
**TŘÍDA:** B (publikovaná konvence, ale s výjimečně silnou shodou).
**ZDROJ:** GOV.UK ("avoid using multiple default buttons on a single page"), NHS, Material Design 3
("used sparingly, ideally for only one action on a page"), Carbon, Atlassian, Apple HIG ("one or
two per view"), Fluent 2, Primer ("never more than one in a group, rarely more than one per page"),
Ant Design ("at most one primary button in a section", vzorec 1 primary + n secondary), Base Web,
Adobe Spectrum (max 3 accent buttons v jednom pohledu).
**KDY NEPLATÍ:** Když jsou na stránce dvě rovnocenné varianty TÉŽE akce (jednorázový nákup vs
předplatné, dvě velikosti balení). To nejsou dvě akce, ale jedna volba, a symetrická hierarchie
je tam správná.

### Baymard cituj jako katalog problémů, ne jako čísla o konverzi

**PRAVIDLO:** Guidelines z Baymardu používej jako seznam pozorovaných failure modes v checkoutu.
Nikdy necituj "35,26% nárůst konverze" jako naměřený výsledek. Když ho potřebuješ zmínit, označ
ho jako modelový odhad potenciálu a řekni, že experiment za ním není.
**KDY PLATÍ:** Vždy, když se v návrhu nebo v nabídce klientovi objeví číslo z tohohle zdroje.
**PROČ:** Metodika je moderovaný think-aloud, eye-tracking a EXPERTNÍ benchmark. A/B testování ani
měření konverze na živém provozu v ní nejsou, takže lift z ní vzejít nemůže. Dvě desetinná místa
navíc vytvářejí falešnou přesnost u čísla, jehož výpočet není publikovaný.
**TŘÍDA:** B pro guidelines jako katalog, C pro čísla o konverzi.
**ZDROJ:** Vlastní self-reported metodika Baymard Institute: 200 000+ hodin, 4 400+ **sessions**
(ne osob), 32 účastníků eye-trackingu, 335 webů, 794 guidelines. Neauditované, s vnitřními
nekonzistencemi (250 vs 335 webů, 650 vs 700 vs 794 guidelines).
**KDY NEPLATÍ:** Pozorované failure modes samotné jsou použitelné a hodnotné, ten katalog je
skutečná práce. Pravidlo se týká čísel, ne nálezů.

### Nepoužívej ani cart abandonment jako fakt o svém obchodu

**PRAVIDLO:** Průměr opuštěných košíků neber jako benchmark, proti kterému se měříš. Vlastní číslo
si spočítej z vlastních dat a definici napiš vedle něj (co se počítá jako košík, od jakého kroku).
**KDY PLATÍ:** Každý argument typu "průmyslový standard je X %".
**PROČ:** Kolující hodnota 70,22 % je prostý nevážený průměr z metaanalýzy asi 50 cizích studií
z let 2006 až 2025 s nesouměřitelnými definicemi opuštění. Vážení není publikované. Průměr napříč
nesouměřitelnými definicemi není benchmark.
**TŘÍDA:** C.
**ZDROJ:** Rozbor metodiky Baymard Institute (evidenční audit 7/2026).
**KDY NEPLATÍ:** Nikdy nepotřebuješ cizí průměr, když máš vlastní analytiku. Pokud ji nemáš,
je řešení ji nasadit, ne dosadit cizí číslo.

### Číselná pole nejsou čísla

**PRAVIDLO:** Číslo karty, PSČ, telefon, IČO a číslo objednávky nesázej jako `type="number"`.
Jsou to řetězce číslic. Použij textové pole s vhodným `inputmode` a s formátováním, které
nezasahuje do hodnoty.
**KDY PLATÍ:** Všechna platební a doručovací pole.
**PROČ:** Pokud dvě hodnoty nemůžeš sečíst, nejsou to čísla. Numerické pole přidává spinner,
reaguje na scroll, mění hodnotu při kolečku myši a podléhá locale formátování, což na
identifikátorech vytváří chyby, které uživatel nevidí. Sémantika před estetikou.
**TŘÍDA:** B (publikovaná konvence GOV.UK number input pattern).
**ZDROJ:** GOV.UK Design System, vzor pro číselné vstupy. Diskuse
`news.ycombinator.com/item?id=22433654`.
**KDY NEPLATÍ:** Množství v košíku je skutečné číslo, tam stepper i numerický vstup smysl mají.
Pozor jen na velikost cíle (2.5.8, minimálně 24×24 px).

### Destruktivní akci nerozlišuj jen barvou

**PRAVIDLO:** Odebrání z košíku, zrušení objednávky, smazání adresy nebo platební metody musí mít
textové pojmenování toho, co se stane. U nevratných akcí přidej potvrzovací krok, u vratných undo.
Červená barva sama nestačí.
**KDY PLATÍ:** Každá akce, která maže nebo ruší.
**PROČ:** Barva nemůže nést význam sama, protože ji část uživatelů nerozliší (barvoslepost
u 8 % mužů a 0,5 % žen). Napříč design systémy se shoduje, že destruktivní akce potřebuje text
plus potvrzení. GOV.UK jde dál a warning button rezervuje jen pro "serious destructive consequences
that cannot be easily undone", plus explicitně: "Do not only rely on the red colour of a warning
button".
**TŘÍDA:** B.
**ZDROJ:** GOV.UK Design System (warning button), USWDS (demografie barvosleposti, princip
"start in black and white"), Carbon (destruktivní akce jako primární krok = primary danger, jako
jedna z voleb = tertiary/ghost danger), Atlassian anti-pattern: "Don't use warning or danger for
CTAs that aren't warning or danger."
**KDY NEPLATÍ:** Odebrání jedné položky z košíku je vratné, tam stačí undo a potvrzovací dialog je
jen frikce. Potvrzení si rezervuj pro to, co se vrátit nedá.

### Disabled tlačítko není validace

**PRAVIDLO:** Nezakazuj tlačítko "Pokračovat", dokud formulář není platný. Nech ho aktivní a po
odeslání ukaž konkrétní chyby u konkrétních polí, textem.
**KDY PLATÍ:** Formuláře v checkoutu, registraci a při zadávání adresy.
**PROČ:** Disabled stav má prokazatelně špatný kontrast a plete uživatele, protože nesděluje,
CO chybí. GOV.UK to formuluje jako "poor contrast and can confuse some users, avoid if possible"
a NHS o svých disabled variantách sám přiznává, že nesplňují kontrastní poměry. Uživatel u šedého
tlačítka nemá kam kliknout, aby se dozvěděl, co je špatně.
**TŘÍDA:** B.
**ZDROJ:** GOV.UK Design System, NHS Service Manual (vlastní přiznání k disabled variantám).
**KDY NEPLATÍ:** Akce, kterou nelze zopakovat, typicky už běžící platba. Tam je disabled plus
loading stav ochrana proti dvojímu odeslání, ne validace.

### Nešij seznam produktů z borderů

**PRAVIDLO:** V dlaždicích produktů a v souhrnu košíku neoddělovej každou položku plnou linkou.
Použij spacing, jemný podklad nebo stín.
**KDY PLATÍ:** Výpis produktů, souhrn objednávky, seznam adres a platebních metod.
**PROČ:** Hodně borderů vytváří dojem zanesené obrazovky, protože každá linka soutěží o pozornost.
Oddělení jde udělat mezerou nebo pozadím, což je tišší.
**TŘÍDA:** C (řemeslná praxe, čistá autorita, žádný výzkum).
**ZDROJ:** Refactoring UI, pravidlo o nahrazení borderů stínem, kontrastním pozadím nebo spacingem.
**KDY NEPLATÍ:** Tabulka s hodnotami, kde linka pomáhá držet řádek. A v Google Sheets platí domácí
override: gridlines zůstávají viditelné, viz [sheets znalostní báze](../../sheets/znalostni-baze.md).

---

## Co v tomhle sektoru NENÍ

| Tvrzení | Stav |
|---|---|
| "Lepší checkout dá 35 % nárůst konverze" | C, modelový odhad bez experimentu, necitovat jako fakt |
| "Baymard otestoval 18 000 uživatelů" | nepotvrzené, číslo 18 000 se váže postupně na users, reviewed pages i annotated designs |
| "4 400 lidí v Baymard výzkumu" | jsou to sessions, ne osoby |
| "70,22 % košíků se opouští" | nevážený průměr napříč nesouměřitelnými definicemi |
| Konkrétní hodnota border-radius pro tlačítko "Koupit" | evidence žádnou hodnotu nestanovuje |

K poslední řádce: jediná doménově shodná opora pro zakulacení klikatelných marketingových prvků
je Biswas, Abell, Chacko (2024), Journal of Consumer Research 51(3), 552-570, tři field experimenty
s reálným CTR. Ale je to binární srovnání curved vs sharp, ŽÁDNÁ dose-response na konkrétní radius,
N a effect sizes nepotvrzené (closed access), a kolující číslo "CTR o 17 až 55 % vyšší"
se nepodařilo ověřit, takže se necituje. Poctivě: zakulacení je bezpečný default a mírné plus proti
ostrým 90° rohům, žádná konkrétní hodnota z toho nevyplývá.

## Souvisí

- [Kontext: senioři](seniori.md), povinné čtení, pokud e-shop cílí i na starší publikum
- [Kontext: luxury](luxury.md), když je obchod prémiový a positioning je součást zadání
- [Kontext: dev tools a SaaS](dev-tools-saas.md), pro placené plány a self-service checkout
  v produktu
- [Etika v UX](../ux-zaklady/etika-v-ux.md), dark patterns v košíku a při upsellu
- [UX Laws](../zakony-principy/ux-laws.md), Fitts na dimenzování cílů, včetně oprav
