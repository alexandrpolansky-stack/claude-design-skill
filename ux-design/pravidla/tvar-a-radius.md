# Tvar a radius: ostré vs. kulaté hrany

Nota řeší volbu border-radius: kdy hranaté, kdy kulaté, jak postavit radius škálu a jak
spočítat radius vnořeného prvku. Otevři ji, když rozhoduješ o tvaru komponent, nebo když
potřebuješ zdůvodnit, proč je něco kulaté.

**Varování hned na úvod: tohle je evidenčně nejslabší téma celé knihovny.** Dva nezávislé
průzkumy (komunitní diskuse i forenzní audit zdrojů, 2026) skončily stejně: na otázku
"proč tady ostré a tady kulaté" neexistuje měřená odpověď. Jediný tvrdý nález je
negativní: nejcitovanější zdůvodnění oboru se při ověření rozpadlo (sekce "Co je
nepodložené" níže). Pravidla v téhle notě proto stojí na publikovaných konvencích
(třída B) a jsou tak označená. Kdo tu hledá "vědecky správný radius", nenajde ho,
protože žádný doložený neexistuje. Ani Refactoring UI, jinak nejcitovanější zdroj
implementačních škál, žádné pravidlo pro radius nemá (prohledáno, nenalezeno).

Sesterská nota: [Stroke a hranice](stroke-a-hranice.md) (border vs. stín vs. whitespace).

## Použitelná pravidla

### Výchozí radius škála: Material 3

**PRAVIDLO:** Když potřebuješ radius škálu, převezmi Material 3: 0 / 4 / 8 / 12 / 16 /
20 / 28 / 32 / 48 / full (px). Vyber z ní pro projekt 3 až 4 stupně a přiřazuj je podle
požadované kulatosti role, ne podle velikosti komponenty.
**KDY PLATÍ:** Nový projekt bez zděděného design systému; kdykoliv hrozí, že v projektu
vznikne pět různých ad hoc radiusů.
**PROČ:** Je to jediný plně parametrický publikovaný radius systém. Hodnota není
v konkrétních číslech (ta nikdo netestoval), ale v omezení počtu různých radiusů,
takže tvary působí jako jeden systém.
**TŘÍDA:** B (interní konvence Googlu, žádný publikovaný user test)
**ZDROJ:** https://m3.material.io/styles/shape/corner-radius-scale
**KDY NEPLATÍ:** Existující design systém s vlastní škálou, konzistence s ním má
přednost. Brand záměrně stroze pravoúhlý: GOV.UK žádnou radius škálu nepublikuje
a funguje.

### Optická kulatost vnořených prvků

**PRAVIDLO:** U prvku vnořeného do zakulaceného kontejneru spočítej vnitřní radius jako
vnější radius minus padding. Příklad z Material 3: kontejner radius 48, padding 14,
vnitřní prvek 48 − 14 = 34.
**KDY PLATÍ:** Obrázky v kartách, tlačítka v zaoblených panelech, avatary v chipech,
vnořené inputy. Čím větší vnější radius, tím je pravidlo důležitější.
**PROČ:** Stejný radius uvnitř i vně vytváří opticky nestejnou mezeru, v rohu se mezera
zaškrtí. Odečtení paddingu drží obě křivky koncentrické, mezera je vizuálně konstantní.
**TŘÍDA:** B (Material 3 konvence)
**ZDROJ:** https://m3.material.io/styles/shape/corner-radius-scale
**KDY NEPLATÍ:** Když vyjde vnitřní radius nula nebo záporný (padding je větší než
vnější radius), nech vnitřní prvek hranatý. U malých radiusů (do 4 px) je rozdíl pod
rozlišovací schopností, neřeš ho.

### Odlišuj interaktivní od neinteraktivního, konzistentně uvnitř systému

**PRAVIDLO:** Rozhodni jednou, čím se u tebe liší interaktivní prvky od neinteraktivních
(např. tlačítka zaoblená, panely a loga hranatá), a drž to v celém systému bez výjimky.
**KDY PLATÍ:** Vždy. Je to jediné zdůvodnění volby radiusu, které přežilo audit.
**PROČ:** Rozpoznatelnost tlačítka nese konzistentní odlišení uvnitř tvého systému, ne
kulatost sama. Přesně tohle NHS reálně otestovala (uživatelé poznali jejich tlačítka
jako tlačítka) a přesně tohle je legitimní jádro jejich volby: zaoblená interaktiva se
odliší od hranatého loga a panelů zbytku systému.
**TŘÍDA:** B (publikovaná konvence NHS; jejich usability test neměl kontrolní podmínku
s hranatými rohy, takže dokládá rozpoznatelnost, ne přínos kulatosti)
**ZDROJ:** https://service-manual.nhs.uk/design-system/components/buttons; řemeslné
odůvodnění hodnoty 4 px: https://github.com/nhsuk/nhsapp-frontend/issues/12
(3px spodní hrana nedává prostor pro 3D efekt; aktuálně `border-radius: 4px;
box-shadow: 0 4px 0 #00401e`)
**KDY NEPLATÍ:** Pravidlo neurčuje směr. Zaoblené interaktivní + hranaté statické
funguje stejně jako opak. A přestane rozlišovat, když stejný radius dáš interaktivním
i dekorativním prvkům zároveň.

### Zakulacení u klikatelných marketingových prvků

**PRAVIDLO:** U CTA tlačítek, bannerů a produktových obrázků v marketingovém kontextu
ber zakulacení jako bezpečný default a mírné plus proti ostrým 90° rohům. Žádnou
konkrétní hodnotu radiusu z toho neodvozuj.
**KDY PLATÍ:** Landing pages, online reklama, e-commerce dlaždice, tedy kontexty, kde
je metrika CTR.
**PROČ:** Jediná doménově shodná studie celého tématu: tři field experimenty
s reálným CTR plus eye-tracking, na CTA tlačítkách, obrázcích a logách na webu
a v online reklamě.
**TŘÍDA:** B/C hraničně (peer-reviewed field experimenty, ale closed access: N ani
velikosti efektů se nepodařilo ověřit; srovnání je binární curved vs. sharp, žádná
dose-response na hodnotu radiusu)
**ZDROJ:** Biswas, D., Abell, A., & Chacko, R. (2024). Curvy Digital Marketing Designs.
*Journal of Consumer Research*, 51(3), 552-570. DOI 10.1093/jcr/ucad078
**KDY NEPLATÍ:** Produktové UI a usability: studie měří marketingový klik, ne
použitelnost ani vnímanou klikatelnost. A nikdy s číslem "CTR o 17 až 55 % vyšší":
to číslo koluje s odkazem na tento paper, ale nepodařilo se ověřit, necitovat.

### Radius nezdůvodňuj psychologií

**PRAVIDLO:** Volbu radiusu zdůvodňuj konzistencí vlastního systému a konvencí sektoru.
Nikdy ji nezdůvodňuj tvrzeními "zaoblené je klikatelnější", "kulaté je přátelštější"
ani "ostré hrany mozek vnímá jako nebezpečí". Platí i pro texty pro klienty
a dokumentaci design systému.
**KDY PLATÍ:** Vždy, hlavně když se píše zdůvodnění, které někdo bude číst a citovat.
**PROČ:** Všechna tahle tvrzení jsou třída C. NHS "research" neexistuje, preference
zakřivení na UI doložena není a amygdala argument stojí na fMRI s N = 16 z jiné domény,
přičemž meta-analýza mechanismus u prožitku nepotvrdila. Detaily v sekcích níže.
**TŘÍDA:** C (metodické pravidlo téhle knihovny, opřené o negativní rešerši 2026,
ne o měření)
**ZDROJ:** Forenzní stopa a meta-analýza v sekcích níže (NHS commit, Chuquichambi 2022).
**KDY NEPLATÍ:** Až někdo publikuje UI studii s kontrolní podmínkou hranatých rohů
a měřeným chováním, tuhle notu přepiš. Do té doby výjimka není.

## Co je nepodložené: "zaoblené rohy jsou klikatelnější" (třída C, nejhorší podtyp)

Nejcitovanější zdůvodnění kulatých rohů zní: "there is research to suggest that rounded
corners make things more clickable" (NHS design system, stránka Buttons). Tvrzení se
tváří jako věda, ale zdroj neexistuje. Forenzní stopa (ověřeno 2026):

- Věta žije v souboru `app/views/design-system/components/buttons/index.njk` (ř. 228)
  v repu `nhsuk/nhsuk-service-manual`. Přišla commitem
  [`01a66a29`](https://github.com/nhsuk/nhsuk-service-manual/commit/01a66a29d7200a5519321efd07a014f8d5f428f6)
  z 19. 2. 2019: hromadný redakční commit ("Change design examples and other content",
  24 souborů), bez citace v diffu.
- PR [nhsuk/nhsuk-service-manual#125](https://github.com/nhsuk/nhsuk-service-manual/pull/125):
  0 komentářů, 0 review komentářů.
- **Co ta věta nahradila, je nejdůležitější detail.** Původní text byl užší a poctivý:
  "We tested a primary button on a 'Register with a GP' form. Users understood that it
  was a button and knew what action it performed." Commit posunul zdůvodnění
  z "otestovali jsme jeden formulář" na "existuje výzkum".
- Logická vada: NHS testovala rozpoznatelnost svých vlastních, už zaoblených tlačítek.
  Bez kontrolní podmínky s hranatými rohy je výsledek kompatibilní s tím, že radius
  nehraje žádnou roli.
- Code search přes celou organizaci `nhsuk`: fráze "more clickable" má jediný výskyt,
  a je to sama ta stránka. Zdroj neexistuje nikde v organizaci.
- Za 7 let se nikdo nezeptal na citaci (issue
  nhsuk-service-manual-community-backlog#7, otevřená od 2/2019, 38 komentářů do 1/2026).
- Vzorec se zopakoval 2025: nhsuk/nhsapp-frontend#308 tvrdí přínos zaoblení "based on
  Gestalt principles" a odkazuje na přehledovou stránku Gestalt principů, která corner
  radius ani klikatelnost vůbec nezmiňuje.

Rozděl to na dvě tvrzení s různou třídou:

- "Zaoblené rohy dělají prvky klikatelnějšími" = **třída C**, nejhorší podtyp: tváří se
  jako věda, zdroj neexistuje.
- "NHS používá radius 4 px na tlačítkách" = **třída B**, obhajitelné jako konzistentní
  odlišení interaktivních prvků ve vlastním systému (viz pravidlo výše).

Symetrická poznámka k druhé straně sporu: **GOV.UK nikdy nepublikoval odůvodnění svých
hranatých rohů.** "Vláda = hranaté" je konvence bez publikované teorie. Ani jedna strana
sporu ostré vs. kulaté tedy nemá evidenci, jen NHS své (chybné) zdůvodnění aspoň napsala.

## Preference zakřivení (Bar & Neta) na UI nepřenášej

Bar, M., & Neta, M. (2006). Humans Prefer Curved Visual Objects. *Psychological Science*,
17(8), 645-648. DOI 10.1111/j.1467-9280.2006.01759.x. Nejčastější "vědecká" citace pro
kulaté rohy. Problémy:

- Abstrakt neobsahuje jediné číslo ani metodu, paper je closed access. N = 14
  a expozice 84 ms jsou dostupné jen ze sekundárního zdroje (Gómez-Puerto et al. 2016).
- Amygdala claim ("ostré aktivuje strach") v paperu z 2006 vůbec není. Je z Bar & Neta
  2007 (*Neuropsychologia*, 45(10), fMRI, N = 16, PMC4024389). Kdo ho připisuje 2006,
  cituje špatně.

Rozhodující je meta-analýza: Chuquichambi et al. (2022), *Annals of the New York Academy
of Sciences*, 1518(1), 151-165, PMC10091794. 61 studií, 106 vzorků, 11 023 účastníků.
Celkově preference zakřivení existuje (Hedges' g = 0,39 [0,25-0,52], publikační bias
nenalezen), ale **efekt vyhasíná přesně po ose směrem k UI:**

| Typ stimulu | g | signifikantní |
|---|---|---|
| Abstraktní patterny (meaningless) | 0,56 | ano |
| Reálné objekty | 0,42 | ano |
| Symbolic design (loga, typefaces) | 0,30 | **NE** |
| Spatial design (interiéry, fasády) | −0,04 | **NE** |

Dál: u expertů g = 0,13 (nesignifikantní), při neomezeném čase prohlížení klesá efekt
na polovinu (0,32 vs. 0,75 při limitované expozici). Tedy největší je přesně
v laboratorním paradigmatu Bar & Neta a nejmenší, když se člověk normálně dívá.

**V celé meta-analýze není ani jedna studie na UI, web, obrazovku, button nebo ikonu.**
Autoři verbatim: "preference for visual curvature is a reliable but not universal
phenomenon". K mechanismu: amygdala na hranaté reaguje, ale "found no evidence that
pleasure-related neural structures respond differently".

Verdikt: preference zakřivení je reálná u abstraktních tvarů a citace Bar & Neta pro
border-radius je cross-domain skok. Blogová tvrzení typu "mozek vnímá ostré jako
nebezpečné, proto zaobluj tlačítka" jsou nedoložená.

## Jak rozhodnout v praxi

1. Existuje zděděný systém nebo sektorová konvence? Drž se jich (viz škála výše).
2. Není? Vezmi Material 3 škálu, vyber 3 až 4 stupně, přiřazuj podle role.
3. Odliš interaktivní od neinteraktivního a drž to konzistentně.
4. Vnořené prvky: vnitřní radius = vnější − padding.
5. Zdůvodnění piš přes konzistenci a konvenci, nikdy přes psychologii tvarů.

Související: [Stroke a hranice](stroke-a-hranice.md) (borderů se týká stejný princip
konzistence), [Layout Theory](../layout/layout-theory.md) (whitespace jako alternativa
ohraničování).
