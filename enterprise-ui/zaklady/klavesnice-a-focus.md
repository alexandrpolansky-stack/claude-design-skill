# Klávesnice a focus napříč komponentami

Referenční tabulka klávesové obsluhy a chování focusu pro každou komponentu, kterou Carbon
dokumentuje. Otevři vždy, když stavíš interaktivní prvek, a hlavně když si píšeš vlastní komponentu
místo hotové z knihovny.

Tahle nota zaplňuje mezeru, kterou [STATUS.md](../../STATUS.md) jmenuje explicitně: klávesová
navigace, ARIA vzory a focus management napříč komponentami. Kontrast a velikost terče jsou pokryté
jinde, viz [kontrast a barva](../../ux-design/pravidla/kontrast-a-barva.md) a
[tlačítka](../../ux-design/pravidla/tlacitka.md).

Související: [Oznámení pro čtečky](oznameni-pro-ctecky.md) ·
[Disabled versus read-only](../vzory/disabled-vs-read-only.md)

---

## Základní princip: Tab dovnitř, šipky uvnitř

**PRAVIDLO:** Jednoduchý prvek (tlačítko, odkaz, vstup, checkbox) je vlastní tabstop. Složená
komponenta (tablist, skupina radio buttonů, skupina single-select dlaždic, otevřený seznam voleb) je
**jeden** tabstop a uvnitř se pohybuješ šipkami.
**KDY PLATÍ:** Vždy. Je to nejčastější chyba u vlastních komponent.
**PROČ:** Když má tablist s osmi taby osm tabstopů, uživatel klávesnice se k obsahu dostane na devátý
stisk. Šipky uvnitř skupiny to zkrátí na dva.
**TŘÍDA:** B
**ZDROJ:** Carbon, Tabs accessibility, verbatim: „Tabs take at least two tabstops, one for the
tablist and one for the tabpanel." a „Arrow keys are used to navigate between individual tab items in
the tablist." https://carbondesignsystem.com/components/tabs/accessibility/ ·
Carbon, Tile accessibility, u single-select skupiny: „the group is treated as a single tab stop...
Users can navigate through the items using the arrow keys."
https://carbondesignsystem.com/components/tile/accessibility/
**KDY NEPLATÍ:** Checkboxy. Ty jsou i ve skupině každý vlastní tabstop, protože to odpovídá
zavedenému chování HTML. Carbon: „Each checkbox can be reached by `Tab` and selected with `Space`
independently. This matches the established HTML interaction pattern."
https://carbondesignsystem.com/components/checkbox/accessibility/

**Proč právě tenhle rozdíl mezi checkboxem a radiem:** Carbon to zdůvodňuje tím, že checkbox je jedna
samostatná volba, zatímco skupina radio buttonů tvoří jednu vzájemně se vylučující volbu, takže se
chová jako jeden prvek. Stejnou logiku přenáší na dlaždice.
Zdroj: https://carbondesignsystem.com/components/tile/accessibility/

---

## Referenční tabulka

### Akce a tlačítka

| Komponenta | Klávesy |
|---|---|
| Tlačítko | `Tab` na něj, `Space` nebo `Enter` aktivuje |
| Ikonové tlačítko bez labelu | Stejné. Label se vypisuje na hover **a na focus**, ne jen na hover |
| Odkaz použitý jako tlačítko | Musí být dokódovaný, aby fungoval i `Space`. Odkaz sám reaguje jen na `Enter` |
| Přepínací tlačítko (toggle button) | Stav nese `aria-pressed` true/false, nebo změna názvu odrážející změnu ikony (play / pause) |

**ZDROJ:** Carbon, Button accessibility, verbatim: „Where links have been 'repurposed' as a button,
they need to be coded so the `Space` key can also activate (since links are only activated by default
by `Enter`)." https://carbondesignsystem.com/components/button/accessibility/

### Vstupy

