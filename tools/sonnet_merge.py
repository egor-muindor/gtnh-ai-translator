"""Merge Sonnet second-tier improvements over the Haiku baseline, QA-gated.

A Sonnet 'improve' is accepted only if it passes the QA gate; otherwise we keep
the QA-passing Haiku version (never regress).

Input : work/sonnet_results.json ([{id, verdict, ru?, note?}])
        work/translations_haiku.json (Haiku baseline, all QA-passing)
Output: work/translations.json (final), ru_RU.lang, work/sonnet_diff.json
"""
import json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import qa, build
from finalize import legit_latin

segs = {s['key']: s for s in json.load(open('work/segments.json'))}
haiku = json.load(open('work/translations_haiku.json'))
sonnet = json.load(open('work/sonnet_results.json'))

final = dict(haiku)            # start from Haiku baseline
accepted, rejected, kept = [], [], 0
diff = []

for r in sonnet:
    k = r.get('id')
    if k not in segs:
        continue
    if r.get('verdict') != 'improve' or not r.get('ru'):
        kept += 1
        continue
    new = r['ru']
    src = segs[k]['src']
    issues = qa.qa_segment(src, new)
    errs = [i for i in issues if i['severity'] == 'error']
    ok = (not errs) or (set(i['code'] for i in errs) <= {'UNTRANSLATED', 'NO_CYRILLIC'}
                        and legit_latin(src))
    if ok:
        if new != haiku.get(k):
            diff.append({'id': k, 'haiku': haiku.get(k, ''), 'sonnet': new,
                         'note': r.get('note', '')})
        final[k] = new
        accepted.append(k)
    else:
        rejected.append({'id': k, 'issues': [i['code'] for i in errs]})

json.dump(final, open('work/translations.json', 'w'), ensure_ascii=False)
json.dump(diff, open('work/sonnet_diff.json', 'w'), ensure_ascii=False)
json.dump(rejected, open('work/sonnet_rejected.json', 'w'), ensure_ascii=False)

print(f'sonnet reviewed: {len(sonnet)}')
print(f'  kept (verdict=keep): {kept}')
print(f'  improvements accepted: {len(accepted)} (actually changed text: {len(diff)})')
print(f'  improvements rejected by QA (fell back to Haiku): {len(rejected)}')
if rejected:
    print('  reject codes:', dict(collections.Counter(c for x in rejected for c in x['issues'])))

res = build.build('ru_RU.lang')
print('--- build ---')
for k, v in res.items():
    print(f'  {k}: {v}')
