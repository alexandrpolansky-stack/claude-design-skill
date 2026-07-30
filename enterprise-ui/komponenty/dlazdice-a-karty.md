# Dlaždice a karty

Odpověď na otázku, kterou [STATUS.md](../../STATUS.md) jmenuje jako mezeru: **kdy je karta klikatelná
celá a kdy jen CTA uvnitř.**

Související: [Volba komponenty](../zaklady/volba-komponenty.md) ·
[Klávesnice a focus](../zaklady/klavesnice-a-focus.md) ·
[Portfolio a work grid](../../ux-design/pravidla/portfolio-a-work-grid.md) ·
[Hloubka a stíny](../../ux-design/pravidla/hloubka-a-stiny.md)

---

## Rychlé rozhodnutí

1. Dlaždice **obsahuje** odkazy nebo tlačítka = **base tile**, dlaždice sama není interaktivní.
2. Celá dlaždice naviguje jinam = **clickable tile**. Ta **nesmí obsahovat vlastní CTA uvnitř**.
3. Dlaždice je volba ze sady = **selectable tile**, single nebo multi select.
4. Dlaždice odkrývá a skrývá obsah = **expandable tile**.
5. **Nikdy neklaď interaktivní prvky na interaktivní plochu.** Když potřebuješ obojí, použij base tile.
6. **Nedávej dlaždici stín.** Dlaždice je na stejné úrovni jako pozadí, nemá elevaci.
7. Sekundární informaci nebo akci **neodkrývej dlaždicí**, na to je modal, popover nebo dialog.
8. Minimální výška dlaždice = poměr **2:1**.
9. Ve standardním layoutu mají všechny dlaždice ve skupině **stejnou výšku i šířku**.
10. Odkaz dovnitř base tile dej **vlevo dole**, tlačítko na **plnou šířku dole**.

---

## Dlaždice versus karta

**Carbonova definice:** dlaždice je jednoduchá a základová. **Karty mohou být velmi složité.** Karty
jsou postavené **na základu dlaždice** a mají různé vzory hierarchie informace, víc akcí, overflow
menu, vybíratelné funkce a tak dál.

**Carbon kartu jako vzor nemá.** Odkazuje na kartové vzory ve svém ekosystému (Carbon for IBM Products,
IBM.com), které v přečtené kopii nejsou.

**ZDROJ:** Carbon, Tile usage, Tiles versus cards, verbatim: „Tiles are simple and foundational. Cards
can be very complex. Cards are built upon the tile foundation."
https://carbondesignsystem.com/components/tile/usage/

**Praktický důsledek:** když stavíš „kartu", stavíš dlaždici plus vlastní vrstvu hierarchie. Pravidla
dlaždice (klikatelnost, elevace, zarovnání) platí pořád. Hierarchii obsahu uvnitř si musíš navrhnout
sám, a na to je v knihovně [neuro-design master](../../neuro-design/neuro-design-master.md) (vizuální
váha prvků) a [portfolio a work grid](../../ux-design/pravidla/portfolio-a-work-grid.md) (hierarchie
dlaždic v gridu).

## Kdy dlaždici použít

Carbon jmenuje čtyři případy:

1. K obsažení souvisejících skupin informace nebo akcí.
2. K nasměrování uživatele k akci nebo navigaci.
3. K prezentaci možností pro jeden nebo víc výběrů.
4. Ke skrytí nebo zobrazení velkého množství obsahu.

Dlaždice jsou podle Carbonu **záměrně bez předdefinovaných stylů a flexibilní**, aby si produktové týmy
určily obsah pro svoje případy.

**ZDROJ:** Carbon, Tile usage, When to use.
https://carbondesignsystem.com/components/tile/usage/

## Kdy dlaždici nepoužít: pravidlo o elevaci

**PRAVIDLO:** Dlaždice sídlí **na stejné rovině jako pozadí stránky a nemají elevaci**. Organizují
zásadní informaci a mají **stejnou vizuální hierarchii jako obsah na téže stránce**. **Nepřidávej
dlaždicím stín** a nepoužívej je na odkrývání sekundární informace, akcí nebo notifikací. Na to použij
**modaly, popovery a dialogy**, které elevaci mají a jsou pro tenhle případ vhodné.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Tile usage, When not to use, verbatim: „Do not add a drop shadow to tiles and use
them to reveal secondary information, actions, or notifications. Use modals, popovers, and dialogs that
have elevation and are appropriate for this use case instead."
https://carbondesignsystem.com/components/tile/usage/
**KDY NEPLATÍ:** Toto je Carbonovo systémové rozhodnutí, ne měřený nález. Knihovna má k elevaci vlastní
notu, která ověřené elevation škály (včetně Carbonovy) srovnává a nechává spor Carbon versus Comeau
o konstantní opacitě stínu otevřený. Viz [hloubka a stíny](../../ux-design/pravidla/hloubka-a-stiny.md).
Tam je i tvrdé pravidlo, že **stín nikdy nesmí nést hranici ovládacího prvku**.

