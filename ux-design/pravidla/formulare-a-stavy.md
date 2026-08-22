# Formuláře, validace a stavy rozhraní

Pravidla pro moment, kdy stavíš formulář nebo řešíš, co se zobrazí, když data nejsou, načítají se
nebo něco spadlo. Tři témata držím v jedné notě, protože se v praxi řeší současně: formulář bez
chybového a bez odesílacího stavu není hotový.

Nota je postavená na vlastním dohledávání zdrojů, ne na průzkumu fáze 1. Fáze 1 formuláře ani stavy
nepokryla. Jediný přenesený kus je Cowan 2001 u multi-step formulářů, viz sekce Multi-step.

**Třídy důkazu:** **A** = tvrdá opora (peer-reviewed studie, právní požadavek, normativní text).
**B** = publikovaná konvence (design systém, výzkumná organizace, dohledatelný nepeer-reviewed
experiment). **C** = řemeslná praxe bez měření. Třídu nikdy nepovyšuj.

Související: [anti-slop](anti-slop.md) · [UX Laws](../zakony-principy/ux-laws.md) ·
[Osmibodová mřížka](../zakony-principy/osmibodova-mrizka.md) ·
[Content strategy a UX writing](../ux-zaklady/content-strategy-ux-writing.md)

---

## Rychlý průchod, když nemáš čas na celou notu

1. Viditelný label nad každým polem. Placeholder nikdy jako label ani jako hint.
2. Jeden sloupec, šířka pole podle očekávané délky obsahu, `autocomplete` na každém poli.
3. Validuj při odeslání. Inline na blur jen u polí s tvrdým formátem, nikdy během prvního psaní.
4. Chyba = error summary nahoře s focusem, plus hláška u pole. Zadané hodnoty nemazat.
5. Hláška říká co se stalo a jak to opravit, imperativem. Žádné "invalid", "oops", "please".
6. Prázdný stav = stav systému plus vysvětlení plus akce. Nikdy jen "žádná data".
7. Do 1 s bez indikátoru, 1 až 10 s spinner, nad 10 s procentní progress.

---

## Struktura formuláře

### Viditelný label u každého pole

**PRAVIDLO:** Každé vstupní pole má vlastní `<label>` svázaný přes `for`/`id`, a ten label je
viditelný. Placeholder není label. Skrytý label jen tam, kde je popis nesporný z okolí (search
v hlavičce), a i tam musí existovat v DOM pro čtečku.
**KDY PLATÍ:** Vždy, každý formulář, každá platforma.
**PROČ:** WCAG 3.3.2 to vyžaduje na úrovni A. Čtečky obrazovky placeholder nečtou jako label
(W3C WAI to říká explicitně) a placeholder zmizí při psaní, takže uživatel nemůže před odesláním
zkontrolovat, co kam napsal.
**TŘÍDA:** A
**ZDROJ:** WCAG 2.2 SC 3.3.2 Labels or Instructions, Level A, verbatim: "Labels or instructions are
provided when content requires user input."
https://www.w3.org/WAI/WCAG22/quickref/ · W3C WAI Forms tutorial verbatim: "placeholder text is not
a replacement for labels. Assistive technologies, such as screen readers, do not treat placeholder
text as labels." https://www.w3.org/WAI/tutorials/forms/instructions/
**KDY NEPLATÍ:** Nikdy pro absenci labelu. Skrytí (`visually hidden`) je legitimní jen když je účel
pole zřejmý z kontextu a v DOM label zůstává.

### Placeholder nepoužívej vůbec, ani na hinty a příklady

**PRAVIDLO:** Nedávej do `placeholder` label, hint ani příklad formátu. Hint dej jako samostatný
viditelný text pod label a nad pole, jednu krátkou větu bez tečky, svázaný přes `aria-describedby`.
**KDY PLATÍ:** Všude, kde uživatel do pole píše.
**PROČ:** Tři nezávislé důvody, ne jeden: zmizí při psaní (paměťová zátěž, nejde zkontrolovat
odpověď), čtečky ho nečtou spolehlivě, a defaultní styl prohlížeče typicky nesplňuje WCAG 1.4.3
kontrast 4,5:1. NN/g navíc z eye-trackingu uvádí, že oči jdou k prázdným polím, takže vyplněně
vypadající pole lidé přeskočí.
**TŘÍDA:** B pro imperativ, A pro kontrastní část (WCAG 1.4.3 AA).
**ZDROJ:** GOV.UK Design System, Text input, verbatim: "Do not use placeholder text in place of
a label, or for hints or examples, as: it vanishes when the user starts typing, which can cause
problems for users with memory conditions or when reviewing answers; not all screen readers read it
out; its browser default styles often do not meet WCAG 2.2 success criterion 1.4.3 Contrast
(minimum)". https://design-system.service.gov.uk/components/text-input/ ·
Katie Sherwin, Placeholders in Form Fields Are Harmful, NN/g, 11. 5. 2014, revize 10. 9. 2018.
https://www.nngroup.com/articles/form-design-placeholders/ · Home Office Design System, verbatim:
"Do not: use placeholders". https://design.homeoffice.gov.uk/accessibility/interactivity/forms
**KDY NEPLATÍ:** Padá jen u polí, kde nelze psát a hodnota je vybíraná (nativní `select` s prvním
neaktivním prvkem), a i tam je lepší label plus explicitní volba.

### Label nad polem

