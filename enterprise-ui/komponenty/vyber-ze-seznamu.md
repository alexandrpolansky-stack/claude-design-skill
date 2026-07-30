# Výběr ze seznamu: select, dropdown, combo box, multiselect

Čtyři komponenty, které vypadají skoro stejně a chovají se různě. Kdy kterou a proč.

Související: [Volba komponenty](../zaklady/volba-komponenty.md) ·
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md) · [Skladba formuláře](../vzory/formular-skladba.md) ·
[Filtrování](../vzory/filtrovani.md)

---

## Rychlé rozhodnutí

1. **Dvě** možnosti = radio buttony. Nikdy dropdown.
2. **Pod tři** možnosti = radio buttony. Nikdy select.
3. **Nad pět** možností = seznamová komponenta, ne checkboxy ani radia.
4. Formulář odesílající data, hlavně na mobilu = **nativní select**.
5. Filtrování nebo řazení obsahu na stránce, nebo potřeba víc voleb = **dropdown**.
6. Dlouhý nebo nepředdefinovaný seznam, uživatel může zadat vlastní hodnotu = **combo box**.
7. Víc voleb z dlouhého seznamu = **multiselect**, případně filterable.
8. **Nikdy nevnořuj dropdowny.**
9. Label je vždy povinný. Placeholder ho nenahrazuje.
10. Volby řaď **abecedně**, pokud nemáš důvod jinak.
11. Jedna velikost vstupů na celou obrazovku.

---

## Rozhodovací tabulka

| Komponenta | Kolik vybere | Píše uživatel | Kdo určuje vzhled | Typické použití |
|---|---|---|---|---|
| Nativní select | Jednu | Ne | **Prohlížeč** | Formulář odesílající data |
| Dropdown | Jednu | Ne | Design systém | Filtrování, řazení, akce |
| Multiselect | Víc | Ne (filterable varianta ano) | Design systém | Filtrování podle víc kritérií |
| Combo box | Jednu, **nebo zadá vlastní** | Ano, filtruje | Design systém | Dlouhý nebo nepředdefinovaný seznam z databáze |

## Select versus dropdown: čtyři rozdíly

Carbon je jmenuje explicitně:

1. **Kód a vzhled:** dropdown je stylovaný, aby odpovídal design systému. **Vzhled selectu určuje
   prohlížeč.**
2. **Účel:** dropdown použij ve formulářích, na výběr víc možností naráz a na filtrování nebo řazení
   obsahu na stránce. **Select nemá filtrování ani multiselect.**
3. **Formulář:** select použij, když je zkušenost převážně formulářová. Vlastní dropdowny tam použít
   lze, ale **nativní select pracuje snadněji s nativním formulářem při odesílání dat**.
4. **Mobil:** select použij, když se zkušenost bude často používat na mobilu. **Nativní select používá
   nativní ovládání platformy, což ho dělá snadnějším na použití.**

**ZDROJ:** Carbon, Dropdown usage, Dropdown versus Select a Select usage, Select versus Dropdown.
https://carbondesignsystem.com/components/dropdown/usage/ ·
https://carbondesignsystem.com/components/select/usage/

**Carbonovo souhrnné rozlišení:** „A select presents a list of options from which the users can select
only one item from that list. It works best in forms when users choose an option from the select list
and submit data." versus „A dropdown presents a list of options that users can select one or several
options from that list. Dropdown options are used for taking an action, filtering, or sorting existing
content."

## Dropdown versus combo box

- U **dropdownu** je vybraná volba vždy viditelná a ostatní volby se zobrazí kliknutím a otevřením
  seznamu.
- **Combo box** je kombinace standardního list boxu nebo dropdownu, která **nechá uživatele psát do
  pole**, aby našel volbu odpovídající zadané hodnotě.

**Kdy combo box:** když uživatel potřebuje vybrat jednu volbu, ale **seznam může být velmi dlouhý nebo
nepředdefinovaný**. Combo box dovolí vybrat z navržených voleb, **nebo zadat vlastní hodnotu**. Carbon
dodává, že je užitečný, když data pro seznam přicházejí z databáze.

**ZDROJ:** Carbon, Dropdown usage, Combo box a Dropdown versus Combo box.
https://carbondesignsystem.com/components/dropdown/usage/

