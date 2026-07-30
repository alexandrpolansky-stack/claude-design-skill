# Textová pole: input, text area, password

Kdy které pole, jak volit mezi helper textem, placeholderem a tooltipem, a jak se pole chová
při přetečení.

**Nadřazený zdroj pro labely, placeholder a validaci** je
[Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md) (WCAG, GOV.UK, NN/g). Tahle nota
přidává Carbonovu typologii, velikosti, stavy a rozhodnutí mezi třemi druhy nápovědy.

Související: [Skladba formuláře](../vzory/formular-skladba.md) ·
[Výběr ze seznamu](vyber-ze-seznamu.md) · [Tooltip a toggletip](tooltip-a-toggletip.md)

---

## Rychlé rozhodnutí

1. Jeden řádek = **text input**. Víc než pár slov, může přetéct na víc řádků = **text area**.
2. Tajná hodnota = **password input**, vždy s možností odkrytí a s helper textem o požadavcích.
3. Hodnota jde z předdefinovaného výčtu = **nepoužívej textové pole**, dej selekční prvek.
4. Label je **povinný**. Bez viditelného labelu jen po konzultaci s přístupnostním expertem.
5. Nápověda: **potřebuje ji uživatel vždycky = helper text.** Formát nebo příklad = placeholder.
   Doplňkový kontext = tooltip. **Nikdy zásadní informaci do tooltipu.**
6. Šířka pole má odrážet očekávanou délku obsahu.
7. Když jsou pole vedle sebe a jedno má helper text a druhé ne, zarovnej **pole**, ne labely.
8. Text area má měnitelnou výšku úchytem, ale šířku uživatel měnit nemůže.
9. Počítadlo znaků nebo slov: po dosažení limitu **zabraň dalšímu zadání a dej o tom vědět**.

---

## Dvě varianty

| Varianta | Kdy |
|---|---|
| Text input | Očekávaný vstup je **jeden řádek** textu. Fixní výška, jednoduché volné zadání, jakákoliv kombinace písmen, čísel a symbolů |
| Text area | Očekávaný vstup je **víc než pár slov** a může se rozprostřít na víc řádků. Typicky komentáře uživatele nebo popisy |

**Text area podporuje všechny stejné stavy a funkce jako text input, kromě funkce hesla.** Naopak má
funkce, které text input nemá: **úchyt na zvětšení, počítadlo slov a počítadlo znaků**.

**ZDROJ:** Carbon, Text input usage, Variants a Text area.
https://carbondesignsystem.com/components/text-input/usage/

## Kdy textové pole nepoužít

**PRAVIDLO:** Když uživatel může zadat jen volbu z předdefinovaného seznamu, **vyhni se volnému
textovému vstupu**, protože pravděpodobně povede k chybě. Použij selekční prvek: dropdown, select nebo
skupinu radio buttonů.
**KDY PLATÍ:** Vždy, když je množina platných hodnot známá.
**TŘÍDA:** B
**ZDROJ:** Carbon, Text input usage, When not to use, verbatim: „If a user can only enter an option
from a predefined list then avoid using a free-form text input as it is likely to result in an error."
https://carbondesignsystem.com/components/text-input/usage/

**Kdy naopak textové pole ano:** když uživatel zadává unikátní informaci, kterou nelze předvídat sadou
voleb. Nebo když zadává zapamatovatelná data, která jdou rychleji zadat volným způsobem než složitějším
ovládacím prvkem.

## Tři druhy vstupu ve formuláři podle délky obsahu

| Prvek | Na co | Carbonovy příklady |
|---|---|---|
| Text input | Zachytit maximálně několik slov | Jména, telefonní čísla, adresy |
| Password input | Sběr privátních dat skrytím znaků | Hesla, čísla sociálního pojištění, PINy, údaje z platební karty |
| Text area | Zachytit víc řádků textu | Zpětná vazba, žádosti o podporu |

**ZDROJ:** Carbon, Forms pattern, Text inputs.
https://carbondesignsystem.com/patterns/forms-pattern/

## Anatomie

**Text input:**

1. **Label:** informuje o obsahu, který má uživatel zadat. **Je povinný**, pokud nemáš schválenou
   přístupnostní výjimku.