**PRAVIDLO:** Label zarovnej nad pole, na levou hranu pole, sentence case, bez dvojtečky na konci.
**KDY PLATÍ:** Default pro webové a mobilní formuláře.
**PROČ:** Label nad polem je s polem v jednom svislém skenu, takže se čte jedním pohybem oka.
Zarovnání vlevo od pole vytváří dva nezávislé cíle a horizontální saccade.
**TŘÍDA:** B jako konvence design systémů. Konkrétní čísla k saccade jsou C.
**ZDROJ:** GOV.UK Design System, Text input, verbatim: "You should align labels above the text input
they refer to. They should be short, direct and written in sentence case. Do not use colons at the
end of labels." https://design-system.service.gov.uk/components/text-input/ ·
Podpora třídy C: Matteo Penzo, Label Placement in Forms, UXmatters, 12. 7. 2006 (uvádí ~50 ms
saccade u labelu nad polem vs ~500 ms u labelu zarovnaného vlevo, ale **velikost vzorku v článku
není uvedena**, takže se na ta čísla nedá opřít).
https://www.uxmatters.com/mt/archives/2006/07/label-placement-in-forms.php
**KDY NEPLATÍ:** Hustá interní datová mřížka nebo editovatelná tabulka, kde je svislé místo dražší
než jeden saccade a uživatel je expert na opakovaný úkon. Existuje i peer-reviewed eye-tracking
práce k zarovnání labelů (NordiCHI 2008, DOI 10.1145/1463160.1463217), ale plný text je za
paywallem a její nálezy jsem neověřil, takže ji jako oporu neuvádím.

### Jeden sloupec

**PRAVIDLO:** Pole skládej do jednoho svislého sloupce, jedno pole na řádek. Výjimka jsou části
jedné logické hodnoty (den/měsíc/rok, jméno/příjmení, PSČ/město) v jednom `fieldset`.
**KDY PLATÍ:** Každý formulář, který uživatel vyplňuje poprvé nebo zřídka.
**PROČ:** Dva sloupce nutí uživatele rozhodnout, kterým směrem pokračovat, a rozbíjejí svislý sken
na cik-cak. V měřeném srovnání to stálo přes 15 sekund na formuláři.
**TŘÍDA:** B. Je to online experiment s randomizací, ne peer-reviewed studie, a autoři sami
generalizaci omezují.
**ZDROJ:** Speero (dříve CXL Institute), Form Field Usability: Single or Multi-Column Forms,
originální výzkum 6/2016, publikováno 17. 10. 2016. N = 702 (356 single-column, 346 multi-column),
desktop. Verbatim: "Survey participants completed the linear, single-column form (n = 356) an
average of 15.4 seconds faster than the multi-column form (n = 346)", signifikantní na 95 %.
Vlastní limitace autorů verbatim: "These results are therefore not directly transferable to all
form types and situations."
https://speero.com/post/form-field-usability-should-you-use-single-or-multi-column-forms-original-research
**KDY NEPLATÍ:** Interní nástroj, kde profík vyplňuje stejný formulář stokrát denně a chce vidět
celý stav na jedné obrazovce bez scrollu. Tam optimalizuješ na počet stisků, ne na první průchod.

### Označuj volitelná pole, ne povinná

**PRAVIDLO:** Za label volitelného pole napiš `(optional)`, respektive `(nepovinné)`, stejnou barvou
jako hint text. Povinná pole neoznačuj hvězdičkou ani ničím jiným. Zároveň volitelných polí měj
minimum, každé pole musí obhájit svou existenci.
**KDY PLATÍ:** Veřejné formuláře, registrace, checkout, žádosti.
**PROČ:** Hvězdička je nesémantická značka, kterou musí uživatel dekódovat z legendy, a při většině
polí povinných značíš vlastně celý formulář. Označit menšinu je méně šumu.
**TŘÍDA:** B, publikovaná konvence GOV.UK. Měřený rozdíl v konverzi jsem nenašel.
**ZDROJ:** GOV.UK Design System, Addresses pattern používá `Address line 2 (optional)` a
`County (optional)`, povinná pole neoznačuje.
https://design-system.service.gov.uk/patterns/addresses/
Na odfiltrování zbytečných polí: question protocol, UXmatters, odkazovaný GOV.UK.
https://www.uxmatters.com/mt/archives/2010/06/the-question-protocol-how-to-make-sure-every-form-field-is-necessary.php
**KDY NEPLATÍ:** Formulář, kde je povinné jen jedno nebo dvě pole z mnoha. Pak označ povinná
a nepoužívej hvězdičku, ale slovo.

### Šířka pole nese informaci o délce obsahu

**PRAVIDLO:** Pole na PSČ, telefon nebo číslo karty udělej fixně široké přibližně na očekávaný
obsah. Nedávej všem polím stejnou plnou šířku.
**KDY PLATÍ:** Kdykoliv má vstup známou délku.
**PROČ:** Šířka je afordance. Pole na 5 znaků říká "sem patří pět znaků" bez jediného slova hintu.
**TŘÍDA:** B
**ZDROJ:** GOV.UK Design System, Text input, verbatim: "Help users understand what they should enter
by making text inputs the right size for the content they're intended for."
https://design-system.service.gov.uk/components/text-input/
**KDY NEPLATÍ:** Mobilní layout pod 320 px šířky, kde fixní šířky rozbíjejí reflow. WCAG 1.4.10
Reflow (AA) má přednost.

### autocomplete na každém poli o uživateli

**PRAVIDLO:** Na každé pole, které se ptá na údaj o uživateli, dej `autocomplete` s hodnotou z HTML
specifikace (`email`, `tel`, `postal-code`, `bday-day`, `street-address`, `cc-number`).
**KDY PLATÍ:** Produkce. V prototypu to není potřeba.
**PROČ:** Prohlížeč pak umí pole vyplnit sám, což je největší jednotlivá úspora práce ve formuláři
vůbec, a hlavně to WCAG vyžaduje na úrovni AA.
**TŘÍDA:** A
**ZDROJ:** WCAG 2.2 SC 1.3.5 Identify Input Purpose, Level AA, nové v 2.1.
https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html · GOV.UK Design System,
Text input a Addresses, verbatim: "Use the `autocomplete` attribute on each individual address field
to help users enter their address more quickly."
**KDY NEPLATÍ:** Pole, které se neptá na údaj o uživateli (hledání, poznámka, částka faktury cizího
subjektu). Tam `autocomplete` nemá co doplnit.

### Viditelný okraj a dost velký terč

