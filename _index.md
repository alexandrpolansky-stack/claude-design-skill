# Knihovna designové znalosti (MOC)

Vstupní bod do celé knihovny. Princip: tahle mapa je levný index, ze kterého se vytáhne jen
relevantní nota. Nenačítat všechno.

Značky u not:

| Značka | Význam |
|---|---|
| **[stub]** | nota je zatím kostra, hodí se doplnit |
| **[archiv]** | studijní materiál z původního vaultu nebo téma mimo rozsah knihovny. **Při návrhu sem nesahej**, je to tu jako záznam, ne jako opora |

**Tři vrstvy důvěryhodnosti.** Když si dvě noty odporují, **vyhrává vyšší vrstva**. Žádná sekce
nestojí mimo tuhle tabulku.

| Vrstva | Kde | Co to znamená |
|---|---|---|
| 1. Evidence | `ux-design/pravidla/`, `ux-design/kontext/` | Každé pravidlo má **třídu důkazu** a zdroj. Přebíjí všechno ostatní. |
| 2. Konvence | `enterprise-ui/` | Publikovaná konvence design systému (IBM Carbon), třída B. Ustupuje vrstvě 1, přebíjí vrstvu 3. |
| 3. Import | zbytek `ux-design/`, celý `neuro-design/`, `web-dev/` | Studijní poznámky z původního vaultu, **bez třídy důkazu**. Použitelný materiál, nikdy argument proti vrstvě 1 nebo 2. |

`sheets/` stojí vedle škály: jsou to domácí pravidla pro konkrétní výstup a pro Sheets platí
přednostně, včetně míst, kde jdou proti obecnému výzkumu (viz override blok o gridlines).

**Pozor na `neuro-design/`.** Doporučuje se jako první čtení u větší stavby a je to jediné místo
v knihovně s explicitní metodikou vizuální hierarchie (váhy prvků, focal point, vzorec pro
whitespace). Přitom je ve vrstvě 3: nemá u tvrzení zdroje a na dvou místech opakuje vyvrácené
tvrzení. **Ber z něj metodiku, ne čísla.**

Rozpor mezi vrstvami se řešil už třikrát (gridlines, počet fontů, Millerova sedmička) a pokaždé
to stálo měsíce špatné rady, takže to není teorie. Detail v [STATUS.md](STATUS.md).

Stav a mezery: [STATUS.md](STATUS.md).

## Sekce

| Sekce | Not | O čem |
|---|---|---|
| [neuro-design/](neuro-design/) | 1 | Kognitivní ergonomie, eye-tracking, algoritmy vizuální váhy. Nejhutnější dokument v knihovně. |
| [ux-design/](ux-design/) | 51 | UX zákony, proces, barvy, typografie, layout, trendy, etika, hotový design systém, evidence-based pravidla, kontext podle sektoru. |
| [enterprise-ui/](enterprise-ui/) | 30 | Produktové aplikace: volba komponenty podle úkolu, vzory (prázdné stavy, notifikace, filtrování), komponenty (tabulky, formulářové prvky, taby), klávesnice a čtečky. Principy z IBM Carbonu, bez jeho vizuálu. |
| [web-dev/](web-dev/) | 4 | HTML/CSS základy, vkládání CSS, stylizace textu, práce s obrázky. |
| [sheets/](sheets/) | 3 | Google Sheets reporty: rozhodovací rámec, brand tokeny, Apps Script vrstva. |

---

## Neuro-design (začni tady u větší stavby)

- [Neuro-design master document](neuro-design/neuro-design-master.md) - kognitivní ergonomie a architektura datových rozhraní. Pět modulů: biologie vizuální percepce (F/Z-pattern, kognitivní zátěž), matematika mřížek a Gestalt, algoritmy sémantického škálování (výpočet vizuální váhy prvku), persuasive design a vedení pozornosti, diagnostika chyb a fail-safe protokoly. Psané přímo jako instrukční rámec pro generování a evaluaci UI.

## UX základy

