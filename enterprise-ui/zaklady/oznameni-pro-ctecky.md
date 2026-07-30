# Oznámení pro čtečky: názvy, role, live regiony

Co musí být v UI dostupné asistivní technologii, aby uživatel čtečky poznal totéž co uživatel oka.
Otevři, když komponenta mění stav bez přenačtení stránky, když má prvek jen ikonu bez textu, nebo když
si píšeš vlastní komponentu.

Sesterská nota: [Klávesnice a focus](klavesnice-a-focus.md). Ta řeší, jak se k prvku dostat. Tahle
řeší, co se o něm uživatel dozví.

---

## Přístupný název musí existovat u každé komponenty

**PRAVIDLO:** Každá komponenta potřebuje přístupný název: `aria-label`, `aria-labelledby` nebo
`title`. Carbon to připomíná zvlášť u tabulky, dlaždice a formulářových prvků, protože tam se to
nejčastěji zapomíná.
**KDY PLATÍ:** Vždy. Bez názvu je prvek pro čtečku bezejmenný.
**PROČ:** Carbon odkazuje na vlastní pravidlo IBM Equal Access „accessible name exists".
**TŘÍDA:** A jako požadavek (WCAG 4.1.2 Name, Role, Value), B pro Carbonovu konkrétní formulaci.
**ZDROJ:** Carbon, Data table accessibility, verbatim: „Remember to supply an `aria-label`,
`aria-labelledby` or `title` to the `Table` component to comply with accessible naming."
https://carbondesignsystem.com/components/data-table/accessibility/ · Stejná formulace u dlaždice a
formuláře: https://carbondesignsystem.com/components/tile/accessibility/ ·
https://carbondesignsystem.com/components/form/accessibility/
**KDY NEPLATÍ:** Nikdy.

**Ikonové tlačítko:** vždycky potřebuje tooltip s textem, který vysvětluje, co tlačítko udělá.
Carbon je v tom bezvýjimečný: „Regardless of how recognizable an icon may or may not be, or whether
that action lies within the universal actions list, a tooltip is always required with text explaining
what the icon button would do if clicked."
Zdroj: https://carbondesignsystem.com/components/button/usage/

**Návrhový důsledek:** Carbon vyžaduje, aby designér text tooltipu **napsal do návrhu**, s explicitním
odůvodněním: „If designers do not specify the text, developers are less likely to implement tooltips."
Výjimku dává jen ikonám se zavedeným názvem a funkcí (Bold, Italics).
Zdroj: https://carbondesignsystem.com/components/tooltip/accessibility/

## Label a helper text musí být svázané programově

**PRAVIDLO:** Label svázat s polem přes `for`. Helper text a instrukce vystavit přes
`aria-describedby`. Povinnost pole vyjádřit programově, buď v labelu, nebo přes `aria-required`.
Formulář obalit prvkem `<form>`.
**KDY PLATÍ:** Každý formulář.
**TŘÍDA:** A jako požadavek, B pro konkrétní techniku.
**ZDROJ:** Carbon, Form accessibility, verbatim: „A form must be wrapped in a `<form>` element.
Required fields must be identified programmatically, either via the label or with `aria-required`.
Helper text and other instructions should be surfaced to users via `aria-describedby` or other
accessible techniques." https://carbondesignsystem.com/components/form/accessibility/ ·
Carbon, Text input accessibility: „Labels are properly associated with inputs using the `for`
attribute. Helper text is surfaced to assistive technology through `aria-describedby`."
https://carbondesignsystem.com/components/text-input/accessibility/

**Skupiny checkboxů a radio buttonů** seskup přes `<fieldset>` a `<legend>`, aby čtečka oznámila
skupinový label a rozsah skupiny.
Zdroj: https://carbondesignsystem.com/components/checkbox/accessibility/

## Požadavky formuláře oznam na začátku, ne v polích

