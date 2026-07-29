# NEURO-DESIGN MASTER DOCUMENT: KOGNITIVNÍ ERGONOMIE A ARCHITEKTURA DATOVÝCH ROZHRANÍ

## SYSTÉMOVÁ ROLE A ÚČEL DOKUMENTU
Tento dokument slouží jako absolutní instrukční databáze a referenční rámec pro generování a evaluaci UI/UX designu, prezentačních layoutů a informační architektury. Syntetizuje interní datové sady (UX zákony, teorii barev, pravidla mřížek) s nejnovějším empirickým výzkumem z let 2024–2026 v oblasti očního trasování (eye-tracking), neuroestetiky a redukce kognitivní zátěže. Cílem je poskytnout modelu Claude exaktní, algoritmické postupy pro tvorbu vizuálních rozhraní, která respektují biologické limity lidského vnímání, a eliminovat kritické systémové chyby identifikované v analyzovaných datasetech (např. prezentační deck *Trustsoft*).

---

## MODUL 1: BIOLOGIE VIZUÁLNÍ PERCEPCE
*(Zdroj: Extrahováno z Google Search výzkumů 2024–2026 + Interní poznámky k UX)*

### Fyziologie očního trasování a filtrace vizuálního šumu
Lidské oko nečte digitální rozhraní plynule, ale pohybuje se pomocí rychlých skoků (sakád) a krátkých zastavení (fixací). Kognitivní věda a moderní eye-tracking teplotní mapy z roku 2026 neúprosně ukazují, že uživatelé a publikum věnují **80 % svého vizuálního času horní třetině obrazovky**. Spodních 30 % je často zcela ignorováno, pokud k nim nevede silný vizuální vektor. 

Rozlišujeme dva primární vzorce skenování, které musí každý algoritmus generování layoutu respektovat:
1. **F-Pattern (F-vzor):** Typický pro textově orientovaná rozhraní. Uživatelé skenují horizontálně horní část, následně se posunou mírně dolů pro druhý horizontální sken a zbytek obsahu skenují přísně vertikálně podél levého okraje, kde hledají klíčová slova. 
2. **Z-Pattern (Z-vzor):** Aplikovatelný pro vizuálnější "Hero" sekce a prezentační slajdy. Oči putují zleva doprava nahoře, následně diagonálně do levého dolního rohu a končí horizontálním pohybem vpravo dole.

### Kognitivní zátěž a paralýza analýzy (Cognitive Load Theory)
Kognitivní zátěž definuje množství mentální kapacity potřebné k dekódování rozhraní. Dělí se na vnitřní (náročnost samotného úkolu), vnější (zbytečná zátěž způsobená špatným designem) a relevantní (učení). 

**Biologický důvod selhání uniformních mřížek:**
Pokud algoritmus vygeneruje na slajdu mřížku s 15 prvky o naprosto stejné matematické velikosti (viz analyzovaný slajd *Trusted by industry leaders*), vyvolá masivní nárůst *vnější kognitivní zátěže* (Extraneous Load). Podle *Hickova zákona* (čas potřebný k rozhodnutí se zvyšuje s počtem možností) a biologické absence ohniska nedokáže vizuální kortex určit prioritu. Mozek se snaží zpracovat všechny podněty se stejnou vahou, což vede ke kognitivnímu přehlcení, frustraci a tzv. "paralýze analýzy".

---

## MODUL 2: MATEMATIKA MŘÍŽEK A GESTALT FYZIKA
*(Zdroj: Interní dokumenty "Osmibodová mřížka", "Gestaltovy zákony", "Layout Theory")*

### Pravidla pro asymetrickou stabilitu
Zatímco symetrie působí staticky a po čase nudně, asymetrická stabilita vytváří dynamické, ale vyvážené napětí. Vychází z distribuce optické hmoty napříč osami "Gridu". Velký prvek na jedné straně musí být vyvážen negativním prostorem (Whitespace) a shlukem menších prvků s vysokou saturací na straně druhé.

### Exaktní výpočet ochranné zóny (Whitespace)
Whitespace není prázdné místo, je to aktivní strukturální element, který definuje tzv. kognitivní dýchání designu. Základem je *Krabicový model* (Box model - Padding, Margin, Border) vázaný na přísnou **8-bodovou mřížku**. 

`Základní jednotka (Base Unit) = 8px` (nebo 8pt)

**Logický vzorec pro generování bezpečných zón:**
```javascript
// Algoritmus pro výpočet minimálního Marginu kolem kritických elementů
function calculateWhitespace(element_importance, base_unit) {
    if (element_importance === 'Hero') {
        return base_unit * 8;  // 64px pro izolaci a vynucení Von Restorffova efektu
    } else if (element_importance === 'Grouping') {
        return base_unit * 4;  // 32px pro makro kompozici (Zákon společné oblasti)
    } else {
        return base_unit * 2;  // 16px pro mikro prvky v rámci celku
    }
}
```

