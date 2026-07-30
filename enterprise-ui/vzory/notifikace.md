# Notifikace: stav krát typ

Carbonův model: notifikace se skládá ze **stavu** (co sděluje) a **typu** (jak moc smí přerušit).
Obojí se volí zvlášť a kombinuje.

Související: [Dialogy a panely](dialogy-a-panely.md) · [Stavové indikátory](stavove-indikatory.md) ·
[Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md)

---

## Rychlé rozhodnutí

1. Vyvolala to akce uživatele v konkrétním místě? = **inline**, umísti to k dotčené věci.
2. Vyvolal to systém bez vazby na místo na stránce? = **toast**.
3. Musí uživatel reagovat, jinak nemůže dál? = **modal**. Jinak modal ne.
4. Má být vidět **před** akcí a natrvalo? = **callout**. Callout nemá success ani error stav.
5. Celoproduktová zpráva mimo úkol (odstávka, expirace)? = **banner**, jen jeden na obrazovku.
6. Notifikace s akcí = **persistuje, dokud ji uživatel nezavře**. Jedna akce, label max dvě slova.
7. Nikdy nespoléhej na barvu samotnou. Stav vždycky nese i ikona a text.
8. Kritická zpráva **nesmí** mizet na časovač.
9. Zpráva max dvě řádky. Delší = actionable notifikace s odkazem „Zobrazit více".

---

## Tři principy

| Princip | Definice podle Carbonu |
|---|---|
| Relevant | Notifikace souvisí s cíli uživatele a je podaná v kontextu toho, co právě dělá |
| Timely | Uživatel je průběžně informovaný a kritické notifikace vidí okamžitě |
| Informative | Notifikace dá kontext a další kroky potřebné k tomu, aby ji uživatel pochopil a odbavil |

**ZDROJ:** Carbon, Notification pattern, tabulka Key principles.
https://carbondesignsystem.com/patterns/notification-pattern/

## Dva zdroje notifikace

| Zdroj | Definice | Příklady Carbonu | Kam patří |
|---|---|---|---|
| Task-generated | Reakce na akci uživatele v rámci konkrétního úkolu, přímá okamžitá zpětná vazba | Formulář odeslán, problém s nahráním souboru, nenalezené přihlašovací údaje | Do oblasti stránky, kde uživatel pracuje, a musí souviset s jeho akcí |
| System-generated | Vyvolává aplikace nebo systém nezávisle na akci uživatele. Stav procesů na pozadí nebo dokončené události mimo kontext | Ztráta připojení, plánovaná odstávka, nový report je hotový, blížící se vypršení session | Kamkoliv, typicky toast |

**Praktický důsledek pro text:** task-generated notifikace nepotřebuje rozsáhlý kontext, protože
uživatel právě něco udělal. System-generated notifikace naopak typicky **nesouvisí** s tím, co
uživatel právě dělá, takže musí kontext dodat, aby jí uživatel rozuměl.

**ZDROJ:** Carbon, Notification pattern, When to use.
https://carbondesignsystem.com/patterns/notification-pattern/

## Stav notifikace

| Stav | Kdy | Barva | Ikona | Dostupný u |
|---|---|---|---|---|
| Informational | Doplňující informace, která nemusí souviset s aktuální akcí nebo úkolem | Modrá | information filled | inline, toast, actionable, callout |
| Success | Potvrzení, že úkol proběhl podle očekávání | Zelená | checkmark filled | inline, toast, actionable |
| Warning | Uživatel dělá něco nežádoucího nebo s nečekaným výsledkem | Žlutá | warning filled | inline, toast, actionable, callout |
| Error | Chyba nebo kritické selhání, volitelně blokuje pokračování, dokud se to nevyřeší | Červená | error filled | inline, toast, actionable |

