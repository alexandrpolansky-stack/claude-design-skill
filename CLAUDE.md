# Instrukce pro práci v tomhle repu

Tohle je knihovna designové znalosti ve second-brain stylu. Čti to celé, než něco přidáš nebo změníš.
Platí pro každého, kdo do repa zapisuje, člověka i Claude.

## Co to je

Knihovna je rozdělená do tematických sekcí v rootu (`neuro-design/`, `ux-design/`, `web-dev/`,
`sheets/`). `skills/` je tenká vrstva, která Claudeovi říká, KDY do knihovny sáhnout a jak se
rozhodovat. Hloubka je vždy v knihovně, nikdy ve skillu.

Vstupní bod je [`_index.md`](_index.md). Nota, která v něm není, prakticky neexistuje, protože
se k ní nikdo nedostane.

## HARD pravidlo: jen grafika a design

**Do repa patří jen znalost o tom, jak něco vypadá, jak se v tom člověk orientuje a jak s tím
interaguje.** Nic jiného.

| Patří sem | Nepatří sem |
|---|---|
| UX zákony, kognitivní zátěž, vnímání | Terraform, IAM, AWS, Lambda |
| Barvy, typografie, layout, mřížky | Jira, HubSpot, BambooHR, Make |
| Komponenty, tlačítka, formuláře, stavy | Python, SQL, DNS, webhooky |
| Landing pages, propagace, prezentace | Firemní procesy, fakturace, onboarding |
| HTML/CSS jako implementace designu | Backend, infra, CI/CD |
| Dataviz, grafy, reporty, tabulky | Slovníky IT pojmů, ops runbooky |

Důvod není čistota složek. Skill funguje tím, že má úzké téma. Kdyby v knihovně byla nota
o Terraformu, `design-advisor` po ní může sáhnout při návrhu tlačítka, a hlavně se rozmaže,
kdy se má skill vůbec spustit. Široká knihovna = horší skill, ne lepší.

Když máš znalost, která sem nepatří, ale je cenná, patří do jiného repa s vlastním skillem.
Nepřidávej ji sem s odůvodněním, že „se to taky někdy hodí".

## Second-brain zásady

Drž se jich, jinak z knihovny bude sklad.

1. **Jedna nota = jedno téma.** Když nota začne vysvětlovat dvě věci, rozděl ji. Radši dvacet
   krátkých not než pět dlouhých, ve kterých se nedá najít odstavec.
2. **Nota musí být užitečná sama.** Kdo ji otevře bez kontextu, pozná, co řeší a kdy ji použít.
   Žádné „viz výše" napříč soubory.
3. **Index je povinný.** Novou notu zapiš do [`_index.md`](_index.md) jednou řádkou: odkaz plus
   jedna věta, čím je nota užitečná při stavbě. Ne obsah, ale důvod ji otevřít.
4. **Odkazuj mezi notami.** Když nota souvisí s jinou, odkaž na ni. Propojená znalost se používá,
   izolovaná zapadne.
5. **Hloubka do knihovny, imperativy do skillu.** Když do `SKILL.md` přiteče teorie, přestane se
   vyplácet ho načítat. Do skillu jde jen rozhodovací postup a tvrdá pravidla.
6. **Zdroj uveď.** U výzkumu, čísla nebo pravidla napiš, odkud je (kniha, studie, URL). Bez zdroje
   se za rok nedá poznat, co je ověřené a co dojem.
7. **Konkrétně, ne obecně.** „Kontrast min. 4.5:1 pro tělo textu" je použitelné. „Dbej na dobrý
   kontrast" není.

## Kam co patří

| Vrstva | Kde | Co tam patří | Co tam NEpatří |
|---|---|---|---|
| Skill | `skills/*/SKILL.md` | Kdy skill spustit, rozhodovací postup, tvrdá pravidla, ukazatele do knihovny | Teorie, dlouhé výčty, historie rozhodnutí |
| Knihovna | `neuro-design/ ux-design/ web-dev/ sheets/` | Hloubka, odůvodnění, příklady, obrázky | Interní cesty, tokeny, jména klientů |
| Pravidlo | `rules/` | Imperativy pro moment psaní kódu | Cokoliv, co není akční u editoru |

Vodítko: co Claude potřebuje vědět, **aby se rozhodl skill použít**, jde do `SKILL.md`.
Co potřebuje vědět, **až už skill používá**, jde do knihovny.

## Jak přidat notu

1. Vyber sekci podle tématu. Novou sekci v rootu zakládej jen tehdy, když v ní budou aspoň tři noty.
2. Ulož notu do tematické podsložky (např. `ux-design/color/`).
3. **Jméno souboru:** ASCII kebab-case, bez diakritiky a mezer (`font-pairing.md`). Obsah česky,
   jméno souboru anglicky. Diakritika a mezery v cestách rozbíjí odkazy na Linuxu a Windows.
