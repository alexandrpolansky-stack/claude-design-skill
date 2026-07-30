# Disabled, read-only, nebo skryté

Tři způsoby, jak udělat prvek neovladatelný. Nejsou zaměnitelné a volba mezi nimi je přístupnostní
rozhodnutí, ne vizuální.

Související: [Klávesnice a focus](../zaklady/klavesnice-a-focus.md) ·
[Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md) ·
[Skladba formuláře](formular-skladba.md)

---

## Rychlé rozhodnutí

1. Potřebuje uživatel obsah **přečíst**? Ano = **read-only**. Nikdy ne disabled.
2. Je to **dočasné** a odemkne to akce nebo rozhodnutí uživatele? = **disabled**.
3. Nemá uživatel **oprávnění** to vidět ani s tím pracovat? = **skryté**.
4. Disabled prvek **nikdy nesmí zmizet** z pohledu uživatele, když je zablokovaný jen dočasně.
5. Disabled a read-only **nezaměňuj a nepřeklápěj** mezi sebou.
6. Prvek, který je disabled, zůstane disabled i v read-only režimu zobrazení.
7. Read-only nepoužívej na statickou informaci u prvku, který **nemá** aktivní stav.
8. Když dočasně zablokovaný prvek ovlivňuje víc věcí nebo primární akci flow, přidej **inline
   varovnou notifikaci**, která řekne, jak to odemknout.

---

## Tři varianty a co dělají

| Varianta | Co se stane |
|---|---|
| Default disabled | Nedá se kliknout, vybrat ani s tím interagovat. **Nečte ho čtečka.** Má výchozí disabled vizuální styl |
| Read-only | Uživatel s tím nemůže interagovat, ale **obsah je pořád čitelný a dostupný čtečce**. Vizuální styl nesmí obsahovat žádné interaktivní indikátory: interaktivní barvu, hover stavy ani textové ozdoby (podtržení) |
| Hidden | Komponenta je úplně skrytá z pohledu. **Uživatel neví, že ta možnost existuje** |

**ZDROJ:** Carbon, Disabled states pattern, tabulka Disabled variations.
https://carbondesignsystem.com/patterns/disabled-states/

## Default disabled

**Kdy:** komponenta je **dočasně** zablokovaná kvůli závislostem (jeden kus softwaru se opírá o jiný)
nebo předpokladům. Je to dočasná změna stavu, kterou nejčastěji vyvolá akce **nebo nečinnost**
uživatele. Jak se závislosti vyřeší nebo předpoklady splní, komponenta se vrátí do aktivního stavu.

**PRAVIDLO:** V dočasně zablokovaném scénáři komponenta **nikdy nesmí úplně zmizet** z pohledu
uživatele.
**KDY PLATÍ:** Každý dočasně disabled prvek.
**PROČ:** Kdyby zmizela, uživatel nemá jak zjistit, že možnost existuje a co ji odemkne.
**TŘÍDA:** B
**ZDROJ:** Carbon, Disabled states, Default disabled, verbatim: „In a temporarily disabled scenario the
component should never fully disappear from the user's view."
https://carbondesignsystem.com/patterns/disabled-states/
**KDY NEPLATÍ:** Nikdy pro dočasné blokování. Pro trvalé blokování bez oprávnění je správná varianta
skryté, ne disabled.

**Styl:** Carbon disabled stavy nejčastěji řeší **snížením průhlednosti**, bez změny na hover a s
kurzorem `not-allowed`. Konkrétní hodnoty, které Carbon uvádí:

| Atribut | Disabled styl |
|---|---|
| Komponenta | 50 % opacity |
| Text | 25 % opacity |
| Ikony | 50 % opacity |
| Hover | Žádný |
| Kurzor | `not-allowed` |

Carbon zároveň dodává, že správný disabled stav je u každé komponenty definovaný zvlášť, takže tuhle
tabulku ber jako výchozí vzorec, ne jako univerzální pravidlo.

**Doplňkové varování:** když dočasně zablokovaná položka ovlivňuje **víc položek** nebo **primární
akci flow**, lze zobrazit **inline varovnou notifikaci**. Ta má popsat, jak uživatel může komponentu
zapnout nebo znovu zapnout.
**ZDROJ:** Carbon, Disabled states, Additional warning.
https://carbondesignsystem.com/patterns/disabled-states/
Detail notifikace: [Notifikace](notifikace.md)

## Read-only

**Kdy:** obsah zablokované komponenty je pro uživatele **pořád relevantní** nebo důležitý pro dokončení
úkolu. Uživatel si informaci může přečíst, ale nemůže s ní interagovat ani ji změnit. **Read-only obsah
musí být vždy dostupný čtečce.**

**Read-only stav je považovaný za aktivní** a data v něm **může aplikace používat ve svých procesech**.
Změna stavu přemění účel komponenty z interaktivního na čistě informativní.