**PRAVIDLO:** Před formulářem musí být instrukce, která říká, jestli jsou označená povinná, nebo
volitelná pole. Tradiční formulace je „All fields are required unless marked as optional", nebo
obráceně.
**KDY PLATÍ:** Vždy, a zvlášť tam, kde označuješ jen volitelná pole.
**PROČ:** Carbon dovoluje označovat buď povinná, nebo volitelná pole (podle toho, kterých je
menšina). Uživatel ale musí vědět, který z těch dvou režimů platí, jinak neoznačené pole nedokáže
interpretovat. Carbon zároveň přiznává, že tradiční implementace (hvězdička plus legenda) je pořád
považovaná za nejpřístupnější.
**TŘÍDA:** B
**ZDROJ:** Carbon, Form accessibility, verbatim: „Traditionally, a legend at the start of a form
identifies the symbol (often an asterisk) used for required fields, and the symbol is repeated as part
of the label for each appropriate field. This is still considered the most accessible implementation."
plus „Especially where only optional fields are indicated, an instruction should precede a form."
https://carbondesignsystem.com/components/form/accessibility/
**KDY NEPLATÍ:** Carbon jmenuje výjimku: jednoduchý přihlašovací formulář se jménem a heslem tuhle
instrukci nepotřebuje, protože je kontext zjevný.

**Poznámka k rozporu s knihovnou:** [Formuláře a
stavy](../../ux-design/pravidla/formulare-a-stavy.md) doporučuje označovat volitelná pole a povinná
neoznačovat, s citací GOV.UK. Carbon to samé pravidlo obrací podle poměru polí (označ menšinu) a jako
příklad používá „complex forms" v enterprise softwaru, kde je většina polí volitelná, takže se
označují povinná. **Nejsou to protiklady, jsou to dvě kontextové varianty téhož principu „označ
menšinu".** Pro veřejné formuláře platí přísnější GOV.UK pravidlo, pro konfigurační obrazovky
enterprise produktu platí Carbonovo.

## Live regiony: kdy polite a kdy assertive

Carbon má u načítacích komponent dvě různá nastavení a je za tím rozdíl ve významu.

| Situace | Co Carbon používá |
|---|---|
| Celostránkové nebo sekční načítání (loading spinner) | `aria-live` = **assertive**, aby se stav oznámil okamžitě |
| Inline načítání u jednoho prvku | `aria-live` = **polite** |
| Notifikace, která nevyžaduje akci | role `alert`, `log` nebo `status` |
| Notifikace, která vyžaduje akci | role `alertdialog` |
| Callout | **Nemá** `aria-live` a čtečka ho automaticky neoznámí |
| Determinovaný progress bar | role `progressbar` plus `aria-valuemin`, `aria-valuemax`, `aria-valuenow` |
| Načítání části stránky | Na související prvek `aria-busy="true"` a `aria-describedby` s id progress baru |

**ZDROJ:** Carbon, Loading accessibility: „Carbon uses `aria-live` set to 'assertive' to immediately
surface a loading status to assistive technologies."
https://carbondesignsystem.com/components/loading/accessibility/ ·
Inline loading accessibility: „Carbon uses an `aria-live` region set to 'polite'."
https://carbondesignsystem.com/components/inline-loading/accessibility/ ·
Notification accessibility: „Use the roles `alert`, `log`, or `status` for notifications that do not
require user action. Use the role `alertdialog` for notifications that require user action. Callouts do
not have an aria-live attribute, and are not automatically announced by screen readers."
https://carbondesignsystem.com/components/notification/accessibility/ ·
Progress bar accessibility: https://carbondesignsystem.com/components/progress-bar/usage/

**Carbonovo varování k rolím:** nedoporučuje experimentovat za hranicí `alert`, `log`, `status`
a `alertdialog` u notifikací řízených událostmi, protože to přináší specifické problémy. Nabízí dvě
prozkoumatelné cesty: sbírat notifikace do trvalé oblasti v aplikaci, kam uživatel dojde a odbaví je,
nebo je vykreslovat do už existujícího `region`, do kterého se skočí hotkeyí a po dojití na konec
oblasti se focus vrátí tam, kde byl. Sám dodává, že ani jedna cesta není bezvadná.
Zdroj: https://carbondesignsystem.com/components/notification/accessibility/

## Konec načítání se musí oznámit taky

