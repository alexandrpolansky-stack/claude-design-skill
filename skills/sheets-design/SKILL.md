---
name: sheets-design
description: >-
  Sáhni po tomhle, když stavíš nebo styluješ konkrétní Google Sheets report, dashboard nebo
  přehled pro člověka (výstup automatizace, reporting, KPI přehled, sdílená tabulka).
  Sheets-specifické, v TrustSoft identitě, a Claude umí styling rovnou aplikovat na živý Sheet
  přes Sheets API bez copy-paste. Spouštěj PROAKTIVNĚ a sám (model-invoked), i když to uživatel
  neřekne výslovně, kdykoliv vzniká Sheet co má vypadat profesionálně. Na obecná UX rozhodnutí
  mimo Sheets (weby, appky, e-maily, dokumenty) použij design-advisor.
---

# Sheets design

Google Sheet má vypadat jako report v **TrustSoft identitě**, ne jako rozsypaná tabulka. Kvalita = kázeň v mřížce a mazání všeho bez informace, ne dekorace. Sheets-specifický sourozenec `design-advisor` (obecné UX). Hloubku drží znalostní báze, tady je destilát + jak to aplikovat živě.

## Zdroj pravdy (přečti relevantní sekci před stavbou)
- **Design + brand:** [sheets/znalostni-baze.md](../../sheets/znalostni-baze.md) — rozhodovací rámec otázka→graf, TrustSoft paleta+font, A/B slop→profi, archetypy reportů, kritéria kvality.
- **Podklad výzkumu:** [sheets/notebooklm-destilat.md](../../sheets/notebooklm-destilat.md) — surovější destilát včetně URL zdrojů.
- **Apps Script varianta:** [sheets/apps-script-vrstva.md](../../sheets/apps-script-vrstva.md).
- **Živý tool:** `sheets-styler` v interním repu `trustsoft-tools` (Sheets API v4, user-OAuth, creds v Keychain). Není součástí tohoto repa.

## Postup
1. **Souvislosti:** kdo čte, jaká otázka, jaký archetyp (exec KPI dashboard / operativní tracker / finanční model / sdílený přehled). Z toho plyne struktura, paleta, typy grafů.
2. **Struktura:** odděl Data / Výpočty / Prezentaci; hlavní sdělení a KPI vlevo nahoře (F-pattern); max 5-9 prvků na jeden view (Miller), zbytek za filtry.
3. **Styling v TrustSoft brandu** (mantinely níže).
4. **Aplikace živě** přes `sheets-styler`: dry-run → test na KOPII → `--apply`.
5. **Verify:** slop self-check + test 24 vteřin (člověk mimo projekt pochopí hlavní sdělení bez vysvětlení).

## Anti-slop mantinely + TrustSoft brand (tvrdá pravidla)
Paleta a font jsou brand tokeny, přebíjí generické:
- **navy `#202C39`** struktura/hlavičky/text, **green `#8EC641`** JEDINÝ akcent, **dkGreen `#35601A`** zelená pro text na bílém (akcentní green je moc světlá → nízký kontrast), grey ramp (`#F5F7FA #E2E8EF #C7D0DA #8B97A4 #5A6672 #38424E`), **coral `#EA6044` / amber `#F0C602` jen funkčně** (chyba/varování), gray999 `#707070` muted. AWS/Azure barvy opt-in only.
- **Font Work Sans.** Hierarchie velikostí/váhou, ne barvou.
- Barva = jen význam; **stav vždy i textem**; kontrast text 4.5:1 / grafika 3:1; na tmavém pozadí text jen bílá/green.
- **Gridlines VŽDY nechat viditelné.** Existující TrustSoft listy (Access Overview a spol.) je mají; skrývání vypadá cize a nový list nesedne k ostatním → NIKDY nevolej `hide_gridlines` / `setHiddenGridlines(true)` na TrustSoft listech. Obecný dataviz výzkum tvrdí opak, tohle domácí pravidlo ho přebíjí. Čísla doprava bez balastních desetin, zebra white/`n50`, tenké `n100` linky, freeze hlavičky.
- Zamčený table styling: navy hlavička + bílý bold; zebra white/`n50`; muted sloupec `gray999`; highlight sloupec `hi` (`#EFF5E3`) + navy bold.
- **Green dosage:** max jedna velká zelená masa (jinak přehoď sekundární prvky na navy/grey).
- **Nikdy:** 3D/zkosené grafy, gradienty/fake stíny, ohraničení všude, rainbow, >6 barev, >2 fonty, data-heavy do karet/bulletů (data = tabulka), em-dashe.
- **Slop self-check před „hotovo":** nese každá barva význam? >2 fonty / >6 barev? stav čitelný černobíle? gridlines VIDITELNÉ? KPI srozumitelné bez luštění?

## Živé stylování (Claude to udělá sám, bez copy-paste)
Tool `sheets-styler` = Sheets API v4 `batchUpdate` (user-OAuth, creds v Keychain). `sheets_styler.py` má brand paletu `TS` + `FONT` a builder funkce (format_cells, set_row_height/col_width, merge, banding, borders, cond_*). Sestav `requests`, pak:
1. **dry-run** (bez `--apply` jen vypíše, nic nezapíše),
2. první ostrý zápis vždy na **KOPII / throwaway Sheetu**, ne na živém reportu,
3. `--apply`.

Idempotence: banding smaž (deleteBanding) před addBanding, CF nahraď celým seznamem. batchUpdate je atomický (vše nebo nic). GridRange 0-indexovaný, end exkluzivní. Když styling má žít v Sheetu (menu/trigger), použij Apps Script vrstvu + clasp.

## Časté chyby
- Generická paleta místo TrustSoft brandu → vždy `TS` tokeny.
- Zápis rovnou na živý report → nejdřív kopie + dry-run.
- Akcentní green na text na bílém → dkGreen `#35601A`.
- Cpát data do karet/bulletů → data-heavy = tabulka.
- **Skrývat gridlines → NIKDY** na TrustSoft listech. Nový tab musí vizuálně sednout k existujícím.

## Vztah k ostatním
`design-advisor` = obecné UX i mimo Sheets. Tenhle = Sheets-specifická implementace + živá aplikace v TrustSoft brandu.
