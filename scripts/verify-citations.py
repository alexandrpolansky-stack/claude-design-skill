#!/usr/bin/env python3
"""Ověří, že doslovné citace v notách pořád stojí na uvedené URL.

Použití:
    python3 scripts/verify-citations.py <soubor.md> [...]
    python3 scripts/verify-citations.py $(git ls-files '*.md')

Rozpoznává dva tvary:

1. **ZDROJ:** blok, tedy od `**ZDROJ:` do prázdného řádku. Citace v českých uvozovkách
   smí přetékat přes víc řádků, URL může být holá i v zpětných apostrofech. Blok bez citace
   se hlásí jako BEZ CITACE, u toho se ověřuje jen dostupnost stránky.
2. Jednotlivý řádek, který obsahuje citaci i URL zároveň (řádek markdown tabulky).

Vyžaduje `scrapling` na PATH. Vrací nenulový kód, když něco neprošlo, takže se dá
zapojit před push.

Co to dokáže: chytit přejmenovanou stránku, smazaný odstavec, přeformulované tvrzení
a tiché přesměrování. Co to nedokáže: poznat, že citace nikdy neexistovala. Na to je
jen poctivé první ověření u zdroje.
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CZ_QUOTE = re.compile(r'„([^"]{20,600})"')
URL_IN = re.compile(r'(?:https?://[^\s`,)\]]+|`(?:https?://)?[a-z0-9.-]+\.[a-z]{2,}/[^`\s]*`)')
ZDROJ_START = re.compile(r'^\s*\*\*ZDROJ')

_cache: dict[tuple[str, bool], tuple[str, str]] = {}


def normalize(s: str) -> str:
    """Srovná markdown zvýraznění, odkazy a bílé znaky, ať se porovnává obsah, ne sazba."""
    for _ in range(3):
        s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'[*_`\\]', '', s)
    s = s.replace('’', "'").replace('‘', "'")
    s = s.replace('“', '"').replace('”', '"').replace('„', '"')
    s = s.replace(' ', ' ').replace('‑', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()


def loose(s: str) -> str:
    """Porovnávací tvar: jen písmena a číslice.

    Převod stránky na markdown umí z odkazu `[button groups](#button-groups)` nechat jen
    `#button-groups`. Zahozením interpunkce a mezer se tenhle rozdíl smaže a u citace delší
    než dvacet znaků je riziko náhodné shody zanedbatelné.
    """
    return re.sub(r'[^a-z0-9]', '', normalize(s))


CZ_DIACRITICS = set('áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ')
EN_STOPWORDS = {'the', 'a', 'an', 'of', 'to', 'is', 'are', 'and', 'or', 'in', 'for', 'be',
                'that', 'this', 'with', 'when', 'should', 'not', 'can', 'it', 'as', 'by'}


def is_czech(s: str) -> bool:
    """V českých uvozovkách bývá i křížový odkaz na domácí pravidlo, ne jen citace zdroje.

    Diakritika sama nestačí: „ne spinner v tabulce" ji nemá. Proto se navíc vyžaduje,
    aby se v citaci vyskytlo aspoň jedno anglické funkční slovo.
    """
    if sum(1 for c in s if c in CZ_DIACRITICS) / max(len(s), 1) > 0.01:
        return True
    words = set(re.findall(r'[a-z]+', s.lower()))
    return not (words & EN_STOPWORDS)


def fragments(quote: str) -> list[str]:
    """Rozdělí citaci s vypuštěným místem na části, které musí být na stránce všechny.

    Noty používají „…", „..." nebo „(...)" tam, kde autor vypustil kus originálu.
    Takovou citaci nelze hledat jako jeden řetězec, ale každý úsek zvlášť ano.
    """
    parts = re.split(r'\(\s*\.\.\.\s*\)|\.\.\.|…', quote)
    return [p for p in (x.strip() for x in parts) if len(p) >= 15] or [quote]


def clean_url(raw: str) -> str:
    u = raw.strip('`').rstrip('.,;')
    return u if u.startswith('http') else 'https://' + u


THIN = 3000  # pod tolik znaků to na dokumentační stránce vypadá na nevykreslené SPA


def _pdf_text(url: str) -> str:
    """Stáhne PDF a vrátí jeho text, nebo prázdný řetězec.

    Scrapling na PDF vrací binární obsah, ve kterém žádná citace nikdy nesedne, takže bez
    tohohle kroku se každý PDF zdroj hlásí jako NEDOSTUPNE a citace z něj se neověří vůbec.
    Vyžaduje `pdftotext` z balíku poppler; když chybí, chová se to jako dřív.
    """
    if not shutil.which('pdftotext'):
        return ''
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as fh:
        raw = fh.name
    try:
        got = subprocess.run(['curl', '-sSL', '--max-time', '120', '-o', raw, url],
                             capture_output=True, timeout=180)
        if got.returncode != 0 or Path(raw).stat().st_size == 0:
            return ''
        proc = subprocess.run(['pdftotext', '-layout', raw, '-'],
                              capture_output=True, text=True, timeout=120)
        return proc.stdout or ''
    except (OSError, subprocess.SubprocessError):
        return ''
    finally:
        Path(raw).unlink(missing_ok=True)


def _run(url: str, browser: bool) -> tuple[str, str]:
    with tempfile.NamedTemporaryFile(suffix='.md', delete=False) as fh:
        out = fh.name
    cmd = (['scrapling', 'extract', 'fetch', '--network-idle', '--timeout', '45000', url, out]
           if browser else ['scrapling', 'extract', 'get', url, out])
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        m = re.search(r'<GET (\S+)>', proc.stderr or '')
        return Path(out).read_text(encoding='utf-8', errors='replace'), (m.group(1) if m else url)
    except (OSError, subprocess.SubprocessError):
        return '', url
    finally:
        Path(out).unlink(missing_ok=True)


def fetch(url: str, browser: bool = False) -> tuple[str, str]:
    """Vrátí (text stránky, cílová URL). Prázdný text znamená, že se stáhnout nepodařilo.

    Dvoustupňově: nejdřív prostý požadavek, a když vrátí podezřele málo, ještě prohlížeč.
    Dokumentace Atlassianu, Apple HIG a spol. se skládá až v prohlížeči, prostý požadavek
    na ní vrátí skořápku bez obsahu.
    """
    key = (url, browser)
    if key in _cache:
        return _cache[key]
    if url.lower().split('?')[0].endswith('.pdf'):
        text = _pdf_text(url)
        _cache[key] = (text, url)
        return text, url
    text, final = _run(url, browser)
    if not browser and len(text) < THIN:
        text2, final2 = _run(url, True)
        if len(text2) > len(text):
            text, final = text2, final2
    _cache[key] = (text, final)
    return text, final


def units(lines: list[str]):
    """Vrátí (cislo_radku, text) pro každou jednotku k ověření."""
    i = 0
    while i < len(lines):
        if ZDROJ_START.match(lines[i]):
            start = i
            buf = []
            while i < len(lines) and lines[i].strip():
                buf.append(lines[i])
                i += 1
            yield start + 1, ' '.join(buf)
        else:
            if CZ_QUOTE.search(lines[i]) and URL_IN.search(lines[i]):
                yield i + 1, lines[i]
            i += 1


def check(path: Path) -> tuple[int, int]:
    problems = 0
    checked = 0
    for lineno, text in units(path.read_text(encoding='utf-8').splitlines()):
        urls = [clean_url(u) for u in URL_IN.findall(text)]
        # odkazy na jiné noty v repu neověřujeme, to dělá kontrola mrtvých odkazů
        urls = [u for u in urls if not u.endswith('.md')]
        quotes = [q for q in CZ_QUOTE.findall(text) if not is_czech(q)]
        if not urls:
            continue
        pages = [fetch(u) for u in urls]
        if not quotes:
            dead = [u for u, (p, _) in zip(urls, pages) if not p]
            tag = 'NEDOSTUPNE' if dead else 'BEZ CITACE'
            if dead:
                problems += 1
            print(f'  {tag:<11} {path.name}:{lineno}  {(dead or urls)[0]}')
            continue
        blob = ' || '.join(loose(p) for p, _ in pages)
        retried = False
        for q in quotes:
            checked += 1
            if not blob.strip():
                print(f'  NEDOSTUPNE  {path.name}:{lineno}  {urls[0]}')
                problems += 1
                continue
            if not all(loose(f) in blob for f in fragments(q)) and not retried:
                # druhy pokus pres prohlizec, nez nalez vydame za posun ve zdroji
                retried = True
                pages = [fetch(u, browser=True) for u in urls]
                blob = ' || '.join(loose(p) for p, _ in pages)
            if all(loose(f) in blob for f in fragments(q)):
                moved = [f for (p, f), u in zip(pages, urls)
                         if p and f.rstrip('/') != u.rstrip('/')]
                note = f'  (presmerovano: {moved[0]})' if moved else ''
                print(f'  OK          {path.name}:{lineno}  {q[:54]}...{note}')
            else:
                print(f'  CITACE PRYC {path.name}:{lineno}  {urls[0]}')
                print(f'              hledano: {q[:110]}')
                problems += 1
    return checked, problems


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit(2)
    tot_c = tot_p = 0
    for arg in sys.argv[1:]:
        c, p = check(Path(arg))
        tot_c += c
        tot_p += p
    print(f'\nCelkem: overeno {tot_c} citaci, problemu {tot_p}')
    raise SystemExit(1 if tot_p else 0)
