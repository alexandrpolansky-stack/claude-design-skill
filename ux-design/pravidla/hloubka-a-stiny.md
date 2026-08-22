# Hloubka a stíny

Kdy tuhle notu otevřít: navrhuješ kartu, panel, dropdown, modál, tooltip, sticky lištu nebo
cokoliv, co má vypadat "nad" něčím jiným. A vždycky, když se chystáš napsat `box-shadow`.

Hlavní věc, kterou si odsud odnes: **stín není nástroj na hloubku, je to nástroj na oddělení
plovoucí vrstvy od obsahu, který pod ní projíždí.** Hloubku v toku obsahu nese barva plochy.
Dva velké design systémy se k tomu nezávisle dopracovaly, viz pravidlo 1.

## Rozhodovací postup, než napíšeš box-shadow

1. **Leží plocha v toku obsahu?** (karta, dlaždice, panel, sekce, vnořený kontejner, řádek
   tabulky) → hloubku dělej krokem v barvě plochy, bez stínu.
2. **Plave prvek nad obsahem?** (dropdown, popover, tooltip, modál, sticky hlavička, drag
   preview, toast) → stín ano, úroveň podle toho, jak vysoko plave.
3. **Potřebuješ, aby byl prvek rozpoznatelný jako ovládací?** (input, icon button, checkbox) →
   to není práce pro stín. Tam patří hranice s kontrastem 3:1, viz pravidlo 8.

---

## Pravidla

### Hloubku nes barvou plochy, stín jen na plovoucí vrstvy

