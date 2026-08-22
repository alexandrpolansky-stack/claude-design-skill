# Navigace v hierarchii: drobenka a indikátor postupu

Dvě komponenty, které odpovídají na dvě různé otázky: „kde jsem" a „jak daleko jsem".

Související: [Volba komponenty](../zaklady/volba-komponenty.md) · [Taby](taby.md) ·
[Formulář: skladba](../vzory/formular-skladba.md) · [Stavové indikátory](../vzory/stavove-indikatory.md) ·
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md)

---

## Rychlé rozhodnutí

1. **Hierarchie hlubší než dvě úrovně = drobenka.** Dvouúrovňová navigace drobenku nepotřebuje,
   vytváří jen zmatek.
2. **Vícekrokový proces = indikátor postupu, ne drobenka.** Carbon to říká explicitně.
3. **Indikátor postupu až od tří kroků.** Pod tři kroky ne. Když může proces jít v jakémkoli pořadí,
   taky ne. Když se počet kroků mění podle podmínek, taky ne.
4. **Drobenka je vždycky sekundární** a nikdy nenahrazuje primární navigaci.
5. **Aktuální stránka v drobence výchozím stavem není.** Když ji zařadíš, je poslední a **není odkaz**.
6. **Drobenka se nikdy nezalamuje na druhý řádek.** Při nedostatku místa první + poslední dva odkazy
   a zbytek do overflow menu.
7. **Na mobilu začíná drobenka overflow menu**, po něm jedna drobenka.
8. **Indikátor postupu radši vertikálně**, když to jde.
9. **Krok validuj, než uživatele pustíš dál.**
10. **Drobenka je `<nav>` se seznamem odkazů**, ne řada divů s lomítky.

---

## Která komponenta na co

| Otázka uživatele | Komponenta |
|---|---|
| „Kde jsem v informační architektuře a jak se dostanu o úroveň výš?" | **Drobenka** |
| „Kolik kroků procesu mám za sebou a kolik před sebou?" | **Indikátor postupu** |
| „Jaký pohled na tenhle jeden obsah si mám vybrat?" | **Taby**, viz [Taby](taby.md) |

Carbon k rozhraní mezi prvními dvěma říká přímo: **„If you are taking users through a multistep
process use a progress indicator instead."**

**ZDROJ:** Carbon, Breadcrumb usage, When not to use.
https://carbondesignsystem.com/components/breadcrumb/usage/

**Rozdíl proti tabům:** taby přepínají pohled na **stejný obsah na stejné úrovni**, drobenka ukazuje
**cestu mezi úrovněmi**, indikátor postupu ukazuje **pozici v čase**. Když si nejsi jistý, zeptej se,
jestli mezi položkami existuje pořadí. Taby pořadí nemají, kroky ho mají, úrovně hierarchie ho mají.

---

# Drobenka (breadcrumb)

Sekundární navigační vzor, který uživateli pomůže **porozumět hierarchii mezi úrovněmi a navigovat
zpátky skrz ně**. Drobenka ukazuje aktuální umístění vůči informační architektuře a nechá uživatele
rychle přejít **o úroveň výš nebo na předchozí krok**.

## Kdy použít a kdy ne

**PRAVIDLO:** Drobenka je účinná v produktech a prostředích, které mají **velké množství obsahu
organizované v hierarchii o víc než dvou úrovních**. Zabere málo místa a přitom dá kontext o místě
uživatele v navigační hierarchii.
**KDY NEPLATÍ:** **Nepoužívej drobenku u produktů, které mají jednoúrovňovou navigaci**, protože
vytváří nadbytečný zmatek.
**TŘÍDA:** B
**ZDROJ:** Carbon, Breadcrumb usage, When to use / When not to use, verbatim: „They shouldn't be used
for products that have single level navigation because they create unnecessary clutter."
https://carbondesignsystem.com/components/breadcrumb/usage/

**PRAVIDLO:** Drobenka je **vždy sekundární** a **nikdy nemá úplně nahradit primární navigaci**.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Breadcrumb usage, When not to use, verbatim: „Breadcrumbs are always treated as
secondary and should never entirely replace the primary navigation."
https://carbondesignsystem.com/components/breadcrumb/usage/