## Čtyři varianty

| Varianta | Kdy | Klikatelnost |
|---|---|---|
| Base | Vysokoúrovňový, krátký a strávitelný obsah: funkce, plány, nabízené služby | Dlaždice sama **není** operovatelná. Interaktivní jsou jen prvky uvnitř |
| Clickable | Vyvolání akce, navigace nebo nasměrování na jinou informaci o daném tématu | **Celá dlaždice** je klikatelná |
| Selectable | Prezentace možností strukturovaně, například sada cenových plánů | Celá dlaždice je vybíratelná |
| Expandable | Skrývání a odkrývání velkého množství obsahu, aby se zaostřilo na konkrétní informaci | Podle toho, jestli obsahuje interaktivní prvky, viz níže |

**ZDROJ:** Carbon, Tile usage, Variants.
https://carbondesignsystem.com/components/tile/usage/

## Base tile: dlaždice jako kontejner

- Používá se na zobrazení informace: funkce, nabízené služby. Carbon jmenuje typický výskyt: marketingové
  stránky na propagaci obsahu, nebo vysoce interaktivní dashboardy.
- **Může mít vnitřní CTA**, například tlačítka nebo odkazy.
- **Stavy: jen enabled**, protože není operovatelná myší ani klávesnicí.
- Myší není operovatelná, **pokud neobsahuje interaktivní prvky**.
- Klávesnicí **nedostane focus**, pokud neobsahuje interaktivní prvky. `Tab` prochází prvky uvnitř.

**Zarovnání vnitřních prvků:** když do base tile umísťuješ interaktivní prvky, dej **odkazy vlevo dole**
a **tlačítka na plnou šířku dole**, aby označovaly výzvu k akci.

**Carbonovo doporučení pro dlaždice s tlačítkem:** „When in doubt, use full-span button alignment within
tiles."

**ZDROJ:** Carbon, Tile usage, Base a Related, Buttons.
https://carbondesignsystem.com/components/tile/usage/

## Clickable tile: celá dlaždice je odkaz

**PRAVIDLO:** Klikatelnou dlaždici používej jako navigační prvek, který uživatele přesměruje na novou
stránku. V takové situaci je **celá dlaždice v klikatelném stavu**. **Kvůli přístupnosti nemůže
klikatelná dlaždice obsahovat samostatná vnitřní CTA**, ale může obsahovat piktogramy, ikony nebo média
jako ilustrace a obrázky.
**KDY PLATÍ:** Vždy, když je dlaždice celá klikatelná.
**PROČ:** Carbon: „Avoid confusing the user with multiple click targets, like interactive links or
buttons, since the whole tile is already clickable."
**TŘÍDA:** B
**ZDROJ:** Carbon, Tile usage, Clickable, verbatim: „Due to accessibility concerns, clickable tiles
cannot contain separate internal CTAs but can contain pictograms, icons, or media such as illustrations
or images." https://carbondesignsystem.com/components/tile/usage/
**KDY NEPLATÍ:** Nikdy. Když potřebuješ jak klikatelnou plochu, tak vnitřní CTA, je odpověď base tile
s explicitními CTA, ne klikatelná dlaždice s vnořeným tlačítkem.

**Ikona navigace:** na klikatelné dlaždici použij **šipku** a dej ji **vpravo dole**, aby značila
navigaci.

**Stavy:** enabled, hover, focus, disabled.

## Selectable tile

- Prezentuje různé možnosti k výběru.
- **Může obsahovat vnitřní CTA** (například odkazy do dokumentace), **ale jen tehdy, když má CTA vlastní
  klikatelný cíl** vedle klikatelného cíle dlaždice.
- Single-select: uživatel může vybrat jen jednu dlaždici ze skupiny.
- Multi-select: uživatel může vybrat víc dlaždic.
- Stavy: enabled, hover, hover selected, selected, focus, disabled.

**ZDROJ:** Carbon, Tile usage, Selectable, verbatim: „Selectable tiles can contain internal CTAs, like
links to documentation, if the CTA is given a click target of its own in addition to the tile's click
target." https://carbondesignsystem.com/components/tile/usage/

