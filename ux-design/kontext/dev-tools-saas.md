# Kontext: dev tools a SaaS

**Kdo je čtenář.** Vývojář nebo technický nákupčí, který obvykle přichází z dokumentace, z hledání
nebo z odkazu, a je uprostřed jiné práce. Do několika sekund posuzuje jednu věc: dělá ten nástroj
to, co potřebuju, a dá se to zapojit. U produktového rozhraní je to ten samý člověk v pracovním
soustředění, často s klávesnicí místo myši a s víc otevřenými okny.

**Dopad chyby.** Neztrácí se důvěra typu "obere mě to o peníze", ale pozornost. Chyba se projeví
jako frikce ve flow (nadbytečné kroky, přeskládané rozhraní, rozházené zkratky) nebo jako dojem,
že produkt je hračka. Obojí je tichý odchod bez stížnosti.

**Regulace vs volba.** Volby je tu víc než v jiných sektorech. European Accessibility Act 2019/882
jmenuje e-commerce, spotřebitelské bankovnictví, e-knihy, self-service terminály a dopravu, takže
B2B dev nástroj do jeho výčtu automaticky nespadá. Co váže tvrdě: zákon č. 99/2019 Sb. u českého
státního nebo municipálního klienta (WCAG 2.1 AA plus publikované prohlášení o přístupnosti),
Section 508 u federálních agentur USA (jen WCAG 2.0 AA) a ADA Title II u americké státní a místní
správy (WCAG 2.1 AA, deadline 26. 4. 2027 pro populaci nad 50 000 a 26. 4. 2028 pod). Nezávisle
na tom je WCAG AA v tomhle sektoru běžný požadavek v enterprise poptávkách, takže se vyplatí ho
držet i bez právní povinnosti.

**Klíčový nález o sektoru.** Dev-tool firmy publikují VÝKONOVÉ a PŘÍSTUPNOSTNÍ principy, téměř
nikdy vizuální. Stripe publikoval barvy jako přístupnostní problém. GitHub Primer publikuje flow,
rychlost, kompaktnost a přístupnost od začátku. Linear má brand principy o odstupu od assetů
a Method dokument o produktové filozofii, žádná vizuální pravidla. Praktický důsledek: když
v tomhle sektoru hledáš oporu pro rozhodnutí, hledej ji ve výkonu a přístupnosti. Vizuální oporu
nehledej, sektor ji nepublikuje. "Linear look", tedy temný podklad, vysoká hustota a jemné
1px bordery, není nikde publikovaně odůvodněný. Je to konvence, třída C.

Legenda tříd: A = tvrdá opora (měření), B = publikovaná konvence nebo regulace, C = řemeslná praxe
či pozorování bez opory.

Sesterské noty: [e-commerce.md](e-commerce.md), [luxury.md](luxury.md), [vlada.md](vlada.md)
(rozpis regulatorních rámců a WCAG parametrů), [finance.md](finance.md),
[zdravotnictvi.md](zdravotnictvi.md), [seniori.md](seniori.md), [deti.md](deti.md).

---

## Pravidla

### Barevný systém odvozuj v percepčně uniformním prostoru

**PRAVIDLO:** Barevné škály generuj v CIELAB nebo LCH, ne krokováním v HSL nebo RGB. Cíl je,
aby žádná barva na téže úrovni škály nevystupovala nad ostatní.
**KDY PLATÍ:** Vždy, když má paleta víc barevných rodin a víc úrovní (typicky sémantické barvy
success/warning/danger/info krát 5 až 10 odstínů).
**PROČ:** Různé odstíny jsou vnímané jako různě světlé i při stejné číselné světlosti. Stejná
`lightness` v HSL u modré a u žluté nedá stejnou vnímanou světlost, takže systém postavený v HSL
má nechtěnou hierarchii: jedna sémantická barva vždy křičí víc než ostatní. CIELAB je navržený
tak, aby číslo odpovídalo vnímání, takže "stejná úroveň" v něm opravdu znamená stejná úroveň.
**TŘÍDA:** B (publikovaná konvence, bez user testu).
**ZDROJ:** Stripe, Accessible color systems (2019), `stripe.com/blog/accessible-color-systems`,
verbatim: "different hues are inherently perceived as different levels of lightness", cíl
"no single color appears to take priority".
**KDY NEPLATÍ:** Jednorázová marketingová stránka se dvěma nebo třemi barvami, kde není škála,
kterou by šlo porušit. Tam je to zbytečná režie.

