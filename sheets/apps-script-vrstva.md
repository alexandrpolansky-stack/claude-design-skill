
# Apps Script vrstva – Sheets styling (kompetenční cheat-sheet)

> Vrstva 2 skillu `sheets-design` (implementace: jak Claude sám píše a aplikuje styling skript). Design/proč = [Sheets design – znalostní báze](znalostni-baze.md). Vše ověřeno proti oficiální referenci; jediné neúplně ověřené = přesný tvar objektu pro transparentní pozadí grafu (viz níže).

## 1. Výkon a pasti
- **Batch `getValues()`/`setValues()` na 2D poli místo cyklu.** Per-buňkový `setBackground` přes 10 000 buněk ~70 s; jedním `setBackgrounds(2Dpole)` ~1 s (řádově 70x). Každé `getValue()`/`setValue()` překračuje service boundary; look-ahead read a write caching fungují jen když nestřídáš read a write. Vzor: čti celý rozsah jedním `getValues()` → zpracuj v paměti → zapiš jedním `setValues()`. Nikdy nestřídej read/write v cyklu.
- **`SpreadsheetApp.flush(): void`** vynutí čekající zápisy. Použij když další krok závisí na zapsaném stavu (typicky před `getBandings()`/`getConditionalFormatRules()` po zápisu, nebo před `alert`). Ve stylingu většinou netřeba (batch ho nahrazuje).
- **`getDataRange()` vs full-column.** `getDataRange()` = jen rozsah s daty; `getRange('A:Z')` natáhne miliony prázdných buněk. Když znáš rozměry, `getRange(row, col, numRows, numCols)` nejpřesnější.
- **Limity běhu a kvóty** (reset 24 h, per user): script runtime **6 min/execution** (consumer i Workspace, mýtus o 30 min neplatí), custom function 30 s, simple trigger 30 s; triggers total 90 min/den (consumer) vs 6 h/den (Workspace); UrlFetch 20k vs 100k/den; simultánních exekucí 30/user (1000/script).
- **LockService** proti race condition paralelních triggerů: `getScriptLock()` (globálně), `getUserLock()` (per user), `getDocumentLock()` (per dokument, null ve standalone). `Lock.waitLock(ms)` (hodí při timeoutu), `tryLock(ms): boolean`, `releaseLock()`, `hasLock()`. Vzor: `const l=LockService.getScriptLock(); l.waitLock(10000); try{...} finally{l.releaseLock();}`.

## 2. Konvence
- **Konfigurace nahoře:** `const CFG = {...}` (barvy, šířky, názvy listů, formáty). Odděl DATA od FORMÁTOVÁNÍ.
- **Entry point:** jedna veřejná funkce (`buildReport()`) volaná z menu/triggeru/`clasp run`; pomocné privátní konvencí (`_styleHeader_`).
- **Idempotence** (opakovaný běh = stejný výsledek) stojí na 4 vzorcích:
  1. List: `getSheetByName(name)` a když existuje `clear()`/`clearContents()`, jinak `insertSheet(name)`. Nikdy slepě `insertSheet` v cyklu.
  2. Formátování nastav explicitně na fixní hodnoty (`setBackground` fixní barva = vždy stejné).
  3. Banding: `applyRowBanding` na rozsah co už banding má → chyba; nejdřív `sheet.getBandings().forEach(b => b.remove())`.
  4. Conditional format: `sheet.setConditionalFormatRules(kompletníSeznam)`, NE `push` na `getConditionalFormatRules()` (jinak duplikuje každý běh). Stejně named ranges: `removeNamedRange`/přepis, ne slepé přidávání.
- **Error handling a logování:** `console.log()`/`console.error()` → Cloud Logging (preferované); `Logger.log()` je legacy. Exec log: editor Executions nebo GCP Logs Explorer. Obal entry point `try { ... } catch(e){ console.error(e.stack); throw e; }` proti tichému selhání.

