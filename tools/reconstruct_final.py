"""Deterministically rebuild the FINAL translations.json from saved artifacts:
  Haiku baseline -> Sonnet improvements (QA-gated) -> deterministic §-fixes
  -> haiku markup fixes -> sonnet markup fixes (badness rule) -> bare-% normalize.
"""
import json, os, sys, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import langlib as L, qa, build
from finalize import legit_latin

T = L.entries(L.parse('template.lang'))
base = L.entries(L.parse('ru_RU.original.lang'))
segs = {s['key']: s for s in json.load(open('work/segments.json'))}

def codes(s): return collections.Counter(qa.RE_COLOR.findall(s))
def bare_pct(s): return len(re.findall(r'(?<!%)%(?![%n])', s))
def hard_ok(src, x):
    e = [i['code'] for i in qa.qa_segment(src, x) if i['severity'] == 'error']
    return not (set(e) - {'UNTRANSLATED', 'NO_CYRILLIC'})
def badness(src, x):
    return (1 if codes(x) != codes(src) else 0) + (1 if bare_pct(x) else 0)

# 1) Haiku baseline
trans = dict(json.load(open('work/translations_haiku.json')))
print('haiku baseline:', len(trans))

# 2) Sonnet quality improvements (QA-gated; never regress)
sonnet = json.load(open('work/sonnet_results.json'))
n_son = 0
for r in sonnet:
    k = r.get('id')
    if k not in segs or r.get('verdict') != 'improve' or not r.get('ru'):
        continue
    new = r['ru']
    e = [i['code'] for i in qa.qa_segment(T[k], new) if i['severity'] == 'error']
    ok = (not e) or (set(e) <= {'UNTRANSLATED', 'NO_CYRILLIC'} and legit_latin(T[k]))
    if ok:
        trans[k] = new; n_son += 1
print('sonnet improvements applied:', n_son)

# 3) deterministic §-code fixes (full corrected strings) — ours + originals
mf = json.load(open('work/markup_fixes.json'))
trans.update(mf)
print('deterministic markup fixes:', len(mf))

# 4+5) LLM markup candidates (haiku then sonnet) via badness rule
def apply_candidates(cands):
    n = 0
    for r in cands:
        k, new = r.get('id'), r.get('ru')
        if not k or not new or k not in T:
            continue
        cur = trans.get(k, base.get(k))
        if badness(T[k], new) < badness(T[k], cur) and hard_ok(T[k], new) and bare_pct(new) == 0:
            trans[k] = new; n += 1
    return n

haiku_mk = json.load(open('work/markup_haiku_results.json'))
sonnet_mk = json.load(open('work/markup_sonnet_results.json'))
print('haiku markup accepted:', apply_candidates(haiku_mk))
print('sonnet markup accepted:', apply_candidates(sonnet_mk))

# 6) bare-% -> %%
BARE = re.compile(r'(?<!%)%(?![%n])')
nb = 0
for k, v in list(trans.items()):
    nv = BARE.sub('%%', v)
    if nv != v:
        trans[k] = nv; nb += 1
print('bare-% normalized:', nb)

json.dump(trans, open('work/translations.json', 'w'), ensure_ascii=False)
res = build.build('ru_RU.lang')
print('--- build ---', {k: res[k] for k in ('entries_out', 'dupes', 'missing_inserted', 'overrides_applied')})

# verify markup
out = L.entries(L.parse('ru_RU.lang'))
cm = sum(1 for k in set(T) & set(out) if codes(T[k]) != codes(out[k]))
bp = sum(1 for k in out if bare_pct(out[k]))
print('FINAL §code mismatches:', cm, '| bare-%:', bp)
