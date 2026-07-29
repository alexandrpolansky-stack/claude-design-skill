# Jak přidat nebo upravit znalost

Repo je zdroj pravdy pro skilly. Neupravuj obsah v Obsidian vaultu a nečekej, že se to propíše.

## Kam co patří

Tři vrstvy, každá má jinou roli. Když se to smíchá, skill se přestane vyplácet načítat.

| Vrstva | Soubor | Co tam patří | Co tam NEpatří |
|---|---|---|---|
| Skill | `skills/*/SKILL.md` | Kdy skill spustit, rozhodovací postup, tvrdá pravidla, ukazatele do references | Teorie, dlouhé výčty, historie rozhodnutí |
| Znalost | `neuro-design/ ux-design/ web-dev/ sheets/` | Hloubka, odůvodnění, příklady, obrázky | Interní cesty, tokeny, jména klientů |
| Pravidlo | `rules/frontend-ux.md` | Imperativy pro moment psaní kódu | Cokoliv, co není akční u editoru |

Praktické vodítko: když to Claude potřebuje vědět, **aby se rozhodl skill použít**, jde to do
SKILL.md. Když to potřebuje vědět, **až už skill používá**, jde to do references.

## Přidání nové noty

1. Ulož do tematické podsložky v `ux-design/`.
   Nová podsložka jen když tam budou aspoň dvě noty.
2. **Jméno souboru:** ASCII kebab-case, bez diakritiky a mezer (`font-pairing.md`).
   Obsah česky, jméno souboru anglicky. Diakritika v cestách rozbíjí odkazy na jiných OS.
3. **Zapiš do [_index.md](_index.md)** jednou řádkou:
   odkaz + popis do jedné věty, čím ta nota je užitečná při stavbě. Nota, která není v indexu,
   se nenajde.
4. Když je nota zatím kostra, označ ji v indexu `**[stub]**` a přidej do [STATUS.md](STATUS.md).

## Odkazy a obrázky

- **Odkazy relativní markdown**, tedy text v hranatých a cesta v kulatých závorkách
  (`layout/layout-theory.md` relativně ke složce noty).
  Žádné Obsidian wikilinky `[[...]]` - mimo Obsidian se nerozkliknou.
- **Obrázky** do `references/_assets/`, jméno taky ASCII kebab-case.
  Mapování na původní jména z vaultu drží [`ux-design/_assets/README.md`](ux-design/_assets/README.md).
- Neodkazuj na obrázek, který nenahráváš. Když ukázka chybí, radši popiš slovy, co měla ukázat.

## Co do repa nesmí

- Klientská data, jména klientů, interní URL, ID projektů.
- Tokeny, klíče, hesla, cesty do Keychainu, obsah `.env`.
- Interní projektové logy a rozhodovací zápisy (ty zůstávají ve vaultu).
- Materiály třetích stran k dalšímu šíření (kupované e-booky, PDF z kurzů). Poznatky z nich ano,
  přepsané vlastními slovy a s odkazem na zdroj.

Před commitem projdi `git diff --cached`, ať víš, co odesíláš.

## Když měníš tvrdé pravidlo

Domácí pravidla (např. gridlines v Sheets zůstávají viditelné) občas jdou proti obecnému výzkumu
v references. Když takové pravidlo měníš, **oprav obě místa** - SKILL.md i znalostní bázi. Historicky
se tohle rozešlo a báze pak radila opak toho, co skill; viz [STATUS.md](STATUS.md) sekci 4.

## Commity

Conventional commits, anglicky:

```
docs(design-advisor): add accessibility note on focus management
fix(sheets-design): align gridlines guidance with house rule
```

Typy, které tu dávají smysl: `docs` (znalost), `feat` (nový skill nebo schopnost),
`fix` (špatná nebo protiřečící si rada), `chore` (struktura, přejmenování).

Žádná AI atribuce v commitech ani MR.

## Ověření před pushem

Skilly nemají testy, ale tohle projdi:

```bash
# rozbité relativní odkazy mezi markdown soubory
python3 - <<'EOF'
import re, pathlib
bad = []
for p in pathlib.Path('.').rglob('*.md'):
    for m in re.finditer(r'\[[^\]]*\]\(([^)#:]+\.(?:md|png|jpg|jpeg|gif|svg))\)', p.read_text(encoding='utf-8')):
        if not (p.parent / m.group(1)).exists():
            bad.append(f'{p}: {m.group(1)}')
print('\n'.join(bad) if bad else 'odkazy OK')
EOF

# zbylé Obsidian wikilinky
grep -rn "\[\[" --include="*.md" . || echo "wikilinky OK"
```

Pak si v Claude Code nech skill načíst a zadej reálný úkol. Když Claude nedojde k tomu, co
očekáváš, chyba je nejčastěji v `description` ve frontmatteru (skill se nespustí) nebo v INDEXu
(nota se nenajde), ne v obsahu noty.
