# Kontext: děti

**Kdo je čtenář.** Dvě různé osoby najednou. Dítě v jednom ze tří věkových pásem (3 až 5, 6 až 8,
9 až 12), která se od sebe liší tak moc, že "pro děti" není cílová skupina, a dospělý gatekeeper
(rodič, učitel), který o použití rozhoduje, platí ho a čte podmínky. Rozhraní pro dospělého se řídí
běžnými pravidly, ne pravidly z téhle noty.

**Dopad chyby.** Dítě neúspěch nenahlásí. Nezvládnutou interakci si vyloží jako vlastní chybu,
zkusí něco jiného, nebo skončí. Zpětná vazba tedy nepřijde, což znamená, že chyby se musí odchytit
testováním, ne stížnostmi. Druhá vrstva dopadu je právní: chyba v defaultech a ve sběru dat je
sankcionovatelná, i když je rozhraní jinak funkční.

**Regulace vs volba.** Regulace v tomhle sektoru je o SOUKROMÍ, ne o vzhledu. ICO Age Appropriate
Design Code (Children's Code) je vynutitelný ve Velké Britanii od 9/2021, má 15 standardů a stojí
na kritériu "best interests of the child". Řídí defaulty, sběr dat, profilování a nudging.
Nemíchat ho s nálezy o typografii, jsou to dvě nesouvisející věci. Vizuální a interakční rozhodnutí
jsou volba, s výjimkou WCAG kritérií, která platí jako všude.

**Evidenčně je to jeden z lépe podložených sektorů v knihovně.** Nálezy o věkové segmentaci,
velikosti písma a o tom, že animace a zvuk jsou u dětí žádoucí, mají za sebou opakované testování
s dětmi. Naopak "děti mají rády syté barvy" je tradovaná konvence bez opory.

Legenda tříd: A = tvrdá opora (měření), B = publikovaná konvence nebo regulace, C = řemeslná praxe
či pozorování bez opory.

Sesterské noty: [seniori.md](seniori.md), [e-commerce.md](e-commerce.md), [vlada.md](vlada.md)
(rozpis regulatorních rámců a WCAG parametrů), [zdravotnictvi.md](zdravotnictvi.md),
[dev-tools-saas.md](dev-tools-saas.md), [finance.md](finance.md), [luxury.md](luxury.md).

---

## Pravidla

### Segmentuj podle věku, nestav "pro děti"

**PRAVIDLO:** Rozhodni, pro které pásmo stavíš (3 až 5, 6 až 8, 9 až 12), a nemíchej je v jednom
rozhraní. Pásma se liší v tom, jestli uživatel vůbec čte, jak skenuje a jestli zvládne scroll.
**KDY PLATÍ:** Na začátku projektu, dřív než padne první rozhodnutí o layoutu.
**PROČ:** Nejmladší pásmo nečte vůbec a interaguje explorativně. Nejstarší pásmo skenuje podobně
jako dospělí. Rozhraní optimalizované pro průměr těch tří skupin nefunguje ani pro jednu.
**TŘÍDA:** A.
**ZDROJ:** NN/g, kumulativně 125 dětí ve třech vlnách testování (2001, 2010, 2018).
**KDY NEPLATÍ:** Rodičovská nebo učitelská část aplikace je rozhraní pro dospělého. Tam platí běžná
pravidla a věkovou segmentaci na ni neaplikuj.

### Velikost písma podle pásma

**PRAVIDLO:** Default velikost těla textu 14pt pro 3 až 8 let a 12pt pro 9 až 12 let, a nikdy
méně. V CSS to je přibližně 18,7 px a 16 px (převod 72pt na 96 px na palec).
**KDY PLATÍ:** Veškerý text určený dítěti.
**PROČ:** Menší text mladší děti prostě nepřečtou dost rychle, aby ho použily jako instrukci.
Doporučení je z testování s dětmi, ne z dospělé typografie.
**TŘÍDA:** A pro hodnoty v pt, C pro převod na CSS px (převod je aritmetika, ale původní doporučení
vznikla pro desktopové obrazovky své doby, ne pro dnešní hustoty a mobil).
**ZDROJ:** NN/g, testování s dětmi (125 dětí, tři vlny).
**KDY NEPLATÍ:** Pravidlo dává podlahu, ne strop. Větší text je v pořádku. A neplatí pro rozhraní
dospělého v téže aplikaci.

### U začínajících čtenářů bezpatkový font a velká velikost

**PRAVIDLO:** Pro text určený začínajícím čtenářům (přibližně 6 až 8 let) použij bezpatkový font
v přibližně 18pt (asi 24 CSS px).
**KDY PLATÍ:** Cvičení a obsah, kde dítě text skutečně čte, ne jen prochází.
**PROČ:** Z testovaných kombinací fontu a velikosti vyšla Arial 18pt nejlépe pro začínající
čtenáře. Mechanismus je velikost a jednoduchost tvarů, ne konkrétní jméno fontu.
**TŘÍDA:** A ve své studii, ale s výhradou: konkrétní čísla máme jen ze sekundárního zdroje,
primární text nebyl získán, takže přesnou metodiku, N ani effect size neuvádět.
**ZDROJ:** Woods, Davis, Scharff (2005), srovnání fontů a velikostí u začínajících čtenářů.
**KDY NEPLATÍ:** Neber to jako "Arial je nejlepší font pro děti". Studie testovala konkrétní sadu
kombinací, ne všechny fonty. Jakýkoliv čitelný bezpatkový font v té velikosti je legitimní volba.

### Animace a zvuk jsou u dětí žádoucí, ne šum

**PRAVIDLO:** U dětí do přibližně 8 let používej animaci a zvuk jako součást zpětné vazby
a odměny. Nepotlačuj je podle pravidel pro dospělá rozhraní.
**KDY PLATÍ:** Interakce, u kterých má dítě poznat, že jeho akce něco udělala.
**PROČ:** Děti animaci a zvuk aktivně vyhledávají a berou je jako součást zážitku. To je přímý
opak dospělých uživatelů, kterým totéž vadí a hlásí to jako rušení. Pravidla pro dospělá
produktová rozhraní se tady tedy nepřenášejí.
**TŘÍDA:** A pro preferenci.
**ZDROJ:** NN/g, testování s dětmi (125 dětí, tři vlny).
**KDY NEPLATÍ:** Zvuk musí být vypnutelný a nikdy nesmí být jediný nositel informace, protože
dítě může být v prostředí bez zvuku nebo se sluchovým postižením (to je C, řemeslná zásada
odvozená z obecného principu neschovávat informaci do jednoho kanálu). Respektuj taky
`prefers-reduced-motion`. A neplatí to na rodičovskou část aplikace.

### U nejmladších nenes instrukci textem

**PRAVIDLO:** Pro 3 až 5 let nedávej instrukci textem. Použij ikonu, ukázku pohybem, animovanou
demonstraci nebo namluvený hlas. Text ber jako doplněk pro dospělého, který sedí vedle.
**KDY PLATÍ:** Každá instrukce, nápověda a chybová zpráva v nejmladším pásmu.
**PROČ:** Nejmladší děti nečtou vůbec. Text pro ně není nositelem informace, je to grafika.
**TŘÍDA:** A.
**ZDROJ:** NN/g, testování s dětmi.
**KDY NEPLATÍ:** V pásmu 9 až 12 už text funguje a skenování se blíží dospělému. Tam je naopak
mluvený komentář, který nejde přeskočit, zdržení.

### U mladších drž interakci bez scrollu

**PRAVIDLO:** Pro 3 až 8 let drž jednu úlohu na jedné obrazovce bez scrollování. Co je pod hranou
viewportu, pro ně neexistuje.
**KDY PLATÍ:** Herní a cvičební obrazovky v mladších pásmech.
**PROČ:** Mladší děti se scrollování aktivně vyhýbají a obsah pod hranou nenajdou. Není to otázka
motivace, prostě nezkusí, že by tam mohlo něco být.
**TŘÍDA:** A.
**ZDROJ:** NN/g, testování s dětmi.
**KDY NEPLATÍ:** Pásmo 9 až 12 scrolluje bez problému. A když je scroll součástí hry (vertikální
mapa, časová osa), je to jiná situace než skrytý obsah.

### Sytou paletu neodůvodňuj tím, že "děti mají rády barvy"

**PRAVIDLO:** Volbu palety odůvodni kontrastem, rozlišitelností prvků a brandem. Nepoužívej
argument "děti preferují syté barvy", ten nemá zdroj.
**KDY PLATÍ:** Vždy, když se paleta obhajuje dojmem o cílové skupině.
**PROČ:** Žádná studie tvrzení nepodporuje. Nejblíž je nález z jiné domény, kde design založený
na silné barvě jedné rodiny byl hodnocen jako MÉNĚ estetický než varianty s velkými obrázky nebo
s vyváženým poměrem obrazu a textu. Na dětský kontext se to přenést přímo nedá (byly to firemní
weby a dospělí hodnotitelé), ale univerzálku "sytější je lepší" to nepodporuje.
**TŘÍDA:** C, NENALEZENO.
**ZDROJ:** Prohledáno v rámci evidenčního auditu (7/2026), nenalezeno nic. Nejblíž Douneva, Jaron,
Thielsch (2015/2016), Interacting with Computers 28(4), 552-567, N=458: kategorie SCOFA (silná
barva jedné rodiny) hodnocena jako méně estetická než LAPIC (velké obrázky) a SAPAT (vyvážený
poměr), SAPAT navíc s nejlepší paměťovou výbavností.
**KDY NEPLATÍ:** Když barva nese funkci (úroveň, tým, kategorie), řeš rozlišitelnost a nespoléhej
jen na barvu. Sytost tam může být důsledek funkce, ne estetické rozhodnutí.

### Children's Code je privacy rámec, ne vizuální norma

**PRAVIDLO:** U služby, ke které se pravděpodobně dostanou děti a která je dostupná ve Velké
Britanii, projdi 15 standardů Children's Code a řeš defaulty, minimalizaci sběru dat, profilování,
geolokaci a nudging. Nepoužívej ten kód jako argument pro vizuální rozhodnutí.
**KDY PLATÍ:** Služby dostupné v UK, které dítě může používat, i když na děti primárně necílí.
**PROČ:** Kód je privacy-by-design rámec postavený na kritériu "best interests of the child".
Řeší, co se s dítětem děje v datech a jak ho rozhraní tlačí k rozhodnutím. Vzhled ani typografii
neupravuje, takže citovat ho u volby fontu je záměna.
**TŘÍDA:** B (regulace, vynutitelná od 9/2021).
**ZDROJ:** ICO, Age Appropriate Design Code (Children's Code), `ico.org.uk`, 15 standardů.
**KDY NEPLATÍ:** Mimo britskou jurisdikci není vynutitelný. Jako designové kritérium ("nejlepší
zájem dítěte") je použitelný i tam, ale pak je to volba, ne povinnost. K nudgingu a temným vzorům
viz [Etika v UX](../ux-zaklady/etika-v-ux.md).

### Testuj s dětmi, ale netvrď pokrytí

**PRAVIDLO:** Iteruj po malých kolech (řádově pět dětí na kolo) v tom věkovém pásmu, pro které
stavíš. Netvrď, že pět dětí odhalilo většinu problémů.
**KDY PLATÍ:** Formativní testování v průběhu vývoje.
**PROČ:** Malý vzorek najde většinu problémů v OČEKÁVANÉ hodnotě, ale rozptyl je obrovský:
v jedné replikaci některé náhodné pětice našly 99 % problémů a jiné jen 55 %. U dětí je navíc
heterogenita vyšší než u dospělých (věk, čtení, motorika, zkušenost se zařízením), a model malého
vzorku předpokládá právě homogenitu.
**TŘÍDA:** A.
**ZDROJ:** Faulkner (2003), Behavior Research Methods, peer-reviewed, N=60, verbatim: "Some of the
randomly selected sets of 5 participants found 99% of the problems; other sets found only 55%."
Deset lidí dá v nejhorším případě 80 %, dvacet 95 %.
**KDY NEPLATÍ:** Na kvantifikaci (kolik procent dětí zvládne úkol) malý vzorek nestačí vůbec.
NN/g sama uvádí minimálně 20 účastníků na kvantitativní studii, 15 na card sorting a 39 na
stabilní heatmapy.

---

## Co v tomhle sektoru NENÍ

| Tvrzení | Stav |
|---|---|
| "Děti preferují vysokou saturaci barev" | C, NENALEZENO |
| Children's Code předepisuje něco o vzhledu | NE, je to privacy rámec |
| Existuje vizuální norma pro dětská rozhraní | NENALEZENO |
| "Arial je nejlepší font pro děti" | přestřelené, studie testovala konkrétní sadu kombinací |

## Souvisí

- [Kontext: senioři](seniori.md), druhý sektor, kde má publikum měřitelně jiné schopnosti než
  designér, a kde platí opačná pravidla o animaci
- [Kontext: e-commerce](e-commerce.md), když aplikace pro děti obsahuje nákupy (kombinace
  s Children's Code je pak nejrizikovější místo celého produktu)
- [Etika v UX](../ux-zaklady/etika-v-ux.md), nudging a temné vzory
- [Design Research Methods](../ux-zaklady/design-research-methods.md), metody testování
- [Typography, základy a anatomie](../typography/typography-zaklady-anatomie.md), čitelnost
  a velikosti obecně