## Dva typy a proč si musíš vybrat jeden

| Typ | Co ukazuje |
|---|---|
| **Location-based** | Ilustruje **hierarchii webu** a ukazuje uživateli, kde v té hierarchii je |
| **Path-based** | Ukazuje **skutečné kroky, kterými se uživatel na aktuální stránku dostal**, ne informační architekturu. Path-based drobenka je vždy generovaná dynamicky |

**PRAVIDLO:** Oba typy jsou stylované stejně, ale způsob plnění drobenky je jiný. **Použitý typ musí
být konzistentní napříč produktem.**
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Breadcrumb usage, Types, verbatim: „The breadcrumb type used should be consistent
across a product." https://carbondesignsystem.com/components/breadcrumb/usage/

**Praktický důsledek:** protože jsou vizuálně nerozlišitelné, uživatel se z pohledu nedozví, jestli
mu drobenka slibuje strukturu, nebo historii. Když v jedné aplikaci mícháš oba typy, sliboval jsi
oboje a splnil jsi jedno. **Rozhodni typ jednou pro celý produkt a zapiš to.**

## Anatomie a velikosti

**Dva prvky:** 1. **odkaz na stránku** (vede na nadřazenou stránku), 2. **oddělovač** (jasně odděluje
jednotlivé stránky).

| Velikost | Kdy |
|---|---|
| **Small** | Běžně v **hlavičkách stránek**. Taky ve stísněných prostorech a na menších breakpointech. Nebo když ladíš vyváženou hierarchii obsahu a potřebuješ menší drobenku k tomu, s čím ji páruješ |
| **Medium** | Typicky **když hlavička stránky není** a drobenka je na začátku stránky. **Medium je výchozí velikost** |

**ZDROJ:** Carbon, Breadcrumb usage, Sizing. Carbon k velikostem uvádí konkrétní typografické tokeny,
ty záměrně nepřebírám. https://carbondesignsystem.com/components/breadcrumb/usage/

## Umístění

**PRAVIDLO:** Drobenka je v **levé horní části stránky**. Sedí **pod hlavičkou a navigací, ale nad
titulkem stránky**.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Breadcrumb usage, Placement, verbatim: „They sit underneath the header and
navigation, but above the page title."
https://carbondesignsystem.com/components/breadcrumb/usage/

## Obsah odkazů

- Každý odkaz má být **krátký** a **jasně odrážet umístění nebo entitu**, na kterou vede.
- **Začni nejvyšší nadřazenou stránkou** a postupuj hlubší do informační architektury, jak drobenka
  pokračuje.
- **Aktuální stránka výchozím stavem v drobence není.**

**PRAVIDLO:** Když stránka **nemá titulek** nebo **aktuální stránka není jasná**, může být aktuální
stránka do drobenky zařazená. Pak je **vždy poslední text v pořadí a není interaktivní odkaz**.
**KDY PLATÍ:** Jen v těch dvou situacích. Výchozí stav je aktuální stránku neuvádět.
**TŘÍDA:** B
**ZDROJ:** Carbon, Breadcrumb usage, Page link a Modifiers.
https://carbondesignsystem.com/components/breadcrumb/usage/

## Přetečení a zkracování

**PRAVIDLO:** Když je místa málo, použij **overflow menu** ke zkrácení drobenky. Zobraz **první
a poslední dva** odkazy, **zbylé drobenky mezi nimi sbal do overflow menu**. **Drobenka se nikdy nemá
zalomit na druhý řádek.**
**KDY PLATÍ:** Vždy při nedostatku místa.
**TŘÍDA:** B
**ZDROJ:** Carbon, Breadcrumb usage, Overflow content, verbatim: „The first and last two page links
should be shown, but the remaining breadcrumbs in between are condensed into an overflow menu.
Breadcrumbs should never wrap onto a second line."
https://carbondesignsystem.com/components/breadcrumb/usage/

