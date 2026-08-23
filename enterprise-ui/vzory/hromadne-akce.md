# Hromadné akce nad filtrovanou a stránkovanou množinou

Co znamená „vybráno", když je tabulka filtrovaná i stránkovaná, a co se stane, když dávková akce
selže jen zčásti. Tohle je nejběžnější enterprise obrazovka a zároveň místo, kde Carbon i většina
design systémů mlčí: popisují lištu dávkových akcí, ne sémantiku množiny, na kterou se akce použije.

Související: [Datové tabulky](../komponenty/datove-tabulky.md) ·
[Filtrování](filtrovani.md) · [Stránkování](../komponenty/strankovani.md) ·
[Běžné akce](bezne-akce.md) · [Dialogy a panely](dialogy-a-panely.md) ·
[Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md)

## Rychlé rozhodnutí

1. **Pojmenuj tři množiny a nikdy je nezaměňuj:** vybrané řádky, výsledek filtru, celá tabulka.
2. **Checkbox v hlavičce vybírá jen aktuální stránku.** Nikdy ne celý výsledek filtru.
3. **Když je vybraná celá stránka a filtr má víc záznamů, nabídni druhý krok:** „Vybrat všech 4 812
   odpovídajících". Až tohle je výběr nad filtrem.
4. **Výběr ruš při každé změně pohledu** (stránka, řazení, filtr) a oznam to. Držet ho přes
   stránky smíš jen tehdy, když je vidět souhrn toho, co je vybráno mimo obrazovku.
5. **Počet vybraných piš do každého labelu akce.** „Smazat 12 uživatelů", ne „Smazat".
6. **U nevratné dávky nesmí potvrzení znít obecně.** Nech uživatele napsat počet, ne název.
7. **Dávka selhává po částech.** Návrh musí umět „197 hotovo, 3 selhaly" včetně toho, které.
8. **Nikdy neposílej dávku, u které nevíš, kolik položek zasáhne.**

## Tři množiny, které se pletou

| Množina | Co to je | Kde vzniká |
|---|---|---|
| **Vybrané řádky** | To, co uživatel zaškrtl | Checkboxy v řádcích |
| **Výsledek filtru** | Všechno, co odpovídá filtru, napříč stránkami | Filtr plus hledání |
| **Celá tabulka** | Všechno bez filtru | Zrušení filtrů |

**PRAVIDLO:** V UI smí být jednou akcí zasažena vždy jen jedna z těch tří množin a uživatel musí
z obrazovky poznat, která to je. Když to z labelu a z potvrzení nepoznáš ty při návrhu, nepozná to
ani uživatel.
**KDY PLATÍ:** Každá tabulka, která má zároveň výběr a stránkování nebo filtr.
**PROČ:** Záměna „vybrané" a „odpovídající filtru" je u mazání nevratná a tichá. Uživatel klikne
v domnění, že maže 25 řádků na stránce, a smaže 4 812.
**TŘÍDA:** C. Vlastní syntéza, nedohledal jsem k tomu měření ani normativní text.
**KDY NEPLATÍ:** Tabulka bez stránkování a bez filtru, kde jsou všechny tři množiny totožné.

## Checkbox v hlavičce: co vybírá

Carbon popisuje mechaniku, ne rozsah.

**ZDROJ (třída B):** Carbon, Data table usage, Selectable. Verbatim: „The user can select all rows
at once by selecting the checkbox in the column header. Checkboxes in the rows have only two states,
checked and unchecked. However, the check all checkbox in the column header has three states, check,
unchecked, and indeterminate."
https://carbondesignsystem.com/components/data-table/usage/

**Co Carbon neříká:** co je „all rows", když je tabulka stránkovaná. Zbytek téhle sekce je doplnění
knihovny, třída C.

**PRAVIDLO:** Checkbox v hlavičce vybere **řádky aktuální stránky**, nic víc. Když existuje víc
odpovídajících záznamů než na stránce, zobraz hned pod hlavičkou pruh s druhým krokem:

