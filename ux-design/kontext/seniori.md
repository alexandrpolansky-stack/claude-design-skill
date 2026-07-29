# Kontext: senioři

**Kdo je čtenář.** Člověk nad 65 let, který sám sebe hodnotí jako méně schopného ve všech třech
dimenzích, na kterých rozhraní stojí: zrak 82 % (kontrolní skupina 95 %), obratnost 73 % (95 %),
paměť 49 % (63 %). To sebehodnocení se potvrzuje v naměřeném výkonu, není to skromnost.

**Dopad chyby.** Nejtvrději měřitelný ze všech sektorů v knihovně. Úspěšnost úkolu 55,3 % proti
74,5 % u kontrolní skupiny, čas na úkol 7:49 proti 5:28 (tedy o 43 % pomalejší), chyby 2,4 proti
1,1 na úkol. Chyba v designu se tady neprojeví jako nižší konverze, ale jako nedokončený úkol.

**Regulace vs volba.** Klíčové zjištění: samostatný "senior standard" neexistuje a nepotřebuje se.
Přehled literatury W3C WAI (2008) uzavřel, že kritéria WCAG potřeby stárnutí VĚCNĚ pokrývají,
a problém je jen POVĚDOMÍ o tom, že se dají takhle použít, ne chybějící kritéria. Praktický důsledek:
důsledné WCAG 2.1 AA je z velké části totéž jako "design pro seniory". Nestav oddělený senior mód,
splň AA na hlavním rozhraní a přidej jen to, co WCAG neřeší (čas, počet kroků, formulace, správa
oken).

**Vrstvení.** Struktura a pozice se neodchylují, u téhle populace stojí odchylka nejvíc. Regulatorní
parametry jsou mantinel a tady se vyplatí jít nad minimum. Povrch je volný.

Legenda tříd: A = tvrdá opora (měření), B = publikovaná konvence nebo regulace, C = řemeslná praxe
či pozorování bez opory.

Sesterské noty: [deti.md](deti.md), [e-commerce.md](e-commerce.md), [zdravotnictvi.md](zdravotnictvi.md)
(pozadí, dyslexie, stres), [vlada.md](vlada.md) (rozpis regulatorních rámců),
[finance.md](finance.md), [dev-tools-saas.md](dev-tools-saas.md), [luxury.md](luxury.md).

---

## Pravidla

### Žádný senior mód, důsledné WCAG AA na hlavním rozhraní

**PRAVIDLO:** Nestav oddělené zjednodušené rozhraní pro starší uživatele. Splň WCAG 2.1 AA
důsledně na hlavním rozhraní (1.4.3, 1.4.4, 1.4.10, 1.4.11, 1.4.12, 2.5.8) a přidej jen to, co
WCAG neupravuje: časové limity, počet kroků, jazyk a správu oken.
**KDY PLATÍ:** Každý produkt s podílem starších uživatelů, tedy prakticky každý veřejný web.
**PROČ:** Kritéria WCAG pokrývají věkové změny věcně, chybí jen vědomí, že se tak dají použít.
Oddělené rozhraní navíc znamená dvě verze k údržbě, z nichž jedna zaostane, a nutí uživatele
přiznat, že patří do zvláštní kategorie.
**TŘÍDA:** B (publikace W3C plus regulace).
**ZDROJ:** W3C WAI, přehled literatury o stárnutí a webové přístupnosti (2008): kritéria potřeby
stárnutí věcně pokrývají, problém je povědomí.
**KDY NEPLATÍ:** Specializované zařízení nebo klinické použití, kde jsou požadavky nad AA (fyzické
ovladače, velké dotykové plochy). A pravidlo neříká, že AA stačí, jen že oddělený mód není řešení.

### Minimálně 12pt tělo textu a funkčnost při 200 % zvětšení