| Komponenta | Klávesy |
|---|---|
| Text input, text area | Každé pole je tabstop. Informační ikona před polem je taky tabstop (otevře `Enter`/`Space`, zavře `Esc`) |
| Password input | Přepnutí viditelnosti hesla je obsluhovatelné `Enter` nebo `Space` |
| Pohyb v textu | `Ctrl` (Windows) nebo `Option` (Mac) plus šipky vlevo/vpravo po slovech, nahoru/dolů na začátek a konec obsahu |
| Chování při focusu | V text inputu se existující text označí a přepíše se při psaní. V text area se text neoznačí, kurzor je na začátku nebo na místě poslední interakce |
| Checkbox | `Tab` na každý, `Space` přepne |
| Search | V tab orderu, na focus lze hned psát, `Enter` odešle, `Esc` vymaže. Křížek pro vymazání je další tabstop, aktivuje ho `Space` nebo `Enter` |

**ZDROJ:** https://carbondesignsystem.com/components/text-input/accessibility/ ·
https://carbondesignsystem.com/components/search/accessibility/ ·
https://carbondesignsystem.com/components/checkbox/accessibility/

### Seznamy voleb: každá varianta se ovládá jinak

Tohle je místo, kde se nejčastěji chybuje, protože prvky vypadají stejně a chovají se různě.

| Varianta | Otevře se | Pohyb | Vybere | Zavře bez změny |
|---|---|---|---|---|
| Nativní select | `Space`, `Up`, `Down` | šipky, plus skok na první položku daným písmenem | `Space` nebo `Enter` (zavře) | `Esc` |
| Dropdown | `Enter`, `Space`, `Down` | šipky | `Space` nebo `Enter` (zavře) | `Esc` nebo `Tab` |
| Multiselect | `Down`, `Enter`, `Space` | šipky | `Enter` nebo `Space` přepíná jednotlivé volby, seznam zůstává otevřený | `Esc`. `Delete` ve sbaleném poli vymaže všechny volby |
| Combo box | `Enter`, `Up`, `Down`, nebo psaní (filtruje) | šipky | `Enter` (vybere zvýrazněné a zavře) | `Esc` sbalí seznam nebo vymaže napsaný text |

**Tvrdé specifikum combo boxu:** `Space` v combo boxu **nevybírá**, protože vloží mezeru do
filtrovaného textu. Kdo to v custom komponentě navěsí na `Space`, rozbije psaní.
**ZDROJ:** Carbon, Dropdown accessibility, verbatim: „`Space` cannot be used for selecting, as
pressing it will submit a space character into the filter string."
https://carbondesignsystem.com/components/dropdown/accessibility/

**Kam skočí focus po otevření:** Carbon má u dropdownu, multiselectu i combo boxu stejné pravidlo.
Focus se přesune do seznamu voleb **jen** tehdy, když už je nějaká volba vybraná, nebo když se seznam
otevřel šipkou (u combo boxu i když se napsal odpovídající text). Jinak zůstane na poli.
**ZDROJ:** https://carbondesignsystem.com/components/dropdown/accessibility/

### Přepínání obsahu

| Komponenta | Klávesy |
|---|---|
| Tabs (tablist) | Jeden tabstop. `Left` a `Right` mezi taby, na konci se pohyb **zabalí** na druhý konec. Scrollovací tablist se posouvá sám, aby byl fokusovaný tab vidět |
| Tabs, další tabstop | `Tab` z tablistu jde na první ovladatelný prvek v panelu. Když panel žádný nemá, focus dostane **celý panel**, aby se dal scrollovat |
| Automatický tablist | Focus a výběr jsou synchronizované: šipka tab zároveň vybere a panel se překreslí |
| Manuální tablist | Šipka jen přesune focus, výběr zůstává. Vybere se `Enter` nebo `Space` |
| Progress indicator (interaktivní varianta) | `Left` a `Right` mezi kroky |
| Breadcrumb | Každý odkaz `Tab`, aktivuje `Enter`. Aktuální stránka, pokud je v drobence, není odkaz. Výpustka pro přetečení je v tab orderu |

**Kdy manuální tablist:** když se obsah panelu načítá dlouho. Automatický by uživatele klávesnice nebo
čtečky nutil čekat na každý načtený panel při průchodu.
**ZDROJ:** Carbon, Tabs usage: „Use manual tabs when information in the tab panel will take a longer
time to load. This will allow a keyboard user or screen reader to navigate through the tablist without
having to wait for content to load." https://carbondesignsystem.com/components/tabs/usage/

