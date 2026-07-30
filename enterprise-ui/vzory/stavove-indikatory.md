# Stavové indikátory

Jak sdělit stav nebo závažnost. Čtyři varianty a pravidlo, kolik prvků musí stav nést, aby splnil
WCAG.

Související: [Notifikace](notifikace.md) ·
[Kontrast a barva](../../ux-design/pravidla/kontrast-a-barva.md) ·
[Datové tabulky](../komponenty/datove-tabulky.md)

---

## Rychlé rozhodnutí

1. Stav musí nést **aspoň dva** ze tří prvků: barva, tvar, symbol. Barva samotná nikdy nestačí.
2. Kontrast **min. 3:1** mezi barvami indikátorů navzájem i mezi indikátorem a pozadím.
3. Je dost místa a stav potřebuje maximální pozornost = **icon indicator** (ikona plus tvar plus
   barva plus popisek).
4. Málo místa nebo se skenuje hodně dat = **shape indicator** (tvar plus barva plus popisek).
   Tvarový indikátor **musí** mít popisek, protože nemá symbol.
5. Počet nových položek je důležitý = **badge s číslem**. Není důležitý nebo neznámý = **tečka**.
6. Sledování změn ve velkých sadách statistik = **differential indicator** se znaménkem nebo šipkou.
7. Když akce uživatele není potřeba a stav není dost významný, **použij prostý text**, ne indikátor.
8. Víc než pět nebo šest indikátorů na obrazovce uživatele zavalí.
9. Když se stavy konsolidují do jednoho, použij **barvu s nejvyšší pozorností** z těch podřízených.
10. Nepoužívej stejný tvar v různých barvách v jedné zkušenosti.

---

## Čtyři varianty

| Varianta | Kdy | Typické použití |
|---|---|---|
| Icon indicator | Rozvržení nabízí dost místa a obsah potřebuje maximální pozornost. Vyžaduje ikonu, tvar, významovou barvu a **popisný inline label** | Notifikace, progress indikátory, datové tabulky, seznamy úkolů, dashboardové widgety |
| Shape indicator | Užitečný v menších prostorech, nebo když uživatel skenuje velké množství dat | Seznamy, dashboardy, datové tabulky, datové vizualizace, síťové diagramy |
| Badge s číslem | Když je dostupný počet nových nebo aktualizovaných položek a je důležité, aby uživatel znal číslo | Notifikační panely v hlavičce, spolu s avatary nebo ikonami |
| Badge bez čísla (tečka) | Když nové položky jsou, ale počet je neznámý nebo pro uživatele nepodstatný. Tečka je kompaktnější a diskrétnější | Notifikační panely v hlavičce, ikonová tlačítka v toolbarech |
| Differential indicator | Když uživatel monitoruje rozdíly ve velkých seznamech statistik a cokoliv jiného než typografie by bylo příliš rušivé | Finanční dashboardy, zdůraznění delt, datové vizualizace |

**ZDROJ:** Carbon, Status indicator pattern, tabulka variant.
https://carbondesignsystem.com/patterns/status-indicator-pattern/

## Icon versus shape: k čemu který slouží

Carbon je v tom explicitní a je to nejužitečnější rozlišení celého vzoru:

| Indikátor | Co reprezentuje |
|---|---|
| Icon indicator | **Zdraví systému.** Informuje, jestli všechno běží hladce, nebo nastal problém. Například dokončení nebo selhání úkolu po odeslání formuláře. Dává zpětnou vazbu na celkový stav produktu, systémové notifikace |
| Shape indicator | **Sekundární sada indikátorů**, kterou si produkt může definovat po svém. Pomáhá prioritizovat úkoly (červený trojúhelník pro vysokou prioritu), nebo ukazuje aktuální fázi životního cyklu komponenty (aktivováno, deaktivováno). **Nemusí nutně znamenat urgenci** |