4. **Zapiš notu do [`_index.md`](_index.md)** do správné sekce.
5. Když je nota zatím kostra, označ ji v indexu `**[stub]**` a přidej do [`STATUS.md`](STATUS.md).
6. Když nota mění nebo doplňuje tvrdé pravidlo, uprav i příslušný `SKILL.md`. Viz níže.

## Odkazy a obrázky

- **Odkazy relativní markdown**, tedy text v hranatých a cesta v kulatých závorkách, relativně
  ke složce noty. Žádné Obsidian wikilinky `[[...]]`, mimo Obsidian se nerozkliknou.
- **Obrázky** do `_assets/` v dané sekci, jméno taky ASCII kebab-case.
- **Neodkazuj na obrázek, který nenahráváš.** V repu je 97 mrtvých odkazů z prvního importu,
  označených `*[chybějící obrázek: ...]*`. Nepřidávej další. Když ukázka chybí, popiš slovy,
  co měla ukázat, to je použitelnější než prázdné místo.

## Co do repa nesmí

- Klientská data, jména klientů, interní URL, ID projektů.
- Tokeny, klíče, hesla, cesty do Keychainu, obsah `.env`.
- Interní projektové logy a rozhodovací zápisy.
- Materiály třetích stran k dalšímu šíření (kupované e-booky, PDF a scany z kurzů). Poznatky z nich
  ano, přepsané vlastními slovy a s odkazem na zdroj.

Před commitem projdi `git diff --cached`, ať víš, co odesíláš.

## Když měníš tvrdé pravidlo

Domácí pravidla občas jdou proti obecnému výzkumu v knihovně. Příklad, který se tu už jednou
vymstil: obecný dataviz výzkum (Tufte, data-ink ratio) doporučuje v tabulkách skrývat gridlines,
ale domácí pravidlo je nechat je VIDITELNÉ, protože existující reporty je mají a nový list, který
je skryje, vypadá cize.

Skill se tehdy opravil, znalostní báze ne, a půl roku radila opak toho, co skill.

Proto: **když měníš tvrdé pravidlo, oprav obě místa** a v knihovně nech výzkum být, jen nad něj dej
override blok s vysvětlením, proč u nás platí jinak. Výzkum nemaž, jinak se ten spor otevře znovu
bez kontextu. Detail v [`STATUS.md`](STATUS.md), sekce dluhů.

## Ověření před pushem

```bash
# rozbité relativní odkazy mezi soubory
python3 - <<'EOF'
import re, pathlib
bad = []
for p in pathlib.Path('.').rglob('*.md'):
    if '.git/' in str(p): continue
    for m in re.finditer(r'\[[^\]]*\]\(([^)#:]+\.(?:md|png|jpg|jpeg|gif|svg))\)', p.read_text(encoding='utf-8')):
        if not (p.parent / m.group(1)).exists():
            bad.append(f'{p}: {m.group(1)}')
print('\n'.join(bad) if bad else 'odkazy OK')
EOF

# zbylé Obsidian wikilinky (CLAUDE.md a CONTRIBUTING.md je zmiňují v textu, to je OK)
grep -rn "\[\[" --include="*.md" . | grep -vE "^\./(CLAUDE|CONTRIBUTING)\.md"

# validita manifestů
python3 -c "import json;[json.load(open(f)) for f in ['.claude-plugin/marketplace.json','.claude-plugin/plugin.json']];print('JSON OK')"
```

Pak si skill nech načíst a zadej reálný úkol. Když Claude nedojde k tomu, co očekáváš, chyba je
nejčastěji v `description` ve frontmatteru `SKILL.md` (skill se nespustí) nebo v `_index.md`
(nota se nenajde), ne v obsahu noty.

## Struktura je záměrná, neroztahuj ji

Knihovna je v rootu proto, aby byla vidět. Skilly do ní míří relativně (`../../ux-design/`), takže
**repo musí zůstat naklonované celé**. Nekopíruj složku jednoho skillu jinam, přišla by o knihovnu.

## Commity

Conventional commits, anglicky:

```
docs(ux-design): add note on button states and hierarchy
docs(web-dev): document CSS grid basics
fix(sheets): align gridlines guidance with house rule
refactor: split layout-theory into whitespace and margins
```

Typy: `docs` (znalost), `feat` (nový skill nebo schopnost), `fix` (špatná nebo protiřečící si rada),
`refactor` (struktura, přejmenování, dělení not).

Žádná AI atribuce v commitech ani MR. Žádné `Co-Authored-By: Claude`, žádné „Generated with".
