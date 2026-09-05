# Stabilita layoutu při změně dat

Když uživatel zúží filtr, přepne rozsah nebo se data sama obnoví, má se změnit **obsah a nic
jiného**. Otevři při stavbě jakékoli obrazovky, kde jedno ovládání mění sadu záznamů pod sebou.

Související: [Filtrování](filtrovani.md) · [Datové tabulky](../komponenty/datove-tabulky.md) ·
[Přetečení a zkracování](preteceni-a-truncation.md) ·
[Načítání a čekání](nacitani-a-cekani.md) · [Překryvy a vrstvení](prekryvy-a-vrstveni.md)

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
| Procenta **plus** `min-width` ze součtu podlah | Nad podlahou rostou všechny sloupce ve stejném poměru, na podlaze má každý přesně na svou nejdelší hodnotu | Podlahu je nutné **změřit**, ne odhadnout, a přeměřit po každé změně typografie |

Volba mezi prvními dvěma závisí na tom, jestli tabulka obsahuje atomické hodnoty, které nesmí být
rozlomené ani zkrácené. Když ano, vyhrávají pixely: vodorovný scroll je poctivá odpověď, rozpůlené
číslo není. Viz [Přetečení a zkracování](preteceni-a-truncation.md).

**Třetí řádek tu volbu ruší** a je popsaný v sekci níž. Stojí za pozornost, že cena, kterou platí,
není vizuální, ale procesní: přesune se z rozhodování do měření.

## Procenta s podlahou: když má tabulka růst i nezkracovat

**PRAVIDLO:** Dej každému sloupci procento se součtem 100 % a tabulce `min-width` rovnou součtu
změřených podlah. Procento sloupce **je** jeho podlaha dělená tím součtem, ne odhad. Pod podlahou
scrolluje obal tabulky, nad ní se přebytek dělí v poměru podlah.
**KDY PLATÍ:** Fixní layout, pět a víc sloupců, většina s tvarem, a požadavek, aby se tabulka
roztáhla do šířky monitoru.
**PROČ:** Procenta zkracují v úzkém okně jen proto, že se šířka sloupce může dostat pod jeho
nejdelší hodnotu. `min-width` je přesně to místo, kde se to zakáže, takže cena prvního řádku
tabulky výš zmizí. Cena druhého řádku zmizí taky: nechat jediný sloupec bez šířky znamená, že
spolkne celý přebytek sám, protože to specifikace fixního layoutu takhle předepisuje. S procenty
roste každý sloupec.
**TŘÍDA:** **A** pro mechanismus (specifikace), **C** pro tu kombinaci: ověřeno měřením na jedné
produktové aplikaci (tři tabulky, 5. 9. 2026), ne studií.
**ZDROJ:** W3C, CSS 2.2, 17.5.2.1 Fixed table layout, verbatim: „Any remaining columns equally
divide the remaining horizontal table space (minus borders or cell spacing)." a „If the table is
wider than the columns, the extra space should be distributed over the columns."
https://www.w3.org/TR/CSS22/tables.html

## Stejné podíly: když se všechny podlahy nevejdou

**PRAVIDLO:** Dej každému sloupci `100 / n` procent a hodnotu, která se do svého podílu nevejde,
nech zkrátit výpustkou s celou hodnotou v `title`. Žádné ruční dolaďování po sloupcích.
**KDY PLATÍ:** Když součet změřených podlah přesahuje šířku, kterou tabulka reálně dostane, nebo
když je pravidelná mřížka sloupců cennější než to, aby každá hodnota byla vidět celá.
**PROČ:** Je to aritmetika, ne vkus. `n` stejných sloupců, které uživí nejširší podlahu,
potřebuje `n × podlaha_max`. Když je to víc než nabízená šířka, **stejné sloupce a nezkrácené
hodnoty nejde mít obojí**. Naměřený případ: osm sloupců, nejširší podlaha 162px, potřeba
8 × 162 = 1296px, a karta na 1440px monitoru dostala 1126. Předchozí pravidlo (procenta z podlah)
v té situaci nezkracuje nic, ale sloupce jsou pak 85 až 202px široké a mezera za popiskem
hlavičky, což je šířka sloupce minus délka popisku, kolísá mezi 57 a 140px. To si přesně
všimne designér a přečte to jako rozbitý spacing.
**CENA A JAK JI UNÉST:** Zkrácená hodnota musí nést celou hodnotu v tooltipu, jinak je to ztráta
dat a ne zkrácení, viz [Přetečení a zkracování](preteceni-a-truncation.md). Zkrácený
**identifikátor** je zvlášť drahý: dvě různá čísla pak vypadají stejně. Než na to přistoupíš,
zkontroluj, jestli se ten identifikátor nedá zkrátit u zdroje (konstantní prefix na každém řádku
nenese žádnou informaci).
**A CO NEDĚLAT:** Neřeš to délkou popisku. Prodloužit „ID" na „Request ID", aby se mezera zaplnila,
je stejný výsledek z opačného konce a rozpadne se to při prvním dalším sloupci. Popisek se mění
tehdy, když je nepřesný, ne když je krátký.
**TŘÍDA:** **A** pro mechanismus (procento sloupce je relativní k šířce tabulky, specifikace),
**C** pro to rozhodnutí: ověřeno měřením na jedné produktové aplikaci (tři tabulky, 6. 9. 2026).
**ZDROJ:** W3C, CSS 2.2, 17.5.2.1 Fixed table layout, verbatim: „A percentage value for a column
width is relative to the table width." https://www.w3.org/TR/CSS22/tables.html