**Proč callout nemá success a error:** callout dává vodítko **před** tím, než uživatel začne, není to
zpětná vazba po akci. Ostatní varianty jsou reaktivní.
**ZDROJ:** Carbon, Notification usage, tabulka statusů, verbatim: „The callout variant is unique, as
it provides guidance before users begin a task or take action and, therefore, does not include success
or error statuses." https://carbondesignsystem.com/components/notification/usage/

**Barva sama nestačí.** Každý stav má vlastní barvu **i** ikonu. Zdůvodnění a WCAG kritéria jsou
ve [Stavových indikátorech](stavove-indikatory.md) a v
[kontrastu a barvě](../../ux-design/pravidla/kontrast-a-barva.md).

## Typ notifikace

| Typ | Kdy | Trvání a interakce |
|---|---|---|
| Inline | Nerušivá zpětná vazba nebo stav akce | Persistuje, dokud se problém nevyřeší nebo ji uživatel nezavře. Může mít ghost tlačítko |
| Toast | Krátká časově omezená zpráva, vysouvá se a zasouvá | Bez akce může zmizet sám nebo ho zavře uživatel. **S akcí persistuje, dokud ho uživatel nezavře** |
| Actionable | Interaktivní prvky uvnitř notifikace, stylovaná jako inline nebo toast | Persistuje, dokud se neprovede akce nebo uživatel nezavře |
| Callout | Zdůraznění důležité informace kontextově v obsahu stránky | **Nevyvolává ji uživatel ani systém**, načte se s obsahem stránky, je trvalá a **nelze ji zavřít** |
| Banner | Notifikace na úrovni produktu nebo systému, nesouvisí s úkolem | Persistuje, dokud ji uživatel nezavře. Může mít ghost tlačítko nebo odkaz |
| Notification panel | Centrum notifikací se systémově generovanými zprávami | Otevírá a zavírá uživatel |
| Modal | Vysoce rušivá notifikace s kritickou informací vyžadující pozornost nebo akci | Persistuje a blokuje úkoly, dokud ji uživatel nezavře |

**ZDROJ:** Carbon, Notification pattern, tabulka Notification types.
https://carbondesignsystem.com/patterns/notification-pattern/

**Pozor na zralost:** Carbon u **banneru** i u **notification panelu** sám uvádí, že potřebuje víc
iterací a testování s uživateli, než pokyny ustálí, a komponentu na ně **nemá**. Když je stavíš, staví
si je tým sám.

## Inline notifikace

- Umísti ji k souvisejícím prvkům.
- Ve formulářích může být nahoře nebo dole. Carbon na jiném místě konkretizuje: **dole nad tlačítky
  odeslat a zrušit**. Když se chyba týká konkrétního vstupu, doplňuje chybový stav toho pole, nenahrazuje ho.
- Zpráva max dvě řádky.
- Nepřekrývej jí jiný obsah.
- Šířka se mění podle kontextu a rozvržení, může vyplnit kontejner nebo obsahovou oblast a má se
  zarovnat na sloupce mřížky.
- Buď popisný a dej jasné další kroky.
- **Nezmizí sama.** Persistuje, dokud ji uživatel nezavře nebo se problém nevyřeší.
- Zavírací křížek je volitelný a **nemá tam být**, když je kritické, aby si uživatel notifikaci
  přečetl nebo s ní interagoval.

**ZDROJ:** Carbon, Notification pattern, Inline notification, Best practices ·
Carbon, Notification usage, Inline formatting a Dismissal.
https://carbondesignsystem.com/components/notification/usage/

## Toast

- Vysouvá se a zasouvá typicky vpravo nahoře.
- Rušivější než inline. Nejlepší pro systémové zprávy, které neodpovídají konkrétní sekci UI.
- Fixní šířka, **nerozšiřuj ho na obsahovou oblast**.
- Víc toastů se stohuje svisle, nejnovější nahoře, starší se odtlačují dolů.
- Timestamp je volitelný, ale musí být konzistentní v celém produktu: buď všechny toasty, nebo žádný.
  Odebráním timestampu získáš místo na třetí řádek textu.