- [GENERAL UX KNOWLEDGE](ux-design/ux-zaklady/general-ux-knowledge.md) - Don Norman, afordance, viditelnost, zpětná vazba, mapování, role v UX týmu, tech terminologie.
- [Design Research Methods](ux-design/ux-zaklady/design-research-methods.md) - metody UX výzkumu.
- [Content strategy a UX writing](ux-design/ux-zaklady/content-strategy-ux-writing.md) - think like an editor, obsahová strategie.
- [Define the problem](ux-design/ux-zaklady/define-the-problem.md) - definice problému před návrhem řešení.
- [Design Process](ux-design/ux-zaklady/design-process.md) - celkový designový proces.
- [Understand who your users are](ux-design/ux-zaklady/understand-your-users.md) - kdo jsou uživatelé, persony.
- [Discovery](ux-design/ux-zaklady/discovery.md) - fáze objevování problému a kontextu.
- [Etika v UX](ux-design/ux-zaklady/etika-v-ux.md) - etika, dark patterns naopak.
- [UX experience](ux-design/ux-zaklady/ux-experience.md) - dva vlastní zápisky o špatném UX, ilustrace, ne pravidla. **[archiv]**

## Zákony a principy (teorie a původ, ne návod ke stavbě)

- [UX Laws](ux-design/zakony-principy/ux-laws.md) - co který zákon říká a odkud pochází: Fitts, Hick, Jakob, Miller, Tesler, Postel, Parkinson, Gestalt. **Návrh jimi nezdůvodňuj:** populární verze Fittse, Hicka i Millera je vyvrácená (větší tlačítko není míň chyb, kratší menu není rychlejší rozhodnutí, 7±2 neplatí) a u každého je v notě opravný callout.
- [Osmibodová mřížka](ux-design/zakony-principy/osmibodova-mrizka.md) - 8pt grid pro konzistentní spacing.
- [Efekty](ux-design/zakony-principy/efekty.md) - kognitivní efekty v UX.
- [Principy a Pravidla](ux-design/zakony-principy/principy-a-pravidla.md) - návrhové principy a pravidla.

## Pravidla (evidence-based, s třídou důkazu)

Vzniklo z fáze 2 projektu design-rule-system (29. 7. 2026). Každé pravidlo má šest povinných
částí: PRAVIDLO, KDY PLATÍ, PROČ, TŘÍDA (A tvrdá opora / B publikovaná konvence nebo regulace /
C řemeslná praxe), ZDROJ, KDY NEPLATÍ. Otevři, když stavíš konkrétní komponentu a chceš vědět,
proč zrovna tahle hodnota, ne jiná.

