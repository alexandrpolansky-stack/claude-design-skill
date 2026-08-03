# Stabilita layoutu při změně dat

Když uživatel zúží filtr, přepne rozsah nebo se data sama obnoví, má se změnit **obsah a nic
jiného**. Otevři při stavbě jakékoli obrazovky, kde jedno ovládání mění sadu záznamů pod sebou.

Související: [Filtrování](filtrovani.md) · [Datové tabulky](../komponenty/datove-tabulky.md) ·
[Přetečení a zkracování](preteceni-a-truncation.md) ·
[Načítání a čekání](nacitani-a-cekani.md)

---

## Rychlé rozhodnutí

1. Tabulka, jejíž sadu řádků mění filtr = **deklaruj šířky sloupců**. Automatický layout je měří
   z právě načtených řádků, takže s každou změnou filtru dostane uživatel jinou mřížku.
2. Nech **bez šířky právě jeden sloupec**, ten s nejméně předvídatelným obsahem. Zbytek prostoru
   připadne jemu.
3. Číslo, které se mění (počet u filtru, hodnota v KPI), potřebuje **tabulární číslice i rezervu na
   počet číslic**. Tabulární číslice řeší tvar, ne délku.
4. Text, který se mění s volbou (podnadpis, popisek rozsahu), drž **stejně dlouhý**. Když jedna
   varianta zalomí na druhý řádek a jiná ne, posune se celá stránka.
5. Ovládání, které tu změnu vyvolává, patří **nad všechno, co mění**. Jinak se pohne dřív, než
   uživatel pustí tlačítko.
6. Prvek, který se objevuje a mizí podle dat, umísti tak, aby rostl **do volného prostoru**, ne do
   sousedů.

---

## Proč to není kosmetika

Uživatel klikne na jednu věc a čeká jednu změnu. Když se při tom přeskládá mřížka, musí celou
obrazovku znovu přečíst, aby zjistil, jestli se změnilo i něco, o co nežádal. U tabulky, kterou
člověk prochází očima shora dolů, to znamená ztratit místo, kde byl.

Je to zároveň měřitelná vada, ne jen dojem: pohyb obsahu, který uživatel nevyvolal, je přesně to, co
měří Cumulative Layout Shift.

**TŘÍDA:** C (vlastní syntéza z praxe, Carbon tenhle problém nikde nepojmenovává)

## Tabulka: automatický layout je funkce dat

**PRAVIDLO:** Jakmile se sada řádků v tabulce mění za běhu, deklaruj šířky sloupců a přepni tabulku
na fixní layout. Nech bez šířky jediný sloupec, ten s nejméně předvídatelným obsahem, aby pobral
zbývající místo.
**KDY PLATÍ:** Tabulka s filtrem, přepínačem rozsahu, stránkováním nebo automatickým obnovováním.
**PROČ:** Automatický layout měří šířku sloupce z buněk, které v něm právě jsou. Tři řádky a padesát
řádků jsou dvě různé sady, takže je to i dvakrát jiná mřížka. Uživatel přepnul rozsah a dostal
posun všech sloupců.
**TŘÍDA:** C

Carbon k šířkám říká jen tolik, že se **může lišit podle obsahu** a že se vyžaduje minimální mezera
mezi sloupci (viz [Datové tabulky](../komponenty/datove-tabulky.md)). To je pravda o jednom
vykreslení. O tom, co se stane při druhém, nic neříká.

**Které sloupce mají tvar:** identifikátor v pevném formátu, datum, částka, odznak stavu. Ty
deklaruj. Uživatelem psaný název, popis nebo důvod tvar nemá; ten nech bez šířky.

### Pixely, nebo procenta

Rozhodnutí, které se dělá jednou a pak se s ním žije:

| | Chování | Cena |
|---|---|---|
| Procenta se součtem 100 % | Tabulka se vždy vejde, nikdy nescrolluje vodorovně | V úzkém okně dostane každý sloupec málo, takže se **zkracuje i to, co se zkracovat nemá** (identifikátor, datum) |
| Pixely plus `min-width` na tabulce | Sloupec má vždy dost místa na svou nejdelší reálnou hodnotu | Pod tou šířkou tabulka **scrolluje vodorovně** |