## 3. Formátovací API (ověřené signatury)
Všechny `Range.set*` vrací `Range` (řetězení).
```
Range.setBackground(color)            Range.setBackgrounds(String[][])
Range.setFontColor(color)             Range.setFontColors(String[][])
Range.setFontFamily(f)  .setFontSize(int)  .setFontWeight('bold'|'normal')
Range.setFontLine('underline'|'line-through'|'none')
Range.setHorizontalAlignment('left'|'center'|'right')
Range.setVerticalAlignment('top'|'middle'|'bottom')
Range.setNumberFormat(pattern)        Range.setNumberFormats(String[][])
Range.setBorder(top,left,bottom,right,vertical,horizontal: Boolean)
Range.setBorder(...6x Boolean, color: String, style: BorderStyle)   // BorderStyle.SOLID|SOLID_MEDIUM|DASHED
Range.merge()  .mergeAcross()  .mergeVertically()  .setWrap(bool)
Range.setValues(Object[][])  .setValue(Object)  .getValues(): Object[][]
Range.applyRowBanding()  .applyRowBanding(theme)  .applyRowBanding(theme, showHeader, showFooter): Banding
```
Sheet (rozměry/layout; `setRowHeight`/`setColumnWidth` vrací `Sheet`, `setFrozenRows`/`insertChart` vrací `void`):
```
Sheet.setRowHeight(pos,h)  .setRowHeights(start,num,h)
Sheet.setColumnWidth(pos,w)  .setColumnWidths(start,num,w)  .autoResizeColumn(pos)
Sheet.setHiddenGridlines(bool)  .setFrozenRows(int): void  .setFrozenColumns(int): void
Sheet.setTabColor(color)  .getRange(r,c,nr,nc)  .getDataRange()
Sheet.clear() / clearContents() / clearFormats()
Sheet.newChart(): EmbeddedChartBuilder   .insertChart(chart): void
Sheet.getBandings(): Banding[]   .protect(): Protection
Sheet.insertSlicer(range, anchorRow, anchorCol): Slicer   .getSlicers(): Slicer[]
```
**Banding – barvy JDOU customizovat:** `applyRowBanding(...)` → `Banding` s `setHeaderRowColor()`, `setFirstRowColor()`, `setSecondRowColor()`, `setFooterRowColor()` (+ sloupcové varianty), `setRange(range)`, `remove()`. Varianty `*ColorObject()` berou `Color` místo CSS stringu.

**Conditional formatting:**
```
const rule = SpreadsheetApp.newConditionalFormatRule()
  .whenNumberLessThan(0)        // whenNumberGreaterThan / whenNumberBetween(a,b)
  .whenTextContains(text)       // whenTextEqualTo / whenTextStartsWith / whenCellNotEmpty
  .whenFormulaSatisfied('=A1>B1')
  .setBackground('#F4C7C3')     // setFontColor / setBold(true)
  .setGradientMinpoint(color) / .setGradientMaxpoint(color)   // color scale = heatmapa
  .setRanges([range]).build();
sheet.setConditionalFormatRules([rule]);   // idempotentně: kompletní seznam
```
**Charts (EmbeddedChartBuilder):**
```
const chart = sheet.newChart()
  .setChartType(Charts.ChartType.COLUMN)   // BAR, LINE, PIE, SCATTER...
  .addRange(range).setPosition(anchorRow, anchorCol, offsetX, offsetY)  // 1-indexováno
  .setNumHeaders(1)
  .setOption('title', 'Report 2026')
  .setOption('backgroundColor', 'transparent')   // viz caveat níže
  .build();
sheet.insertChart(chart);
```
`setOption(key, value)` je pass-through do Google Charts configu, NEvaliduje se. **Caveat (jediné neověřené):** transparentní pozadí grafu přes `backgroundColor` string `'transparent'` vs objekt `{ fill: 'transparent' }` je Google Charts config, ne AS signatura → otestovat naostro.