**PRAVIDLO:** Zmizení spinneru je druhá informace („hotovo"), a tu uživatel, který ho nevidí,
nedostane. Oznam dokončení jednou ze dvou cest: buď focus přejde na nový obsah (typicky po načtení
celé stránky), nebo pošli neviditelnou stavovou zprávu („loading complete") do `aria-live` oblasti
nebo přes `role="status"`.
**KDY PLATÍ:** Vždy, a zvlášť u načítání delších než pár sekund.
**PROČ:** Carbon: „a user who cannot see the icon disappear needs to be made aware the system is no
longer 'loading' and is thus available for usage."
**TŘÍDA:** B pro techniku, A pro požadavek (WCAG 4.1.3 Status Messages, AA).
**ZDROJ:** Carbon, Loading accessibility, sekce „Convey when loading has completed".
https://carbondesignsystem.com/components/loading/accessibility/ ·
Obecné oznamování stavů včetně WCAG 4.1.3:
[Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md), sekce Chybové stavy.
**KDY NEPLATÍ:** Nikdy, ale Carbon nechává volbu techniky na kontextu. Když focus přejde na nový
obsah, samostatná zpráva už potřeba není.

**Návrhový důsledek:** Carbon vyžaduje anotaci, která komponenta dostane focus po dokončení načítání.

**Inline loading bez viditelného textu** vystavuje stav přes `title` stavové ikony, aby čtečka řekla
„active", „finished" nebo „error". Když text viditelný je, použije se ten.
Zdroj: https://carbondesignsystem.com/components/inline-loading/accessibility/

## Stav a hodnota, kterou vidíš, musí být i v kódu

| Co | Jak to Carbon vystavuje |
|---|---|
| Řazení sloupce | `aria-sort` |
| Částečně zaškrtnutý checkbox (indeterminate) | `aria-checked="mixed"` |
| Otevřený nebo zavřený seznam voleb | `aria-expanded` |
| Vybraný tab | `aria-selected="true"` a `tabindex="0"`, ostatní `"false"` a `"-1"` |
| Vazba tabu na panel | `aria-controls` |
| Modal | role `dialog` a `aria-modal="true"`, název přes `aria-label` se stejným textem jako titulek |
| Přepínací tlačítko | `aria-pressed` |
| Dropdown a multiselect | `button` s `aria-haspopup="listbox"` |
| Combo box | `input` s `role="combobox"`, `aria-autocomplete="list"`, `aria-haspopup="listbox"`, `autocomplete="off"`, `aria-controls` na `div` s `role="listbox"` |
| Vyhledávání | celá interakce má `role="search"`, vstup `role="searchbox"` (nebo `type="search"`), neviditelné labely „search" a „clear search input" |
| Drobenka | `<nav>` (nebo landmark „navigation") s názvem „breadcrumb", odkazy jako položky seznamu, výpustka je tlačítko „more breadcrumbs" |
| Toggletip | `aria-expanded` na triggeru, `aria-controls` na obsah, trigger má `aria-label="Show information"` |
| Tooltip | span s `role="tooltip"` a `aria-hidden="true"`, trigger má `aria-labelledby` |

**ZDROJ:** Příslušné stránky `accessibility` jednotlivých komponent Carbonu, lokální kopie přečtená
30. 7. 2026. Například https://carbondesignsystem.com/components/tabs/accessibility/ ·
https://carbondesignsystem.com/components/dropdown/accessibility/ ·
https://carbondesignsystem.com/components/breadcrumb/accessibility/

**Pozor na jeden detail u tooltipu:** kombinace `role="tooltip"` s `aria-hidden="true"` na obsahu
a `aria-labelledby` na triggeru znamená, že text tooltipu funguje jako **název triggeru**, ne jako
samostatně čtený obsah. Proto do tooltipu nepatří nic, co má být čteno jako obsah, a proto tam nesmí
být interaktivní prvky.

## Sémantická struktura, ne jen vizuál

- Každý odkaz v drobence je položka neuspořádaného seznamu, aby čtečka dala kontext. Vizuální
  oddělovače (lomítka) nejsou text a nemají být navigovatelné, Carbon je dělá v CSS.
- Sloupcové hlavičky tabulky a structured listu musí popisovat data v řádcích a sloupcích.
- Popis nebo caption tabulky svázat přes `aria-describedby`.
- Skupina checkboxů: `<fieldset>` plus `<legend>`.

**ZDROJ:** https://carbondesignsystem.com/components/breadcrumb/accessibility/ ·
https://carbondesignsystem.com/components/structured-list/accessibility/

## Dekorativní obrázky se mají přeskočit

**PRAVIDLO:** Ilustrace v prázdném stavu je dekorativní a čtečka ji má přeskočit: prázdný `alt`.
Carbon doporučuje prázdný `alt` místo `role="presentation"`, protože je širší podpora. A dekorativní
obrázek nesmí nést žádnou informaci.
**KDY PLATÍ:** Ilustrace v prázdných stavech, dekorace v dlaždicích.
**TŘÍDA:** A jako požadavek (WCAG, W3C tutoriál k dekorativním obrázkům), B pro volbu techniky.
**ZDROJ:** Carbon, Empty states pattern, Accessibility, verbatim: „As an empty `alt` tag is more
widely supported, we recommend you align with the WCAG guidance and avoid assigning `role` to
`presentation` until support is more ubiquitous."
https://carbondesignsystem.com/patterns/empty-states-pattern/ ·
Carbon, Tile accessibility: „Decorative images should have an empty `alt` attribute (`alt=""`) while
informative images should include descriptive `alt` text."
https://carbondesignsystem.com/components/tile/accessibility/
**KDY NEPLATÍ:** Obrázek, který nese informaci. Ten potřebuje popisný `alt`.

## Prázdný stav musí nahradit obsah, ne se přidat k němu

**PRAVIDLO:** Prázdný stav tabulky nahradí celou tabulku, včetně záhlaví a zápatí. Nezobrazuj prázdnou
tabulku se zprávou pod ní.
**KDY PLATÍ:** Každý prázdný stav uvnitř datové komponenty.
**PROČ:** Carbon dává přímo přístupnostní důvod: jinak čtečka přečte celou tabulku, než se dostane
ke zprávě, že v ní nic není.
**TŘÍDA:** B
**ZDROJ:** Carbon, Empty states pattern, Best practices, verbatim: „Empty states should replace the
element that would ordinarily show. For example, an empty state for a table would replace the table
and the column headers and footer should not be present. This practice avoids having a screen reader
read the entire table before getting to the message that there is no content in the table."
https://carbondesignsystem.com/patterns/empty-states-pattern/
**KDY NEPLATÍ:** Nikdy. Platí i pro prázdný výsledek hledání: podkladový obsah se má nahradit
zprávou.

## Nezobrazuj rich text jako nositele významu v notifikaci

**PRAVIDLO:** Čtečka přečte titulek i tělo notifikace jako jednu větu. Nespoléhej na formátování
textu (tučné, kurzíva) jako na nositele významu.
**TŘÍDA:** B
**ZDROJ:** Carbon, Notification usage, verbatim: „When using rich text, such as in a title, a screen
reader will read aloud the entire message as one sentence. Because the message will be read as one
string, do not depend on text styling to convey meaning."
https://carbondesignsystem.com/components/notification/usage/

## Časované notifikace nejsou pro kritické zprávy

**PRAVIDLO:** Nepoužívej notifikaci, která zmizí sama, pro kritickou nebo havarijní zprávu. Někteří
uživatelé potřebují víc času na přečtení nebo na interakci.
**KDY PLATÍ:** Toast s časovačem.
**TŘÍDA:** A jako požadavek (WCAG 2.2.4 No Timing, AAA), B pro Carbonovo doporučení.
**ZDROJ:** Carbon, Notification pattern, Accessibility, verbatim: „Don't use notifications that dismiss
on a timer for critical or emergency messages. Some users with disabilities need more time to read or
interact with messages and timed actionable toasts may not provide sufficient time." s odkazem na
WCAG 2.1 SC 2.2.4 (AAA). https://carbondesignsystem.com/patterns/notification-pattern/
**Druhé pravidlo ze stejné sekce:** uživatel musí mít možnost spravovat nebo omezit nekritické
notifikace, s odkazem na WCAG 2.1 SC 2.2.3 Interruptions (AAA). Carbon k tomu dodává, že je to
užitečné hlavně pro uživatele s kognitivním omezením.

---

## Co tahle nota neřeší

- Klávesovou obsluhu. To je [Klávesnice a focus](klavesnice-a-focus.md).
- Kontrastní požadavky na text a nesouvislý obsah.
  [Kontrast a barva](../../ux-design/pravidla/kontrast-a-barva.md), tam je to s třídou A.
- Oznamování validačních chyb a error summary. To má tvrdší zdroje ve
  [formulářích a stavech](../../ux-design/pravidla/formulare-a-stavy.md).
- Testování s reálnými čtečkami. Carbon u notifikací uvádí, že chování zavírání klávesou je stejné
  ve VoiceOveru, JAWS i NVDA, ale metodiku testování nedokumentuje.

## Zdroj

IBM Carbon Design System, stránky `accessibility` u 20 komponent plus sekce Accessibility ve vzorech
prázdných stavů, notifikací, dialogů, načítání a read-only stavů. Lokální kopie přečtená 30. 7. 2026.
Carbon odkazuje na WAI-ARIA Authoring Practices, W3C WAI tutoriály a IBM Equal Access Toolkit.
Třída **B** pro Carbonovy konkrétní techniky, **A** pro odkazované WCAG požadavky.