2. **Value:** obsah, který uživatel zadal.
3. **Field:** kontejner, do kterého uživatel zadává. **Musí splnit požadavek 3:1 na non-text kontrast.**
4. **Helper text** (volitelný): asistenční text s další pomocí nebo kontextem. Často se používá na
   vysvětlení správného formátu dat. V default stylu je pod polem, ve fluid stylu se podává tooltipem.

**Text area má navíc:** úchyt na zvětšení, indikátor volitelnosti nebo povinnosti a volitelné
počítadlo (znaků nebo slov).

**ZDROJ:** Carbon, Text input usage, Anatomy.
https://carbondesignsystem.com/components/text-input/usage/

**Poznámka ke kontrastu pole:** požadavek 3:1 na okraj pole má knihovna s WCAG oporou (SC 1.4.11
Non-text Contrast, AA) plus s naměřeným nákladem bezokrajového UI (NN/g, Moran 2017: +22 % času).
Viz [formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md) a
[anti-slop](../../ux-design/pravidla/anti-slop.md).

## Velikosti

Tři výšky, stejná škála jako ostatní vstupy:

| Velikost | Výška | Kdy |
|---|---|---|
| Small | 32 px | Stísněný prostor, nebo pole v dlouhém a složitém formuláři |
| Medium | 40 px | **Výchozí a nejčastější. Když nevíš, použij tuhle** |
| Large | 48 px | Když je hodně prostoru. Typicky jednoduché formuláře, nebo když je pole na stránce samo |

**Konzistence:** používej jednotnou výšku pole, když na stejné stránce páruješ formulářové komponenty.

**Fluid varianta:** jedna výška, vizuálně větší než default. Je to nastavená výška, **kromě situace,
kdy se dole přidá varovná nebo chybová hláška**.

**Text area:** proměnná výška, uživatel ji mění úchytem. **Defaultně minimální výška 40 px, maximum
žádné.** Úchyt **neovlivňuje šířku**, jen výšku. Když uživatel zkrátí pole pod výšku obsahu, objeví se
svislý scroll.

**ZDROJ:** Carbon, Text input usage, Sizing a Resize handle.
https://carbondesignsystem.com/components/text-input/usage/

## Šířka a zarovnání