**PRAVIDLO:** Vrstvy v toku obsahu odděluj krokem v barvě plochy (base → layer 01 → 02 → 03).
`box-shadow` použij jen u prvku, který plave nad scrollujícím obsahem.
**KDY PLATÍ:** karty, dlaždice, panely, sekce, vnořené kontejnery, tabulky, a zvlášť tvrdě
v tmavém tématu.
**PROČ:** Barevný krok je vidět po celé ploše, stín jen na jejím okraji. Krok barvy navíc drží
funkci v obou tématech, černý stín na tmavém pozadí nemá luminanční rozdíl, o který by se opřel.
**TŘÍDA:** B (dvě nezávislé organizace, Google a IBM, se stejným posunem od stínu k barvě plochy)
**ZDROJ:** Carbon 11, verbatim: "There are four layers within a theme: base layer, layer 01,
layer 02, and layer 03. Layers stack one on top of the other in a set order."
[carbondesignsystem.com/elements/color/usage](https://carbondesignsystem.com/elements/color/usage/).
Material 3 dělá hloubku primárně tonálním rozdílem barvy a stín přidává jen při potřebě oddělení
od pozadí, což je posun proti M2, kde byl stín default
([m3.material.io/styles/elevation/overview](https://m3.material.io/styles/elevation/overview),
stránka je JS-only a nešla fetchnout, tvrzení pochází z fáze 1 průzkumu).
**KDY NEPLATÍ:** když prvek opravdu plave nad obsahem (bod 2 postupu výše); když je téma
jednobarevné a další čitelný krok plochy už není k dispozici; když plochu obtéká obrázek nebo
video, kde barevný krok zmizí.

### Stín má konečnou škálu, ne libovolné hodnoty

**PRAVIDLO:** Definuj 4 až 6 pojmenovaných úrovní a používej jen je. Žádné ad hoc
`0 3px 7px rgba(0,0,0,.13)` v komponentě.
**KDY PLATÍ:** vždy, jakmile ve projektu vznikne druhý stín.
**PROČ:** Stín kóduje "jak vysoko". Když má každá komponenta vlastní hodnotu, přestane být
pořadí vrstev čitelné a začnou vznikat dvojice prvků, které vypadají ve stejné výšce, ale
překrývají se.
**TŘÍDA:** B (publikovaná konvence, IBM Carbon a Google Material)
**ZDROJ:** Carbon má 6 pojmenovaných vrstev na škále 0 až 24, verbatim: "Each layer is a defined
marker along the elevation scale. There is not a layer for each level of the scale."
([archiv Carbon v9, Guidelines / Layer](http://web.archive.org/web/20240610013500/https://v9.carbondesignsystem.com/guidelines/layer/)).
Material 3 má 6 úrovní, hodnoty v dp 0 / 1 / 3 / 6 / 8 / 12
([Google, tokeny `_md-sys-elevation.scss`](https://raw.githubusercontent.com/material-components/material-web/main/tokens/versions/v0_192/_md-sys-elevation.scss)).
**KDY NEPLATÍ:** jednorázová grafika, hero ilustrace, dekorativní vrstva, kde stín nekóduje
pořadí vrstev, ale je součástí obrázku.

### Jedno světlo pro celou stránku

**PRAVIDLO:** Všechny stíny mají stejný směr. Prakticky: `x-offset` drž na 0, `y-offset` kladný.
Když x nenulové být musí, drž konstantní poměr, u Comeaua je vertikální offset dvojnásobek
horizontálního.
**KDY PLATÍ:** každý stín v rozhraní.
**PROČ:** Rozhraní se čte jako jedna scéna. Stíny do různých směrů čtou jako víc světel, což
v reálné scéně znamená víc zdrojů světla a mozek to registruje jako nekonzistenci, i když to
uživatel nepojmenuje.
**TŘÍDA:** C řemeslné odvození (Josh Comeau), ale podepřené praxí: Carbon má u všech šesti
úrovní `x-offset` rovný nule.
**ZDROJ:** [joshwcomeau.com/css/designing-shadows](https://www.joshwcomeau.com/css/designing-shadows/),
verbatim: "Every shadow on the page should share the same ratio", světlo "above and slightly to
the left", vertikální offset "2x the horizontal one". Carbon tabulka viz pravidlo výše.
**KDY NEPLATÍ:** vnitřní stín (`inset`) u vtlačených prvků, kde je směr dán geometrií prvku;
focus ring, který stínem není, i když se dělá `box-shadow`.

### Blur ať je dvojnásobek y-offsetu, spread nula

**PRAVIDLO:** Odvozuj stín z jednoho čísla. Když je elevace `e`, ber `y = e/2` a `blur = e`,
`spread = 0`.
**KDY PLATÍ:** stavíš vlastní škálu stínů od nuly a nemáš žádnou převzatou.
**PROČ:** Fyzikálně: čím dál je prvek od plochy, tím dál stín padá a tím víc se rozptýlí.
Vztah 1:2 mezi offsetem a blurem drží stín "pod" prvkem, ne za ním. Spread nula proto, že
roztažení stínu do strany simuluje větší předmět, ne větší vzdálenost.
**TŘÍDA:** B (Carbon, měřitelný vzor napříč celou škálou)
**ZDROJ:** Carbon v9 tabulka, ověřená hodnota za hodnotou:
`0 1px 2px`, `0 4px 8px`, `0 6px 12px`, `0 8px 16px`, `0 12px 24px`, plus verbatim: "Each unit
on the elevation scale is equal to the pixel value of the coded blur applied to shadow."
([archiv Carbon v9](http://web.archive.org/web/20240610013500/https://v9.carbondesignsystem.com/guidelines/layer/)).
**KDY NEPLATÍ:** velmi nízká elevace, kde `y = 0.5px` nejde vyrenderovat, tam ber `0 1px 2px`
jako podlahu. A u vrstvených stínů, kde se poměr počítá pro každou vrstvu zvlášť.

### Opacitu si rozhodni jednou, protože zdroje si tady protiřečí

**PRAVIDLO:** Zvol jednu ze dvou strategií a drž ji celým systémem. Buď konstantní opacita napříč
škálou a roste jen offset s blurem, nebo s rostoucí elevací opacitu snižuj a blur zvyšuj.
Nemíchej to.
**KDY PLATÍ:** definuješ škálu stínů.
**PROČ:** Carbon drží opacitu konstantní na 0,10 u všech pěti nenulových úrovní a mění jen
offset a blur. Comeau odvozuje z rozptylu světla, že vzdálenější prvek má stín méně opakní
a rozmazanější. Ani jedno není měření, obojí je konvence plus řemeslné odvození. Rozdíl v praxi:
konstantní opacita dává předvídatelnější tokeny, klesající dává jemnější vysoké úrovně.
**TŘÍDA:** B pro Carbonovu variantu (IBM, publikovaná konvence bez publikovaného měření),
C pro Comeauovu (řemeslné odvození z fyziky). Samo "rozhodni se jednou a drž to" je C, protože
mezi těmi dvěma nemá kdo rozhodnout.
**ZDROJ:** Carbon všech pět stínů má `rgba(0,0,0,0.10)`
([archiv Carbon v9](http://web.archive.org/web/20240610013500/https://v9.carbondesignsystem.com/guidelines/layer/)).
Comeau: s rostoucí vzdáleností roste offset, blur je "larger", stín je "less opaque"
([joshwcomeau.com](https://www.joshwcomeau.com/css/designing-shadows/)).
**KDY NEPLATÍ:** nikdy, tohle je volba, ne fakt. Jen ji nedělej dvakrát různě v jednom projektu.

### Vysoko plovoucí prvek dělej vrstveným stínem

**PRAVIDLO:** U modálu, popoveru a drag preview slož stín ze 3 až 5 vrstev s exponenciálně
rostoucím offsetem a blurem, každou s nízkou alfou, místo jedné vrstvy s velkým blurem.
**KDY PLATÍ:** nejvyšší dvě úrovně škály. U nízkých úrovní se to nevyplatí, rozdíl není vidět.
**PROČ:** Jedna vrstva s velkým blurem má lineární gradient a čte se jako šedá aura. Reálný
polostín světla není lineární, hustota klesá se vzdáleností od předmětu, a několik nasazených
vrstev tu křivku aproximuje.
**TŘÍDA:** C (řemeslné odvození, Josh Comeau; hodnoceno ve fázi 1 jako nejlepší nalezené "proč"
v celém průzkumu, ale je to odvození, ne měření)
**ZDROJ:** [joshwcomeau.com/css/designing-shadows](https://www.joshwcomeau.com/css/designing-shadows/),
jeho pětivrstvý příklad: offsety a blury `1px / 2px / 4px / 8px / 16px`, každá vrstva alfa 0,075.
**KDY NEPLATÍ:** stovky instancí na jedné stránce (řádky dlouhé tabulky, mřížka karet), tam se
vrstvení nevyplatí ani vizuálně, ani výkonově. A na mobilu, kde je prvek přes celou šířku a
okraj skoro nevidíš.

### Stín tónuj do odstínu pozadí, nikdy čistá černá

**PRAVIDLO:** Barvu stínu vezmi z hue pozadí a sniž saturaci a světlost. Ne `rgba(0,0,0,α)`
na barevném pozadí.
**KDY PLATÍ:** pozadí, které není neutrální šedá nebo bílá.
**PROČ:** Čistě černý stín na barevném pozadí ho odsatuje a výsledek vypadá zašedle. Stín
v odstínu pozadí zůstane součástí scény.
**TŘÍDA:** C (Josh Comeau)
**ZDROJ:** [joshwcomeau.com/css/designing-shadows](https://www.joshwcomeau.com/css/designing-shadows/),
doporučuje například `hsl(220deg 60% 50%)` místo `hsl(0deg 0% 0%)`, aby stín nebyl "washed-out".
**KDY NEPLATÍ:** neutrálně šedé nebo bílé pozadí, kde je černá s nízkou alfou správná odpověď.
A v tmavém tématu, kde stín nefunguje vůbec, viz poslední pravidlo.

### Stín nikdy nenese hranici ovládacího prvku

**PRAVIDLO:** Rozpoznatelnost inputu, tlačítka nebo checkboxu musí stát na hranici nebo ploše
s kontrastem alespoň 3:1 proti sousední barvě. Stín je dekorace nad tím, ne náhrada.
**KDY PLATÍ:** každý interaktivní prvek a každý grafický objekt nesoucí informaci.
**PROČ:** WCAG 1.4.11 Non-text Contrast žádá 3:1 pro UI komponenty a grafiku. Měkký rozptýlený
stín má na hraně gradient, který 3:1 nedosáhne prakticky nikdy, takže "bezokrajový input se
stínem" je nesplněné AA kritérium, ne minimalismus.
**TŘÍDA:** A jiného druhu než studie: právní požadavek. AA od WCAG 2.1, u českého státního
a municipálního klienta vynutitelné zákonem č. 99/2019 Sb., v privátním sektoru přes EAA
2019/882 (e-commerce, bankovnictví) živé od 28. 6. 2025.
**ZDROJ:** [W3C, Understanding SC 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html);
regulatorní tabulka z fáze 1 průzkumu.
**KDY NEPLATÍ:** neinteraktivní dekorativní grafika a prvky, kterým hranici kreslí user agent
(nestylovaný nativní input). Vypnutý (`disabled`) stav je z 1.4.11 vyňatý, ale GOV.UK i NHS
shodně říkají, že disabled se má hlavně nepoužívat.

### Oddělení plochy řeš v pořadí spacing, barva, border, stín

**PRAVIDLO:** Když potřebuješ dvě plochy odlišit, zkus nejdřív mezeru, pak barvu plochy, a teprve
pak kresli hranu. O tom, jestli hrana bude stín nebo border, nerozhoduj podle vzhledu, ale podle
významu: stín když prvek plave, border když nese kontrast nebo když stín nefunguje. Nedávej border
a stín současně na tentýž prvek.
**KDY PLATÍ:** hustá rozhraní, dashboardy, mřížky karet, formuláře.
**PROČ:** Každá nakreslená linka i každý stín je práce pro oko. Refactoring UI to formuluje přímo:
příliš borderů čte jako zaneřáděné a nahrazuje se stínem, kontrastním pozadím nebo spacingem.
První dva kroky, mezera a barva plochy, nepřidávají do obrazu žádný nový prvek, proto jdou první.
**TŘÍDA:** C (Refactoring UI, autorská konvence, žádný výzkum)
**ZDROJ:** Refactoring UI, zaznamenáno ve fázi 1 průzkumu jako "příliš borderů = zaneřáděno,
nahradit box shadow / kontrastním pozadím / spacingem".
**KDY NEPLATÍ:** když border nese kontrast podle 1.4.11 (pravidlo výše), tam ho vyhodit nesmíš.
Prostředí, kde stín nefunguje spolehlivě (e-mailové klienty, tisk), border potřebuje vždy.
A nepoužívej na oddělení obarvený levý okraj karty: ten je v komunitě rozpoznaný jako marker
generického AI vzhledu, viz anti-slop poznámky ve fázi 1 průzkumu.
**Detail rozhodování border vs. stín vs. whitespace** je v sesterské notě
[Stroke a hranice](stroke-a-hranice.md), tahle nota řeší jen tu stínovou stranu.

### Elevaci na hover měň jen u prvku, který se opravdu zvedá

**PRAVIDLO:** U hover a press stavů použij state layer, tedy poloprůhlednou překryvnou barvu, ne
změnu stínu. Změnu elevace si nech pro prvky, které se v interakci fyzicky zvedají, typicky drag.
**KDY PLATÍ:** karty, řádky, tlačítka, dlaždice, položky seznamu.
**PROČ:** Změna stínu na hover posune obsah opticky nahoru a u mřížky karet se to sečte do
poskakující plochy. State layer změní jen jasnost, geometrie zůstane. Material 3 kvantifikuje
kroky jako opacity: hover 8 %, focus 10 %, press 10 %, drag 16 %.
**TŘÍDA:** B (Material Design 3, interní konvence Google, žádný publikovaný user test)
**ZDROJ:** M3 state layers, hodnoty zaznamenané ve fázi 1 průzkumu
([m3.material.io](https://m3.material.io/foundations/interaction/states/state-layers), JS-only).
**KDY NEPLATÍ:** drag a drop, kde je zvednutí prvku hlavní zpětná vazba. A prvek, který se
při interakci opravdu stane plovoucí vrstvou (karta se rozbalí do modálu).

### V tmavém tématu je nositel hloubky světlejší plocha, ne stín

**PRAVIDLO:** V dark mode udělej výše ležící vrstvu světlejší než tu pod ní a stín ber jen jako
doplněk. Nepřenášej světlou škálu stínů do tmavého tématu jedna ku jedné.
**KDY PLATÍ:** každé tmavé téma.
**PROČ:** Stín je tmavší plocha. Na tmavém pozadí mezi nimi není luminanční rozdíl, o který by
se oko opřelo, takže vrstva zmizí. Čtyřvrstvý barevný model (base a layer 01 až 03) tenhle problém
nemá, protože se v tmavém tématu jen obrátí směr kroku.
**TŘÍDA:** C pro mechanismus (řemeslné odvození z toho, jak stín funguje), B pro řešení
(Carbon 11 dělá vrstvení barvou plochy v obou tématech).
**ZDROJ:** [Carbon 11, color usage](https://carbondesignsystem.com/elements/color/usage/),
čtyři vrstvy tématu. Konkrétní hex hodnoty tmavých témat Carbonu jsem neověřoval, neuvádím je.
**KDY NEPLATÍ:** plovoucí vrstva nad tmavým obsahem pořád stín potřebuje, jen ho čti jako
oddělovač okraje, ne jako nositele hloubky. Tam se stín kombinuje s viditelně světlejší plochou.

---

## Referenční škály, ověřené hodnoty

Carbon v9, šest pojmenovaných vrstev. Všimni si vzoru: `x = 0`, `blur = 2 × y`, `spread = 0`,
opacita konstantní 0,10, `y = elevace / 2`.

| Vrstva | Elevace | box-shadow |
|---|---|---|
| Base | 0 | none |
| Flat | 1 | none |
| Raised | 2 | `0 1px 2px 0 rgba(0,0,0,0.10)` |
| Overlay | 8 | `0 4px 8px 0 rgba(0,0,0,0.10)` |
| Sticky nav | 12 | `0 6px 12px 0 rgba(0,0,0,0.10)` |
| Temporary nav | 16 | `0 8px 16px 0 rgba(0,0,0,0.10)` |
| Pop-out | 24 | `0 12px 24px 0 rgba(0,0,0,0.10)` |

Zdroj: [archiv Carbon v9, Guidelines / Layer](http://web.archive.org/web/20240610013500/https://v9.carbondesignsystem.com/guidelines/layer/).
Dvě věci, které z té tabulky plynou a v diskusích o stínech se ztrácejí: **dvě ze šesti vrstev
mají stín `none`**, tedy plochy v toku obsahu (Base, Flat) jsou u IBM ploché, a vrstvy se stínem
jsou výhradně plovoucí (overlay, navigace, pop-out). Druhá věc: aktuální Carbon 11 už samostatnou
stránku o elevaci nemá, hloubka se v něm dělá layer tokeny, tedy barvou.

Material 3, šest úrovní v dp: **0, 1, 3, 6, 8, 12**. Zdroj:
[Google, `_md-sys-elevation.scss`](https://raw.githubusercontent.com/material-components/material-web/main/tokens/versions/v0_192/_md-sys-elevation.scss).
V M3 je ta hodnota vstup do tonálního posunu plochy, ne primárně do stínu.

## Co si o stínech nemyslet

- **"Měkký stín vypadá kvalitněji než tvrdý"** je řemeslná praxe (Refactoring UI), ne měření.
  Používej to jako default, ne jako argument v diskusi.
- **Stín nekóduje důležitost, kóduje vzdálenost od plochy.** Když chceš zvýraznit prvek, který
  neplave, sáhni po barvě, velikosti nebo poloze, ne po elevaci.
- Ke stínu se nesmí přidávat druhý význam. Jakmile v jednom rozhraní znamená stín u jednoho
  prvku "plave" a u jiného "je vybraný", přestane fungovat obojí.

## Souvisí

- [Stroke a hranice](stroke-a-hranice.md) je sesterská nota: ta řeší volbu mezi borderem, stínem,
  pozadím a mezerou, tahle řeší, jak má stín vypadat, jakmile už je rozhodnuto pro něj.
- [Pohyb](pohyb.md) pro to, jak se plovoucí vrstva má objevit a zmizet (vstupní a odchodová
  animace, přerušitelnost).
- [Layout Theory](../layout/layout-theory.md) pro whitespace a spacing, tedy pro první dva kroky
  z pravidla o oddělení ploch.
- [Osmibodová mřížka](../zakony-principy/osmibodova-mrizka.md) pro to, ať offsety a blury sedí
  na stejnou škálu jako spacing.
- [Design system DRIVE](../priklady-ds/design-system-drive.md) jako příklad, jak se tokeny
  zapisují do hotového systému.
- Box model má [HTML a CSS](../../web-dev/html-a-css.md). **Syntaxi `box-shadow` knihovna nikde
  nepopisuje**, `web-dev/` je úvod do HTML a CSS a stín v něm není. Ber ji z MDN.
