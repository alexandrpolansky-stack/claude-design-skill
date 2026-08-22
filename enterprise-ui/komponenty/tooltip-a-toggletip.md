# Tooltip a toggletip

Vypadají stejně, chovají se různě. Rozdíl je v tom, **jak se vyvolávají** a **jestli obsah potřebuje
interakci**.

Související: [Textová pole](textova-pole.md) ·
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md) ·
[Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md) ·
[Překryvy a vrstvení](../vzory/prekryvy-a-vrstveni.md)

---

## Rychlé rozhodnutí

1. Krátká doplňková informace, **jen text** = **tooltip**, na hover nebo focus.
2. Uvnitř musí být **tlačítko, odkaz nebo obrázek** = **toggletip**, na klik nebo `Enter`.
3. Informace je **zásadní pro dokončení úkolu** = **ani jedno**, dej helper text.
4. Kritická informace nebo povinný vstup = **modal**.
5. **Nikdy nedávej interaktivní prvky do tooltipu.**
6. Ikonové tlačítko **vždycky** potřebuje tooltip. Bez výjimky.
7. Ikona pro doplňkovou informaci je **„i"**, ne „?".
8. Tooltip zavírá `Esc`. Toggletip taky, a vrací focus na trigger.
9. Toggletip max **288 px** šířky, doporučeně do čtyř sloupců.
10. Tooltip **nesmí zakrývat obsah zásadní pro úkol** ani vytéct ze stránky.

---

## Rozdíl v jedné tabulce

| | Tooltip | Toggletip |
|---|---|---|
| Vyvolání | **Hover nebo focus** | **Klik nebo `Enter`** |
| Zavření | Odhoverování, přesun focusu, `Esc` | Další klik na trigger, klik mimo, `Esc` |
| Obsah | **Jen text**, neinteraktivní | Text **i interaktivní prvky** |
| Dostane focus | **Ne** | Obsah ano, když má interaktivní prvky |
| Vzor | Popover jako základ | **Disclosure pattern** |

**Carbonova formulace rozdílu verbatim:** „A tooltip is exposed on hover or focus when you need to
disclose brief, supplemental information that is not interactive. A toggletip is used on click or enter
when you must expose interactive elements, such as a button, that a user needs to interact with."
**ZDROJ:** Carbon, Tooltip usage, Tooltips versus toggletips a Toggletip usage, Toggletips versus
tooltips. https://carbondesignsystem.com/components/tooltip/usage/ ·
https://carbondesignsystem.com/components/toggletip/usage/

## Tooltip je vestavěný, ne samostatný

**PRAVIDLO:** Tooltip je **vložený v jiných komponentách**, ne používaný samostatně. Většina komponent
(ikonová tlačítka, ikonové taby, slidery, kopírovací tlačítka) **už tooltip vestavěný má**, takže není
potřeba ho přidávat zvlášť. **Přizpůsobení je povolené, ale nedoporučené.**
**Jediná výjimka:** definition tooltip, který zůstává samostatnou komponentou.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Tooltip usage, Overview, verbatim: „By default, most components such as icon buttons,
icon tabs, sliders, and copy buttons already have built-in tooltips, so there's no need to add one
separately. Customization is allowed but not recommended."
https://carbondesignsystem.com/components/tooltip/usage/

**Poznámka k aktuálnosti:** Carbon u tooltipu uvádí, že vodítko **aktualizoval** a už nevyčleňuje
„standard" a „icon button" tooltip jako samostatné varianty, protože jsou tooltipy vložené v jiných
komponentách. Breaking changes v tom podle něj nejsou.

## K čemu tooltip použít

Carbon jmenuje čtyři případy:

1. Zobrazit názvy ovládacích prvků, například ikonových tlačítek, které nemají vizuální label.
2. Dodat doplňkovou informaci k fokusovatelným prvkům, aby uživatel mohl udělat informované rozhodnutí.
3. Nabídnout víc kontextu nebo vysvětlení ke konkrétním prvkům.
4. Definovat pojem nebo dodat detaily k inline položce (**definition tooltip**).

