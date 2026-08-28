# Tlačítka: varianty, hierarchie, stavy, destruktivní akce

Rozhodovací pravidla pro moment, kdy stavíš tlačítko: kolik jich na obrazovku patří, jakou variantu
akci přiřadit, jak musí vypadat stavy, jak se dělá nevratná akce a jaké jsou tvrdé mantinely
velikosti a kontrastu.

**Jak číst třídu důkazu:** `A` = měření nebo studie se vzorkem a metodou (u regulace: právní
požadavek, taky tvrdý, ale jiného druhu). `B` = publikovaná konvence, organizace to tvrdí a dodržuje,
studie za tím není. `C` = řemeslná praxe, konkrétní praktik to tvrdí a zdůvodňuje, důkaz neexistuje.

**Nejdůležitější věc na téhle notě:** u tlačítek prakticky neexistuje třída A kromě regulace
a Fittsovy linie výzkumu o míření. Počet primárních tlačítek, pořadí variant i barva destruktivní
akce jsou třída B, tedy konvence, kterou drží deset a více organizací nezávisle na sobě. To je
slabší než studie a výrazně silnější než vkus. Nikdy to neprodávej jako výzkum.

Citace pocházejí z průzkumu fáze 1 (29. 7. 2026). Čtyři systémy, které v podkladu neměly URL
(Atlassian, Apple HIG, Fluent 2, Base Web), jsou od 28. 8. 2026 ověřené přímo v jejich dokumentaci:
u nich stojí URL a doslovná anglická formulace tak, jak ji publikují. Jedno tvrzení se ověřit
nepodařilo a je označené, viz pravidlo o varovné barvě.

---

## Kolik tlačítek

### Jedno primární tlačítko na sekci