**Tři případy, které read-only vyvolávají:**

| Případ | Popis |
|---|---|
| Aplikační proces | Proces aplikace dočasně brání uživateli komponentu upravit, dokud proces neskončí |
| Locked | Aplikace omezuje, kolik uživatelů může komponentu upravovat ve stejnou dobu |
| Permissions | Přihlašovací údaje uživatele mu dovolí komponentu vidět, ale neupravit |

**ZDROJ:** Carbon, Read-only states pattern, When to use.
https://carbondesignsystem.com/patterns/read-only-states-pattern/

### Kdy read-only nepoužít

Carbon jmenuje tři situace:

1. **Když komponenta nemá aktivní stav**, nepoužívej read-only na zobrazení statické informace.
2. **Jako alternativu k disabled stavu.** Read-only a disabled slouží různým účelům. Když je komponenta
   dočasně nedostupná v očekávání akcí nebo rozhodnutí uživatele (dokončení formuláře, volba možnosti),
   stav má být **dočasně disabled, ne read-only**.
3. **Když by komponenta jinak byla disabled.** Komponenty v disabled stavu se nemají překlápět do
   read-only.

**ZDROJ:** Carbon, Read-only states pattern, When not to use.
https://carbondesignsystem.com/patterns/read-only-states-pattern/

### Anatomie read-only stavu

Čtyři změny, které Carbon jmenuje:

1. **Změna barvy pozadí:** u polí průhledné pozadí.
2. **Změna barvy okraje:** de-emfáze výběru a klikatelnosti, aby byla informace čitelnější.
3. **Barva textu se nemění.** Zůstává stejná jako v aktivním stavu a **musí pořád splňovat pravidlo
   kontrastu 4,5:1**.
4. **Změna barvy ikony:** vložené ikony zůstávají v komponentě kvůli kontextu, ale změnou barvy
   a kurzoru se sdělí, že nejsou interaktivní.

**Struktura zůstává:** komponenty mají udržet stejnou strukturu a rozestupy jako v aktivním stavu.
Ve většině případů jsou prvky z aktivního stavu přítomné i v read-only.

**Detail chování polí:** u komponent s default stylem pozadí pole **splyne s pozadím UI nebo vrstvy**.
U fluid komponent pozadí pole **zůstane stejné** jako v aktivním stavu.

**ZDROJ:** Carbon, Read-only states pattern, Formatting a Visual guidance.
https://carbondesignsystem.com/patterns/read-only-states-pattern/

### Interakce v read-only

| Vstup | Chování |
|---|---|
| Myš | **Kurzor šipky** (ne text, ne pointer). Posiluje, že komponenta není interaktivní |
| Klávesnice | Interaktivní operace z aktivního stavu se odeberou nebo změní. **Komponenta zůstane navigovatelná klávesnicí** |

**ZDROJ:** Carbon, Read-only states pattern, Interactions.
https://carbondesignsystem.com/patterns/read-only-states-pattern/

### Obsah v read-only

