# UX copy v produktu: velká písmena, tón, slovník

Pravidla pro texty uvnitř aplikace: labely, nadpisy, tlačítka, hlášky. Otevři, když píšeš jakýkoliv
text, který bude v UI. Doplňuje [Content strategy a UX
writing](../../ux-design/ux-zaklady/content-strategy-ux-writing.md), která řeší obsahovou strategii.
Tahle nota řeší mechaniku jednotlivé věty a slova.

Pozor na jazyk: pravidla o velkých písmenech jsou anglická konvence. Co z nich platí v češtině,
řeším v poslední sekci.

Související: [Běžné akce](../vzory/bezne-akce.md) · [Notifikace](../vzory/notifikace.md) ·
[Textová pole](../komponenty/textova-pole.md)

---

## Velká písmena

### Sentence case všude

**PRAVIDLO:** Ve všech textech UI použij sentence case: velké písmeno jen na začátku a u vlastních
jmen. Platí pro nadpisy stránek, taby, labely, tlačítka, záhlaví tabulek i obsah tabulek.
**KDY PLATÍ:** Všechen text v produktu.
**PROČ:** Carbon uvádí dva důvody: sentence case umožňuje rozlišit obecné a vlastní jméno, a je
podle něj nejrychlejší na čtení.
**TŘÍDA:** B. Carbon k rychlosti čtení neuvádí studii, tvrdí „is generally considered the quickest
form to read".
**ZDROJ:** Carbon, Writing style, verbatim: „Use sentence-case capitalization for all UI text
elements. This style is predominantly lowercase. Capitalize only the initial letter of the first word
in the text and other words that require capitalization, such as proper nouns." a
„Sentence-style capitalization makes it easy for readers to distinguish between common nouns and
proper nouns, and is generally considered the quickest form to read."
https://carbondesignsystem.com/guidelines/content/writing-style/
**KDY NEPLATÍ:** Názvy produktů, služeb a značek. Carbon k tomu cituje IBM Style Guide: „Do not
capitalize the names of features and components unless they are sold separately or are trademarked."

### Title case ne

**PRAVIDLO:** Nepoužívej title case (velká písmena u většiny slov).
**PROČ:** Carbon uvádí tři důvody: vyžaduje, aby každý, kdo píše copy, znal poměrně složitá
gramatická pravidla; opírá se o subjektivní názor, co je „důležité"; a zpomaluje čtení, protože je
těžší rozlišit vlastní a obecná jména.
**TŘÍDA:** B
**ZDROJ:** Carbon, Writing style, sekce „Do not use title case capitalization", verbatim:
„Title case can also slow reading and comprehension down as it is more difficult for readers to
distinguish between proper nouns and common nouns."
https://carbondesignsystem.com/guidelines/content/writing-style/
**KDY NEPLATÍ:** Nikdy v UI. Carbon žádnou výjimku neuvádí.

### Verzálky ne

**PRAVIDLO:** Nepoužívej text celý velkými písmeny.
**PROČ:** Carbon: verzálky se čtou pomaleji, hlavně u víc než pár slov, protože jednotlivé tvary
písmen jsou méně rozlišitelné (stejná výška, žádné horní ani dolní dotažnice). A zaberou víc místa
na písmeno než sentence case.
**TŘÍDA:** B. Carbon říká „has been shown to be slower to read", ale studii necituje.
**ZDROJ:** Carbon, Writing style, sekce „Do not use all caps capitalization".
https://carbondesignsystem.com/guidelines/content/writing-style/
**KDY NEPLATÍ:** Zavedené zkratky a akronymy (ASCII, FAQ, HTML, PDF, OK). Ty Carbon velkými písmeny
psát velí. Poznámka: „OK", ne „Ok" ani „Okay".

### Velká písmena si zaslouží jen tenhle výčet

Carbon uvádí uzavřený seznam. Co v něm není, se nepíše s velkým písmenem:

- jména firem a organizací,
- oficiální nebo chráněné názvy produktů a služeb (kromě těch, které záměrně začínají malým, jako
  iPhone),
- iniciálové zkratky a akronymy,
- jména lidí,
- jména zemí a míst,
- odkaz na label v UI, který je sám s velkým písmenem,
- začátek věty.

**PRAVIDLO:** Nedávej slovu velké písmeno, aby vypadalo důležitě. Když potřebuješ zdůraznit,
použij kurzívu nebo tučné, ne obojí.
**ZDROJ:** Carbon, Writing style, „When to use capital letters" a „Capitalizing all other words",
verbatim: „Don't give a word a capital letter to denote 'specialness'."
https://carbondesignsystem.com/guidelines/content/writing-style/

### Jak v textu odkazovat na prvek UI

