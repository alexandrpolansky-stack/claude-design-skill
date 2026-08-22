# Anti-slop: markery generického a špatného vzhledu

Seznam konkrétních vizuálních znaků, po kterých člověk pozná, že rozhraní vzniklo za dvě hodiny bez
rozhodování. Používej ho dvakrát: jako zákaz při stavbě a jako checklist před odevzdáním.

**Co tahle nota NENÍ:** není to seznam věcí, které jsou samy o sobě ošklivé. Zaoblená karta, gradient
ani dark mode nejsou chyba. Chyba je použít je bez rozhodnutí, ve výchozí kombinaci, kterou má
i tisíc jiných stránek, a nechat je porušit kontrast nebo afordanci. Marker není verdikt, je to
signál "tady se nerozhodovalo".

**Třídy důkazu:** **A** = tvrdá opora (peer-reviewed studie, právní požadavek, normativní text).
**B** = publikovaná konvence nebo dohledatelné publikované pozorování. **C** = řemeslná praxe bez
měření. U třídy C nehledej falešnou oporu, radši ji nech jako C.

Související: [Formuláře a stavy](formulare-a-stavy.md) ·
[Pravidlo 60-30-10](../color/pravidlo-60-30-10.md) ·
[Osmibodová mřížka](../zakony-principy/osmibodova-mrizka.md) ·
[Font pairing](../typography/font-pairing.md) · [Grafické trendy](../trendy/graficke-trendy.md)

---

## Nejdřív rám: proti čemu se tady vlastně stojí

### Nízká kvalita nekoreluje s použitím AI, ale s časem a údržbou

**PRAVIDLO:** Nehodnoť výstup podle toho, jestli u něj byl AI nástroj. Hodnoť ho podle znaků
investovaného času: dořešené stavy, konzistentní škály, opravené hrany, známky údržby. Když je
předmětem kritiky "vypadá to jako AI", přelož si to na "vypadá to jako výchozí nastavení, kterým se
nikdo nezabýval", a hledej konkrétní markery níž.
**KDY PLATÍ:** Vždy, i při vlastním review.
**PROČ:** Markery, které lidé čtou jako "AI vzhled", jsou defaulty. Vznikají stejně, když vývojář
vysype knihovnu bez rozhodnutí. Rozdíl mezi dobrým a špatným výstupem je počet učiněných rozhodnutí,
ne nástroj.
**TŘÍDA:** B, publikované pozorování z velké technické diskuse, ne měření.
**ZDROJ:** HN vlákno "Scoring Show HN submissions for AI design patterns", 333 bodů, 235 komentářů.
Verbatim z vlákna: "vibe-coded projects... show no evidence of long term maintenance. That might be
the new signal" a "You can take 2 months or 2 hours. HN is flooded by the latter."
https://news.ycombinator.com/item?id=47864393
**KDY NEPLATÍ:** Nikdy jako výmluva. "Kvalita nezávisí na nástroji" neznamená, že výchozí výstup je
v pořádku. Znamená, že se do něj musí zasáhnout.

### Homogenizace webu je měřená a její příčina není lenost

**PRAVIDLO:** Když ti něco přijde generické, ověř si, jestli to není konvence, která má funkci.
Sdílené knihovny, standardizované palety a mobilní podpora sblížily layouty měřitelně. Odchyluj se
tam, kde odchylka něco přinese, ne proto, abys nebyl podobný.
**KDY PLATÍ:** Před každým rozhodnutím "udělám to jinak, protože takhle to má každý".
**PROČ:** Sblížení layoutů je technický a device jev, ne selhání designérů. Zaútočit na konvenci
proto, že je konvence, znamená zaplatit orientací uživatele bez protihodnoty.
**TŘÍDA:** A pro měření sblížení (peer-reviewed CHI paper), B pro odvozený imperativ.
**ZDROJ:** Goree, S., Doosti, B., Crandall, D., Su, N. M. (2021). CHI '21,
DOI 10.1145/3411764.3445156. Computer vision nad weby 2003 až 2019, layouty se sblížily o více než
30 % od roku 2007. Uvedené příčiny: sdílené knihovny a kód, standardizace palet, mobilní podpora.
Doprovodná diskuse: HN "Why do all websites look the same", 269 bodů.
https://news.ycombinator.com/item?id=18414001
**KDY NEPLATÍ:** Povrchová vrstva (paleta, písmo, motion, foto). Tam je odchylka legitimní, viz
poslední sekce téhle noty.

