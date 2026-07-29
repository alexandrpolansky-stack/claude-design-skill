# Kontext: luxury a prestižní positioning

**Tohle je nejslabší evidenčně podložený sektor v celé knihovně.** Většina konvencí, které se
v praxi používají (patkové písmo jako signál luxusu, pomalé animace jako signál kvality, tenké
řezy), jsou třída C: řemeslná zkušenost a vzájemné okopírování, ne výzkum. Nenašla se ani jedna
studie, která by je tvrdila. Žádný luxusní dům (LVMH, Gucci, Hermès) nemá publikovaný design
systém, takže ani referenční systém, na který by se dalo odkázat, neexistuje. Když někdo v tomhle
sektoru cituje výzkum, skoro vždy cituje něco z jiné domény.

Poctivý postoj: v luxury se rozhoduje podle brand konzistence, referencí a řemesla, a to se řekne
nahlas. Nevyrábět si oporu, která neexistuje, jen aby rozhodnutí vypadalo podložené.

**Kdo je čtenář.** Člověk, který o nákupu často nerozhoduje na webu. Rozhodnutí padá v butiku,
přes vztah, přes doporučení, přes kampaň jinde. Web drží positioning a slouží jako ověření, že
značka je pořád ta, za kterou se vydává. U dostupnějšího "premium" e-shopu je to ale jinak, tam
je metrikou konverze a platí [e-commerce nota](e-commerce.md), ne tahle.

**Dopad chyby.** Asymetrický a neměřitelný. Web, který vypadá levně, poškodí brand equity, ale
nikdo to nezachytí v čísle. Právě proto v sektoru není výzkum: chybí metrika, na které by se
experiment dal postavit.

**Regulace vs volba.** Volby je tu skoro všechno, s jednou tvrdou výjimkou. Když web prodává,
spadá do výčtu European Accessibility Act 2019/882 (e-commerce), který je živý od 28. 6. 2025
a vyžaduje EN 301 549, tedy prakticky WCAG 2.1 AA. To přímo koliduje s estetikou tenkých řezů
a nízkého kontrastu. Kontrast a velikost cíle nejsou stylová volba, jsou mantinel.

**Vrstvení, které platí i tady.** Strukturu a pozice (navigace, hledání, košík, login) neodchyluj.
Regulatorní parametry ber jako mantinel. Odchyluj povrch: paletu, písmo, fotografii, motion.
Tam je v luxury prostor a tam se novost vyplácí.

Legenda tříd: A = tvrdá opora (měření), B = publikovaná konvence nebo regulace, C = řemeslná praxe
či pozorování bez opory. C se nikdy nepovyšuje na A, ani když se tak v praxi cituje.

Sesterské noty: [e-commerce.md](e-commerce.md), [dev-tools-saas.md](dev-tools-saas.md),
[finance.md](finance.md), [vlada.md](vlada.md), [zdravotnictvi.md](zdravotnictvi.md),
[deti.md](deti.md), [seniori.md](seniori.md).

---

## Pravidla

### Whitespace jako nosný prvek, ne jako zbytek

**PRAVIDLO:** Dej obsahu výrazně víc prázdna než u běžného webu: hero s jedním objektem a jednou
větou, sekce oddělené řádově většími mezerami (na desktopu 96 až 160 px místo běžných 48 až 64 px),
a uvolněné místo nezaplňuj dalším sdělením.
**KDY PLATÍ:** Prestižní positioning, kde je cílem vnímaná hodnota, ne počet zobrazených položek.
**PROČ:** Prázdná plocha se čte jako ekonomický signál. Plocha, kterou si značka může dovolit
nechat nevyužitou, sděluje, že nemusí prodávat každým pixelem.
**TŘÍDA:** C. Jediná existující opora je Pracejus, Olsen, O'Guinn (2006 a 2013) o whitespace jako
ekonomickém signálu prestiže, ale exaktní výsledek NEOVĚŘEN (paywall), takže ani nevíme, jak silný
efekt naměřili a na jakém vzorku. Konkrétní pixelové hodnoty výše jsou řemeslná praxe, žádná
evidence žádnou hodnotu nestanovuje.
**ZDROJ:** Pracejus, Olsen, O'Guinn (2006, 2013), whitespace jako ekonomický signál. Primární text
nezískán, přesné znění výsledku a metodiku neuvádět.
**KDY NEPLATÍ:** Katalog a výpis produktů, kde uživatel potřebuje porovnávat. Prázdno tam mění
srovnávání na scrollování. Taky na mobilu, kde 160px mezera znamená, že na obrazovku nezbyde obsah.

