# claude-design-skill

Knihovna designové znalosti, kterou umí Claude použít. Second-brain styl: znalost je rozdělená do
tematických sekcí v rootu, `skills/` je jen tenká vrstva, která Claudeovi říká, kdy do knihovny sáhnout.

**92 not, ~147 000 slov.** Vstupní bod do celé knihovny: [`_index.md`](_index.md).

## Knihovna

| Sekce | Not | O čem |
|---|---|---|
| [neuro-design/](neuro-design/) | 1 | Kognitivní ergonomie, eye-tracking, algoritmy vizuální váhy, fail-safe protokoly. Nejhutnější dokument. |
| [ux-design/](ux-design/) | 51 | UX zákony, proces, barvy, typografie, layout, trendy, etika, hotový design systém, evidence-based pravidla s třídou důkazu, kontext podle sektoru. |
| [enterprise-ui/](enterprise-ui/) | 27 | Produktové aplikace: volba komponenty podle úkolu, vzory, komponenty, klávesnice a čtečky. Principy z IBM Carbonu, bez jeho vizuálu. |
| [web-dev/](web-dev/) | 4 | HTML/CSS základy, vkládání CSS, stylizace textu, práce s obrázky. |
| [sheets/](sheets/) | 3 | Google Sheets reporty: rozhodovací rámec, brand tokeny, Apps Script vrstva. |

## Skilly

| Skill | Kdy se spustí |
|---|---|
| [`design-advisor`](skills/design-advisor/SKILL.md) | Cokoliv user-facing: weby, komponenty, tlačítka, landing pages, propagace, formuláře, ale i layout tabulky, reportu nebo e-mailu. Model-invoked. |
| [`sheets-design`](skills/sheets-design/SKILL.md) | Google Sheets reporty a dashboardy, včetně živé aplikace stylů přes Sheets API. Model-invoked. |

Plus [`rules/`](rules/) – destiláty imperativů pro moment, kdy se reálně píše UI kód. Nejsou to noty
z knihovny, je to zkrácená verze toho, co je v ní rozepsané.

## Jak to používat

### Naklonovat (spolehlivá cesta)

```bash
git clone git@github.com:alexandrpolansky-stack/claude-design-skill.git
```

Skilly čtou knihovnu relativními cestami z `skills/*/` do rootu repa, takže **repo musí být
naklonované celé**. Nekopíruj jen složku jednoho skillu, přišel by o knihovnu.

Aby Claude skilly viděl, nalinkuj celé repo jako plugin dir, nebo si `skills/` nalinkuj do
`~/.claude/skills/` a nech repo na místě:

```bash
ln -s "$(pwd)/skills/design-advisor" ~/.claude/skills/design-advisor
ln -s "$(pwd)/skills/sheets-design"  ~/.claude/skills/sheets-design
```

Path-scoped pravidlo zkopíruj:

```bash
cp rules/frontend-ux.md ~/.claude/rules/
```

### Jako plugin

```bash
/plugin marketplace add git@github.com:alexandrpolansky-stack/claude-design-skill.git
/plugin install design-skill
```

Layout odpovídá konvenci pluginů (`.claude-plugin/` a `skills/` v rootu), ale tuhle instalační
cestu jsem neodzkoušel naostro. Když nezabere, jeď přes klonování výše.

## Struktura

```
_index.md              # MOC, vstupní bod do knihovny
neuro-design/          # kognitivní ergonomie
ux-design/             # UX zákony, barvy, typografie, layout, proces, pravidla, sektory
  _assets/             # obrázky k notám
enterprise-ui/         # produktové aplikace: základy, vzory, komponenty
web-dev/               # HTML/CSS
sheets/                # Google Sheets reporty
skills/
  design-advisor/SKILL.md
  sheets-design/SKILL.md
rules/                 # destiláty pro psaní kódu
.claude-plugin/        # manifest pluginu
STATUS.md              # co je hotové, co jsou mezery
```

Princip vrstvení: `SKILL.md` je krátký destilát a rozhodovací postup, knihovna drží hloubku.
Claude čte SKILL.md vždy, z knihovny bere jen to, co k úkolu patří. Když do SKILL.md přiteče
teorie, přestane se vyplácet ho načítat.

## Odkud znalost pochází

Noty vznikly jako osobní studijní materiál (UX/design kurzy, Don Norman, Laws of UX, Tufte,
IBM Carbon, NN/G) v Obsidian vaultu. Tenhle repo je jejich kurátorovaná, sdílená verze:
ASCII jména souborů, relativní odkazy místo Obsidian wikilinků, bez interních cest a projektových logů.

**Repo je zdroj pravdy pro skilly.** Vault zůstává studijním materiálem. Když upravíš znalost,
uprav ji tady, ne ve vaultu, jinak se to rozejde.

Poznámka ke `sheets/`: ta sekce drží konkrétní firemní brand tokeny (paleta, font), protože bez nich
by rady o Sheets reportech byly obecné až k nepoužitelnosti. Zbytek knihovny je značkově neutrální.

## Známé mezery

Knihovna má **tři vrstvy důvěryhodnosti** a v konfliktu vyhrává vyšší: `ux-design/pravidla/`
a `ux-design/kontext/` (třídy důkazu A) → `enterprise-ui/` (třída B) → zbytek `ux-design/`
a `web-dev/` (původní import studijních poznámek, bez tříd). Noty označené **[archiv]** jsou
studijní materiál nebo téma mimo rozsah a při návrhu se nepoužívají.

Po úklidu 23. 8. 2026 zbývá **24 odkazů na chybějící obrázky** (z 99) a všechny leží v notách
označených **[archiv]**, kde obsah byl právě v těch obrázcích. Dvě noty jsou kostry.

Hotové od původního snímku: evidence-based pravidla s třídou důkazu a sektorový kontext
(`ux-design/pravidla/`, `ux-design/kontext/`), pak přístupnost do hloubky, komponenty a jejich stavy,
formuláře, prázdné a chybové stavy, breakpointy (`enterprise-ui/`).

Pořád nepokryté a přitom potřebné: landing pages jako struktura stránky, dataviz mimo Sheets, design
tokeny jako proces, mobil jako layout strategie (palec zóna, gesta), brand tokeny mimo Sheets.
Konkrétní seznam a priority: [STATUS.md](STATUS.md).

## Přidáváš do knihovny?

Přečti [CLAUDE.md](CLAUDE.md). Je to závazek pro každého, kdo do repa zapisuje, člověka i Claude,
a Claude Code si ho v repu načte sám. Drží dvě věci, na kterých knihovna stojí:

- **Jen grafika a design.** Terraform, Jira, Python ani firemní procesy sem nepatří. Široká knihovna
  neznamená lepší skill, ale horší, protože se rozmaže, kdy se má skill vůbec spustit.
- **Second-brain zásady.** Jedna nota = jedno téma, nota je užitečná sama, každá nota musí být
  zapsaná v [`_index.md`](_index.md), hloubka do knihovny a imperativy do skillu.

Krátká verze: [CONTRIBUTING.md](CONTRIBUTING.md).