**ZDROJ:** Carbon, Status indicator pattern, Icon indicators versus shape indicators.
https://carbondesignsystem.com/patterns/status-indicator-pattern/

## Čtyři prvky, kterými se stav dá nést

Carbon jmenuje čtyři základní prvky (animaci a zvuk vzor záměrně neřeší):

1. Symboly
2. Tvary
3. Barvy
4. Typografie

**PRAVIDLO:** Pro splnění WCAG musí být přítomné **aspoň tři** z těchto prvků.
**TŘÍDA:** B pro Carbonovu formulaci. Pozor, Carbon má na dvou místech dvě různá čísla, viz níže.
**ZDROJ:** Carbon, Status indicator pattern, Visual guidance, verbatim: „There are four basic elements
that comprise Carbon status indicators. (Note: we won't get into animation and sound in this pattern.)
And for WCAG compliance, at least three of these elements must be present."
https://carbondesignsystem.com/patterns/status-indicator-pattern/

**Vnitřní nesrovnalost Carbonu, kterou je potřeba znát:** v sekci Visual guidance Carbon říká
„aspoň tři ze čtyř prvků". V sekci Accessibility téhož vzoru říká: „status indicators should rely on at
least two of the following elements: color, shape, or symbol". Ta druhá formulace je z jinak
vymezeného seznamu (tři prvky, bez typografie). **Bezpečné čtení, které splní obojí:** barva plus tvar
nebo symbol plus textový popisek. To je moje sjednocení, ne Carbonovo tvrzení.

### Symboly

Ikony jsou vizuální symboly reprezentující ideje, objekty nebo akce. Pomáhají komunikovat zprávu
rychle, podporují interaktivitu a zdůrazňují důležitou informaci. Carbonovy příklady: vykřičník pro
varování, checkmark pro úspěch, otazník pro nápovědu.

### Tvary

Geometrické figury (čtverce, kruhy, obdélníky), protože jsou okamžitě čitelné i v malých velikostech.
Carbon jmenuje asociace: tvary s přímými linkami a pravými úhly typicky sdělují strukturu a řád
(jako mřížka), zaoblené tvary jsou přívětivější a symbolizují kontinuitu a spojení.

**Carbonovo varování:** tvary mají i kulturní asociace. V dopravě a značení hexagon znamená stop,
obrácený trojúhelník dej přednost. **Nesprávné použití tvaru může narušit naučené vzorce rozpoznávání
a zmást uživatele**, což může zhoršit celou zkušenost.

### Barvy

Carbon má vlastní stavovou paletu a její obsazení (třída **B**, je to konvence, ne norma):

| Barva | Význam podle Carbonu |
|---|---|
| Červená | Nebezpečí nebo chyba |
| Oranžová | Závažné varování |
| Žlutá | Běžné varování |
| Zelená | Normální stav nebo úspěch |
| Modrá | Pasivní notifikace, typicky doplňující informace a postup ve flow |
| Šedá | Návrhy (drafts) nebo úkoly, které nezačaly |
| Purpurová | Odchylky (outliers) nebo nedefinované stavy |

**Poznámka k rozšířené paletě:** Carbon má i „extended status palette" a je u ní explicitní, že je
**jen pro zlepšení kontrastu u žlutých a oranžových**, není součástí IBM brand palety a je vyhrazená
pro velmi selektivní použití v datových vizualizacích a některých stavových indikátorech. Verbatim:
„Do not use this palette in any other context or layout." Konkrétní hodnoty téhle palety do knihovny
záměrně nepřebírám, jsou to IBM tokeny.

### Typografie

Carbon dává doporučené párování velikostí ikony a písma:

| Varianta | Velikost ikony | Velikost písma |
|---|---|---|
| Icon indicator | 20 px | 16 pt |
| Icon indicator | 16 px | 14 pt |
| Shape indicator | 16 px | 14 pt |
| Shape indicator | 16 px | 12 pt |

Carbon dodává, že tvarový indikátor lze párovat i s větší velikostí, ale doporučuje 14 pt nebo 12 pt
v menších prostorech, nebo když jde o sekundární sadu indikátorů vedle sady ikonových.

**ZDROJ:** Carbon, Status indicator pattern, Visual guidance a Status type.
https://carbondesignsystem.com/patterns/status-indicator-pattern/

## Kognitivní zátěž: kdy indikátor nepoužít

**PRAVIDLO:** Nepoužívej stavové indikátory, když **není potřeba žádná akce uživatele**, nebo když
stavová informace není dost významná, aby se zdůrazňovala. Použij prostý text, ať rozhraní nezavalíš
zbytečnými indikátory. Carbon nedává striktní limit, ale říká, že víc než pět nebo šest indikátorů
může uživatele zavalit a zhoršit soustředění.
**KDY PLATÍ:** Každá obrazovka s víc stavy.
**TŘÍDA:** B. Číslo pět nebo šest Carbon neopírá o měření, sám říká „we won't set a strict limit".
**ZDROJ:** Carbon, Status indicator pattern, Cognitive load, verbatim: „Avoid using status indicators
when no user action is required or when the status information isn't significant enough to highlight.
Instead, use plain text to prevent overloading the interface with unnecessary indicators."
https://carbondesignsystem.com/patterns/status-indicator-pattern/
**Souvislost:** limity kapacity krátkodobé paměti a jejich hraniční podmínky (Cowan, Miller) jsou
v [UX Laws](../../ux-design/zakony-principy/ux-laws.md) a ve
[formulářích a stavech](../../ux-design/pravidla/formulare-a-stavy.md). **Na počet viditelných položek
se limit 7±2 nevztahuje**, takže Carbonových pět nebo šest neber jako kapacitní argument, ale jako
řemeslné doporučení.

## Konsolidovaný stav

**PRAVIDLO:** Když se víc stavů konsoliduje do jednoho, použij pro skupinu barvu s **nejvyšší
pozorností**. Carbonův příklad: když jsou stavy podřízených komponent zelený, žlutý a červený,
konsolidovaný indikátor je **červený**.
**KDY PLATÍ:** Dashboardy, agregované pohledy, stav skupiny služeb.
**TŘÍDA:** B
**ZDROJ:** Carbon, Status indicator pattern, Consolidated statuses.
https://carbondesignsystem.com/patterns/status-indicator-pattern/

## Úrovně závažnosti

Carbon definuje tři úrovně a nechává na produktovém týmu, aby je obsadil podle svých potřeb, s ohledem
na to, jak každá úroveň ovlivní reakci uživatele.

| Úroveň | Kdy |
|---|---|
| High attention | Vyžaduje **okamžitou** akci uživatele kvůli nepravidelnosti systému, poruše nebo potenciálně destruktivní akci. Alerty, výjimky, potvrzení, chyby |
| Medium attention | Okamžitá akce **není** potřeba, nebo jde o zpětnou vazbu na akci uživatele. Potvrzení přijetí, progress indikátory |
| Low attention | Něco je připravené k zobrazení, systémová zpětná vazba, nebo signál, že se od poslední interakce něco změnilo |

**ZDROJ:** Carbon, Status indicator pattern, Severity levels.
https://carbondesignsystem.com/patterns/status-indicator-pattern/

## Labely a zarovnání

- **Icon indicator** Carbon nazývá „kontextový" indikátor: je svázaný s konkrétním prvkem UI nebo
  obsahem a **musí být umístěný blízko něj**.
- Když label není popisný nebo je párovaný jen s číslem, přidej nadpis nebo doplňkový obsah, který
  vyjasní, co stav znamená.
- **Shape indicator musí mít stavový label**, protože nemá rozpoznatelnost ikony.
- Když indikátory stohuješ svisle, ikony drž **zarovnané vlevo** s doprovodným textem, aby se dobře
  skenovaly.
- Tvarový indikátor dávej **před** label. Za text ho dej jen tehdy, když nemají texty rozdílnou délku,
  jinak vypadne ze zarovnání.
- Indikátory uvnitř notifikace mají **jiné rozestupy**, protože jsou integrované do komponenty a
  neřídí se inline pravidly.

**ZDROJ:** Carbon, Status indicator pattern, Labeling and type pairing, Alignment.
https://carbondesignsystem.com/patterns/status-indicator-pattern/

## Tvary v jedné zkušenosti

**PRAVIDLO:** Vyhýbej se použití **stejného tvaru v různých barvách** v rámci jedné zkušenosti.
**PROČ:** Carbon: tvarové stavy nabízejí větší volnost v interpretaci než ikonové, protože tvar může
mít pro různé situace různou barvu. To je zároveň riziko.
**TŘÍDA:** B
**ZDROJ:** Carbon, Status indicator pattern, Shape indicator, Best practices, verbatim: „consider
avoiding the use of the same shape with different colors within the same experience."
https://carbondesignsystem.com/patterns/status-indicator-pattern/

## Badge

| Varianta | Pravidla |
|---|---|
| S číslem | Limit **tři číslice**, poslední znak je pak plus. Carbon ji povoluje **jen u velkého ikonového tlačítka (48 px)** jako globální akce v hlavičce |
| Bez čísla (tečka) | Subtilnější, ale pořád efektivně přitáhne pozornost. Běžně na ikonových tlačítkách v toolbarech |

Badge se zobrazuje **nad ghost ikonovým tlačítkem**, typicky v hlavičce, značí aktivní notifikaci
a **zruší se, jak uživatel notifikaci vezme na vědomí**. Tlačítko může podle situace otevřít novou
stránku, nebo spustit modal, panel či flyout.

**ZDROJ:** Carbon, Status indicator pattern, Badge indicator.
https://carbondesignsystem.com/patterns/status-indicator-pattern/

## Differential indicator

**Skládá se ze:** symbolu, volitelné barvy a popisného labelu.

**PRAVIDLO:** Differential indicator **musí** mít buď znaménko „+" nebo „-", nebo caret, nebo šipku,
aby označil pozitivní či negativní hodnotu. Barva je **volitelná**, dokud je znaménko nebo ikona
přítomná. Pokud data nejsou o teplotě, pozitivní hodnoty jsou v zeleném spektru a negativní v červeném.
**KDY PLATÍ:** Delty, finanční dashboardy, datové vizualizace.
**TŘÍDA:** B
**ZDROJ:** Carbon, Status indicator pattern, Differential indicator, verbatim: „Color is optional in
these situations as long as the value has either a '+' or '-' in front of it, a chevron icon, or an
arrow icon. Unless the data involves temperature, positive values are represented by the green spectrum
and negative values are represented by the red spectrum."
https://carbondesignsystem.com/patterns/status-indicator-pattern/
**Poznámka:** typografický indikátor by sám o sobě fungoval jen s plus nebo minus, ale Carbon říká,
že v jeho systému se nejčastěji páruje se šipkou nebo caretem kvůli jasnosti.

## Přístupnost

### Barva samotná nestačí

**PRAVIDLO:** Spoléhat se jen na barvu je nedostatečné, zvlášť pro uživatele s poruchou barvocitu.
Barva musí být párovaná s textem nebo jiným vizuálním vodítkem. Pro splnění non-text contrast musí být
**aspoň 3:1 kontrast mezi barvami použitými pro stavové indikátory** a taky **mezi indikátorem
a pozadím stránky**. Když je kontrast dostatečný, uživatel by měl stavy rozlišit i v odstínech šedi.
**KDY PLATÍ:** Každý stavový indikátor.
**TŘÍDA:** A jako požadavek (WCAG 2.2 SC 1.4.1 Use of Color a SC 1.4.11 Non-text Contrast), B pro
Carbonovu formulaci.
**ZDROJ:** Carbon, Status indicator pattern, Accessibility, s odkazy na
https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html a
https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast
https://carbondesignsystem.com/patterns/status-indicator-pattern/
**Souvislost:** WCAG 1.4.11 a sémantika stavů jsou v knihovně podrobněji ve
[kontrastu a barvě](../../ux-design/pravidla/kontrast-a-barva.md).

### Ikona sama je přijatelná, ale label je lepší

Carbonova pozice: ikony samotné **mohou** být efektivní, když splní požadavek 3:1 na non-text contrast.
Carbon se ale zavazuje dodávat stavové indikátory **s ikonou i labelem**, aby stav pochopili na první
pohled všichni včetně uživatelů se zrakovým omezením.

### Obrysy

| Indikátor | Potřebuje obrys |
|---|---|
| Icon indicator | **Ne.** Není interaktivní a symboly mají dostatečný kontrast proti barvě svého tvaru |
| Shape indicator | **Ano.** Spoléhá jen na tvary a barvy, což nemusí být dost pro čtečky a uživatele se slabým barvocitem. Obrys plus párování s textem je zásadní, hlavně u světlejších stavových barev jako oranžová a žlutá ve světlých tématech |

**ZDROJ:** Carbon, Status indicator pattern, Accessibility, Outlines.
https://carbondesignsystem.com/patterns/status-indicator-pattern/

## Standardizace

Carbon vyžaduje, aby všechny stavové ikony byly schválené a publikované v jeho ikonové knihovně, aby
byla zajištěná konzistence napříč produkty. Uvádí, že jeho pokyny obsahují **jen ty nejběžnější**
stavové indikátory, a když produkt potřebuje ikonu, která ve vzoru není, má o její přidání požádat.

**Praktický důsledek pro nás:** ikonovou knihovnu Carbonu nepřebíráme. Přenositelné je pravidlo:
**měj uzavřenou, schválenou sadu stavových ikon a nepřidávej k nim ad hoc.** Carbon svoje omezení
odůvodňuje předcházením nepotřebným variacím v design systému.

**ZDROJ:** Carbon, Status indicator pattern, Standardization.
https://carbondesignsystem.com/patterns/status-indicator-pattern/

**Poznámka:** konkrétní názvy stavů, které Carbon navrhuje, jsou v jeho dokumentaci v interaktivní
komponentě (`StatusIndicatorTable`), která se v přečtené textové kopii nevykresluje. Carbon k nim
sám dodává, že jsou to návrhy podle běžných případů použití a **nemají diktovat finální názvy stavů
v tvém produktu**.

---

## Co tahle nota neřeší

- Notifikace jako komponenty a jejich typy. [Notifikace](notifikace.md).
- Konkrétní hodnoty kontrastu a jejich evidenční základ.
  [Kontrast a barva](../../ux-design/pravidla/kontrast-a-barva.md).
- Psychologii barev obecně. [Color psychology](../../ux-design/color/color-psychology.md).
- Progress indicator jako komponentu s vlastními stavy.
  [Navigace v hierarchii](../komponenty/navigace-v-hierarchii.md).
- Datovou vizualizaci a palety pro data. To je zatím jen v [sheets](../../sheets/znalostni-baze.md).

## Zdroj

IBM Carbon Design System, Status indicator pattern, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/patterns/status-indicator-pattern/
Carbon k tomuhle vzoru cituje NN/g (Visibility of System Status 2018, Indicators, Validations, and
Notifications 2015), Nick Babich (UX Planet 2020), Miklos Philips (2020) a WCAG 2.2.
Třída **B**, u WCAG kritérií **A**. Vnitřní nesrovnalost Carbonu v počtu povinných prvků je popsaná
výše, neber tedy ani jedno z těch dvou čísel jako přesné.