---

## Markery s oporou (A a B)

### Barevný levý okraj karty

**PRAVIDLO:** Nedávej kartám ani boxům barevný svislý pruh na levé hraně jako výchozí dekoraci.
Barevný levý okraj používej jen tam, kde nese kategorii nebo závažnost, a pak konzistentně
(například tři definované stavy: info, varování, chyba), nikdy na všech kartách stejně.
**KDY PLATÍ:** Karty, panely, boxy s obsahem, callouty.
**PROČ:** Je to nejcitovanější jednotlivý marker generického vzhledu vůbec. Když má pruh každá karta
a nic neznamená, je to jen barva navíc.
**TŘÍDA:** B
**ZDROJ:** HN 47864393, verbatim: "colored left borders are almost as reliable a sign of
AI-generated design as em-dashes". https://news.ycombinator.com/item?id=47864393
**KDY NEPLATÍ:** Systémy, kde levý pruh je definovaný token se sémantikou (citace, diff, log level,
severity v monitoringu). Tam nese informaci a je správně.

### Dark mode s fialovým nebo hnědým textem na tmavém pozadí

**PRAVIDLO:** V dark mode neber tělo textu do fialové, hnědé ani jiné tónované šedi jen proto, že
"ladí". Změř kontrast: tělo textu 4,5:1, velký text 3:1. Fialový text na fialovém pozadí a béžový
text na hnědém typicky padají pod 4:1.
**KDY PLATÍ:** Každý dark mode, každá tmavá sekce světlého webu.
**PROČ:** Je to zároveň nejčastější marker generického dark modu a zároveň porušení WCAG 1.4.3,
tedy v EU u e-commerce, bankovnictví a u českého státního klienta právní problém, ne estetický.
**TŘÍDA:** A pro kontrastní práh, B pro fialovou a hnědou jako marker.
**ZDROJ:** WCAG 2.2 SC 1.4.3 Contrast (Minimum), Level AA, 4,5:1 pro text a 3:1 pro velký text.
https://www.w3.org/WAI/WCAG22/quickref/ · HN 47864393, verbatim: "dark-mode sites... text (and
subtext) are various shades of dark brown or beige", "how many dark mode websites with purple there
are right now", "purple-on-purple-with-glowing-purple mess".
https://news.ycombinator.com/item?id=47864393
**KDY NEPLATÍ:** Dekorativní text, logo a vypnutý (disabled) stav jsou z 1.4.3 vyňaté. To ale
neznamená, že je dobré udělat je nečitelné.

### Mřížka zakulacených karet s ikonou nebo emoji v hlavičce

**PRAVIDLO:** Sekci "features" nestav automaticky jako tři nebo šest stejných zakulacených karet
s ikonou nahoře, nadpisem a dvěma řádky textu. Když sáhneš po kartách, musí mít karta důvod:
oddělitelný obsah, na který se dá klikat nebo který se dá řadit. Když to je jen odstavec s ikonou,
udělej z toho odstavec s ikonou.
**KDY PLATÍ:** Landing pages, marketing sekce, dashboardy s "přehledem".
**PROČ:** Je to nejrozpoznatelnější výchozí layout generovaného webu. Zároveň karta bez interakce
platí za orámování, které neslouží ničemu.
**TŘÍDA:** B pro marker, C pro tvrzení o zbytečném orámování (řemeslná praxe, Refactoring UI radí
příliš mnoho borderů nahradit spacingem nebo kontrastním pozadím).
**ZDROJ:** HN 47864393, verbatim: "grid of rounded rects" s kartami s ikonou nahoře.
https://news.ycombinator.com/item?id=47864393
**KDY NEPLATÍ:** Skutečně kartový obsah: produkty, položky feedu, dlaždice s vlastní akcí. Tam je
karta správná komponenta.

