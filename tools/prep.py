"""Build the CAT working environment from template.lang + ru_RU.original.lang.

Produces under work/:
  segments.json   ordered bilingual segment store (the project's source of truth)
  tm.json         translation memory: clean EN->RU pairs (style + exact-match reuse)
  sets.json       key lists per working set (good / qa_broken / suspect / missing / obsolete)
Run: python3 work/prep.py
"""
import json, re, os, collections
import langlib as L
import qa

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

ti = L.parse('template.lang')
ri = L.parse('ru_RU.original.lang')
T = L.entries(ti)   # en
R = L.entries(ri)   # ru

# quest/questline id -> english name, for context attachment
def base_and_field(key):
    # betterquesting.quest.<ID>.name  /  .desc
    m = re.match(r'(betterquesting\.(?:quest|questline)\.(.+))\.(name|desc)$', key)
    if not m:
        return None, None, None
    return m.group(1), m.group(2), m.group(3)  # base, id, field

en_name = {}   # base -> english name
for k, v in T.items():
    base, _id, field = base_and_field(k)
    if field == 'name':
        en_name[base] = v

shared = set(T) & set(R)
only_t = sorted(set(T) - set(R))     # missing in ru
only_r = sorted(set(R) - set(T))     # obsolete

segments = []          # ordered by template position, then any ru-only extras
sets = {'good': [], 'qa_broken': [], 'suspect': [], 'missing': [], 'obsolete': only_r}
tm = []

seen = set()
# iterate in TEMPLATE order so segment store is canonical & complete
for it in ti:
    if it['kind'] != 'entry':
        continue
    k = it['key']
    base, _id, field = base_and_field(k)
    src = T[k]
    tgt = R.get(k)
    ctx = en_name.get(base, '')
    if k in shared:
        status, issues = qa.classify(src, tgt)
        qa_status = {'clean': 'good', 'broken': 'qa_broken', 'suspect': 'suspect'}[status]
        seg = {'key': k, 'field': field, 'src': src, 'tgt': tgt, 'ctx': ctx,
               'qa_status': qa_status, 'issues': [i['code'] for i in issues]}
        sets[qa_status].append(k)
        if qa_status == 'good':
            tm.append({'key': k, 'field': field, 'en': src, 'ru': tgt})
    else:
        seg = {'key': k, 'field': field, 'src': src, 'tgt': None, 'ctx': ctx,
               'qa_status': 'missing', 'issues': ['MISSING']}
        sets['missing'].append(k)
    segments.append(seg)
    seen.add(k)

# ru-only obsolete keys appended for completeness (kept in final via base file)
for k in only_r:
    base, _id, field = base_and_field(k)
    segments.append({'key': k, 'field': field, 'src': None, 'tgt': R[k], 'ctx': '',
                     'qa_status': 'obsolete', 'issues': ['OBSOLETE']})

json.dump(segments, open('work/segments.json', 'w'), ensure_ascii=False)
json.dump(sets, open('work/sets.json', 'w'), ensure_ascii=False)
json.dump(tm, open('work/tm.json', 'w'), ensure_ascii=False)

print('segments:', len(segments))
for k, v in sets.items():
    print(f'  {k}: {len(v)}')
print('TM (clean pairs):', len(tm))
# review set for Haiku = good + suspect (linguistic judgment); qa_broken auto-flagged
print('Haiku review set (good+suspect):', len(sets['good']) + len(sets['suspect']))
print('Translate set so far (qa_broken+missing):', len(sets['qa_broken']) + len(sets['missing']))
