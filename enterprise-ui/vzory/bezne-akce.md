# Běžné akce: co která znamená a jak se podává

Slovník opakujících se akcí. Carbon je definuje záměrně úzce a velí je používat **jen** popsaným
způsobem, aby byla platforma konzistentní.

Související: [UX copy v produktu](../zaklady/ux-copy-v-produktu.md) ·
[Tlačítka: varianty a volba](../komponenty/tlacitka-varianty.md) ·
[Dialogy a panely](dialogy-a-panely.md) · [Filtrování](filtrovani.md)

---

## Rychlé rozhodnutí

1. **Delete** zničí objekt. **Remove** ho jen vyjme ze seznamu, objekt zůstane. Nezaměňuj je.
2. **Clear** vymaže data z pole nebo výběr. **Reset** vrátí hodnoty do posledního uloženého stavu.
3. Mazání se odstupňuje podle dopadu: bez varování / potvrzení / **opsání názvu** ručně.
4. Zrušit = sekundární tlačítko nebo odkaz. Zavřít = ikona křížku, **nikdy tlačítko**.
5. Reset = typicky odkaz.
6. Po smazání se vrať na stránku se seznamem, animuj odebrání a dej success notifikaci.
7. Když mazání selže, zvedni notifikaci, a když to jde, pošli druhou jiným kanálem (e-mail).
8. U každé akce s dopadem si projdi Carbonův seznam otázek (níže).

---

## Kontrolní otázky, které Carbon dává u akcí s dopadem

Carbon je uvádí u **Add** a shodně u **Remove**. Jsou přenositelné na jakoukoliv akci:

1. Jaké to má pro uživatele dopady? Jsou v tom finanční, přístupové nebo právní důsledky?
2. Má uživatel k té akci správná oprávnění?
3. Je akce trvalá?
4. Jaký časový rámec akce zabere (sekundy, minuty, hodiny, dny)?
5. Co má uživatel dělat, když akce selže?
6. Je to akce na jedné položce, nebo dávková?

**ZDROJ:** Carbon, Common actions, Add, Considerations a Remove, Considerations.
https://carbondesignsystem.com/patterns/common-actions/
**Carbonovo zdůvodnění:** „Small adjustments in your messaging will reduce user uncertainty."

## Slovník akcí

| Akce | Definice podle Carbonu | Forma |
|---|---|---|
| **Add** | Vloží **existující** objekt do seznamu, sady nebo systému. Příklad: přidání dokumentu do složky | Podle důležitosti vysoká, střední nebo nízká emfáze. U vysoké jedno primární tlačítko, všechna ostatní sekundární |
| **Cancel** | Zastaví aktuální akci a zavře komponentu nebo položku | **Sekundární tlačítko nebo odkaz** |
| **Clear** | Odebere data z pole nebo odebere výběry. Může taky smazat obsah dokumentu, například logu. U prvků s výchozí volbou nebo hodnotou (radio buttony) se **výchozí volba resetuje** | **Ikona `close` na pravé straně** pole, položky nebo hodnoty |
| **Close** | Ukončí aktuální stránku, okno nebo menu. Používá se taky na zavření informace, například notifikace | **Ikona `close`**, typicky vpravo nahoře. **Close nepoužívej v tlačítku** |
| **Copy** | Vytvoří novou identickou instanci vybraného objektu | Ikona `copy` s potvrzovacím tooltipem „copied" po kliknutí nebo tapnutí |
| **Delete** | **Zničí objekt.** Nelze snadno vzít zpět a je typicky trvalé | Ikona `delete` nebo `trash can`, danger tlačítko, nebo danger volba v menu. Danger modal se použije, když je potřeba varování k potvrzení akce |
| **Edit** | Umožní změnit data nebo hodnoty. Typicky vyvolá změnu stavu cílového objektu nebo vstupní položky | Volba v menu, tlačítko, nebo ikona `edit` |
| **Next** | Posune uživatele na další krok v posloupnosti, například ve wizardu | Tlačítko s ikonou, nebo samostatná ikona `forward` |
| **Refresh** | Znovu načte pohled na objekt, seznam nebo datovou sadu, když se zobrazený pohled rozešel se zdrojem | Ikona `refresh` nebo tlačítko |
| **Remove** | Odebere objekt ze seznamu nebo položky. **Odlišné od delete: odebraná položka není zničená.** Lze odebrat víc objektů zároveň | Tlačítko nebo ikona či glyf `subtract`. **Remove je zřídka primární akce na stránce a nemá být přehnaně zdůrazněná** |
| **Reset** | Vrátí hodnoty do **posledního uloženého** stavu. Ten obsahuje hodnoty uložené naposled, kdy uživatel spustil **Apply** | Typicky **odkaz** |

**ZDROJ:** Carbon, Common actions, jednotlivé sekce.
https://carbondesignsystem.com/patterns/common-actions/

**Nejčastěji porušovaná dvojice:** Delete versus Remove. Carbon k Remove přímo přiznává riziko:
„This action can be confused with deleting."

