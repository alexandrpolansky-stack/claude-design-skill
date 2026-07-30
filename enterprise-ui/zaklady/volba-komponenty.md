# Volba komponenty: od úkolu k prvku

Rozhodovací tabulky pro nejčastější situaci v enterprise UI: vím, co má uživatel udělat, a musím
vybrat prvek. Otevři, když váháš mezi dvěma podobnými komponentami. Každý řádek říká, čím se ty dvě
liší, ne jak vypadají.

Související: [Vrstvy enterprise UI](vrstvy-a-vzory.md) ·
[Výběr ze seznamu](../komponenty/vyber-ze-seznamu.md) ·
[Datové tabulky](../komponenty/datove-tabulky.md) · [Dialogy a panely](../vzory/dialogy-a-panely.md)

---

## Uživatel má něco zadat

| Vstup | Komponenta | Rozhodující znak |
|---|---|---|
| Krátký volný text (jméno, telefon, adresa) | Text input | Hodnotu nelze předvídat výčtem |
| Víc řádků (komentář, popis, žádost) | Text area | Očekává se víc než pár slov |
| Tajná hodnota (heslo, PIN, číslo karty) | Password input | Znaky se musí skrýt, s možností odkrytí |
| Číslo s krokem (počet, kvóta, limit) | Number input | Inkrement má význam |
| Číslo z rozsahu (procenta, hlasitost) | Slider | Uživateli stačí přibližná hodnota a chce ji vidět v kontextu rozsahu |
| Datum, čas, rozsah dat | Date picker / time picker | Formát je zdroj chyb, komponenta ho vynutí |
| Soubor | File uploader | |

Vstupy s omezeným rozsahem (number, slider, date, time) Carbon nazývá *bound entry controls*:
nedovolí zadat neplatnou hodnotu, takže u nich nepotřebuješ validaci formátu.
Zdroj: https://carbondesignsystem.com/patterns/forms-pattern/

## Uživatel má vybrat z možností

Rozhoduje **počet možností** a **kolik jich smí vybrat**.

| Počet možností | Vybírá jednu | Vybírá víc |
|---|---|---|
| 2 | Radio button (nebo toggle, když je to zapnuto/vypnuto a platí okamžitě) | Checkbox |
| 3 až 5 | Radio button, všechny vidět najednou | Checkbox, svisle pod sebou |
| 6 a víc | Dropdown nebo select | Multiselect |
| Dlouhý nebo neznámý seznam (z databáze) | Combo box (píše a filtruje, může zadat vlastní hodnotu) | Filterable multiselect |

**Tvrdá pravidla z Carbonu:**

- Dvě možnosti nikdy nedávej do dropdownu, dej radio buttony.
  Zdroj: https://carbondesignsystem.com/components/dropdown/usage/
- Pod tři možnosti nedávej ani nativní select.
  Zdroj: https://carbondesignsystem.com/components/select/usage/
- Nad pět možností nepoužívej checkboxy ani radio buttony, přejdi na seznamovou komponentu.
  Zdroj: https://carbondesignsystem.com/patterns/forms-pattern/
- Dropdowny nikdy nevnořuj do sebe.
  Zdroj: https://carbondesignsystem.com/components/dropdown/usage/

Detail rozdílu select versus dropdown versus combo box, včetně toho, kdy se vyplatí nativní prvek:
[Výběr ze seznamu](../komponenty/vyber-ze-seznamu.md).

### Toggle versus checkbox

**PRAVIDLO:** Toggle použij, když se změna aplikuje okamžitě bez potvrzení. Checkbox použij, když
je to jeden vstup ve větším formuláři, který se potvrzuje odesláním.
**KDY PLATÍ:** Nastavení, preference, oprávnění.
**PROČ:** Toggle slibuje okamžitý efekt. Když toggle vyžaduje ještě „Uložit", uživatel neví, jestli
se změna už stala. Zároveň toggle musí být popsaný slovem ovlivněné vlastnosti, protože barva sama
stav nesmí nést.
**TŘÍDA:** B
**ZDROJ:** Carbon, checkbox versus toggle: „Toggle switches are preferred when the resulting action
will be instantaneously applied, without the need for further confirmation."
https://carbondesignsystem.com/components/checkbox/usage/
**KDY NEPLATÍ:** Jediná binární volba stojící mimo formulář, kde je obojí přijatelné.

## Uživatel má vidět víc záznamů

| Situace | Komponenta |
|---|---|
| Data ve sloupcích, potřeba řazení, výběru řádků, dávkových akcí | Data table |
| Jednoduchý seznam párů (termín a definice, vlastnost a hodnota), bez řazení | Structured list |
| Jedna volba z několika strukturovaných variant (tarify, plány) | Selectable structured list nebo selectable tile |
| Málo položek v úzkém prostoru (panel, karta) | Contained list |
| Vizuálně bohatý obsah s obrázkem, nadpisem a akcí | Tile nebo karta |

**Rozhodující znak tabulka versus seznam:** tabulka je pro data, která mají sloupce a mezi kterými
uživatel porovnává. Structured list je pro čtení, ne pro porovnávání, a nesnese vnořování.
Carbon k tomu říká, že složitější obsah patří do tabulky, protože ta vnořování podporuje.
Zdroj: https://carbondesignsystem.com/components/structured-list/usage/

**Tabulka není tabulkový procesor.** Carbon explicitně uvádí, že datová tabulka není náhrada
spreadsheetu a nemá se používat, když je potřeba složitější zobrazení nebo interakce.
Zdroj: https://carbondesignsystem.com/components/data-table/usage/

## Uživatel má přepnout obsah nebo projít krok za krokem

