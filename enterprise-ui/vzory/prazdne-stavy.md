# Prázdné stavy

Co zobrazit v místě, kde nejsou data. Otevři, když navrhuješ seznam, tabulku, dashboard, dlaždici nebo
panel, který může být prázdný. Podle Carbonu jsou prázdné stavy nejčastěji první věc, kterou uživatel
v produktu uvidí, a zároveň se na ně nejčastěji zapomíná.

Doplňuje [Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md), sekce Prázdné stavy.
Ta má vlastní zdroje (NN/g, Baymard) a rozlišení tří druhů prázdna. Tahle nota přidává Carbonovu
anatomii, typologii a rozvržení.

Související: [Hledání](hledani.md) · [Načítání a čekání](nacitani-a-cekani.md) ·
[Datové tabulky](../komponenty/datove-tabulky.md)

---

## Anatomie

Carbon jmenuje pět částí, tři z nich volitelné:

1. **Obrázek** (volitelný): neinteraktivní, souvisí se situací.
2. **Titulek**: krátké a jasné vysvětlení. Kde to jde, formulovaný **pozitivně**. Carbonův vlastní
   příklad: „Start by adding data assets" je pozitivnější než „You don't have any data assets".
   Alternativa: „You don't have any data assets yet".
3. **Tělo**: jasně vysvětli, co je další akce, kterou se prostor naplní. Můžeš vysvětlit i proč je
   prostor prázdný a jaký je přínos toho kroku. Na primární akci lze odkázat třemi způsoby:
   tlačítkem pod textem, odkazem uvnitř textu, nebo **ukázáním na konkrétní prvek UI**.
4. **Primární akce** (volitelná): tlačítko nebo odkaz v textu.
5. **Sekundární výzva** (volitelná): například odkaz do dokumentace, jako odkaz pod textem.

**Proč je varianta „ukaž na prvek UI" zajímavá:** Carbon k ní dává důvod, který ostatní dvě nemají.
Učí uživatele, kde prvky jsou a jak bude úkony provádět příště.
**ZDROJ:** Carbon, Empty states pattern, Anatomy, verbatim: „Direct the user to the UI element (...)
This has the benefit of teaching the user where elements are and how they will perform tasks in the
future." https://carbondesignsystem.com/patterns/empty-states-pattern/

## Typologie: tři základní prázdné stavy

| Typ | Kdy nastane | Cíl stavu | Kdy ho použít |
|---|---|---|---|
| Bez dat | První použití, data ještě nejsou | Uživatel chápe, co v prostoru bude, až data budou, a ví, jak je přidat sám | Jednodušší situace, sekundární funkce, kde je lepší malé sousto informace |
| Reakce na akci uživatele | Hledání bez výsledku, potvrzení dokončeného procesu | Uživatel chápe, jak upravit dotaz nebo filtry. Nebo že proces úspěšně dokončil | Když potřebuješ dát zpětnou vazbu na interakci |
| Chybový stav | Chybí oprávnění, systémový problém, potřeba konfigurace | Uživatel chápe problém, a pokud existuje oprava, ví, co udělat, nebo má možnosti, jak to napravit | Když je něco v nepořádku a je potřeba zásah nebo řešení potíží. Vyšší míra detailu a konkrétnosti uživatele podpoří lépe |

**ZDROJ:** Carbon, Empty states pattern, tabulka „Basic empty states".
https://carbondesignsystem.com/patterns/empty-states-pattern/

**Rozlišení tří prázden má v knihovně i vlastní pravidlo** (bez oprávnění versus filtr nic nenašel
versus ještě nic nevytvořil), viz
[Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md). Carbon a to pravidlo se shodují,
Carbon k tomu navíc přidává tabulku chybových podtypů:

| Druh chyby | Vysvětli, proč nejsou data | Vysvětli, co může uživatel udělat |
|---|---|---|
| Oprávnění | Uživatel nemá právo data vidět | Navrhni postup, jak o přístup požádat |
| Systémový problém | Problém v navázaném systému brání dodání dat | Vysvětli, jak zjistí, co se stalo (například prohlédnout log aktivit) |
| Potřeba konfigurace | K přístupu k datům je nutná další konfigurace | Vysvětlení plus první krok konfigurace |
| Nepodporovaná akce | Například nahrání nepodporovaného typu souboru | Vysvětli, které typy souborů podporujete |

## Kolik obsahu: víc není lepší