**PRAVIDLO:** Na **větších breakpointech** drž **první domovský odkaz co nejdéle**, i když už je
overflow přítomné. Na **mobilu a malých viewportech začni overflow menu**, po něm následuje **jedna
drobenka**.
**KDY PLATÍ:** Vždy v responzivním chování.
**TŘÍDA:** B
**ZDROJ:** Carbon, Breadcrumb usage, Truncation, verbatim: „Also for mobile or small viewpoints, start
with the overflow first, following by one breadcrumb."
https://carbondesignsystem.com/components/breadcrumb/usage/
Souvislost: [Přetečení a truncation](../vzory/preteceni-a-truncation.md),
[2x grid a breakpointy](../zaklady/2x-grid-a-breakpointy.md).

**Proč zachovávat domovský odkaz:** je to jediný odkaz, který má konstantní význam nezávisle na tom,
kde uživatel je. Když ho sbalíš do overflow, ztratí uživatel jediný spolehlivý únikový bod.
Poznámka: tohle je moje odůvodnění, Carbon k tomu důvod neuvádí, jen pravidlo. **TŘÍDA: C.**

## Interakce a klávesová obsluha

**Všechny stránky v drobence mají být interaktivní** (kromě aktuální) a vést na své stránky.
**Oddělovače nejsou interaktivní.**

| Vstup | Chování |
|---|---|
| Myš | Kliknutí na odkaz. Oddělovače nejsou klikatelné |
| Klávesnice | Mezi odkazy `Tab` a `Shift-Tab`, aktivace `Enter` |
| Overflow | Když je drobenka zkrácená, **tlačítko s výpustkou je v tab orderu** |

**ZDROJ:** Carbon, Breadcrumb usage, Interactions a Breadcrumb accessibility, Keyboard interactions.
https://carbondesignsystem.com/components/breadcrumb/accessibility/

## Struktura pro čtečku

**PRAVIDLO:** Každý odkaz implementuj jako **položku nesetříděného seznamu** uvnitř **navigační
oblasti pojmenované „breadcrumb"**. Carbon používá HTML element `<nav>`, jde to i landmarkem
„navigation" na `<div>`. Tlačítko s výpustkou má přístupný název **„more breadcrumbs"**.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Breadcrumb accessibility, Labeling and regions a Development considerations.
Odůvodnění Carbonu k seznamu, verbatim: „Each link in the breadcrumb is implemented as an unordered
list item so that screen readers provide more context."
https://carbondesignsystem.com/components/breadcrumb/accessibility/

**Vizuální oddělovače nemusí být text.** Carbon je dělá CSS a **nejsou určené k navigaci**. Když je
uděláš jako text v DOM, čtečka je bude předčítat mezi každou položkou.

Detail: [Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md).

---

# Indikátor postupu (progress indicator)

Vede uživatele **jakoukoli lineární, vícekrokovou úlohou** tím, že ukazuje dokončené, aktuální
a budoucí kroky. Řídí očekávání: ukazuje, na kterém kroku uživatel je, **celkový počet kroků**
a celkový postup v dokončení úlohy.

## Kdy použít

Carbon jmenuje čtyři situace:

1. Když uživatel prochází **lineárním procesem, který se dá rozdělit do tří nebo víc kroků**.
2. Když uživateli pomůže **porozumět svému postupu v dlouhých formulářích**, například e-shopová
   kasa, onboarding, žádost o vízum.
3. Když se mají **uživatelské vstupy validovat před postupem na další krok**.
4. K **doplnění standardní navigace zpět a dál** v lineární posloupnosti.

**ZDROJ:** Carbon, Progress indicator usage, When to use.
https://carbondesignsystem.com/components/progress-indicator/usage/

**Konflikt s knihovnou: indikátor postupu není samozřejmost.** Carbon ho výše u dlouhých formulářů
a onboardingu doporučuje. Knihovna má v
[Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md), sekce „Progress indikátor
u multi-step není samozřejmost", pravidlo **nepřidávej automaticky, měj důvod**, opřené o případ
týmu Carer's Allowance, který dvanáctikrokový indikátor odebral „with no effect on completion rates
or times".

