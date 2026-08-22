# Stránkování

Dvě varianty, dvě různá umístění a pravidlo, kdy stránkovat vůbec nemá smysl.

Související: [Datové tabulky](datove-tabulky.md) · [Načítání a čekání](../vzory/nacitani-a-cekani.md) ·
[Přetečení a truncation](../vzory/preteceni-a-truncation.md)

---

## Rychlé rozhodnutí

1. Stránkování **pod tabulku**, naskládané, **bez odsazení**. Nikdy nad ni.
2. Stránkování nad **obsahem stránky** (ne tabulkou) plave pod obsahem, zarovnané vpravo. Když nevíš,
   vpravo.
3. **Nepoužívej stránkování na lineární cestu** (postup ve formuláři). Tam progress bar nebo tlačítka.
4. **Nepoužívej stránkování zbytečně.** Musí zlepšit použitelnost nebo výkon.
5. Výška stránkování se má rovnat výšce řádku tabulky. Na XL řádky použij LG, na XS řádky SM.
6. Výpustka v pagination nav **nikdy na začátku ani na konci** posloupnosti stránek.
7. Na kraji rozsahu se nedostupné tlačítko stává **nenavigovatelným**, jako každý disabled prvek.

---

## Kdy stránkovat

Carbon jmenuje pět důvodů:

1. Když by načtení všech dostupných dat naráz nebo ve scrollovacím pohledu zabralo značný čas.
2. Když je dat příliš mnoho na jednu stránku nebo jeden pohled komponenty.
3. Aby byla velká množství dat pro uživatele **strávitelnější**.
4. K optimalizaci prostoru na stránce.
5. Aby měl uživatel **víc kontroly** nad tím, jak si velké množství informací zobrazí.

**ZDROJ:** Carbon, Pagination usage, When to use.
https://carbondesignsystem.com/components/pagination/usage/

## Kdy nestránkovat

**PRAVIDLO:** **Nepoužívej stránkování na zobrazení lineárních cest**, například postupu ve formuláři.
Na navigaci dopředu a dozadu použij **progress bar** nebo **tlačítka**. A **nepoužívej stránkování
nadbytečně**, ať slouží k zlepšení použitelnosti nebo výkonu.
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Pagination usage, When not to use, verbatim: „Do not use pagination superfluously, and
aim to use it to improve usability or performance."
https://carbondesignsystem.com/components/pagination/usage/

**Praktický důsledek:** stránkování má výkonový důvod (nenačítat vše naráz) nebo orientační (uživatel
chce vědět, kolik toho je). Když ani jedno neplatí, přidáváš uživateli kliky za nic.

**Souvislost:** [Přetečení a truncation](../vzory/preteceni-a-truncation.md) má alternativu „Zobrazit
více" nebo „Načíst více", která má proti stránkování jinou vlastnost: nezahodí předchozí obsah. Carbon
„Load more" doporučuje, když je problém s výkonem a data se mají načítat v postupných dávkách.

## Dvě varianty

| Varianta | Kde |
|---|---|
| Pagination | Typicky **připojená pod datovou tabulku**, aby stránkovala velké množství dat |
| Pagination nav | Hlavně **on-page situace**: stránkování celé stránky nebo sekcí stránky |

**ZDROJ:** Carbon, Pagination usage, Variants.
https://carbondesignsystem.com/components/pagination/usage/

## Anatomie

**Pagination (lišta u tabulky):**

1. **Items per page:** aktuální počet položek na stránku.
2. **Range of items:** aktuální rozsah položek a celkové množství položek.
3. **Current page:** aktuální stránka a celkový počet stránek.
4. **Předchozí a další:** tlačítka na předchozí nebo další stránku.
5. **Kontejner:** lišta celé komponenty.

**Pagination nav:**

1. **Nevybrané tlačítko stránky.**
2. **Vybrané tlačítko stránky:** aktuální stránka.
3. **Overflow tlačítko:** obsahuje dostupné stránky, na které se lze navigovat, ale nelze je zobrazit
   dopředu kvůli aktuálnímu viewportu.