**PRAVIDLO:** Hledej rovnováhu mezi situací a množstvím obsahu. Víc obsahu neznamená lepší řešení,
protože obsah na stránce má kognitivní cenu. Platí to zvlášť při prvním setkání s produktem, takže
rozsáhlejší edukativní momenty si nechej na primární funkce a složitější situace.
**KDY PLATÍ:** Každý prázdný stav.
**TŘÍDA:** B. Carbon mluví o „cognitive cost", ale studii necituje.
**ZDROJ:** Carbon, Empty states pattern, When to use, verbatim: „Strive for a balance between the
situation and the content you're providing. More content doesn't necessarily mean it's a better
solution as there is a cognitive cost for having more content on the page."
https://carbondesignsystem.com/patterns/empty-states-pattern/

## Rozvržení

**Zarovnání:** prvky prázdného stavu zarovnej vlevo jako blok. **Jediná výjimka** je prázdný stav
v malé dlaždici: tam dej obrázek vycentrovaný nad vlevo zarovnaný text a akci. Carbon k té výjimce
dává důvod: aby prázdný stav nevypadal příliš jako obsah, který lze přeskočit. Vycentrovaný obrázek
v malém prostoru přitáhne pozornost ke stavu, který může vyžadovat akci.

**Malé prostory** (malé dlaždice, boční panely):

- Obrázek má souviset se situací.
- Velikost prostoru určuje velikost obrázku. Když je místa málo, použij jen text.

**Velké prostory** (velká dlaždice, tabulka, celá stránka), dvě volby pro každou osu:

- Poloha bloku: buď širší levý okraj, nebo blokově vycentrovaný vlevo zarovnaný blok.
- Poloha obrázku: nad titulkem (lepší pro širší obrázky), nebo vlevo od bloku (lepší pro vyšší).

**ZDROJ:** Carbon, Empty states pattern, Visual guidelines.
https://carbondesignsystem.com/patterns/empty-states-pattern/

## Dvě pravidla, na která se zapomíná

### Prázdný stav nahrazuje prvek, který by se normálně zobrazil

**PRAVIDLO:** Prázdný stav tabulky nahradí tabulku včetně záhlaví a zápatí, ne se přidá k prázdné
tabulce. Stejně u hledání: podkladový obsah se nahradí zprávou o nulovém výsledku.
**PROČ:** Carbon dává přístupnostní důvod: jinak čtečka přečte celou tabulku, než dojde ke zprávě,
že v ní nic není.
**TŘÍDA:** B
**ZDROJ:** Carbon, Empty states pattern, Best practices, verbatim citace v
[Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md).
https://carbondesignsystem.com/patterns/empty-states-pattern/

### Víc prázdných stavů na jedné obrazovce má jiná pravidla

**PRAVIDLO:** Když může být na obrazovce víc prázdných stavů zároveň (dashboard, kde se nepodaří
načíst víc widgetů), použij pro výzvu k akci **terciární** tlačítko, aby na obrazovce nebylo víc
primárních tlačítek. A zvaž prázdný stav jen s textem, bez ilustrace, protože opakovaná ikona ztrácí
účinek.
**KDY PLATÍ:** Dashboardy, mozaiky widgetů, obrazovky s víc panely.
**TŘÍDA:** B
**ZDROJ:** Carbon, Empty states pattern, verbatim: „In situations where there could be multiple empty
states showing at once, we recommend using a tertiary button for the call to action. This avoids
scenarios with multiple primary action buttons in the UI." a „the repetition of the empty state may
not have the same impact if you use illustrative icons. In this case, an empty state that uses just
text may be preferable." https://carbondesignsystem.com/patterns/empty-states-pattern/
**Souvislost:** Carbon má i obrácené pravidlo u tlačítek: v prázdném stavu na stránce, která už má
primární akci, je terciární tlačítko ideální volbou pro spuštění nového toku.
https://carbondesignsystem.com/components/button/usage/

## Do a Don't

Carbonovy seznamy pro stav bez dat:

**Do:** buď konkrétní v tom, co v prostoru bude, až tam data budou. Drž slova na minimu, aby se
daly rychle přečíst a odbavit. Když existuje další krok, dej do textu přímý odkaz nebo primární
tlačítko, nebo naveď na to, na co má uživatel kliknout.

**Don't:** nepokrývej víc možností jedním prázdným stavem (když jich je víc, vyber nejdůležitější
a drž fokus na ní). Nepoužívej produktové termíny, které uživatel ještě nemusí znát. Nedávej do
prázdného stavu obsah o jiných částech aplikace, buď kontextový. A jako obecné pravidlo nevoď
uživatele do slepé uličky.