**PRAVIDLO:** Rámeček inputu, checkboxu a ikonového tlačítka musí mít kontrast alespoň 3:1 proti
sousednímu pozadí. Klikatelný terč nesmí být menší než 24 × 24 CSS px.
**KDY PLATÍ:** Vždy, včetně dark mode a včetně stavů hover a focus.
**PROČ:** WCAG 1.4.11 (AA) a 2.5.8 (AA, nové v 2.2) to vyžadují. Nezávisle na tom: když prvek nemá
signifikátor, lidé ho hledají výrazně déle a nejsou si jistí, i když ho vidí. NN/g to naměřila jako
o 22 % delší čas na stránce a o 25 % víc fixací.
**TŘÍDA:** A
**ZDROJ:** WCAG 2.2 SC 1.4.11 Non-text Contrast (AA, 2.1) a SC 2.5.8 Target Size (Minimum) (AA,
nové v 2.2, 5. 10. 2023), 5 výjimek. https://www.w3.org/WAI/WCAG22/quickref/ · Kate Moran, Flat UI
Elements Attract Less Attention and Cause Uncertainty, NN/g, 3. 9. 2017, eye-tracking, N = 71,
between-subjects. U jedné z devíti dvojic stránek našlo cílový odkaz 50 % (12/24) uživatelů ve
slabé verzi vs 86 % (25/29) v silné, p < 0,005.
https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/
**KDY NEPLATÍ:** 2.5.8 má pět publikovaných výjimek (spacing, equivalent, inline, user agent,
essential). Inline odkaz v odstavci pod 24 px není porušení.

---

## Validace

### Default: validuj při odeslání, ne při odchodu z pole

**PRAVIDLO:** Ve veřejné službě, žádosti a formuláři pro širokou populaci validuj až po stisku
Odeslat nebo Pokračovat. Nevaliduj při blur.
**KDY PLATÍ:** Veřejný sektor, formuláře pro nesegmentované publikum, cokoliv, co má splnit WCAG AA
a být použitelné pro pomalé pisatele a uživatele čteček.
**PROČ:** Validace na blur potrestá každého, kdo pole opustí kvůli přemýšlení nebo přepnutí okna.
GOV.UK to takhle testovala dlouhodobě na obnově pasu pro dospělé.
**TŘÍDA:** B
**ZDROJ:** GOV.UK Design System, Recover from validation errors, verbatim: "Do not validate when the
user moves away from a field. Wait until they try to move to the next part of the service - usually
by clicking the 'continue' or 'submit' button at the bottom of the page." Odůvodnění: inline validace
"can cause problems - especially for users who type more slowly".
https://design-system.service.gov.uk/patterns/validation/
**KDY NEPLATÍ:** Pole s tvrdým, okamžitě rozhodnutelným formátem, kde uživatel má z okamžité
odpovědi prokazatelný přínos (dostupnost uživatelského jména, heslo proti politice, počítadlo znaků).
Tam platí následující pravidlo. GOV.UK to sama povoluje pod podmínkou, že to obhájíš výzkumem.

### Inline validace jen na blur a jen u tvrdého formátu

**PRAVIDLO:** Když inline validaci děláš, spusť ji nejdřív po opuštění pole (blur), případně
v momentě, kdy vstup dosáhl známé správné délky (PSČ, číslo karty). Pozitivní potvrzení (zaškrtnutí
u správně vyplněného pole) je v pořádku a snižuje kontrolování na konci.
**KDY PLATÍ:** Checkout, registrace, pole s deterministickým formátem, produkty s vlastním výzkumem.
**PROČ:** V jediném dohledaném kontrolovaném srovnání timingu byla varianta "po dokončení pole"
nejlepší a varianta "před a během psaní" nejhorší.
**TŘÍDA:** B. Wroblewski 2009 je publikovaný, ale malý (N = 22) a nepeer-reviewed. Baymard je
moderované think-aloud plus expertní benchmark, **bez A/B testu a bez měření konverze na živém
provozu** (viz klasifikace v průzkumu fáze 1).
**ZDROJ:** Luke Wroblewski, Inline Validation in Web Forms, A List Apart, 1. 9. 2009. N = 22, věk
21 až 49, eye-tracking, šest variant formuláře v randomizovaném pořadí. Hlášené výsledky proti
kontrole: success rate +22 %, chyby −22 %, satisfaction +31 %, čas dokončení −42 %, fixace −47 %.
Nejlepší timing "after (on blur)", nejhorší "before and while".
https://alistapart.com/article/inline-validation-in-web-forms/ ·
Baymard Institute, Usability Testing of Inline Form Validation. https://baymard.com/blog/inline-form-validation
**KDY NEPLATÍ:** Pole, jehož správnost nelze rozhodnout bez serveru a odpověď trvá. Blikající
"kontroluji" u každého pole je horší než jedna validace při odeslání.

### Nikdy nevaliduj během prvního psaní

**PRAVIDLO:** Nezobraz chybu, dokud uživatel pole poprvé nedokončil. Žádné "neplatný e-mail" po
třetím znaku.
**KDY PLATÍ:** Vždy, i tam, kde inline validaci povolíš.
**PROČ:** Uživatel dostane vytýkáno něco, co ještě nedopsal. Ve Wroblewského srovnání to byla
nejhorší z testovaných variant, s doslovnou reakcí účastníka "it's flashing red before I've even
started". Baymard to nazývá premature validation a popisuje, že se lidé cítili napadeni.
**TŘÍDA:** B
**ZDROJ:** viz předchozí pravidlo, obě citace.
**KDY NEPLATÍ:** Počítadlo znaků a měřič síly hesla, které nejsou chyba, ale průběžná informace,
a nejsou červené.

### Chybu ruš okamžitě, jak ji uživatel opraví