**PRAVIDLO:** Když v textu (dokumentaci, nápovědě, hlášce) odkazuješ na prvek rozhraní, použij
přesně tu velikost písmen, jakou má v UI. Když je pole „Name", píšeš „pole Name". Když stránka
„My network", píšeš „stránka My network", ne „My Network".
**ZDROJ:** Carbon, Writing style, „How to refer to UI elements".
https://carbondesignsystem.com/guidelines/content/writing-style/

## Jednoduchost

**PRAVIDLO:** Používej nejjednodušší výraz vhodný pro publikum. Krátká slova před dlouhými
a působivými. Věty krátké a jednoduché. Vypusť vatu a redundanci.
**PROČ:** Carbon to formuluje jako respekt k času uživatele: „Respect a user's time and make things
quick and easy to read. Always trim back to as few words as possible, although don't be terse."
**TŘÍDA:** B
**ZDROJ:** Carbon, Writing style, „Simple writing", verbatim včetně „Use the simplest term that is
appropriate for your audience. For example, use large instead of voluminous, and use small instead of
diminutive." https://carbondesignsystem.com/guidelines/content/writing-style/

**Tip, který Carbon dává:** veď si pro produkt seznam preferovaných a zakázaných slov. Pomáhá to
s konzistencí v čase, hlavně když copy píše víc lidí.

**PRAVIDLO:** Piš v jednoduchém přítomném čase. Když musíš do minulého nebo budoucího, vyhýbej se
tvarům se „have, has, had, been, should, would, will".
**ZDROJ:** Carbon, Writing style, „Use simple present tense".

## Tón

| Prostředek | Carbonovo pravidlo |
|---|---|
| Stažené formy (v angličtině) | Používej, když se hodí do kontextu a zlepší tok |
| Věta začínající „a", „ale", „takže" | Není zakázané, když to udělá věty krátké a skenovatelné. Nepřehánět. |
| Vykřičník | Jen u pozitivních zpráv, nikdy u negativních. Maximálně jeden v jednom kontextu (jedno okno, jedno téma). |
| Zdvořilostní obraty („prosím", „děkujeme") | Používej opatrně. Carbon doporučuje se jim v UI vyhýbat, protože mohou být v některých kulturních kontextech nevhodné nebo urážlivé. Výjimka: když uživatele reálně zdržujeme („Indexování může chvíli trvat. Vydržte."). |
| Osoba | Druhá osoba („vy", „vaše") tak často, jak to jde. První osoba jen v nadpisech a labelech vázaných na uživatelova data („Můj účet"), v navazujícím vysvětlení přepni na druhou. |
| „my" | Když mluvíš za organizaci, hlavně u vysvětlení, proč něco chceme („Proč potřebujeme váš e-mail?"). |
| Rod ve třetí osobě | Vyhýbej se genderově specifickým zájmenům. |

**ZDROJ:** Carbon, Writing style, sekce „Conversational style", „Formal versus casual tone",
„Terms of politeness", „Pronouns", „Inclusive language", verbatim u vykřičníků: „Use exclamation
marks only positively, not negatively. Make sure you use no more than one exclamation mark in
a context, such as a single window or a single Docs topic." a u zdvořilosti: „We recommend avoiding
terms of politeness such as please and thank you in a UI as they can be inappropriate or offensive in
some cultural contexts." https://carbondesignsystem.com/guidelines/content/writing-style/

**Poznámka k rozporu:** [Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md) zakazuje
„please" v chybové hlášce úplně, s citací GOV.UK („does not help fix the problem"). Carbon je
mírnější a povoluje zdvořilost tam, kde uživatele zdržujeme. V chybové hlášce platí přísnější
pravidlo, protože má tvrdší zdroj. V hlášce o čekání je Carbonova výjimka v pořádku.

## Aktivum a pasivum

**PRAVIDLO:** Kde fungují obě, zvol aktivum, je přímější. Pasivum je legitimní, když je skutečným
subjektem systém a člověk je až druhý.
**PŘÍKLAD Z CARBONU:** aktivum „Next, the admin configures access privileges." místo „Next, access
privileges are configured by the admin." Ale naopak „The database needs to be rebooted." místo
„Someone needs to reboot the database."
**TŘÍDA:** B
**ZDROJ:** Carbon, Writing style, „Active and passive voice".
https://carbondesignsystem.com/guidelines/content/writing-style/

## Slovník: can, may, might

**PRAVIDLO:** „Can" znamená schopnost, „may" znamená povolení (a někdy nejistotu). Když by šlo použít
„may" i „might", použij „might", aby nebylo zaměnitelné s významem povolení.
**ZDROJ:** Carbon, Writing style, „Can, may, and might".
https://carbondesignsystem.com/guidelines/content/writing-style/
**Pro češtinu:** analogie je „lze / může" versus „smí". Rozlišuj, jestli mluvíš o možnosti, nebo
o oprávnění, protože v produktu s rolemi je to zásadní rozdíl.