- [Tlačítka](ux-design/pravidla/tlacitka.md) - kolik primárních tlačítek, jak přiřadit variantu, pět stavů, focus ring, destruktivní akce a tvrdé mantinely velikosti (Fitts, SMALLER-OF model, WCAG 2.5.8).
- [Tvar a radius](ux-design/pravidla/tvar-a-radius.md) - border-radius: Material 3 škála jako výchozí systém, optická kulatost vnořených prvků, a forenzní důkaz, že „zaoblené je klikatelnější" je nepodložený folklór (NHS commit bez citace).
- [Stroke a hranice](ux-design/pravidla/stroke-a-hranice.md) - kdy border vs. stín vs. whitespace, WCAG 3:1 pro viditelnost hranic komponent, 1px oddělovače, focus ring na zaoblených prvcích.
- [Hloubka a stíny](ux-design/pravidla/hloubka-a-stiny.md) - kdy hloubku nést barvou plochy a kdy stínem, ověřené elevation škály (Carbon, Material 3), proč stín nikdy nesmí nést hranici ovládacího prvku.
- [Pohyb](ux-design/pravidla/pohyb.md) - jak dlouho má trvat přechod, kterou vlastnost animovat, jak rychle točit spinner (vztah k vnímanému čekání je konvexní, ne lineární: Ding & Kyung 2025, N≈7000), přerušitelnost, prefers-reduced-motion, WCAG 2.2.2/2.3.3. **Neřeší** animace spouštěné scrollem.
- [Kontrast a barva](ux-design/pravidla/kontrast-a-barva.md) - proč 4,5:1 je regulatorní baseline, ne percepční práh (a proč má slabší evidenci než aesthetic-usability effect), WCAG 1.4.11, USWDS magic number, sémantika stavů.
- [Typografie](ux-design/pravidla/typografie.md) - délka řádku 45-75 znaků, WCAG text spacing a resize 200 %, škála jako nástroj konzistence, proč Miller/Cowan neplatí na hierarchii nadpisů.
- [Formuláře a stavy](ux-design/pravidla/formulare-a-stavy.md) - **nejakčnější nota v sekci.** Label vs. placeholder, kdy validovat (výchozí: až při odeslání), text chybové hlášky, vícekrokový formulář a onboarding wizard, tři prahy čekání a který indikátor při jaké délce, krok kontroly před nevratnou akcí (WCAG 3.3.4), prázdné a chybové stavy. Proti skeleton screenům má měření, ne jen pochybnost. **Cowanovo 3-5 se tu netýká počtu kroků**, ale informace, kterou si uživatel musí nést mezi nimi.
- [Anti-slop](ux-design/pravidla/anti-slop.md) - markery generického vzhledu s třídou důkazu, včetně naměřeného nálezu, že bezokrajové flat UI stojí uživatele o 22 % víc času (NN/g, Moran 2017).
- [Vizuální craft](ux-design/pravidla/vizualni-craft.md) - vrstva art direction, kterou zbytek `pravidla/` neřeší: kdy pojmenovat klasický vs. expresivní pól, proč zdrženlivost není nulová osobnost, jak rozvíjet craft úsudek a párovat typografické hlasy (Hobday, Kowalski, + 3 živě ověřené Awwwards příklady, třída C).
- [Portfolio a work grid](ux-design/pravidla/portfolio-a-work-grid.md) - hierarchie dlaždic v portfolio gridu (vlajková dlaždice, smíšený obsah) a barva celé sekce jako wayfinding, ze 3 živě ověřených Awwwards nominací (třída C).

## Kontext a sektor (proč web pro úřad nevypadá jako web pro zubaře)

Osm sektorů, každý s vlastní tabulkou parametr → hodnota → třída důkazu. Otevři podle klienta,
pro kterého stavíš.

- [Vláda a veřejná správa](ux-design/kontext/vlada.md) - právní mantinely (zákon 99/2019 Sb., Section 508, ADA Title II), konkrétní WCAG prahy, identita provozovatele před vizuálem.
- [Zdravotnictví](ux-design/kontext/zdravotnictvi.md) - vizuál jako prahová zkouška, NHS čitelnost a tón, forenzní rozbor „zaoblené je klikatelnější" folklóru.
- [Finance a fintech](ux-design/kontext/finance.md) - vizuál jako nejsilnější páka kredibility (54,6 % zmínek u Fogg 2002), FCA Consumer Duty, EAA pro banking.
- [Luxury](ux-design/kontext/luxury.md) - nejslabší evidenčně podložený sektor v knihovně, poctivě přiznané.
- [Dev tools a SaaS](ux-design/kontext/dev-tools-saas.md) - osm pravidel pro nástroje, které uživatel používá denně: odvození barev v percepčně uniformním prostoru, hustota a rychlost jako záměrný parametr, přednost známým vzorům, přístupné neznamená výrazné. Plus proč „Linear look" a temný hustý vzhled jsou konvence, ne evidence.
- [E-commerce](ux-design/kontext/e-commerce.md) - nejvyšší výchozí nedůvěra ze všech sektorů, jak citovat Baymard bez čísel o konverzi.
- [Děti](ux-design/kontext/deti.md) - tři věková pásma, velikosti písma z testování s dětmi, Children's Code jako privacy rámec.
- [Senioři](ux-design/kontext/seniori.md) - nejtvrdší čísla v knihovně (43 % pomalejší, 45 % problém s taby), řešením je WCAG AA, ne oddělený senior mód.
- [Gastro](ux-design/kontext/gastro.md) - restaurace/bar/kavárna na ose destinace ↔ sousedská utilita; alergenová a EAA regulace ověřená proti primárním textům, menu-design výzkum (Yang 2012 vyvrací zlatý trojúhelník, Ip & Chark 2023 diskontuje laboratorní nálezy na třetinu), dvě fabrikované citace odhalené a zdokumentované.