**Tenhle spor nevyhrává knihovna automaticky.** Obě strany jsou třída B a knihovna svůj zdroj sama
označuje za slabší (jedna služba, jeden případ, publikoval ho vlastník služby). Rozhoduje se podle
toho, co indikátor slibuje:

| Situace | Co udělat | Proč |
|---|---|---|
| Pevný a dopředu známý počet kroků (kasa, onboarding na čtyři kroky) | Indikátor **ano** | Nese slib „skončí to u čtvrtého", a ten slib dodržíš. Carbon i knihovna se tu shodnou, viz „KDY NEPLATÍ" v pravidle knihovny |
| Dlouhý wizard, kde si uživatel potřebuje nachystat podklady | Indikátor **ano** | Odpovídá na „mám do toho jít teď?" |
| Počet kroků závisí na odpovědích | Indikátor **ne** | Slib porušíš, tři z pěti se změní na tři ze sedmi. Platí i pro dynamický počet |
| Dlouhá řada krátkých otázek bez jasného konce | **Zvaž odebrání** | Tady měřený případ ukazuje, že indikátor nic nepřidal |

Krátce: **rozhoduje předvídatelnost počtu kroků, ne jejich počet.**

## Kdy nepoužít

**PRAVIDLO:** Nepoužívej indikátor postupu, když:
- proces nebo formulář má **méně než tři kroky**,
- proces se dá dokončit **v jakémkoli pořadí**,
- **počet kroků se může měnit** podle podmíněné logiky.

**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Progress indicator usage, When not to use.
https://carbondesignsystem.com/components/progress-indicator/usage/

**Praktický důsledek pro třetí bod:** indikátor postupu slibuje **konečný a známý počet kroků**.
Když se počet mění podle toho, co uživatel vyplní, ten slib porušíš a uživatel má za sebou tři kroky
z pěti, které se najednou proměnily v tři ze sedmi. **Když počet kroků neznáš dopředu, indikátor
postupu nepoužívej, ani s dynamickým počtem.**

**Souvislost:** vícekrokové formuláře a jejich skladba jsou v
[Formulář: skladba](../vzory/formular-skladba.md). Progres bar u lineárních cest ve stránkování
nepatří, viz [Stránkování](strankovani.md).

## Anatomie: pět prvků

1. **Stavový indikátor:** komunikuje, jestli je krok dokončený, aktuální, nezapočatý, disabled nebo
   má chybu.
2. **Aktivní čára kroku:** označuje dokončené kroky a krok, na kterém uživatel je.
3. **Label:** komunikuje, co uživatel v každém kroku splní. **Číslování kroků dělá postup zřejmější.**
4. **Neaktivní čára kroku:** označuje nezapočaté kroky a taky kroky v chybě, disabled nebo ve
   skeleton stavu.
5. **Helper text:** označuje krok jako volitelný nebo v chybovém stavu.

**ZDROJ:** Carbon, Progress indicator usage, Anatomy.
https://carbondesignsystem.com/components/progress-indicator/usage/
Ke stavovému indikátoru Carbon odkazuje na vlastní vzor, detail:
[Stavové indikátory](../vzory/stavove-indikatory.md).

## Zarovnání a umístění

**PRAVIDLO:** Indikátor postupu může být vertikální nebo horizontální podle případu použití
a struktury UI. **Když to jde, uspořádej ho vertikálně, kvůli snazšímu čtení.**
**TŘÍDA:** B
**ZDROJ:** Carbon, Progress indicator usage, Alignment, verbatim: „When possible, arrange the progress
indicator vertically for easier reading."
https://carbondesignsystem.com/components/progress-indicator/usage/

**Kam se dá umístit:** na **plnou stránku**, do **modálu**, do **side panelu**. Carbon dodává, že je
běžné použít ho i v tearsheetu (komponenta z IBM Products).

Souvislost: [Dialogy a panely](../vzory/dialogy-a-panely.md).

## Label a helper text