Carbonovy seznamy pro chybový prázdný stav navíc:

**Do:** proberte s týmem, jaké informace jsou vůbec k dispozici. Použij přímý, prostý jazyk.
Buď k uživateli ohleduplný, nevtipkuj a nepiš lehkovážně. Obrázky musí odpovídat situaci a být
citlivé k tomu, že to může být vážná situace.

**Don't:** nevoď do slepé uličky, vždycky nabídni cestu k řešení. Když je věcí k vyzkoušení víc,
udělej mezi nimi hierarchii, aby bylo jasné, která je primární akce.

**ZDROJ:** Carbon, Empty states pattern, sekce Do a Don't u obou typů.
https://carbondesignsystem.com/patterns/empty-states-pattern/

## Chybový prázdný stav navazuje na Nielsenovu heuristiku

Carbon chybové prázdné stavy explicitně opírá o devátou Nielsenovu heuristiku „Help users recognize,
diagnose, and recover from errors" a cituje ji verbatim: „Error messages should be expressed in plain
language (no codes), precisely indicate the problem, and constructively suggest a solution."
Zdroj: Jakob Nielsen, 10 Usability Heuristics for User Interface Design, NN/g, 1994.
https://www.nngroup.com/articles/ten-usability-heuristics/
Na text chybové hlášky Carbon dál odkazuje na NN/g Error Message Guidelines.
https://www.nngroup.com/articles/error-message-guidelines/

## Když základní prázdný stav nestačí

Carbon nabízí tři náročnější alternativy pro první použití. Obecné vodítko, které k tomu dává:
primární zdroj na stránce může těžit z edukativnějšího přístupu, u sekundárních zdrojů stačí základní
prázdný stav.

| Typ | Kdy | Co je za to |
|---|---|---|
| Inline dokumentace | Zavádíš primární funkci a je příležitost ukázat přínos používání | Vyšší nároky na údržbu, hlavně když použiješ produktové screenshoty (a při lokalizaci navíc lokalizované obrázky) |
| Onboarding | Primární funkce vyžaduje vysvětlení konceptů nebo provedení celým flow | Onboarding je typicky volitelný, takže **musí** existovat i základní prázdný stav |
| Startovní obsah | Složité situace: uživatel si hraje se vzorovými daty a učí se šťouráním | Vyžaduje plánování s celým produktovým týmem. A když jde startovní obsah smazat, potřebuješ základní prázdný stav jako záložní |

**ZDROJ:** Carbon, Empty states pattern, In-depth alternatives, tabulka „Alternative approaches".
https://carbondesignsystem.com/patterns/empty-states-pattern/
Carbon u startovního obsahu cituje Jenifer Tidwell, Designing Interfaces (O'Reilly, 2. vydání, 2011),
s. 9: „When someone feels like she can explore an interface and not suffer dire consequences, she's
likely to learn more (...) than someone who doesn't explore."

## Otázky, které si Carbon velí položit v návrhu

1. Jak budou stránky, dlaždice, tabulky a boční panely vypadat bez obsahu?
2. Jaké všechny kroky může uživatel udělat, aby situaci vyřešil?
3. Existuje užitečný obsah, který by šlo zobrazit?
4. Jak z téhle situace udělat něco zajímavého a užitečného?

**ZDROJ:** Carbon, Empty states pattern, Designing with empty states.
https://carbondesignsystem.com/patterns/empty-states-pattern/

---

## Co tahle nota neřeší

- Prázdný výsledek hledání do detailu, včetně toho, proč nesmí být slepá ulička (Baymard).
  [Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).
- Text chybové hlášky a zakázaný slovník. Tamtéž, s tvrdšími zdroji.
- Rozdíl mezi prázdným a chybovým stavem po straně tónu. Tamtéž, tabulka tří tříd chyb.
- Chybové stavy jako samostatný vzor. Carbon ho v době snímku dokumentace **neměl**, uvádí ho jako
  plánovaný.

## Zdroj

IBM Carbon Design System, Empty states pattern, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/patterns/empty-states-pattern/
Carbon k tomuhle vzoru cituje NN/g (Error Message Guidelines 2001, Top 10 Application-Design Mistakes
2019, 3 Guidelines for Search Engine „No Results" Pages 2014), Tidwell 2011 a WCAG.
Třída **B** pro vzor, **A** pro odkazované WCAG požadavky na dekorativní obrázky.