### Patkové písmo není doložený signál luxusu

**PRAVIDLO:** Nepoužívej patkové písmo s odůvodněním "serif působí luxusně". Když ho použiješ,
odůvodni ho brand manuálem klienta nebo konkrétní dohledanou referencí v segmentu, a to odůvodnění
zapiš.
**KDY PLATÍ:** Vždy, když se volba písma obhajuje dojmem místo vstupem.
**PROČ:** Tvrzení "serif = luxus" nemá zdroj. Je to konvence okopírovaná mezi značkami, což je
legitimní důvod (typičnost kategorie se vyplácí), ale je to jiný důvod než ten, který se uvádí.
**TŘÍDA:** C, NENALEZENO. Žádná studie to netvrdí.
**ZDROJ:** Prohledáno v rámci evidenčního auditu sektoru (7/2026), nenalezeno nic. K obecnému
rozhodování o patkách viz [Serif a Sans Serif](../typography/serif-a-sans-serif.md).
**KDY NEPLATÍ:** Když brand manuál klienta patkové písmo předepisuje. Pak to není designové
rozhodnutí, ale vstup, a nepotřebuje evidenci.

### Tenký řez a nízký kontrast jsou porušení, ne styl

**PRAVIDLO:** Na tělo textu nepoužívej light a thin řezy ani světle šedou na bílé. Drž 4,5:1 pro
text a 3:1 pro okraje inputů, ikony a focus indikátory. U textu pod 24 px nesnižuj váhu pod regular.
**KDY PLATÍ:** Vždy. U webu, který prodává, je to navíc právní požadavek (EAA 2019/882 od 6/2025).
**PROČ:** WCAG 1.4.3 vylučuje světle šedý text na bílém, což je velká část "minimalistické"
prémiové typografie. WCAG 1.4.11 vynucuje viditelné okraje inputů a ikon, čímž vylučuje bezokrajové
"invisible UI". Poměr 4,5:1 je navíc u tenkých řezů a malých velikostí NEDOSTATEČNÁ podmínka, ne
dostatečná, protože model kontrastu ignoruje prostorovou frekvenci a polaritu.
**TŘÍDA:** B (regulace, právně vynutitelná u e-commerce v EU). Samostatné tvrzení "tenký řez
signalizuje prémiovost" je C, NENALEZENO, a jde proti tomuto pravidlu.
**ZDROJ:** WCAG 2.0 SC 1.4.3 a 2.1 SC 1.4.11 (ověřeno proti W3C), EN 301 549, European
Accessibility Act 2019/882 živý od 28. 6. 2025.
**KDY NEPLATÍ:** Na dekorativní velkoformátový text nad 24 px (nebo 18,66 px bold) platí mírnější
práh 3:1. Logo a čistě dekorativní grafika pod kontrastní kritéria nespadají.

### Pomalý pohyb neodůvodňuj kvalitou

**PRAVIDLO:** Interakční odezvu (hover, press, otevření menu, přepnutí tabu) drž do cca 200 ms.
Delší trvání dej jen dekorativním, neblokujícím přechodům, které nestojí mezi uživatelem a akcí.
Respektuj `prefers-reduced-motion`.
**KDY PLATÍ:** Vždy, když animace leží na cestě k akci.
**PROČ:** Prahová hodnota 200 ms na odezvu je konvence design engineeringu, ne měřený práh.
Tvrzení "pomalejší animace se čte jako vyšší kvalita" nemá zdroj nikde. Co je jisté: animace
na cestě k akci přidává čas k úkolu, a přerušitelná CSS transition se chová lépe než keyframes,
protože se dá zrušit v půlce.
**TŘÍDA:** C pro obojí. 200 ms je řemeslná konvence (Rauno Freiberg, `interfaces.rauno.me`),
"pomalé = kvalitní" je NENALEZENO.
**ZDROJ:** `interfaces.rauno.me` (Web Interface Guidelines), Emil Kowalski `emilkowal.ski` k volbě
transition místo keyframes. Obojí craft zdroje bez user testu.
**KDY NEPLATÍ:** Úvodní intro animace stránky, cinematický scroll v kampaňové microsite a přechod
mezi kapitolami příběhu. Tam je pohyb obsahem, ne odezvou, a delší čas je legitimní volba.

