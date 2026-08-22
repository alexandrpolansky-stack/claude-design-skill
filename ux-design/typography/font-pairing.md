# Font pairing

Jak zkombinovat dvě písmové rodiny, aby to vypadalo jako rozhodnutí, ne jako nehoda.

> [!important] Oprava proti původní verzi téhle noty
> Původní verze radila „3-4 fonty na design, u menších 2-3". **To je špatně a jde to proti
> [Anti-slop](../pravidla/anti-slop.md), pravidlu „Víc než dva fonty".** Platí strop **dvě
> rodiny**, a pro většinu projektů stačí jedna se dvěma až třemi řezy. Rozpor byl o to horší, že
> `anti-slop.md` na tuhle notu odkazoval jako na svůj zdroj, takže evidence-classed pravidlo
> citovalo oporu, která tvrdila opak. Opraveno 23. 8. 2026, stejným postupem jako precedens
> gridlines (viz [STATUS.md](../../STATUS.md)).

Související: [Typografie](../pravidla/typografie.md) · [Anti-slop](../pravidla/anti-slop.md) ·
[Serif a Sans Serif](serif-a-sans-serif.md) · [Práce s fontem](prace-s-fontem.md)

---

## Kolik rodin

**Dvě jsou strop.** Když sáhneš po druhé, musí mít jasnou roli (nadpisy vs. text), ne „aby to bylo
pestré". Každá další rodina je další sada rozhodnutí o velikostech, řezech a spacingu, která se musí
udržet konzistentní.

Nepočítá se jako třetí rodina: displejové písmo použité na jediném místě (logotyp, jeden hero
nadpis) a monospace na kód.

Autoritativní znění pravidla je v [Anti-slop](../pravidla/anti-slop.md), sekce „Víc než dva fonty".
Tahle nota řeší, **jak** ty dvě vybrat.

## Na čem párování stojí

**Základ: dost kontrastu mezi rodinami.** Dva podobné fonty vedle sebe vypadají jako chyba
v nastavení, ne jako záměr. Když je rozdíl malý, čtenář ho nepřečte jako hierarchii, ale jako
nekonzistenci.

Kombinace, které fungují:

| Kombinace | Proč funguje |
|---|---|
| **Serif + sans-serif** | Nejspolehlivější pár. Přítomnost a nepřítomnost patek je rozdíl, který se pozná i v malé velikosti |
| **Jedna rodina, kontrastní řezy** | Nejbezpečnější volba vůbec. Rozdíl nese weight a velikost, ne druhá rodina |
| **Lowercase u jednoho, uppercase u druhého** | Kontrast tvaru slova, funguje i uvnitř jedné rodiny |
| **Script + bold sans-serif** | Pro expresivní polohu. Script nese osobnost, sans nese čitelnost |
| **Script + slab serif** | Totéž s tvrdším, méně elegantním výsledkem |

## Kdy párování vůbec neřešit

Když nemáš důvod pro druhou rodinu, nepárujej. Jedna dobře zvolená rodina se škálou velikostí
a dvěma až třemi řezy unese celý produkt a je to výchozí volba, ne ústupek. Druhá rodina je
rozhodnutí, které se platí konzistencí.

---

## Co tahle nota neřeší

- **Kolik fontů je slop a proč.** [Anti-slop](../pravidla/anti-slop.md).
- **Velikosti, délka řádku, line-height, WCAG požadavky.**
  [Typografie](../pravidla/typografie.md), tam jsou tvrdá čísla se třídou důkazu.
- **Který konkrétní řez na co.** [Práce s fontem](prace-s-fontem.md).
- **Kategorie patkových a bezpatkových písem.** [Serif a Sans Serif](serif-a-sans-serif.md).

## Zdroj

Řemeslná praxe, **třída C**. Strop dvou rodin má oporu v [Anti-slop](../pravidla/anti-slop.md),
kde je to pravidlo se třídou a odůvodněním. Zbytek téhle noty je konvence bez měření: kombinace
v tabulce jsou to, co se v praxi drží, ne to, co někdo testoval.

Původní verze noty byla nezdrojovaná poznámka z kurzu a obsahovala chybné doporučení o počtu
rodin. Ukázka „font pairing guide", na kterou odkazovala, v repu není a nikdy nebyla.