### Gestalt fyzika jako gravitační síly
Při generování UI aplikujeme Gestalt principy jako vektory fyzikální přitažlivosti:
*   **Zákon blízkosti (Proximity):** Prvky oddělené mezerou menší než `base_unit * 3` jsou mozkem vnímány jako jedna sémantická jednotka. Slouží ke shlukování dat ("chunking" dle Millerova zákona, který limituje paměť na 7±2 položky).
*   **Zákon podobnosti (Similarity):** Stejný font, barva či tvar vytváří propojení bez ohledu na vzdálenost.
*   **Zákon společné oblasti:** Ohraničení boxem nebo podbarvením vytváří neprostupnou kognitivní zeď.

---

## MODUL 3: ALGORITMY SÉMANTICKÉHO ŠKÁLOVÁNÍ
*(Zdroj: Google Search výzkum 2025–2026 a interní syntéza)*

Každý element na plátně musí mít definovanou vizuální váhu, která matematicky odpovídá jeho informační hodnotě. Vizuální váha je kalkulována na základě velikosti, barevné saturace a kontrastu.

### Sémantická škálovací matice (Heuristika pro Visual Weight)
```python
# Výpočet celkové vizuální váhy prvku
def get_visual_weight(area_px, saturation_index, contrast_ratio):
    # saturation_index: 0.0 (šedá) - 1.0 (neonová)
    # contrast_ratio: 1.0 (neviditelný) - 21.0 (černá vs. bílá)
    base_weight = area_px * (1 + saturation_index)
    return base_weight * math.log(contrast_ratio)
```

**Pravidla alokace prostoru:**
1.  **Level 1 (Hero Element):** 100% vizuální váha. Přiděluje se striktně pouze jednomu hlavnímu prvku (nadpis, klíčový graf).
2.  **Level 2 (Supporting Elements):** Max 50% vizuální váha vůči Hero prvku. Zajišťují kontext.
3.  **Level 3 (Micro Elements):** Max 15% vizuální váha. Footer, tagy, metadata.

### STRIKTNÍ ZÁKAZ A FAIL-SAFE PRAVIDLO
**ZÁKAZ:** Generování homogenních polí obrázků (např. sekce "Naši partneři" nebo "Technologie") o stejné matematické velikosti `width x height`.
**DŮVOD:** Logo ve tvaru plného čtverce (např. *Adcubum*) o rozměrech 200x200px má obrovskou vizuální denzitu. Logo tvořené úzkým textem (např. *Richemont*) ve stejném boxu vizuálně zanikne. Vzniká tak náhodná hierarchie, která mate uživatele a znehodnocuje značky.
**ŘEŠENÍ:** Algoritmus musí aplikovat vyvážení podle optického objemu.

---

## MODUL 4: PERSUASIVE DESIGN A VEDENÍ POZORNOSTI
*(Zdroj: Interní data "Zákony UX", "Color Theory", Google Search)*

Rozhraní nesmí být pasivním úložištěm informací, musí fungovat jako navigační tunel pozornosti (Parkinsonův zákon omezení prostoru a času).

### Extrémní kontrast a pravidlo jednoho Focal Pointu
Podle *Von Restorffova efektu* (Izolační efekt) si lidé pamatují prvek, který narušuje vzorec. 
*   **Pravidlo:** Každý slajd či screen smí mít matematicky právě **JEDEN Focal Point**. 
*   **Aplikace:** Použití pravidla 60-30-10. Focal point využívá 10% akcentní barvu s vysokou saturací (nad 90 %) a světlostí (nad 90 %). Zbylých 90 % tvoří neutrální a primární tóny.

### Topologie Call-to-Action (CTA) prvků
Na základě biologických očních map musí být interaktivní prvky (nebo klíčová sdělení) umístěny v terminálních bodech skenovacích vzorců.
*   Při **Z-Patternu** je cílovým terminálem **pravý dolní roh** bloku.
*   Při **F-Patternu** leží nejteplejší zóna v levé části obrazovky na konci horizontálních řádků.
*   Z hlediska *Fittsova zákona* musí být CTA dostatečně veliké, aby snížilo čas nutný pro interakci (vizuální i motorickou). Pokud CTA postrádá kontext, spouští se *Efekt utopených nákladů* a *Zeigarnikové efekt* (uživatel si pamatuje nedokončené cesty, pokud jsou správně naznačeny).

---

## MODUL 5: DIAGNOSTIKA CHYB A FAIL-SAFE PROTOKOLY
*(Zdroj: Interní reverzní inženýrství přiloženého PDF decku Trustsoft)*