### Bezokrajové prvky a plochý styl bez signifikátoru klikatelnosti

**PRAVIDLO:** Každý klikatelný prvek musí mít viditelný signifikátor, který ho odlišuje od
neklikatelného textu: rámeček s kontrastem alespoň 3:1, podtržení, výplň nebo jasně jiná barva.
Nespoléhej na to, že "z kontextu je to jasné". To platí i pro vstupní pole a ikonová tlačítka.
**KDY PLATÍ:** Vždy. Tohle je nejdražší marker v celé notě, protože nekazí jen vzhled, ale funkci.
**PROČ:** Naměřeno: se slabými signifikátory lidé strávili na stránce v průměru o 22 % víc času
a udělali o 25 % víc fixací, a u nejtvrdšího případu našla cílový odkaz jen polovina uživatelů proti
86 % ve verzi se silnými signifikátory. Zároveň WCAG 1.4.11 (AA) vyžaduje 3:1 na okraje UI komponent,
takže "invisible UI" bez rámečků není jen odvážné, je to nesoulad s AA.
**TŘÍDA:** A
**ZDROJ:** Kate Moran, Flat UI Elements Attract Less Attention and Cause Uncertainty, NN/g,
3. 9. 2017. Eye-tracking, N = 71, between-subjects, devět dvojic stránek. Nejtvrdší případ: 50 %
(12/24) vs 86 % (25/29) uživatelů zaměřilo cílový odkaz, p < 0,005. Verbatim: "The problem is not
that users never see a weakly signified UI element."
https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/ ·
Kate Moran, Flat Design: Its Origins, Its Problems, and Why Flat 2.0 Is Better for Users, NN/g,
27. 9. 2015. https://www.nngroup.com/articles/flat-design/ ·
WCAG 2.2 SC 1.4.11 Non-text Contrast, Level AA. https://www.w3.org/WAI/WCAG22/quickref/
**KDY NEPLATÍ:** Nikdy pro klikatelné prvky. U dekorativní grafiky 1.4.11 neplatí a signifikátor
tam nemá co dělat.

### Přehuštěný monospace v terminálové estetice

**PRAVIDLO:** Monospace nepoužívej na tělo textu, nadpisy a navigaci současně. Drž ho na kód, data,
identifikátory a tabulková čísla. Když už jde o záměrnou terminálovou estetiku, neseškrtávej řádkovou
délku a řádkování na hustotu skutečného terminálu.
**KDY PLATÍ:** Landing pages a docs pro technické produkty, kde je pokušení největší.
**PROČ:** Monospace má jinou šířku znaku, takže při stejné šířce sloupce nese jiný počet znaků, a
v souvislém textu má nižší čitelnost. Delší řádek než ~75 znaků pak stojí čtení.
**TŘÍDA:** B pro marker (HN), B pro délku řádku (Bringhurst 45 až 75 znaků, ideál 66, se nezávisle
potkává s webovou praxí 40 až 80).
**ZDROJ:** HN 47864393, verbatim: "using that somewhat hard to read console-ish font Claude seems to
love" a "cram huge amounts of tiny text into every visible inch".
https://news.ycombinator.com/item?id=47864393 ·
Bringhurst, R., *The Elements of Typographic Style*, 45 až 75 znaků na řádek (podrobná klasifikace
v průzkumu fáze 1, vrstva D).
**KDY NEPLATÍ:** Skutečná konzole, editor kódu, log viewer, monitoring. Tam je monospace obsah,
ne dekorace.

### Přehuštěný drobný text jako výplň prostoru