### Přístupné neznamená výrazné

**PRAVIDLO:** Každou kombinaci textu a pozadí v paletě navrhni na 4,5:1 a UI prvky, okraje inputů,
ikony a focus indikátory na 3:1, a ověř to dřív, než paletu schválíš. Když barva neprojde, uber
saturaci nebo posuň světlost. Neslevuj z kontrastu.
**KDY PLATÍ:** Každá paleta, která jde do produktu. U veřejného sektoru je to právní požadavek.
**PROČ:** Kontrast je testovatelný a nástrojově podporovaný, takže je to jediná část palety, která
se dá ověřit strojem a nemusí se o ní diskutovat. Zároveň platí, že sytost a přístupnost jdou
v praxi proti sobě: syté značkové barvy skoro nikdy neprojdou na text.
**TŘÍDA:** B (regulace WCAG 1.4.3 a 1.4.11, plus konvence Stripe "Accessible doesn't mean vibrant").
**ZDROJ:** WCAG 2.0 SC 1.4.3 (4,5:1 text, 3:1 velký text), WCAG 2.1 SC 1.4.11 (3:1 pro UI
komponenty a grafiku), ověřeno proti W3C. Stripe, Accessible color systems.
**KDY NEPLATÍ:** 4,5:1 není percepční práh čitelnosti, je to odvozená regulatorní baseline
(3:1 z ISO 9241-3 a ANSI/HFES vynásobené faktorem 1,5, který podle vlastní diskuse W3C v issue
w3c/wcag#1705 nemá oporu). U světlého textu na tmavém pozadí, u tenkých řezů a u malých velikostí
ber 4,5:1 jako NEDOSTATEČNOU podmínku. Nikdy netvrď, že je to vědecky ověřená hranice.

### Přístupnost se řeší od začátku, ne jako fáze před vydáním

**PRAVIDLO:** Klávesovou obsluhu, focus stavy a sémantiku řeš ve fázi návrhu komponenty, ne
v auditu před releasem. Konkrétně: každý interaktivní prvek má viditelný focus stav s kontrastem
3:1 a dá se obsloužit klávesnicí bez myši.
**KDY PLATÍ:** Každá komponenta v produktu.
**PROČ:** Přístupnost dodaná zpětně znamená přepis komponenty, ne úpravu stylu, protože chybí
struktura (co je tlačítko, co je odkaz, jaký je pořádek fokusu). Focus ring dělej přes `box-shadow`,
ne `outline`, protože `outline` nerespektuje `border-radius` a Safari to opravil až v 16.4.
**TŘÍDA:** B pro princip (Primer), C pro technický detail focus ringu (craft).
**ZDROJ:** GitHub Primer, verbatim: "Accessibility and inclusive design needs to be considered
from the start." Detail focus ringu: `interfaces.rauno.me`.
**KDY NEPLATÍ:** Nic, tohle nemá výjimku. U prototypu, který se zahodí, se dá odložit, ale
prototypy mají tendenci se nezahazovat.

### Hustota a rychlost jsou designový parametr

**PRAVIDLO:** V pracovním rozhraní počítej počet viditelných řádků a počet kroků jako měřitelný
parametr. Neroztahuj řádkování a padding kvůli "vzdušnosti", když to sníží počet viditelných
řádků v tabulce, logu nebo seznamu.
**KDY PLATÍ:** Produktová rozhraní, kde uživatel pracuje opakovaně a dlouho: tabulky, logy,
seznamy issues, diffy, konzole.
**PROČ:** Cíl rozhraní je flow a soustředění, ne dojem z jednoho screenshotu. Když se na obrazovku
vejde méně řádků, uživatel scrolluje a ztrácí kontext, což je přesně to, co u opakované práce bolí.
**TŘÍDA:** B (publikovaná konvence).
**ZDROJ:** GitHub Primer, verbatim: "encourage flow, focus, and an experience that is fast
and compact."
**KDY NEPLATÍ:** Marketingová a onboardingová část produktu, kde uživatel čte poprvé a hustota
škodí. Taky WCAG 1.4.12 stanovuje podlahu: `line-height` musí být nastavitelný na 1,5násobek
velikosti písma bez rozbití layoutu, takže hustotu nelze získat pevně zamčeným řádkováním.

### Známé vzory přednostně, inovuj jen tam, kde je úspora

**PRAVIDLO:** U navigace, klávesových zkratek, tabulek, filtrů a formulářů použij vzor, který
uživatel zná z jiných nástrojů téže třídy. Inovuj jen tam, kde vzniká reálná úspora kroků nebo
času, a tu úsporu pojmenuj.
**KDY PLATÍ:** Struktura a pozice prvků, tedy to, co uživatel hledá, aniž by o tom myslel.
**PROČ:** Netypické umístění prvku znamená měřitelně víc fixací a delší nalezení. Kompenzovat
to lze vysokou vizuální saliencí a konvenčním vzhledem prvku, ale to je zaplacení, ne obejití.
Novost se vyplácí, dokud nezasáhne rozpoznatelnost kategorie: měň povrch, nesahej na strukturu.
**TŘÍDA:** A pro měřenou cenu odchylky, B pro formulaci v Primeru.
**ZDROJ:** Roth, Tuch, Mekler, Bargas-Avila, Opwis (2013), IJHCS 71(3), 228-235, N=40,
eye-tracking, reálné weby. Hekkert, Snelders, van Wieringen (2003), Brit J Psychol 94(1), 111-124:
"people prefer novel designs as long as the novelty does not affect typicality." GitHub Primer,
verbatim: "familiar patterns help people intuitively navigate."
**KDY NEPLATÍ:** Když je v sektoru zavedený vzor prokazatelně horší a máš na to vlastní data.
Pak je odchylka odůvodněná, ale zaplať ji saliencí a onboardingem.

### Nestylované primitivy: nediktuj vizuál

**PRAVIDLO:** Když stavíš komponentovou knihovnu pro cizí vývojáře, dodej chování, přístupnost
(ARIA, klávesnice, focus management) a stylovací háčky. Vizuální rozhodnutí nediktuj.
**KDY PLATÍ:** Knihovna určená ke použití v cizích produktech s cizím brandem.
**PROČ:** Většina komponent na webu je nepřístupná, a to je problém, který knihovna vyřešit může.
Vzhled je naopak to, co si spotřebitel knihovny musí určit sám, protože nese vlastní brand.
Absence vizuálního pravidla je v tomhle kontextu rozhodnutí, ne mezera v dokumentaci.
**TŘÍDA:** B (publikovaná konvence a explicitní rationale dvou rozšířených knihoven).
**ZDROJ:** Radix (`radix-ui.com`) rationale: nestylované primitivy s ARIA, klávesovou obsluhou
a focus logikou, protože většina komponent na webu je nepřístupná. shadcn/ui staví na tomtéž.
**KDY NEPLATÍ:** Interní design systém jedné firmy, kde je konzistence cílem. Tam vizuální
rozhodnutí naopak diktovat musíš, jinak se systém rozpadne na varianty.

### Temný hustý vzhled je konvence, ne evidence

**PRAVIDLO:** Temné pozadí, vysokou hustotu a jemné 1px bordery použij, když sedí produktu
a publiku. Neodůvodňuj to výzkumem ani tím, že to tak dělá Linear.
**KDY PLATÍ:** Vždy, když padne argument "tak to má Linear" nebo "je dokázáno, že vývojáři
preferují dark mode".
**PROČ:** Firmy, po kterých se tenhle vzhled kopíruje, ho nikde nezdůvodňují. Linear publikuje
brand principy o odstupu od assetů a produktovou filozofii, ne vizuální pravidla. Vzhled navíc
neseparuje příčinu od následku: kopíruje se to, co je vidět u úspěšné firmy, ne to, co ji
úspěšnou udělalo (halo efekt a survivorship bias).
**TŘÍDA:** C.
**ZDROJ:** Nenalezeno publikované odůvodnění (evidenční audit sektoru 7/2026). K halo efektu
a survivorship biasu diskuse "How Stripe Designs Websites",
`news.ycombinator.com/item?id=15838270`.
**KDY NEPLATÍ:** Dark mode jako uživatelská volba je legitimní funkce a nemá s tímhle pravidlem
nic společného. Pravidlo mluví o odůvodnění vzhledu, ne o existenci tmavého tématu.

### Vyhýbej se markerům generického AI vzhledu

**PRAVIDLO:** Na landing page a v produktu nepoužívej: barevné levé okraje karet, mřížku
zaoblených karet s emoji v hlavičce, dark mode s fialovým nebo hnědým textem na tmavém pozadí
pod 4:1, a přehuštěný monospace v "terminálové" estetice.
**KDY PLATÍ:** Marketingová a produktová prezentace v tomhle sektoru, kde je publikum na tyhle
markery citlivé a nahlas je pojmenovává.
**PROČ:** Publikum je čte jako signál, že stránka vznikla bez investice a bez údržby.
Nízká kvalita koreluje s časovou investicí a chybějící údržbou, ne se samotným použitím AI, ale
signál funguje bez ohledu na to, jak stránka vznikla. U dark mode s fialovým textem je to navíc
i skutečné porušení kontrastu.
**TŘÍDA:** C pro seznam markerů (komunitní pozorování), B pro kontrastní část (WCAG 1.4.3).
**ZDROJ:** Diskuse Scoring Show HN submissions for AI design patterns,
`news.ycombinator.com/item?id=47864393` (333 bodů). Autor jednoho z markerů ho označil za "stejně
spolehlivý signál jako em-dash".
**KDY NEPLATÍ:** Barevný okraj jako funkční kód (stav buildu, severita logu) je legitimní, pokud
barva není jediný nositel informace. Monospace v nástroji, který zobrazuje kód, je taky na místě.

---

## Co v tomhle sektoru NENÍ

| Tvrzení | Stav |
|---|---|
| "Linear look" (temný, hustý, jemné bordery) má publikované odůvodnění | NENALEZENO, konvence |
| Existuje vizuální design systém dev-tool firmy s user testy | NENALEZENO, publikují výkon a přístupnost |
| Radix a shadcn/ui mají vizuální pravidla | NEMAJÍ, a je to záměr, ne mezera |
| Vývojáři měřitelně preferují dark mode | v knihovně bez opory, netvrdit |

Poslední bod je datový: kontext "knihovna pro vývojáře" znamená ABSENCI diktovaného UX rozhodnutí.
Když v takovém projektu vizuální pravidlo chybí, není to nedodělek, je to správná odpověď.

## Souvisí

- [Kontext: e-commerce](e-commerce.md), když je v produktu placený plán a checkout, tam už platí
  EAA a tvrdší pravidla na formuláře
- [Kontext: luxury](luxury.md), pro srovnání sektoru, který nepublikuje nic
- [Kontext: senioři](seniori.md), když má produkt i netechnické publikum, například admin rozhraní
  pro klientovy zaměstnance
- [UX Laws](../zakony-principy/ux-laws.md), Fitts a Hick včetně oprav, na dimenzování cílů
  a rozhodování o délce menu
- [Osmibodová mřížka](../zakony-principy/osmibodova-mrizka.md), spacing škála pro hustá rozhraní