**PRAVIDLO:** Jakmile vstup vyhoví, chybovou hlášku odstraň hned, na úrovni jednotlivého znaku.
Nečekej na blur ani na další odeslání.
**KDY PLATÍ:** Vždy, když už je chyba zobrazená.
**PROČ:** Chyba, která svítí i po opravě, uživatele nutí hádat, jestli oprava zabrala.
**TŘÍDA:** B
**ZDROJ:** Baymard Institute, Usability Testing of Inline Form Validation, doporučení odstraňovat
chybovou zprávu okamžitě při opravě vstupu. https://baymard.com/blog/inline-form-validation
**KDY NEPLATÍ:** Chyba, kterou nelze lokálně vyhodnotit (server odmítl kód, kolize s cizím
záznamem). Ta zmizí až po dalším pokusu, a musí to být z hlášky jasné.

### Nikdy nemaž, co uživatel zadal

**PRAVIDLO:** Při chybě zachovej všechny hodnoty, správné i chybné. Nikdy nevyprazdňuj pole ani
neresetuj formulář. Napříč kroky procesu už zadané údaje předplňuj nebo nabídni k vybrání.
**KDY PLATÍ:** Vždy. Tohle je hard.
**PROČ:** Přepisování hodnoty za uživatele mu bere možnost vidět, co udělal špatně, a nutí ho psát
znovu. WCAG 2.2 na to má vlastní kritérium.
**TŘÍDA:** A pro opakované zadávání napříč procesem (WCAG 3.3.7 Redundant Entry, Level A, nové
v 2.2), B pro konkrétní imperativ "nemaž pole při validační chybě".
**ZDROJ:** WCAG 2.2 SC 3.3.7 Redundant Entry, Level A, verbatim: "Information previously entered by
or provided to the user that is required to be entered or submitted again in the same process or
across a persistent user session is either auto-populated or made available for the user to select."
https://www.w3.org/WAI/WCAG22/quickref/ · GOV.UK Design System, Error message, verbatim: "Do not
clear any form fields when showing the Error message component. Keep both passing and failing
answers." https://design-system.service.gov.uk/components/error-message/
**KDY NEPLATÍ:** Pole s citlivou hodnotou, kterou nesmíš vrátit v HTML (CVC kódu, jednorázový kód).
Tam pole vyprázdni a řekni to.

### Text chybové hlášky: co se stalo a jak to opravit

**PRAVIDLO:** Hláška má dvě části, popis problému a instrukci k opravě, imperativem, plain jazykem.
Různé chyby na jednom poli mají různé hlášky (prázdné vs špatný formát vs špatná délka). Zakázané:
technický žargon ("form post error", "unspecified error"), obviňování ("you forgot", "illegal",
"forbidden"), "please", "sorry", "valid"/"invalid", vtípky ("oops").
**KDY PLATÍ:** Každá validační chyba.
**PROČ:** WCAG 3.3.1 (A) vyžaduje, aby byla chyba popsaná textem, a 3.3.3 (AA) aby byla nabídnutá
oprava, pokud ji znáš. Generická hláška obojí nesplní. "Please" implikuje volbu, kterou uživatel
nemá, "sorry" neopravuje nic.
**TŘÍDA:** A pro požadavek popisu a návrhu opravy, B pro konkrétní slovník.
**ZDROJ:** WCAG 2.2 SC 3.3.1 Error Identification, Level A, verbatim: "If an input error is
automatically detected, the item that is in error is identified and the error is described to the
user in text." https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html ·
SC 3.3.3 Error Suggestion, Level AA. https://www.w3.org/WAI/WCAG22/quickref/ ·
GOV.UK Design System, Error message: "Describe what has happened and tell them how to fix it. The
message must be in plain English, use positive language and get to the point." a příklad verbatim:
"'Enter your first name' is clearer, more direct and natural than 'First name must have an entry'".
https://design-system.service.gov.uk/components/error-message/ ·
Tim Neusesser, Evan Sunwall, Error-Message Guidelines, NN/g, 14. 5. 2023: "Use human-readable
language", "Take a positive tone and don't blame the user", "Preserve the user's input".
https://www.nngroup.com/articles/error-message-guidelines/
**KDY NEPLATÍ:** Katastrofické selhání celého systému, kde NN/g omluvný tón naopak povoluje. Viz
sekce Chybové stavy, tam je to jiná třída chyby s jiným tónem.

### Error summary nahoře, hláška u pole, obojí stejným textem

**PRAVIDLO:** Při validační chybě zobraz souhrn nahoře nad `<h1>` s nadpisem "Je tu problém",
přesuň na něj klávesový focus, každou položku prolinkuj na příslušné pole, a **současně** nech
hlášku u pole s červeným okrajem. Text v souhrnu a u pole musí být stejný. Do `<title>` stránky dej
na začátek "Chyba: ".
**KDY PLATÍ:** Vždy, i když je chyba jen jedna.
**PROČ:** Souhrn dá přehled a je jediné místo, kde uživatel čtečky zjistí, že odeslání neprošlo,
bez procházení celé stránky. Hláška u pole dá lokální kontext. Dva různé texty pro tu samou chybu
vypadají jako dvě chyby.
**TŘÍDA:** B pro tvar komponenty, A pro požadavek, aby byla chyba identifikovaná v textu (3.3.1).
**ZDROJ:** GOV.UK Design System, Error summary, verbatim: "Always show an error summary when there
is a validation error, even if there's only one." Komponenta sama posune focus.
https://design-system.service.gov.uk/components/error-summary/ · GOV.UK, Recover from validation
errors: přidat "Error: " na začátek page title, aby to čtečka oznámila okamžitě.
https://design-system.service.gov.uk/patterns/validation/
**KDY NEPLATÍ:** Formulář s jediným polem na obrazovce, kde je souhrn duplicitní. I tak ale musí
existovat jedno místo, které čtečka oznámí.

### Krok kontroly před nevratným odesláním