## Kdy dropdown nepoužít

Carbon jmenuje tři situace:

1. **Málo možností.** Když jsou dvě možnosti na výběr, použij skupinu **radio buttonů**.
2. **Vnořování.** **Nevnořuj dropdowny** ani jimi nezobrazuj příliš složitou informaci. Drž výběr voleb
   tak přímý, jak to jde.
3. **Formulářová nebo mobilní platforma.** Zvaž select, když je zkušenost převážně formulářová nebo se
   často používá na mobilu.

**ZDROJ:** Carbon, Dropdown usage, When not to use.
https://carbondesignsystem.com/components/dropdown/usage/

**A u selectu:** nepoužívej, když je **méně než tři** možnosti. Tam skupina radio buttonů.
Zdroj: https://carbondesignsystem.com/components/select/usage/

## Anatomie

**Dropdown má šest částí:**

1. **Label:** text, který uživateli řekne, co může v seznamu voleb očekávat.
2. **Helper text:** asistenční text, který mu pomůže vybrat správně.
3. **Field:** persistuje otevřený i zavřený.
4. **Menu:** seznam voleb, zobrazený v otevřeném stavu.
5. **Option:** volba pro uživatele.
6. **Parent checkbox:** u multiselectu, pro výběr všech voleb v menu.

**Select má navíc:** výchozí prázdnou volbu (vybranou defaultně, lze změnit na předvyplněnou první
volbu v abecedním pořadí, nebo na častou či běžně používanou volbu ze seznamu), stavovou ikonu
(error nebo warning) a chybový či varovný text, který **nahrazuje** helper text, když ten stav nastane.

**ZDROJ:** Carbon, Dropdown usage a Select usage, Anatomy.
https://carbondesignsystem.com/components/dropdown/usage/

## Velikosti

Tři výšky, stejná škála jako u ostatních vstupů (třída **B**, Carbonova volba):

| Velikost | Výška | Kdy |
|---|---|---|
| Small | 32 px | Když je prostor stísněný, nebo když je dropdown v dlouhém a složitém formuláři |
| Medium | 40 px | **Výchozí a nejčastěji používaná.** Když nevíš, použij tuhle |
| Large | 48 px | Když je hodně prostoru. Typicky v jednoduchých formulářích, nebo když je dropdown na stránce sám, například jako filtr |

**PRAVIDLO:** Použij **konzistentní velikost pro všechny formulářové komponenty na stejné stránce**.
Když používáš medium dropdown, používej stejnou velikost i pro textové vstupy, tlačítka a tak dál.
**KDY PLATÍ:** Každá formulářová obrazovka.
**TŘÍDA:** B
**ZDROJ:** Carbon, Dropdown usage, Sizing, verbatim: „use a consistent size for all form components on
the same page." https://carbondesignsystem.com/components/dropdown/usage/

**Otevřené menu:** každá volba v menu má být **stejně vysoká jako pole**.

**Fluid varianta:** jedna výška pole (64 px), ale **dvě velikosti položek menu**: default (64 px, když
je voleb málo, v expresivních momentech) a condensed (40 px, když je voleb hodně, aby se jich vidělo
víc bez scrollování).

**Šířka:** minimum ani maximum není, šířku si přizpůsob kontextu.

## Chování při otevření

| Aspekt | Pravidlo |
|---|---|
| Směr | Dropdown se může otevřít nahoru nebo dolů podle pozice na obrazovce. Když je u spodní hrany rozhraní, rozbalí se nahoru, aby nebyl odříznutý. **Defaultně se otevírá dolů** |
| Elevace | Otevřené menu má stín, aby působilo výš než obsah za ním. Stejný mechanismus jako u overflow menu a kalendáře date pickeru |
| Scrollování | Scrollbary nemusí být vždy zapnuté, takže Carbon doporučuje **zobrazit 50 % výšky kontejneru poslední volby**, aby bylo vidět, že v menu je víc obsahu. Scroll doporučuje začít **u šesté volby** v seznamu, ale to se může podle případu lišit |