Analýza dodaných vizuálů odhalila závažné kolize s neuro-designovými pravidly. Pro každou chybu je definován "Fail-Safe" protokol, který si model Claude musí osvojit při generování instrukcí pro kód nebo design.

### CHYBA 1: "Logo Soup" (Slajd "Trusted by industry leaders")
*   **Symptom:** Na ploše se nachází 15 logotypů seřazených v uniformní mřížce 3x5. Logo *MSD* a *Sunrise* opticky drtí zbytek plátna. Logo *Richemont* je nečitelné mikro-smetí. Chybí jakákoliv hierarchie. Vizuální váha je zcela destruována.
*   **Diagnóza:** Algoritmické zarovnání na střed bounding-boxů bez zohlednění vnitřní vizuální hustoty jednotlivých křivek. Extrémní nárůst kognitivní zátěže.
*   **Fail-Safe Algoritmus:**
    ```python
    def enforce_optical_balance(logo_array):
        # KROK 1: Rozdělení do Tiers (např. Tier 1 = klíčoví klienti, Tier 2 = ostatní)
        tiered_array = group_by_importance(logo_array)
        
        # KROK 2: Aplikace kompenzátoru optického objemu
        for logo in tiered_array:
            if logo.shape == "horizontal_thin_text":
                logo.scale = base_scale * 1.5
            elif logo.shape == "heavy_solid_block":
                logo.scale = base_scale * 0.75
            else:
                logo.scale = base_scale
        
        # KROK 3: Vytvoření dynamické asymetrie (zakázána prostá mřížka 3x5)
        return generate_masonry_or_weighted_layout(tiered_array)
    ```

### CHYBA 2: Narušená konektivita a vizuální napětí (Slajd "Visibility ≠ Control")
*   **Symptom:** Levá strana obrazovky obsahuje masivní, podbarvené kartičky (Cloud dashboards, atd.). Pravá strana (What they're actually missing) je tvořena pouhým textem s malými žlutými tečkami.
*   **Diagnóza:** Porušení zákona těžiště a Gestalt *Zákona společné oblasti*. Levá strana je "těžká", pravá "lehká", čímž se rozhraní opticky překlápí doleva. Chybí jednotný kontejner, který by vyvážil pravou stranu.
*   **Fail-Safe Algoritmus:**
    ```yaml
    CONDITION: side_by_side_comparison
    ACTION: 
      IF left_column HAS background_fill AND border_radius:
         THEN right_column MUST HAVE balancing_container OR reciprocal_visual_weight
         ELSE remove background_fill FROM left_column TO equalise cognitive tension.
    ```

### CHYBA 3: Kognitivní tření u překryvů (Slajd "About Trustsoft")
*   **Symptom:** Tři obří zelené kruhy reprezentující statistiky se vzájemně překrývají (Vennův diagram bez průniku dat). Text uvnitř je stísněný, nerespektuje dostatečný negativní prostor (Margin blížící se nule u okrajů kružnice). 
*   **Diagnóza:** Nesmyslná aplikace překrývání. Překryv (overlap) signalizuje relaci nebo sloučení. Zde jde o nezávislá data (100+ certifikací, 370+ projektů, 150+ expertů). Výsledkem je porušení sémantiky a snížení čitelnosti textu (malý vnitřní padding).
*   **Fail-Safe Algoritmus:**
    ```javascript
    if (layout_type === 'data_points' && is_venn_diagram === false) {
        prohibit(overlap_shapes);
        apply(linear_grid_with_equal_spacing);
        enforce(inner_padding >= 4 * base_unit); // Text musí v kruhu dýchat
    }
    ```

### CHYBA 4: Absence ohniska (Slajd "What we can do")
*   **Symptom:** Tři sloupce (Migrate, Optimize, Operate) mají identickou grafickou úpravu, barvu i velikost ikony. Neexistuje žádný primární kotevní bod (Focal Point).
*   **Diagnóza:** Selhání asymetrické rovnováhy a Von Restorffova pravidla. Oko uživatele klouže po povrchu bez jasného bodu vstupu do informace.
*   **Fail-Safe Algoritmus:**
    *Zásada:* I při výčtu vlastností musí být jeden bod vyzdvižen jako "Most Popular", "Doporučený", nebo vizuálně ukotven asymetrickou zátěží (např. ztmavením pozadí jedné karty), aby oko získalo výchozí souřadnici pro oční trasování. Vždy aplikuj `FORCE_ASYMMETRICAL_FOCAL_POINT` logiku.

Tento master dokument stanovuje neoddiskutovatelná pravidla. Očekává se, že jakákoli budoucí generace UI, kódu či textového popisu layoutů plně absorbuje výše uvedené kognitivní limity a algoritmické fail-safe systémy.