**PRAVIDLO:** Před akcí s právním nebo finančním dopadem, před smazáním dat a před odesláním testu
zařaď stránku s přehledem odpovědí, kde jde každou položku změnit a vrátit se zpátky na přehled.
Nevyplněné volitelné položky zobraz jako "Nevyplněno", ne jako prázdno.
**KDY PLATÍ:** Platby, žádosti, smlouvy, mazání, cokoliv nevratného.
**PROČ:** WCAG 3.3.4 (AA) to vyžaduje pro právní a finanční transakce a pro mazání uživatelských
dat. Prakticky je to jediné místo, kde uživatel chybu z předchozích kroků ještě uvidí.
**TŘÍDA:** A pro požadavek, B pro konkrétní podobu přehledu.
**ZDROJ:** WCAG 2.2 SC 3.3.4 Error Prevention (Legal, Financial, Data), Level AA.
https://www.w3.org/WAI/WCAG22/quickref/ · GOV.UK Design System, Check answers, verbatim: "Show
a single check answers page immediately before the confirmation screen for small to medium-sized
transactions." https://design-system.service.gov.uk/patterns/check-answers/
**KDY NEPLATÍ:** Vratná akce s undo. Undo je lepší než potvrzovací dialog, protože nezdržuje.
U nevratné akce undo neexistuje a potvrzení není volitelné.

---

## Multi-step formuláře

### Jedna otázka na stránku jako výchozí volba

**PRAVIDLO:** U dlouhého nebo zřídka vyplňovaného formuláře začni s jednou otázkou na stránku.
Sdružuj jen otázky, které spolu tvoří jednu věc.
**KDY PLATÍ:** Veřejné žádosti, onboarding, cokoliv, co uživatel dělá jednou nebo dvakrát v životě.
**PROČ:** Jedna otázka na obrazovce nemá konkurenci o pozornost a chybu lze lokalizovat bez hledání.
**TŘÍDA:** B
**ZDROJ:** GOV.UK Design System, Question pages, verbatim: "Asking just one question per question
page helps users understand what you're asking them to do, and focus on the specific question and
its answer." A výjimka verbatim: "Sometimes it makes sense to group a number of related questions
on the same page." https://design-system.service.gov.uk/patterns/question-pages/
**KDY NEPLATÍ:** Interní služba, kde jde o rychlé přepínání mezi úkony (GOV.UK to jako výjimku
jmenuje sama), a formulář, který uživatel vyplňuje denně.

### 3 až 5 položek, když uživatel nese informaci mezi kroky

**PRAVIDLO:** Když uživatel musí nést hodnotu z jednoho kroku do druhého bez toho, aby ji viděl na
displeji (kód z SMS, hodnota k porovnání ve druhém tabu, součet z předchozí obrazovky), počítej
s kapacitou 3 až 5 položek, ne 7. Nad tuhle hranici hodnotu zobraz, ne po uživateli chtěj, aby si
ji pamatoval.
**KDY PLATÍ:** Jen a pouze v téhle situaci: informace není dostupná ve chvíli výbavnosti.
**PROČ:** Cowan vypisuje hraniční podmínky, za kterých je kapacitní limit vůbec měřitelný: musí být
zablokované překódování a rehearsal a podnět nesmí být dostupný při výbavnosti. Multi-step formulář
tyhle podmínky splňuje. Viditelný seznam položek je nesplňuje ani jednou, proto se pravidlo
nevztahuje na počet položek v menu.
**TŘÍDA:** B. Cowan 2001 je BBS target article, tedy syntéza s peer komentářem, **bez vlastního
vzorku**. Weinschenk, kterou se pravidlo často podpírá, ho v naivní podobě sama odmítá.
**ZDROJ:** Cowan, N. (2001). The magical number 4 in short-term memory. *Behavioral and Brain
Sciences* 24(1), 87-114, DOI 10.1017/S0140525X01003922. Abstrakt verbatim: "three to five
chunks... averaging about four chunks". Podrobný audit včetně hraničních podmínek a Weinschenkina
odmítnutí je v průzkumu fáze 1, sekce "Cowan 2001".
Návazně: [UX Laws](../zakony-principy/ux-laws.md) obsahuje starší verzi tohoto tématu jako Miller
7±2. **Ta verze je pro počet viditelných položek vyvrácená**, včetně vyjádření NN/g. Neber ji jako
oporu pro délku menu.
**KDY NEPLATÍ:** Cokoliv, co je při rozhodování vidět. Počet položek v navigaci, počet karet,
počet polí na obrazovce. Tam žádný limit 4 ani 7 neplatí.

### Progress indikátor u multi-step není samozřejmost

**PRAVIDLO:** Indikátor postupu u vícekrokového formuláře nepřidávej automaticky. Když ho přidáváš,
měj důvod. Když krokování stejně nejde odhadnout dopředu (počet kroků závisí na odpovědích),
indikátor spíš lže.
**KDY PLATÍ:** Formuláře s více než třemi kroky.
**PROČ:** Jediný publikovaný dohledaný případ ze státní služby ukazuje, že odebrání dvanáctikrokového
indikátoru nezměnilo ani dokončení, ani čas.
**TŘÍDA:** B, a slabší: jedna služba, jeden případ, publikováno vlastníkem služby.
**ZDROJ:** GOV.UK Design System, Question pages, cituje případ týmu Carer's Allowance, který
odstranil dvanáctikrokový indikátor postupu "with no effect on completion rates or times".
https://design-system.service.gov.uk/patterns/question-pages/
**KDY NEPLATÍ:** Checkout se známým pevným počtem kroků, kde indikátor slouží jako slib, že to
neskončí u pátého kroku. A dlouhý wizard, kde uživatel potřebuje vědět, jestli má začínat teď, nebo
si nachystat dokumenty.

---

## Prázdné stavy

### Prázdný stav = stav systému plus vysvětlení plus akce