**ZDROJ:** Carbon, Dropdown usage, Universal behaviors.
https://carbondesignsystem.com/components/dropdown/usage/
**Poznámka k elevaci:** konkrétní hodnotu stínu Carbon uvádí, ale nepřebírám ji, je to token. Kdy nést
hloubku barvou plochy a kdy stínem řeší
[hloubka a stíny](../../ux-design/pravidla/hloubka-a-stiny.md), a je tam i zaznamenaný spor
Carbon versus Comeau o konstantní opacitě stínu.

## Obsah

| Prvek | Pravidlo |
|---|---|
| Label | Řekne uživateli, co v seznamu očekávat. **Krátký, na jednu řádku.** **Neodstraňuj label ve prospěch placeholderu.** Labely jsou vždy silně doporučené |
| Helper text | Podstatná informace, která pomůže vybrat správně. **Je dostupná vždy, i když je pole ve focusu**, a je pod labelem |
| Placeholder v poli | Volitelný, když ještě nic není vybrané. **Nedávej do něj důležitou informaci**, zmizí po výběru. Důležitou informaci nech pro label nebo helper text, které zůstanou vidět. Carbonův typický příklad placeholderu: „Choose an option" |
| Text volby | **Krátký, přesný, ne popisný.** **Nikdy nepoužívej dekorativní obrázky ani ikony** uvnitř dropdownu. Carbon doporučuje **abecední pořadí** |
| Parent checkbox | Protože je parent checkbox jednou z voleb, **neformuluj ho jako akci.** Použij slovo „All". Případně přidej druhé popisné slovo, například „All roles" |

**Pořadí seznamu u selectu:** kde to jde, abecedně, nebo vzestupně relativně k obsahu. Jinak podle
**frekvence použití**.

**Přetečení:** vyhýbej se víc řádkům textu v dropdownu. Když se text nevejde na řádek, přidej výpustku
a **tooltip s celým textem**, přednostně Carbonový tooltip kvůli klávesové přístupnosti.

**ZDROJ:** Carbon, Dropdown usage, Content a Select usage, Content.
https://carbondesignsystem.com/components/dropdown/usage/ ·
https://carbondesignsystem.com/components/select/usage/
**Souvislost:** k placeholderu má knihovna **přísnější** pravidlo, zakazuje ho i na hinty a příklady,
s WCAG a GOV.UK oporou. Viz [formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md). Tam,
kde si Carbon a knihovna odporují, platí knihovna.

## Multiselect

**Kdy:** uživatel potřebuje vybrat víc voleb z předdefinovaného seznamu. Dobrá volba, když potřebuje
filtrovat nebo řadit obsah na stránce podle víc kritérií. U každé volby je checkbox.

**Chování výběru:**

- Defaultně je v zavřeném poli placeholder. Aktivací se otevře menu.
- Každá volba má checkbox **vlevo od textu**.
- **Menu zůstane otevřené**, dokud se vybírá. Zavře se kliknutím na pole, kliknutím mimo, `Esc`, nebo
  odtabováním z komponenty.

**Zpětná vazba:**

- Po výběru se **vlevo od textu v poli objeví tag s celkovým počtem** vybraných voleb a s možností
  všechny zrušit.
- Placeholder se může změnit na text, který lépe odráží vybrané.
- **Vybrané volby se při dalším otevření přesunou nahoru** v menu, v alfanumerickém pořadí.
- Na rozdíl od dropdownu a combo boxu se menu po výběru **nezavírá**.