- Zpráva **nesmí přesáhnout tři řádky**, toast je zpráva na jeden pohled.
- Ve výchozím stavu persistuje, ale lze ho naprogramovat, aby zmizel po pěti sekundách.
- Protože toast zakrývá obsah, musí být vždy snadno zavíratelný.
- **Protože může zmizet sám, uživatel musí mít možnost se k obsahu dostat i potom.** Carbon k tomu
  navrhuje notification panel.

**ZDROJ:** Carbon, Notification pattern, Toast ·
Carbon, Notification usage, Toast formatting a Dismissal, verbatim: „users should be able to access
them elsewhere after the toast notification disappears if they need more time to read the notification
or who want to refer to it later." https://carbondesignsystem.com/components/notification/usage/

## Actionable notifikace

**PRAVIDLO:** Actionable notifikace **si bere focus** při vyvolání a je proto podle Carbonu vysoce
rušivá pro uživatele čteček a klávesnice. Používej ji jen tam, kde je interakce potřeba.
**Jedna akce na notifikaci.** Label akce max dvě slova. Persistuje, dokud ji uživatel nezavře.
**KDY PLATÍ:** Vždy, když do notifikace dáváš tlačítko.
**TŘÍDA:** B
**ZDROJ:** Carbon, Notification pattern, Actionable, verbatim: „Actionable notifications, since they
require user interaction, take focus when triggered and can be highly disruptive to screen readers and
keyboard users." a Best practices: „Only one action per notification. Limit action labels to two words
or less." https://carbondesignsystem.com/patterns/notification-pattern/

**Varianty tlačítka:** actionable ve stylu inline má **ghost** tlačítko. Actionable ve stylu toast má
**tertiary** tlačítko. U toastu platí, že s akcí zůstane na obrazovce, dokud ho uživatel nezavře, aby
měl čas na tlačítko kliknout.

**Protože toast mizí:** Carbon velí zajistit alternativní cestu k cíli odkazu.

## Callout

- Zdůrazňuje důležitou informaci kontextově v obsahu stránky, **nelze ji zavřít**.
- Není zpětná vazba, je trvale na obrazovce.
- Použij, abys pomohl uživateli udělat dobré rozhodnutí nebo se vyhnout špatné zkušenosti.
- Umísti ji kontextově vedle akčního tlačítka, vstupu nebo dat, kterých se týká.
- **Nezaplňuj stránku víc callouty a nestohuj je.**
- Používej ji střídmě, na informaci, která nesmí být přehlédnutá. Na všechno ostatní použij běžný text.
- Titulek vynech, když je redundantní a rušil by tok čtení. Použij ho jen tehdy, když pomůže obsah
  skenovat, aniž by to odvedlo pozornost od úkolu.
- Callout **nemá vlastní akční tlačítko.** Místo toho ho umísti k tlačítku.
- Odkaz smí obsahovat, ale jen když dává kontext nebo informaci nutnou pro aktuální cestu uživatele.
  Ne na propagaci odbočky do jiné cesty.

**Umístění podle situace:**

| Vedle čeho | Kam |
|---|---|
| Tlačítko nebo vstup | **Nad** ně, aby si uživatel byl akcí jistý předtím, než ji provede |
| Data nebo informace | Kontextově před nebo za nimi, podle toho, co se hodí |
| Inline notifikace | Callout jde **nad** inline notifikaci, krátkodobá inline notifikace se dá blíž k tlačítku nebo vstupu, který ji vyvolal |

**ZDROJ:** Carbon, Notification usage, Callout ·
Carbon, Notification pattern, Callout, Best practices.
https://carbondesignsystem.com/components/notification/usage/

## Banner

- Přebírá horní část rozhraní, obecné notifikace produktu nebo systému, nesouvisí s úkolem.
- Umísti ho nahoru té obsahové oblasti, ke které patří.
- Celosystémové zprávy dej **přímo pod hlavní hlavičku nebo navigační lištu**.
- **Není sticky**, scrolluje s ostatním obsahem.
- Nepřekrývej jím jiný obsah.
- **Jen jeden banner najednou.**
- Může persistovat napříč víc sezeními.

