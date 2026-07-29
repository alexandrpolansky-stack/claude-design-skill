# Kontext: finance a fintech

Čtenář je člověk, který svěřuje peníze a rozhoduje se na první pohled: kredibilitu hodnotí
povrchem, ne obsahem. Dopad chyby: ztráta důvěry je okamžitá a u regulovaných produktů má
špatně podaná informace i právní následky (misleading communication). Regulace je tu mantinel
i pro čistě privátní hráče: v EU váže bankovní UI European Accessibility Act, v UK jde FCA
Consumer Duty explicitně po designu a layoutu. Volbou zůstává tón (formální banka vs hravý
fintech) a povrch, obojí v mezích čitelnosti rizik.

Legenda tříd: A = tvrdá opora (měření), B = publikovaná konvence nebo regulace,
C = řemeslná praxe či pozorování bez opory.

Sesterské noty: [vlada.md](vlada.md), [zdravotnictvi.md](zdravotnictvi.md).

---

### Vizuál je ve financích nejsilnější páka kredibility

**PRAVIDLO:** Investuj do vizuální kvality (typografie, konzistence, profesionální polish)
víc než v jiných sektorech. Neopírej kredibilitu o přesnost obsahu, čtenář ji nehodnotí.
**KDY PLATÍ:** weby a appky finančních služeb pro spotřebitele.
**PROČ:** Fogg 2002 (N=2684): u finančních webů lidé při hodnocení kredibility zmiňují design
look v 54,6 % komentářů, nejvyšší hodnota v celém datasetu (průměr 46,1 %). Information
accuracy naopak jen 8,0 %, nejnižší v datasetu. Dále company motive 21,0 % a name recognition
21,8 %. Lidé u financí hodnotí, jak to vypadá a jestli tomu věří na první pohled, ne přesnost
čísel. Přesný opak vlády a neziskovek, kde vizuál je podprůměrná páka a rozhoduje identita
provozovatele (viz [vlada.md](vlada.md)).
**TŘÍDA:** A
**ZDROJ:** Fogg et al. (2002), Consumer WebWatch study, N=2684, 10 kategorií webů.
**KDY NEPLATÍ:** není to povolení mít nepřesný obsah: regulátor a novinář ho čtou, i když
uživatel ne. Data z roku 2002, USA.

### Klíčové informace zviditelni layoutem, ne disclaimerem

**PRAVIDLO:** Klíčové informace o produktu zvýrazni přes "headings, layout, font, tables,
bullet points". Komunikace musí být "clear, fair and not misleading". Nadbytečné disclaimery
odstraň, ředí to podstatné.
**KDY PLATÍ:** právně závazné pro firmy regulované FCA (UK), PRIN 2A.5.3R a 2A.5.7G.
Mimo UK silná dobrá praxe.
**PROČ:** FCA Consumer Duty mluví přímo o designu: srozumitelnost pro průměrného zákazníka
je regulatorní povinnost a dosahuje se layoutem, ne právním textem navíc. Hromada disclaimerů
je z pohledu regulátora anti-pattern, protože zakrývá to podstatné.
**TŘÍDA:** B (regulatorní mantinel; FCA Handbook PRIN 2A neověřen verbatim z primárního
zdroje, substance ze sekundárních)
**ZDROJ:** FCA Handbook PRIN 2A.5.3R, PRIN 2A.5.7G (Consumer Duty).
**KDY NEPLATÍ:** povinné regulatorní texty (KID, sazebníky) vypustit nejde; pravidlo říká,
že nemají pohřbít klíčové sdělení, ne že zmizí.

### Rizika stejně viditelná jako benefity, frikce u rozhodnutí je žádoucí

**PRAVIDLO:** Risk warning nikdy malým písmem ani nízkým kontrastem. U závažných rozhodnutí
(investice, půjčka, pojištění) vkládej krátké záměrné pauzy v customer journey místo
maximální hladkosti konverze.
**KDY PLATÍ:** regulované finanční produkty; závazné pod FCA (UK), jinde dobrá praxe.
**PROČ:** FCA v rámci Consumer Duty cituje jako dobrou praxi "short, purposeful pauses in the
customer journey" a jako špatnou praxi "risk warnings displayed in small or low contrast
formats". To je pozitivní frikce: opak běžné konverzní optimalizace. Odstranit každé tření
před podpisem úvěru není dobrý UX, je to regulatorní riziko.
**TŘÍDA:** B (regulatorní mantinel)
**ZDROJ:** FCA Consumer Duty, publikované příklady dobré a špatné praxe k PRIN 2A.
**KDY NEPLATÍ:** běžné servisní úlohy (přihlášení, zůstatek, platba známému příjemci):
tam frikce navíc škodí. Pauzy patří k nevratným a závažným rozhodnutím.