**PRAVIDLO:** Prázdný kontejner nikdy nenech doslova prázdný ani neodbývej hláškou "žádná data".
Musí obsahovat tři věci: co se stalo z pohledu systému, co sem patří a proč, a klikatelnou cestu
k tomu, jak to naplnit.
**KDY PLATÍ:** Každý seznam, tabulka, panel a dashboard, který může být prázdný.
**PROČ:** Prázdný stav u nové aplikace je často první obrazovka, kterou člověk uvidí, takže je to
buď návod na první úkol, nebo mrtvý bod. Bez zprávy o stavu navíc uživatel nepozná, jestli se to
načítá, spadlo, nebo je prostě prázdno.
**TŘÍDA:** B. NN/g to opírá o příklady a heuristiky, **žádnou studii k tomu necituje**.
**ZDROJ:** Kate Kaplan, Designing Empty States in Complex Applications: 3 Guidelines, NN/g,
19. 9. 2021. Tři vodítka: komunikuj stav systému, dej kontextovou nápovědu jak prostor naplnit, dej
přímou cestu k úkonu. Příklad zprávy o stavu verbatim: "There are no records to display for the
selected date range". https://www.nngroup.com/articles/empty-state-interface-design/
**KDY NEPLATÍ:** Prázdno, které je dobrá zpráva a normální stav (inbox bez nepřečtených, nula
otevřených incidentů). Tam nepatří výzva k akci, ale potvrzení stavu.

### Rozliš tři různá prázdna

**PRAVIDLO:** "Ještě jsi nic nevytvořil", "filtr nic nenašel" a "nemáme oprávnění to zobrazit" jsou
tři různé stavy s třemi různými akcemi. Nepoužívej na ně jednu komponentu s jedním textem.
**KDY PLATÍ:** Kdykoliv má seznam filtry, oprávnění nebo onboarding fázi.
**PROČ:** Akce se v každém případě liší: vytvořit první záznam vs zrušit filtr vs požádat o přístup.
Jedna generická hláška nevede ani k jedné z nich.
**TŘÍDA:** C, řemeslná praxe. Měřený rozdíl jsem nenašel. Nepřímá opora je v tom, že NN/g žádá
komunikovat stav systému, a tyhle tři stavy jsou tři různé stavy.
**ZDROJ:** vlastní syntéza nad NN/g Empty States (výše). Neuváděj to jako doložený nález.
**KDY NEPLATÍ:** Interní jednorázový nástroj, kde jeden z těch stavů reálně nemůže nastat.

### Prázdný výsledek hledání nesmí být slepá ulička

**PRAVIDLO:** Stránka bez výsledků musí nabídnout cestu dál: související kategorie, alternativní
dotaz s náhledem výsledků, doporučení podle historie, kontakt na člověka. Rady typu "zkuste jiná
klíčová slova" jako jedinou náplň nepoužívej.
**KDY PLATÍ:** Každé hledání a filtrování nad katalogem.
**PROČ:** Chybí produkt, ne cesta. Když stránka nabídne jen tipy, uživatel odchází, protože nemá
kam kliknout. Search tipy lidé podle Baymardu skoro nečtou.
**TŘÍDA:** B, a s výhradou k metodice: Baymard je moderované think-aloud, eye-tracking a expertní
benchmark. **A/B testování ani měření konverze na živém provozu v jeho metodice není** (ověřeno
v průzkumu fáze 1), takže procenta z Baymardu ber jako popis rozšíření chyby, ne jako naměřený lift.
**ZDROJ:** Baymard Institute, 5 Proven UX Strategies For "No Results" Pages. Uvádí, že přibližně
polovina e-shopů nenabízí funkční cestu z neúspěšného hledání, a že samotné search tipy mohou
opuštění naopak zvýšit. https://baymard.com/blog/no-results-page
**KDY NEPLATÍ:** Interní vyhledávání v uzavřené množině, kde alternativa objektivně neexistuje.
Tam řekni jednoznačně, že položka neexistuje, a nenabízej náhražky.

---

## Chybové stavy

### Tři třídy chyb, tři různé tóny a tři různé akce

**PRAVIDLO:** Nezacházej se všemi chybami stejně. Rozliš:

| Třída | Kdo to způsobil | Tón | Primární akce |
|---|---|---|---|
| Validační chyba (uživatelský vstup) | uživatel, nezáměrně | neutrální imperativ, bez omluvy, bez obviňování | oprav pole, focus na první chybu |
| Systémová chyba (500, timeout, spadlá závislost) | my | krátká omluva, přiznání, že je to na nás | zkusit znovu, cesta zpět do funkční části, kontakt |
| Prázdný výsledek | nikdo, je to legitimní stav | neutrální, informativní | rozšířit dotaz, zrušit filtr, jiná cesta |

Prázdný výsledek nikdy nebarvi červeně ani nepiš jako chybu. Systémovou chybu nikdy neformuluj jako
by ji způsobil uživatel.
**KDY PLATÍ:** Vždy, každé rozhraní.
**PROČ:** U validace uživatel může něco udělat hned, takže hláška je instrukce. U systémové chyby
udělat nemůže nic, takže hláška je informace plus cesta ven, a tam má omluva smysl. U prázdného
výsledku se nestalo nic špatného, takže signalizovat chybu je lež.
**TŘÍDA:** B pro validační a systémovou vrstvu, C pro tuhle konkrétní trojtabulku (moje syntéza).
**ZDROJ:** GOV.UK Design System, Error message: u validačních chyb explicitně nepoužívat "sorry",
"because it does not help fix the problem".
https://design-system.service.gov.uk/components/error-message/ ·
NN/g Error-Message Guidelines: u totálního selhání systému naopak omluvný tón povoluje.
https://www.nngroup.com/articles/error-message-guidelines/
Tenhle rozpor není rozpor, je to důkaz, že třídy chyb jsou různé.
**KDY NEPLATÍ:** Chyba, kterou způsobil uživatel záměrně a opakovaně (rate limit, pokus o zneužití).
Tam je tón faktický a hláška nemusí vysvětlovat mechanismus.

### Žádný technický žargon a žádný stack trace na povrch