**Data validation (dropdown):**
```
const rule = SpreadsheetApp.newDataValidation()
  .requireValueInList(['A','B','C'])   // requireNumberBetween(0,100) / requireCheckbox()
  .setAllowInvalid(false).setHelpText('Vyber').build();
range.setDataValidation(rule);
```
**Protections (zámek vzorců):** `range.protect()` nebo `sheet.protect()` → `Protection`: `setDescription()`, `setWarningOnly(bool)`, `addEditor(email)`/`removeEditor()`, `setUnprotectedRanges([inputRange])` (u sheet.protect povolené díry). Enum `SpreadsheetApp.ProtectionType.RANGE|SHEET`; čtení `sheet.getProtections(type): Protection[]`.
**Named ranges:** `ss.setNamedRange(name, range): void`, `getRangeByName(name)`, `removeNamedRange(name)`, `getNamedRanges()`.

## 4. Triggery a menu
**Custom menu (simple trigger `onOpen(e)`):**
```
function onOpen(e){ SpreadsheetApp.getUi().createMenu('Report')
  .addItem('Postavit report','buildReport').addToUi(); }
```
Simple trigger omezení: max 30 s, nemůže volat autorizované služby (Gmail, cizí Drive), neběží u read-only otevření, a `setValue` skriptem NEspustí `onEdit`.
**Installable time-driven (mohou volat autorizované služby):**
```
ScriptApp.newTrigger('buildReport').timeBased().everyHours(6).create();
ScriptApp.newTrigger('buildReport').timeBased().onWeekDay(ScriptApp.WeekDay.MONDAY).atHour(9).create();
```
Limity: max 20 triggerů/user/script; běží pod účtem tvůrce. Idempotence: před create smaž existující přes `ScriptApp.getProjectTriggers()` → filtr `getHandlerFunction()` → `ScriptApp.deleteTrigger(t)`.

## 5. Deploy bez copy-paste (clasp)
Instalace `npm install @google/clasp -g` (Node 20+). Zapni „Google Apps Script API" na script.google.com/home/usersettings.
```
clasp login
clasp create --type sheets --title "X"     # nebo --parentId <driveFileId> na existující Sheet
clasp clone <scriptId>
clasp push        # lokál -> projekt
clasp pull        # projekt -> lokál
clasp deploy [version] [desc]
```
Mapování: `.clasp.json` drží `scriptId` (+ volitelně `rootDir`); struktura adresářů se zachová; `.gs`/`.js` se nahrávají jako AS soubory; `appsscript.json` manifest povinný (timeZone, oauthScopes, executionApi). `.clasprc.json` v HOME drží refresh token → do `.gitignore`, nikdy necommitovat.

**`clasp run <fn>`** spouští vzdáleně, ale netriviální setup: (1) `projectId` do `.clasp.json`; (2) vlastní OAuth client Desktop, `clasp login --creds client_secret.json --use-project-scopes`; (3) `appsscript.json` → `"executionApi": { "access": "ANYONE" }`; (4) editor Deploy → New deployment → **API Executable**; (5) všechny scopes v `oauthScopes`. Pro „postav report a skonči" je často jednodušší installable trigger nebo web app (`doGet`) než `clasp run`.

## 6. TOP 10 pastí
1. **1-indexace** `getRange`/pozice grafů, ale 2D pole z `getValues()` je 0-indexované → off-by-one.
2. **`getActiveSheet()` v triggeru/`clasp run`** nemá aktivní UI → otevírej `openById(ID)` + `getSheetByName(NAME)`.
3. **Locale/desetinná čárka** number-format pattern vždy s `.` a `,`, zobrazení dle locale; do buněk piš `Number`, ne string.
4. **Timezone** `new Date()`/`formatDate` dle timezone SKRIPTU (manifest), ne tabulky → předej `'Europe/Prague'` explicitně.
5. **Tiché selhání** obal entry point try/catch + `console.error(e.stack)` + re-throw.
6. **Quota exhaustion** běh >6 min = „Exceeded maximum execution time" → dávkuj + continuation trigger.
7. **`appendRow()` v cyklu** round-trip + flush každé volání → nasbírej do 2D pole a `setValues` jednou.
8. **Full-column rozsahy** → `getDataRange()` nebo přesné rozměry.
9. **Neidempotentní kumulace** push na CF rules, opakovaný `applyRowBanding`, `insertSheet` bez kontroly → duplicity/chyby při 2. běhu.
10. **Chybějící LockService** u paralelních triggerů nad stejným dokumentem → race condition.
Bonus: `setValue` skriptem NEspustí `onEdit`; `insertChart`/`setFrozenRows` vrací `void` (neřetězí).

