# Pohyb

Kdy tuhle notu otevřít: chystáš se animovat cokoliv. Otevření modálu, dropdown, toast, přechod
mezi stavy, loading indikátor, hover, accordion, page transition.

Hlavní věc, kterou si odsud odnes: **pohyb v rozhraní není dekorace, je to informace o tom, odkud
prvek přišel a kam odešel.** Z toho plyne skoro každé číslo níž. Vstup zpomaluje, protože prvek
přilétá a zastavuje se. Odchod zrychluje, protože odlétá pryč. Trvání je krátké, protože uživatel
čeká na výsledek své akce, ne na animaci.

Druhá věc: **animace musí být přerušitelná.** Uživatel může kliknout znovu dřív, než skončí, a
většina "rozbitých" animací je rozbitá právě tímhle, ne špatnou křivkou.

## Rozhodovací postup

1. **Reaguje to na vstup uživatele?** (klik, hover, tap) → viditelná odezva do 100 ms, animace
   150 až 300 ms, `ease-out`, jako CSS transition.
2. **Přichází prvek na obrazovku?** → decelerate křivka (`ease-out`), delší trvání.
3. **Odchází prvek z obrazovky natrvalo?** → accelerate křivka (`ease-in`), kratší trvání než vstup.
4. **Hýbe se prvek v ploše a je vidět celou dobu?** → standard křivka (`ease-in-out`).
5. **Běží to samo a opakovaně?** (spinner, karusel, blikání) → nad 5 s musí jít zastavit,
   a rychlost drž ve středním pásmu, viz pravidlo o konvexním efektu.
6. **Poslední krok vždy:** co se stane při `prefers-reduced-motion: reduce`.

---

## Pravidla

### Trvání 150 až 300 ms, strop 400, nad 500 nikdy