4. **Předchozí a další.**
5. **Kontejner.**

**ZDROJ:** Carbon, Pagination usage, Anatomy.
https://carbondesignsystem.com/components/pagination/usage/

## Velikosti a párování s tabulkou

Tři velikosti u obou variant: **large, medium, small**.

**PRAVIDLO:** Používej **stejnou výšku stránkování jako výšku řádku** datové tabulky, ke které je
připojené.
**Problém:** tabulka má **pět** výšek řádku, stránkování jen **tři**. Carbonovo řešení:

| Výška řádku tabulky | Stránkování |
|---|---|
| Extra large | **Large** |
| Large | Large |
| Medium | Medium |
| Small | Small |
| Extra small | **Small** |

**ZDROJ:** Carbon, Pagination usage, Data table size pairings, verbatim: „When using the extra large data
table row height, use the large pagination. When using the extra small data table row height, use the
small pagination." https://carbondesignsystem.com/components/pagination/usage/

## Umístění

**Obecné pravidlo:** dej stránkování **blízko související komponenty nebo oblasti stránky**, jejíž
informace se stránkuje.

### S datovou tabulkou

**PRAVIDLO:** Stránkování má být **naskládané a pod tabulkou, bez odsazení mezi nimi**.
**Nedávej stránkování nad tabulku.**
**KDY PLATÍ:** Vždy.
**TŘÍDA:** B
**ZDROJ:** Carbon, Pagination usage, Placing pagination with data table. Carbon to má jako explicitní
Do (naskládat pod tabulku) a Don't (naskládat nad tabulku).
https://carbondesignsystem.com/components/pagination/usage/

### Na stránce

**PRAVIDLO:** Pagination nav **plave pod obsahem**, který stránkuje. Lze ho zarovnat vpravo nebo vlevo
k obsahu nad ním. **Když nevíš, zvol zarovnání vpravo.**
**TŘÍDA:** B
**ZDROJ:** Carbon, Pagination usage, Placing pagination nav on a page, verbatim: „When it doubt, choose
right alignment." https://carbondesignsystem.com/components/pagination/usage/

## Obsah

| Prvek | Pravidlo |
|---|---|
| Label text | **Stručný a instruktivní.** Popisuje položky na stránku a počet stránek nebo položek. Carbon doporučuje **label neupravovat**, pokud to konkrétní případ nevyžaduje |
| Text volby v selectu | Zobrazený jako **číslo**, značí položky na stránku a aktuální stránku. Alternativně lze u „Items per page" použít místo čísla **slovo** |

**Přetečení u pagination nav:** mezi stránkami se objeví **tlačítko s výpustkou**, které značí, že
v jeho menu je hodně stránek. **Carbon doporučuje výpustku nikdy nedávat na začátek ani na konec
posloupnosti stránek.**

**ZDROJ:** Carbon, Pagination usage, Content a Overflow content.
https://carbondesignsystem.com/components/pagination/usage/

## Stavy

Stránkování **nemá vlastní stavy**, dědí je z komponent, které v sobě má:

| Varianta | Vnořené komponenty |
|---|---|
| Pagination | **Select** a **ghost ikonové tlačítko** |
| Pagination nav | **Ghost ikonové tlačítko** a **overflow tlačítko drobenky** |

**ZDROJ:** Carbon, Pagination usage, States.
https://carbondesignsystem.com/components/pagination/usage/

## Klikatelné oblasti

**Pagination má čtyři:** dva selecty (počet položek na stránku, číslo stránky) a dvě ghost ikonová
tlačítka (předchozí, další).

**Pagination nav:** klikatelné je **každé tlačítko**. Dvě ghost ikonová tlačítka na předchozí a další,
zbytek jsou tlačítka jednotlivých stránek.

**ZDROJ:** Carbon, Pagination usage, Clickable areas.
https://carbondesignsystem.com/components/pagination/usage/