Volba závisí na tom, jestli tabulka obsahuje atomické hodnoty, které nesmí být rozlomené ani
zkrácené. Když ano, vyhrávají pixely: vodorovný scroll je poctivá odpověď, rozpůlené číslo není.
Viz [Přetečení a zkracování](preteceni-a-truncation.md).

## Číslo se mění a bere s sebou šířku

**PRAVIDLO:** U čísla, které se mění za běhu, nastav tabulární číslice **a** rezervuj šířku na
očekávaný počet číslic.
**KDY PLATÍ:** Počty u filtračních chipů, hodnoty v KPI pásu, čítače v záhlaví.
**PROČ:** Tabulární číslice zaručí, že `1` je stejně široká jako `4`. Nezaručí, že `19` je stejně
široké jako `9`. V zalamovací řadě chipů se ta ztráta jednoho znaku násobí počtem chipů, a řada se
přelomí o řádek dřív nebo později. Filtrační pruh o řádek naroste a všechno pod ním poskočí, jako
odpověď na stisk něčeho nad ním.
**TŘÍDA:** C

Rezervu volí podle řádu, který data reálně dosahují, ne podle teoretického maxima. Tři číslice
pokryjí většinu produktových počtů a stojí pár pixelů.

## Text, který se mění s volbou

**PRAVIDLO:** Varianty jedné věty (podnadpis závislý na režimu, popisek rozsahu) drž na podobné
délce.
**KDY PLATÍ:** Kdykoli jeden prvek ukazuje jiný text podle volby uživatele.
**PROČ:** Rozdíl pěti slov je neviditelný, dokud jedna varianta nezalomí na druhý řádek. Pak se
o výšku řádku posune všechno pod ní, a to při každém přepnutí tam i zpět.
**TŘÍDA:** C

## Kam patří ovládání

**PRAVIDLO:** Přepínač, který mění rozsah celé obrazovky, patří **nad** všechno, co mění. Filtr,
který mění jen řádky, patří k řádkům.
**KDY PLATÍ:** Vždy, když jedno ovládání ovlivňuje víc než jednu oblast.
**PROČ:** Dvě věci najednou. Ovládání nad měněnou oblastí se samo nikdy neposune, takže zůstane pod
kurzorem i po překreslení. A pořadí shora dolů čte uživatel jako příčinu a následek: přepínač pod
čísly, která přepočítává, tvrdí, že čísla byla dřív.
**TŘÍDA:** C

## Prvek, který se objevuje a mizí

**PRAVIDLO:** Když se podle dat objevuje odznak, plaketa nebo hláška, umísti ji tak, aby rostla do
volného prostoru, ne do sousedních prvků.
**KDY PLATÍ:** Počítadla a stavové plakety v hlavičce, vedle akčních tlačítek.
**PROČ:** Skupina zarovnaná na pravý okraj roste doleva a tlačítka v ní zůstanou stát. Ta samá
skupina zarovnaná vlevo posune všechno za sebou. Je to rozdíl jedné vlastnosti a uživatel ho pozná
tak, že mine tlačítko.
**TŘÍDA:** C

---

## Kontrolní seznam

1. Přepni filtr tam a zpět. Pohnul se nějaký sloupec?
2. Přepni na sadu s jiným řádem počtu (jednotky proti stovkám). Přelomila se řada filtrů?
3. Projdi všechny varianty textu, který se mění s volbou. Zalomí některá o řádek víc?
4. Nech obrazovku obnovit se stejnými daty. Hnulo se cokoliv? Nemělo.
5. Zúžit okno na nejmenší podporovanou šířku a zopakovat body 1 a 2.

## Co tahle nota neřeší

- Kdy vůbec ukázat skeleton a kdy spinner. To je [Načítání a čekání](nacitani-a-cekani.md).
  Souvisí ale přímo: skeleton, který nahradí celou stránku při každém obnovení, je největší možný
  posun layoutu.
- Umístění a chování filtrů jako takových. [Filtrování](filtrovani.md).
- Kde se smí zkracovat. [Přetečení a zkracování](preteceni-a-truncation.md).

## Zdroj

Vlastní syntéza z produktové praxe, **třída C**. Carbon tenhle problém nepojmenovává; jeho věta
o šířkách sloupců (`Data table, Style`) popisuje jedno vykreslení, ne dvě po sobě. Souvislost
s Cumulative Layout Shift je z Web Vitals, kde je posun obsahu, který uživatel nevyvolal, přímo
měřenou metrikou: https://web.dev/articles/cls
