# Souhrny a agregace

Jak se staví pruh čísel nad daty, aby říkal pravdu i o tom, co se v součtu ztratí. Otevři,
když stavíš dashboard, KPI pás, souhrnný řádek tabulky nebo cokoliv, co jedním číslem mluví
za víc jednotek.

Související: [Stavové indikátory](stavove-indikatory.md) ·
[Stabilita layoutu](stabilita-layoutu.md) · [Datové tabulky](../komponenty/datove-tabulky.md) ·
[Prázdné stavy](prazdne-stavy.md)

---

## Rychlé rozhodnutí

1. Souhrn má odpovědět na otázku **„je potřeba zasáhnout"**, ne jen „kolik toho je". Když na ni
   neodpovídá, není to dashboard, je to výpis.
2. Co se má porovnávat, musí být vidět **zároveň**. Přehled rozřezaný na výběry porovnání
   znemožní, a přitom každý jednotlivý pohled vypadá v pořádku.
3. Samotné číslo nic neříká. Přidej k němu **porovnání** (cíl, historie, práh) a **kvalitativní
   stav** (dobré, uspokojivé, špatné).
4. Zajímá-li čtenáře odchylka, ukaž **rovnou ji**, ne dvě čísla k odečtení. U různě velkých
   jednotek **v procentech**, jinak se ta horší schová.
5. **Agregát přes nerovnoměrně vytížené jednotky zamlčí tu, která je v problému.** Průměr ani
   součet neřeknou, že jeden člen hoří. Ukaž rozložení, ne jen střed.
6. Konsolidovaný stav bere **nejzávažnější** ze stavů, které konsoliduje. Pravidlo je
   v [Stavových indikátorech](stavove-indikatory.md), sekce Konsolidovaný stav.
7. Když je vizuálně výrazné všechno, nevyčnívá nic. Prominentní má být to, co **teď** potřebuje
   pozornost.
8. Nestřídej typy zobrazení pro rozmanitost. Pět stejných ukazatelů se čte jednou naučenou
   strategií, pět různých pětkrát.
9. Přesnost na souhrnu jen taková, jaká se čte. `$3,848,305.93` na dashboardu zdržuje.
10. Signál, který se počítá a nikde nezobrazuje, je **kandidát na smazání**, ne na doplnění.

---

## Souhrn má říct, kdy je potřeba zasáhnout

**PRAVIDLO:** Souhrnná obrazovka musí poskytnout přehled, ze kterého se pozná, že je potřeba
akce, a cestu k detailu, který určí jakou. Když nejde poznat, že je někde problém, souhrn
neplní svůj účel, i kdyby všechna čísla na něm byla správně.
**KDY PLATÍ:** Dashboard, KPI pás, přehledová stránka, souhrnný řádek nad tabulkou.
**PROČ:** Je to obsažené v samotné definici dashboardu, která se v oboru ujala: displej
nejdůležitějších informací potřebných k dosažení cíle, na jedné obrazovce, sledovatelný na
první pohled. „Na první pohled" je funkční požadavek, ne estetický.
**TŘÍDA:** B (přijatá konvence oboru, ne měření)
**ZDROJ:** Stephen Few, *Common Pitfalls in Dashboard Design*, Perceptual Edge 2005, definice
poprvé publikovaná v Intelligent Enterprise, březen 2004, verbatim: „A dashboard is a visual
display of the most important information needed to achieve one or more objectives,
consolidated and arranged on a single screen so the information can be monitored at a glance."
a dál „it must provide the overview that is needed to know when action is required, and ideally
should provide an easy gateway to any additional information that is needed to determine the
precise action that is appropriate."
https://www.perceptualedge.com/articles/Whitepapers/Common_Pitfalls.pdf
**KDY NEPLATÍ:** Výkaz, který se čte jednou za měsíc a nese úplnost, ne pohotovost. Tam je
sledovatelnost na první pohled špatné kritérium a patří tam detail.

## Přehled nerozřezávej na výběry