**PRAVIDLO:** Default velikost těla textu minimálně 12pt (přibližně 16 CSS px) a rozhraní musí
zůstat funkční při zvětšení textu na 200 %, bez ztráty obsahu a bez horizontálního scrollu
na 320 CSS px.
**KDY PLATÍ:** Vždy.
**PROČ:** 12pt je naměřená podlaha z testování se seniory, ne odvozená hodnota. Podpora zvětšení
je důležitější než samotný default, protože uživatel, který si zvětšuje, to dělá kvůli zraku,
a rozbitý layout mu tu možnost bere.
**TŘÍDA:** A pro 12pt (NN/g, N=75), B pro 200 % (WCAG 1.4.4) a pro reflow (WCAG 1.4.10).
**ZDROJ:** NN/g, studie seniorů, N=75 (65 až 89 let) proti kontrole N=20 (21 až 55 let), doporučení
minimálně 12pt. WCAG 2.0 SC 1.4.4, WCAG 2.1 SC 1.4.10 (ověřeno proti W3C).
**KDY NEPLATÍ:** Převod pt na CSS px je aritmetika (72 pt na 96 px na palec), ale původní
doporučení vznikla pro desktopové obrazovky, takže na mobilu ber 16 px jako podlahu, ne jako cíl.

### Počítej s 43 % delším časem, nepoužívej časové limity

**PRAVIDLO:** Nepoužívej timeouty, mizející oznámení (toasty), automaticky rotující karusely
ani časové limity ve formulářích. Kde je timeout nezbytný (bezpečnost), dej ho prodloužit a upozorni
na něj předem.
**KDY PLATÍ:** Každý tok, kde uživatel něco čte, vyplňuje nebo opisuje.
**PROČ:** Naměřený čas na úkol byl 7:49 proti 5:28 u kontrolní skupiny, tedy o 43 % delší. Cokoliv,
co zmizí za pár sekund, tahle populace nestihne přečíst, a cokoliv s limitem nestihne dokončit.
**TŘÍDA:** A pro čísla, C pro konkrétní seznam vzorců, které z nich odvozuju.
**ZDROJ:** NN/g, studie seniorů, N=75 proti kontrole N=20: čas 7:49 vs 5:28, úspěšnost 55,3 %
vs 74,5 %, chyby 2,4 vs 1,1.
**KDY NEPLATÍ:** Bezpečnostní odhlášení v bankovnictví a zdravotnictví má důvod. Řešením je
varování před vypršením a možnost prodloužit, ne zrušení limitu.

### Drž flow na jedné stránce, žádné přepínání oken

**PRAVIDLO:** Nevyžaduj přepínání mezi taby ani okny. Co uživatel potřebuje opsat nebo porovnat
(kód z e-mailu, číslo objednávky, podmínky v PDF), drž na téže stránce nebo do stránky vlož.
Odkazy, které otevírají nové okno, používej minimálně a označuj je.
**KDY PLATÍ:** Registrace, ověřování, platba, srovnávání variant, souhlasy.
**PROČ:** 45 % seniorů v testování mělo problém se správou tabů v prohlížeči, tedy s tím udržet
přehled, kde vlastně jsou. K tomu se přidává paměťový limit: 3 až 5 chunků platí právě tehdy, když
uživatel nese informaci mezi kroky bez opory na displeji, což je přesně tenhle případ.
**TŘÍDA:** A pro podíl 45 %, A pro paměťový limit v podmínkách, kdy je měřitelný.
**ZDROJ:** NN/g, studie seniorů (45 % mělo problém se správou tabů). Cowan (2001), Behavioral and
Brain Sciences 24(1), 87-114, DOI 10.1017/S0140525X01003922: "three to five chunks... averaging
about four chunks", s explicitně vypsanými hraničními podmínkami (zablokované rehearsal a překódování,
podnět nedostupný při výbavnosti).
**KDY NEPLATÍ:** Na počet TRVALE VIDITELNÝCH položek se paměťový limit nevztahuje, viditelné menu
obě Cowanovy podmínky porušuje. Nezkracuj kvůli tomu navigaci, viz opravy
v [UX Laws](../zakony-principy/ux-laws.md).

### Cíle nad regulatorní minimum a relevantní je ten menší rozměr

