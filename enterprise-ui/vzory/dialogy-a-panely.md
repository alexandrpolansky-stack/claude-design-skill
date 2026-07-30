# Dialogy, modaly a boční panely

Kdy přerušit uživatele překryvem a kdy ne. Kde má být akce a co se stane při chybě.

Související: [Volba komponenty](../zaklady/volba-komponenty.md) ·
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md) · [Notifikace](notifikace.md) ·
[Skladba formuláře](formular-skladba.md)

---

## Rychlé rozhodnutí

1. Vyvolal to uživatel? Ne = **nepoužívej dialog**, použij toast.
2. Je odpověď povinná pro pokračování? Ano = modal. Ne = nemodální dialog nebo inline.
3. Potřebuje uživatel při rozhodování vidět něco pod dialogem? Ano = **ne modal**, dej boční panel
   nebo nemodální dialog.
4. Vstupů pod pět = modal. Nad pět = boční panel. Složitý nebo dlouhý úkol = celá stránka.
5. Nikdy nevnořuj modal do modalu.
6. Modal nikdy nedělej na celou stránku. Když nestačí velký modal, patří to na stránku.
7. Tlačítka: Zrušit nejvíc vlevo, primární nejvíc vpravo, jedno primární na dialog.
8. Focus po otevření: první vstupní pole. Bez polí = primární tlačítko. Destruktivní = Zrušit.
9. Validuj **před** zavřením. Při chybě dialog zůstane otevřený.

---

## Modal versus nemodální dialog

| Typ | Kdy | Co dělá s pozadím |
|---|---|---|
| Modal | Kritická informace nebo povinný vstup potřebný k dokončení flow | Obsah pod ním je zakrytý a nedostupný, dokud se úkol nedokončí nebo dialog nezavře |
| Nemodální | Nekritická informace, volitelný úkol | Obsah stránky zůstane dostupný a lze s ním pracovat |

**ZDROJ:** Carbon, Dialog pattern, tabulka typů, verbatim: „Modal: Use to present critical information
or request required input needed to complete a workflow." / „Non-modal: Use to present non-critical
information or optional user tasks." https://carbondesignsystem.com/patterns/dialog-pattern/

**Nemodální dialog lze posunout** z původní pozice, aby uživatel viděl, co je pod ním. Carbon jako
příklad použití jmenuje „find and replace" a in-context nápovědu nebo tutoriál.

## Kdy dialog použít a kdy ne

**Použij** pro: zaostření pozornosti, krátké dokončení úkolu, získání vstupu od uživatele, zobrazení
relevantní informace.

**Nepoužívej**, když: obsah nesouvisí s aktuálním flow, jde o složitá nebo velká data, chtěl bys
v dialogu znovu postavit celou aplikaci nebo stránku, dialog nevyvolal uživatel.

**ZDROJ:** Carbon, Dialog pattern, When to use / When not to use.
https://carbondesignsystem.com/patterns/dialog-pattern/

### Dialog musí vyvolat uživatel

**PRAVIDLO:** Dialog otevírá akce uživatele. Nevyskakuj s dialogem, když ho uživatel nečeká. Vyhýbej
se systémově generovaným popupům, které ruší při práci (Carbonův příklad: Net Promoter Score). Když
alert generuje systém a není to důsledek akce uživatele, ale reakce na dění na pozadí, **použij toast**.
**KDY PLATÍ:** Vždy.
**PROČ:** Carbon: dialogy jsou rušivé, a když se používají na věci mimo flow, uživatel je začne
ignorovat nebo odklikávat bez přečtení. To pak vede k unáhleným rozhodnutím u těch kritických.
**TŘÍDA:** B
**ZDROJ:** Carbon, Dialog pattern, Best practices, verbatim: „If the system is autogenerating an alert
that is not a consequence of a user's action, but a response to processes happening in the background,
then a toast notification should be used instead."
https://carbondesignsystem.com/patterns/dialog-pattern/
**KDY NEPLATÍ:** Nepřímý důsledek akce je v pořádku. Carbonův příklad: uživatel zavírá tab
s neuloženým obsahem a dialog se zeptá, jestli chce změny uložit.

### Tři důvody, proč modal nepoužít

1. **Modal odřízne stránku.** Když uživatel potřebuje při rozhodování nahlédnout na informaci mimo
   modal, nepoužívej modal. Úkol v modalu musí být splnitelný s tím, co je v modalu.
2. **Nevnořuj modaly.** Jeden modal nikdy nesmí vyvolat druhý. Carbon k tomu dává důsledek: když je
   první úkol závislý na potvrzovacím modalu, neměl ten první úkol být v modalu vůbec.