| Situace | Komponenta | Proč ne to druhé |
|---|---|---|
| Skupiny souvisejícího obsahu ve stejném kontextu | Tabs | |
| Dvě až tři formy toho samého obsahu (graf/tabulka, den/týden) | Content switcher | Tabs jsou hierarchicky výš, content switcher se používá dovnitř tabu |
| Lineární proces s pořadím a validací kroků | Progress indicator | Tabs nepodporují postupný úkol a nedají znát pořadí |
| Uživatel musí obsah dvou skupin porovnávat | Ani jedno, zobraz vedle sebe | Přepínání nutí klikat tam a zpět |
| Kde jsem v hierarchii stránek | Breadcrumb | Progress indicator značí postup v úkonu, ne pozici v IA |

Zdroj: https://carbondesignsystem.com/components/tabs/usage/ ·
https://carbondesignsystem.com/components/breadcrumb/usage/
Detail: [Taby](../komponenty/taby.md) · [Navigace v hierarchii](../komponenty/navigace-v-hierarchii.md)

## Systém potřebuje něco sdělit

Rozhoduje **kdo to vyvolal** a **jak moc to smí přerušit**.

| Situace | Prvek |
|---|---|
| Reakce na akci uživatele v místě, kde pracuje | Inline notifikace |
| Systémová událost bez vazby na místo na stránce | Toast |
| Nutná odpověď, bez které nelze pokračovat | Modal |
| Informace, která má být vidět před akcí, natrvalo | Callout |
| Celoproduktová zpráva (odstávka, expirace) | Banner |
| Kontextové vysvětlení termínu nebo ikony, jen text | Tooltip |
| Kontextový obsah s odkazem nebo tlačítkem | Toggletip |
| Trvale potřebná instrukce k poli | Helper text pod polem, nikdy tooltip |

**Nejčastější chyba:** modal jako notifikace. Modal je pro kritickou informaci vyžadující akci.
Pro nekritickou zpětnou vazbu je to toast nebo inline notifikace.
Zdroj: https://carbondesignsystem.com/components/modal/usage/
Detail: [Notifikace](../vzory/notifikace.md) · [Tooltip a toggletip](../komponenty/tooltip-a-toggletip.md)

## Uživatel má něco potvrdit nebo zadat mimo hlavní tok

| Situace | Prvek |
|---|---|
| Krátký úkol, méně než pět vstupů, uživatel nepotřebuje nic z pozadí | Modal |
| Víc než pět vstupů, nebo uživatel potřebuje vidět data pod tím | Side panel |
| Komplexní nebo dlouhý úkol, víc rozhodnutí | Samostatná stránka |
| Volitelný úkol paralelně s prací na stránce (najít a nahradit) | Nemodální dialog |

Zdroj: https://carbondesignsystem.com/patterns/forms-pattern/ ·
https://carbondesignsystem.com/patterns/dialog-pattern/
Detail: [Dialogy a panely](../vzory/dialogy-a-panely.md)

## Uživatel čeká

| Délka a typ | Prvek |
|---|---|
| Pod 1 s | Nic |
| Krátká akce jednoho prvku (uložení, ověření) | Inline loading u tlačítka nebo prvku |
| Nad 3 s, celá stránka nebo sekce | Loading indikátor s overlayem |
| První načtení obsahu, jehož tvar znáš | Skeleton, s výhradou níže |
| Postup lze vyčíslit (download, upload, dávka) | Determinovaný progress bar |
| Postup vyčíslit nelze, ale běží dlouho | Nedeterminovaný progress bar |
| Krokovaný proces s akcí uživatele mezi kroky | Progress indicator, nikoliv progress bar |

Prahy 0,1 / 1 / 10 s a spor o skeleton screeny řeší
[Formuláře a stavy](../../ux-design/pravidla/formulare-a-stavy.md), sekce Loading stavy. Tam je
i doložený nález **proti** skeletonům, který jde proti Carbonu. Než skeleton použiješ, přečti to.
Detail: [Načítání a čekání](../vzory/nacitani-a-cekani.md)

## Uživatel má zúžit množinu dat

| Situace | Prvek |
|---|---|
| Zná klíčové slovo | Search |
| Zná kritérium z předem daného výčtu | Filtr |
| Obojí | Search plus filtr, výsledek se počítá dohromady |
| Vybírá z jedné kategorie, výsledek přijde hned | Filtr s okamžitou aplikací |
| Vybírá z víc kategorií nebo je dotaz drahý | Filtr s dávkovým „Použít filtry" |

Zdroj: https://carbondesignsystem.com/patterns/filtering/ ·
https://carbondesignsystem.com/patterns/search-pattern/
Detail: [Filtrování](../vzory/filtrovani.md) · [Hledání](../vzory/hledani.md)

---

## Co tahle nota neřeší

- Vizuální podobu vybraného prvku. To je v příslušné notě v [`komponenty/`](../komponenty/).
- Tvrdá pravidla velikosti a kontrastu terče. To je
  [tlačítka](../../ux-design/pravidla/tlacitka.md) a
  [kontrast a barva](../../ux-design/pravidla/kontrast-a-barva.md), s třídou A.
- Komponenty, které Carbon nemá dokumentované v přečtené kopii (accordion, overflow menu, content
  switcher, UI shell). Zmiňuju je v rozhodování, ale nemám k nim detailní podklad.

## Zdroj

Destilát rozhodovacích tabulek z dokumentace IBM Carbon Design System, lokální kopie přečtená
30. 7. 2026. Kanonický zdroj: https://carbondesignsystem.com/. Přepsáno vlastními slovy, tokeny
a vizuální hodnoty vynechané záměrně, viz [Vrstvy enterprise UI](vrstvy-a-vzory.md).
Třída **B** (publikovaná konvence design systému), pokud u jednotlivého pravidla není uvedeno jinak.