## Podlahu změř, nespočítej z počtu znaků

**PRAVIDLO:** Podlahu sloupce zjisti tak, že jeho **nejdelší reálnou hodnotu vykreslíš do živé
buňky té tabulky** a přečteš její box. Přičti žlaby. Za obsah počítej i **hlavičku**, protože
v úzkých sloupcích bývá širší než data.
**KDY PLATÍ:** Vždy, když deklaruješ šířku sloupce nebo jeho podlahu.
**PROČ:** Šířka řetězce v proporcionálním písmu není funkce počtu znaků. Odhad selhal opakovaně
v jednom směru: sedmnáctiznakový identifikátor odhadnutý na 124px renderoval 139 a s `nowrap`
přetekl do sousedního sloupce. Měření té samé hodnoty v té samé buňce je jediná odpověď, která
přežije změnu velikosti písma, prostrkání nebo řezu.
**TŘÍDA:** C (řemeslná praxe, ověřená měřením)

**Past, na kterou nic neupozorní:** hlavička může být širší než nejdelší hodnota ve sloupci.
Verzálkový `Environment` se sortovacím tlačítkem renderuje 98px, zatímco nejdelší hodnota pod ním
je 52px. Když je sloupec deklarovaný podle dat, text hlavičky vyteče ven a **položí se na sousední
hlavičku**. Nic to nenahlásí: viditelně přetečená hlavička nescrolluje a neořízne se, takže
kontrola na scroll ani na `scrollWidth` ji nechytí. Chytne ji jen porovnání šířky textu hlavičky
proti šířce sloupce, nebo oko.

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
6. U každého sloupce porovnat šířku textu hlavičky se šířkou sloupce. Vyteklá hlavička se
   nenahlásí sama.
7. Po jakékoli změně typografie řádku podlahy **přeměřit**. Velikost, řez i prostrkání mění
   šířku řetězce, takže stará podlaha je od té chvíle číslo o něčem jiném.
8. Změřit mezery mezi popisky hlavičky, ne jen šířky sloupců. Mezera je šířka sloupce minus
   délka popisku, takže kolísá i v tabulce, kde je každý sloupec sám o sobě správně, a je to
   ta nepravidelnost, které si člověk všimne první.
9. Porovnat, kde začíná první sloupec a kde titulek karty nad ním. Vnější okraj patří kartě,
   vnitřní žlab tabulce; když se ty dvě hodnoty liší o 8px, čte se to jako posunutá tabulka.
10. Zkontrolovat, že hlavička je zarovnaná stejně jako hodnoty pod ní. Sloupec zarovnaný
    doprava mezi dvěma doleva rozdělí prázdno velmi nerovnoměrně; peníze patří na konec řádku.

## Co tahle nota neřeší

- Kam patří stav ovládání, které změnu vyvolalo, aby přežil sdílení odkazem a tlačítko zpět, je v [Stav pohledu v URL](stav-pohledu-v-url.md).
- Kdy vůbec ukázat skeleton a kdy spinner. To je [Načítání a čekání](nacitani-a-cekani.md).
  Souvisí ale přímo: skeleton, který nahradí celou stránku při každém obnovení, je největší možný
  posun layoutu.
- Umístění a chování filtrů jako takových. [Filtrování](filtrovani.md).
- Kde se smí zkracovat. [Přetečení a zkracování](preteceni-a-truncation.md).

## Zdroj

Vlastní syntéza z produktové praxe, **třída C**, s jednou výjimkou: mechanismus fixního layoutu
tabulky je citovaný ze specifikace (**A**), viz sekci o procentech s podlahou. Carbon tenhle
problém nepojmenovává; jeho věta o šířkách sloupců (`Data table, Style`) popisuje jedno
vykreslení, ne dvě po sobě. Souvislost
s Cumulative Layout Shift je z Web Vitals, kde je posun obsahu, který uživatel nevyvolal, přímo
měřenou metrikou: https://web.dev/articles/cls