**Definition tooltip:** používá se k definici pojmů nebo k dodání pomoci uvnitř textu. Funguje dobře na
labelech UI, slovech v odstavcích, nebo v kompaktních prostorech jako datové tabulky, kde by ikony
navíc zaplácávaly rozhraní.

**ZDROJ:** Carbon, Tooltip usage, When to use.
https://carbondesignsystem.com/components/tooltip/usage/

## Dvě věci, které tooltip nesmí

### Nést zásadní informaci

**PRAVIDLO:** Protože tooltip zmizí, když uživatel odhoveruje, **nedávej do něj informaci podstatnou
pro dokončení úkolu**. Na zásadní informace, jako jsou povinná pole, použij **helper text, který je vždy
viditelný a dostupný**.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Tooltip usage, When not to use, Provide critical information.
https://carbondesignsystem.com/components/tooltip/usage/
**Souvislost:** Carbon k tomu ve Forms pattern dodává argument s odkazem na výzkum: uživatel by neměl
muset hledat tooltip, aby se dostal k informaci zásadní pro dokončení úkolu (NN/g, Tooltip Guidelines,
2019). Detail rozhodnutí helper text versus placeholder versus tooltip:
[Textová pole](textova-pole.md).

### Obsahovat interaktivní prvky

**PRAVIDLO:** **Nedávej do tooltipu interaktivní prvky.**
**PROČ:** Carbon dává dva důvody: interaktivní prvky v tooltipech jsou pro některé uživatele nedostupné
a jsou těžko použitelné pro všechny, **protože tooltipy nedostávají focus**. Když je potřeba dát do
doplňkové informace obrázky, tlačítka nebo odkazy, použij **toggletip** a disclosure pattern, který
umožňuje lepší strukturu tabování a focusu.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Tooltip usage, When not to use, Include interactive elements, verbatim: „Interactive
elements in tooltips are inaccessible for some users and are hard to use for all users since tooltips do
not receive focus." https://carbondesignsystem.com/components/tooltip/usage/
**Technický důvod navíc:** Carbon tooltip implementuje jako span s `role="tooltip"` a `aria-hidden="true"`,
a trigger má `aria-labelledby`. To znamená, že text tooltipu funguje jako **název triggeru**, ne jako
samostatně čtený obsah. Detail: [Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md).

## Anatomie tooltipu

1. **UI trigger:** jakákoliv komponenta s integrovaným tooltipem, nebo definiční pojem s tečkovaným
   podtržením.
2. **Caret tip:** úzce asociuje kontejner se souvisejícím triggerem.
3. **Kontejner:** obsahuje krátký text.

**ZDROJ:** Carbon, Tooltip usage, Anatomy.
https://carbondesignsystem.com/components/tooltip/usage/

## Zarovnání a umístění tooltipu

- Kontejner lze zarovnat na **start, center nebo end**, aby nevytékal ze stránky ani nezakrýval důležitou
  informaci.
- **Trigger tlačítko a caret tip mají být svisle vycentrované navzájem**, aby se tooltip s triggerem
  asocioval. Carbon dodává, že to pomáhá zvlášť, když je vedle sebe víc prvků blízko.
- Směry jsou defaultně **auto**: tooltip při otevření detekuje hrany prohlížeče, aby se umístil viditelně
  a kontejner nebyl odříznutý. Lze místo toho zvolit konkrétní směr: **right, left, bottom, top**.
- **Nezakrývej související obsah, který je pro úkol uživatele zásadní.** Tooltip **nesmí vytékat ze
  stránky ani za jiný obsah**.
- U **definition tooltipu** navíc: **nezakrývej slova vlevo a vpravo od triggerového slova**. Když je
  aktivní, musí překrývat jiný obsah a nesmí být odříznutý okolními komponentami ani vytékat ze stránky.

**ZDROJ:** Carbon, Tooltip usage, Alignment a Placement.
https://carbondesignsystem.com/components/tooltip/usage/

