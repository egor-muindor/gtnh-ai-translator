"""Merge LLM markup-repair results, accepting a candidate ONLY if it strictly
reduces markup badness without regressing.

badness(value) = (§codes != source ? 1 : 0) + (has bare single % ? 1 : 0)

%% COUNT parity is intentionally NOT part of badness: a literal %% is content
(a percent sign), and the Russian may legitimately use % where English spells
"percent". The only %%-related defect is a BARE single % (invalid in .lang).
"""
import json, os, sys, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import langlib as L, qa

T = L.entries(L.parse('template.lang'))
trans = json.load(open('work/translations.json'))
base = L.entries(L.parse('ru_RU.original.lang'))
mk = json.load(open('work/markup_llm_results.json'))

def codes(s): return collections.Counter(qa.RE_COLOR.findall(s))
def bare_pct(s): return len(re.findall(r'(?<!%)%(?![%n])', s))
def badness(src, x):
    return (1 if codes(x) != codes(src) else 0) + (1 if bare_pct(x) else 0)
def hard_ok(src, x):
    e = [i['code'] for i in qa.qa_segment(src, x) if i['severity'] == 'error']
    return not (set(e) - {'UNTRANSLATED', 'NO_CYRILLIC'})

accepted, rejected = 0, []
for r in mk:
    k, new = r.get('id'), r.get('ru')
    if not k or not new or k not in T:
        continue
    src = T[k]
    cur = trans.get(k, base.get(k))
    if badness(src, new) < badness(src, cur) and hard_ok(src, new) and bare_pct(new) == 0:
        trans[k] = new
        accepted += 1
    else:
        rejected.append(k)

json.dump(trans, open('work/translations.json', 'w'), ensure_ascii=False)
print(f'markup fixes accepted (strict improvement): {accepted} | not accepted: {len(rejected)}')

import build
res = build.build('ru_RU.lang')
print('rebuilt:', res['entries_out'], 'entries, dupes', res['dupes'])