**PRAVIDLO:** Label má komunikovat, co uživatel v každém kroku splní, **v jednom nebo dvou slovech**.
Jedna možnost je jasně označit akci kroku formulkou **{verb} + {noun}**, například „Configure IdP"
nebo „Define endpoints". Label může mít **jedno slovo, když je univerzálně pochopitelné**, například
„Košík", „Doprava", „Platba". **Vyhni se vágním termínům jako „Zpracování".** Kroky můžeš navíc
**očíslovat**, aby byl postup zřejmější.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Progress indicator usage, Label. Vágní termín, který Carbon uvádí jako příklad
čeho se vyhnout, je verbatim „Processing".
https://carbondesignsystem.com/components/progress-indicator/usage/
Detail k formulce a k tomu, co z ní platí v češtině:
[UX copy v produktu](../zaklady/ux-copy-v-produktu.md).

**Helper text** používej k označení, že je krok **volitelný**, nebo že je **v chybovém stavu**.

**Přetečení:**

| Prvek | Co dělat při nedostatku místa |
|---|---|
| Label | **Přeformuluj**, nebo zkrať výpustkou a **dej tooltip** s doplňující informací |
| Helper text | **Radši zalomení na druhý řádek než zkrácení.** Zalom pod label, aby si oba držely zarovnání vlevo |

**ZDROJ:** Carbon, Progress indicator usage, Overflow content.
https://carbondesignsystem.com/components/progress-indicator/usage/
Souvislost: [Tooltip a toggletip](tooltip-a-toggletip.md),
[Přetečení a truncation](../vzory/preteceni-a-truncation.md).

## Sedm stavů

| Stav | Kdy nastává |
|---|---|
| **Completed** | Uživatel vyplnil požadované informace v kroku a postoupil na následující. **Když to jde, potvrď dokončení kroku validací, než uživatel pokračuje** |
| **Current** | Uživatel právě pracuje s informacemi v tom kroku |
| **Not started** | Uživatel s krokem ještě neinteragoval: kroky, na které ještě nedošel, nebo budoucí kroky |
| **Error** | Uživatel zadal **neplatné nebo nekompletní** informace. Může jít i o chybu na straně serveru. **Dej jasnou informaci o chybě a vodítko, jak ji vyřešit** |
| **Disabled** | Odebrané všechny interaktivní funkce |
| **Hover** | Kurzor myši je nad krokem indikátoru |
| **Focus** | Uživatel na krok tabnul nebo klikl |

**ZDROJ:** Carbon, Progress indicator usage, States.
https://carbondesignsystem.com/components/progress-indicator/usage/

**Carbonova definice disabled, kterou stojí za to citovat celou:** „Unlike read-only states, disabled
states are not focusable, are not read by screen readers, and do not need to pass visual contrast,
making them inaccessible if they need to be interpreted." Tohle je přesně důvod, proč disabled krok
v indikátoru postupu **nesmí nést informaci, kterou uživatel potřebuje**. Detail:
[Disabled vs. read-only](../vzory/disabled-vs-read-only.md).

## Interaktivní varianta

**Výchozím stavem indikátor postupu interaktivní není**, dává jen vizuální aktualizaci postupu
uživatele. Existuje **volba interaktivního indikátoru**, který uživateli dovolí navigovat na každý krok.

| Vstup | Chování v interaktivní variantě |
|---|---|
| Myš | Kliknutí **kdekoli v kontejneru labelu kroku** |
| Klávesnice | **První krok je vybraný výchozím stavem.** Mezi kroky se navigují **šipky `Right` a `Left`** |

**ZDROJ:** Carbon, Progress indicator usage, Interactions.
https://carbondesignsystem.com/components/progress-indicator/usage/

**Klávesový model:** je to složená komponenta. Tab do ní, šipky uvnitř. Stejný model jako taby.
Detail: [Klávesnice a focus](../zaklady/klavesnice-a-focus.md).

## Validace

**PRAVIDLO:** Když to jde, **potvrď validací, že je krok dokončený, než uživatel pokračuje**. Když je
kterýkoli vstup neplatný, indikátor postupu má **ukázat chybový stav**. Navíc má být neplatný vstup
označený chybovým stavem a mít **inline chybovou zprávu**, která uživateli pomůže porozumět problému
a jak ho spravit. Když uživatel nemůže pokračovat kvůli **problému na straně serveru**, má se objevit
**inline notifikace**.
**KDY PLATÍ:** Vždy u vícekrokových formulářů.
**TŘÍDA:** B
**ZDROJ:** Carbon, Progress indicator usage, Validation.
https://carbondesignsystem.com/components/progress-indicator/usage/