**Návrhový důsledek:** automatický a manuální tablist jsou ve wireframu nerozlišitelné. Carbon proto
vyžaduje, aby designér do návrhu **anotoval**, která varianta se implementuje, a aby to rozhodl
společně s vývojářem, protože je to rozhodnutí o latenci.
**ZDROJ:** https://carbondesignsystem.com/components/tabs/accessibility/

### Kontejnery a dlaždice

| Situace | Klávesy |
|---|---|
| Dlaždice bez vlastní interakce (obsahuje odkazy nebo tlačítka) | Dlaždice sama focus nedostane. `Tab` prochází prvky uvnitř, pak jde mimo dlaždici |
| Klikatelná dlaždice (celá je odkaz) | Dlaždice je tabstop, `Enter` aktivuje |
| Single-select skupina dlaždic | Celá skupina je **jeden** tabstop, šipky uvnitř. `Tab` skupinu opustí. Nic nemusí být předvybrané, pak focus přijde na první položku |
| Multi-select dlaždice | Každá je tabstop, `Space` nebo `Enter` přepíná |
| Rozbalovací dlaždice bez interaktivních prvků | `Space` nebo `Enter` rozbalí a sbalí celou dlaždici |
| Rozbalovací dlaždice s interaktivními prvky | Rozbaluje ikonové tlačítko s chevronem, ne kontejner |
| Structured list, selectable | `Tab` na další řádek, `Space` vybere, `Up` a `Down` posouvají focus |

**Tvrdé pravidlo:** neklaď interaktivní prvky na plochu, která je sama interaktivní. Carbon:
„avoid placing interactive elements on top of a directly interactive tile, as actions should not
overlap on an actionable surface". Řešení je základní dlaždice bez rámečku, která interaktivní není.
**ZDROJ:** https://carbondesignsystem.com/components/tile/accessibility/
Detail: [Dlaždice a karty](../komponenty/dlazdice-a-karty.md)

### Tabulky a stránkování

| Situace | Klávesy |
|---|---|
| Řaditelné záhlaví | Hlavička sloupce je dosažitelná `Tab`, řadí `Space` nebo `Enter` |
| Prvky v buňkách | Odkazy, vstupy a další ovládací prvky jsou v tab orderu a chovají se normálně |
| Rozbalovací řádky | Chovají se jako accordion |
| Pagination | Tab order zleva doprava. Selecty otevře `Space`, `Up` nebo `Down` (šipky zároveň cyklují hodnoty), vybere `Space` nebo `Enter`, zavře `Esc`. Předchozí a další stránka `Space` nebo `Enter` |
| Pagination na kraji rozsahu | Nedostupné tlačítko přestane být navigovatelné i ovladatelné, jako každý disabled prvek |

**Návrhový důsledek u řazení:** řaditelnost tabulky nemá trvalý vizuální indikátor (ikony se
objevují na hover a focus), takže designér musí do návrhu anotovat, že se má tabulka implementovat
s řaditelnými hlavičkami.
**ZDROJ:** https://carbondesignsystem.com/components/data-table/accessibility/ ·
https://carbondesignsystem.com/components/pagination/accessibility/

### Dialogy

**Focus při otevření modalu závisí na typu dialogu.** Carbon má dvě formulace, které se liší podle
místa v dokumentaci, a je potřeba znát obě:

| Typ dialogu | Kam přijde první focus |
|---|---|
| Dialog s vstupními polemi (transakční) | První pole, které přijímá vstup. Ne tlačítko |
| Dialog bez polí, potvrzení nebo rozhodnutí | Primární tlačítko, bez ohledu na počet tlačítek |
| Pasivní dialog (jen informace) | Zavírací křížek, protože jiné tlačítko nemá |
| Destruktivní akce (danger) | Tlačítko **Zrušit**, ne červené destruktivní tlačítko |

**Zbytek mechaniky:**

1. Focus se při otevření přesune do dialogu.
2. Focus zůstane uvnitř (trap). `Tab` ani `Shift+Tab` ho nedostanou mimo modal.
3. `Esc` dialog zavře.
4. Po zavření se focus vrátí na prvek, který dialog vyvolal.
5. Tab order: první interaktivní prvek v těle, dál zleva doprava a shora dolů tělem, pak primární
   akce, sekundární akce, zavírací křížek.