**Druhá dvojice, která se plete:** Clear versus Reset. Clear vyprázdní, Reset vrátí do uloženého stavu.
V praxi se u filtrů používá Clear (vrátí do výchozího stavu filtru, viz [Filtrování](filtrovani.md))
a u formulářů Reset.

## Cancel: varuj před důsledky

**PRAVIDLO:** U Cancel varuj uživatele před jakýmikoliv negativními důsledky, když proces nepokračuje,
například poškození nebo ztráta dat.
**TŘÍDA:** B
**ZDROJ:** Carbon, Common actions, Cancel, verbatim: „Warn the user of any negative consequences if the
process doesn't progress, such as data corruption or data loss."
https://carbondesignsystem.com/patterns/common-actions/
**Souvislost:** v dialogu má Cancel navíc konkrétní chování: **vrátí všechny aplikované změny**
(„Cancel undoes all applied changes"). Viz [Dialogy a panely](dialogy-a-panely.md).

## Mazání: tři úrovně dopadu

Tohle je nejužitečnější část celého vzoru. Carbon odstupňuje potvrzení podle toho, jak drahé je data
obnovit.

| Úroveň | Kdy | Co se stane |
|---|---|---|
| **Low-impact** | Když je smazání triviální vzít zpět, nebo data snadno vytvořit znovu | Smaž data **po kliknutí bez dalšího varování** |
| **Moderate-impact** | Když akci nelze vzít zpět, nebo data nelze snadno vytvořit znovu. Užitečné i tehdy, když mažeš víc věcí | Vyžádej si potvrzení smazání, **s vysvětlením, co se stane**, když to smaže |
| **High-impact** | Když by bylo velmi drahé nebo časově náročné data znovu vytvořit. Taky když akce maže velké množství dat, nebo když by v důsledku byly smazané další důležité položky | Kromě dialogu nech uživatele **napsat název zdroje**, který maže (ruční potvrzení) |

**ZDROJ:** Carbon, Common actions, Delete, tři úrovně.
https://carbondesignsystem.com/patterns/common-actions/
**Souvislost:** knihovna má k nevratným akcím tvrdší pravidlo s WCAG oporou: před akcí s právním nebo
finančním dopadem, před smazáním dat a před odesláním testu má být krok kontroly (WCAG 2.2 SC 3.3.4
Error Prevention, AA). A pravidlo, že **undo je lepší než potvrzovací dialog**, protože nezdržuje. Viz
[formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).

### Po smazání

**PRAVIDLO:** Po smazání dat vrať uživatele na stránku, která smazaná data vypisovala. **Animuj
odebrání** dat ze seznamu nebo stránky a zobraz **success notifikaci**.

Když smazání **selže**: zvedni notifikaci, která uživateli řekne, že smazání selhalo. Když to jde,
pošli **druhou notifikaci jiným komunikačním kanálem**, například e-mailem. A když to jde, **animuj
data zpátky** na stránku.

**KDY PLATÍ:** Každé mazání.
**TŘÍDA:** B
**ZDROJ:** Carbon, Common actions, Delete, Post-deletion, verbatim: „If the deletion fails, raise
a notification to tell the user that deletion failed. Send a second notification on another
communication channel, like email, if possible. Animate the data back onto the page if possible."
https://carbondesignsystem.com/patterns/common-actions/
**Poznámka k animaci:** pravidla pro trvání, easing a `prefers-reduced-motion` jsou v knihovně ve
[pohybu](../../ux-design/pravidla/pohyb.md). Animace odebrání řádku musí být přerušitelná a musí
respektovat `prefers-reduced-motion`.

## Chyby jako akce

Carbon má „Errors" v seznamu běžných akcí, protože obsluha chyby je opakující se vzor.

**Co Carbon říká:**

- Chyba nastane, když akce nebo proces neuspěje.
- Chybové notifikace mohou zabírat **celé stránky, formulářová pole, notifikace i modaly**.
- Chybová notifikace má dát **kontext toho, co se stalo, a jasnou cestu, jak pokračovat**.
- Zvaž přesměrování uživatele do předchozího stavu, na stránku podpory, nebo nabídnutí doporučení.
  **Buď poctivý a užitečný.**
- Některé komponenty (text input, chyby formulářových polí) jsou malé a vyžadují promyšlenější
  přístup k prostoru a umístění obsluhy chyby. Tam zvaž **inline chybové notifikace**.

**Délka textu:**

| Kontext | Limit |
|---|---|
| Celostránkové chyby a velké modaly | **Max tři řádky** odstavce |
| Chyby formuláře | **Max dvě řádky** |

**Tón:** buď stručný, poctivý a podpůrný. Vysvětli, co se stalo a co může uživatel udělat, aby chybu
vyřešil.

**ZDROJ:** Carbon, Common actions, Errors, Content guidelines, verbatim: „Be brief, honest, and
supportive." https://carbondesignsystem.com/patterns/common-actions/
**Souvislost:** text chybové hlášky, zakázaný slovník a rozlišení tří tříd chyb podle toho, kdo je
způsobil, jsou v knihovně s tvrdšími zdroji (WCAG 3.3.1, 3.3.3, GOV.UK, NN/g). Viz
[formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md). **Carbon a knihovna se u tónu
u systémových chyb rozcházejí:** Carbon říká „be honest and helpful", knihovna rozlišuje, že u
validační chyby se neomlouvá, u systémové chyby ano.

## Hierarchie a umístění akcí

Carbon dává pravidlo u **Add**: podle důležitosti akce na stránce může být emfáze vysoká, střední
nebo nízká. Příklad: akce s vysokou emfází používá **jedno primární tlačítko** a všechna ostatní jsou
sekundární.

U **Remove** naopak: **je zřídka primární akcí** na stránce a nemá být přehnaně zdůrazněná.

**ZDROJ:** Carbon, Common actions, Add a Remove, Hierarchy and placement.
https://carbondesignsystem.com/patterns/common-actions/
Detail variant tlačítek a jejich hierarchie:
[Tlačítka: varianty a volba](../komponenty/tlacitka-varianty.md).

## Ikony pro univerzální akce

Carbon má uzavřenou sadu akcí, u kterých doporučuje ikonu vedle labelu tlačítka, protože mají jasně
definované a široce rozpoznané ikony:

Create/Add, Edit, Copy, Delete (trash can), Remove (subtract alt), Export, Upload, Download,
Play/Start, Pause, Stop, Refresh (restart).

**PRAVIDLO:** **Nepoužívej definovanou ikonu pro jinou univerzální akci.** Carbon k tomu dává důvod:
používání ikon z toho seznamu pro jiné akce může zamlžit očekávaný výsledek a zkušenost.
**KDY PLATÍ:** Kdykoliv dáváš ikonu k akci.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Universal actions with well-established icons.
https://carbondesignsystem.com/components/button/usage/
**KDY NEPLATÍ:** Ikony, které v seznamu nejsou, se v tlačítkách použít **můžou**, pokud jasně
vyjadřují zamýšlenou akci. Carbon doporučuje ověřit očekávané použití podle názvu ikony v knihovně.

**Launch ikona:** má být na každé výzvě k akci, která uživatele pošle do **jiného tabu** (bez ohledu
na to, jestli je obsah nového tabu součástí stejného produktu, nebo je to úplně jiný web). Cíl akce
musí být uživateli jasný z labelu a okolního kontextu. Carbon jmenuje typická místa: levá navigace,
boční panel, karty, modaly.

**Konzistence ve skupině tlačítek:** ikony ve skupině jsou volitelné, ale Carbon doporučuje **ukázat
ikonu u každého tlačítka ve skupině, nebo u žádného**. Zdůvodnění: ikona s labelem vizuálně popíše
akci a nasměruje na ni pozornost, ale příliš mnoho tlačítek s ikonami v jedné skupině vytváří nežádoucí
šum a zbytečně komplikuje jednoduchou zkušenost. A ve skupinách používej ikony **jen** pro univerzální
akce ze seznamu, nebo pro akce s běžně asociovanou ikonou.

## Pravidla pro ikony v tlačítku

- Ikona 16 px v tlačítku, 20 px v large expressive tlačítku.
- Ikony jsou rozlišené plným tvarem s vykrojenými detaily.
- Ikona vždy **vpravo od labelu**.
- Ikona musí přímo souviset s akcí, kterou uživatel provádí.
- Ikona musí mít stejnou barevnou hodnotu jako label v tlačítku.
- Používej **výchozí variantu** ikon. Carbon má u některých ikon plné (filled) varianty, ale ne u
  všech, takže radí používat výchozí volbu u všech. Jediná výjimka jsou stavové ikony, které mají
  vlastní definovanou ikonu.
- Ikony používej **střídmě**: přehnané používání vytváří vizuální šum a zhoršuje použitelnost. Když
  použiješ tlačítko s ikonou v jedné části UI, neznamená to, že musíš přidat ikony všem ostatním
  tlačítkům.

**ZDROJ:** Carbon, Button usage, Button with icon.
https://carbondesignsystem.com/components/button/usage/

---

## Co tahle nota neřeší

- Varianty tlačítek (primary, secondary, tertiary, ghost, danger) a jejich kombinace ve skupině.
  [Tlačítka: varianty a volba](../komponenty/tlacitka-varianty.md).
- Text chybové hlášky do detailu a zakázaný slovník.
  [Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md), s tvrdšími zdroji.
- Krok kontroly před nevratnou akcí (WCAG 3.3.4). Tamtéž.
- Trvání a easing animací. [Pohyb](../../ux-design/pravidla/pohyb.md).
- Carbonův schválený seznam labelů akcí. Stránka `guidelines/content/action-labels` v přečtené kopii
  není, mám jen to, co na ni odkazuje z jiných stránek.

## Zdroj

IBM Carbon Design System, Common actions pattern, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/patterns/common-actions/
Doplněno pravidly o ikonách z Button usage. Vzor nemá sekci References, Carbon k němu žádné externí
zdroje neuvádí. Třída **B**.