**PRAVIDLO:** Klikatelné prvky dimenzuj nad AA minimum 24×24 CSS px, u primárních akcí blíž
44×44 CSS px, a dej mezi ně mezeru. Při dimenzování počítej s tím MENŠÍM z rozměrů výšky a šířky.
**KDY PLATÍ:** Všechny interaktivní prvky, nejvíc na dotykových zařízeních.
**PROČ:** Sebehodnocení obratnosti je 73 % proti 95 %. Pro 2D terče je nejlepším prediktorem
obtížnosti MENŠÍ z rozměrů: u tlačítka 200×24 px je relevantní rozměr 24, takže rozšiřovat široké
tlačítko do strany je bezcenné. U prstu navíc existuje podlaha absolutní přesnosti nezávislá na
rychlosti, kterou nelze vykoupit zpomalením. Jediný fix je zvětšit terč.
**TŘÍDA:** A pro modely, B pro prahy 24 a 44 px.
**ZDROJ:** MacKenzie & Buxton, CHI '92, N=12, 1170 trialů na subjekt: SMALLER-OF model r = .9501
proti status quo r = .8097, p < .001, verbatim "a clear refutation of applying the status quo model".
Bi, Li, Zhai, FFitts law, CHI 2013, N=12, R² >= 0,91. WCAG 2.2 SC 2.5.8 (24×24, AA),
WCAG 2.1 SC 2.5.5 (44×44, AAA).
**KDY NEPLATÍ:** Fittsův zákon modeluje ČAS při předpokládané konstantní chybovosti, chybovost
nepredikuje. Tvrzení "větší tlačítko znamená méně chyb" z Fittse nevyplývá, opora pro velký terč
u prstu je FFitts. Detail viz [UX Laws](../zakony-principy/ux-laws.md).

### Nevyžaduj, aby si uživatel něco pamatoval mezi kroky

**PRAVIDLO:** V multi-step formuláři zobrazuj už zadané hodnoty, dovol návrat bez ztráty dat
a nikdy nevyžaduj zapamatování kódu, čísla nebo instrukce mezi obrazovkami. Souhrn před potvrzením
je povinný.
**KDY PLATÍ:** Wizardy, checkout, registrace, ověřovací toky, dvoufaktorová autentizace.
**PROČ:** Sebehodnocení paměti je 49 % proti 63 %, což je největší rozdíl ze tří měřených dimenzí.
Limit 3 až 5 chunků platí přesně v téhle situaci, tedy když informace není na displeji.
**TŘÍDA:** A.
**ZDROJ:** NN/g, studie seniorů (sebehodnocení paměti 49 % vs 63 %). Cowan (2001), BBS 24(1),
87-114.
**KDY NEPLATÍ:** Opět: na viditelné položky se limit nevztahuje. A neznamená to zjednodušovat
obsah, znamená to nechat ho na obrazovce.

### Chyby pojmenuj u pole a textem

**PRAVIDLO:** Chybu ukaž u konkrétního pole, textem, s návodem, co udělat dál. Nespoléhej na barvu
ani na samotnou ikonu. Okraje inputů a chybové indikátory musí mít kontrast 3:1.
**KDY PLATÍ:** Každý formulář.
**PROČ:** Naměřená chybovost je 2,4 proti 1,1 chyby na úkol, takže uživatel se z chyby musí dostat
sám a častěji. Barva sama informaci nenese, protože ji část lidí nerozliší (barvoslepost u 8 % mužů
a 0,5 % žen). WCAG 1.4.11 navíc vyžaduje 3:1 na hranice inputů a indikátory, takže jemné šedé
na šedém není volba.
**TŘÍDA:** B (regulace a shoda systémů), A pro chybovost.
**ZDROJ:** WCAG 2.1 SC 1.4.11. USWDS (demografie barvosleposti, princip "start in black and white",
tedy nejdřív navrhnout bez barvy). NN/g, studie seniorů (chyby 2,4 vs 1,1).
**KDY NEPLATÍ:** Nic. U chybových stavů výjimka není.

### Nesahej na pozice a nepřeskládávej rozhraní