```
Vybráno 25 řádků na této stránce.  [Vybrat všech 4 812 odpovídajících filtru]
```

Po použití druhého kroku se pruh změní na stav, ze kterého jde vycouvat:

```
Vybráno všech 4 812 záznamů odpovídajících filtru.  [Zrušit výběr]
```

**PROČ:** Dvoukrokový výběr je jediný způsob, jak odlišit „stránka" od „filtr" bez toho, aby si
uživatel musel domýšlet rozsah. Jednokrokové „vybrat vše" nutně znamená jednu z těch dvou věcí
a druhá se pak stane omylem.
**TŘÍDA:** C. Pozorovaná konvence, ne měření: takhle to řeší Gmail, GitHub i Google Drive.
Zdrojem je pozorování produktů, ne studie.
**KDY NEPLATÍ:** Když výsledek filtru vždycky vejde na jednu stránku. Pak druhý krok jen mate.

## Co se stane s výběrem při navigaci

Tady si dva zdroje odporují a rozpor je zapsaný, ne zameten.

**Cloudscape (AWS), třída B.** Verbatim: „The parent checkbox, living on the table header, only
selects rows visible on the page. Any actions triggered after selection only affects the selected
visible rows. **Selection is overwritten by: Table sorting, Pagination, Preferences**, and as soon
as they are no longer visible on the page."
https://cloudscape.design/patterns/resource-management/view/table-view/

**Původní znění téhle noty, třída C,** naopak velelo výběr přes stránkování a řazení držet.
**Cloudscape vyhrává,** protože publikovaná konvence systému, který jede na konzoli AWS, je tvrdší
opora než řemeslná úvaha. Držení výběru přes stránky ale zůstává legitimní, jen za podmínky, kterou
většina implementací nesplní.

**PRAVIDLO:** Výchozí chování je **výběr zrušit při každé změně pohledu**. Držet ho smíš jen tehdy,
když zároveň ukážeš, co je vybráno mimo obrazovku.