3. **Modal není stránka.** Když obsah potřebuje víc místa, než dovolí velký modal, patří na vlastní
   stránku.

**ZDROJ:** Carbon, Dialog pattern, When not to use, verbatim: „One modal should never trigger another
modal." a „A modal is not an alternative to page."
https://carbondesignsystem.com/patterns/dialog-pattern/

### Opakovaný úkon nepatří do modalu

**PRAVIDLO:** Modaly jsou pro krátké a nefrekventované úkony (editace, správa). Když uživatel musí
úkon dělat opakovaně, udělej ho splnitelný na hlavní stránce.
**PROČ:** Carbon: modal přidává interakční náklad, vytrhne uživatele z předchozího kontextu a chce
další akce na dokončení a zavření. Kontrolní otázka, kterou Carbon dává: je to kritické pro jeho
aktuální flow?
**TŘÍDA:** B
**ZDROJ:** Carbon, Modal usage / Dialog pattern, verbatim: „If a user needs to repeatedly perform
a task, consider making the task do-able from the main page. A modal dialog adds to a workflow's
interaction cost." https://carbondesignsystem.com/components/modal/usage/

## Varianty modalu

| Varianta | Kdy | Tlačítka |
|---|---|---|
| Passive | Informace, o které má uživatel vědět, ohledně aktuálního flow | Žádná akce |
| Transactional | Vyžaduje akci, aby se dal dokončit a zavřít | Zrušit plus primární |
| Danger | Podvarianta transactional pro destruktivní nebo nevratné akce | Zrušit plus danger tlačítko místo primárního |
| Acknowledgment | Systém potřebuje potvrzení, že uživatel informaci vzal na vědomí | Jedno tlačítko, typicky OK |
| Progress | Víc kroků, které je nutné projít, než se dá zavřít | Zrušit, Předchozí, Další nebo dokončovací |

**ZDROJ:** Carbon, Dialog pattern a Modal usage, tabulky variant.
https://carbondesignsystem.com/components/modal/usage/

### Tři důvody pro modal, které Carbon jmenuje

1. **Vyžádat okamžitou odpověď:** informace, která systému brání pokračovat v procesu, jejž uživatel
   spustil.
2. **Oznámit urgentní informaci** ohledně aktuální práce. Typicky systémové chyby nebo důsledek akce
   uživatele.
3. **Potvrdit rozhodnutí uživatele.** Jasně popiš potvrzovanou akci a vysvětli možné důsledky.
   **Titulek i tlačítko musí odrážet akci, která se stane.** Když je akce destruktivní nebo nevratná,
   použij transactional danger modal.

**ZDROJ:** Carbon, Dialog pattern, Modal dialogs, When to use.
https://carbondesignsystem.com/patterns/dialog-pattern/

## Zavírání podle varianty

| Varianta | Křížek | Klik mimo | `Esc` | Dokončení | Zrušit |
|---|---|---|---|---|---|
| Passive | ano | **ano** | ano | nemá | nemá |
| Transactional, progress, acknowledgment | ano | **ne** | ano | ano | ano, vrátí všechny změny |
| Nemodální | ano | ne | ano | podle varianty | ano, když tlačítko je |

**Klíčový rozdíl:** klik mimo zavírá **jen pasivní** modal. U transakčního by to znamenalo zahodit
zadaná data omylem.
**ZDROJ:** Carbon, Dialog pattern, Dismissing variant modals a Modal usage, sekce Dismissing
u jednotlivých variant. https://carbondesignsystem.com/patterns/dialog-pattern/

**Křížek nikdy neodesílá data.** Carbon to u všech variant opakuje: „will close the modal without
submitting any data and return the user to its previous context." Zrušit navíc **vrací všechny
aplikované změny**: „Cancel undoes all applied changes."

## Tlačítka v dialogu

**PRAVIDLO:** Zrušit je vždy nejvíc vlevo, primární akce vždy nejvíc vpravo. Na dialog smí být jen
jedna primární akce. Tlačítka v dialogu jdou vždy na plnou šířku (full bleed) a jsou přilepená ke
spodní hraně dialogu.
**KDY PLATÍ:** Každý dialog.
**TŘÍDA:** B
**ZDROJ:** Carbon, Dialog pattern, Button groups, verbatim: „When placing buttons, Cancel is always
the outmost left button option and the primary action is always the outmost right button. There should
only ever be one primary action per dialog. Dialog buttons are always full bleed and attached to the
bottom of a dialog." https://carbondesignsystem.com/patterns/dialog-pattern/