**PRAVIDLO:** Navigaci, hledání, login a košík drž na konvenčních místech, nepoužívej skryté menu
na desktopu a nepřeskládávej položky mezi stránkami ani podle frekvence použití.
**KDY PLATÍ:** Celé rozhraní, včetně adaptivních a personalizovaných částí.
**PROČ:** Netypické umístění znamená měřitelně víc fixací a delší nalezení. Rozhodovací čas roste
logaritmicky jen u naučené, prostorově STABILNÍ volby mezi známými alternativami, takže adaptivní
přeskládávání menu tu výhodu ruší a nutí uživatele znovu hledat. U populace, která je už tak o 43 %
pomalejší, se cena odchylky sčítá s tím zpomalením (to sčítání je moje odvození, ne měřený efekt).
**TŘÍDA:** A pro cenu odchylky a pro model rozhodovacího času, C pro odvození o kumulaci.
**ZDROJ:** Roth, Tuch, Mekler, Bargas-Avila, Opwis (2013), IJHCS 71(3), 228-235, N=40, eye-tracking,
reálné weby: typické umístění znamená méně fixací a rychlejší nalezení, netypickou pozici lze
kompenzovat vysokou saliencí a konvenčním vzhledem prvku. Cockburn, Gutwin, Greenberg, CHI 2007,
N=8: u nováčka je čas hledání v menu LINEÁRNÍ s délkou menu, logaritmický vztah nastupuje až
u experta s prostorovou pamětí.
**KDY NEPLATÍ:** Odchýlit se lze, ale zaplatíš viditelností. Když to musí být, dej prvku vysokou
salienci a konvenční vzhled.

### Světle šedý text a tenké řezy jsou u téhle populace nejhorší volba

**PRAVIDLO:** Nepoužívej světle šedý text na bílém ani light a thin řezy na tělo textu. U světlého
textu na tmavém pozadí a u malých velikostí ber 4,5:1 jako nedostatečnou podmínku a přidej rezervu.
**KDY PLATÍ:** Celá typografie rozhraní.
**PROČ:** Práh 4,5:1 je odvozený, ne měřený: vychází z 3:1 doporučeného ISO 9241-3 a ANSI/HFES
pro standardní text a zrak, vynásobeného faktorem 1,5, který má odpovídat ostrosti 20/40, popsané
jako "typical visual acuity of elders at roughly age 80". Ten faktor ale oporu nemá a W3C to má
zdokumentované u sebe. Prakticky: kritérium, které se prodává jako ochrana starších uživatelů,
je expertní úsudek, takže minimum splň, ale neber ho jako záruku čitelnosti.
**TŘÍDA:** B pro práh jako regulatorní baseline, B pro to, že to není percepční práh (dokumentováno
ve vlastní diskusi W3C).
**ZDROJ:** Understanding SC 1.4.3 (řetězec derivace). GitHub issue w3c/wcag#1705 (2021, uzavřeno
2024 bez změny dokumentace): číslo 1,50 u Arditi & Faye (2004) je INTERCEPT regrese, ne
multiplikátor; Bruce Bailey z AGWG verbatim: "I concur that Aries Arditi never suggested 4.5:1",
a k derivaci: "It is a rational basis, just not maybe a great one." Model navíc ignoruje
prostorovou frekvenci a polaritu.
**KDY NEPLATÍ:** Neznamená to, že se má honit AAA všude. 7:1 prakticky vylučuje pastelové palety
pro text, což je legitimní cíl (NHS ho deklaruje), ale je to rozhodnutí, ne povinnost.

---

## Co v tomhle sektoru NENÍ

| Tvrzení | Stav |
|---|---|
| Existuje samostatný standard přístupnosti pro seniory | NEEXISTUJE a nepotřebuje se, WCAG to pokrývá věcně |
| "4,5:1 je práh čitelnosti pro starší zrak" | odvozený, ne měřený, faktor 1,5 nemá oporu |
| "Senioři potřebují zjednodušené rozhraní" | v knihovně bez opory, měřené jsou čas, chyby a úspěšnost, ne potřeba jiného rozhraní |
| "Max 7 položek v menu, protože paměť" | vyvrácené, viz UX Laws, u top-level navigace evidence podporuje spíš širší menu |

## Souvisí

- [Kontext: děti](deti.md), druhý sektor s měřitelně jiným publikem, ale s opačnými pravidly
  o animaci a zvuku
- [Kontext: e-commerce](e-commerce.md), kombinace je nejčastější reálný případ (e-shop se starším
  publikem) a EAA tam navíc přidává právní povinnost
- [Kontext: dev tools a SaaS](dev-tools-saas.md), když admin rozhraní obsluhují netechničtí
  zaměstnanci klienta
- [UX Laws](../zakony-principy/ux-laws.md), Fitts, Hick, Miller a Cowan včetně oprav
- [Neuro-design master dokument](../../neuro-design/neuro-design-master.md), kognitivní zátěž
  a vedení pozornosti
