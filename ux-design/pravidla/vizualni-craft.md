# Vizuální craft: art direction a rozvoj vkusu

Související je [Logo design](../logo-foto/logo-design.md): tytéž otázky o rozpoznatelnosti
a redukci, jen na jednom znaku místo celé stránky.

Nota řeší vrstvu, kterou zbytek `pravidla/` záměrně neřeší: kdy je návrh technicky správný
(kontrast OK, radius konzistentní, pohyb podle pravidel), ale přesto působí ploše, genericky
nebo bezradně. Otevři ji při volbě vizuálního směru projektu (odvážný vs. zdrženlivý), při
finálním art-direction průchodu před odevzdáním, nebo když je výsledek formálně v pořádku,
ale nikdo v týmu mu nevěří.

**Jiná třída zdrojů než zbytek knihovny.** Ostatní noty v `pravidla/` staví na měřené evidenci
nebo publikované konvenci designových systémů. Tahle nota staví na psaných esejích uznávaných
praktiků (product/design engineer, ne akademik), bez citované studie za tvrzením. Fáze 1
průzkumu to označila jako nejlepší dostupný „proč" obsah k tématu vizuálního řemesla —
lepší než YouTube tutoriály, protože autoři rozepisují uvažování, ne jen výsledek. Je to ale
pořád **třída C: řemeslná praxe**, ne měření. Bereme ji vážně proto, že v celé knihovně
neexistuje pro tohle téma nic silnějšího, ne proto, že by autoritativnost byla stejná jako
u WCAG nebo Fitts.

Sesterské noty: [Kontrast a barva](kontrast-a-barva.md) (kdy je barva čitelná),
[Pohyb](pohyb.md) (jak animaci technicky provést), [Anti-slop](anti-slop.md) (markery
generického vzhledu). Tahle nota řeší rozhodnutí o SMĚRU, ty ostatní o PROVEDENÍ.

## Použitelná pravidla

### Pojmenuj pól: klasická, nebo expresivní estetika

**PRAVIDLO:** Na začátku vizuálního směru vědomě rozhodni mezi klasickým pólem (řád, symetrie,
jednoduché tvary, málo barev, univerzálně přijatelné) a expresivním pólem (variace, kontrast,
víc barev, riskantnější technika, zapamatovatelné). Rozhodnutí zapiš, ať není defaultem, ke
kterému se sklouzne mlčky.
**KDY PLATÍ:** vždy na začátku návrhu vizuálního směru, hlavně když brief obsahuje slova jako
„odvážný", „nezapomenutelný", „jako [uznávané studio]" na jedné straně, nebo „důvěryhodný",
„klidný", „univerzální" na druhé.
**PROČ:** Anthony Hobday to shrnuje jako tvrdý tradeoff: klasická estetika je „universally
beautiful" ale „boring", expresivní je „exciting" ale „divides audiences". Není to spor
o to, který pól je lepší, je to spor o to, který se hodí k publiku a účelu. Kdo pól
nepojmenuje, sklouzne k tichému defaultu (klasická, protože je bezpečnější) a výsledek
vyjde ploše i tam, kde prostor pro odvahu byl.
**TŘÍDA:** C (řemeslná esej, Anthony Hobday, product designer)
**ZDROJ:** https://anthonyhobday.com/blog/20260411, „Notes on visual design"
**KDY NEPLATÍ:** sektor/kontext už pól rozhodl (viz `kontext/*.md`) — státní správa,
zdravotnictví a finance defaultně klasická, dětský/luxury/kreativní sektor má prostor pro
expresivní. Pravidlo je o VĚDOMÉ volbě, ne o doporučení jednoho pólu nad druhým.

### Zdrženlivost není nulová vizuální osobnost