## 7. Minimální vzor idempotentního styling skriptu
```javascript
// ==== KONFIGURACE (odděleno od dat i logiky) ====
const CFG = {
  SHEET: 'Report',
  HEADER_BG: '#1f3864', HEADER_FG: '#ffffff',
  BAND_FIRST: '#ffffff', BAND_SECOND: '#eef2f7',
  FONT: 'Arial', NUM_FMT: '#,##0.00', TZ: 'Europe/Prague',
  COL_WIDTHS: [220, 120, 120],   // px, 1-indexovaně sloupce 1..n
};

function buildReport() {
  const lock = LockService.getScriptLock();
  lock.waitLock(30000);
  try {
    const ss = SpreadsheetApp.getActiveSpreadsheet();   // v triggeru radši openById(ID)
    const sh = ss.getSheetByName(CFG.SHEET) || ss.insertSheet(CFG.SHEET);  // najdi-nebo-vytvoř

    const data = getReportData_();
    const rows = data.length, cols = data[0].length;

    // 1) DATA jedním batch zápisem
    sh.clearContents();
    sh.getRange(1, 1, rows, cols).setValues(data);

    // 2) FORMÁTOVÁNÍ explicitně = idempotentní
    sh.getRange(1, 1, 1, cols).setBackground(CFG.HEADER_BG).setFontColor(CFG.HEADER_FG)
      .setFontWeight('bold').setHorizontalAlignment('center');
    sh.getRange(2, 1, rows - 1, cols).setFontFamily(CFG.FONT).setVerticalAlignment('middle');
    sh.getRange(2, 2, rows - 1, cols - 1).setNumberFormat(CFG.NUM_FMT);
    sh.getRange(1, 1, rows, cols)
      .setBorder(true, true, true, true, true, true, '#c0c0c0', SpreadsheetApp.BorderStyle.SOLID);
    CFG.COL_WIDTHS.forEach((w, i) => sh.setColumnWidth(i + 1, w));   // 1-indexováno
    sh.setFrozenRows(1);
    sh.setHiddenGridlines(true);

    // 3) BANDING idempotentně: smaž existující (jinak applyRowBanding hodí chybu)
    sh.getBandings().forEach(b => b.remove());
    sh.getRange(1, 1, rows, cols)
      .applyRowBanding(SpreadsheetApp.BandingTheme.LIGHT_GREY, true, false)
      .setHeaderRowColor(CFG.HEADER_BG).setFirstRowColor(CFG.BAND_FIRST).setSecondRowColor(CFG.BAND_SECOND);

    // 4) CONDITIONAL FORMAT idempotentně: kompletní seznam, NE push
    const negRule = SpreadsheetApp.newConditionalFormatRule()
      .whenNumberLessThan(0).setFontColor('#cc0000')
      .setRanges([sh.getRange(2, 2, rows - 1, cols - 1)]).build();
    sh.setConditionalFormatRules([negRule]);

    SpreadsheetApp.flush();
  } catch (e) {
    console.error('buildReport selhal: ' + e.stack);   // Cloud Logging, ne tiché selhání
    throw e;
  } finally {
    lock.releaseLock();
  }
}

function getReportData_() {
  return [
    ['Položka', 'Částka', 'Rozdíl'],
    ['Alfa', 1200.5, -30.0],
    ['Beta', 980.0, 15.25],
  ];   // čísla jako Number, ne string
}

function onOpen() {
  SpreadsheetApp.getUi().createMenu('Report').addItem('Postavit report', 'buildReport').addToUi();
}
```

## Zdroje (oficiální)
best-practices · guides/services/quotas · reference/lock/lock-service · reference/spreadsheet/{range,sheet,spreadsheet,spreadsheet-app,conditional-format-rule-builder,embedded-chart-builder,banding,data-validation-builder,protection} · guides/triggers(+installable) · guides/clasp · github.com/google/clasp/blob/master/docs/run.md (vše developers.google.com/apps-script).