### Globální rozvržení nese estetiku, detail ne

**PRAVIDLO:** Investuj čas do celkové kompozice stránky (poměr ploch, umístění bloků, rytmus sekcí)
dřív než do mikro-detailů. Když je málo času, obětuj polish detailu, ne kompozici.
**KDY PLATÍ:** Prestižní positioning, kde je estetické hodnocení hlavní metrikou.
**PROČ:** Nízké prostorové frekvence, tedy to, co z obrázku zbyde po rozostření, nesou estetické
hodnocení unikátně. Detail k němu přidává málo. Zároveň mezi nízkými prostorovými frekvencemi
a hodnocením použitelnosti nebyla nalezena souvislost, takže kompozice řeší dojem, ne funkci.
**TŘÍDA:** A.
**ZDROJ:** Thielsch & Hirschfeld (2010), Ergonomics 53(8): "no connection between low spatial
frequencies and usability evaluations."
**KDY NEPLATÍ:** U funkčních obrazovek (checkout, účet, filtrování) rozhoduje funkce, ne dojem.
A studie neříká, že detail je zbytečný, jen že nese estetiku slabší než celek.

### Velký obraz místo jedné silné barvy

**PRAVIDLO:** Když stavíš vizuální dojem, postav ho na velké fotografii nebo na vyváženém poměru
obrazu a textu. Nestav ho na sytém odstínu jedné barevné rodiny přes celou stránku.
**KDY PLATÍ:** Homepage, kampaňová stránka, produktová prezentace.
**PROČ:** Ze tří testovaných designových kategorií vyšly velké obrázky a vyvážený poměr
obraz/text estetičtěji než silná barva jedné rodiny. Vyvážený poměr měl navíc nejlepší paměťovou
výbavnost.
**TŘÍDA:** A ve své doméně, C jako přenos. Doména studie jsou FIREMNÍ weby, ne luxury.
**ZDROJ:** Douneva, Jaron, Thielsch (2015/2016), Interacting with Computers 28(4), 552-567, N=458.
Kategorie SCOFA (silná barva jedné rodiny), LAPIC (velké obrázky), SAPAT (vyvážený poměr).
**KDY NEPLATÍ:** Když je monochromatická plocha vlastní brand asset značky (a je v manuálu), pak
je to vstup. Taky u produktu, který se nefotí dobře.

### Nekopíruj paletu sektoru mechanicky

**PRAVIDLO:** Když si uděláš vizuální audit segmentu, převezmi z něj strukturu a konvence (co
kde je, jak se to jmenuje), ne barevnou paletu. Paletu volej podle brandu a kontrastu.
**KDY PLATÍ:** Vždy, když vznikl "průzkum konkurence" a hrozí, že se z něj stane vizuální kopie.
**PROČ:** Typičnost pomáhá u struktury a umístění. U barevného konceptu je opora slabá a existuje
konkrétní protipříklad: méně typické palety byly hodnoceny atraktivněji než typické. Zároveň
platí, že novost se vyplácí přesně do chvíle, kdy začne narušovat rozpoznatelnost kategorie.
**TŘÍDA:** C. Protipříklad je nepublikovaná diplomová práce, na pravidlo to nestačí, jako varování
proti mechanickému kopírování ano.
**ZDROJ:** Hanchar (2012, diplomová práce, Basel), typičnost barevného konceptu šla proti trendu.
Protiváha: Hekkert, Snelders, van Wieringen (2003), Brit J Psychol 94(1), 111-124: typicalita
a novost jsou stejně silné prediktory preference a potlačují si vzájemně efekt, "people prefer
novel designs as long as the novelty does not affect typicality".
**KDY NEPLATÍ:** Když má barva v segmentu funkční význam (například kategorie produktu podle
barvy etikety), pak je součástí struktury, ne povrchu.

### Struktura a pozice zůstávají konvenční

**PRAVIDLO:** I u nejvíc stylizovaného webu drž navigaci, hledání, košík, login a kontakt na
konvenčních místech. Když se od pozice odchýlíš, zaplať to vysokou vizuální saliencí prvku
a jeho konvenčním vzhledem.
**KDY PLATÍ:** Každý web, který má víc než jednu obrazovku a nějakou transakci nebo dohledávání.
**PROČ:** Netypické umístění prvku znamená víc fixací a delší nalezení, měřeno eye-trackingem na
reálných webech. Kompenzovat to jde saliencí a tím, že prvek sám vypadá konvenčně, ale je to
zaplacení, ne obejití.
**TŘÍDA:** A.
**ZDROJ:** Roth, Tuch, Mekler, Bargas-Avila, Opwis (2013), IJHCS 71(3), 228-235, N=40,
eye-tracking, reálné weby.
**KDY NEPLATÍ:** Jednoúčelová kampaňová microsite bez navigace a bez transakce, kde uživatel nic
nehledá a stránka je jeden lineární příběh.

