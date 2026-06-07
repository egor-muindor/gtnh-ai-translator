"""Build rework_detail.json: per-key translation mode (fresh vs fix) + issue note.

fresh = retranslate from English (existing ru is garbage/missing/badly wrong)
fix   = minimally correct the existing ru, preserving its good wording
"""
import json, os, collections
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sets = json.load(open('work/sets.json'))
val = {r['id']: r for r in json.load(open('work/val_rework.json'))}
segs = {s['key']: s for s in json.load(open('work/segments.json'))}

FRESH_MAJOR_CATS = {'mistranslation', 'untranslated', 'mixed_language',
                    'fluency', 'terminology', 'register', 'other'}

detail = {}

# deterministic-broken -> always fresh
for k in sets['qa_broken']:
    detail[k] = {'mode': 'fresh', 'issue': 'QA: ' + ','.join(segs[k]['issues']),
                 'severity': 'major', 'category': 'garbage_mt'}

# missing -> fresh (no existing translation)
for k in sets['missing']:
    detail[k] = {'mode': 'fresh', 'issue': 'missing translation',
                 'severity': 'major', 'category': 'missing'}

# llm-flagged
reviewed = set(sets['good']) | set(sets['suspect'])
for k, r in val.items():
    if k not in reviewed:
        continue
    sev = r.get('severity', 'major')
    cat = r.get('category', 'other')
    if sev == 'major' and cat in FRESH_MAJOR_CATS:
        mode = 'fresh'
    else:
        mode = 'fix'
    detail[k] = {'mode': mode, 'issue': r.get('reason', ''),
                 'severity': sev, 'category': cat}

json.dump(detail, open('work/rework_detail.json', 'w'), ensure_ascii=False)
json.dump(sorted(detail), open('work/rework_keys.json', 'w'), ensure_ascii=False)

modes = collections.Counter(v['mode'] for v in detail.values())
print('total rework:', len(detail))
print('by mode:', dict(modes))
fields = collections.Counter(segs[k]['field'] for k in detail)
print('by field:', dict(fields))