**Konflikt s knihovnou k načasování validace:** Carbon tady říká, že inline (client-side) validace
má proběhnout **jakmile pole opustí focus**. Knihovna má v
[`ux-design/pravidla/formulare-a-stavy.md`](../../ux-design/pravidla/formulare-a-stavy.md) opačné
výchozí nastavení: **validovat při odeslání** (GOV.UK). **Knihovna vyhrává**, protože má tvrdší zdroj
z veřejných služeb. Carbonova pozice je legitimní u enterprise produktů s vlastním výzkumem, ale není
to výchozí volba. Stejný konflikt je popsaný podrobněji v
[Formulář: skladba](../vzory/formular-skladba.md).

## Přístupnost

Carbon říká, že u indikátorů postupu **nejsou potřeba přístupnostní anotace**, ale uvádí dvě
uvažování pro vlastní implementaci:

1. **Text odkazu** je viditelný label nativního HTML odkazu a slouží k tomu, aby byl **účel odkazu
   jasný a snadno pochopitelný pro všechny uživatele**.
2. **Labely jsou jasné, stručné a obsahují stav každého kroku.**

Carbon k tomu odkazuje na **W3C Web Accessibility Tutorial for Multi-Page Forms** a jmenuje
tyhle WCAG kritéria: **1.3.1 Info and Relationships**, **1.3.2 Meaningful Sequence**, **2.1.1
Keyboard**, **2.4.3 Focus Order**, **2.4.6 Headings and Labels**, **2.4.7 Focus Visible**,
**4.1.2 Name, Role, Value**.

**ZDROJ:** Carbon, Progress indicator accessibility.
https://carbondesignsystem.com/components/progress-indicator/accessibility/
W3C tutoriál: https://www.w3.org/WAI/tutorials/forms/multi-page/
Detail: [Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md).

**Praktický důsledek druhého bodu:** stav kroku nesmí být jen tvar kolečka. „Krok 2 z 5, Doprava,
dokončeno" musí být v přístupném názvu, ne jen v grafice. Souvislost:
[Stavové indikátory](../vzory/stavove-indikatory.md), kde je pravidlo, že stav nikdy nenes jedním
kanálem.

---

## Co tahle nota neřeší

- **Primární a globální navigaci** (UI shell header, levá navigace, global header). Carbon je má
  v samostatných komponentách a vzorech, v přečtené kopii k nim nic není.
- **Overflow menu** jako komponentu. Zmiňuju jen její roli v zkrácené drobence.
- **Tearsheet.** Komponenta z IBM Products, v přečtené kopii není.
- **Progress bar** jako indikátor průběhu operace, který není o krocích. To je jiná komponenta,
  patří k [Načítání a čekání](../vzory/nacitani-a-cekani.md).
- **Skeleton stav** indikátoru postupu. Carbon ho jmenuje v anatomii, ale nepopisuje. Postoj knihovny
  ke skeletonům je v [Načítání a čekání](../vzory/nacitani-a-cekani.md).
- Tokeny, výšky a barvy. Carbon je má na stránkách `style`, záměrně je nepřebírám.

## Zdroj

IBM Carbon Design System, lokální kopie přečtená 30. 7. 2026:
- Breadcrumb usage a Breadcrumb accessibility.
  https://carbondesignsystem.com/components/breadcrumb/usage/
- Progress indicator usage a Progress indicator accessibility.
  https://carbondesignsystem.com/components/progress-indicator/usage/

Carbon u obou komponent neuvádí sekci References, žádné externí zdroje k nim nemá. Jeho doporučení
jsou **třída B**. Odkazovaná WCAG kritéria a W3C tutoriál jsou **třída A** (normativní text
a oficiální dokumentace W3C). Odůvodnění o domovském odkazu je moje, **třída C**, a je označené
v místě.
