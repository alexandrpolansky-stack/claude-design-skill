# Kontext: vládní a veřejnosprávní weby

Čtenář je kdokoliv. Celá populace včetně lidí s postižením, seniorů, lidí s nízkou digitální
gramotností a lidí ve stresu (úřední lhůta, sociální nouze). Nemá alternativu: služba existuje
jen na tomhle webu. Dopad chyby je proto vyšší než jinde, občan nedokončí zákonnou povinnost
nebo nedosáhne na dávku. A většina mantinelů tu není designová volba, ale zákon: přístupnost
je právně vymahatelná v ČR, EU i USA. Volbou zůstává tón, obsah a povrch (paleta, typografie,
tvary) uvnitř těch mantinelů.

Legenda tříd: A = tvrdá opora (měření), B = publikovaná konvence nebo regulace,
C = řemeslná praxe či pozorování bez opory.

Sesterské noty: [zdravotnictvi.md](zdravotnictvi.md), [finance.md](finance.md).

---

### Identita provozovatele před vizuálem

**PRAVIDLO:** Ukaž na první obrazovce, kdo web provozuje: plný oficiální název instituce,
oficiální doména, kontakt, vazba na stát. Do rozpoznatelnosti provozovatele investuj dřív
než do vizuálních efektů.
**KDY PLATÍ:** weby vlády, samospráv, veřejné správy a neziskovek.
**PROČ:** Fogg 2002 (N=2684): u nonprofit a vládních webů lidé při hodnocení kredibility
spontánně zmiňují identitu provozovatele ve 28,9 % komentářů (průměr napříč sektory 8,8 %),
zatímco design look jen ve 39,4 % (podprůměr, průměr 46,1 %). Kredibilita se tu odvozuje od
toho, kdo za webem stojí, ne od toho, jak vypadá. Přesný opak financí, kde je vizuál nejsilnější
páka (viz [finance.md](finance.md)).
**TŘÍDA:** A
**ZDROJ:** Fogg et al. (2002), Consumer WebWatch study, N=2684, 10 kategorií webů.
**KDY NEPLATÍ:** není to povolení zanedbat vizuál, 39,4 % je pořád skoro dvě pětiny zmínek
a web musí projít vizuální prahovou zkouškou (Sillence 2004, viz
[zdravotnictvi.md](zdravotnictvi.md)). Data jsou z roku 2002 a z USA.

### Estetika se podřizuje přístupnosti

**PRAVIDLO:** Když se elegance a přístupnost střetnou, obětuj eleganci. Žádný vizuální nápad
nesmí snížit srozumitelnost, kontrast nebo ovladatelnost.
**KDY PLATÍ:** vždy v tomhle sektoru, publikum je celá populace bez možnosti odejít jinam.
**PROČ:** GOV.UK Design Principles (je jich 11) to říkají explicitně: "This is for everyone...
If we have to sacrifice elegance, so be it. We're building for needs, not audiences."
A princip "Do the hard work to make it simple": jednoduchost pro čtenáře je práce designéra,
ne vlastnost obsahu.
**TŘÍDA:** B (publikovaná konvence GOV.UK)
**ZDROJ:** https://www.gov.uk/guidance/government-design-principles
**KDY NEPLATÍ:** prakticky nikdy zde. Konflikt bývá falešný: dobrá typografie a vysoký kontrast
nejsou v rozporu s estetikou, jen s konkrétním estetickým nápadem.

### Právní režim urči před návrhem

**PRAVIDLO:** Než začneš navrhovat, urči, kterým rámcem je klient vázán, a z něj plynoucí
standard:

| Rámec | Koho váže | Standard | Stav |
|---|---|---|---|
| zákon č. 99/2019 Sb. | český stát a samosprávy | EN 301 549 (≈WCAG 2.1 AA) + povinné prohlášení o přístupnosti | v platnosti od 4/2019, tedy už dnes |
| Web Accessibility Directive 2016/2102 | veřejný sektor EU | EN 301 549 + prohlášení o přístupnosti | od 2018 |
| Section 508 | jen federální agentury USA | jen WCAG 2.0 AA, ne 2.1 | od 18.1.2018 |
| ADA Title II (28 CFR 35) | státní a místní správa USA | WCAG 2.1 AA | deadline 26.4.2027 (≥50 000 obyvatel), 26.4.2028 (menší) |
| 21st Century IDEA + OMB M-23-22 | federální weby USA | konzistence s USWDS, mobile-first, plain language (~8. třída) | od 20.12.2018 |

**KDY PLATÍ:** jakýkoliv web pro vládního nebo veřejnoprávního klienta. Pro českého státního
či municipálního klienta platí zákon 99/2019 Sb. bez přechodných lhůt: WCAG 2.1 AA plus
publikované prohlášení o přístupnosti.
**PROČ:** regulatorní mantinel, ne doporučení. Nesplnění je právní vada dodávky, ne vkusová.
**TŘÍDA:** B (regulatorní mantinel)
**ZDROJ:** zákon č. 99/2019 Sb. (substance potvrzena 4+ nezávislými sekundárními zdroji,
verbatim paragrafy neověřeny primárně); směrnice 2016/2102; Section 508; 28 CFR 35;
21st Century IDEA; OMB M-23-22.
**KDY NEPLATÍ:** nezaniká, mění se jen standard podle jurisdikce. Pozor na zastaralá data:
deadliny ADA Title II byly interim rulem z 4/2026 posunuty o rok, starší zdroje uvádějí
2026/2027 a to už neplatí.

