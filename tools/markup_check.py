"""Validate that text markup is preserved between English source and translation.

Checks every token class the questbook uses:
  %n  line break          §x  color/format codes      %%  literal percent
  [note]/[warn]/[url]/[quest] tags     [url]...[/url] link body (byte-identical)

Reports, for the assembled file, every segment whose translation does NOT
preserve the source markup, split by whether the value was changed by us or is
an untouched original.

Run: python3 work/markup_check.py [file]   (default ru_RU.lang)
"""
import json, os, sys, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import langlib as L, qa

FILE = sys.argv[1] if len(sys.argv) > 1 else 'ru_RU.lang'
T = L.entries(L.parse('template.lang'))
orig = L.entries(L.parse('ru_RU.original.lang'))
out = L.entries(L.parse(FILE))
ourkeys = set(json.load(open('work/translations.json')))   # values we produced

def tokens(s):
    return {
        '%n': s.count('%n'),
        '%%': s.count('%%'),
        '§codes': dict(qa.color_codes(s)),
        'tags': dict(qa.tags(s)),
        'url_bodies': qa.url_bodies(s),
    }

rows = []
counts = collections.Counter()
for k in sorted(set(T) & set(out)):
    en, ru = T[k], out[k]
    te, tr = tokens(en), tokens(ru)
    probs = []
    if te['%n'] != tr['%n']:
        probs.append(f"%n {tr['%n']}≠{te['%n']}")
    if te['%%'] != tr['%%']:
        probs.append(f"%% {tr['%%']}≠{te['%%']}")
    if te['§codes'] != tr['§codes']:
        probs.append('§codes')
    if te['tags'] != tr['tags']:
        probs.append('tags')
    if te['url_bodies'] != tr['url_bodies']:
        probs.append('url')
    if probs:
        src = 'OURS' if k in ourkeys else 'orig'
        rows.append((src, k, probs))
        for p in probs:
            counts[p.split()[0]] += 1

ours = [r for r in rows if r[0] == 'OURS']
origs = [r for r in rows if r[0] == 'orig']

print(f'=== markup preservation: {FILE} ===')
print(f'segments checked: {len(set(T) & set(out))}')
print(f'markup mismatches total: {len(rows)}  (in OUR translations: {len(ours)}, in untouched originals: {len(origs)})')
print('by token:', dict(counts))
print()
print('--- mismatches in OUR translations (should be ~0 for hard tokens) ---')
for src, k, probs in ours[:60]:
    print(f"  {k.split('betterquesting.')[-1]:48} {probs}")
if len(ours) > 60:
    print(f'  ... +{len(ours)-60} more')

# machine-readable
json.dump([{'src': s, 'key': k, 'problems': p} for s, k, p in rows],
          open('work/markup_report.json', 'w'), ensure_ascii=False)

# hard-token violations in our translations = real defects
hard = [r for r in ours if any(p.startswith('%n') or p == 'tags' or p == 'url'
                               or p.startswith('%%') for p in r[2])]
print()
print(f'HARD-token (%n/tags/url/%%) violations in OUR translations: {len(hard)}')
for s, k, p in hard:
    print(f"  {k.split('betterquesting.')[-1]} {p}")