**PRAVIDLO:** V jedné vizuálně oddělené sekci nech nejvýš jedno primární (plné, akcentní) tlačítko.
Všechny ostatní akce v téže sekci dej sekundární nebo nižší variantou.
**KDY PLATÍ:** Vždy, když v jednom zorném poli existuje víc než jedna akce. Jednotka není dokument,
ale sekce nebo skupina (karta, modál, panel, řádek formuláře).
**PROČ:** Primární varianta je nositel informace „tohle je doporučený další krok". Dvě plné plochy
vedle sebe tu informaci ruší: uživatel místo přečtení hierarchie musí porovnat dva labely a rozhodnout
se sám. GOV.UK to zdůvodňuje snížením dopadu (víc default tlačítek = každé z nich má menší tah
a roste nejistota), Apple kognitivní zátěží („Presenting too many prominent buttons increases
cognitive load, requiring people to spend more time considering options before making a choice.")
a Atlassian soutěží o pozornost („Having multiple primary CTAs in one area can be confusing or
visually overwhelming because they compete for attention.").
**TŘÍDA:** B. Shoda 10+ publikovaných systémů s odlišnými zájmy a publiky:

| Systém | Publikovaná formulace |
|---|---|
| GOV.UK | „Avoid using multiple default buttons on a single page" |
| Material Design 3 | „used sparingly, ideally for only one action on a page" |
| Atlassian | „Only include one primary button or call to action (CTA) in a page or area." |
| Apple HIG | „Keep the number of prominent buttons to one or two per view." |
| Primer (GitHub) | „never more than one in a group, rarely more than one per page" |
| Ant Design | „at most one primary button in a section" |
| Fluent 2 | „Only use one primary button in a layout for the most important action." |
| Base Web | „These are to be used sparingly as the sole action of a view." |
| NHS, Carbon, Adobe Spectrum | shodná formulace, viz podklad fáze 1 |

**Na čem se systémy neshodnou: jednotka.** Atlassian mluví o „page or area", Apple a Base Web
o „view", Ant Design a Primer o sekci nebo skupině, Fluent 2 o „layout". Shoda je na počtu (jedno),
ne na tom, kde se ten počet měří. Formulace „na sekci" v pravidle nahoře je proto syntéza té nejužší
varianty, ne citát žádného z nich. Kdo se odvolává na konkrétní systém, ať použije jeho jednotku.

**ZDROJ:** `design-system.service.gov.uk/components/button/`, `m3.material.io`, `primer.style`,
`ant.design/components/button`, `service-manual.nhs.uk/design-system`,
`carbondesignsystem.com/components/button/usage`, `spectrum.adobe.com/page/button`.
Ověřeno přímo ve zdroji 28. 8. 2026: `atlassian.design/components/button/usage` (sekce „Use one
primary call to action"), `developer.apple.com/design/human-interface-guidelines/buttons`,
`fluent2.microsoft.design/components/web/react/core/button/usage`, `baseweb.design/components/button/`.
**KDY NEPLATÍ:**
- Stránka rozdělená na nezávislé oblasti (dashboard s widgety, seznam karet, kde každá karta má
  vlastní akci) může mít primárních tlačítek víc, každé ve své sekci. Primer to formuluje per group.
  Atlassian píše „in a page or area", takže oblast připouští, ale stránku uvádí jako první. Na
  Atlassian se u dashboardu odvolávej opatrně, výjimku plně nekryje.
- Apple HIG připouští dvě na view, takže dvojice „potvrdit / uložit jako" v modálu není chyba, pokud
  jedna z nich vizuálně vede.
- Dvě skutečně rovnocenné, vzájemně se vylučující volby (typicky nevratné rozhodnutí bez doporučené
  odpovědi). Tam je čistší dát obě stejnou nižší variantou než hádat, která je primární. Tohle je
  odvození, ne zdroj: žádný z výše uvedených systémů ten případ neřeší.
- Nepoužívej to jako protiargument proti měření. V podkladu není jediný test dopadu počtu primárních
  tlačítek na konverzi. Když ti A/B test na tvém produktu ukáže opak, platí test.

### Nejvýš tři akcentní tlačítka v jednom pohledu

**PRAVIDLO:** Součet akcentních (primárních) tlačítek na jednom pohledu drž na maximu 3, i když jsou
každé ve své sekci.
**KDY PLATÍ:** Delší stránky a hustá rozhraní, kde předchozí pravidlo („jedno na sekci") při dost
velkém počtu sekcí povolí libovolný počet akcentů.
**PROČ:** Akcent funguje jako výjimka proti klidné ploše. Nad určitou hustotou přestane být výjimkou,
plocha se stane pruhovaná a akcent přestane nést informaci o důležitosti.
**TŘÍDA:** B (Adobe Spectrum). Bez studie.
**ZDROJ:** `spectrum.adobe.com/page/button`, citováno v podkladu fáze 1 jako „max 3 accent buttons
v jednom pohledu".
**KDY NEPLATÍ:** Velmi dlouhá stránka, kde se do jednoho zorného pole nikdy nedostanou dvě sekce
(typicky landing page s celoobrazovkovými bloky): limit je „v jednom pohledu", ne „v jednom
dokumentu", takže se odpočítává podle výřezu, ne podle délky. Neplatí ani na aplikační toolbary
a tabulky, kde akce nejsou akcentní varianta.

### Tři a více souběžných akcí sbal do menu

**PRAVIDLO:** Když jedna sekce potřebuje 3 a více souběžných akcí, nech viditelnou jednu primární
plus nejnutnější sekundární a zbytek přesuň do rozbalovacího menu.
**KDY PLATÍ:** Řádky tabulek, hlavičky karet, detailové obrazovky s víc operacemi.
**PROČ:** Ant Design to formuluje jako vzorec „1 primary + n secondary" a při 3+ souběžných akcích
doporučuje Dropdown. Mechanismus je, že vedle sebe stojící tlačítka soutěží o pozornost a při čtyřech
už žádné nevede, zatímco menu ten výběr převede na krok, který uživatel udělá až když ho potřebuje.
**TŘÍDA:** B (Ant Design). Bez studie.
**ZDROJ:** `ant.design/components/button`.
**KDY NEPLATÍ:**
- Když akci uživatel musí vidět, aby vůbec věděl, že existuje (objevitelnost). Skrytí do menu tu cenu
  přesouvá na hledání a ta není nulová: Cockburn, Gutwin, Greenberg (CHI 2007, N = 8) doložili, že
  u nováčka roste čas hledání v menu **lineárně** s jeho délkou, ne logaritmicky. Menu se čtyřmi
  položkami tedy nezlevní na nulu.
- Na dotykovém zařízení přidává menu druhý tap a překryv obsahu. U dvou akcí to bývá dražší než dvě
  tlačítka vedle sebe.
- Hlavní konverzní akce nikdy nepatří do menu.

---

## Varianty a jejich role

### Variantu přiřazuj podle role v toku, ne podle vzhledu

**PRAVIDLO:** Nejdřív pojmenuj, co akce dělá s tokem (posouvá dopředu, je alternativa na téže
stránce, je vedlejší nebo zrušení), a teprve pak vyber variantu. Mapování role → varianta drž
v celém produktu stejné.
**KDY PLATÍ:** Každý produkt s víc než jednou obrazovkou.
**PROČ:** Varianta je jediný nositel pořadí důležitosti, který uživatel čte bez přečtení labelu.
Když se mapování mezi obrazovkami mění, nedá se naučit a každou obrazovku musí uživatel číst od nuly.
Publikovaná pořadí, ze kterých se dá vyjít:
- **Material 3** (nejsilnější → nejslabší): Filled > Elevated > Tonal > Outlined > Text.
- **USWDS**: outline varianta pro akce, které zůstávají na aktuální stránce, default varianta pro
  další krok toku nebo odchod ze stránky.
- **Carbon**: primary / secondary / tertiary / ghost, s vlastní danger sadou pro destruktivní akce.

**TŘÍDA:** B. U Material 3 to podklad výslovně označuje jako interní konvenci Google **bez
publikovaného user testu**. USWDS a Carbon totéž, jen publikovaná konvence.
**ZDROJ:** `m3.material.io`, `designsystem.digital.gov/components/button/`,
`carbondesignsystem.com/components/button/usage`.
**KDY NEPLATÍ:** Nestylované knihovny primitiv (Radix, shadcn/ui) hierarchii záměrně nediktují,
protože řeší ARIA, klávesnici a focus, ne vzhled. Tam mapování definuje aplikace a je chyba čekat, že
ho knihovna přinese. Neplatí ani na obrazovku s jedinou akcí, kde hierarchie není co vyjadřovat.

### Co nenese text, musí mít kontrast 3:1

**PRAVIDLO:** U icon-only tlačítek, ghost a outline variant a u focus indikátoru drž kontrast
minimálně 3:1 proti sousední barvě. Jemná šedá na šedé je porušení, ne styl.
**KDY PLATÍ:** Vše, co na tlačítku nese význam a není text: ikona, obrys, focus ring, stavový rámeček.
**PROČ:** WCAG 2.1 zavedlo kritérium 1.4.11 Non-text Contrast (úroveň AA) právě na komponenty
rozhraní a grafiku. Prakticky to vylučuje bezokrajové „invisible UI", protože u ghost tlačítka bez
labelu a bez obrysu není nic, co by prošlo.
**TŘÍDA:** A (regulatorní, ne empirická). Kritérium je právní a nástrojově testovatelné, není to
naměřený percepční práh. Pro srovnání: derivace prahu 4,5:1 u textu (SC 1.4.3) je doložitelně slabá,
faktor 1,5 pochází z interceptu regrese v Arditi & Faye (2004), ne z měření, a W3C to má
zdokumentované u sebe (w3c/wcag#1705).
**ZDROJ:** W3C WCAG 2.1, SC 1.4.11 Non-text Contrast.
**KDY NEPLATÍ:** Dekorace bez významu a stavy, které nesou informaci jinak (disabled je z 1.4.11
výslovně vyňatý, což je zároveň důvod, proč disabled tlačítka matou, viz níže). Vlastní focus styl
neodstraňuj bez náhrady, i když 3:1 splní jinak: kritérium 2.4.7 Focus Visible je v podkladu fáze 1
neověřené, ale existuje, ověř si ho, než se rozhodneš outline vypnout.

---

## Destruktivní akce

### Destruktivní akci nikdy nenes jen barvou

**PRAVIDLO:** U nevratné akce napiš do labelu, co konkrétně zmizí („Smazat 12 souborů", ne „Smazat"),
a před provedením vlož potvrzovací krok. Červená barva je až třetí signál v řadě, ne první.
**KDY PLATÍ:** Každá akce, kterou uživatel nemůže snadno vrátit.
**PROČ:** Barva je pro část uživatelů nedostupný kanál. USWDS to argumentuje demografií: barvoslepost
zasahuje 8 % mužů a 0,5 % žen, a proto radí navrhovat „start in black and white", tedy nikdy
neschovávat informaci výhradně do barvy. U destruktivní akce se ta cena platí přesně v momentě, kdy
už není co vrátit. GOV.UK to říká přímo: „Do not only rely on the red colour of a warning button". Apple přidává druhou
stranu téže mince: destruktivní akci nedávej primární roli, protože „Because of its visual prominence,
people sometimes choose a primary button without reading it first."
**TŘÍDA:** B. Shoda napříč systémy plus explicitní formulace GOV.UK, USWDS a Apple HIG. Studie na to
v podkladech není.
**ZDROJ:** `design-system.service.gov.uk/components/button/`, `designsystem.digital.gov`,
`developer.apple.com/design/human-interface-guidelines/buttons` („Don't assign the primary role to
a button that performs a destructive action, even if that action is the most likely choice.",
ověřeno 28. 8. 2026).
**KDY NEPLATÍ:**
- Když je akce spolehlivě vratná (undo s dostatečným okamžikem), potvrzovací dialog jen přidává krok
  a uživatel se ho naučí odklikávat naslepo, čímž pojistka přestane fungovat. Tohle je řemeslná
  úvaha (třída C), ne zdroj z podkladu.
- Hromadné a opakované operace: potvrzuj dávku, ne každou položku, jinak potvrzení degeneruje
  v mechanický klik.
- Pravidlo o labelu neplatí, když počet dotčených objektů nejde v momentě kliknutí zjistit. Pak popiš
  rozsah slovně, ne číslem, které si domyslíš.

### Warning variantu drž na nevratné následky a používej ji zřídka

**PRAVIDLO:** Zvláštní varovnou (warning, danger) variantu tlačítka použij jen pro akce se závažnými
destruktivními následky, které nejde snadno vrátit. Ve většině produktů to znamená žádnou.
**KDY PLATÍ:** Volba, jestli varovnou variantu do systému vůbec zavést.
**PROČ:** Varianta funguje na kontrastu proti zbytku. GOV.UK ji vymezuje na „serious destructive
consequences that cannot be easily undone", NHS jde dál a píše: „They are only effective if used very
sparingly. Most services should not need one." Když se použije na běžnou akci, přestane signalizovat
nebezpečí a uživatel ji začne ignorovat.
**TŘÍDA:** B (GOV.UK, NHS Service Manual).
**ZDROJ:** `design-system.service.gov.uk/components/button/`,
`service-manual.nhs.uk/design-system/components/buttons`.
**KDY NEPLATÍ:** Produkt, jehož celá náplň je destruktivní operace (administrace, mazací nástroje,
správa infrastruktury). Tam je varovná varianta běžný pracovní prvek a mantinelem je potvrzovací krok
a rozsah v labelu, ne vzácnost varianty. NHS mluví o službách pro pacienty, ne o admin konzoli.

### Nepoužívej varovnou barvu na akci, která není varování

**PRAVIDLO:** Nikdy nedávej danger nebo warning barvu tlačítku, které nedělá nic nebezpečného.
Oranžové „Save" je chyba, ne odlišení.
**KDY PLATÍ:** Volba barvy jakéhokoli CTA.
**PROČ:** Sémantické barvy jsou slovník. Když se stejná barva použije jednou pro „pozor" a jednou pro
„ulož", uživatel se ten slovník nenaučí a v momentě, kdy má varování zabrat, nezabere.
**TŘÍDA:** C. Ověření 28. 8. 2026 selhalo. Formulace „Don't use warning or danger for CTAs that
aren't warning or danger", kterou podklad fáze 1 připisuje Atlassianu, na jeho stránkách k tlačítku
není: prošel jsem `atlassian.design/components/button` i `/components/button/usage` a slova
„warning" ani „danger" se v sekcích s doporučeními nevyskytují ani jednou. **Necitovat jako
Atlassian.** Pravidlo platí dál, ale jako řemeslná úvaha o sémantických barvách, ne jako publikovaná
konvence.
**ZDROJ:** Nedohledáno. Co Atlassian doopravdy publikuje, je vymezení obou variant významem, což
pravidlo podpírá definicí místo zákazu: „Warning buttons confirm actions that may cause a significant
change or a loss of data." a „A danger button appears as a final confirmation for a destructive and
irreversible action, such as deleting." (`atlassian.design/components/button`, ověřeno 28. 8. 2026).
**KDY NEPLATÍ:** Když je akcentní barva brandu shodou okolností v oranžovém nebo červeném pásmu.
Tam pravidlo padá na úroveň systému: pak musí varovná varianta být rozlišená jinak (obrys, ikona,
tvar), protože barvu už nese primární akce. Pravidlo se týká sémantiky, ne hue.

### Variantu destruktivního tlačítka vyber podle role v toku

**PRAVIDLO:** Je-li destrukce hlavním krokem workflow (obrazovka „Zrušit předplatné"), použij plnou
danger variantu. Je-li jednou z několika možností v seznamu nebo menu, použij tertiary nebo ghost
danger.
**KDY PLATÍ:** Systémy s vlastní danger sadou variant.
**PROČ:** Carbon to odvozuje z role, ne z nebezpečnosti: plná varianta znamená „tohle je ten krok,
proč tu jsi". Když se dá plná danger varianta jedné z pěti položek v menu, uživatel čte, že to je
doporučená akce.
**TŘÍDA:** B (IBM Carbon).
**ZDROJ:** `carbondesignsystem.com/components/button/usage`.
**KDY NEPLATÍ:** Systém, který danger variantu nemá vůbec (GOV.UK má jednu warning variantu bez
odstupňování). Tam se role vyjádří pozicí a potvrzovacím krokem, ne stupněm varianty. Nezavádět tři
danger varianty do systému, který má celkem dvě varianty tlačítka.

---

## Stavy

### Pět stavů musí být vizuálně odlišitelných

**PRAVIDLO:** Navrhni a implementuj pět stavů tlačítka tak, aby se od sebe daly rozeznat na pohled:
enabled, disabled, hover, focus, pressed. Focus a pressed nesmí být tentýž vzhled.
**KDY PLATÍ:** Každé interaktivní tlačítko.
**PROČ:** Stav je zpětná vazba na akci uživatele. Když se hover a focus nedají rozlišit, uživatel
na klávesnici neví, kde je, a když se pressed vizuálně neděje, klik se jeví jako neproběhlý a lidé
klikají znovu.
**TŘÍDA:** B (Nielsen Norman Group, Button States 101). NN/g je organizace, která to publikuje
a dodržuje, ale studii k tomu neuvádí. Nepovyšuj na A jen proto, že je to NN/g: podklad fáze 1
u jiných jejich tvrzení (F-pattern, „5 uživatelů stačí") doložil, jak snadno se u nich přeceňuje
evidence.
**ZDROJ:** NN/g, Button States 101, `youtube.com/watch?v=3xfagjg5iRA`.
**KDY NEPLATÍ:** Hover stav se na dotykovém zařízení neuplatní (viz pravidlo o `@media (hover: hover)`
níže), takže „pět stavů" neznamená pět stavů na mobilu. A disabled nemusíš navrhovat vůbec, pokud ho
podle pravidla níže nepoužíváš. Pravidlo neříká, ČÍM stavy odlišíš, jen že musí být rozlišitelné.

### State layer jako opacita: hover 8, focus 10, press 10, drag 16 procent

**PRAVIDLO:** Stavy řeš průsvitnou vrstvou nad barvou tlačítka s hodnotami hover 8 %, focus 10 %,
press 10 %, drag 16 %, ne ručně namíchanou barvou pro každý stav.
**KDY PLATÍ:** Systém stavěný na Material 3 nebo systém, který zatím vlastní hodnoty nemá a potřebuje
výchozí sadu.
**PROČ:** Jedna vrstva s definovanou opacitou drží konzistenci automaticky napříč všemi variantami
a barvami. Ručně míchané stavy se rozjedou v momentě, kdy přidáš druhou barvu tlačítka.
**TŘÍDA:** B (Material Design 3). Podklad fáze 1 to výslovně označuje: interní konvence Google,
**žádný publikovaný user test**.
**ZDROJ:** `m3.material.io/foundations/interaction/states`.
**KDY NEPLATÍ:**
- Focus a press mají v M3 shodnou hodnotu 10 %, takže samotná vrstva ty dva stavy nerozliší. Focus
  musí navíc nést ring, jinak porušíš pravidlo o pěti rozlišitelných stavech.
- Nemíchej dvě soustavy. Když produkt jede na Carbonu nebo vlastních tokenech, použij jejich hodnoty,
  ne tyhle.
- U ghost a text variant na světlém pozadí je 8 % nad průhledným pozadím velmi jemná změna. Ověř ji
  na reálné ploše, ne v návrhovém nástroji na šedém plátně.

### Hover styluj jen v `@media (hover: hover)`

**PRAVIDLO:** Každý hover stav zabal do `@media (hover: hover)`.
**KDY PLATÍ:** Jakýkoli web nebo webová aplikace, kterou lze otevřít na dotykovém zařízení.
**PROČ:** Na dotyku hover po tapnutí uvízne. Tlačítko zůstane vizuálně ve stavu „myš nad ním"
i po odchodu prstu, takže vypadá jako aktivní nebo vybrané, a uživatel čte falešný stav.
**TŘÍDA:** C (Rauno Freiberg, Web Interface Guidelines, Staff Design Engineer @ Vercel). Zdůvodněná
řemeslná praxe, měření za tím není.
**ZDROJ:** `interfaces.rauno.me`.
**KDY NEPLATÍ:** Aplikace, která běží výhradně na desktopu s myší (interní nástroj, kiosk s myší).
I tam ale dotaz nic nerozbije, takže odchylka nemá výnos. Pozor na hybridní zařízení: dotyk plus myš
splní `hover: hover`, takže tam hover zůstane zapnutý.

### Feedback na press dělej krátkou přerušitelnou transition

**PRAVIDLO:** Reakci na stisk drž do ~200 ms a škáluj proporcionálně a málo: `scale(0.96)`, ne
`scale(0.8)`. Piš to jako CSS `transition`, ne jako keyframes.
**KDY PLATÍ:** Mikrointerakce tlačítka, hlavně u dotykových a často používaných akcí.
**PROČ:** Nad ~200 ms se odezva přestane jevit jako okamžitá a vloží se mezi klik a výsledek.
Velký scale vypadá jako hračka a u velkého tlačítka se posune obsah kolem. `transition` je
přerušitelná, takže rychlé opakované kliknutí ji plynule převezme, zatímco keyframes animace musí
doběhnout nebo skočit.
**TŘÍDA:** C. Timing a hodnota scale: Rauno Freiberg. Argument o přerušitelnosti: Emil Kowalski
(autor Sonner a Vaul), formulovaný na enter transition toastu (400 ms ease), přenos na tlačítko je
odvození, ne jeho tvrzení.
**ZDROJ:** `interfaces.rauno.me`, `emilkowal.ski/ui/building-a-toast-component`.
**KDY NEPLATÍ:** `prefers-reduced-motion` (tam scale vypusť a nech jen barevnou změnu stavu).
A u tlačítka, které spouští dlouhou operaci, není mikroanimace dostatečná zpětná vazba, tam je
potřeba stav probíhající operace. Ten podklad fáze 1 neřeší vůbec, viz mezery níže.

### Disabled tlačítka se vyhýbej

**PRAVIDLO:** Nepoužívej disabled tlačítko jako způsob, jak uživateli oznámit, že něco chybí nebo
nesmí. Buď akci nech dostupnou a chybu vysvětli po pokusu, nebo tlačítko vůbec nezobrazuj.
**KDY PLATÍ:** Formuláře, wizardy, akce vázané na oprávnění nebo na stav objektu.
**PROČ:** Disabled prvek nese dvě vady současně. GOV.UK: „poor contrast and can confuse some users,
avoid if possible". NHS o svých vlastních disabled variantách přiznává, že nesplňují kontrastní
poměry. Zároveň disabled neříká, PROČ je akce blokovaná, takže uživatel nemá co udělat. Šedé tlačítko
je tedy komponenta, která vědomě nesplňuje kontrast a neposkytuje cestu dál. Atlassian to zužuje
na nejčastější případ: „Don't disable form submission buttons, as this doesn't give people clear
a direction for how to proceed." (překlep „clear a direction" je jejich, cituju doslova).
**TŘÍDA:** B (GOV.UK Design System, NHS Service Manual, Atlassian Design System). Studie na to není,
ale tři organizace to publikují jako doporučení a NHS to o sobě přiznává.
**ZDROJ:** `design-system.service.gov.uk/components/button/`,
`service-manual.nhs.uk/design-system/components/buttons`,
`atlassian.design/components/button/usage` (ověřeno 28. 8. 2026).
**KDY NEPLATÍ:**
- Krátkodobá blokace během probíhající operace (zabránit dvojímu odeslání). Tam disabled drží stav
  několik sekund a alternativa, tedy dvojí odeslání, je horší.
- Když je důvod blokace zjevný z bezprostředního okolí (nezaškrtnutý souhlas přímo nad tlačítkem).
  I tam ale platí kontrastní vada.
- Náhradu už není nutné dovozovat. Atlassian ji publikuje přímo: „Use validation or other clear
  on-screen directions to help people proceed." Tím se ta část dostává z třídy C na B. GOV.UK
  v citovaném místě pořád jen varuje a náhradu nenabízí.

---

## Focus

### Focus ring přes `box-shadow`, ne `outline`

**PRAVIDLO:** Focus indikátor kresli `box-shadow`, ne `outline`, pokud musíš podporovat Safari starší
než 16.4.
**KDY PLATÍ:** Tlačítka a jakékoli zakulacené interaktivní prvky.
**PROČ:** `outline` nerespektuje `border-radius`, takže na zakulaceném tlačítku vykreslí hranatý
rámeček mimo tvar prvku. Safari to opravil až ve verzi 16.4.
**TŘÍDA:** C (Rauno Freiberg, Web Interface Guidelines).
**ZDROJ:** `interfaces.rauno.me`.
**KDY NEPLATÍ:** Na moderním targetu (Safari 16.4+, Chrome, Firefox) `outline` radius respektuje
a pravidlo tím ztrácí původní důvod. `box-shadow` má navíc jinou nevýhodu: rodič s `overflow: hidden`
ho může odstřihnout, zatímco `outline` je kreslený mimo layout. Podklad fáze 1 to neověřuje, tak si
to v konkrétním layoutu vyzkoušej, než pravidlo přeneseš na komponenty v kartách a tabulkách.
Ať zvolíš cokoliv, focus indikátor musí splnit 3:1 (viz výše) a nesmí se odstranit bez náhrady.

---

## Velikost a terč

### Nejmenší rozměr klikací plochy alespoň 24 CSS px

**PRAVIDLO:** Žádný rozměr klikací plochy tlačítka nesmí být pod 24 CSS px. U primárních dotykových
akcí miř na 44 CSS px.
**KDY PLATÍ:** Ikonová tlačítka, zavírací křížky, inline ovládání, tlačítka v hustých tabulkách.
Tam se ten limit láme nejčastěji.
**PROČ:** WCAG 2.2 zavedlo SC 2.5.8 Target Size (Minimum) na 24×24 CSS px jako úroveň **AA**, tedy
podlahu, ne doporučení. 44×44 je SC 2.5.5 Target Size (Enhanced), úroveň AAA z WCAG 2.1.
**TŘÍDA:** A (regulatorní).
**ZDROJ:** W3C WCAG 2.2, SC 2.5.8 (přidáno 5. 10. 2023); WCAG 2.1, SC 2.5.5.
**KDY NEPLATÍ:**
- SC 2.5.8 má pět výjimek: spacing, equivalent, inline, user agent control, essential. Ikona v běžícím
  textu (inline) pod ně spadá.
- Právní rámce dnes na WCAG 2.2 většinou neukazují: Section 508 váže jen 2.0 AA, EN 301 549
  a evropská linie (Web Accessibility Directive, European Accessibility Act, u nás zákon č. 99/2019
  Sb.) odpovídá 2.1 AA, ADA Title II míří na 2.1 AA s posunutými deadliny 26. 4. 2027 (populace
  ≥ 50 000) a 26. 4. 2028. Ve 2.1 kritérium 2.5.8 **není**. 24 px je tedy dnes standard a dobrá
  praxe, ne u každého klienta zákon. Nepředstírej opak, ale ani to neber jako povolení klesnout.

### Zvětšuj menší rozměr tlačítka, ne ten už dlouhý

**PRAVIDLO:** U širokého a nízkého tlačítka (typicky 200×24 px) zvyšuj výšku, tedy vertikální padding.
Rozšiřování do strany už čas míření nezkrátí.
**KDY PLATÍ:** Optimalizace rychlosti a spolehlivosti zásahu u kurzoru i prstu.
**PROČ:** MacKenzie & Buxton porovnali tři způsoby, jak do Fittsova modelu dosadit šířku terče ve 2D.
Vyhrál model SMALLER-OF, tedy menší z rozměrů (r = .9501, p < .001), proti dosud používanému
horizontálnímu W (r = .8097). Autoři to formulují jako „a clear refutation of applying the status quo
model". Prakticky: u tlačítka 200×24 px je relevantní rozměr 24, nikoliv 200.
**TŘÍDA:** A (MacKenzie & Buxton, CHI '92, N = 12, 1170 pokusů na účastníka).
**ZDROJ:** MacKenzie, I. S., & Buxton, W. (1992). Extending Fitts' law to two-dimensional tasks. CHI '92.
**KDY NEPLATÍ:**
- Model predikuje **čas**, ne chybovost. Fitts sám chybovost nemodeloval, jeho vlastní data byla
  1,2 až 1,3 % celkově a instrukce zněla „Emphasize accuracy rather than speed". Tvrzení „větší
  tlačítko = méně chyb" z Fittse **nevyplývá**.
- U prstu existuje podlaha absolutní přesnosti nezávislá na rychlosti (FFitts law, Bi, Li, Zhai,
  CHI 2013, N = 12, R² ≥ 0,91). Pod určitou velikost ji nelze vykoupit zpomalením, jediný fix je
  zvětšit terč.
- Full-width tlačítko u spodní hrany mobilu má jiný důvod než míření (nemusíš mířit na ose X). Jeho
  výška je ale pořád ten rozměr, který rozhoduje, takže „je přes celou šířku" neopravňuje ke 32 px
  výšce.
- Původní Fitts 1954 měl N = 52 studentů, 1D úlohu se stylusem na plechových terčích, u části pokusů
  výhradně praváky muže. Není to model obrazovky, je to model pohybu.

---

## Ověření hotového tlačítka

Nejlevnější kontrola před odevzdáním. Vzorem je USWDS, jediný systém v podkladu, který publikuje
testovací matici na komponentu: u tlačítka 9 testů proti WCAG 2.1 AA
(`designsystem.digital.gov/components/button/accessibility-tests/`).

1. V sekci je jedno primární tlačítko. Na celém pohledu nejvýš tři akcentní.
2. Každá varianta má v produktu jedno stálé mapování na roli v toku.
3. Pět stavů se od sebe pozná, focus není totéž co press.
4. Focus indikátor je vidět, splní 3:1, a nebyl odstraněn bez náhrady.
5. Hover je jen v `@media (hover: hover)`.
6. Nejmenší rozměr klikací plochy je 24 CSS px a víc.
7. Ikona nebo obrys, které nesou význam, mají 3:1 proti okolí.
8. Destruktivní akce má rozsah v labelu a potvrzovací krok, ne jen červenou.
9. Žádné disabled tlačítko bez zjevného důvodu blokace v okolí.
10. Varovná varianta se v produktu vyskytuje výjimečně, nebo vůbec.

---

## Co k tlačítkům v podkladech není

Vypsané schválně, aby se to příště nedomýšlelo.

- **Žádná studie na počet primárních tlačítek ani na výnos jednotlivých variant.** Material 3
  u své hierarchie sám přiznává, že publikovaný user test neexistuje. Celá kapitola „kolik a jaká
  varianta" je konvence.
- **Stav probíhající operace (loading, spinner v tlačítku) v podkladu chybí úplně.** Žádný
  z prověřených systémů k tomu v podkladu není citovaný, takže tady zatím žádné pravidlo nemáme.
- **Label: délka, slovosled, imperativ.** Nic měřitelného. Nejblíž je obecné UX writing, ne pravidlo
  o tlačítku.
- **Border-radius tlačítka.** Podklad má k tomu jen negativní zjištění: NHS tvrzení „rounded corners
  make things more clickable" je nedohledatelné ke zdroji (třída C, nejhorší podtyp, tváří se jako
  věda), meta-analýza preference zakřivení (Chuquichambi et al. 2022, 61 studií, 11 023 účastníků)
  u symbolického a prostorového designu efekt neprokázala a **neobsahuje ani jednu studii na UI**.
  Doménově shodná je jen Biswas et al. (2024, JCR, field experimenty na CTR), ale binárně curved vs
  sharp, žádná dose-response na konkrétní hodnotu radiusu. Kolující číslo „CTR o 17 až 55 % vyšší"
  se nepodařilo ověřit, **necitovat**.
- **GOV.UK A/B test zelených start buttonů** (GitHub issue #34) existuje a zvýšil click-through, ale
  podklad k němu nemá vzorek ani čísla. Neopírej o to volbu barvy a rozhodně z toho nedělej „zelená
  konvertuje".
- **Anti-pattern „nedávej warning nebo danger barvu na CTA, které není varování" se nepodařilo
  připsat Atlassianu.** Podklad fáze 1 ho cituje jako jejich formulaci, v jejich dokumentaci
  k tlačítku ale není (ověřeno 28. 8. 2026). Pravidlo v notě zůstává, zdroj u něj ne. Je to druhý
  případ v téhle notě, kdy se citace bez URL po dohledání rozpadla, první je NHS a zakulacené rohy.
- **Tlačítka v hustých mřížkách a tabulkách** (kolizní zóna s pravidlem 24 px) v podkladu nejsou.

---

## Souvisí

- [UX Laws](../zakony-principy/ux-laws.md): Fitts a Hick v populární podobě. **Pozor:** audit ve
  fázi 1 ukázal, že tamní podání Millera (7±2) a Hicka je pro UI nepoužitelné a Fitts je platný jen
  s limity uvedenými výše. Ta nota je určená k přepsání, ber ji jako slovník pojmů, ne jako oporu.
- [Design system DRIVE](../priklady-ds/design-system-drive.md): reálná ukázka, jak se tahle pravidla
  převedou na tokeny konkrétní komponenty včetně tlačítek.
- [Pravidlo 60-30-10](../color/pravidlo-60-30-10.md): kolik plochy může akcentní barva zabrat, což
  je druhá strana limitu na počet akcentních tlačítek.
- [Neuro-design master dokument](../../neuro-design/neuro-design-master.md): výpočet vizuální váhy
  prvku, hlubší vrstva pod hierarchií variant.
- [Tvar a radius](tvar-a-radius.md): proč tahle nota o radiusu tlačítka žádné pravidlo nemá a co
  místo toho platí.
- [Stroke a hranice](stroke-a-hranice.md): kdy obrys, kdy stín, kdy jen spacing. Přímo se to týká
  outline a ghost variant.