| Počet tlačítek | Rozvržení |
|---|---|
| 1 | Vpravo, zabírá 50 % šířky dialogu, k hraně. Typicky acknowledgment. V většině případů primární |
| 2 | Sekundární vlevo, primární vpravo, každé 50 % šířky, k hraně |
| 3 | Každé 25 % šířky, zarovnané doprava. **Primární smí být jen to nejvíc vpravo**, ostatní dvě sekundární. Když mají všechny tři stejnou váhu, ať jsou všechny tři sekundární |
| Progress (3) | Zrušit vlevo jako ghost. Předchozí (sekundární) a Další (primární) spolu na pravé polovině. Každé 25 % |

**V posledním kroku sekvence** se label tlačítka Další musí změnit na finální akci.
**ZDROJ:** Carbon, Dialog pattern, Progress indicator buttons.

## Chování

| Aspekt | Pravidlo |
|---|---|
| Trigger | Akce uživatele: tlačítko, odkaz, ikona. Z klávesnice `Enter` nebo `Space` |
| Focus | Po otevření na první místo přijímající vstup, pak trap v dialogu. Detail podle typu dialogu: [Klávesnice a focus](../zaklady/klavesnice-a-focus.md) |
| Scroll | Každá velikost modalu má maximální výšku. Když je obsah delší, **scrolluje jen tělo**, hlavička a zápatí zůstávají na místě. Obsah má na konci těla vizuálně zeslábnout, aby bylo vidět, že pokračuje |
| Horizontální scroll | Nikdy. Použij větší modal |
| Validace | Před zavřením. Neplatný vstup = dialog zůstane otevřený, pole v chybovém stavu, inline chybová hláška |
| Serverová chyba | Inline notifikace v dialogu |
| Dokončení | Má proběhnout okamžitě. Krátké čekání = spinner s overlayem nad tělem dialogu, obsah disabled, primární tlačítko disabled. Rychlé čekání = inline loading na primárním tlačítku |
| Dlouhé čekání | Nad pár sekund zobraz informaci o postupu **jinde na obrazovce**, ne v dialogu |

**ZDROJ:** Carbon, Dialog pattern, Behaviors a Modal usage, Universal behaviors.
https://carbondesignsystem.com/patterns/dialog-pattern/ ·
https://carbondesignsystem.com/components/modal/usage/