**ZDROJ:** Carbon, Notification pattern, Banner, Best practices.
https://carbondesignsystem.com/patterns/notification-pattern/

## Notification panel

- Pro uživatele, kteří dostávají velké množství systémových notifikací nebo se k nim potřebují vracet.
- Používá se **spolu s toasty**: toast upozorní, panel archivuje.
- Zajistí, že se dají všechny notifikace přečíst bez zaplácání obrazovky trvalými zprávami.
- Carbon jmenuje, komu to konkrétně pomáhá: uživatelům, kteří potřebují víc času na přečtení, uživatelům
  čteček a těm, kdo chtějí notifikace omezit.
- Dej uživateli možnost spravovat preference notifikací.
- **Neposílej tu samou notifikaci opakovaně**, když s ní uživatel neinteraguje.
- Řaď chronologicky. Lze seskupovat podle zdroje nebo urgence.

**ZDROJ:** Carbon, Notification pattern, Notification panel, Best practices.
https://carbondesignsystem.com/patterns/notification-pattern/

## Priorita a vizuální styl

**PRAVIDLO:** Přiřaď rušivost notifikace k urgenci informace. Carbon k inline a toastu nabízí dva
kontrastní styly: **high-contrast** pro urgentní a kritické, **low-contrast** pro doplňkové zprávy
a nízkou prioritu. Toast a inline mohou používat různé styly, ale **nikdy nemíchej styly uvnitř jedné
varianty**. Když nevíš, použij low-contrast.
**KDY PLATÍ:** Volba vizuální varianty notifikace.
**TŘÍDA:** B
**ZDROJ:** Carbon, Notification pattern, Notification priority, verbatim: „Toast and inline
notifications can use different styles, but you should never mix styles within the variations." ·
Carbon, Notification usage, Modifiers: „When in doubt, use low-contrast notifications."
https://carbondesignsystem.com/components/notification/usage/

## Volitelná versus vyžadovaná akce

| Typ akce | Pravidlo |
|---|---|
| Volitelná | Actionable notifikace může mít ghost nebo tertiary tlačítko. Akce **nesmí blokovat** uživatele v pokračování. Typicky vede na flow nebo stránku, kde se to vyřeší |
| Vyžadovaná | Některé vzory musí uživateli zabránit notifikaci zavřít nebo pokračovat, dokud ji neodbaví. Typicky chyby ve formuláři nebo prázdná povinná pole. Blokující notifikace **musí** souviset s aktuálním úkolem a dát kroky k vyřešení |

**Carbonovo varování:** blokování je rušivé a zhoršuje celkovou zkušenost, takže se má používat jen
tehdy, když je kritické, aby uživatel notifikaci viděl, nebo když musí zasáhnout okamžitě.
**ZDROJ:** Carbon, Notification pattern, General user action.
https://carbondesignsystem.com/patterns/notification-pattern/

## Text notifikace