## Labely tlačítek a akcí

**PRAVIDLO:** Label tlačítka piš vzorcem {verb} + {noun}, kromě zavedených jednoslovných akcí
(„Done", „Close", „Cancel", „Add", „Delete"). Abstraktní „Submit" nepoužívej, uživateli říká, že
formulář je generický.
**KDY PLATÍ:** Každé tlačítko a akce.
**PROČ:** Carbon: „Buttons need to be clear and predictable." U formulářů dodává, že abstraktní
termíny dávají uživateli dojem, že formulář je generický.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button content, verbatim: „use the {verb} + {noun} content formula on buttons
except in the case of common actions like 'Done', 'Close', 'Cancel', 'Add', or 'Delete'."
https://carbondesignsystem.com/components/button/usage/ ·
Carbon, Forms pattern, „Naming actions": „Abstract terms like 'Submit' give the user the impression
that the form is generic." https://carbondesignsystem.com/patterns/forms-pattern/
**KDY NEPLATÍ:** Carbon sám připouští výjimku, když by delší label rozbil kompaktní UI nebo zhoršil
lokalizaci. Vzorec ale zůstává doporučenou praxí.

**Label tlačítka a titulek dialogu se musí shodovat.** Když se dialog otevírá tlačítkem
„Create access group", titulek dialogu je „Create access group". Carbon varuje před tendencí míchat
labely a titulky (ikona „New user" a titulek „Create user" je chyba).
**ZDROJ:** https://carbondesignsystem.com/components/modal/usage/

**Nezkracuj label tlačítka výpustkou.** Když se nevejde, ať se zalomí na druhý řádek.
**ZDROJ:** Carbon, Button, Overflow content: „We do not recommend truncating a button label."

## Labely polí

- Každý vstup má label, i když je formátovaný jinak.
- Label není helper text. Jedno až tři slova.
- Bez dvojtečky na konci.
- Sentence case.

**ZDROJ:** Carbon, Forms pattern, Labels, verbatim: „Do not use colons after label names." a
„Labels are not helper text; be succinct. Use one to three words only."
https://carbondesignsystem.com/patterns/forms-pattern/
Detail k helper textu, placeholderu a tooltipu: [Textová pole](../komponenty/textova-pole.md).

---

## Co z toho platí v češtině

Tohle je moje vyhodnocení, ne Carbonovo tvrzení (**třída C**):

| Pravidlo | Platí v češtině |
|---|---|
| Sentence case | Ano, a je to i česká typografická norma. Čeština title case nemá, takže tenhle problém odpadá. |
| Verzálky ne | Ano, důvod (nerozlišitelné tvary písmen) je jazykově nezávislý. |
| Uzavřený seznam velkých písmen | Ano v principu, ale řídí se českými pravidly (názvy institucí, zeměpisná jména). |
| Neděl velké písmeno pro důležitost | Ano, v češtině je to ještě viditelnější chyba (kalk z angličtiny). |
| Jednoduchá slova, krátké věty | Ano. |
| Druhá osoba | Ano, ale řeš vykání versus tykání konzistentně napříč produktem. Carbon tenhle problém v angličtině nemá. |
| Stažené formy, věta od „a" | Netýká se, jiná gramatika. |
| Vyhýbat se genderově specifickým zájmenům | Ano, ale v češtině je to těžší (rod v přechodnících a příčestích). Praktické řešení je obcházet formulaci, ne hledat neutrální zájmeno. |
| {verb} + {noun} na tlačítku | Ano („Přidat uživatele", ne „Odeslat"). |

## Co tahle nota neřeší

- Obsahovou strategii a strukturu delšího textu.
  [Content strategy a UX writing](../../ux-design/ux-zaklady/content-strategy-ux-writing.md).
- Text chybové hlášky do detailu, včetně zakázaného slovníku. To má tvrdší zdroje ve
  [formulářích a stavech](../../ux-design/pravidla/formulare-a-stavy.md).
- Markery generického AI textu. [Anti-slop](../../ux-design/pravidla/anti-slop.md).
- Konkrétní schválené labely akcí. Carbon na to má stránku `guidelines/content/action-labels`, která
  v přečtené kopii není. Co z ní vím zprostředkovaně, je v [Běžné akce](../vzory/bezne-akce.md).

## Zdroj

IBM Carbon Design System, Content guidelines, Writing style, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/guidelines/content/writing-style/
Doplněno pravidly o labelech z Button usage, Forms pattern a Modal usage. Třída **B**, Carbon
u tvrzení o rychlosti čtení neuvádí studii.
