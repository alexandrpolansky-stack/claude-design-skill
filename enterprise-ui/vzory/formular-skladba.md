# Skladba formuláře v enterprise produktu

Rozvržení, sekce, mezery, poloha tlačítek a technika pro dlouhé formuláře.

**Přečti si nejdřív** [Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md). Ta má
labely, placeholder, validaci a chybové hlášky s tvrdšími zdroji (WCAG, GOV.UK) a je nadřazená všude,
kde si s Carbonem odporují. Tahle nota přidává to, co tam není: kompozici formuláře, mezery, polohu
tlačítek a rozlišení jednoduchý versus komplexní formulář.

Související: [Dialogy a panely](dialogy-a-panely.md) · [Textová pole](../komponenty/textova-pole.md) ·
[Výběr ze seznamu](../komponenty/vyber-ze-seznamu.md) · [Běžné akce](bezne-akce.md)

---

## Rychlé rozhodnutí

1. Jeden sloupec je default. Dva až tři vstupy na řádek jen tehdy, když logicky patří k sobě.
2. Vstupů pod pět = dialog. Nad pět = boční panel. Složité nebo dlouhé = celá stránka.
3. Většina polí povinná? Označ **jen volitelná**. Většina volitelná? Označ **jen povinná**. A drž to
   konzistentně v celém produktu.
4. Tlačítka **vždycky dole**, nikdy nahoře.
5. Poloha primárního tlačítka: in-page formulář = **vlevo**. Wizard, dialog, boční panel = **vpravo**.
6. Label tlačítka konkrétně, ne „Odeslat".
7. Krátký formulář se serverovou validací: primární tlačítko můžeš držet disabled. **Dlouhý ne.**
8. Po odeslání primární tlačítko disabluj, aby nešlo odeslat dvakrát.
9. Nezavírej informace do accordionu ani tabů v dialogu ani v bočním panelu.
10. Skupiny polí odděl sekcemi s nadpisem, mezera mezi skupinami > mezera mezi poli.

---

## Jednoduchý versus komplexní formulář

Tohle rozlišení je klíč k celé notě, protože z něj Carbon vyvozuje označování polí.

| Typ | Charakteristika | Poměr polí |
|---|---|---|
| Simple | Kratší, orientovaný na uživatele nebo zákazníka: registrace, kontaktní formulář, checkout | **Většina polí povinná** |
| Complex | Delší, orientovaný na produkt: vlastnosti a nastavení ke konfiguraci enterprise softwaru | Bude mít aspoň jedno povinné pole, ale **většina bude volitelná** |

**ZDROJ:** Carbon, Forms pattern, Optional vs. mandatory, verbatim: „Complex forms - generally longer
and product-oriented; contain properties and settings that are used to configure Enterprise software.
Although they will usually contain at least one required field, the majority of the fields will tend
to be optional." https://carbondesignsystem.com/patterns/forms-pattern/

## Označuj menšinu

**PRAVIDLO:** Když je většina polí povinná, označ **jen** volitelná pole slovem „(optional)". Když je
většina volitelná, označ **jen** povinná slovem „(required)". Rozhodnutí dělej podle celkového počtu
polí **v celém produktu**, ne v jednom formuláři, a drž ho konzistentně napříč produktem, nebo aspoň
napříč stejnými typy formulářů.
**KDY PLATÍ:** Každý formulář.
**PROČ:** Carbon: snížíš vizuální šum a zajistíš konzistenci uvnitř produktu i napříč produkty.
**TŘÍDA:** B
**ZDROJ:** Carbon, Forms pattern, Optional vs. mandatory. Konkrétní příklad Carbonu verbatim:
„if you have 100 types of connections properties forms and the fields are optional in 85 of the 100
forms, all 100 should use the required pattern."
https://carbondesignsystem.com/patterns/forms-pattern/
**KDY NEPLATÍ:** Rozpor s knihovnou. [Formuláře a
stavy](../../ux-design/pravidla/formulare-a-stavy.md) velí označovat **volitelná** pole a povinná
neoznačovat, s citací GOV.UK, a jako výjimku uvádí formulář s jedním nebo dvěma povinnými polemi.
**To je totéž pravidlo „označ menšinu", jen aplikované na jiný typ formuláře.** Pro veřejné služby,
registrace a checkout platí knihovna. Pro konfigurační obrazovky enterprise produktu platí Carbon.
Obojí zakazuje hvězdičku bez legendy.