## Enterprise UI (produktové aplikace: dashboardy, CRUD, administrace)

**Tři noty v téhle sekci platí i mimo produktové aplikace, protože popisují chování prohlížeče, ne konvenci Carbonu:** [stabilita layoutu](enterprise-ui/vzory/stabilita-layoutu.md), [překryvy a vrstvení](enterprise-ui/vzory/prekryvy-a-vrstveni.md) a [přetečení a zkracování](enterprise-ui/vzory/preteceni-a-truncation.md). Jsou třída A z MDN. Sáhni po nich i u marketingového webu.

Odvozeno z dokumentace IBM Carbon Design System (lokální kopie, čteno 30. 7. 2026). Přebrané jsou
**principy, vzory a rozhodovací pravidla**, ne vizuál: žádné Carbon tokeny, hex hodnoty, IBM Plex,
elevation škály ani ikonová knihovna. Většina pravidel je třída **B** (publikovaná konvence design
systému), citované WCAG a peer-reviewed studie jsou **A**, vlastní syntéza je označená **C**.
Kde se Carbon rozchází s `ux-design/pravidla/`, vyhrává knihovna a konflikt je popsaný v místě.

Tři noty ve `vzory/` z Carbonu nepocházejí: stabilita layoutu, překryvy a vrstvení a část přetečení
stojí na MDN a na praxi, a jsou proto **třída A**. Řeší jednu rodinu problémů: chování, které mlčky
neproběhne a jehož symptom vypadá jako úplně jiná chyba.

### Základy

- [Vrstvy enterprise UI](enterprise-ui/zaklady/vrstvy-a-vzory.md) - vstupní nota sekce: tři vrstvy (prvky, komponenty, vzory), v jaké vrstvě hledat jakou odpověď, a explicitní seznam toho, co z Carbonu záměrně nepřebíráme a proč.
- [Volba komponenty](enterprise-ui/zaklady/volba-komponenty.md) - **vstupní bod podle úkolu, ne podle komponenty. Otevři jako první, i když neváháš.** Osm situací („uživatel má něco zadat", „vybrat z možností", „vidět víc záznamů", „přepnout obsah nebo projít krok za krokem", „zúžit množinu dat", „čeká", „něco potvrdit", „systém potřebuje něco sdělit") a u každé tabulka, který prvek zvolit a čím se liší od podobného.
- [Mřížka, breakpointy a chování panelů](enterprise-ui/zaklady/2x-grid-a-breakpointy.md) - 2x grid, pět breakpointů, fluid vs. fixed, gutter módy, poměry stran, chování plovoucích a fixních panelů.
- [UX copy v produktu](enterprise-ui/zaklady/ux-copy-v-produktu.md) - sentence case jako pravidlo, uzavřený seznam výjimek pro velká písmena, tón, aktivní vs. pasivní, can/may/might, plus co z toho platí v češtině.
- [Klávesnice a focus napříč komponentami](enterprise-ui/zaklady/klavesnice-a-focus.md) - které klávesy musí komponenta obsloužit a kam dát výchozí focus v dialogu podle jeho typu (transakční na první pole, potvrzovací na primární tlačítko, destruktivní na Zrušit). Otevři vždy, když píšeš vlastní interaktivní komponentu nebo modál.
- [Oznámení pro čtečky](enterprise-ui/zaklady/oznameni-pro-ctecky.md) - přístupné názvy, drátování labelu a helper textu, live regiony (polite vs. assertive), vystavení stavu a hodnoty, dekorativní obrázky.

### Vzory