**PRAVIDLO:** Nezaplňuj každý volný pixel dalším řádkem drobného textu. Když je na obrazovce
prázdno, je to rozhodnutí, ne chyba k opravě.
**KDY PLATÍ:** Landing pages, dashboardy, karty s metrikami.
**PROČ:** Hustota drobného textu je jmenovaný marker generovaného vzhledu a zároveň porušuje WCAG
1.4.12 Text Spacing (AA), pokud je řádkování zamčené pod 1,5.
**TŘÍDA:** B pro marker, A pro spacing práh.
**ZDROJ:** HN 47864393, verbatim: "cram huge amounts of tiny text into every visible inch".
https://news.ycombinator.com/item?id=47864393 · WCAG 2.2 SC 1.4.12 Text Spacing, Level AA, nové
v 2.1: line-height alespoň 1,5×, odstavcové mezery alespoň 2×, letter-spacing 0,12×, word-spacing
0,16×. https://www.w3.org/WAI/WCAG22/quickref/
**KDY NEPLATÍ:** Datová mřížka a tabulka pro experta, kde je hustota funkce a uživatel ji chce.
I tam ale musí layout přežít override řádkování.

### Celá stránka postavená na jedné silné barevné rodině

**PRAVIDLO:** Nestav celou stránku z odstínů jedné výrazné barvy (fialová na fialové s fialovým
glowem, všechno modré, všechno tmavě zelené). Drž poměr základní/doplňková/akcentní barva a akcent
používej střídmě.
**KDY PLATÍ:** Volba palety u čehokoliv veřejného.
**PROČ:** V měřeném srovnání designových kategorií byl typ "silná barva jedné rodiny" hodnocen
esteticky nejhůř, a nejlepší paměťovou výbavnost měl vyvážený poměr obrázek a text. Zároveň je to
jmenovaný marker generovaného dark modu.
**TŘÍDA:** B
**ZDROJ:** Douneva, M., Jaron, R., Thielsch, M. T. (2015/2016). *Interacting with Computers* 28(4),
552-567, N = 458. Tři kategorie designu: SCOFA (silná barva jedné rodiny), LAPIC (velké obrázky),
SAPAT (vyvážený poměr obrázek a text). LAPIC a SAPAT hodnoceny esteticky lépe než SCOFA, SAPAT má
nejlepší paměťovou výbavnost. (Přeneseno z průzkumu fáze 1, sekce o kontextové podmíněnosti.) ·
HN 47864393 k fialovému dark modu. https://news.ycombinator.com/item?id=47864393 ·
Praktický poměr: [Pravidlo 60-30-10](../color/pravidlo-60-30-10.md) (vrstva 3, poměr je třída C; nota nese override k hodnotám barev).
**KDY NEPLATÍ:** Brand, který jednu barvu vlastní a má ji ukotvenou (a i tam se řeší poměr, ne
monochrom). A pozor na protipříklad: v jedné diplomce ze stejné laboratoře vyšly méně typické palety
atraktivnější, takže mechanické kopírování palety sektoru není bezpečná cesta.

---

## Markery z řemeslné praxe (C)

Tyhle nejsou měřené. Jsou to konvence, se kterými se dá nesouhlasit. Neuváděj je jako výzkum.

### Gradient bez funkce

**PRAVIDLO:** Gradient používej jen tam, kde něco dělá: vytváří hloubku, oddělí vrstvu, zajistí
čitelnost textu nad obrázkem (překryv), nebo nese brand. Nedávej gradient na tlačítka, karty
a nadpisy jako výchozí dekoraci, a nedělej gradient přes dva vzdálené odstíny (fialová do tyrkysové).
**KDY PLATÍ:** Kdykoliv sahá po gradientu.
**PROČ:** Gradient přes dva vzdálené odstíny mění kontrast textu po délce prvku, takže část textu
splní kontrast a část ne.
**TŘÍDA:** C. Kontrastní část se dá ověřit měřením, samotný zákaz dekorativního gradientu je konvence.
**ZDROJ:** obecně uznávaná praxe. Nemá publikovanou oporu, kterou bych ověřil.
**KDY NEPLATÍ:** Překryv nad fotkou, kde je gradient jediný způsob, jak udržet text čitelný nad
proměnlivým podkladem. To je funkce.

### Glassmorphism a neumorphism