**Přístupnostní doplněk:** Carbon k tomu velí dát před formulář instrukci, který z těch dvou režimů
platí („All fields are required unless marked as optional"), a přiznává, že tradiční hvězdička plus
legenda je pořád považovaná za nejpřístupnější. Detail v
[Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md).

**Nadbytek volitelných polí:** Carbon říká, že se má vyhýbat. Když je velké množství volitelných polí
nutné, doporučuje **vyčlenit celou sekci na volitelná pole**, aby se označení nemuselo pořád opakovat.

## Respekt k uživateli: pět Carbonových požadavků

1. Respektuj GDPR a další soukromí regulující předpisy: ptej se **jen** na informace, které jsou
   absolutně nutné.
2. Seskup související úkoly pod nadpisy sekcí, aby byl kontext jasnější a rozhraní se dalo skenovat.
3. Drž logické, předvídatelné pořadí (jméno první, příjmení druhé).
4. Nech uživatele zůstat u jedné metody vstupu tak dlouho, jak to jde. **Nenuť ho opakovaně přepínat
   mezi klávesnicí a myší** v jednom formuláři.
5. Při návrhu ber v úvahu správce hesel a schopnost prohlížeče předvyplnit data.

Šestý bod: postupně odhaluj další vstupy až ve chvíli, kdy jsou relevantní.

**ZDROJ:** Carbon, Forms pattern, Respect the user.
https://carbondesignsystem.com/patterns/forms-pattern/
**Souvislost:** bod 5 je v knihovně tvrdší, s WCAG 1.3.5 Identify Input Purpose (AA) a atributem
`autocomplete`. Viz [formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).

## Sloupce

**PRAVIDLO:** Carbon obecně doporučuje **jednosloupcové** formuláře, protože vícesloupcové jsou
náchylnější k nesprávné interpretaci, a odkazuje se na výzkum NN/g. Když je velká obrazovka a hodně
prázdného místa, vícesloupcový formulář může být na místě, ale počet sloupců musí vycházet z počtu
vstupů, jejich vzájemného vztahu a velikosti okna.
**KDY PLATÍ:** Každý formulář.
**PROČ:** Carbon: „multicolumn forms are more prone to misinterpretation".
**TŘÍDA:** B
**ZDROJ:** Carbon, Forms pattern, Columns, s odkazem na Kathryn Whitenton, Website Forms Usability:
Top 10 Recommendations (NN/g, 2016). https://www.nngroup.com/articles/web-form-design/
**KDY NEPLATÍ:** Dva až tři vstupy na jednom řádku nezpůsobí problém, když **logicky patří k sobě**.
Carbonovy vlastní příklady: [jméno][prostřední] [příjmení], [číslo karty][expirace] [CVC],
[město][kraj] [PSČ].

**Alternativa místo přeplácání:** Carbon říká, že když by to vedlo k zavalení uživatele informacemi,
je lepší vícekrokový formulář.

**Knihovna tohle pravidlo má taky**, s měřeným online experimentem (Speero, N = 702, jednosloupcový
formulář o 15,4 s rychlejší) a s výjimkou pro interní nástroje, kde profesionál vyplňuje formulář
stokrát denně. Viz [formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).

**Chování dvousloupcového řádku:** když má formulář víc sloupců, mají být proporcionální a zarovnané
na sloupce mřížky. **Řádek musí reagovat jako skupina:** když levé pole zneplatní a odtlačí obsah dolů
kvůli chybové hlášce, pravé pole musí narůst taky, aby si to místo drželo.
Zdroj: https://carbondesignsystem.com/components/form/usage/

## Nadpisy a sekce

| Prvek | Pravidlo |
|---|---|
| Nadpis formuláře | Popisuje formulář. **Největší velikost písma v hierarchii formuláře.** Když je formulář jediný prvek na stránce, použij větší velikost než v kontejneru nebo dialogu. Může za ním následovat krátký popisek |
| Nadpis skupiny nebo sekce | Popisuje skupinu ovládacích prvků a polí. Velikost mezi nadpisem formuláře a labely polí: **větší než labely, zřetelně menší než nadpis formuláře**. Krátce a přesně, s možností krátkého popisu skupiny |
| Seskupení | Vstupy seskup tak, aby uživatel logicky pochopil, co se od něj chce |

**ZDROJ:** Carbon, Forms pattern, Layout.
https://carbondesignsystem.com/patterns/forms-pattern/

## Mezery

Carbon dává konkrétní hodnoty. Přebírám je jako vnitřně konzistentní referenci (třída **B**), ne jako
normu. Princip za nimi je důležitější než čísla: **mezera mezi skupinami musí být větší než mezera
mezi jednotlivými poli.**

| Kontext | Mezera mezi vstupy |
|---|---|
| Formulář na vlastní stránce | 32 px |
| Formulář v kontejneru (boční panel, modal) | 24 px, nebo i 16 px |
| Výchozí doporučení komponenty form | 32 px |

**Odstup skupin:** upravuj v relaci k odstupu jednotlivých položek. Carbonovy příklady:
odstup polí 24 px → před prvním vstupem a mezi sekcemi 32 px. Odstup polí 32 px → mezi sekcemi 40 px.

**Před tlačítky:** Carbon doporučuje **48 px** mezi posledním vstupem a tlačítkem nebo skupinou
tlačítek. Na mobilu a v některých kontejnerových formulářích se to bude lišit.

**Výška pole:** jednotlivá vstupní pole mají v produktu **40 px bez ohledu na kontext**.

**Čím se řídit:** na formulářích na vlastní stránce používej responzivní mřížku. Formuláře v dialogu
a bočním panelu se vracejí k box modelu, takže se šířky polí řídí mini unitem. Konzistence zarovnání
a geometrie je v obou případech klíčová.

**ZDROJ:** Carbon, Forms pattern, Spacing a Form context, verbatim: „Individual input fields default to
a 40px height in product regardless of context. On dedicated-page forms, we recommend a 32px spacer
between input fields. In contained forms, such as side panels or modals, designers can revert to 24px
or even 16px between inputs." https://carbondesignsystem.com/patterns/forms-pattern/
Detail mřížky: [2x grid a breakpointy](../zaklady/2x-grid-a-breakpointy.md).

**Co Carbon nemá:** vodicí linky (rules) mezi skupinami polí. Sám přiznává, že k jejich šířce,
tloušťce a svislým odstupům konsolidované pokyny nemá.

## Tlačítka

### Nikdy nahoru

**PRAVIDLO:** Nedávej primární a sekundární akci na horní hranu formuláře na vlastní stránce.
Tlačítka patří dolů.
**KDY PLATÍ:** Formuláře na vlastní stránce.
**PROČ:** Carbon dává tři důvody, poslední označuje za nejdůležitější:
1. Máme se ptát jen na nutný vstup a stručně, takže je legitimní předpokládat, že uživatel projde
   pole scrollem, než formulář odešle.
2. Formulář na stránce **není modal** a uživateli nebrání vrátit se do předchozího flow: má drobenku,
   progress indicator nebo tlačítko zpět v prohlížeči. Carbon z toho vyvozuje tvrdé pravidlo:
   **„back should never be an action on a secondary button"**, sekundární tlačítko je typicky
   rezervované pro zrušení úkolu.
3. Tlačítka připnutá nahoře vytvářejí velmi nešikovný vztah k obsahu ve chvíli, kdy uživatel formulář
   dokončí a chce odeslat.
**TŘÍDA:** B
**ZDROJ:** Carbon, Forms pattern, Do not top-align buttons.
https://carbondesignsystem.com/patterns/forms-pattern/
**KDY NEPLATÍ:** Carbon sám připouští, že kdyby se v budoucnu k připnutým akcím vracel, cesta by byla
připnutá **patička** nebo tray se skupinou tlačítek, ne horní lišta.

### Zarovnání a poloha primárního tlačítka

| Zarovnání | Sahá k hraně | Kdy |
|---|---|---|
| Vlevo | Ne | Formuláře na stránce, ne v dialogu |
| Vpravo | Ne | Vícekrokové formuláře a wizardy, kde primární akce znamená krok vpřed |
| Plná šířka | Ano | Všechny formuláře v dialogu a bočním panelu, v některých případech formuláře v dlaždici |

**Poloha primárního tlačítka:** vlevo a **nalevo od** sekundárního u formulářů na stránce a většiny
jiných rozvržení. Vpravo a **napravo od** sekundárního u progresivních formulářů, wizardů a formulářů
ve strukturovaných kontejnerech (dialog, boční panel).

**Když je obsah tlačítek příliš dlouhý** na uspořádání na plnou šířku, naskládej tlačítka svisle
s **primárním dole** a zachovej jejich margin a padding.

**ZDROJ:** Carbon, Forms pattern, Buttons.
https://carbondesignsystem.com/patterns/forms-pattern/
**Poznámka:** Carbon u tlačítek explicitně uvádí, že tohle vodítko **změnil**. Dřív doporučoval držet
primární tlačítko napravo od sekundárního i u zarovnání vlevo, po rozhovorech s týmy a dalším výzkumu
pozici revidoval. https://carbondesignsystem.com/components/button/usage/

### Variant a pojmenování

- Primární tlačítko pro hlavní akci, sekundární pro sekundární akce jako Zrušit nebo Zahodit.
- Label konkrétně, ne abstraktně. Detail v [UX copy v produktu](../zaklady/ux-copy-v-produktu.md).

### Enable a disable primárního tlačítka

**PRAVIDLO:** U **krátkých** formulářů, které vyžadují serverové odeslání, než vrátí chyby, Carbon
doporučuje držet primární tlačítko disabled, dokud nejsou splněné všechny požadavky formuláře.
U **dlouhých** formulářů tlačítko **nedisabluj**, protože chybové hlášky a primární tlačítko nemusí
být na obrazovce vidět zároveň.
**KDY PLATÍ:** Rozhodování o disabled stavu odesílacího tlačítka.
**TŘÍDA:** B
**ZDROJ:** Carbon, Forms pattern, Enabling and disabling buttons.
https://carbondesignsystem.com/patterns/forms-pattern/
**Vždycky platí:** po odeslání primární tlačítko disabluj, aby nešlo odeslat dvakrát. A když
zpracování zabere chvíli, dej to uživateli vědět zpětnou vazbou a progress indikátory.
Detail: [Načítání a čekání](nacitani-a-cekani.md)

## Tři techniky pro dlouhé formuláře

Carbon úvodem přiznává, že univerzální odpověď na správnou délku formuláře neexistuje: rozhoduje
publikum, jeho záměry a kontext produktu.

| Technika | Co dělá | Stav u Carbonu |
|---|---|---|
| Postupné odhalování | Odhalí další obsah podle předchozí volby uživatele. Uživatel se soustředí na relevantní informaci a flow zůstane krátké | Doporučené |
| Accordion formulář | Uživatel dynamicky odkrývá a skrývá sekce souvisejících informací, bez navigace mezi stránkami | **Nedoporučené v dialogových formulářích.** Carbon uvádí, že výzkum ukazuje výrazné zlepšení rychlosti dokončení a rychlosti načtení, ale **tentýž výzkum** ukazuje, že vzniká zmatek u primárních tlačítek: platí pro sekci, nebo pro celý formulář? Carbon konsolidované pokyny **nemá** |
| Vícekrokový formulář | Rozloží pole na víc obrazovek plus progress indicator (svislý nebo vodorovný). Mezi poli na obrazovce má být logický vztah a mezi sekcemi lineární vztah | Doporučené. Výhoda: umožňuje ukládat postup a vracet se ke kontrole předchozích kroků |

**ZDROJ:** Carbon, Forms pattern, Designing for longer forms, u accordionu s odkazem na
Luke Wroblewski, Testing Accordion Forms (2010). https://www.lukew.com/ff/entry.asp?1190
https://carbondesignsystem.com/patterns/forms-pattern/

**Poznámka ke vícekrokovým formulářům:** knihovna má tvrdší pravidlo o progress indikátoru. Není to
samozřejmost, u dvanáctikrokového indikátoru se ve státní službě jeho odebrání neprojevilo ani na
dokončení, ani na čase. A pro nesení informace mezi kroky platí kapacita 3 až 5 položek (Cowan 2001),
ne 7. Viz [formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).

## Inline editace

Carbon k inline editaci **nemá konsolidované pokyny** a sám to přiznává: je to věc, ke které
produkty přistupují různě. Uvádí jen princip: inline editace nechá uživatele upravit text na místě,
místo aby ho vedla na jinou stránku, takže nemusí obnovovat celý formulář kvůli jedné úpravě.
Zdroj: https://carbondesignsystem.com/patterns/forms-pattern/

## Formulář v dialogu a v bočním panelu

Obojí má **stejné omezení**: neschovávej informace do accordionů ani tabů.

| Kontext | Počet vstupů |
|---|---|
| Dialog | Méně než pět |
| Boční panel | Víc než pět |

**ZDROJ:** Carbon, Forms pattern, Variants.
https://carbondesignsystem.com/patterns/forms-pattern/
Detail: [Dialogy a panely](dialogy-a-panely.md)

## Fluidní versus default styl formuláře

| Styl | Vzhled | Zarovnání | Kdy |
|---|---|---|---|
| Default | Label nad polem, vně. Tři velikosti pole: 32, 40, 48 px | Vstupy naskládané s 32 px odstupem, zarovnané na sloupce mřížky | Když je potřeba prostor mezi vstupy, když jsou potřeba menší komponenty, nebo v produktivních momentech jako složité formuláře |
| Fluid | Label **uvnitř** pole, zarovnaný s textem vstupu. Jen jedna velikost, 64 px | Vstupy naskládané **těsně na sebe, 0 px** mezi nimi. Používá condensed mřížku a může zasahovat do mezery | V expresivních momentech nebo když větší komponenty pomůžou zdůraznit hlavní formulář |

**Fluidní formulář má výjimku z pravidla o tooltipech:** nemá pod polem místo na helper text, takže
**všechna** asistenční informace, i ta zásadní, jde do tooltipu. Carbon to označuje za výjimku
z jinak platného pravidla „žádná kritická informace v tooltipu".

**ZDROJ:** Carbon, Form usage, Styling a Tooltips in fluid components, verbatim: „Fluid inputs are an
exception to the no critical information in tooltips rule."
https://carbondesignsystem.com/components/form/usage/
**Pozor:** knihovna má u placeholderu i helper textu přísnější pravidla s WCAG oporou. Fluidní styl
s labelem uvnitř pole je z jejího pohledu riziko, protože label a hodnota si konkurují o stejné místo.
Než ho použiješ, přečti [formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md), sekce
Struktura formuláře.

## Výchozí hodnoty

**PRAVIDLO:** Výchozí hodnotu lze nastavit u všech typů vstupů. Musí to být něco, co by se běžně
použilo, a co **nezpůsobí zmatek nebo chybu**, když uživatel zapomene nebo se rozhodne to nezměnit
před odesláním.
**PROČ:** Carbon: dobré výchozí hodnoty snižují kognitivní zátěž.
**TŘÍDA:** B
**ZDROJ:** Carbon, Forms pattern, Default values, plus Carbonovy konkrétní příklady: předvolená zem
podle detekované lokality, předplněná běžná nebo minimální hodnota (kvóta, limit paměti), předplněný
název firmy, aktuální datum jako výchozí počáteční datum.
https://carbondesignsystem.com/patterns/forms-pattern/
**Doplněk z komponenty:** kde to jde, přidej programovou asistenci. Detekuj a předplň vstupy, ať se
sníží chyby a ušetří čas. Když software hodnotu určit neumí, použij type-ahead a nabídni návrhy.
https://carbondesignsystem.com/components/form/usage/

## Ovládací prvky podle typu vstupu

Carbon dělí vstupy do tří interakčních typů. Detailní rozhodovací tabulky jsou ve
[Volbě komponenty](../zaklady/volba-komponenty.md).

| Typ | Definice | Příklady |
|---|---|---|
| Free form inputs | Uživatel může zadat jakoukoliv kombinaci znaků | text input, text area |
| Selection controls | Výběr z předem daných možností | checkbox, radio button, file uploader, toggle, combo box, multiselect |
| Bound entry controls | Numerický vstup s omezeným rozsahem. **Dovolí jen platné hodnoty, takže validace formátu není potřeba** | number input, slider, date picker, time picker |

**ZDROJ:** Carbon, Forms pattern, Data inputs, verbatim: „They only allow valid entries, so field
validation isn't needed." https://carbondesignsystem.com/patterns/forms-pattern/

**Praktický důsledek:** volbou bound entry controlu se zbavíš celé jedné kategorie chyb. Carbon to
říká i explicitně u dialogů: „Decrease the chances of invalid data by using selection controls and
bound entry controls components that provide users with specific input choices."

**Dvě konkrétní pravidla pro selection controls:**

- Radio buttony: **předvyber výchozí možnost.** Pro „nic z toho" nabídni radio button s labelem
  „None".
- Radio buttony a checkboxy: text vpravo od ovládacího prvku, skupiny **svisle** kvůli skenovatelnosti.

## První focus

**PRAVIDLO:** První **povinné** vstupní pole ve formuláři má dostat focus při zobrazení uživateli.
**TŘÍDA:** B
**ZDROJ:** Carbon, Forms pattern, Text inputs, Best practices, verbatim: „The first required input
field in a form should receive focus on presentation to a user."
https://carbondesignsystem.com/patterns/forms-pattern/
**Pozor:** v modalu je pravidlo o focusu jiné a závisí na typu dialogu. Viz
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md).