## Text tooltipu

- **Relevantní a konkrétní obsah.**
- **Nesmí obsahovat zásadní instrukce k úkolu**, protože tooltip není trvalý.
- Tooltipy u komponent s jen ikonou (ikonová tlačítka) mají dát **stručný jedno nebo dvouslovný popis
  funkce** tlačítka.
- U definic a instruktivních tooltipů použij **sentence case** a piš plné věty s interpunkcí, **pokud
  není prostor omezený**.

**ZDROJ:** Carbon, Tooltip usage, Content.
https://carbondesignsystem.com/components/tooltip/usage/

## Chování tooltipu

**Stavy:** dva, **on** (hover a focus) a **closed**. Defaultně je tooltip skrytý a neaktivní.

**Myš:** vyvolá se hoverem nad triggerem. Persistuje, dokud myš zůstává nad aktivním kontejnerem nebo
nad triggerem. Zavře se přehoverováním na jiný prvek.

**Definition tooltip může použít hover nebo klik**, podle situace: hover, když uživatel potřebuje rychlý
pohled na informaci. Klik, když potřebuje víc času, nebo když by se tooltip mohl vyvolávat nechtěně.

**Klávesnice:** `Tab` na trigger tooltip zobrazí. Zavírá `Esc`. U tooltipů, které odkrývají kontejnery
na focus, kontejner zmizí, když focus odejde.

**ZDROJ:** Carbon, Tooltip usage, Behaviors.
https://carbondesignsystem.com/components/tooltip/usage/

## Ikonové tlačítko: tooltip je povinný

**PRAVIDLO:** **Bez ohledu na to, jak rozpoznatelná ikona je**, a bez ohledu na to, jestli je akce
v seznamu univerzálních akcí, **tooltip s textem vysvětlujícím, co by tlačítko udělalo po kliknutí, je
vždy povinný**.
**KDY PLATÍ:** Každé ikonové tlačítko bez viditelného labelu.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Tooltips for icon only buttons, verbatim: „Regardless of how recognizable
an icon may or may not be, or whether that action lies within the universal actions list, a tooltip is
always required with text explaining what the icon button would do if clicked."
https://carbondesignsystem.com/components/button/usage/

**Návrhový důsledek:** Carbon vyžaduje, aby designér text tooltipu **napsal do návrhu**, s odůvodněním:
„If designers do not specify the text, developers are less likely to implement tooltips." Výjimku dává
jen ikonám se zavedeným názvem a funkcí (Bold, Italics).
Zdroj: https://carbondesignsystem.com/components/tooltip/accessibility/

## Toggletip

**Kdy použít:**

1. Když **musí být interaktivní prvek** uvnitř otevřeného toggletipu.
2. Pro **rychlou editaci v kontextu**.
3. Pro **filtrační panely**, které překrývají obsah.

**Kdy nepoužít:** **na kritickou informaci nebo na povinný vstup potřebný k dokončení flow.** Tam patří
**modal**.

**ZDROJ:** Carbon, Toggletip usage, When to use / When to not use.
https://carbondesignsystem.com/components/toggletip/usage/
Detail: [Dialogy a panely](../vzory/dialogy-a-panely.md)

**Anatomie:**

1. **UI trigger:** prvky, které toggletip vyvolají na klik nebo `Enter`.
2. **Caret tip:** vizuálně spojuje kontejner obsahu s triggerem a značí, odkud obsah pochází.
3. **Kontejner:** obsahuje text a interaktivní prvky.

**Rozměry:** kontejner má **maximální šířku 288 px**, výška se mění podle obsahu. Carbon doporučuje
**držet šířku do čtyř sloupců**.

**Umístění:** lze použít na různých částech UI, Carbon jmenuje hlavičky, datové tabulky, boční panely,
modaly a read-only karty. Když je aktivní, popover může být **top, bottom, left nebo right** vůči
triggeru.