- [Prázdné stavy](enterprise-ui/vzory/prazdne-stavy.md) - co ukázat tam, kde nejsou data. Podle Carbonu je prázdný stav často první věc, kterou uživatel v produktu vidí.
- [Načítání a čekání](enterprise-ui/vzory/nacitani-a-cekani.md) - který indikátor při jakém čekání, a doložený rozpor: Carbon skeletony doporučuje, knihovna má proti nim měření a Carbonova citace jeho vlastní tvrzení nepodpírá.
- [Dialogy, modaly a boční panely](enterprise-ui/vzory/dialogy-a-panely.md) - kdy přerušit uživatele překryvem a kdy ne, kde má být akce, co se stane při chybě uvnitř dialogu.
- [Notifikace: stav krát typ](enterprise-ui/vzory/notifikace.md) - co uživateli ukázat po dokončené nebo selhané akci a jak moc ho tím smíš přerušit. Stav a typ se volí zvlášť a kombinují. Inline, toast, callout, banner, panel: který kam, co smí zmizet samo, co ne, a kdy notifikaci neposílat vůbec.
- [Filtrování](enterprise-ui/vzory/filtrovani.md) - zúžení množiny dat předem danými atributy: kam filtry umístit (víc kategorií nikdy do dropdownu), kdy aplikovat okamžitě a kdy dávkově tlačítkem, a co musí být vidět na zavřeném filtru. Zobrazení aktivních filtrů jako odstranitelných tagů je v [Tagy](enterprise-ui/komponenty/tagy.md).
- [Hledání](enterprise-ui/vzory/hledani.md) - tři typy podle velikosti datové sady a podle toho, kam uživatel po hledání jde.
- [Skladba formuláře](enterprise-ui/vzory/formular-skladba.md) - rozvržení, sekce, mezery, poloha tlačítek, technika pro dlouhé formuláře, a rozpor s knihovnou v načasování validace.
- [Stavové indikátory](enterprise-ui/vzory/stavove-indikatory.md) - **sloupec „stav" v tabulce, odznak u položky, závažnost zprávy.** Čtyři prvky, kterými stav jde nést (symbol, tvar, barva, typografie), proč barva sama podle WCAG nestačí, badge, konsolidovaný stav nad skupinou a kdy indikátor nepoužít vůbec.
- [Přetečení obsahu a zkracování](enterprise-ui/vzory/preteceni-a-truncation.md) - kde smíš zkrátit výpustkou, kde nikdy, a kdy místo zkrácení nabídnout „Zobrazit více".
- [Překryvy a vrstvení](enterprise-ui/vzory/prekryvy-a-vrstveni.md) - **proč modál nevyleze nad header, i když má z-index 9999**, proč se sticky prvek nedrží při scrollu, nebo se fixed prvek pozicuje vůči něčemu jinému, než čekáš. Co všechno zakládá stacking context, top layer jako řešení, sonda do konzole. Třída A ze specifikace.
- [Stabilita layoutu při změně dat](enterprise-ui/vzory/stabilita-layoutu.md) - když uživatel přepne filtr nebo rozsah, má se změnit obsah a nic jiného. Proč automatická šířka sloupců je funkce dat, proč tabulární číslice nestačí, a kam patří ovládání, které tu změnu vyvolává.
- [Disabled, read-only, nebo skryté](enterprise-ui/vzory/disabled-vs-read-only.md) - tři způsoby, jak udělat prvek neovladatelný. Volba mezi nimi je přístupnostní rozhodnutí, ne vizuální.
- [Běžné akce](enterprise-ui/vzory/bezne-akce.md) - co přesně znamená Add, Cancel, Clear, Close, Copy, Delete, Edit, Next, Refresh, Remove a Reset a čím se liší (Delete zničí objekt, Remove ho jen vyjme ze seznamu). Tři úrovně dopadu mazání a jak podle nich odstupňovat potvrzení. **Save ve slovníku není.**
- [Hromadné akce nad filtrovanou a stránkovanou množinou](enterprise-ui/vzory/hromadne-akce.md) - **co vlastně znamená „vybráno", když je tabulka filtrovaná i stránkovaná.** Checkbox v hlavičce vybírá stránku, ne filtr; co s výběrem při přepnutí stránky a při změně filtru; jak potvrdit smazání 200 položek, když žádný jeden název neexistuje; a co ukázat, když z dávky projde jen část. Většina pravidel je třída C, Carbon tuhle oblast nepokrývá.

### Komponenty