**PRAVIDLO:** Šířka pole u text inputu i text area má **odrážet zamýšlenou délku obsahu**, a přitom se
zarovnat na sloupce mřížky nebo na mini unit mřížku. Minimum ani maximum šířky není, ale **vyhni se
nadměrně širokým polím, která jsou disproporční k zamýšleným datům**.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Text input usage, Placement, verbatim: „you should avoid excessively wide fields
that are disproportionate to the intended data being collected."
https://carbondesignsystem.com/components/text-input/usage/
**Souvislost:** knihovna má tohle pravidlo zdrojované z GOV.UK jako afordanci („šířka nese informaci
o délce obsahu") a s výjimkou pro mobilní layouty pod 320 px, kde má přednost WCAG 1.4.10 Reflow. Viz
[formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).

**Zarovnání:** labely a kontejnery polí se mají svisle zarovnat na mřížku a s ostatními formulářovými
komponentami. **Default vstupy sedí zarovnané na sloupce, fluid vstupy zasahují do mezer.**

**Pravidlo pro nestejná pole vedle sebe:** když jsou pole vedle sebe a jedno má helper text a druhé ne,
**zarovnej vždycky pole (input fields), ne labely**.
**ZDROJ:** Carbon, Forms pattern, Helper text, verbatim: „When fields appear side-by-side and one input
has helper text while the other one doesn't; always top align the input fields, not the labels."
https://carbondesignsystem.com/patterns/forms-pattern/

## Nápověda: helper text versus placeholder versus tooltip

Tohle je nejpraktičtější rozhodnutí celé noty. Carbonovo kritérium je **kdy informace zmizí**.

| Prvek | Kdy je vidět | Na co |
|---|---|---|
| **Helper text** | **Vždycky, i když je pole ve focusu** | **Need-to-know informace.** Proto je to správná volba pro cokoliv, co uživatel potřebuje vědět, typicky správný formát dat |
| **Placeholder** | Zmizí, jak uživatel začne psát | Nápověda nebo příklad formátu (`YYYY-MM-DD`). **Nesmí obsahovat zásadní informaci** |
| **Tooltip** | Jen na hover nebo focus triggeru | Nice-to-have kontext nebo pozadí. **Nikdy zásadní informaci** |

**ZDROJ:** Carbon, Forms pattern, Offering help, verbatim: „Helper text is always available, even when
the field is focused, that's why it's the correct choice for need-to-know information. For context or
background information that is 'nice to have', use placeholder text or a tooltip."
https://carbondesignsystem.com/patterns/forms-pattern/

### Helper text

**Do:** ber ho jako zásadní informaci, která je sekundární k labelu. Drž ho **tak krátký a konkrétní,
jak to jde**. Používej ho **jen když je opravdu potřeba**, ať uživatele nepřehltíš.

**Don't:** **nikdy** nepoužívej helper text místo labelu pole. **Nemá být delší než vstupní oblast.**

**Formát:** sentence case, ve většině případů plné věty s interpunkcí. Objeví se trvale pod polem,
**kromě chvíle, kdy ho nahradí chybová nebo varovná hláška**.

**ZDROJ:** Carbon, Forms pattern, Helper text a Text input usage, Content.
https://carbondesignsystem.com/patterns/forms-pattern/

### Placeholder

**Do:** drž nápovědu **tak krátkou, jak to jde**, a nikdy nepřetékej pole. **Řádně anonymizuj
příklady**, nepoužívej reálné hodnoty.

**Don't:** nepoužívej placeholder na komplexní a dlouhé požadavky (například požadavky na heslo), na to
použij infotip. Nedávej placeholder, když není potřeba. **Nikdy ho nepoužívej jako náhradu labelu.**

**Formát:** sentence case, ve většině případů přímé tvrzení **bez interpunkce**. Placeholder **není
povinný a defaultně se v Carbonu v textových polích nezobrazuje**.

**Carbonovo vlastní varování:** „Placeholder text can be harmful to user interactions and should only
be added when necessary."

**ZDROJ:** Carbon, Text input usage, Placeholder text a Forms pattern, Placeholder text.
https://carbondesignsystem.com/components/text-input/usage/
**Pozor, knihovna je přísnější:** [formuláře a
stavy](../../ux-design/pravidla/formulare-a-stavy.md) placeholder **zakazuje úplně**, i na hinty
a příklady, se třemi nezávislými důvody (zmizí při psaní, čtečky ho nečtou spolehlivě, defaultní styl
prohlížeče typicky nesplňuje WCAG 1.4.3). **Platí knihovna.** Carbonova pozice je mírnější a jeho
vlastní varování jde stejným směrem.

### Tooltip

**Do:** používej tooltipy s obtaženou ikonou „i" (info). Používej je na vysvětlující nebo doplňující
informaci. Tooltip je **microcontent, drž ho stručný**.

**Don't:** tooltip **není odkladiště obsahu, který se nikam nevejde**, musí se používat záměrně a velmi
střídmě. **Nikdy do tooltipu neumísťuj zásadní informaci.**

**Proč „i" a ne „?":** Carbon používá ikonu „i" místo „?", protože značí **doplňující, nikoliv zásadní**
informaci.

**Carbonův argument s odkazem na výzkum:** tooltipy mohou být užitečné pro dodatečné vysvětlení
uživatelům, kteří konkrétní pole neznají, a mohou dát odůvodnění pro to, co může vypadat jako neobvyklý
požadavek. **Ale výzkum naznačuje, že uživatel by neměl muset hledat tooltip, aby se dostal
k informaci, která je zásadní pro dokončení jeho úkolu.**

**Chování:** tooltip se objeví na hover (desktop) a na klik (tablet a mobil).

**ZDROJ:** Carbon, Forms pattern, Tooltips, s odkazem na Alita Joyce, Tooltip Guidelines (NN/g, 2019).
https://www.nngroup.com/articles/tooltip-guidelines/
https://carbondesignsystem.com/patterns/forms-pattern/
Detail rozdílu tooltip versus toggletip: [Tooltip a toggletip](tooltip-a-toggletip.md).

**Výjimka u fluid vstupů:** fluid vstupy nemají pod polem místo na helper text, takže **veškerá
asistenční informace, i ta zásadní, jde do tooltipu**. Carbon to označuje za výjimku z pravidla.
Detail: [Skladba formuláře](../vzory/formular-skladba.md).

## Labely

- Textové pole **má vždycky mít label**. Existují vzácné případy, kdy kontext vstupu potřebu
  viditelného labelu popírá, ale **Carbon radí konzultovat návrh bez labelu s přístupnostním expertem**.
- Sentence case, kromě názvů produktů a vlastních jmen.
- **Krátce a stručně.**
- **Bez dvojtečky** na konci.

**ZDROJ:** Carbon, Text input usage, Labels.
https://carbondesignsystem.com/components/text-input/usage/
Detail včetně WCAG opory: [formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).

## Stavy

Text input a text area mají: **enabled, active, focus, error, warning, disabled, skeleton, read-only**.

| Stav | Kdy |
|---|---|
| Enabled | Pole je aktivní, ale uživatel s ním přímo neinteraguje. Může být prázdné, s placeholderem, nebo s obsahem od uživatele |
| Active | Uživatel právě aktivně píše |
| Focus | Uživatel na pole tabnul nebo kliknul |
| Error | Vstup je neplatný, nebo povinné pole není vyplněné. Nebo systémová chyba. **Vyžaduje reakci uživatele, než se data odešlou nebo uloží** |
| Warning | Potřebuješ upozornit na výjimečnou podmínku. Nemusí to být chyba, ale může způsobit problémy, když se nevyřeší |
| Disabled | Všechny interaktivní funkce odebrané. **Není fokusovatelný, nečte ho čtečka, nemusí splňovat kontrast** |
| Skeleton | Při prvním načtení stránky |
| Read-only | Uživatel může prohlížet, ale neupravovat. **Zůstává fokusovatelný, dostupný čtečce a splňuje kontrast** |

**ZDROJ:** Carbon, Text input usage, States, tabulka.
https://carbondesignsystem.com/components/text-input/usage/
Detail volby mezi disabled a read-only:
[Disabled versus read-only](../vzory/disabled-vs-read-only.md).

## Chybový stav má tři indikátory

**PRAVIDLO:** Chybový stav má **tři** vizuální indikátory: červený okraj, ikonu chyby a chybovou hlášku.
**KDY PLATÍ:** Každá chyba pole.
**PROČ:** Barva sama nestačí (barvocit), takže ikona plus text jsou povinné.
**TŘÍDA:** B pro Carbonovu formulaci, A pro princip (WCAG 1.4.1 Use of Color).
**ZDROJ:** Carbon, Text input usage, Invalid, verbatim: „Error states have three visual indicators to
signify invalid content: a red border, an error icon indicator, and an error message."
https://carbondesignsystem.com/components/text-input/usage/
Detail textu hlášky a kdy validovat: [formuláře a
stavy](../../ux-design/pravidla/formulare-a-stavy.md).

## Přetečení

| Varianta | Chování |
|---|---|
| Text input | Když je obsah nečekaně příliš dlouhý na jeden řádek, hodnota se **vodorovně scrolluje** uvnitř pole při pohybu kurzoru z jednoho konce na druhý |
| Text area | Uživatel pole buď rozšíří úchytem, nebo obsah **svisle scrolluje** v nastavené výšce |

**ZDROJ:** Carbon, Text input usage, Overflow content.
https://carbondesignsystem.com/components/text-input/usage/
**Doplněk z Forms pattern:** „Truncate when an input is too long to be fully displayed in the field."
To se vztahuje na zobrazení hodnoty, ne na možnost zadání. Detail:
[Přetečení a truncation](../vzory/preteceni-a-truncation.md).

## Password input

- Podvarianta text inputu na sběr privátních dat, znaky skrývá.
- Uživatel může viditelnost znaků **přepnout ikonou oka** vpravo v poli.
- **Vždycky dodej detailní helper text s požadavky na formát dat**, například povolené typy znaků nebo
  strukturu.
- Přepnutí viditelnosti musí být obsluhovatelné klávesnicí (`Enter` nebo `Space`).

**ZDROJ:** Carbon, Text input usage, Password input a Text input accessibility.
https://carbondesignsystem.com/components/text-input/usage/

## Počítadlo znaků a slov

**PRAVIDLO:** Do text area lze přidat počítadlo znaků nebo slov, které zobrazí zadaný počet i celkový
povolený počet. **Po dosažení maxima musí text area zabránit dalšímu zadání a dát uživateli zprávu, že
byl limit dosažen.**
**KDY PLATÍ:** Kdykoliv počítadlo použiješ.
**TŘÍDA:** B
**ZDROJ:** Carbon, Text input usage, Character counter a Word counter, verbatim: „Once the max number of
characters is reached the text area should prevent the user from entering any additional character and
provide messaging to the user that a limit has been met."
https://carbondesignsystem.com/components/text-input/usage/
**Souvislost:** knihovna počítadlo znaků a měřič síly hesla jmenuje jako legitimní výjimku z pravidla
„nevaliduj během prvního psaní", protože to není chyba, ale průběžná informace, a není červené. Viz
[formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).

## Chování při focusu (detail, který se opomíná)

- V **text inputu** se existující text na focus **označí a přepíše se**, jak uživatel začne psát.
- V **text area** se existující text **neoznačí**, kurzor se dá na začátek nebo na místo poslední
  interakce uživatele.

**ZDROJ:** Carbon, Text input accessibility, Keyboard interaction.
https://carbondesignsystem.com/components/text-input/accessibility/

**Praktický důsledek:** u text inputu s předplněnou hodnotou uživatel jedním stiskem klávesy smaže celou
hodnotu. Když je předplněná hodnota drahá na znovuzadání, počítej s tím.

## Default versus fluid styl

| Styl | Vzhled | Kdy |
|---|---|---|
| Default | Label a helper text **vně pole**. Nejběžnější | Když je potřeba bílý prostor mezi vstupy, nebo v produktivních momentech, kde je prostor drahý a jsou potřeba menší komponenty |
| Fluid | Label **uvnitř** pole. Vizuálně větší | V expresivních momentech, fluidních formulářích, uzavřených prostorech, nebo připojené na složitou komponentu jako toolbar. **Fluid komponenty vždy sedí zároveň s okolními** |

**ZDROJ:** Carbon, Text input usage, Text input, tabulka stylů.
https://carbondesignsystem.com/components/text-input/usage/

## Předplňování

**PRAVIDLO:** **Předplňuj známé hodnoty, když to jde**, například defaultní IP adresu. Kde to jde, přidej
programovou asistenci: detekuj a předplň vstupy, ať snížíš chyby a ušetříš čas. Když software hodnotu
určit neumí, použij **type-ahead** a nabídni návrhy. Sentence case u výchozích hodnot, detekovaných
hodnot a autocomplete textu.
**KDY PLATÍ:** Vždy, když hodnotu můžeš znát.
**TŘÍDA:** B
**ZDROJ:** Carbon, Forms pattern, Text inputs, Best practices a Form usage, Default values.
https://carbondesignsystem.com/components/form/usage/
**Souvislost:** knihovna má na tohle tvrdší pravidlo s WCAG oporou: atribut `autocomplete` s hodnotou
z HTML specifikace na každém poli, které se ptá na údaj o uživateli (WCAG 1.3.5 Identify Input Purpose,
AA). Viz [formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).

**A pravidlo pro mobil:** Carbon velí zajistit, aby uživatelé mohli zadat informaci i na menších
velikostech obrazovky.

---

## Co tahle nota neřeší

- Labely, placeholder a validaci s WCAG a GOV.UK oporou.
  [Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md). **Nadřazený zdroj.**
- Rozvržení formuláře, mezery a polohu tlačítek.
  [Skladba formuláře](../vzory/formular-skladba.md).
- Selekční prvky a bound entry controls. [Výběr ze seznamu](vyber-ze-seznamu.md).
- Number input, date picker, slider, file uploader. Carbon je má, ale v přečtené kopii jejich stránky
  nejsou.
- Typografii a délku řádku. [Typografie](../../ux-design/pravidla/typografie.md).

## Zdroj

IBM Carbon Design System, Text input usage, Text input accessibility, doplněno sekcemi z Forms pattern
a Form usage. Lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/components/text-input/usage/
Carbon u text inputu neuvádí sekci References. Odkaz na NN/g Tooltip Guidelines je z Forms pattern.
Třída **B**. Kde si Carbon odporuje s knihovnou (placeholder, autocomplete), platí knihovna.