**PRAVIDLO:** Default trvání animace 150 až 300 ms. 400 ms ber jako strop pro velký pohyb.
Nad 500 ms nejdi.
**KDY PLATÍ:** každá animace vyvolaná interakcí nebo změnou stavu.
**PROČ:** Animace stojí mezi akcí a výsledkem. Uživatel ji nesleduje jako scénu, čeká na
dokončení své akce. NN/g to formuluje přímo: "It is far more common for animations to be too long
than too short."
**TŘÍDA:** B (NN/g jako publikovaná konvence; sám článek přiznává, že doporučení vycházejí
z UX principů, ne z formální studie s časy)
**ZDROJ:** Page Laubheimer, *Executing UX Animations: Duration and Motion Characteristics*,
NN/g, 9. 2. 2020, verbatim: "In general, the duration of most animations should be in the range
of 100–500 ms", "At 500ms, animations start to feel like a real drag for users", "In most cases,
a range of 100–400 ms is appropriate, with 400ms being a very slow animation."
[nngroup.com/articles/animation-duration](https://www.nngroup.com/articles/animation-duration/).
Nezávisle se to shoduje s craft zdroji: Rauno Freiberg doporučuje do ~200 ms
([interfaces.rauno.me](https://interfaces.rauno.me/)), Emil Kowalski verbatim: "Your animations
should also usually be shorter than 300ms."
([emilkowal.ski/ui/great-animations](https://emilkowal.ski/ui/great-animations)).
**KDY NEPLATÍ:** jednoduchá zpětná vazba (checkbox, toggle) patří na ~100 ms, ne na 300.
Onboardingová nebo marketingová animace, kterou uživatel sleduje záměrně a nic za ní nečeká,
může být delší. A opakující se čekací animace se řídí jiným pravidlem, viz konvexní efekt.

### Trvání škáluj podle vzdálenosti a velikosti

**PRAVIDLO:** Čím větší vzdálenost nebo změna velikosti, tím delší animace. Nedávej stejné
trvání toggle switchi a full-screen panelu.
**KDY PLATÍ:** vždy, když v jednom systému animuješ prvky různých velikostí.
**PROČ:** Když má malý a velký prvek stejné trvání, velký se hýbe rychleji a čte se jako trhnutí,
malý naopak jako váhání. Konstantní je vnímaná rychlost, ne čas.
**TŘÍDA:** B (IBM Carbon)
**ZDROJ:** Carbon, verbatim: "Motion's duration should be dynamic based on the size of the
animation; the larger the change in distance or size, the longer the animation takes."
[carbondesignsystem.com/elements/motion/overview](https://carbondesignsystem.com/elements/motion/overview/).
Carbon k tomu má šest duration tokenů, od 70 ms (tlačítko, toggle) po 700 ms (ztmavení pozadí).
**KDY NEPLATÍ:** strop z předchozího pravidla platí i tady. Škálování neznamená, že full-screen
přechod dostane 900 ms.

### Vstup delší než odchod

**PRAVIDLO:** Odchodová animace kratší než vstupní. Typicky vstup 300 ms, odchod 200 až 250 ms.
**KDY PLATÍ:** modály, dropdowny, popovery, panely, toasty.
**PROČ:** Při vstupu se uživatel s prvkem seznamuje, potřebuje ho očima najít. Při odchodu už
rozhodl a čeká, až mu prvek uvolní cestu. Dlouhý odchod je čistá prodleva.
**TŘÍDA:** B (NN/g)
**ZDROJ:** [nngroup.com/articles/animation-duration](https://www.nngroup.com/articles/animation-duration/),
příklad popupu: příchod 300 ms, zmizení 200 až 250 ms.
**KDY NEPLATÍ:** destruktivní nebo nevratná akce, kde má odchod prvku dát krátký moment na
zaregistrování, co se stalo. A když prvek neodchází, jen se posune mimo výřez a zůstane po ruce
(side panel), tam se použije standard křivka, ne odchodová.

### Vstup decelerate, odchod accelerate, pohyb v ploše standard

**PRAVIDLO:** Přilétá na obrazovku → křivka, která začíná rychle a zpomaluje (`ease-out`,
decelerate). Odlétá natrvalo → křivka, která zrychluje (`ease-in`, accelerate). Je vidět celou
dobu a jen se přesouvá → symetrická standard křivka.
**KDY PLATÍ:** každý pohyb, u kterého prvek vzniká nebo mizí.
**PROČ:** Křivka kóduje, kde má pohyb energii. Prvek, který přilétá a zastavuje se, musí
zpomalovat, jinak vypadá, že narazil. Prvek, který odchází natrvalo, zrychluje, protože ho
už nesledujeme až k cíli. Carbon to zdůvodňuje tím, že u odchodu je "departure from the screen
is permanent", tedy nemá cenu animovat konec pohybu, který nikdo nedokoukává.
**TŘÍDA:** B (tři nezávislé organizace mají stejné rozdělení: IBM Carbon, Google Material 3
a doporučení NN/g)
**ZDROJ:** Carbon rozlišuje standard / entrance / exit easing s vlastními cubic-bezier hodnotami
([carbondesignsystem.com/elements/motion/overview](https://carbondesignsystem.com/elements/motion/overview/)).
Material 3 má tokeny `standard-decelerate` a `standard-accelerate`, respektive
`emphasized-decelerate` a `emphasized-accelerate`
([Google, `_md-sys-motion.scss`](https://raw.githubusercontent.com/material-components/material-web/main/tokens/versions/v0_192/_md-sys-motion.scss)).
Hodnoty v tabulce na konci noty.
**KDY NEPLATÍ:** pohyb, který má simulovat fyzikální objekt s hmotou (drag, swipe, pull to
refresh), tam patří spring, ne bezier. A `linear` je správná volba u rovnoměrných dějů:
rotující spinner, progress bar, běžící číslo.

### Na odezvu ovládacího prvku nikdy nedávej ease-in

**PRAVIDLO:** Animace, která je odpovědí na klik nebo hover, musí začít rychle. Použij `ease-out`.
`ease-in` a `ease-in-out` si nech pro odchody a pro přesuny v ploše.
**KDY PLATÍ:** hover, press, focus, otevření menu, expand.
**PROČ:** `ease-in` začíná pomalu. Prvních 50 ms se skoro nic nestane, a přesně v tom okně
uživatel vyhodnocuje, jestli systém zareagoval. NN/g to říká přímo: takové křivky "can feel
unresponsive if the initial motion takes a little while to get going". Emil Kowalski to obrací
do pozitivního tvrzení: `ease-out` "starts fast and slows down at the end, which gives the
impression of a quick response".
**TŘÍDA:** B (NN/g jako publikovaná konvence), craft potvrzení C (Emil Kowalski)
**ZDROJ:** [nngroup.com/articles/animation-duration](https://www.nngroup.com/articles/animation-duration/),
[emilkowal.ski/ui/great-animations](https://emilkowal.ski/ui/great-animations).
**KDY NEPLATÍ:** odchodové animace, kde je pomalý start žádoucí. A když je celkové trvání pod
~120 ms, kde je rozdíl mezi křivkami pod rozlišovací schopnost.

### Odezva na vstup do 100 ms, jinak už to není animace, ale čekání

**PRAVIDLO:** Od kliku k první viditelné změně maximálně 100 ms. Když výsledek nemůže přijít
do 1 s, ukaž stav (spinner, skeleton, progres), ne prázdno.
**KDY PLATÍ:** každá interakce, obzvlášť ta, která spouští síťový požadavek.
**PROČ:** Pod 0,1 s uživatel vnímá reakci jako okamžitou a drží pocit přímé manipulace. Do 1 s
si udrží tok myšlenky, ale okamžitost už je pryč. Nad 10 s odchází pozornost jinam. To jsou
limity vnímání, ne konvence UI.
**TŘÍDA:** B pro čísla (publikovaná konvence NN/g, ale s primárními referencemi: R. B. Miller,
*Response time in man-computer conversational transactions*, AFIPS 1968; Card, Robertson,
Mackinlay, CHI '91)
**ZDROJ:** [nngroup.com/articles/response-times-3-important-limits](https://www.nngroup.com/articles/response-times-3-important-limits/),
verbatim: 0,1 s je "limit for having the user feel that the system is reacting instantaneously",
1,0 s "limit for the user's flow of thought to stay uninterrupted", 10 s "limit for keeping the
user's attention focused on the dialogue".
**KDY NEPLATÍ:** nikdy jako cíl, často jako realita. Ale nepleť si to s trváním animace: tohle
je o latenci odezvy systému, ne o tom, jak dlouho má běžet přechod.
**POZOR na tradovaný doplněk:** v UX blozích koluje "Doherty threshold 400 ms" (Doherty
a Thadhani, IBM Systems Journal 1982) spolu s konkrétními čísly o nárůstu produktivity. Primární
text jsem neověřoval a čísla, která kolují sekundárně, neuvádím. Nepoužívej to jako oporu, dokud
to někdo nepřečte v originále.

### Animace musí být přerušitelná, proto CSS transition, ne keyframes

**PRAVIDLO:** Animuj přes `transition`, ne `@keyframes`, kdykoliv může uživatel stav změnit
během běhu animace.
**KDY PLATÍ:** cokoliv, co se dá zavřít, přepnout, odswipovat nebo kliknout dvakrát: toast,
dropdown, modál, accordion, tab.
**PROČ:** `transition` interpoluje z aktuální hodnoty. Když se stav změní v polovině, plynule
pokračuje z místa, kde prvek je. Keyframe animace má pevný začátek a konec, takže při přerušení
skočí. Uživatel to nevidí jako "špatnou křivku", vidí to jako glitch.
**TŘÍDA:** C (řemeslná praxe, Emil Kowalski, autor knihoven Sonner a Vaul)
**ZDROJ:** [emilkowal.ski/ui/building-a-toast-component](https://emilkowal.ski/ui/building-a-toast-component)
používá enter transition 400 ms ease jako CSS transition právě proto, že transition je
přerušitelná. Obecněji [emilkowal.ski/ui/great-animations](https://emilkowal.ski/ui/great-animations):
uživatel má umět "change the state of the animation at any time while maintaining a smooth
transition"; u Framer Motion se to musí nastavit explicitně, CSS to má zdarma.
**KDY NEPLATÍ:** nekonečné dekorativní smyčky (spinner, pulzující tečka, shimmer skeleton), kde
není co přerušovat. Tam jsou keyframes správná volba.

### Animuj transform a opacity, ne layout vlastnosti

**PRAVIDLO:** Pohyb dělej `transform` (translate, scale, rotate) a průhlednost `opacity`.
Neanimuj `width`, `height`, `top`, `left`, `margin`, `padding`.
**KDY PLATÍ:** vždy, a tvrdě na mobilu a v dlouhých seznamech.
**PROČ:** `transform` a `opacity` se vyhodnotí až v compositing kroku, tedy mimo layout a paint.
Animace `padding` nebo `margin` spustí celou trojici layout, paint, composite pro každý frame,
a u vnořené struktury se to násobí. Hardwarově akcelerovaná CSS animace navíc drží plynulost
i když je main thread zatížený, na rozdíl od animací poháněných JS smyčkou.
**TŘÍDA:** C (craft zdroj, Emil Kowalski; mechanismus je vlastnost renderovacích engine, ale
vendorskou dokumentaci jsem k tomu neověřoval)
**ZDROJ:** [emilkowal.ski/ui/great-animations](https://emilkowal.ski/ui/great-animations),
verbatim doporučuje "`transform` and `opacity` as they only trigger the third rendering step
(composite)" a varuje, že "padding or margin triggers all three".
**KDY NEPLATÍ:** změna výšky obsahu, kterou `transform` neumí (accordion s neznámou výškou).
Tam je řešení `grid-template-rows` s interpolací nebo měření výšky, ne animace `height` na jistotu.

### Škáluj proporcionálně, scale 0.96 ne 0.8

**PRAVIDLO:** Změny velikosti drž jemné. Pro press stav nebo vstup prvku ber `scale(0.96)`,
ne `scale(0.8)`.
**KDY PLATÍ:** press feedback, vstup dialogu, stacking karet, hover zvětšení.
**PROČ:** Velký skok velikosti nemá v rozhraní fyzický korelát. Prvek nemá důvod měnit velikost
o pětinu, takže to čte jako efekt, ne jako chování objektu. Rauno Freiberg to shrnuje tak, že
velký skok působí levně.
**TŘÍDA:** C (řemeslná praxe, Rauno Freiberg, Staff Design Engineer Vercel)
**ZDROJ:** [interfaces.rauno.me](https://interfaces.rauno.me/), Web Interface Guidelines.
Emil Kowalski má u stackovaných toastů konkrétní odvození stejného typu: `scale 0.05 * index`,
tedy druhý toast 0,9 a třetí 0,85
([emilkowal.ski/ui/building-a-toast-component](https://emilkowal.ski/ui/building-a-toast-component)).
**KDY NEPLATÍ:** přechod, kde se prvek opravdu mění na jinou věc (thumbnail se rozbalí do
full-screen obrázku). Tam je velký scale správný, protože to je shodná identita ve dvou
velikostech, ne feedback.

### prefers-reduced-motion: nahraď posun fadem, nevypínej všechno

**PRAVIDLO:** V `@media (prefers-reduced-motion: reduce)` nahraď pohyb a změnu velikosti za
prolnutí opacity, případně zkrať trvání. Nesázej na `animation: none` a `transition: none`
globálně.
**KDY PLATÍ:** každá animace, která není esenciální pro informaci nebo funkci.
**PROČ:** Problematické je zvětšování a posouvání velkých objektů, což jsou vestibulární
triggery. Změna barvy, opacity nebo blurru **bez** změny pozice a velikosti se za motion animation
podle WCAG 2.3.3 vůbec nepočítá, takže fade je z hlediska kritéria bezpečná náhrada. Když ale
pohyb vypneš úplně, přijdeš o kontinuitu: uživatel neuvidí, že se něco změnilo, a to je horší
než klidnější varianta. Media query se jmenuje reduced, ne no motion, a MDN mluví o rozhraní,
které "removes, reduces, or replaces motion-based animations".
**TŘÍDA:** A pro požadavek (WCAG 2.3.3 Animation from Interactions, AAA, nové ve WCAG 2.1),
B pro implementační vzor (MDN a W3C sufficient techniques).
**ZDROJ:** [MDN, prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion),
příklad v dokumentaci nahrazuje `pulse` (scale) za `dissolve` (jen opacity) a komentuje to jako
"Tone down to a less motion-intense animation".
[W3C, Understanding SC 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html):
definice motion animation je "addition of steps between conditions to create the illusion of
movement or to give a sense of a smooth transition", esenciální je jen to, jehož odstranění by
"fundamentally change the information or functionality"; dopady jsou "dizziness, nausea and
headaches"; doporučení je "take advantage of the reduce motion feature in the user agent or
operating system".
**KDY NEPLATÍ:** animace, která nese informaci a nedá se předat jinak (průběh nahrávání,
znázornění, jak se dvě věci spojily). Tu smíš nechat, ale zeslab ji na minimum a nikdy z ní
nedělej parallax.
**Praktická poznámka:** Emil Kowalski dělá totéž konkrétně, tedy z bounce animace se pod reduced
motion stane jen fade ([emilkowal.ski/ui/great-animations](https://emilkowal.ski/ui/great-animations)).

### Automatický pohyb nad 5 sekund musí jít zastavit

**PRAVIDLO:** Cokoliv se hýbe, bliká, scrolluje nebo se samo aktualizuje, startuje bez zásahu
uživatele, běží déle než 5 s a je vedle jiného obsahu, potřebuje ovládání pause / stop / hide.
U auto-aktualizace platí požadavek bez pětisekundové výjimky.
**KDY PLATÍ:** karusely, autoplay video, animované bannery, marquee, živě se obnovující tabulky
a dashboardy, tickery.
**PROČ:** Pohyb vedle textu odvádí pozornost a u části uživatelů znemožňuje čtení úplně. Tohle
není doporučení, je to kritérium úrovně A, tedy minimální úroveň souladu.
**TŘÍDA:** A jiného druhu než studie: normativní požadavek. Úroveň A, v normě od WCAG 2.0.
**ZDROJ:** [W3C, Understanding SC 2.2.2 Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html),
verbatim jádro: "for any moving, blinking or scrolling information that (1) starts automatically,
(2) lasts more than five seconds, and (3) is presented in parallel with other content, there is
a mechanism for the user to pause, stop, or hide it unless the movement, blinking, or scrolling
is part of an activity where it is essential".
**KDY NEPLATÍ:** pohyb, který je podstatou aktivity (přehrávač videa, hra, animace, kterou si
uživatel sám pustil). A loading indikátor u operace, která končí sama, protože k tomu doplňuje
2.2.2 výjimku pro nezbytnou aktivitu. Přesto viz další pravidlo, tam je o spinnerech víc.

### Rychlost opakující se čekací animace drž ve středním pásmu

**PRAVIDLO:** U spinneru a loaderu nevol ani velmi pomalou, ani velmi rychlou rotaci. Střední
tempo, řádově jedna otáčka za 2 až 2,5 s, minimalizuje vnímanou dobu čekání. Rychlá rotace
(řádově 0,4 až 0,5 s na otáčku) vnímané čekání prodlužuje, stejně jako velmi pomalá.
**KDY PLATÍ:** čekací animace, které uživatel nevyvolal a nemá je jak zkrátit (page load,
odesílání formuláře, zpracování).
**PROČ:** Vztah mezi rychlostí animace a vnímaným časem není lineární, ale konvexní. Lidé
odvozují dobu čekání z rychlosti animace, a středně rychlá animace zároveň víc přitahuje
pozornost než statický obrázek nebo než animace rychlá, takže odvádí pozornost od času.
**TŘÍDA:** A (peer-reviewed, 6 hlavních experimentů plus pilotní studie, řádově 7 000 účastníků,
efekt replikovaný až do click-to-landing rate, konverze a hodnocení produktu při mobilním nákupu)
**ZDROJ:** Ding, Y., & Kyung, E. J. *Optimizing Animation Speed: Convex Effects on Perceived
Waiting Time and Digital Customer Experience*. Journal of Consumer Research, 53(1), 136-161.
DOI [10.1093/jcr/ucaf037](https://doi.org/10.1093/jcr/ucaf037). Verbatim z abstraktu: "although
prior research suggests a linear relationship in which faster animations reduce perceived waiting
time, we find a convex relationship between animation speed and time perception: moderate-speed
animations minimize perceived waiting time compared to no, slow-moving, or fast-moving animations".
**KDY NEPLATÍ:** studie měřila opakující se čekací animace (rotující kola, kroužky, tvary), ne
přechody v rozhraní. Nepřenášej to na trvání vstupní animace modálu. Efekt navíc slábne, když
animace odvede pozornost od rychlosti pohybu jinam (dual-attention prvky nebo atypická animace),
takže progres bar s procenty se řídí jinou logikou než neurčitý spinner.
**Nově dohledáno** mimo rámec vaultu, fáze 1 tenhle zdroj nepokryla.

### Neodůvodňuj trvání animace luxusem ani responzivitou

**PRAVIDLO:** Nepiš do design rozhodnutí, že animace je pomalá, protože to působí luxusně, ani
že je rychlá, protože to působí responzivně. Odůvodni ji vzdáleností, velikostí prvku a tím, jak
dlouho uživatel čeká na výsledek.
**KDY PLATÍ:** psaní design specifikace, code review, obhajoba návrhu.
**PROČ:** Obě věty jsou tradované a evidence pro ně je jinde, než se tvrdí:
- **"Pomalé = luxus"** má reálnou oporu, ale ve videoreklamě, ne v rozhraní. Jung a Dubois
  (2023), 12 experimentů, N = 27 227, tři země: produkt zobrazený ve slow motion je vnímaný jako
  luxusnější, mechanismus je zvýšené ponoření a z něj vyšší očekávaná hedonická hodnota. Ani jeden
  z těch experimentů netestoval rozhraní ani interaktivní produkt, testovalo se pasivní sledování
  videa. Aplikovat to na trvání UI animace je skok mezi doménami, stejný typ chyby jako citovat
  Bar a Neta na border-radius. Fáze 1 průzkumu navíc u luxury sektoru zaznamenala "pomalé animace
  = kvalita" jako nenalezeno, žádný zdroj to netvrdí o rozhraní.
- **"Rychlé = responzivní"** má oporu jen pro latenci odezvy systému (Miller 1968, limity 0,1 a
  1 s), ne pro trvání animace jako takové. Pro animace je to konvence, ne měření: NN/g říká, že
  animace jsou častěji moc dlouhé než moc krátké, ale žádná čísla z formální studie k tomu neuvádí.
- Ke stejnému místu jde i výsledek proti intuici: u čekacích animací **není** rychlejší lepší,
  vztah je konvexní (Ding a Kyung, viz pravidlo výše). Takže "rychlejší = lepší pocit" neplatí
  ani tam, kde by se to čekalo nejvíc.

**TŘÍDA:** C pro obě populární tvrzení v UI kontextu (tradovaná moudrost bez opory na rozhraních).
Jung a Dubois je sám třída A, ale pro jinou doménu než rozhraní.
**ZDROJ:** Jung, S., & Dubois, D. (2023). *When and How Slow Motion Makes Products More
Luxurious*. Journal of Marketing Research, 60(6), 1177-1196.
DOI [10.1177/00222437221146728](https://doi.org/10.1177/00222437221146728).
[nngroup.com/articles/animation-duration](https://www.nngroup.com/articles/animation-duration/).
Ding & Kyung, DOI [10.1093/jcr/ucaf037](https://doi.org/10.1093/jcr/ucaf037).
**KDY NEPLATÍ:** marketingová stránka nebo produktové video, kde opravdu jde o pasivní sledování
a ne o interakci. Tam je Jung a Dubois relevantní zdroj a pomalejší tempo je obhajitelné.
**Nově dohledáno** mimo rámec vaultu.

---

## Referenční hodnoty, ověřené

### Easing křivky

Material Design 3, tokeny z Googlem publikovaného souboru
([`_md-sys-motion.scss`](https://raw.githubusercontent.com/material-components/material-web/main/tokens/versions/v0_192/_md-sys-motion.scss)):

| Token | cubic-bezier | Kdy |
|---|---|---|
| `standard` | `0.2, 0, 0, 1` | default, prvek je vidět celou dobu |
| `standard-decelerate` | `0, 0, 0, 1` | vstup na obrazovku |
| `standard-accelerate` | `0.3, 0, 1, 1` | odchod z obrazovky |
| `emphasized` | `0.2, 0, 0, 1` | výraznější přechod, delší trvání |
| `emphasized-decelerate` | `0.05, 0.7, 0.1, 1` | výrazný vstup |
| `emphasized-accelerate` | `0.3, 0, 0.8, 0.15` | výrazný odchod |
| `linear` | `0, 0, 1, 1` | rovnoměrné děje: spinner, progres |

IBM Carbon, dvě sady podle povahy produktu, productive pro pracovní nástroje a expressive pro
výraznější momenty ([carbondesignsystem.com/elements/motion/overview](https://carbondesignsystem.com/elements/motion/overview/)):

| Typ | Productive | Expressive |
|---|---|---|
| Standard | `0.2, 0, 0.38, 0.9` | `0.4, 0.14, 0.3, 1` |
| Entrance | `0, 0, 0.38, 0.9` | `0, 0, 0.3, 1` |
| Exit | `0.2, 0, 1, 0.9` | `0.4, 0.14, 1, 1` |

Vzor si všimni sám: entrance má první dvě čísla nulová (okamžitý rozjezd), exit má poslední dvě
čísla vysoká (na konci pořád zrychluje). To je celý mechanismus zapsaný do čtyř čísel.

### Trvání

| Zdroj | Hodnoty |
|---|---|
| Carbon duration tokeny | 70 ms tlačítko/toggle · 110 ms fade · 150 ms malé rozbalení · 240 ms toast a systémové zprávy · 400 ms velké rozbalení · 700 ms ztmavení pozadí |
| Material 3 duration tokeny | short 50 / 100 / 150 / 200 · medium 250 / 300 / 350 / 400 · long 450 / 500 / 550 / 600 · extra-long 700 / 800 / 900 / 1000 |
| NN/g doporučení | 100 ms jednoduchý feedback · 200 až 300 ms podstatná změna obrazovky · 400 ms strop · 500 ms už "a real drag" |

Material má 16 duration tokenů, což neznamená, že máš používat 16 hodnot. Znamená to, že máš mít
uzavřenou množinu, ze které vybíráš, a Materialovo rozdělení na short / medium / long / extra-long
je použitelná první dělicí linka.

### Konkrétní parametry z praxe, třída C

Z Emila Kowalského, autora Sonner a Vaul
([emilkowal.ski/ui/building-a-toast-component](https://emilkowal.ski/ui/building-a-toast-component)):
vstupní transition 400 ms ease jako CSS transition, stacking `scale 0.05 * index`, swipe threshold
velocity nad 0,11 zahodit. Jsou to hodnoty z konkrétní produkční komponenty, nikoliv obecně
platná čísla. Ber je jako startovní bod, ne jako normu.

## Souvisí

- [Hloubka a stíny](hloubka-a-stiny.md) pro to, co se má vlastně objevit, tedy pro vrstvy
  a elevaci plovoucích prvků.
- [GENERAL UX KNOWLEDGE](../ux-zaklady/general-ux-knowledge.md) pro zpětnou vazbu a afordanci,
  což je důvod, proč se pod 100 ms hraje.
- [Design system DRIVE](../priklady-ds/design-system-drive.md) jako příklad, jak se mikrointerakce
  a jejich hodnoty zapisují do hotového systému.
- [Etika v UX](../ux-zaklady/etika-v-ux.md) pro hranici mezi vedením pozornosti a manipulací,
  což je u pohybu tenká linka.