| Akce uživatele | Výchozí (bezpečné) | Smíš držet, když... |
|---|---|---|
| Přepnutí stránky | **Zruš** | ...je vidět souhrn („Vybráno 30 na 3 stránkách") a jde otevřít, co v něm je |
| Řazení | **Zruš** | ...totéž |
| Změna počtu položek na stránku | **Zruš** | ...totéž |
| Změna filtru nebo hledání | **Zruš vždy** | Nikdy. Filtr mění samotnou množinu |
| Odchod ze stránky a návrat | **Zruš vždy** | Nikdy |

**KDY PLATÍ:** Vždy, když výběr přežívá déle než jednu obrazovku dat.
**PROČ:** Obě strany chrání něco jiného a obojí je skutečné. Zrušení chrání před akcí nad řádky,
které uživatel nevidí, a to je u nevratného mazání ta dražší chyba. Držení chrání rozdělanou práci
u někoho, kdo vybírá napříč stránkami. Rozhodující je, že **držení bez viditelného souhrnu spojuje
nevýhody obojího**: uživatel má vybráno něco, co nevidí, a přitom o tom neví.
**TŘÍDA:** B pro výchozí zrušení (Cloudscape), C pro podmínku, za které jde výběr držet.
**ZDROJ:** Cloudscape Design System, Table view, viz citace výše. Apache 2.0.
**KDY NEPLATÍ:** Tabulka, která se celá vejde na jednu stránku. Tam žádná změna pohledu výběr
neschová.

**Když výběr zrušíš, řekni to.** Tiché zrušení vypadá jako chyba: uživatel odklikal dvacet
checkboxů, přepnul řazení a je pryč. Krátká zpráva („Výběr zrušen, změnilo se řazení") stojí jeden
řádek a ušetří zopakování celé práce.

## Label akce nese počet

**PRAVIDLO:** Každý label dávkové akce obsahuje počet zasažených položek a jejich typ.
„Smazat 12 uživatelů", ne „Smazat". Platí pro tlačítko v liště, pro položku v menu i pro primární
tlačítko v potvrzovacím dialogu.
**KDY PLATÍ:** Vždy u dávky.
**PROČ:** Počet je jediná informace, která odliší „smazat vybrané" od „smazat vše", a je to poslední
místo, kde si uživatel může všimnout, že vybral jinou množinu, než myslel.
**TŘÍDA:** B pro princip (knihovna má pravidlo, že destruktivní akce nese v labelu, co konkrétně
zmizí, viz [Tlačítka](../../ux-design/pravidla/tlacitka.md)), C pro tvar s číslem.

## Potvrzení u nevratné dávky

Knihovna má tři úrovně dopadu mazání v [Běžné akce](bezne-akce.md). U high-impact velí Carbon nechat
uživatele **napsat název mazaného zdroje**. To u dávky nefunguje, protože žádný jeden název
neexistuje.

**PRAVIDLO:** Náhradou za název je **počet**. U nevratné dávky nad hranicí, kterou si produkt určí,
nech uživatele opsat počet mazaných položek do pole. Pod tou hranicí stačí danger dialog s počtem
v labelu.

| Situace | Potvrzení |
|---|---|
| Vratná dávka (jde vzít zpět) | Žádné. Proveď a nabídni undo |
| Nevratná dávka, malý počet | Danger dialog, počet v labelu, focus na Zrušit |
| Nevratná dávka, velký počet nebo drahá data | Danger dialog plus opsání počtu do pole |
| Právní, finanční, nebo mazání uživatelských dat | Krok kontroly se seznamem toho, co zmizí, před potvrzením |

**PROČ:** Ruční potvrzení má fungovat jako zpomalovač, ne jako test paměti. Číslo, které má uživatel
opsat, je zároveň to jediné, co potřebuje zkontrolovat.
**TŘÍDA:** A pro poslední řádek (WCAG 3.3.4 Error Prevention (Legal, Financial, Data), Level AA,
vyžaduje vratnost, kontrolu nebo potvrzení), C pro odstupňování a pro tvar s opsáním počtu.
**ZDROJ:** WCAG 2.2 SC 3.3.4. https://www.w3.org/WAI/WCAG22/quickref/ · Tři úrovně dopadu:
Carbon, Common actions, Delete, viz [Běžné akce](bezne-akce.md).
**KDY NEPLATÍ:** Undo. Když akce jde vzít zpět, potvrzení jen zdržuje. Undo je lepší než dialog.

**Focus v danger dialogu patří na Zrušit**, ne na červené tlačítko. Detail v
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md).

## Částečné selhání

Dávka není jedna operace. Je to N operací, které mohou dopadnout různě, a návrh, který počítá jen
s „hotovo" a „selhalo", tenhle stav prostě nezobrazí.

**PRAVIDLO:** Každá dávková akce má tři možné výsledky, ne dva: **všechno prošlo**, **nic neprošlo**,
**prošla část**. Třetí stav musí umět říct kolik, které a co s tím.

| Výsledek | Co ukázat |
|---|---|
| Všechno prošlo | Success notifikace s počtem. Vybrané odznač, řádky animovaně odeber |
| Nic neprošlo | Error notifikace s důvodem. **Výběr nech být**, ať jde akce zopakovat |
| Prošla část | Warning notifikace s oběma počty plus odkaz na seznam selhaných. Vybrané nech jen ty selhané |

**PROČ:** Když částečné selhání zobrazíš jako úspěch, uživatel odejde s tím, že je hotovo, a tři
záznamy zůstanou nezpracované navždy. Když ho zobrazíš jako chybu, zopakuje celou dávku, což u
nevratných akcí znamená druhý pokus o něco, co už proběhlo.
**TŘÍDA:** C.
**KDY NEPLATÍ:** Transakční dávka, kterou backend provede celou nebo vůbec. Tam třetí stav
neexistuje a je dobré to v UI říct („Změny se použijí najednou").

**Ponechání selhaných ve výběru** je tady to podstatné: uživatel může rovnou kliknout znovu a týká
se to jen toho, co neprošlo.

## Průběh dlouhé dávky

**PRAVIDLO:** Dávku, u které znáš počet položek, ukazuj determinovaným progress barem s počtem
(„Zpracováno 140 z 200"), ne spinnerem. Nad hranici, kde uživatel odejde jinam, přesuň hlášení
do notifikace a pusť ho pryč.
**KDY PLATÍ:** Dávky nad 10 s.
**PROČ:** Počet položek je jediná veličina, kterou u dávky opravdu znáš dopředu, takže procenta
nemusíš odhadovat. Prahy čekání a volba indikátoru jsou v
[Načítání a čekání](nacitani-a-cekani.md) a v
[Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).
**TŘÍDA:** C pro vazbu na počet položek, B pro prahy (viz odkazované noty).

## Přístupnost

**PRAVIDLO:** Změna počtu vybraných a výsledek dávky musí projít do live region. Čtečka jinak
nezjistí ani to, že se něco vybralo, ani že se něco stalo.

| Událost | Co oznámit |
|---|---|
| Změna výběru | „Vybráno 12 z 4 812" |
| Vybrat vše nad filtrem | „Vybráno všech 4 812 záznamů" |
| Zrušení výběru filtrem | „Výběr zrušen, změnil se filtr" |
| Výsledek dávky | „Smazáno 197 z 200, 3 selhaly" |

**TŘÍDA:** A pro požadavek (WCAG 4.1.3 Status Messages, Level AA), C pro konkrétní znění.
**ZDROJ:** WCAG 2.2 SC 4.1.3 Status Messages. https://www.w3.org/WAI/WCAG22/quickref/
Drátování live region je v [Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md).

Lišta dávkových akcí se objevuje a mizí, takže je to změna kontextu. **Focus nepřesouvej**, jen
oznam. Když uživatel dávkový režim opustí tlačítkem cancel, focus patří zpět na checkbox, kterým
režim spustil.

## Co tahle nota neřeší

- **Stav filtru a stránky v URL.** Řeší [Stav pohledu v URL](stav-pohledu-v-url.md), včetně toho,
  proč tam výběr řádků nepatří.
- **Oprávnění na úrovni jednotlivého řádku.** „Nemůžu smazat sám sebe" a „nemůžu smazat posledního
  admina" jsou reálné případy a knihovna k nim nemá nic. Nejblíž je
  [Disabled versus read-only](disabled-vs-read-only.md), ale ta řeší prvek, ne pravidlo.
- **Výchozí počet položek na stránku.** Carbon popisuje komponentu „Items per page" a žádnou
  doporučenou hodnotu neuvádí, viz [Stránkování](../komponenty/strankovani.md).
- **Výběr napříč záložkami nebo pohledy.** Tahle nota počítá s jednou tabulkou.
- **Vzhled lišty dávkových akcí.** To je v [Datové tabulky](../komponenty/datove-tabulky.md).

## Zdroj

- Carbon Design System, Data table usage (Selectable, Batch actions).
  https://carbondesignsystem.com/components/data-table/usage/ Lokální kopie čtena 23. 8. 2026.
- Carbon Design System, Pagination usage.
  https://carbondesignsystem.com/components/pagination/usage/
- Cloudscape Design System (AWS, Apache 2.0), Table view. Zdroj pravidla o rušení výběru
  při změně pohledu. https://cloudscape.design/patterns/resource-management/view/table-view/
  Čteno 23. 8. 2026.
- WCAG 2.2, SC 3.3.4 Error Prevention (Legal, Financial, Data) a SC 4.1.3 Status Messages, Level AA.
  https://www.w3.org/WAI/WCAG22/quickref/
- Dvoukrokový výběr nad filtrem: pozorovaná konvence produktů (Gmail, GitHub, Google Drive), nikoli
  publikované měření. Proto třída C.

**Většina pravidel v téhle notě je třída C.** Carbon popisuje lištu dávkových akcí a tři stavy
hlavičkového checkboxu, ale sémantiku množiny, chování výběru při navigaci ani částečné selhání
nepokrývá. Kdyby se k tomu našlo měření nebo normativní text, tahle nota se má přepsat, ne doplnit.