**PRAVIDLO:** Když brief nebo sektor žádá „klidný", „neagresivní" nebo „důvěryhodný" vzhled,
neber to jako pokyn k nulové expresivitě. Znamená to JEDNO tiché, konzistentní rozhodnutí
(jeden sebevědomý akcent, jasná typografická hierarchie, konzistentní hlas v copy), ne
absenci rozhodnutí.
**KDY PLATÍ:** kontexty vyžadující zdrženlivost (zdravotnictví, finance, státní správa), kde
má výstup přesto působit jako promyšlený produkt, ne jako neutrální placeholder.
**PROČ:** Hobday odvozuje krásu ze „strong relationships between elements", ne z dekorace.
I klasická estetika je tedy o vztazích mezi prvky, ne o jejich vynechání. Zdrženlivý návrh
bez jediného sebevědomého rozhodnutí nečte se jako „klidný", čte se jako nedokončený.
**TŘÍDA:** C (odvozeno z Hobdayho rámce, ne samostatně testováno)
**ZDROJ:** https://anthonyhobday.com/blog/20260411
**KDY NEPLATÍ:** kontexty, kde je záměrem právě absence osobnosti (Radix/shadcn nestylované
primitivy pro vývojáře, viz `kontext/dev-tools-saas.md`) — tam je bezbarvost sama funkcí.

### Malé nesrovnalosti váží víc, než vypadají

**PRAVIDLO:** Zarovnání, mezery a konzistenci odsazení kontroluj jako prioritu finálního
průchodu, ne jako kosmetiku na konec, na kterou už nezbyl čas.
**KDY PLATÍ:** poslední průchod před odevzdáním, hlavně u expresivnějších návrhů, kde jedna
nedbalost prozradí neopatrnost celku silněji než u strohého klasického layoutu.
**PROČ:** Hobday verbatim: „Small visual design issues (e.g. misalignment) catch the eye.
They're a bigger problem than they seem."
**TŘÍDA:** C (řemeslná esej)
**ZDROJ:** https://anthonyhobday.com/blog/20260411
**KDY NEPLATÍ:** rané wireframe/low-fi fáze, kde se řeší struktura, ne povrch.

### Vzácný akcent váží víc než všudypřítomný

**PRAVIDLO:** Když je barva nebo jiný expresivní prvek v systému většinou nepřítomný, jeho
jednorázové použití nese víc váhy, než kdyby byl všude. Soustřeď akcent na moment, který má
vyniknout, neplýtvej jím plošně.
**KDY PLATÍ:** CTA v jinak neutrálním layoutu, jeden důraz v konzervativním sektoru, signální
barva u stavu nebo chyby.
**PROČ:** Hobday verbatim: pokud je prvek „absent (e.g. colour), it will have much more impact
when it is suddenly present."
**TŘÍDA:** C (řemeslná esej)
**ZDROJ:** https://anthonyhobday.com/blog/20260411
**KDY NEPLATÍ:** brand, kde je barva nosným prvkem identity celého systému — tam vzácnost
naopak identitu oslabí, tam má barva být přítomná soustavně.

### Přidej vlastní omezení, i vymyšlené

**PRAVIDLO:** Když návrh působí bezradně nebo obecně, přidej záměrné omezení (paleta na dvě
barvy, jeden font, pevný počet sloupců gridu), i kdyby ho zadání nevyžadovalo.
**KDY PLATÍ:** hledání vizuálního směru, kdy má tvůrce (člověk nebo model) příliš mnoho
stupňů volnosti a výsledek je „o ničem".
**PROČ:** Hobday verbatim: „Creativity is easier if you have constraints. Even if you make
them up."
**TŘÍDA:** C (řemeslná esej)
**ZDROJ:** https://anthonyhobday.com/blog/20260411
**KDY NEPLATÍ:** fáze explorace, kde je cíl záměrně otevřít prostor možností, ne ho hned zúžit.

### Kopíruj bezpečně z klasického pólu, expresivní styl nepřenášej mimo kontext

**PRAVIDLO:** Když přebíráš vizuální styl z reference, klasická estetika se přenáší bezpečně
(je univerzální). Expresivní, dobově nebo oborově specifický styl (např. konkrétní Awwwards
trend) nepřenášej do jiného kontextu bez úpravy.
**KDY PLATÍ:** práce s referencemi typu „chci to jako [uznávané studio nebo web]".
**PROČ:** Hobday verbatim: „It's safer to steal classical aesthetics because they're
universal." A dál: styly „fit their context or purpose well" — mimo něj obvykle selžou.
**TŘÍDA:** C (řemeslná esej)
**ZDROJ:** https://anthonyhobday.com/blog/20260411
**KDY NEPLATÍ:** záměrný pastiš nebo homage, kde je cílem právě evokovat konkrétní dobový
nebo oborový kontext reference.