**PRAVIDLO:** Nepoužívej průhledné rozostřené panely (glassmorphism) a jemné vystouplé plochy bez
okraje (neumorphism) na nic interaktivního. Jako dekorace na neinteraktivní vrstvě je to volba, jako
tlačítko nebo pole je to chyba.
**KDY PLATÍ:** Tlačítka, pole, přepínače, karty s akcí.
**PROČ:** Oba efekty stojí na jemném rozdílu proti pozadí, tedy přesně na tom, co WCAG 1.4.11 zakazuje
u UI komponent (potřeba 3:1). U glassmorphism se navíc kontrast textu mění podle toho, co je pod
panelem, takže ho nelze staticky garantovat.
**TŘÍDA:** C pro zákaz jako takový, A pro kontrastní požadavek, ze kterého vyplývá.
**ZDROJ:** odvozeno z WCAG 2.2 SC 1.4.11 Non-text Contrast (AA).
https://www.w3.org/WAI/WCAG22/quickref/ Samotné spojení "tedy nepoužívej glassmorphism" je moje
odvození, ne citace.
**KDY NEPLATÍ:** Dekorativní vrstva bez textu a bez interakce (pozadí, ozdobný panel), kde se
kontrast neměří.

### Skeuomorfní a 3D efekt na plochém rozhraní

**PRAVIDLO:** Nemíchej vržené stíny s hloubkou, zkosené hrany a plastické přechody do rozhraní, které
je jinak plochý. Vyber jednu úroveň plastičnosti a drž ji napříč komponentami.
**KDY PLATÍ:** Kdykoliv se v jednom rozhraní objeví dvě různé míry hloubky.
**PROČ:** Nekonzistentní hloubka rozbíjí čitelnost vrstev: uživatel neví, co je nad čím a co je
klikatelné. Hloubka je informace o vrstvě, ne dekorace.
**TŘÍDA:** C. Nepřímá opora: Material Design 3 přešel od stínu k tonálnímu rozdílu barvy a Carbon
vyhrazuje elevaci jen pro modály a popovery, dlaždice nechává bez elevace (z průzkumu fáze 1).
**ZDROJ:** obecně uznávaná praxe, doprovázená konvencí design systémů (M3, Carbon).
**KDY NEPLATÍ:** Záměrná retro nebo hravá estetika, provedená důsledně přes celé rozhraní. Chyba je
míchání, ne plastičnost sama.

### Rainbow paleta a víc než tři akcentní barvy