**Klávesová logika, kterou je nutné znát:** single-select skupina je **jeden tabstop se šipkami uvnitř**
(chová se jako radio buttony), multi-select dlaždice je **každá vlastní tabstop se `Space` nebo `Enter`**
(chová se jako checkboxy). Carbonovo zdůvodnění: checkbox reprezentuje jednu volbu jako jeden prvek,
zatímco skupina radio buttonů se bere jako jeden prvek, protože buttony spolu tvoří vzájemně se
vylučující volbu. Detail: [Klávesnice a focus](../zaklady/klavesnice-a-focus.md).

## Expandable tile

**Dvě různá chování podle obsahu:**

| Obsah dlaždice | Co rozbaluje |
|---|---|
| **Bez** interaktivních prvků | Kliknutí kamkoliv v dlaždici rozbalí a sbalí. `Space` nebo `Enter` |
| **S** interaktivními prvky | Rozbaluje **ikonové tlačítko s chevronem** vpravo dole, ne kontejner. Interaktivní prvky uvnitř mají vlastní klikatelné cíle |

**PRAVIDLO:** Použij expanzi kontejneru, když nejsou interaktivní prvky. Použij expanzi tlačítkem, když
interaktivní prvky jsou.
**TŘÍDA:** B
**ZDROJ:** Carbon, Tile usage, Expandable.
https://carbondesignsystem.com/components/tile/usage/

**Stavy:** enabled, hover, focus, disabled.

## Tvrdé přístupnostní pravidlo: nepřekrývej akce

**PRAVIDLO:** U velmi složitých dlaždic **nedávej interaktivní prvky na přímo interaktivní dlaždici**,
protože akce se nemají překrývat na ovladatelné ploše. Místo toho použij **base tile (bez rámečku),
která interaktivní není**.
**KDY PLATÍ:** Vždy.
**PROČ:** Vnořený interaktivní prvek na interaktivní ploše má nejednoznačný klikatelný cíl a
nejednoznačné chování z klávesnice.
**TŘÍDA:** B
**ZDROJ:** Carbon, Tile accessibility, Design recommendations, verbatim: „For highly complex tiles, avoid
placing interactive elements on top of a directly interactive tile, as actions should not overlap on an
actionable surface. Instead, use the base tile (without a border around it) that is non-interactive."
https://carbondesignsystem.com/components/tile/accessibility/
**KDY NEPLATÍ:** Nikdy. Tohle je odpověď na otázku ze STATUS.md: **klikatelná celá dlaždice a CTA uvnitř
jsou vzájemně se vylučující varianty**, ne dva režimy jedné komponenty.

## Feature flag: rámeček jako signál ovladatelnosti

Carbon k dlaždicím přidal změny za feature flagem, které **mění vzhled, ne funkci**, a označuje je za
zlepšení přístupnosti. Dvě věci, které stojí za pozornost, protože jsou přenositelné jako princip:

1. **Rámeček byl přidaný ke clickable, selectable a expandable variantě, aby vizuálně označil, že jsou
   ovladatelné.**
2. **Ikony single-select dlaždic se změnily z checkmarků na radio buttony**, multi-select z checkmarků na
   checkboxy. A **tyhle ikony se zobrazují v aktivním stavu**, ne až na hover před výběrem.

**Přenositelný princip** (moje formulace, ne Carbonovo tvrzení, třída **C**): interaktivita se nesmí
odhalovat až na hover. Znak, že prvek jde ovládat, má být vidět bez interakce. To je konzistentní
s doloženým nálezem knihovny, že bezokrajové flat UI stojí uživatele o 22 % víc času (NN/g, Moran 2017).
Viz [anti-slop](../../ux-design/pravidla/anti-slop.md) a
[stroke a hranice](../../ux-design/pravidla/stroke-a-hranice.md).

**ZDROJ:** Carbon, Tile usage, Feature flags.
https://carbondesignsystem.com/components/tile/usage/

## Rozměry a poměry

- Šířka se mění podle tří režimů mezer mřížky: wide, narrow, condensed.
- Výška se mění podle obsahu, s použitím spacing tokenů a doporučených poměrů stran.
- **Minimální výška dlaždice je poměr 2:1.** Jak obsah roste, nastav svislé mezery mezi sekcemi
  v obsahové oblasti.

**ZDROJ:** Carbon, Tile usage, Sizing.
https://carbondesignsystem.com/components/tile/usage/
Poměry stran a mřížka: [2x grid a breakpointy](../zaklady/2x-grid-a-breakpointy.md).

## Tři rozvržení skupiny dlaždic