**ZDROJ:** Carbon, Dialog pattern, Accessibility, verbatim: „Shift the focus into the dialog when
triggered... the focus should be trapped inside the dialog and must not move outside the modal until
it is closed. After a modal dialog closes, focus should return to the element that invoked the modal."
https://carbondesignsystem.com/patterns/dialog-pattern/ ·
Carbon, Modal accessibility, focus podle typu dialogu verbatim: „For dialogs which prompt for
confirmation or user decision, the primary button takes focus (regardless of number of buttons). For
destructive interactions, the 'cancel' button takes focus, not the red danger/delete button."
https://carbondesignsystem.com/components/modal/accessibility/ ·
Carbon, Modal usage, u dialogu s formulářem: „set the initial focus to the first location that accepts
user input". https://carbondesignsystem.com/components/modal/usage/
**Odkaz na normu:** Carbon odkazuje na WCAG 2.4.3 Focus Order.

**Návrhový důsledek:** u transakčního dialogu musí designér anotovat, které pole dostane focus.
Textový odkaz se za vstup nepočítá.

### Notifikace a nápověda

| Komponenta | Chování focusu |
|---|---|
| Inline a toast notifikace | Neobsahují interaktivní prvky a focus **nedostávají** |
| Actionable notifikace | Při vyvolání si focus **vezme a drží** (trap), dokud se akce neprovede nebo notifikace nezavře. `Tab` mezi akcí a křížkem, zavírá `Enter`, `Space` nebo `Esc` |
| Callout | Může obsahovat odkazy, ty se procházejí `Tab` a aktivují `Enter` nebo `Space` |
| Tooltip | Zobrazí se, když trigger dostane focus. Zavírá `Esc`. Sám focus nedostane a nesmí obsahovat interaktivní prvky |
| Toggletip | Trigger je tlačítko v tab orderu, `Enter` nebo `Space` přepíná a **focus zůstává na triggeru**. Když je uvnitř interaktivní obsah, `Tab` do něj vstoupí. `Esc` zavře a vrátí focus na trigger |
| Tag, read-only | Není v tab orderu, focus nedostane |
| Tag, dismissible | V tab orderu, focus okolo zavíracího křížku, `Enter` nebo `Space` zavře |
| Tag, selectable a operational | V tab orderu, focus okolo celého tagu, `Enter` nebo `Space` přepne nebo rozbalí |

**Proč je actionable notifikace drahá:** protože si bere focus, je podle Carbonu „highly disruptive
to screen readers and keyboard users". Používej ji jen tam, kde je interakce nutná.
**ZDROJ:** https://carbondesignsystem.com/components/notification/accessibility/ ·
https://carbondesignsystem.com/components/tooltip/accessibility/ ·
https://carbondesignsystem.com/components/toggletip/accessibility/ ·
https://carbondesignsystem.com/components/tag/accessibility/

**Kdy tooltip a kdy toggletip:** rozdíl není vizuální, je v tom, jak se vyvolá a jestli obsah
potřebuje interakci. Tooltip na hover nebo focus, jen text, nikdy interaktivní prvky. Toggletip na
klik nebo `Enter`, když musí být uvnitř tlačítko nebo odkaz. Carbon k tomu dodává důvod: tooltip
focus nedostane, takže interaktivní prvky uvnitř jsou pro některé uživatele nedosažitelné.
**ZDROJ:** https://carbondesignsystem.com/components/tooltip/usage/
Detail: [Tooltip a toggletip](../komponenty/tooltip-a-toggletip.md)

### Filtrování s fasetami

Carbon pro fasetový filtr popisuje dvouúrovňovou obsluhu:

1. `Tab` prochází **skupiny** filtrů.
2. `Enter` vstoupí do faset uvnitř skupiny.
3. Šipky se pohybují mezi fasetami.
4. `Enter` na fasetě ji zapne nebo vypne.
5. **Po přepnutí fasety musí focus zůstat na místě**, i když se obsah pod tím přenačte. Jinak
   uživatel musí protabovat všechno znovu při každém dalším filtru.

**ZDROJ:** Carbon, Search pattern, Accessibility, Faceted filtering, verbatim: „After a facet is
selected or deselected, the focus state should be retained as the content reloads, that way users
don't have to `TAB` through everything again as they move down the list."
https://carbondesignsystem.com/patterns/search-pattern/
Detail: [Filtrování](../vzory/filtrovani.md)