- [Datové tabulky](enterprise-ui/komponenty/datove-tabulky.md) - nejsložitější komponenta enterprise UI: kdy tabulku, jak ji vrstvit funkcemi (řazení, výběr, batch akce, rozbalování), výšky řádků, co do ní nepatří.
- [Výběr ze seznamu](enterprise-ui/komponenty/vyber-ze-seznamu.md) - select, dropdown, combo box, multiselect: čtyři komponenty, které vypadají skoro stejně a chovají se různě.
- [Textová pole](enterprise-ui/komponenty/textova-pole.md) - input, text area, password: kdy které, jak volit mezi helper textem, placeholderem a tooltipem, chování při přetečení.
- [Taby](enterprise-ui/komponenty/taby.md) - kdy taby a kdy něco jiného, tři varianty, zarovnání na mřížku, rozdíl mezi automatickým a manuálním tablistem.
- [Dlaždice a karty](enterprise-ui/komponenty/dlazdice-a-karty.md) - kdy je karta klikatelná celá a kdy jen CTA uvnitř. Nejsou to dva režimy, jsou to vzájemně vylučující varianty a míchat je znamená rozbít cíl kliknutí.
- [Tagy](enterprise-ui/komponenty/tagy.md) - **nejčastější použití: ukázat aktivní filtry tak, aby šly po jednom zrušit.** Čtyři varianty se liší funkcí, ne vzhledem (read-only, dismissible, selectable, operational) a zaměnit je je nejčastější chyba. Plus kdy sáhnout po tagu a kdy po stavovém indikátoru.
- [Stránkování](enterprise-ui/komponenty/strankovani.md) - dvě varianty, dvě umístění, párování výšky s výškou řádku tabulky, a pravidlo, kdy stránkovat nemá smysl.
- [Tooltip a toggletip](enterprise-ui/komponenty/tooltip-a-toggletip.md) - vypadají stejně, chovají se různě. Rozdíl je v tom, jak se vyvolávají a jestli obsah potřebuje interakci.
- [Tlačítka: varianty, skupiny, zarovnání](enterprise-ui/komponenty/tlacitka-varianty.md) - taxonomie pěti variant, doporučené kombinace ve skupinách, zarovnání podle kontextu. Tvrdá pravidla o tlačítkách zůstávají v `ux-design/pravidla/tlacitka.md`, tahle nota na ně odkazuje.
- [Navigace v hierarchii](enterprise-ui/komponenty/navigace-v-hierarchii.md) - **drobenka** („kde jsem") a **indikátor postupu** u wizardu, onboardingu nebo vícekrokového formuláře („jak daleko jsem"). Uzavřený seznam, kdy indikátor postupu nepoužít (pod tři kroky, libovolné pořadí, proměnlivý počet kroků), sedm stavů kroku, validace před postupem, a dva popsané konflikty s pravidly knihovny.

## Proces

- [Step by step: UX/UI web a app design](ux-design/proces/step-by-step-ux-ui.md) **[neúplné]** - přehled 21 kroků procesu po jedné řádce, ale rozvedené jsou jen dva: user flow a wireframy, a druhý se láme uprostřed. Otevři na user flow diagram nebo na přehled kroků jako check-list, ne na návod ke konkrétnímu kroku.

## Barvy

- [Color Theory](ux-design/color/color-theory.md) - teorie barev, barevné kruhy, schémata.
- [Color Psychology](ux-design/color/color-psychology.md) - psychologie barev a emoce.
- [Color Grading](ux-design/color/color-grading.md) - color grading videa v Premiere, mimo rozsah knihovny. **[archiv]**
- [Pravidlo 60-30-10](ux-design/color/pravidlo-60-30-10.md) - poměr neutrální, primární a akcentní barvy v paletě. **Nese override:** rada „90 % saturace, 90 % jasu" na akcent vyrábí porušení kontrastu právě u primárního CTA, správně jsou dvě varianty akcentu. Poměr sám je třída C.

## Typografie