**PRAVIDLO:** Uživatel nikdy nevidí kód výjimky, název třídy, SQL, ID transakce bez vysvětlení ani
"unspecified error". Když potřebuješ korelační ID pro podporu, napiš to a označ to jako údaj pro
podporu.
**KDY PLATÍ:** Každá chyba viditelná koncovým uživatelem.
**PROČ:** Technická hláška nedává akci a zvyšuje pocit, že produkt je rozbitý.
**TŘÍDA:** B
**ZDROJ:** GOV.UK Design System, Error message: nepoužívat "technical jargon like 'form post error',
'unspecified error'". https://design-system.service.gov.uk/components/error-message/ ·
NN/g Error-Message Guidelines: "Use human-readable language".
https://www.nngroup.com/articles/error-message-guidelines/
**KDY NEPLATÍ:** Nástroj pro vývojáře, kde je stack trace ten obsah, který uživatel chce. I tam ale
patří pod rozbalení, ne jako hlavní zpráva.

### Změnu stavu musí oznámit i čtečka, bez přesunu focusu

**PRAVIDLO:** Hlášky "Hledám", "Nalezeno 18 výsledků", "Nic nenalezeno", "Uloženo", "Nahrávání 40 %"
musí být v oblasti, kterou čtečka oznámí sama, bez toho, aby na ni skočil focus.
**KDY PLATÍ:** Každý asynchronní stav, který se propíše do UI bez přenačtení stránky.
**PROČ:** WCAG 4.1.3 (AA) to vyžaduje. Vizuální uživatel změnu vidí, uživatel čtečky ne, a přesun
focusu by mu naopak sebral místo, kde je.
**TŘÍDA:** A
**ZDROJ:** WCAG 2.2 SC 4.1.3 Status Messages, Level AA, nové v 2.1, verbatim: "In content
implemented using markup languages, status messages can be programmatically determined through role
or properties such that they can be presented to the user by assistive technologies without
receiving focus." Understanding uvádí jako příklady přímo "Searching...", "18 results returned",
"No results returned". https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html
**KDY NEPLATÍ:** Validační chybový souhrn po odeslání. Tam focus přesunout MÁŠ, viz pravidlo
o error summary. 4.1.3 se týká stavů, které nejsou reakcí na explicitní odeslání.

---

## Loading stavy

### Tři prahy čekání

**PRAVIDLO:** Pracuj se třemi hranicemi: 0,1 s (odezva vnímaná jako okamžitá), 1 s (nepřerušený tok
myšlení, ale už je vhodná zpětná vazba), 10 s (hranice udržení pozornosti u úkonu, nad ni potřebuje
uživatel vědět, kdy to skončí, a možnost dělat něco jiného).
**KDY PLATÍ:** Návrh každého stavu, který na něco čeká.
**PROČ:** Nejde o estetiku, jde o to, kdy člověk přestane věřit, že se něco děje.
**TŘÍDA:** B. Nielsen to kompiluje z cizí práce (Miller 1968, Card et al. 1991, Myers 1985), není to
jeho vlastní měření.
**ZDROJ:** Jakob Nielsen, Response Times: The 3 Important Limits, NN/g, 1. 1. 1993, kapitola 5
knihy *Usability Engineering*. Verbatim: 0,1 s je "the limit for having the user feel that the
system is reacting instantaneously", 1,0 s "the limit for the user's flow of thought to stay
uninterrupted", 10 s "the limit for keeping the user's attention focused on the dialogue".
https://www.nngroup.com/articles/response-times-3-important-limits/
**KDY NEPLATÍ:** Dávkové zpracování, u kterého uživatel dopředu ví, že běží minuty. Tam se řeší
notifikace po dokončení, ne indikátor.

### Který indikátor při jaké délce

**PRAVIDLO:** Pod 1 s nedávej nic. 2 až 10 s: smyčkovaná animace (spinner). Nad 10 s: procentní
indikátor postupu. Statický indikátor ("Načítám...", který se nehýbe) nepoužívej.
**KDY PLATÍ:** Vždy, když čekání odhadneš dopředu.
**PROČ:** Smyčka pod 1 s je rušivá, protože blikne a zmizí. Smyčka nad 10 s nenese informaci o tom,
kdy to skončí, takže uživatel neví, jestli se to zaseklo.
**TŘÍDA:** B
**ZDROJ:** Katie Sherwin, Progress Indicators Make a Slow System Less Insufferable, NN/g,
26. 10. 2014. Verbatim: "This indicator should be reserved for actions that take between 2-10
seconds", "Percent-done progress indicators should be used for longer processes that take 10 or
more seconds", "static indicators should be replaced with another type of indicator, because they do
not offer enough information". Cituje Nah, F. (2004), *Behaviour and Information Technology* 23(3),
studii o tolerovatelné době čekání. https://www.nngroup.com/articles/progress-indicators/
**KDY NEPLATÍ:** Když délku neznáš a může být 0,3 s i 30 s. Pak dej indikátor s odkladem (zobraz ho
až po ~500 ms), aby u rychlé odpovědi neblikl.

### Progress bar: víc menších kroků působí rychleji

