"""Aggregate raw extracted term pairs into a canonical glossary.

Input : work/gloss_raw.json   ([{en, ru}] from the extraction workflow)
        work/glossary_seed.json (hand-curated, wins on conflict)
Output: work/glossary.json     (canonical EN -> RU, with frequency)
        work/glossary.md        (human-readable termbase)
"""
import json, os, re, collections
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

raw = json.load(open('work/gloss_raw.json'))
seed = {k: v for k, v in json.load(open('work/glossary_seed.json')).items()
        if not k.startswith('_')}

def norm_en(s):
    return re.sub(r'\s+', ' ', s.strip())

# group ru variants per english key (case-insensitive)
groups = collections.defaultdict(collections.Counter)
display = {}   # lower -> preferred display casing of EN
for t in raw:
    en = norm_en(t.get('en', ''))
    ru = norm_en(t.get('ru', ''))
    if not en or len(en) > 60:
        continue
    low = en.lower()
    groups[low][ru] += 1
    # prefer a capitalized display if any variant is capitalized (proper noun)
    if low not in display or (en[:1].isupper() and not display[low][:1].isupper()):
        display[low] = en

glossary = {}
for low, ruc in groups.items():
    freq = sum(ruc.values())
    ru, _ = ruc.most_common(1)[0]
    en = display[low]
    # keep if recurring (>=2) or proper-noun-ish (capitalized / multiword)
    if freq >= 2 or en[:1].isupper() or ' ' in en:
        glossary[en] = {'ru': ru, 'freq': freq}

# merge seed (override)
for en, ru in seed.items():
    glossary[en] = {'ru': ru, 'freq': glossary.get(en, {}).get('freq', 0), 'seed': True}

# sort: seed first, then by frequency
items = sorted(glossary.items(), key=lambda kv: (not kv[1].get('seed'), -kv[1]['freq'], kv[0].lower()))
glossary = {k: v for k, v in items}
json.dump(glossary, open('work/glossary.json', 'w'), ensure_ascii=False, indent=1)

# compact form for translator prompts: "en => ru" lines
lines = []
for en, v in items:
    ru = v['ru'] if v['ru'] else en  # empty ru means keep latin
    lines.append(f'{en} => {ru}')
open('work/glossary_compact.txt', 'w').write('\n'.join(lines))

with open('work/glossary.md', 'w') as f:
    f.write('# GTNH RU Termbase\n\n| EN | RU | freq | src |\n|---|---|---|---|\n')
    for en, v in items:
        f.write(f"| {en} | {v['ru']} | {v['freq']} | {'seed' if v.get('seed') else ''} |\n")

print(f'raw pairs: {len(raw)} -> canonical terms: {len(glossary)} '
      f'(seed {sum(1 for v in glossary.values() if v.get("seed"))})')
print('top 25 by frequency:')
for en, v in sorted(glossary.items(), key=lambda kv: -kv[1]['freq'])[:25]:
    print(f'  {en:32} -> {v["ru"]:32} ({v["freq"]})')