**Přetečení:** protože toggletip používá flexibilní popover a disclosure pattern, **scrollování obvykle
není potřeba**. Když je (například v situaci podobné dropdownu), scrolluje **tělo**, hlavička a zápatí
zůstávají na místě, pokud existují. **Nescrolluj vodorovně a nenech obsah vytéct ze stránky.**

**Stavy:** dva, **open** (klik nebo `Enter`) a **closed**. Defaultně skrytý a neaktivní.

**Interakce myší:** vyvolá se klikem, zavře dalším klikem na trigger, nebo klikem kamkoliv mimo aktivní
popover či trigger.

**Klávesnice:** vyvolá `Enter` nebo `Space` na triggeru. Zavírá `Escape`. **Focus po vyvolání zůstává na
triggeru**, `Tab` vstoupí do interaktivních prvků uvnitř. Detail:
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md).

**ZDROJ:** Carbon, Toggletip usage a Toggletip accessibility.
https://carbondesignsystem.com/components/toggletip/usage/

## Toggletip v přístupném formuláři

Carbon toggletip explicitně jmenuje jako **řešení** běžného problému formulářů: jak vynést doplňkovou
informaci, aniž by byl formulář příliš hustý. Informační ikona jako toggletip zajistí, že je informace
**předvídatelná a dostupná klávesnicí**, protože toggletip je tlačítko a je v tab orderu (`Space`
i `Enter` otevírají, `Esc` zavírá).

**ZDROJ:** Carbon, Form accessibility, Information icons.
https://carbondesignsystem.com/components/form/accessibility/

## Související komponenty a jejich vztah

| Komponenta | Vztah |
|---|---|
| Popover | **Základová vrstva** pro tooltipy, overflow menu a dropdown menu |
| Disclosure | Vzor, který používá popover jako základ. Skládá se z kontejneru, textu a interaktivních prvků. **Interaktivní prvky zůstávají v tab orderu stránky** |
| Toggletip | Používá disclosure pattern k přepínání viditelnosti popoveru |
| Chart tooltip | Objevuje se, když je kurzor nad prvkem grafu (datový bod, ikonové tlačítko, zkrácený text). **Je to vestavěné chování grafových komponent** |

**ZDROJ:** Carbon, Tooltip usage, Related.
https://carbondesignsystem.com/components/tooltip/usage/

## Ikona „i" versus „?"

**PRAVIDLO:** Pro doplňkovou informaci používej ikonu **„i" (info)** s obtaženým tvarem, ne otazník.
**PROČ:** Carbon: „i" značí **doplňující, nikoliv zásadní** informaci.
**TŘÍDA:** B
**ZDROJ:** Carbon, Forms pattern, Tooltips, verbatim: „In Carbon, we use the 'i' icon instead of the '?'
icon because it indicates additional rather than essential information."
https://carbondesignsystem.com/patterns/forms-pattern/

**Praktický důsledek:** když u pole potřebuješ otazník („co to znamená?"), je to signál, že informace je
zásadní, a patří do helper textu, ne do tooltipu.

---

## Co tahle nota neřeší

- Rozhodnutí mezi helper textem, placeholderem a tooltipem u formulářového pole.
  [Textová pole](textova-pole.md).
- Popover a disclosure jako samostatné komponenty. Carbon je má, v přečtené kopii jejich stránky nejsou.
- Modal a dialogy. [Dialogy a panely](../vzory/dialogy-a-panely.md).
- Tooltipy v grafech a dataviz. Zatím jen [sheets](../../sheets/znalostni-baze.md).
- Tokeny a rozestupy. Carbon je má na stránce `style`, záměrně je nepřebírám.

## Zdroj

IBM Carbon Design System, Tooltip usage, Tooltip accessibility, Toggletip usage, Toggletip accessibility.
Lokální kopie přečtená 30. 7. 2026. https://carbondesignsystem.com/components/tooltip/usage/ ·
https://carbondesignsystem.com/components/toggletip/usage/
Carbon u tooltipu cituje Alita Joyce, Tooltip Guidelines (NN/g, 2019) a MDN, ARIA tooltip role (2023).
Třída **B**.