| Prvek | Pravidlo |
|---|---|
| Titulek | Krátký a popisný, nese nejdůležitější informaci. **U chyb řekni v titulku, co se zastavilo nebo nejde udělat** (Carbonův příklad: „Server instance unavailable"). Titulek nekonči tečkou |
| Tělo | Jedna až dvě krátké věty. **Neopakuj ani neparafrázuj titulek.** Vysvětli, jak to vyřešit, včetně kroků k odstranění potíží. U chybových hlášek je akce uživatele **povinná** |
| Odkaz | Musí být popisný a smysluplně naznačit cíl. Nemusí být na konci věty, může být uprostřed těla |
| Tlačítko akce | Stručně a jasně, co uživatel může udělat. Jedno až dvě slova |
| Přetečení | Když je potřeba zpráva delší než dvě řádky, použij actionable notifikaci s krátkou zprávou a odkazem „Zobrazit více", který vede na plnou zprávu (stránka s detaily nebo modal) |

**Do a Don't, které Carbon dává na konkrétních textech:**

| Do | Don't |
|---|---|
| „Success! Your resource has been created." (jasný a stručný jazyk) | „503 Service Unavailable" (technický žargon nebo neznámý jazyk) |
| „Script failed to run. Check the log for more detail." (uživatel ví, jak zasáhnout) | „Instance was not created." (uživatel bez dalších kroků) |

**ZDROJ:** Carbon, Notification usage, Content ·
Carbon, Notification pattern, Notification message.
https://carbondesignsystem.com/components/notification/usage/
Carbon odkazuje na IBM Style, Messages, a používá termín „user action" pro povinnou část chybové
hlášky.

## Kdy notifikaci neposílat

**PRAVIDLO:** Posílej notifikace jen tam, kde je to nutné. Každou omez na tu část rozhraní a flow,
ke které patří.
**PROČ:** Carbon dává dva doložené důvody a oba cituje: časté rozptylování snižuje produktivitu
(Brumby, Janssen, Mark, How Do Interruptions Affect Productivity?, 2019) a vede k alert fatigue
(Patient Safety Network, 2019).
**TŘÍDA:** B pro Carbonovo pravidlo, citované zdroje jsou publikované (kapitola v knize a odborný
primer), plný text jsem neověřoval.
**ZDROJ:** Carbon, Notification pattern, When not to use, s odkazy na
https://link.springer.com/chapter/10.1007/978-1-4842-4221-6_9 a
https://psnet.ahrq.gov/primer/alert-fatigue
**Zarámování:** Carbon transparentnost opírá o první z Nielsenových deseti heuristik (viditelnost
stavu systému). https://www.nngroup.com/articles/ten-usability-heuristics/

## Přístupnost

Dvě tvrdá pravidla, obě s odkazem na WCAG:

1. **Nepoužívej notifikace mizící na časovač pro kritické nebo havarijní zprávy.** Někteří uživatelé
   potřebují víc času na přečtení nebo interakci. (WCAG 2.1 SC 2.2.4, AAA.)
2. **Uživatel musí mít možnost spravovat nebo omezit nekritické notifikace.** Dává mu to kontrolu nad
   počtem rozptýlení, což pomáhá zvlášť uživatelům s kognitivním omezením. (WCAG 2.1 SC 2.2.3, AAA.)

Role a live regiony (`alert`, `log`, `status`, `alertdialog`, callout bez `aria-live`) jsou
v [Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md).

**ZDROJ:** Carbon, Notification pattern, Accessibility.
https://carbondesignsystem.com/patterns/notification-pattern/

---

## Co tahle nota neřeší

- Modal jako komponentu a jeho varianty. [Dialogy a panely](dialogy-a-panely.md).
- Stavové indikátory (ikony, tvary, badge, diferenciální). [Stavové indikátory](stavove-indikatory.md).
- Text chybové hlášky do detailu a zakázaný slovník.
  [Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md), tam je to s tvrdšími zdroji
  a s rozlišením tří tříd chyb podle toho, kdo je způsobil.
- Konkrétní barvy sémantických stavů. [Kontrast a barva](../../ux-design/pravidla/kontrast-a-barva.md).

## Zdroj

IBM Carbon Design System, Notification pattern a Notification usage, lokální kopie přečtená
30. 7. 2026. https://carbondesignsystem.com/patterns/notification-pattern/ ·
https://carbondesignsystem.com/components/notification/usage/
Carbon k tomuhle vzoru cituje NN/g (10 Usability Heuristics 1994, Visibility of System Status 2018,
Indicators, Validations, and Notifications 2015), Brumby et al. 2019, Alert Fatigue (PSNet 2019),
W3C ARIA Live Regions a WCAG. Třída **B**, u WCAG kritérií **A** jako požadavek.