### Prodejní tlak je byznys rozhodnutí, ne vizuální

**PRAVIDLO:** Než začneš navrhovat, zjisti, jestli web má prodávat, nebo držet positioning.
Podle toho se rozhoduje struktura a hierarchie CTA, ne paleta.
**KDY PLATÍ:** Na začátku každého luxury projektu, ideálně před prvním wireframem.
**PROČ:** V luxury strategii je potlačený přímý prodej záměr, ne opomenutí. Anti-zákony říkají,
že luxus se nemá prodávat otevřeně a že reklama neslouží k prodeji. Když tohle klient sdílí,
prominentní "Koupit" na homepage jde proti positioningu. Když nesdílí, jde o e-shop a platí jiná
pravidla.
**TŘÍDA:** B (publikovaná konvence). Je to byznys strategie, ne vizuální design, a jako evidence
pro vizuální rozhodnutí ji nepoužívej.
**ZDROJ:** Kapferer & Bastien, The Luxury Strategy, anti-zákony luxusní strategie.
**KDY NEPLATÍ:** Accessible luxury a premium e-shop, kde je konverze hlavní metrikou. Tam platí
[e-commerce nota](e-commerce.md).

### Referenční design systém sektoru neexistuje, nahraď ho auditem

**PRAVIDLO:** Nehledej publikovaný design systém luxusního domu, žádný neexistuje. Místo toho
udělej vizuální audit 5 až 8 konkrétních webů v segmentu klienta, zapiš, co je společné, a označ
to datem a jako pozorování.
**KDY PLATÍ:** Kdykoliv je potřeba obhájit vizuální rozhodnutí a chybí opora.
**PROČ:** Pozorování s datem a vzorkem je poctivější a použitelnější než tradované pravidlo.
Za rok se z něj dá poznat, co bylo ověřené a co dojem.
**TŘÍDA:** C (metoda, ne nález).
**ZDROJ:** Vlastní postup. Analogie s tím, jak GOV.UK a NHS dokumentují "When to use" u komponent,
tedy rozhodnutí plus kontext, ne jen výsledek.
**KDY NEPLATÍ:** Když klient má vlastní brand manuál. Ten audit netrumfuje.

---

## Co v tomhle sektoru NENÍ

Seznam je stejně důležitý jako pravidla, protože brání tomu, aby se konvence citovala jako výzkum:

| Tvrzení | Stav |
|---|---|
| Patkové písmo signalizuje luxus | NENALEZENO, žádná studie to netvrdí |
| Pomalé animace signalizují kvalitu | NENALEZENO |
| Tenký řez a light weight signalizují prémiovost | NENALEZENO, navíc koliduje s WCAG 1.4.3 |
| Whitespace signalizuje prestiž | částečná opora, exaktní výsledek NEOVĚŘEN (paywall) |
| Publikovaný design systém luxusního domu | NEEXISTUJE (LVMH, Gucci, Hermès) |
| Konkrétní hodnota border-radius pro "prémiový" vzhled | NEEXISTUJE, evidence žádnou hodnotu nestanovuje |

Nepřenášej sem ani sektorová čísla o důvěryhodnosti z financí ([finance.md](finance.md)).
V datasetu, který ukazuje, že u financí je vizuál nejsilnější páka, kategorie luxury vůbec není.
Přenos by byl smyšlenka.

## Souvisí

- [Kontext: e-commerce](e-commerce.md), když web prodává a metrikou je konverze
- [Kontext: dev tools a SaaS](dev-tools-saas.md), pro srovnání sektoru, který publikuje výkon
  a přístupnost místo vzhledu
- [Serif a Sans Serif](../typography/serif-a-sans-serif.md), obecné rozhodování o patkách
- [Layout Theory](../layout/layout-theory.md), whitespace, margin, padding
- [Color Psychology](../color/color-psychology.md), s výhradou: psychologie barev je v knihovně
  vedená jako slabě doložená vrstva