---

## Co tahle nota neřeší

- Labely, placeholder, helper text, validaci a chybové hlášky.
  [Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md), s WCAG a GOV.UK oporou.
  Tohle je nadřazený zdroj.
- Placeholder jako anti-pattern. Tamtéž, tam je zakázaný úplně, Carbon je mírnější.
- Šířku pole podle očekávané délky obsahu. Tamtéž. Carbon má stejné pravidlo, tam je zdrojované.
- Detail helper textu, tooltipu a počítadel u vstupu. [Textová pole](../komponenty/textova-pole.md).
- Prázdné a chybové stavy stránky.
  [Prázdné stavy](prazdne-stavy.md) a [formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md).

## Zdroj

IBM Carbon Design System, Forms pattern a Form usage, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/patterns/forms-pattern/ ·
https://carbondesignsystem.com/components/form/usage/
Carbon k tomuhle vzoru cituje NN/g (Tooltip Guidelines 2019, OK-Cancel or Cancel-OK? 2008,
Website Forms Usability 2016, Marking Required Fields 2019, The Power of Defaults 2015),
Luke Wroblewski (Testing Accordion Forms 2010), Preibusch et al. 2013 a W3C WAI Forms tutoriál.
Třída **B**. Kde si Carbon odporuje s knihovnou, platí knihovna, protože má tvrdší zdroje.