| Rozvržení | Pravidlo |
|---|---|
| Standard (nejčastější) | Dlaždice mají **stejnou výšku i šířku** jako všechny ostatní ve skupině |
| Vertical masonry | Dlaždice se mohou lišit **výškou**, ale mají konzistentní **šířku** |
| Horizontal masonry | Dlaždice se mohou lišit **šířkou**. Různé řádky se mohou lišit výškou, ale **dlaždice v jednom řádku mají mít konzistentní výšku** |

**Skupiny dlaždic:** jsou užitečné při zarovnávání dlaždic, které mají silný vztah. Skupiny typicky
plynou vodorovně zleva doprava a mají hierarchickou důležitost, podobně jako navigační nebo katalogové
dlaždice.

**ZDROJ:** Carbon, Tile usage, Alignment.
https://carbondesignsystem.com/components/tile/usage/
**Souvislost:** hierarchii uvnitř dlaždicového gridu (vlajková dlaždice, smíšený obsah) řeší
[portfolio a work grid](../../ux-design/pravidla/portfolio-a-work-grid.md), na základě tří živě
ověřených příkladů (třída C).

## Obsah

Text dlaždice se mění podle obsahu. Může obsahovat nadpisový text, tělový text, label text a interaktivní
prvky.

**Prázdný stav v dlaždici:** má jiná pravidla než na celé stránce. V **malé** dlaždici jde obrázek
**vycentrovaný nad** vlevo zarovnaný text a akci (výjimka z jinak platného pravidla zarovnat vlevo jako
blok). Detail a zdůvodnění: [Prázdné stavy](../vzory/prazdne-stavy.md).

**Skeleton stav:** dlaždice je kontejnerová komponenta, takže skeleton stav mít **může** (na rozdíl od
tlačítek, vstupů a modalů). Viz [Načítání a čekání](../vzory/nacitani-a-cekani.md).

**Načítání v dlaždici:** velký loading indikátor lze použít i na jednotlivé dlaždici, s overlayem, aby
uživatel nemohl interagovat s načítaným obsahem. Tamtéž.

## Ghost tlačítka v dlaždicích na dashboardu

**PRAVIDLO:** Na dashboardech s víc produktivními kartami fungují **ghost tlačítka** dobře, protože
přitahují méně pozornosti než terciární. Aby ghost tlačítko působilo zarovnaně ve svislém uspořádání
uvnitř kontejneru, Carbon doporučuje, aby **se dotýkalo aspoň dvou hran kontejneru**.
**TŘÍDA:** B
**ZDROJ:** Carbon, Button usage, Ghost buttons in productive cards.
https://carbondesignsystem.com/components/button/usage/
Detail: [Tlačítka: varianty a volba](tlacitka-varianty.md)

## Přístupný název dlaždice

**PRAVIDLO:** Interaktivní dlaždice musí mít popisný label, aby byl její účel jasný: `aria-label` nebo
`aria-labelledby`. **Dekorativní obrázky mají prázdný `alt`**, informativní obrázky popisný `alt`.
**TŘÍDA:** A jako požadavek (WCAG 4.1.2), B pro techniku.
**ZDROJ:** Carbon, Tile accessibility, Development considerations.
https://carbondesignsystem.com/components/tile/accessibility/
Detail: [Oznámení pro čtečky](../zaklady/oznameni-pro-ctecky.md)

---

## Co tahle nota neřeší

- Kartu jako plnohodnotný vzor s hierarchií a víc akcemi. **Carbon ji nemá**, odkazuje na svůj
  ekosystém, který v přečtené kopii není.
- Hierarchii dlaždic v gridu a vlajkovou dlaždici.
  [Portfolio a work grid](../../ux-design/pravidla/portfolio-a-work-grid.md).
- Kdy nést hloubku barvou plochy a kdy stínem.
  [Hloubka a stíny](../../ux-design/pravidla/hloubka-a-stiny.md).
- Výpočet vizuální váhy prvku uvnitř dlaždice.
  [Neuro-design master](../../neuro-design/neuro-design-master.md).
- Border-radius dlaždice. [Tvar a radius](../../ux-design/pravidla/tvar-a-radius.md).
- Tokeny vrstev a barev. Carbon je má na stránce `style`, záměrně je nepřebírám.

## Zdroj

IBM Carbon Design System, Tile usage a Tile accessibility, lokální kopie přečtená 30. 7. 2026.
https://carbondesignsystem.com/components/tile/usage/
Carbon u dlaždice cituje Hagan Rivers, Interaction design with cards/tiles (Medium, 2017).
Třída **B**, kde je uvedeno **C**, je to moje formulace.