## Responzivní chování

| Varianta | Na small breakpointu |
|---|---|
| Pagination | **Selecty se odeberou.** Zůstane informace o celkovém počtu položek, o zobrazovaných položkách a tlačítka předchozí a další |
| Pagination nav | Může nabídnout **tlačítko s výpustkou**, které značí, že v jeho menu je víc stránek |

**ZDROJ:** Carbon, Pagination usage, Responsive behavior.
https://carbondesignsystem.com/components/pagination/usage/

## Modifikátory

| Modifikátor | Co dělá |
|---|---|
| Page looping | U pagination nav: místo zneaktivnění předchozího nebo dalšího tlačítka na prvním či poslední stránce lze zapnout **kontinuální cyklení** dostupnými stránkami |
| Page naming | Místo čísla lze u „Items per page" použít **slovo**, když to lépe odpovídá požadavkům |

**ZDROJ:** Carbon, Pagination usage, Modifiers.
https://carbondesignsystem.com/components/pagination/usage/

## Klávesová obsluha

Tab order zleva doprava. U pagination: select otevře `Space`, `Up` nebo `Down` (šipky zároveň cyklují
hodnoty), vybere `Space` nebo `Enter`, zavře `Esc`. Předchozí a další `Space` nebo `Enter`.
U pagination nav: tlačítka stránek a předchozí či další aktivuje `Space` nebo `Enter`. Overflow výpustku
otevře `Space`, `Up` nebo `Down`.

**Na kraji rozsahu:** když je stránkování na začátku nebo na konci rozsahu, jedno z navigačních tlačítek
se stane neplatným a **přestane být navigovatelné i ovladatelné, jako každý disabled prvek**.

**Labely pro čtečku:** ne všechny prvky stránkování mají statické nebo vizuálně izolované labely. Carbon
konstruuje programový název druhého selectu **spojováním dynamicky generovaného textu na obrazovce**
a dodává přístupné názvy pro ikonová tlačítka („Page", „Previous", „Next").

**ZDROJ:** Carbon, Pagination accessibility.
https://carbondesignsystem.com/components/pagination/accessibility/
Detail: [Klávesnice a focus](../zaklady/klavesnice-a-focus.md)

## Stránkování jako součást tabulky

Z pohledu tabulky je stránkování **volitelná komponenta**, která nechá uživatele navigovat data po
stránkách, když je dat příliš mnoho, aby se zobrazila naráz.

Carbon rozlišuje:

| Typ | Co umí |
|---|---|
| Simple | Značí aktuální stránku a nabízí ovládání na předchozí nebo další |
| Advanced | Navíc možnost změnit počet položek na stránku a skočit na konkrétní číslo stránky |

**ZDROJ:** Carbon, Data table usage, Pagination.
https://carbondesignsystem.com/components/data-table/usage/
Detail: [Datové tabulky](datove-tabulky.md)

---

## Co tahle nota neřeší

- Jak se má chovat výběr řádků při přepnutí stránky, je v [Hromadné akce](../vzory/hromadne-akce.md).
- Infinite scroll. Carbon ho nedokumentuje, v přečtené kopii k němu není nic.
- „Zobrazit více" a „Načíst více" jako alternativy.
  [Přetečení a truncation](../vzory/preteceni-a-truncation.md) a
  [Načítání a čekání](../vzory/nacitani-a-cekani.md).
- Progress bar a progress indicator na lineární cestu.
  [Navigace v hierarchii](navigace-v-hierarchii.md) a [Načítání a čekání](../vzory/nacitani-a-cekani.md).
- Tokeny a rozestupy. Carbon je má na stránce `style`, záměrně je nepřebírám.

## Zdroj

IBM Carbon Design System, Pagination usage a Pagination accessibility, lokální kopie přečtená
30. 7. 2026. https://carbondesignsystem.com/components/pagination/usage/
Carbon u stránkování neuvádí sekci References, žádné externí zdroje k němu nemá. Třída **B**.