### WCAG parametry, které reálně ořezávají designový prostor

**PRAVIDLO:** Dodrž tyhle prahy jako tvrdý floor:

| SC | Práh | Úroveň | Verze | Co reálně vylučuje |
|---|---|---|---|---|
| 1.4.3 Contrast (Minimum) | 4,5:1 text, 3:1 velký text | AA | 2.0 | světle šedý text na bílém, velkou část "minimalistické" typografie |
| 1.4.11 Non-text Contrast | 3:1 pro UI komponenty a grafiku | AA | 2.1 | bezokrajové inputy, jemné šedé ikony a focus indikátory ("invisible UI") |
| 1.4.12 Text Spacing | line-height ≥1,5×; mezera odstavců ≥2×; letter-spacing ≥0,12×; word-spacing ≥0,16× | AA | 2.1 | pevný line-height pod 1,5 a layouty, které se při override rozbijí |
| 1.4.10 Reflow | 320 CSS px bez horizontálního scrollu | AA | 2.1 | layouty závislé na desktopové šířce |
| 2.5.8 Target Size (Minimum) | 24×24 CSS px na klikací cíl | AA | 2.2 (nové) | drobné klikatelné ikony, zavírací křížky, těsné inline ovládání |

**KDY PLATÍ:** web pro vládního nebo veřejnoprávního klienta v EU/ČR nebo USA. Mimo tento
sektor je to pořád rozumný baseline (a v EU financích ho vynucuje EAA, viz
[finance.md](finance.md)).
**PROČ:** tohle jsou jediná místa, kde WCAG mluví konkrétním číslem přímo do vizuálního návrhu.
Dvě poznámky k poctivosti: 2.5.8 je nové ve WCAG 2.2, zatímco právní rámce výše odkazují na
2.0/2.1, takže 24×24 px nemusí být všude právně vymahatelné, drž ho i tak. A 4,5:1 je
regulatorní a testovatelný baseline, ne percepční práh čitelnosti: u světlého textu na tmavém
pozadí, tenkých řezů a malých velikostí ho ber jako nedostatečnou podmínku, ne jako cíl.
**TŘÍDA:** B (regulatorní mantinel)
**ZDROJ:** W3C WCAG 2.1 a 2.2, https://www.w3.org/TR/WCAG22/
**KDY NEPLATÍ:** prahy jsou minimum, ne optimum. Neplatí obrácená logika "splnili jsme AA,
takže je to čitelné".

### Plain language je součást návrhu

**PRAVIDLO:** Piš obsah v jednoduchém jazyce, cíl srozumitelnosti zhruba na úrovni 8. třídy.
Krátké věty, běžná slova, žádný úřední žargon. Jazyk plánuj spolu s layoutem, ne jako
copywriting nakonec.
**KDY PLATÍ:** právně závazné pro federální weby USA (OMB M-23-22 k 21st Century IDEA).
Jinde publikovaná konvence sektoru (GOV.UK "Do the hard work to make it simple").
**PROČ:** publikum je celá populace, průměrný čtenář webu instituce není právník instituce.
Složitý jazyk zvyšuje chybovost při úkonech, které mají právní následky.
**TŘÍDA:** B (regulace v USA, konvence jinde)
**ZDROJ:** OMB M-23-22 (verbatim neověřeno primárně, PDF; substance sekundárně potvrzena);
https://www.gov.uk/guidance/government-design-principles
**KDY NEPLATÍ:** odborné dokumenty pro odborné publikum (metodiky pro úředníky, legislativa
samotná). I tam ale plain language shrnutí nahoře pomáhá.

### Hranaté rohy: konvence bez teorie, nevydávej ji za vědu

**PRAVIDLO:** Strohý pravoúhlý vzhled ve stylu GOV.UK/USWDS drž jako sektorovou konvenci
(čtenář pozná "úřad"), ale nikdy ho neodůvodňuj psychologickým účinkem hranatosti.
**KDY PLATÍ:** vládní weby stavěné v tradici GOV.UK, USWDS a příbuzných systémů.
**PROČ:** GOV.UK nikdy nepublikoval odůvodnění svých hranatých rohů, žádná shape/radius škála
ve systému není. Je to konvence bez publikované teorie. Zajímavý kontrast: zdravotnictví (NHS)
se od GOV.UK odchýlilo k zaobleným rohům SE zdůvodněním, jenže to zdůvodnění se ukázalo jako
folklór bez existujícího zdroje (celý forenzní rozbor v [zdravotnictvi.md](zdravotnictvi.md)).
Vláda = nulový radius bez zdůvodnění, zdravotnictví = zaoblený radius se zdůvodněním, které
neobstálo. Hodnota konvence je v konzistenci a rozpoznatelnosti kategorie, ne v měřeném
účinku tvaru.
**TŘÍDA:** B pro "drž konvenci systému" (publikovaná praxe GOV.UK). Jakékoliv tvrzení
o psychologickém účinku hranatých či kulatých rohů je C.
**ZDROJ:** https://design-system.service.gov.uk (absence publikované radius škály
i odůvodnění).
**KDY NEPLATÍ:** když klient má vlastní závazný design systém. A není to pravidlo "vláda musí
být hranatá": odchylka je legitimní, jen ji neprodávej jako výzkumem podloženou.