**PRAVIDLO:** Když je smyslem obrazovky celkový obraz, nesmí být rozřezaný na kusy, které jdou
zobrazit jen po jednom přes přepínač, výběr nebo rozbalovátko. Totéž platí pro scrollování:
co uživatel musí ztratit z očí, aby uviděl zbytek, s tím zbytkem už neporovná.
**KDY PLATÍ:** Přehledová obrazovka, jejíž hodnota je v tom, že se části vidí zároveň.
**PROČ:** Porovnání je nejčastější důvod, proč se na přehled někdo dívá, a rozřezání ho udělá
nemožným, aniž by to bylo na první pohled vidět: každý jednotlivý pohled vypadá v pořádku.
**TŘÍDA:** C
**ZDROJ:** Few, Pitfall #1, verbatim: „Something critical is sacriﬁced when the viewer must lose
sight of some data in order to scroll down or over, or move from screen to screen to see the
rest." a k té konkrétní chybě „With this design, the viewer can never compare the performance of
products or regions, which is a common need. Splitting the big picture into a series of separate
small pictures is a mistake when seeing the big picture is worthwhile."
https://www.perceptualedge.com/articles/Whitepapers/Common_Pitfalls.pdf
**KDY NEPLATÍ:** Když části opravdu nikdo neporovnává a jde jen o úsporu místa. Pak je výběr
v pořádku. Rozhodni to podle úkolu, ne podle toho, kolik se toho vejde. Carbon dochází ke
stejnému závěru pro taby: uživatel, který potřebuje porovnávat mezi skupinami, nemá dostat taby,
viz [Taby](../komponenty/taby.md), sekce Kdy taby a kdy ne.

## Číslo bez kontextu nic neříká

**PRAVIDLO:** Ke každé klíčové míře přidej aspoň jedno porovnání (cíl, historie, práh) a rychlý
vizuální způsob, jak přečíst její kvalitativní stav. Holé číslo nechává čtenáře s otázkou
„a to je hodně, nebo málo".
**KDY PLATÍ:** Každá dlaždice, každý souhrnný údaj.
**PROČ:** Few to formuluje otázkami, které si čtenář položí sám: srovnáno s čím, je to dobře
nebo špatně, jak moc, jsme na plánu. To je rozdíl mezi číslem, které na obrazovce jen sedí,
a číslem, které vede k akci.
**TŘÍDA:** C (řemeslné pozorování doložené příklady, bez měření)
**ZDROJ:** Tamtéž, Pitfall #2, verbatim: „To state that quarter-to-date sales total $736,502
without any context means little. Compared to what? Is this good or bad? How good or bad? Are we
on track? Is this better than before? The right context for the key measures makes the
diﬀerence between numbers that just sit there on the screen and those that enlighten and inspire
action." A k tomu, čím se kontext dodává: „Measures of what's currently going can be enriched by
providing one or more comparative measures, such as a target or some history, as well as a quick
visual means for assessing the measure's qualitative state (for example, good, satisfactory, or
bad)."
https://www.perceptualedge.com/articles/Whitepapers/Common_Pitfalls.pdf
**KDY NEPLATÍ:** Míra, u které kontext neexistuje a vymyslet ho by znamenalo předstírat cíl,
který nikdo nestanovil. Pak je poctivější holé číslo než falešný práh.

## Ukaž rozdíl, ne dva údaje, ze kterých se odečítá

**PRAVIDLO:** Když čtenáře zajímá odchylka, ukaž rovnou ji, ne dvě čísla a odčítání jako domácí
úkol. A když se porovnávají jednotky různé velikosti, vyjádři ji **v procentech**, ne v absolutní
hodnotě.
**KDY PLATÍ:** Skutečnost proti plánu, čerpání proti alokaci, spotřeba proti kvótě. Kdekoliv se
jedna hodnota čte vůči druhé.
**PROČ:** Absolutní odchylka je u různě velkých jednotek nesrovnatelná a schová tu horší z nich.
Fewův příklad je přesný: malé oddělení přes rozpočet o 5 000 může být větší problém než velké
oddělení přes rozpočet o 50 000, a **pozná se to jenom v procentech**. To je zároveň důvod, proč
`usedPct` patří vedle částek a ne místo nich: procento umožní porovnání napříč, částka nese
velikost dopadu.
**TŘÍDA:** C
**ZDROJ:** Few, Pitfall #4, verbatim: „If the dashboard viewer only needs to know by how much
actual revenue diﬀers from budgeted revenue, rather than displaying the actual revenue amount of
$76,934 and the budgeted revenue amount of $85,000 and leaving it to the viewer to calculate the
diﬀerence, why not display the variance amount directly?" a k volbě jednotky „Percentages also
make it easier to compare the variances of multiple items when their actual values diﬀer
signiﬁcantly in scale, such as the variances of actual from budgeted expenses for several
departments, each with it own budget. A small department's over-budget amount of $5,000 could be
more troubling than a large department's over-budget amount of $50,000, but this might only be
obvious if the variance were expressed as a percentage."
https://www.perceptualedge.com/articles/Whitepapers/Common_Pitfalls.pdf
**KDY NEPLATÍ:** Když je absolutní částka sama o sobě rozhodovací veličina (schvaluje se výdaj,
ne jeho poměr). Pak procento odchylku relativizuje a je potřeba obojí, s částkou jako hlavním
údajem.