### Vkus je trénovaný instinkt, rozvíjí se stejným postupem jako řemeslo

**PRAVIDLO:** Craft úsudek (co kdy vyniká, co je jen hlučné) rozvíjej postupem: (1) obklop se
prací uznávaných tvůrců oboru, sleduj je kurátorsky, používej jejich produkty; (2) nezůstávej
u „líbí/nelíbí", rozeber si konkrétně, KTERÝ detail a JAKÝ vztah mezi prvky funguje; (3) tvoř
opakovaně a nech si práci okomentovat od zkušenějšího, ne jen metodou pokus-omyl.
**KDY PLATÍ:** budování designového rule systému i jednotlivé rozhodnutí bez měřené evidence,
kde je potřeba praktikérský úsudek — přesně situace, na kterou tahle nota reaguje.
**PROČ:** Kowalski definuje taste jako „a trained instinct", ne vrozenou vlastnost ani čistou
preferenci: schopnost vidět, co překračuje samozřejmé. Produkty se dnes komoditizují (fungovat
umí každý, hlavně s AI), diferenciátor je vkus.
**TŘÍDA:** C (řemeslná esej, Emil Kowalski, design engineer Linear, autor Sonner a Vaul)
**ZDROJ:** https://emilkowal.ski/ui/developing-taste, „Developing Taste"
**KDY NEPLATÍ:** rozhodnutí, kde existuje měřená evidence (WCAG, Fitts, Cowan) — tam má
evidence přednost před vkusem, viz ostatní noty v `pravidla/`.

### Typografický hlas: párování řezů nese osobnost, ne jen čitelnost

**PRAVIDLO:** Volbu písma neřeš jen čitelností a škálou (viz [Typografie](typografie.md)),
ale jako záměrné párování dvou odlišných hlasů: jeden nosný (display/heading, nese osobnost)
a jeden technický (mono nebo neutrální sans, nese UI popisky, labely, metadata). Kombinace
kurzíva vs. vzpřímené, trackované caps vs. běžná sazba, nebo serif vs. mono jsou nástroj
hierarchie a nálady, ne dekorace navíc.
**KDY PLATÍ:** projekt s vlastní editorialní/brandovou identitou (portfolio, kampaň, studio),
kde má typografie nést část významu, ne jen zobrazit text.
**PROČ:** Živý příklad z 29. 7. 2026: forms.world páruje serif display řez (PP Editorial New,
místy kurzívou) s trackovanými caps a mono popisky pro metadata — výsledek čte jako filmový
titulek, ne jako web. warmnfuzzy.tv naproti tomu drží jeden bold grotesk (SuisseIntl) v celém
systému a osobnost nese tvar loga, ne párování řezů. Obě fungují, protože je to JEDNO vědomé
rozhodnutí, ne směs bez záměru.
**TŘÍDA:** C (vlastní pozorování 2 nezávislých webů, ne publikovaná studie)
**ZDROJ:** živý screenshot a CSS forenzní analýza, forms.world a warmnfuzzy.tv, 29. 7. 2026
(viz případovky níže)
**KDY NEPLATÍ:** systém s už existující typografickou škálou (brand guidelines) — tam se
párování nevymýšlí znovu, drží se dané.

## Jak rozhodnout v praxi

1. Pojmenuj pól (klasická/expresivní) dřív, než začneš stavět, podle sektoru a briefu.
2. I ve zdrženlivém kontextu vlož aspoň jedno sebevědomé rozhodnutí, ne nulu.
3. Přidej omezení, když je návrh moc obecný, i vymyšlené.
4. Reference kopíruj z klasického pólu volně, z expresivního jen s úpravou na vlastní kontext.
5. Finální průchod: zarovnání a mezery zkontroluj jako prioritu, ne jako poslední kosmetiku.
6. Vzácnost akcentu hlídej, plošné použití ho oslabí.
7. Typografii páruj záměrně (nosný řez + technický řez), ne nahodile.

