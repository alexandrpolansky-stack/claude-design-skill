---
name: design-advisor
description: >-
  Sáhni pro UX/UI/vizuální design znalost při návrhu nebo stavbě ČEHOKOLIV, co
  uvidí nebo použije člověk. Nejen weby a appky (UI, komponenty, dashboardy, formuláře, landing
  pages), ale i produktové a enterprise aplikace (CRUD, administrace, datové tabulky, filtrování,
  notifikace, vícekrokové formuláře, klávesová obsluha, čtečky), ALE i ne-webové výstupy: layout
  tabulky nebo Google Sheetu pro automatizaci, report,
  přehled, e-mailová šablona, struktura dokumentu. Spouštěj PROAKTIVNĚ a sám (model-invoked),
  kdykoliv úkol řeší, jak něco vypadá, jak se v tom člověk orientuje, nebo jak s tím interaguje -
  i když to uživatel neřekne výslovně. Cíl: rozhodnutí o designu mají oporu ve znalostní bázi
  (UX zákony, barvy, typografie, layout, přístupnost), ne ad hoc. Spojuj úkol se souvislostmi:
  kdo je čtenář/uživatel, jaký má cíl, co má být na první pohled jasné.
---

# Design advisor

Když navrhuju cokoliv user-facing, nejdřív si vytáhnu relevantní znalost, ať rozhodnutí nejsou nahodilá. Platí i na tabulky a sheety, ne jen weby.

## Zdroj znalosti

Knihovna žije v rootu repa, ne uvnitř skillu. Cesty níže jsou relativní ze složky skillu,
což platí, když je repo naklonované celé. Kdyby relativní cesta neexistovala (skill
nakopírovaný samostatně), najdi `_index.md` v rootu repa `claude-design-skill` a jdi odtud.
[../../_index.md](../../_index.md) – mapa celé knihovny (86 not v pěti sekcích: neuro-design, ux-design, enterprise-ui, web-dev, sheets). Otevři index, vyber relevantní sekce a přečti je. Nečti celý index dokola; vezmi jen to, co k úkolu patří, a odkaž na konkrétní notu.

## Postup
1. **Souvislosti první:** čí je to výstup, kdo ho čte/používá, jaký je jeho cíl, co má být hned jasné, jaký je hlavní flow.
2. **Vytáhni relevantní sekci** z indexu (UX zákony, barvy, typografie, layout, proces, příklad DS).
   U netriviální stavby UI přečti navíc [neuro-design master](../../neuro-design/neuro-design-master.md):
   vizuální váha prvků, F/Z-pattern, kognitivní zátěž, diagnostika chyb. Je to nejhutnější dokument v knihovně.
3. **Stavíš produktovou aplikaci?** (dashboard, CRUD, administrace, interní nástroj, cokoliv
   s datovou tabulkou, filtry, vícekrokovým formulářem nebo notifikacemi.) Pak jdi do
   [enterprise-ui/](../../enterprise-ui/), ne jen do `ux-design/`. Pořadí čtení:
   - [Volba komponenty](../../enterprise-ui/zaklady/volba-komponenty.md) nejdřív. Rozhodovací
     tabulky úkol → prvek, ať nevybíráš komponentu podle vzhledu.
   - Pak konkrétní nota ze `vzory/` nebo `komponenty/` podle toho, co stavíš.
   - [Klávesnice a focus](../../enterprise-ui/zaklady/klavesnice-a-focus.md) a
     [Oznámení pro čtečky](../../enterprise-ui/zaklady/oznameni-pro-ctecky.md) vždy, když píšeš
     vlastní interaktivní komponentu.
   - [Mřížka a breakpointy](../../enterprise-ui/zaklady/2x-grid-a-breakpointy.md) na rozvržení.

   **Konflikty:** `enterprise-ui/` je odvozené z IBM Carbonu, tedy třída **B** (publikovaná
   konvence design systému). Když si odporuje s `ux-design/pravidla/` (třídy A: WCAG, měření,
   peer-reviewed), **vyhrává `ux-design/pravidla/`**. Konkrétní rozpory jsou vypsané v
   [STATUS.md](../../STATUS.md), sekce 0. Z Carbonu nikdy neber tokeny, hex hodnoty, IBM Plex ani
   elevation škály: přebíráme principy, ne vizuál.
4. **Aplikuj základ** (i na tabulky/sheety/reporty, ne jen UI):
   - Hierarchie a seskupování (Gestalt, blízkost): související sloupce/sekce u sebe, oddělené whitespacem nebo oddělovačem.
   - Hick + Miller: neděs člověka 30 sloupci najednou; seskup do logických bloků po 5-9.
   - Konzistence a afordance: stejné věci vypadají stejně; jasné záhlaví, čitelné popisky.
   - Barvy 60-30-10 + sémantika; stav nikdy jen barvou (přidej text/ikonu).
   - Typografie a čitelnost; kontrast WCAG min. 4.5:1.
   - U interaktivního UI navíc: zpětná vazba na akce, viditelný focus, ovladatelnost klávesnicí.
5. **U větší stavby** projdi proces (uživatel → cíl → flow → wireframe): [step-by-step-ux-ui](../../ux-design/proces/step-by-step-ux-ui.md).
6. **Hotový příklad** design systému s konkrétními tokeny: [design-system-drive](../../ux-design/priklady-ds/design-system-drive.md).
7. **Když píšeš UI kód**, drž se destilátu [rules/frontend-ux-detailed.md](../../rules/frontend-ux-detailed.md)
   a implementačních not v [web-dev/](../../web-dev/).

## Vztah k ostatním vrstvám
- Tento skill = trigger podle SMYSLU úkolu (i bez frontend souboru).
- `rules/frontend-ux.md` (root repa, ke zkopírování do `~/.claude/rules/`) = trigger podle TYPU souboru (`.tsx`/`.css`...). Doplňují se.
- `sheets-design` = Sheets-specifická implementace v TrustSoft brandu. Na Sheets použij ten.
- Hloubka je vždy v knihovně v rootu repa (`neuro-design/`, `ux-design/`, `enterprise-ui/`,
  `web-dev/`, `sheets/`), v SKILL.md i v pravidle je jen destilát.