**PRAVIDLO:** Když děláš indikátor postupu, animuj ho v hodně malých krocích, ne ve pár velkých
skocích. Skoky po 25 % působí pomaleji než plynulý běh.
**KDY PLATÍ:** Procentní indikátory a upload/download progress.
**PROČ:** Vnímaná doba závisí na frekvenci vizuálních událostí, ne na skutečné rychlosti pohybu.
Vyšší počet kroků vede k podhodnocení uplynulého času.
**TŘÍDA:** A. Je to peer-reviewed, čtyři experimenty, ale malé vzorky.
**ZDROJ:** Ziat, M., Saoud, W., Prychitko, S., Servos, P., Grondin, S. (2022). Malleability of time
through progress bars and throbbers. *Scientific Reports* 12, 10400, DOI 10.1038/s41598-022-14649-1.
N = 20 / 11 / 21 / 16 podle experimentu, testované délky 3, 4, 5 s a 10, 12, 14 s. Verbatim: "Higher
number of steps produced the impression of a faster progression leading to an underestimation of
time, whereas a progression in large fewer steps... produced slower apparent progression, creating
the illusion of dilated time." https://pmc.ncbi.nlm.nih.gov/articles/PMC9213475/
Navazuje na Harrison, C., Amento, B., Kuznetsov, S., Bell, R. (2007). Rethinking the progress bar.
UIST '07, 115-118, DOI 10.1145/1294211.1294231, a Harrison, C., Yeo, Z., Hudson, S. E. (2010).
Faster Progress Bars: Manipulating Perceived Duration with Visual Augmentations. CHI '10, 1545-1548,
DOI 10.1145/1753326.1753556. **Konkrétní procentní zlepšení z těchto dvou prací jsem neověřil
z primárního textu, koluje číslo 11 %, necituj ho.**
**KDY NEPLATÍ:** Když skutečný postup skáče, protože práce má nestejně dlouhé fáze. Falešně plynulý
běh, který na 90 % zatuhne, je horší než pravdivé skoky.

### Skeleton screen je konvence, ne měřená výhoda

**PRAVIDLO:** Skeleton screen používej, když chceš předem sdělit tvar obsahu, který přijde, a když
je layout stabilní. Nepoužívej ho s odůvodněním, že je prokazatelně rychlejší, a hlavně ne jako
náhradu za zkrácení skutečné doby načítání.
**KDY PLATÍ:** Rozhodování mezi spinnerem a skeletonem u načítání obsahu.
**PROČ:** Jediná dohledaná kontrolovaná studie, která skeleton srovnává se spinnerem a s prázdnou
obrazovkou při stejné délce, ho má nejhorší ve všech měřených metrikách. Populární tvrzení, že
skeleton působí až o polovinu rychleji, se mi nepodařilo dovést k primárnímu zdroji, takže ho
nepoužívej.
**TŘÍDA:** B pro nález proti skeletonu (publikovaný experiment, N = 136, ale ne peer-reviewed
a autoři sami relativizují). C pro samotné doporučení, kdy skeleton použít.
**ZDROJ:** Kathryn Faulkner, Katherine Olvera, A Bone to Pick with Skeleton Screens, Viget,
19. 10. 2017. N = 136 (70 z Mechanical Turku, zbytek organicky), mobilní test, tři animované GIFy
stejné délky: skeleton, spinner, prázdná obrazovka. Průměrná vnímaná doba čekání: skeleton 2,82 s,
spinner 2,41 s, prázdná 2,29 s. "Načetlo se to rychle" odsouhlasilo 59 % u skeletonu, 74 %
u spinneru, 66 % u prázdné. Vlastní výhrada autorek verbatim: "More testing is needed to know for
certain" a "Skeleton screens aren't a silver bullet for increasing perceived performance."
https://www.viget.com/articles/a-bone-to-pick-with-skeleton-screens
**KDY NEPLATÍ:** Známé, opakovaně navštěvované rozhraní (feed, seznam konverzací), kde uživatel tvar
obsahu zná a skeleton mu potvrdí, že jde o to samé místo. Autorky studie samy uvádějí, že skeleton
může fungovat lépe ve známém prostředí a u velmi krátkých čekání.

### Skeleton nesmí po načtení přeskládat layout

**PRAVIDLO:** Skeleton musí mít stejné rozměry a stejný počet prvků jako obsah, který ho vystřídá.
Když se po načtení něco posune, je skeleton horší než prázdné místo.
**KDY PLATÍ:** Vždy, když skeleton použiješ.
**PROČ:** Posun obsahu po načtení znamená, že uživatel klikne na něco jiného, než na co míří.
**TŘÍDA:** C, řemeslná praxe. Přímý zdroj na to jako pravidlo jsem nenašel, opora je nepřímá
(posunující se layout je Core Web Vitals metrika CLS, což je vývojářský, ne UX výzkum).
**ZDROJ:** vlastní praxe, neuváděj jako doložený nález.
**KDY NEPLATÍ:** Obsah s principiálně neznámou výškou (uživatelský text různé délky). Tam raději
rezervuj minimální výšku a přiznej, že se doplní.

---

## Co tahle nota nepokrývá

- Vizuální podobu polí a tlačítek. To je jinde v knihovně, viz index.
- Copy delší než chybová hláška a mikrocopy. Viz
  [Content strategy a UX writing](../ux-zaklady/content-strategy-ux-writing.md).
- Markery generického vzhledu, včetně bezokrajových polí a "oops" hlášek. Viz
  [anti-slop](anti-slop.md).
- Konkrétní implementaci formuláře v HTML. `web-dev/html-a-css.md` má jen základy značek, ne
  formulářové vzory. Rozvržení formuláře drží
  [Skladba formuláře](../../enterprise-ui/vzory/formular-skladba.md), drátování labelů a chyb pro
  čtečky [Oznámení pro čtečky](../../enterprise-ui/zaklady/oznameni-pro-ctecky.md).

## Nedořešené mezery

1. **Konflikt validačního timingu není rozřešený.** GOV.UK zakazuje validaci na blur, Wroblewski
   a Baymard ji doporučují. Rozdíl je pravděpodobně v publiku (nesegmentovaná populace vs zákazník
   e-shopu) a v typu pole, ale kontrolované srovnání napříč populacemi jsem nenašel.
2. **Empty states nemají žádnou měřenou oporu.** Ani NN/g necituje studii. Všechno v té sekci je B
   nebo C.
3. **Chybí evidence k počtu polí.** Tvrzení typu "každé pole navíc snižuje konverzi o X %" jsem
   nedohledal k primárnímu zdroji a v téhle notě proto není.
4. **Skeleton screens mají jednu studii proti a nulu doložených pro.** Pozitivní čísla, která kolují
   (Facebook, "o 50 % rychlejší"), se mi nepodařilo dovést ke zdroji.