## Tři nezávislé příklady, živě ověřené (29. 7. 2026)

Tři weby nominované na Awwwards (`warmnfuzzy.tv`, `forms.world`, `davidspaeth.com`), otevřené
přes Playwright a analyzované i na úrovni skutečného CSS, ne jen popisem. Zvoleny bez výběru
podle výsledku — byly to weby, které si Alex všiml první. Nejsou (ještě) vítězi, jen nominace
v hlasování k 29. 7. 2026.

- **warmnfuzzy.tv** — hravý/grafický pól. Bílo-černá hero fotografie, ale work stránka je
  celá v mustard žluté (`#f7dd47`) s obřím ořezaným nadpisem a dvěma reálnými 3D rendery
  (sýrová a holografická kostka) plovoucími přes text. Portfolio grid je asymetrická masonry
  mřížka: vlajkový projekt dostane velkou dlaždici, ostatní menší, obsah míchá foto/ilustraci/
  plochou barvu s logem. Jeden bold grotesk (SuisseIntl) v celém systému, osobnost nese tvar
  loga a barva sekce, ne párování řezů.
- **forms.world** — cinematický/editorialní pól. Fullscreen video hero (dramatické modré
  světlo), serif display písmo (PP Editorial New) párované s trackovanými caps a mono
  popisky, karusel projektů čtený přes velikost/průhlednost (předchozí/aktuální/další).
  Nulová hravost, čistá filmová nálada.
- **davidspaeth.com** — čistě fotografický/klasický pól. Bílé pozadí, žádná barva navíc,
  dvousloupcová galerie, popisek jako v knize („VETEMENTS FW 21/22 (54)"). Nula CTA,
  nula marketingového textu — fotka nese celou váhu, UI je záměrně neviditelné.

**Proč tohle je důkaz, ne jen ilustrace:** všechny tři jsou nezávisle nominované, žádný nekopíruje
druhý, a přesto každý zvolil jiný pól a drží ho beze zbytku. Potvrzuje to hlavní tezi téhle noty
zpětně: neexistuje jedno „správné" craft řešení, existuje jasně pojmenovaný pól držený důsledně.
**Metodologická poznámka:** čistě zdrojová (CSS) analýza bez renderu minula reálný detail
(zaoblení navigačních tlačítek na forms.world nebylo v žádném staženém CSS souboru, ale na
screenshotu je vidět) — u vizuálního craftu ověřuj renderem, ne jen zdrojovým kódem.

## Co v téhle notě chybí (nepřečtené zdroje, neuzavírat jako hotovo)

Fáze 1 průzkumu pojmenovala další craft zdroje, ze kterých je zatím vytěžená jen technická
vrstva (parametry animace, focus ring, shadow physics — viz [Pohyb](pohyb.md),
[Hloubka a stíny](hloubka-a-stiny.md), [Stroke a hranice](stroke-a-hranice.md)), ne vrstva
art direction/hlasu jako u téhle noty. Než je někdo skutečně přečte, neber je jako uzavřené:

- Emil Kowalski, další eseje: „You Don't Need Animations", „7 Practical Animation Tips" —
  https://emilkowal.ski/
- Rauno Freiberg, `interfaces.rauno.me` — čteno jen na úrovni jednotlivých pravidel (hover
  media query, focus ring, scale), ne celá filozofie webu.
- `devouringdetails.com` (Rauno, placené, 249 $) — kapitoly Simulating physics, Motion
  choreography nepřečteny, za paywallem.
- Locomotive a Active Theory, technická vysvětlení na Medium — zdroj zmíněný ve fázi 1,
  konkrétní články nedohledány.
- Paco Coursey (`paco.me/writing`, autor cmdk a next-themes), Jakub Antalík
  (`transitions.dev`) — zdroje pojmenované, obsah nepřečtený.