**Poznámka k rozporu s knihovnou:** Carbon tady velí inline validaci na blur („should happen as soon
as the field loses focus"). [Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md) má jako
default validaci **při odeslání** s citací GOV.UK a validaci na blur povoluje jen u polí s tvrdým
formátem. Pro veřejné služby a nesegmentované publikum platí přísnější pravidlo z knihovny. Carbonova
poloha je legitimní pro enterprise produkt s vlastním výzkumem. Spor je v knihovně zdokumentovaný
záměrně, viz [STATUS.md](../../STATUS.md).

## Které komponenty do dialogu patří a které ne

**Patří:** formulářové vstupy a ovládací prvky pro získání informace. Content switcher a structured
list na organizaci informace.

**Nepatří:**

| Co | Proč podle Carbonu |
|---|---|
| Odkazy vedoucí jinam | Odvedou uživatele z kontextu a od úkolu. Dialog má pozornost soustředit, ne rozptylovat |
| Accordion a taby | Skrývají informaci a volby, uživatel musí vyvinout úsilí, aby zjistil, co všechno tam je. Když je obsahu tolik, že to potřebuje skrývání, patří to na stránku |
| Datová tabulka | Je to složitá komponenta s vlastním flow a rozhodováním, což volbu a dokončení úkolu zbytečně komplikuje |

**Když datovou tabulku v dialogu potřebuješ:** drž ji co nejjednodušší, s omezenými interakcemi.
Výběr řádků, na které se aplikuje akce dialogu, je v pořádku. Dávkové akce a dávkovou editaci uvnitř
modalu nedělej. U menších množin dat nebo výběrů zvaž structured list, dropdown nebo sadu dlaždic.

**ZDROJ:** Carbon, Dialog pattern, Using components.
https://carbondesignsystem.com/patterns/dialog-pattern/
**Souvisí:** Carbonovo pravidlo pro formuláře v dialogu je stejné: „Do not hide information in
accordions or tabs." https://carbondesignsystem.com/patterns/forms-pattern/

## Dialog, boční panel, nebo stránka

| Varianta | Kdy podle Carbonu | Příklad Carbonu |
|---|---|---|
| Celá stránka | Složitější, delší nebo vícekrokový vstup | Vytvoření nové služby, provisioning, složitější objednávkové formuláře |
| Dialog | Kritické, nefrekventované vyžádání vstupu, typicky editace a správa. **Méně než pět vstupů** | Oprávnění uživatele, upgrade služby |
| Boční panel | Opakované vyžádání vstupu, kdy uživatel potřebuje vidět dotčenou informaci. **Víc než pět vstupů** | Úprava dat řádku v datové tabulce |

**ZDROJ:** Carbon, Forms pattern, Variants, verbatim: „Use a dialog form when dealing with less than
five inputs." a „Use a side panel form when dealing with more than five inputs."
https://carbondesignsystem.com/patterns/forms-pattern/
Carbon u téhle tabulky sám přiznává, že k ní chce od produktových týmů víc vstupu.

## Velikost modalu

**PRAVIDLO:** Vyber velikost podle množství obsahu. Krátký text = extra small nebo small, aby nebyly
příliš dlouhé jednořádkové řádky. Složité komponenty (tabulka) = default nebo large.
Když je v modalu příliš mnoho scrollování kvůli maximální výšce, jdi o velikost výš. Když nestačí ani
large, patří obsah na celou stránku.
**ZDROJ:** Carbon, Modal usage, Sizing.
https://carbondesignsystem.com/components/modal/usage/

## Obsah dialogu

| Prvek | Pravidlo |
|---|---|
| Titulek | Krátká slovesná fráze popisující úkol nebo účel. **Když modal otevírá tlačítko, použij label toho tlačítka jako titulek** |
| Volitelný label nad titulkem | Když je potřeba kontext: na co se akce vztahuje, cesta k objektu |
| Popis | Jen když účel není zjevný. Když je titulek jasný (Edit object pro editaci objektu), popis nepatří |
| Tělo | Jen pole, komponenty a nápověda relevantní k aktuálnímu úkolu. Text na 80 % šířky modalu, komponenty smí 100 % |
| Tlačítka | Aktivní slova popisující účel (Add, Delete, Save). **Vyhýbej se vágním Done a OK** |
| Titulek jako celá zpráva | U krátkých přímých zpráv smí být celá zpráva v titulku. Pak už žádné tělo |

**ZDROJ:** Carbon, Modal usage, Content, verbatim: „If the modal is accessed by clicking a button, use
the button label for the modal title" a „Avoid vague or passive words, such as Done or OK."
https://carbondesignsystem.com/components/modal/usage/
Carbon zároveň upozorňuje: „Be aware of situations where there's a tendency to mix and match button or
icon labels and modal titles." Příklad: ikona „New user" a titulek „Create user" je chyba.

**Poznámka k terminologii:** Carbon uvádí, že v IBM Style se modalu říká dialog. V téhle knihovně
používám modal pro komponentu a dialog pro nadřazený vzor, stejně jako Carbonova dokumentace.

## Modal jako notifikace

**PRAVIDLO:** Modal použij jako notifikaci jen tehdy, když nese kritickou informaci bezprostředně
související s úkolem uživatele. Pro nekritické sdělení použij toast nebo inline notifikaci.
**PROČ:** Carbon: modaly jsou vysoce rušivé a blokují úkol, dokud je uživatel nezavře.
**TŘÍDA:** B
**ZDROJ:** Carbon, Modal usage, Modal versus notification.
https://carbondesignsystem.com/components/modal/usage/
Detail: [Notifikace](notifikace.md)

---

## Co tahle nota neřeší

- Toasty, inline notifikace, callouty a bannery. [Notifikace](notifikace.md).
- Skladbu formuláře uvnitř dialogu. [Skladba formuláře](formular-skladba.md).
- Focus a klávesovou mechaniku do detailu.
  [Klávesnice a focus](../zaklady/klavesnice-a-focus.md).
- Tooltip a toggletip jako lehčí formu překryvu.
  [Tooltip a toggletip](../komponenty/tooltip-a-toggletip.md).
- Tearsheet a side panel jako komponenty. Carbon je má v „Carbon for IBM Products", což v přečtené
  kopii není, takže o jejich vnitřní stavbě podklad nemám.

## Zdroj

IBM Carbon Design System, Dialog pattern a Modal usage, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/patterns/dialog-pattern/ ·
https://carbondesignsystem.com/components/modal/usage/
Carbon k tomuhle vzoru cituje Apple HIG (Modality, Dialogs, 2019), Therese Fessenden, Modal &
Nonmodal Dialogs: When (& When Not) to Use Them (NN/g, 2017), Microsoft Docs a WCAG 2.4.3.
Třída **B**, u focus order **A** (WCAG 2.4.3).