### EAA: přístupnost bankovního UI je od 28.6.2025 zákon i pro privátní sektor

**PRAVIDLO:** Spotřebitelské bankovní weby a appky v EU musí splňovat EN 301 549
(≈WCAG 2.1 AA). Konkrétní parametry, které z toho plynou pro design (kontrast 4,5:1,
3:1 pro UI komponenty, target size, reflow), jsou rozepsané ve [vlada.md](vlada.md).
**KDY PLATÍ:** "consumer banking services" jsou explicitně ve scope European Accessibility
Act 2019/882, živého od 28.6.2025. Nejširší regulatorní páka na privátní finanční UI v EU.
**PROČ:** regulatorní mantinel. Na rozdíl od směrnice pro veřejný sektor dopadá EAA na
soukromé firmy; "jsme banka, ne úřad" už jako výmluva nefunguje.
**TŘÍDA:** B (regulatorní mantinel)
**ZDROJ:** směrnice (EU) 2019/882 (European Accessibility Act).
**KDY NEPLATÍ:** scope je spotřebitelský; u čistě B2B nástrojů si nech potvrdit právní výklad,
nespoléhej automaticky na výjimku.

### Fintech tón: odchylku rámuj jako zjednodušení, ne jako rebelii

**PRAVIDLO:** Když opouštíš formální bankovní tón, prodávej to jako srozumitelnost pro
uživatele ("Finance isn't as complex as banks make it sound"), ne jako boření konvencí.
Drž zásadu "serious isn't the same as formal": vážnost tématu zůstává, formálnost jazyka ne.
**KDY PLATÍ:** fintech a challenger produkty mířící na běžného spotřebitele.
**PROČ:** Monzo, nejcitovanější příklad "odvážného" fintech tónu, svou odchylku v publikovaném
tone of voice rámuje výhradně jako zjednodušení pro uživatele. Explicitní tvrzení typu
"boříme bankovní konvenci" nebylo nalezeno v žádném publikovaném tone-of-voice dokumentu
sektoru. I nejodvážnější hráči tedy mění povrch (jazyk), ne strukturu kategorie: uživatel
musí pořád poznat, že jde o banku, které svěří výplatu.
**TŘÍDA:** B pro Monzo zásady (publikovaný tone of voice). Závěr "nikdo to nerámuje jako
rebelii" je pozorování z průzkumu publikovaných guides (C).
**ZDROJ:** Monzo Tone of Voice (veřejně publikovaný guide).
**KDY NEPLATÍ:** private banking a konzervativní klientela: tam neformálnost naráží na
očekávání kategorie. A hravý tón nikdy nesmí do risk warningů a chybových stavů s dopadem
na peníze.

### Modrá = důvěra: konvence ano, věda ne

**PRAVIDLO:** Modrou ber jako bezpečnou sektorovou konvenci bankovnictví, ne jako prokázaný
psychologický efekt. Nikdy neargumentuj "studie ukazují, že modrá zvyšuje důvěru".
**KDY PLATÍ:** volba palety pro finanční brand nebo produkt.
**PROČ:** tvrzení o modré jako nejdůvěryhodnější barvě v bankovnictví existuje (Ha 2009,
citováno v Kosova 2025), ale sama sekundární práce, která ho cituje, ho kritizuje jako
metodicky slabé. Skutečná hodnota modré je konvenční: uživatel ji u banky očekává, takže
neruší rozpoznatelnost kategorie. Stejný vzorec jako u NHS zaoblených rohů: tvrzení, které
se tváří jako věda a zdroj nenese, viz [zdravotnictvi.md](zdravotnictvi.md).
**TŘÍDA:** C (se skepsí; kdo: Ha 2009 via Kosova 2025, metodika kritizovaná)
**ZDROJ:** Ha (2009), citováno a kritizováno v Kosova (2025).
**KDY NEPLATÍ:** jiná barva není chyba, pokud zbytek designu drží rozpoznatelnost kategorie.
Konvenci navíc přebíjí kontrast: brand modrá, která neprojde 4,5:1 na bílé, jde do textu
upravit nebo nepatří do textu vůbec.