- [Typography - základy, anatomie](ux-design/typography/typography-zaklady-anatomie.md) - anatomie písma, základy.
- [Serif a Sans Serif](ux-design/typography/serif-a-sans-serif.md) - kdy patkové vs. bezpatkové.
- [Práce s fontem](ux-design/typography/prace-s-fontem.md) - praktická práce s fonty.
- [Font pairing](ux-design/typography/font-pairing.md) - jak vybrat dvě rodiny, aby to vypadalo jako rozhodnutí. Přepsáno 23. 8. 2026, původní verze radila 3-4 fonty a šla proti `anti-slop.md`.

## Layout

- [Layout Theory](ux-design/layout/layout-theory.md) - slovníkové definice na 32 řádcích: co je whitespace, margin a focal point. **Padding v ní není.** Na skutečné rozvržení jdi do [Mřížka a breakpointy](enterprise-ui/zaklady/2x-grid-a-breakpointy.md) nebo [Osmibodová mřížka](ux-design/zakony-principy/osmibodova-mrizka.md).
- [Grids a Golden ratio](ux-design/layout/grids-a-golden-ratio.md) - mřížky a zlatý řez.

## Web-dev (implementace)

- [HTML a CSS](web-dev/html-a-css.md) - úvod do HTML a CSS z kurzu: box model, selektory, třídy a ID, vkládání fontů a barev. **Neřeší z-index a vrstvení, grid ani flexbox.** Na vrstvení jdi do [Překryvy a vrstvení](enterprise-ui/vzory/prekryvy-a-vrstveni.md), na mřížku do [Mřížka a breakpointy](enterprise-ui/zaklady/2x-grid-a-breakpointy.md).
- [Stylizace textu](web-dev/stylizace-textu.md) - práce s textem v CSS.
- [Inserting CSS](web-dev/inserting-css.md) - způsoby vkládání CSS. **[stub]**
- [Using best images possible](web-dev/using-best-images.md) - volba a příprava obrázků. **[stub]**

## Google Sheets

- [Znalostní báze](sheets/znalostni-baze.md) - rozhodovací rámec otázka→graf, brand tokeny, archetypy reportů, A/B slop→profi, kritéria kvality.
- [NotebookLM destilát](sheets/notebooklm-destilat.md) - surovější výzkumný podklad včetně URL zdrojů.
- [Apps Script vrstva](sheets/apps-script-vrstva.md) - styling přes Apps Script a clasp.

## Příklad hotového design systému

- [Design system DRIVE](ux-design/priklady-ds/design-system-drive.md) - kompletní DS s konkrétními tokeny: paleta s hex kódy, typografická škála, WCAG kontrasty, komponenty (tlačítka, karty, mikrointerakce). Nejrozsáhlejší nota v knihovně, reálná ukázka převedení designu do specifikací.

## Trendy

- [Grafické trendy](ux-design/trendy/graficke-trendy.md) - deset názvů trendů, všechny ukázky chybí. **[archiv]**
- [Trendy v typografii](ux-design/trendy/trendy-v-typografii.md) - prázdná nota, obsah byl v obrázcích. **[archiv]**

Postoj knihovny k trendům drží [Anti-slop](ux-design/pravidla/anti-slop.md) a
[Vizuální craft](ux-design/pravidla/vizualni-craft.md), tam jsou pravidla se třídou důkazu.

## Další

- [Logo design](ux-design/logo-foto/logo-design.md) - na čem stojí použitelné logo: rozpoznatelnost bez barvy, v každé velikosti, negative space.
- [Photography](ux-design/logo-foto/photography.md) - ovládání fotoaparátu (expozice, clona, ISO), ne práce s fotografií v designu. **[archiv]**

## Destiláty pro moment psaní kódu

Nepatří do knihovny, jsou to imperativy vytažené z toho, co je výše:

- [rules/frontend-ux.md](rules/frontend-ux.md) - path-scoped pravidlo (`.tsx`, `.css`), ke zkopírování do `~/.claude/rules/`.
- [rules/frontend-ux-detailed.md](rules/frontend-ux-detailed.md) - stejné imperativy s odkazy do knihovny.

## Zdroje k učení

- [Kurzy](ux-design/zdroje/kurzy.md) - osobní seznam absolvovaných a plánovaných kurzů. **[archiv]**
- [Videa](ux-design/zdroje/videa.md) - dva odkazy na tutoriály. **[archiv]**