**PRAVIDLO:** Komponenty mají obsahovat stejný obsah jako v aktivním stavu. **Ale** když je obsah
aktivního stavu **instruktivní** (dropdown bez vybrané hodnoty s textem „Vyberte možnost"), musí se
změnit na **informativní**.
**KDY PLATÍ:** Read-only prvky s výzvou nebo instrukcí.
**PROČ:** Instrukce, kterou nelze provést, je pro uživatele šum.
**TŘÍDA:** B
**ZDROJ:** Carbon, Read-only states pattern, Content, verbatim: „when the content in the enabled state
is instructive, like a dropdown with no current selection, the content may need to change to be
informative." https://carbondesignsystem.com/patterns/read-only-states-pattern/

## Skryté

**Kdy:** něco nebo někdo nemá oprávnění část UI vidět, interagovat s ní nebo na ní provést akci.
Varianta komponentu, stránku nebo akci z rozhraní **úplně skryje**. Jediný způsob, jak skrytý prvek
odemknout a znovu ukázat, je **změnit přiřazené oprávnění**.

**Carbonův příklad:** vlastník organizace může přidávat členy. Uživatelům, kteří vlastníci nejsou,
se tlačítko „Add member" na stránce s adresářem týmu nezobrazí. Až se uživatel stane vlastníkem
organizace, **teprve pak** bude tlačítko viditelné.

**ZDROJ:** Carbon, Disabled states pattern, Hidden.
https://carbondesignsystem.com/patterns/disabled-states/

## Tři nejdůležitější pravidla celého vzoru

### Nepoužívej disabled na to, co má uživatel přečíst

**PRAVIDLO:** Nepoužívej disabled stav u komponent, které uživatel potřebuje přečíst.
**PROČ:** Carbon dává dva důvody: na rozdíl od read-only stavů **disabled stavy čtečka nečte a
nesplňují vizuální kontrast**, takže když je potřeba je interpretovat, jsou nepřístupné.
**TŘÍDA:** B pro Carbonovu formulaci, ale opírá se o fakt, že WCAG neaktivní prvky z požadavku na
kontrast vyjímá, takže je to fakticky přesné.
**ZDROJ:** Carbon, Read-only states pattern, Best practices, State readability, verbatim: „Don't use
a disabled state for components if they need to be read by the user. Unlike read-only states, disabled
states are not read by screen readers and do not pass visual contrast, making them inaccessible if
they need to be interpreted." https://carbondesignsystem.com/patterns/read-only-states-pattern/
**KDY NEPLATÍ:** Nikdy. Tohle je hard pravidlo.

**Praktický důsledek, který se v produktech často porušuje:** „přehled objednávky" nebo „souhrn
konfigurace" postavený z disabled inputů je nepřístupný. Má být read-only, nebo prostý text.

### Read-only režim nepřeklápí disabled stavy

**PRAVIDLO:** V read-only pohledu **udrž** disabled stav komponenty. Neměň stav komponenty z disabled
na read-only jen proto, že je aktivní read-only pohled. Některé stavy mají podle situace zůstat
disabled.
**KDY PLATÍ:** Obrazovky, které mají read-only režim (například detail záznamu bez práva editace).
**TŘÍDA:** B
**ZDROJ:** Carbon, Read-only states pattern, Best practices, Read-only viewports.
https://carbondesignsystem.com/patterns/read-only-states-pattern/

### Navigovatelné versus ovladatelné

**PRAVIDLO:** Read-only prvek **je** navigovatelný klávesnicí (aby si uživatel přečetl obsah), ale
**není** ovladatelný (hodnotu nezmění). Disabled prvek není navigovatelný vůbec.
**TŘÍDA:** B
**ZDROJ:** Carbon, Read-only states pattern, Accessibility, verbatim citace v
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md).
https://carbondesignsystem.com/patterns/read-only-states-pattern/

## Které komponenty read-only stav mají

Carbon read-only stav dokumentuje u dvou kategorií ovládacích prvků:

| Kategorie | Prvky |
|---|---|
| Selection controls | checkbox, radio button, toggle, dropdown, select, combo box, multiselect |
| Bound entry controls | number input, slider, date picker, time picker |

Plus text input a text area.

**ZDROJ:** Carbon, Read-only states pattern, Structure a Related.
https://carbondesignsystem.com/patterns/read-only-states-pattern/

**Poznámka k úplnosti stavů komponent:** Carbon u vstupů uvádí sadu stavů **enabled, hover, focus,
error, warning, disabled, skeleton, read-only**. U komponenty `form` má read-only označený jako
„Coming soon", takže napříč Carbonem to není úplně dotažené. Detail sady stavů u konkrétních vstupů:
[Textová pole](../komponenty/textova-pole.md) a
[Výběr ze seznamu](../komponenty/vyber-ze-seznamu.md).

## Disabled stav a kontrast

**Fakt, který je potřeba znát:** Carbon u disabled stavů opakovaně uvádí, že jejich stylování
**nepodléhá požadavku WCAG na kontrast**. Například u tabů: „The styling is not subject to WCAG
contrast compliance."
Zdroj: https://carbondesignsystem.com/components/tabs/usage/

**Proč to tak je** (moje doplnění, ne Carbonovo tvrzení): WCAG neaktivní komponenty rozhraní
z požadavků na kontrast vyjímá. **A přesně proto** platí pravidlo výše: co má uživatel přečíst, nesmí
být disabled. Disabled stav je vizuálně slabý záměrně a legálně, takže na něm nesmí záležet.
Detail k WCAG kontrastu: [kontrast a barva](../../ux-design/pravidla/kontrast-a-barva.md).

---

## Co tahle nota neřeší

- Kdy disablovat odesílací tlačítko formuláře (krátký versus dlouhý formulář).
  [Skladba formuláře](formular-skladba.md).
- Konkrétní disabled a read-only styl jednotlivých komponent. Carbon je má na stránkách `style`,
  odkud tokeny záměrně nepřebírám.
- Skrytí prvku z důvodů jiných než oprávnění (progresivní odhalování, podmíněná pole).
  [Skladba formuláře](formular-skladba.md).

## Zdroj

IBM Carbon Design System, Disabled states pattern a Read-only states pattern, lokální kopie přečtená
30. 7. 2026. https://carbondesignsystem.com/patterns/disabled-states/ ·
https://carbondesignsystem.com/patterns/read-only-states-pattern/
Carbon k read-only stavům cituje MDN (HTML attribute: readonly, 2022), Aaron Gustafson, Web Forum
Conundrum: disabled or read-only? (2017) a W3Schools. Třída **B**.