**Parent checkbox („vybrat vše"):**

- Má **třetí, indeterminate stav**, který se objeví, když je vybraných některých, ale ne všech.
- Kliknutí na indeterminate stav **zruší všechny** volby.
- Kliknutí na nezaškrtnutý checkbox **vybere všechny**.
- Kliknutí na zaškrtnutý **zruší všechny**.
- **Není povinný** v každém multiselectu.
- **Carbon doporučuje ho nepoužívat ve scénářích jako filtry, kde „vybrat vše" a „nevybrat nic"
  znamená totéž.**

**Filterable multiselect:** uživatel píše a seznam se zužuje. Volby, které začínají odpovídat zadání,
zůstanou, ostatní se dočasně odeberou. Po napsání textu se vpravo v poli objeví křížek, který **vymaže
zadaný text** (ne vybrané volby).

**Zrušení všech vybraných:** hover na filtrovatelný tag a klik na křížek u hodnoty. Carbon k tomu
dodává, že se na hover nad křížkem má objevit tooltip prohlížeče, aby bylo jasné, co klik udělá. Když
chceš odvybrat jednotlivé volby, odškrtneš je v seznamu.

**ZDROJ:** Carbon, Dropdown usage, Multiselect.
https://carbondesignsystem.com/components/dropdown/usage/

## Combo box

- Menu se otevře kliknutím kamkoliv do pole, uživatel může psát a probírat se seznamem. **Nejlépe
  odpovídající volba se při psaní zvýrazní.**
- Křížek vymaže vstup, autocomplete zužuje volby při psaní.
- Výběr volby menu zavře a vybraná volba nahradí placeholder.

**Zadání vlastní hodnoty:**

- Když požadovaná volba v seznamu není, uživatel může začít psát vlastní hodnotu přímo do pole, což
  zároveň odfiltruje volby.
- Novou vlastní hodnotu uloží kliknutím mimo pole, nebo `Tab` nebo `Enter`.
- Po uložení se placeholder změní na napsanou vlastní hodnotu.

**ZDROJ:** Carbon, Dropdown usage, Combo box.
https://carbondesignsystem.com/components/dropdown/usage/

**Pozor na klávesovou pastí:** v combo boxu **`Space` nevybírá**, protože vloží mezeru do filtrovaného
textu. Detail celé klávesové mechaniky všech čtyř variant:
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md).

## Inline modifikátor

**PRAVIDLO:** Když dáváš dropdown inline s jiným obsahem, použij inline modifikátor. Vizuální label
u inline dropdownu patří **inline vlevo** od dropdownu. **Když viditelný label není, musíš dodat
přístupnostní label.** Inline je modifikátor **jen pro dropdown a multiselect** a **nezahrnuje
filtrování**.
**TŘÍDA:** B
**ZDROJ:** Carbon, Dropdown usage, Modifiers, Inline.
https://carbondesignsystem.com/components/dropdown/usage/

**Inline select** je borderless, má menší vizuální váhu a Carbon ho doporučuje, když máš ve formuláři
víc select polí.

## Stavy

Dropdown, combo box i multiselect mají stavy: **enabled, hover, focus, error, warning, disabled,
skeleton, read-only**, a to jak pro pole, tak pro menu.

Select má navíc **selected** a **open**. Co který stav znamená:

| Stav | Kdy |
|---|---|
| Enabled | Komponenta je aktivní a uživatel s ní přímo neinteraguje. Výchozí stav. **Aktivní select má obsahovat výchozí hodnotu** |
| Hover | Kurzor je nad polem |
| Selected | Uživatel otevřel seznam a vybral volbu |
| Focus | Uživatel na pole tabnul nebo kliknul |
| Open | Uživatel otevřel seznam |
| Error | Pole označené jako povinné nemá vybranou volbu. Nebo systémová chyba. **Vyžaduje reakci uživatele, než se data odešlou nebo uloží** |
| Warning | Potřebuješ upozornit na výjimečnou podmínku. Nemusí to být chyba, ale může způsobit problém, když se nevyřeší |
| Disabled | Uživatel nemůže interagovat, všechny interaktivní funkce odebrané. **Není fokusovatelný, nečte ho čtečka a nemusí splňovat kontrast**, takže je nepřístupný, když je potřeba ho interpretovat |
| Skeleton | Při prvním načtení, komponenta ještě není načtená |
| Read-only | Uživatel může prohlížet, ale neupravovat. Odebere interaktivní funkce jako disabled, **ale zůstává fokusovatelný, dostupný čtečce a splňuje kontrast pro čitelnost** |

**ZDROJ:** Carbon, Select usage, States, tabulka.
https://carbondesignsystem.com/components/select/usage/
Detail volby mezi disabled a read-only: [Disabled versus read-only](../vzory/disabled-vs-read-only.md).

## Svislé oddělovače v poli

**PRAVIDLO:** Svislé oddělovače fungují jako vizuální separátor **mezi interaktivními prvky** v poli.
Jsou přítomné **jen mezi dvěma interaktivními prvky**. **Nezavádět je** mezi neinteraktivní prvky,
jako jsou chybové stavy, jiné neinteraktivní ikony nebo tlačítka. Oddělovač je taky vlevo od
nejlevější sady interaktivních položek, i když je vedle neinteraktivní položky.
**TŘÍDA:** B
**ZDROJ:** Carbon, Dropdown usage, Vertical dividers in input fields.
https://carbondesignsystem.com/components/dropdown/usage/