## Agregát přes nerovnoměrné jednotky zamlčí tu, která je v problému

**PRAVIDLO:** Když jedno číslo mluví za víc jednotek, které se můžou chovat nerovnoměrně,
neukazuj jen střed nebo součet. Rozložení musí být na obrazovce taky, jinak souhrn tvrdí klid
i ve chvíli, kdy je jeden člen v potížích.
**KDY PLATÍ:** Cokoliv agregovaného přes týmy, účty, uzly, regiony, zákazníky.
**PROČ:** Google SRE to pojmenovává jako past, do které se padá při stavbě monitoringu od nuly,
a jmenuje přímo „mean fullness of your databases": jednotky se dají vytížit velmi nerovnoměrně,
takže střed o nich přestane vypovídat. Bez rozložení je představa, že se členové drží u středu,
jen zbožné přání.
**TŘÍDA:** B (publikovaná konvence velké organizace s odůvodněním, ne studie)
**ZDROJ:** Google SRE Book, *Monitoring Distributed Systems*, sekce Worrying About Your Tail,
verbatim: „it's tempting to design a system based upon the mean of some quantity: the mean
latency, the mean CPU usage of your nodes, or the mean fullness of your databases. The danger
presented by the latter two cases is obvious: CPUs and databases can easily be utilized in a very
imbalanced way." a v poznámce pod čarou „if you're not measuring your distribution, the idea that
most of your requests are near the mean is just hopeful thinking."
https://sre.google/sre-book/monitoring-distributed-systems/
**KDY NEPLATÍ:** Agregát, jehož jednotky jsou zaměnitelné a jejich zdroj je společný (kapacita
jednoho fondu, ze kterého všichni čerpají). Tam součet opravdu odpovídá na otázku „kolik zbývá".
Rozhoduje se to podle toho, jestli přebytek jedné jednotky může pokrýt schodek druhé. **Když
nemůže, součet na otázku o zásahu neodpovídá, ať je aritmeticky jakkoliv správný.**

## Když je výrazné všechno, nevyčnívá nic

**PRAVIDLO:** Vizuální prominenci rozděl podle toho, co potřebuje pozornost teď, ne rovnoměrně
mezi všechna data. Prvky, které nejsou data (logo, navigace), utlum.
**KDY PLATÍ:** Rozvržení souhrnné obrazovky.
**PROČ:** Všechna data na dashboardu mají být důležitá, ale ne stejně důležitá. Když soupeří
o pozornost všechno, oko nedostane žádné vodítko, kam se podívat, a obrazovka selhala jako celek.
**TŘÍDA:** C
**ZDROJ:** Tamtéž, Pitfall #10, verbatim: „You should be able to look at a dashboard and have
your eyes immediately drawn to the information that is most important. When everything is
visually prominent, nothing stands out. All of the data displayed on a dashboard ought to be
important, but not all data are equally important." A z Pitfall #9: „The most important data
ought to be prominent. Data that requires immediate attention ought to stand out."
https://www.perceptualedge.com/articles/Whitepapers/Common_Pitfalls.pdf
**KDY NEPLATÍ:** Nic, ale pozor na obrácenou chybu: utlumit se dá i tak, že se výrazné stane
zase všechno, jen tišeji.

## Rozmanitost zobrazení není hodnota

**PRAVIDLO:** Vyber pro každý údaj to zobrazení, které funguje nejlíp, i kdyby jich na obrazovce
skončilo pět stejných. Nestřídej typy proto, aby to nebylo jednotvárné.
**KDY PLATÍ:** Skladba přehledové obrazovky, opakující se dlaždice, sada ukazatelů.
**PROČ:** Stejné zobrazení znamená, že čtenář použije na všechny stejnou strategii čtení, což ho
stojí míň času. Střídání ho nutí přepínat, a to je práce navíc, kterou nedostal zaplacenou žádnou
informací. Nudit ho nebude data, která potřebuje k práci, ale zdrží ho to, když se k nim musí
prokousávat pokaždé jinak.
**TŘÍDA:** C
**ZDROJ:** Few, Pitfall #6, verbatim: „You should always select the means of display that works
best, even if that results in a dashboard that is ﬁlled with nothing but multiple instances of
the same type of graph." a k odůvodnění „consistency in the means of display whenever
appropriate allows viewers to use the same perceptual strategy for interpreting the data, which
saves them time and energy."
https://www.perceptualedge.com/articles/Whitepapers/Common_Pitfalls.pdf
**KDY NEPLATÍ:** Když dvě data mají opravdu jinou povahu. Pak je jiný typ zobrazení správná
odpověď a jednotvárnost by byla ta chyba. Rozhoduje povaha dat, ne pocit ze stránky.

