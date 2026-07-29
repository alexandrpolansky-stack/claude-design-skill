# claude-design-skill

Designová znalost jako skilly pro Claude Code. Cíl: když Claude staví cokoliv, co uvidí člověk
(web, komponenta, tlačítko, landing page, propagační materiál, dashboard, report, tabulka, e-mail),
rozhoduje podle znalostní báze, ne ad hoc.

Privátní repo, roste postupně. Mezery a priority: [STATUS.md](STATUS.md).
Jak přidat znalost: [CONTRIBUTING.md](CONTRIBUTING.md).

## Co je vevnitř

| Skill | K čemu | Znalost |
|---|---|---|
| `design-advisor` | Obecné UX/UI pro cokoliv user-facing: weby, komponenty, tlačítka, formuláře, landing pages, propagace, ale i layout tabulky, reportu nebo e-mailu. Model-invoked. | 31 not: UX zákony, barvy, typografie, layout, proces, etika, content strategy, hotový příklad design systému |
| `sheets-design` | Google Sheets reporty a dashboardy, včetně živé aplikace stylů přes Sheets API. Model-invoked. | Rozhodovací rámec otázka→graf, brand tokeny, archetypy reportů, A/B slop→profi, Apps Script vrstva |

Navíc [rules/frontend-ux.md](rules/frontend-ux.md) — path-scoped pravidlo, které se aktivuje
podle typu souboru (`.tsx`, `.css`, ...) místo podle smyslu úkolu. Skill a pravidlo se doplňují:
skill chytá „tohle bude někdo číst", pravidlo chytá „právě píšu UI kód".

## Instalace

```bash
# v Claude Code
/plugin marketplace add git@github.com:<owner>/claude-design-skill.git
/plugin install design-skill
```

Path-scoped pravidlo se pluginem nenainstaluje, zkopíruj ručně:

```bash
cp rules/frontend-ux.md ~/.claude/rules/
```

Ověření: v nové session si nech vypsat skilly, `design-advisor` a `sheets-design` mají být v seznamu.

## Struktura

```
.claude-plugin/marketplace.json     # aby šlo /plugin marketplace add
plugin/
  .claude-plugin/plugin.json
  skills/
    design-advisor/
      SKILL.md                      # destilát + postup, tohle Claude čte první
      references/
        INDEX.md                    # mapa znalosti, odsud se vybírá
        ux-zaklady/ zakony-principy/ color/ typography/ layout/
        proces/ trendy/ logo-foto/ priklady-ds/ zdroje/
        frontend-ux-rules.md
        _assets/                    # obrázky k notám
    sheets-design/
      SKILL.md
      references/
rules/frontend-ux.md                # ke zkopírování do ~/.claude/rules/
STATUS.md                           # co je hotové, co jsou mezery
```

Princip vrstvení: `SKILL.md` je krátký destilát a rozhodovací postup, `references/` drží hloubku.
Claude čte SKILL.md vždy, z `references/` bere jen to, co k úkolu patří. Když do SKILL.md přiteče
teorie, přestane se vyplácet ho načítat.

## Odkud znalost pochází

Noty vznikly jako osobní studijní materiál (UX/design kurzy, Don Norman, Laws of UX, Tufte,
IBM Carbon, NN/G) v Obsidian vaultu. Tenhle repo je jejich kurátorovaná, sdílená verze:
ASCII jména souborů, relativní odkazy místo Obsidian wikilinků, bez interních cest a projektových logů.

**Repo je teď zdroj pravdy pro skilly.** Vault zůstává studijním materiálem. Když upravíš znalost,
uprav ji tady, ne ve vaultu, jinak se to rozejde.

Poznámka ke `sheets-design`: ten jeden skill drží konkrétní firemní brand tokeny (paleta, font),
protože bez nich by rady o Sheets reportech byly obecné až k nepoužitelnosti. Zbytek repa je
značkově neutrální.

## Známé mezery

Znalost je nerovná: část not jsou dvouřádkové kostry a 78 odkazů na obrázky ukazuje na soubory,
které v původním vaultu už nejsou (`*[chybějící obrázek: ...]*` v textu). Nejvíc to bolí u
vizuálních témat (Layout Theory, Typography, Trendy), kde nota byla hlavně komentář k obrázkům.

Úplně nepokryté a přitom potřebné: přístupnost do hloubky, formuláře, prázdné a chybové stavy,
responzivita, motion, design tokens jako proces. Konkrétní seznam: [STATUS.md](STATUS.md).
