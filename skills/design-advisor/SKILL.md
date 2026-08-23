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
[../../_index.md](../../_index.md) - mapa celé knihovny (91 not v pěti sekcích: neuro-design, ux-design, enterprise-ui, web-dev, sheets). Otevři index, vyber relevantní sekce a přečti je. Nečti celý index dokola; vezmi jen to, co k úkolu patří, a odkaž na konkrétní notu.

## Postup
1. **Souvislosti první:** čí je to výstup, kdo ho čte/používá, jaký je jeho cíl, co má být hned jasné, jaký je hlavní flow.
2. **Vytáhni relevantní sekci** z indexu (UX zákony, barvy, typografie, layout, proces, příklad DS).
   U netriviální stavby UI přečti navíc [neuro-design master](../../neuro-design/neuro-design-master.md):
   vizuální váha prvků, F/Z-pattern, kognitivní zátěž, diagnostika chyb. Je to jediné místo v knihovně
   s explicitní metodikou vizuální hierarchie, ale je ve vrstvě 3 a nemá u tvrzení zdroje.
   **Ber z něj metodiku, ne čísla** (má nahoře blok „Jak tuhle notu číst" s výčtem toho, co v něm neplatí).
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

   **Konflikty:** knihovna má tři vrstvy důvěryhodnosti a v konfliktu vyhrává ta vyšší:
   1. `ux-design/pravidla/` a `ux-design/kontext/` (třídy A: WCAG, měření, peer-reviewed)
   2. `enterprise-ui/` (třída B, publikovaná konvence design systému, odvozeno z IBM Carbonu)
   3. zbytek `ux-design/`, celý `neuro-design/` a `web-dev/` (původní import studijních poznámek,
      **bez třídy důkazu**)

   `sheets/` stojí vedle škály: domácí pravidla, pro Sheets platí přednostně.

   Noty ve třetí vrstvě jsou často užitečné, ale nikdy nepřebíjejí první dvě, a noty označené
   v indexu **[archiv]** nepoužívej při návrhu vůbec. Konkrétní rozpory jsou vypsané v
   [STATUS.md](../../STATUS.md), sekce 0. Z Carbonu nikdy neber tokeny, hex hodnoty, IBM Plex ani
   elevation škály: přebíráme principy, ne vizuál.
4. **Aplikuj základ** (i na tabulky/sheety/reporty, ne jen UI):
   - Hierarchie a seskupování (Gestalt, blízkost): související sloupce/sekce u sebe, oddělené whitespacem nebo oddělovačem.
   - Hick + Miller: neděs člověka 30 sloupci najednou; seskup do logických bloků po 5-9.
   - Konzistence a afordance: stejné věci vypadají stejně; jasné záhlaví, čitelné popisky.
   - Barvy 60-30-10 + sémantika; stav nikdy jen barvou (přidej text/ikonu).
   - Typografie a čitelnost; kontrast WCAG min. 4.5:1.
   - U interaktivního UI navíc: zpětná vazba na akce, viditelný focus, ovladatelnost klávesnicí.
5. **U větší stavby** projdi proces sám, protože knihovna na něj úplnou notu nemá:
   kdo je uživatel → jaký má cíl → jakou cestou se k němu dostane → co je na které obrazovce →
   teprve pak vzhled. [Step by step](../../ux-design/proces/step-by-step-ux-ui.md) k tomu dá přehled
   21 kroků a materiál k user flow diagramu, ale je **[neúplné]**: rozvedené má jen user flow
   a wireframy a druhá sekce se láme uprostřed. Neber ji jako návod ke krokům, které nepopisuje.
6. **Hotový příklad** design systému s konkrétními tokeny: [design-system-drive](../../ux-design/priklady-ds/design-system-drive.md).
7. **Když píšeš UI kód**, drž se destilátu [rules/frontend-ux-detailed.md](../../rules/frontend-ux-detailed.md).
   Implementační pasti, které mlčky nezaberou (zkracování, `min-width: 0`, stacking context,
   `sticky` pod `overflow`, stabilita layoutu při změně dat), jsou v
   [enterprise-ui/vzory/](../../enterprise-ui/vzory/) a jsou třída A ze specifikace.
   [web-dev/](../../web-dev/) je úvodní materiál k HTML a CSS z původního importu, ne referenční
   příručka: sahej po něm jen na základy, ne na řešení konkrétního problému.

## Vztah k ostatním vrstvám
- Tento skill = trigger podle SMYSLU úkolu (i bez frontend souboru).
- `rules/frontend-ux.md` (root repa, ke zkopírování do `~/.claude/rules/`) = trigger podle TYPU souboru (`.tsx`/`.css`...). Doplňují se.
- `sheets-design` = Sheets-specifická implementace v TrustSoft brandu. Na Sheets použij ten.
- Hloubka je vždy v knihovně v rootu repa (`neuro-design/`, `ux-design/`, `enterprise-ui/`,
  `web-dev/`, `sheets/`), v SKILL.md i v pravidle je jen destilát.