## Přesnost jen taková, jaká se čte

**PRAVIDLO:** Na souhrnu nepiš víc desetinných míst ani jemnější časové jednotky, než kolik
čtenář při sledování použije.
**KDY PLATÍ:** Dlaždice, KPI pás, souhrnné řádky. **Ne** datová tabulka, kde se čísla
sesouhlasují do haléře.
**PROČ:** Každá nadbytečná informace na dashboardu stojí čas, a čas je přesně to, o co při
sledování jde. Few dává příklad na penny: `$3,848,305.93` proti `$3,848,306` nebo rovnou `$3.8M`.
**TŘÍDA:** C
**ZDROJ:** Tamtéž, Pitfall #3, verbatim: „dashboards should never display information that is
more detailed or precise than necessary. To do so would force the viewer to process levels of
data that are irrelevant to the task at hand."
https://www.perceptualedge.com/articles/Whitepapers/Common_Pitfalls.pdf
**KDY NEPLATÍ:** Tabulka, ze které se čísla skládají a musí sednout na součet. Tam je zaokrouhlení
ztráta dat, ne úspora času.

## Signál, který se nikde nezobrazuje, patří pryč

**PRAVIDLO:** Údaj, který se počítá a posílá, ale žádná obrazovka ani upozornění ho nepoužívá,
je kandidát na smazání, ne na doplnění.
**KDY PLATÍ:** Revize kontraktu mezi serverem a obrazovkou, úklid dashboardu.
**PROČ:** Nepoužitý údaj se nikdy neověří proti realitě, takže tiše zestárne nebo se rovnou
spočítá špatně, a první, kdo ho vykreslí, tomu bude věřit. Google SRE ho řadí ke kandidátům na
odstranění vedle konfigurace, která se spouští jednou za čtvrtletí.
**TŘÍDA:** B
**ZDROJ:** Google SRE Book, *Monitoring Distributed Systems*, sekce As Simple as Possible, No
Simpler, verbatim: „Signals that are collected, but not exposed in any prebaked dashboard nor
used by any alert, are candidates for removal."
https://sre.google/sre-book/monitoring-distributed-systems/
**KDY NEPLATÍ:** Údaj vědomě připravený pro obrazovku, která se právě staví. Pak má datum,
do kdy se použije, ne trvalé bydliště v kontraktu.

---

## Kontrolní seznam

1. Kdyby byl jeden člen v problému, poznám to z pruhu nahoře, nebo až z tabulky pod ním?
2. Může přebytek jedné jednotky pokrýt schodek druhé? Když ne, součet neodpovídá na otázku
   o zásahu a musí ho doprovodit rozložení.
3. Je něco, co se má porovnávat, dostupné jen po jednom přes výběr nebo scroll?
4. Má každé číslo v souhrnu porovnání a kvalitativní stav, nebo tam jen sedí?
5. Odečítá si někde čtenář dvě čísla, která bych mu mohl rovnou ukázat jako rozdíl?
6. Porovnávám jednotky různé velikosti? Pak je odchylka v procentech, ne v absolutní hodnotě.
7. Nese konsolidovaný stav nejzávažnější z podřízených, nebo se počítá znovu z agregátu?
8. Kam padne oko jako první? Je to to, co potřebuje pozornost teď?
9. Střídají se na obrazovce typy zobrazení proto, že to data vyžadují, nebo aby to nebylo
   jednotvárné?
10. Kolik desetinných míst se na souhrnu opravdu čte?
11. Počítá server něco, co žádná obrazovka nezobrazuje?

## Zdroje

- Stephen Few, *Common Pitfalls in Dashboard Design*, Perceptual Edge 2005, PDF, 38 stran,
  přečteno 7. 9. 2026. Definice dashboardu je z jeho článku „Dashboard Confusion", Intelligent
  Enterprise, březen 2004. Whitepaper je sponzorovaný (ProClarity) a druhá polovina je produktová
  prezentace; **13 pastí v první polovině na tom nezávisí a jen ty jsou tu použité**.
  https://www.perceptualedge.com/articles/Whitepapers/Common_Pitfalls.pdf
- Google SRE Book, kapitola *Monitoring Distributed Systems*, přečteno 7. 9. 2026.
  https://sre.google/sre-book/monitoring-distributed-systems/

Fewův zdroj je PDF a `scripts/verify-citations.py` na něm původně vracel binární obsah, takže
se každá citace z něj hlásila jako nedostupná. Skript to od 7. 9. 2026 umí: URL končící `.pdf`
protáhne přes `pdftotext`. Všech deset citací v téhle notě je tím ověřených.