---

## Disabled versus read-only z pohledu klávesnice

**PRAVIDLO:** Rozliš navigovatelnost a ovladatelnost. Read-only prvek **zůstává navigovatelný**, aby
si uživatel mohl obsah přečíst, ale není ovladatelný, hodnotu nezmění. Disabled prvek není
navigovatelný vůbec, klávesnice se k němu nedostane.
**KDY PLATÍ:** Vždy, když se rozhoduješ mezi disabled a read-only.
**PROČ:** Když je obsah pro uživatele relevantní, disabled ho z klávesnice i ze čtečky odřízne.
**TŘÍDA:** B
**ZDROJ:** Carbon, Read-only states pattern, Accessibility, verbatim: „A component that can be reached
by keyboard is navigable. Read-only components remain navigable so that users can review the
information they contain. This contrasts with disabled components, which cannot be reached by
a keyboard. However, read-only components are not operable, meaning users can neither manipulate nor
alter their values." https://carbondesignsystem.com/patterns/read-only-states-pattern/
**KDY NEPLATÍ:** Nic, ale Carbon dodává, že se stav nemá překlápět jen kvůli režimu zobrazení: prvek,
který je disabled, má zůstat disabled i v read-only pohledu.
Detail: [Disabled versus read-only](../vzory/disabled-vs-read-only.md)

## Pořadí tabů u vícesloupcového rozvržení

**PRAVIDLO:** Když jsou prvky ve víc sloupcích a mají smysluplné pořadí (dny v týdnu, měsíce),
anotuj, jestli tab order jde po řádcích nebo po sloupcích. Bez toho to implementace uhádne špatně.
**KDY PLATÍ:** Checkboxy a radio buttony ve víc sloupcích, mřížky voleb.
**TŘÍDA:** B
**ZDROJ:** Carbon, Checkbox accessibility, Meaningful order: „Checkboxes can appear in multiple
columns. If there is a meaningful order to the items (such as days of the week), annotate whether the
tab order is by row or by column."
https://carbondesignsystem.com/components/checkbox/accessibility/

---

## Kontrolní seznam před předáním

Vlastní destilát, ne Carbonův seznam (**třída C**):

1. Projdi celou obrazovku jen klávesnicí, bez myši. Dostaneš se všude?
2. Je focus vždycky viditelný? (WCAG 2.4.7, třída A jako požadavek.)
3. Má složená komponenta jeden tabstop a šipky uvnitř?
4. Dostane modal focus při otevření na správný prvek a vrátí ho po zavření?
5. Zavírá `Esc` všechno, co se dá zavřít (modal, dropdown, tooltip, toggletip, notifikaci)?
6. Zůstává focus na místě po přenačtení obsahu filtrem nebo řazením?
7. Je něco, co je disabled, ale uživatel to potřebuje přečíst? Pak to má být read-only.
8. Je u ikonového tlačítka label dostupný i na focus, ne jen na hover?

## Co tahle nota neřeší

- Jak se stav oznámí čtečce. To je [Oznámení pro čtečky](oznameni-pro-ctecky.md).
- Vizuální podobu focus ringu a kontrastní požadavky.
  [Stroke a hranice](../../ux-design/pravidla/stroke-a-hranice.md) a
  [tlačítka](../../ux-design/pravidla/tlacitka.md).
- Velikost klikatelného terče (WCAG 2.5.8). [Tlačítka](../../ux-design/pravidla/tlacitka.md).
- Komponenty, které v přečtené kopii Carbonu nejsou (accordion, overflow menu, date picker, slider,
  toggle, radio button, file uploader, content switcher, UI shell). Klávesová obsluha některých z nich
  je tady zmíněná jen zprostředkovaně, přes komponenty, které na ně odkazují.

## Zdroj

IBM Carbon Design System, stránky `accessibility` u 20 komponent plus sekce Accessibility ve vzorech
dialogu, hledání a read-only stavů. Lokální kopie přečtená 30. 7. 2026.
Carbon u těchto stránek odkazuje na WAI-ARIA Authoring Practices a na IBM Equal Access Toolkit; kde
uvádí konkrétní WCAG kritérium, uvádím ho taky. Třída **B** pro Carbonovu konkrétní mechaniku,
**A** pro odkazované WCAG požadavky.