## Checkbox a radio button: čtyři pravidla

Doplněk, protože jsou to alternativy pro málo možností.

1. **Checkbox je pro víc voleb, ne pro vzájemně se vylučující volbu.** Každý checkbox funguje nezávisle
   na ostatních, zaškrtnutí dalšího neovlivní jiné výběry. Když uživatel může vybrat jen jednu volbu,
   patří tam radio buttony.
2. **Text vpravo od ovládacího prvku, skupiny svisle.** Když to jde, skládej skupiny checkboxů a radio
   buttonů **svisle** kvůli lepší skenovatelnosti.
3. **Vnořování:** parent checkbox vybere všechny potomky, odškrtnutí parenta všechny odškrtne.
   Zaškrtnutí potomka, když aspoň jeden další potomek není vybraný, přepne parenta do **indeterminate**
   stavu. Odškrtnutí potomka, když všichni ostatní zůstávají vybraní, přepne parenta ze zaškrtnutého do
   indeterminate.
4. **Label:** vždy jasný a stručný, doporučeně **pod tři slova**. Label musí existovat v kódu vždy,
   i když není v rozhraní vidět. **Nezkracuj ho výpustkou**, radši přeformuluj, a dlouhý label ať se
   zalomí pod checkbox, aby byl prvek s labelem zarovnaný nahoře.

**Skupinový label:** ve většině případů má sada checkboxů skupinový label. Může uvádět kategorii
seskupení, nebo popisovat, jaké akce se mají níž provést. Sentence case. Když je skupina checkboxů
uvnitř větší skupiny komponent, která už skupinový label má, další už není potřeba.

**Umístění ve formuláři:** Carbon doporučuje checkboxy dát aspoň **32 px** pod nebo před další
komponentu. Když je prostor stísněnější nebo formulář složitější, lze 24 px nebo 16 px.

**Checkbox versus toggle:** toggle je preferovaný, když se akce aplikuje **okamžitě bez potvrzení**.
Checkbox je jeden vstup ve větším flow, které obvykle vyžaduje finální potvrzení.

**ZDROJ:** Carbon, Checkbox usage, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/components/checkbox/usage/
Detail klávesové obsluhy a proč je checkbox vlastní tabstop, ale skupina radií jeden:
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md).

## Toggle: dvě pravidla

1. **Vždycky označ toggle názvem ovlivněné vlastnosti**, kvůli přístupnostním omezením: **barva nesmí
   být jediný indikátor**.
2. Toggle je velmi běžný ovládací prvek v okamžitě aktualizovaných formulářích, kde se nevyžaduje
   odeslání. Samostatný toggle **nebo checkbox** lze použít pro jednu volbu, kterou uživatel zapíná
   a vypíná.

**ZDROJ:** Carbon, Forms pattern, Toggles.
https://carbondesignsystem.com/patterns/forms-pattern/

---

## Co tahle nota neřeší

- Placeholder jako anti-pattern s WCAG oporou.
  [Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md). To je nadřazený zdroj.
- Klávesovou obsluhu jednotlivých variant do detailu.
  [Klávesnice a focus](../zaklady/klavesnice-a-focus.md).
- Radio button, toggle, date picker, number input, slider a file uploader jako samostatné komponenty.
  Carbon je má, ale v přečtené kopii jejich stránky nejsou. Co o nich vím, je zprostředkované přes
  Forms pattern a Read-only states pattern.
- Tagy jako alternativní formu výběru. [Tagy](tagy.md).

## Zdroj

IBM Carbon Design System: Dropdown usage, Select usage, Checkbox usage. Lokální kopie přečtená
30. 7. 2026. https://carbondesignsystem.com/components/dropdown/usage/ ·
https://carbondesignsystem.com/components/select/usage/ ·
https://carbondesignsystem.com/components/checkbox/usage/
Carbon u dropdownu cituje Angie Li, Dropdown: Design Guidelines (NN/g, 2017). Třída **B**.