**PRAVIDLO:** Nepoužívej víc než tři akcentní barvy nad rámec základní palety a nepřiřazuj barvu
každé kategorii jen proto, že kategorie existuje. Barva musí něco znamenat, jinak je to šum.
**KDY PLATÍ:** Dashboardy, tabulky, tagy, stavové odznaky, grafy.
**PROČ:** Když je barevné všechno, není zvýrazněné nic. A informace nesená jen barvou je nedostupná
pro část uživatelů.
**TŘÍDA:** C pro počet, B pro "neschovávej informaci jen do barvy" (USWDS: "Start in black and
white", plus demografie barvosleposti 8 % mužů, 0,5 % žen, z průzkumu fáze 1).
**ZDROJ:** USWDS, designsystem.digital.gov (přes průzkum fáze 1) ·
[Pravidlo 60-30-10](../color/pravidlo-60-30-10.md) (vrstva 3, poměr je třída C; nota nese override k hodnotám barev).
**KDY NEPLATÍ:** Kategorická paleta v grafu, kde je barva jediný nosič kategorie. Tam je víc barev
nutnost, ale musí být doplněná labelem nebo tvarem.

### Víc než dva fonty

**PRAVIDLO:** Dvě písmové rodiny jsou strop, a pro většinu projektů stačí jedna se dvěma až třemi
řezy. Když sáhneš po druhé rodině, musí mít jasnou roli (nadpisy vs text), ne "aby to bylo pestré".
**KDY PLATÍ:** Každý projekt.
**PROČ:** Každá další rodina je další sada rozhodnutí (velikosti, řezy, spacing), která se musí
udržet konzistentní. Tři rodiny se neudrží.
**TŘÍDA:** C
**ZDROJ:** obecně uznávaná praxe. Techniku párování drží [Font pairing](../typography/font-pairing.md),
která byla 23. 8. 2026 opravena, aby s tímhle pravidlem souhlasila (dřív radila 3-4 rodiny).
**KDY NEPLATÍ:** Displejové písmo použité na jediném místě (logotyp, jeden hero nadpis) a technický
monospace na kód. To se nepočítá jako třetí rodina do textového systému.

### Stín na všem a jeden neodstupňovaný stín

**PRAVIDLO:** Nedávej stín na každou kartu, tlačítko a pole. A když stín používáš, měj škálu:
s rostoucí vzdáleností od plochy se snižuje opacita a zvyšuje blur, a stín je vrstvený, ne jeden.
**KDY PLATÍ:** Definice komponent a tokenů.
**PROČ:** Stín má znamenat vzdálenost od plochy. Když ho má všechno stejně, nesděluje nic a jen
zašumí hrany.
**TŘÍDA:** C pro imperativ "ne na všem", B pro odvození parametrů z fyziky.
**ZDROJ:** Josh Comeau, Designing Beautiful Shadows in CSS (proč stín vrstvit a proč s rostoucí
vzdáleností snižovat opacitu a zvyšovat blur), https://www.joshwcomeau.com/css/designing-shadows/ ·
Konvence design systémů: Carbon vyhrazuje elevaci pro modály a popovery, M3 dělá hloubku primárně
tonálním rozdílem barvy (z průzkumu fáze 1).
**KDY NEPLATÍ:** Systém, který hloubku řeší barvou a stín nepoužívá vůbec. To je konzistentní volba.

### Emoji jako ikonografie

**PRAVIDLO:** Nepoužívej emoji jako ikony v nadpisech, tlačítkách, navigaci ani v hlavičkách karet.
Když potřebuješ ikonu, použij ikonovou sadu. Dekorativní emoji, které v obsahu nechat chceš, skryj
pomocným technologiím.
**KDY PLATÍ:** Produktové UI, dokumentace, reporty. V neformální komunikaci si dělej, co chceš.
**PROČ:** Emoji je znak s vlastním jménem, které čtečka přečte nahlas, takže v nadpisu nebo na
tlačítku přidává slova, která tam nechceš. Vykresluje se navíc podle platformy jinak, takže nemáš
kontrolu nad vzhledem. A "zakulacená karta s emoji v hlavičce" je jmenovaný marker generovaného
vzhledu.
**TŘÍDA:** C pro accessibility argument (**nenašel jsem k tomu autoritativní pravidlo v žádném
velkém design systému ani u W3C**, jen vendorské accessibility blogy, které jsem neverifikoval),
B pro marker z HN.
**ZDROJ:** HN 47864393 (karty s emoji v hlavičce jako marker).
https://news.ycombinator.com/item?id=47864393 Argument o čtečkách neuváděj jako doložený, je to
popis chování, které jsem neověřil primárním zdrojem.
**KDY NEPLATÍ:** Obsah, kde emoji je ten obsah (reakce, chat, uživatelský text).

### Hero s generickou stock ilustrací a beztvarým sloganem

**PRAVIDLO:** Nedávej do hero sekce izometrickou stock ilustraci lidí u grafů plus nadpis typu
"Build faster. Ship smarter." Nadpis má říct, co produkt dělá a pro koho. Obrázek má ukázat produkt
nebo skutečné lidi, kteří na něm pracují.
**KDY PLATÍ:** Landing pages, produktové stránky.
**PROČ:** Generický slogan neodfiltruje nikoho, takže nepomůže ani cílovému uživateli. Generická
ilustrace nenese informaci o produktu.
**TŘÍDA:** C pro slogan. Nepřímá B opora pro fotky reálných lidí: Stanford Web Credibility
Guidelines (body o ukázání skutečné organizace a lidí za ní), 10bodový checklist z výzkumu
1999 až 2002 se 4500+ účastníky (z průzkumu fáze 1). https://credibility.stanford.edu/guidelines
**ZDROJ:** obecně uznávaná praxe plus Stanford Guidelines pro tu ověřitelnou část.
**KDY NEPLATÍ:** Produkt, který se nedá zobrazit (infrastruktura, pojištění). Tam ilustrace smysl má,
ale musí být vlastní a musí něco vysvětlovat.

### Centrovaný dlouhý text

**PRAVIDLO:** Necentruj odstavce delší než dva řádky. Centrovat lze nadpis, krátký claim a popisek.
Tělo textu zarovnej vlevo.
**KDY PLATÍ:** Vždy, včetně marketingových sekcí.
**PROČ:** Centrovaný text mění pozici začátku každého řádku, takže oko musí hledat, kde další řádek
začíná.
**TŘÍDA:** C
**ZDROJ:** obecně uznávaná praxe.
**KDY NEPLATÍ:** Jeden až dva řádky, citát, hero claim. Tam centrování funguje.

### Nekonzistentní radius a spacing mimo škálu

**PRAVIDLO:** Radius a spacing ber ze škály, ne z citu na každém prvku zvlášť. Když je někde 6 px,
jinde 8, jinde 10 a nikde není důvod, je to marker. U vnořených prvků platí optická kulatost:
vnitřní radius = vnější radius mínus padding.
**KDY PLATÍ:** Definice tokenů, každá nová komponenta.
**PROČ:** Škála je jediný způsob, jak zůstat konzistentní bez rozhodování u každého prvku.
**TŘÍDA:** C pro imperativ, B pro konkrétní škály z publikovaných systémů.
**ZDROJ:** Material Design 3, corner radius scale s deseti stupni (0, 4, 8, 12, 16, 20, 28, 32, 48,
full) a pravidlem optické kulatosti u vnořených prvků, https://m3.material.io/styles/shape/corner-radius-scale ·
Refactoring UI, spacing škála 4/8/16/24/32/48/64 (z průzkumu fáze 1, vrstva D) ·
[Osmibodová mřížka](../zakony-principy/osmibodova-mrizka.md).
**KDY NEPLATÍ:** Optická korekce jednotlivého prvku, kterou umíš vysvětlit (ikona potřebuje o 2 px
jiný padding, aby opticky sedla). To není nekonzistence, to je záměr.

### Generické mikrocopy u chyb a prázdných stavů

**PRAVIDLO:** Nepiš "Oops! Something went wrong.", "Invalid input", "No data". Chybová hláška říká,
co se stalo a jak to opravit. Prázdný stav říká, co sem patří a jak to naplnit.
**KDY PLATÍ:** Všechny chybové, prázdné a potvrzovací stavy.
**PROČ:** Detailně včetně zakázaného slovníku a citací je to v samostatné notě.
**TŘÍDA:** B, přeneseno.
**ZDROJ:** [Formuláře a stavy](formulare-a-stavy.md), sekce Validace a Prázdné stavy. Primárně
GOV.UK Design System (Error message) a NN/g Error-Message Guidelines.
**KDY NEPLATÍ:** Viz ta nota, sekce o třech třídách chyb. U totálního selhání systému je omluvný tón
naopak v pořádku.

---

## Protijed: anti-slop není "buď divný"

Nejčastější způsob, jak tuhle notu použít špatně, je začít porušovat konvence, aby výsledek nevypadal
generický. To je horší chyba než slop, protože stojí orientaci uživatele.

### Odchyluj se na povrchu, nesahej na strukturu

**PRAVIDLO:** Rozděl rozhodnutí na tři vrstvy a odchyluj se jen v nejvyšší.
1. **Struktura a pozice** (kde je navigace, hledání, přihlášení, košík, primární akce): neodchyluj se.
2. **Regulatorní parametry** (kontrast, velikost terče, reflow, řádkování): nejsou předmětem designu,
   jsou to mantinely.
3. **Povrch** (paleta, písmo, radius, foto, tón, motion): tady je prostor a novost se vyplácí.
**KDY PLATÍ:** Každé rozhodnutí "udělám to jinak".
**PROČ:** Netypické umístění prvku měřitelně stojí fixace a čas na nalezení. Zároveň platí, že
typičnost a novost jsou stejně silné prediktory preference a potlačují si vzájemně efekt: lidé
preferují nové řešení, dokud novost nezasáhne rozpoznatelnost kategorie.
**TŘÍDA:** A pro obě opory.
**ZDROJ:** Roth, S. P., Tuch, A. N., Mekler, E. D., Bargas-Avila, J. A., Opwis, K. (2013). *IJHCS*
71(3), 228-235, DOI 10.1016/j.ijhcs.2012.09.001, N = 40, eye-tracking na reálných webech: typické
umístění znamená méně fixací a rychlejší nalezení. Netypickou pozici lze kompenzovat vysokou vizuální
saliencí. · Hekkert, P., Snelders, D., van Wieringen, P. C. W. (2003). *British Journal of
Psychology* 94(1), 111-124: typicalita a novost jsou stejně silné prediktory a potlačují si vzájemně
efekt, verbatim: "People prefer novel designs as long as the novelty does not affect typicality."
· Tuch, A. N. et al. (2012). *IJHCS* 70(11), 794-811, DOI 10.1016/j.ijhcs.2012.06.003: hlavní efekt
prototypičnosti η²p = 0,812. (Vše přeneseno z průzkumu fáze 1, kde je i mantinel: studie NEDOVOLUJE
tvrdit, že konkrétní radius nebo font zvyšuje prototypičnost.)
**KDY NEPLATÍ:** Produkt, jehož hodnota je právě v jiné interakci (kreativní nástroj, hra). Tam je
struktura předmětem návrhu, ale platí se to učením.

---

## Checklist před odevzdáním

Projdi to očima, ne z hlavy. Zabere to dvě minuty.

- [ ] Má nějaká karta barevný levý pruh, který nic neznamená?
- [ ] Změřil jsem kontrast těla textu v dark mode? 4,5:1, ne "vypadá to čitelně".
- [ ] Má každý klikatelný prvek viditelný okraj, podtržení nebo výplň s kontrastem 3:1?
- [ ] Je klikatelný terč aspoň 24 × 24 CSS px?
- [ ] Je "features" sekce mřížka stejných zakulacených karet s ikonou nahoře?
- [ ] Kolik akcentních barev tam je? Víc než tři?
- [ ] Kolik písmových rodin? Víc než dvě?
- [ ] Je stín na všem? Má škálu?
- [ ] Je radius a spacing ze škály, nebo jsem to střílel od boku?
- [ ] Je někde emoji v nadpisu, tlačítku nebo hlavičce karty?
- [ ] Je někde odstavec delší než dva řádky vycentrovaný?
- [ ] Řekne hero nadpis, co produkt dělá a pro koho, nebo je to "Ship faster"?
- [ ] Mají chybové a prázdné stavy vlastní text, nebo tam svítí "Oops" a "No data"?
- [ ] Neposunul jsem navigaci, hledání nebo primární akci z místa, kde ji lidé hledají?

## Nedořešené mezery

1. **Většina markerů je třída B nebo C.** HN vlákno je pozorování, ne měření. Jediné tvrdě naměřené
   položky v téhle notě jsou signifikátory klikatelnosti (NN/g 2017), kontrastní a spacing prahy
   (WCAG) a vrstvení struktura vs povrch (Roth 2013, Hekkert 2003, Tuch 2012).
2. **Emoji a čtečky obrazovky.** Autoritativní pravidlo od W3C ani od velkého design systému jsem
   nenašel. Chování je dohledatelné jen u vendorských accessibility blogů, které jsem neověřoval.
3. **Neexistuje měřený test "slop vs ne-slop".** Nikdo nepublikoval studii, která by ukázala, že
   uživatel produkt s těmi markery hodnotí horší. Nejblíž je Douneva 2015/2016 (silná barva jedné
   rodiny hodnocena esteticky nejhůř) a to je jen jeden z markerů.
