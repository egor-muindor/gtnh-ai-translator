"""Generate review_data.json for the translation-review UI.

One record per QUEST (grouped name+desc), including ONLY quests where at least
one field changed (new translation differs from old, or was newly added).
Each record carries English source, old RU, new RU for name and desc, plus the
validation category/severity that triggered the rework.
"""
import json, os, re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

segs = {s['key']: s for s in json.load(open('work/segments.json'))}
new = json.load(open('work/translations.json'))           # our produced values
detail = json.load(open('work/rework_detail.json'))        # mode/issue/category
val = {r['id']: r for r in json.load(open('work/val_rework.json'))}

def base_field(key):
    m = re.match(r'(betterquesting\.(?:quest|questline)\.(.+))\.(name|desc)$', key)
    return (m.group(1), m.group(3)) if m else (key, None)

quests = {}
order = []
for key, s in segs.items():
    base, field = base_field(key)
    if field is None:
        continue
    if base not in quests:
        quests[base] = {'questId': base.split('.')[-1], 'base': base,
                        'name': None, 'desc': None}
        order.append(base)
    old = s['tgt']
    nw = new.get(key, old)            # new value (or unchanged old)
    changed = (key in new) and (nw != old)
    rec = {'en': s['src'], 'old': old or '', 'new': nw or '',
           'changed': bool(changed),
           'category': (detail.get(key, {}).get('category')
                        or val.get(key, {}).get('category') or ''),
           'severity': (detail.get(key, {}).get('severity')
                        or val.get(key, {}).get('severity') or ''),
           'mode': detail.get(key, {}).get('mode', ''),
           'reason': (val.get(key, {}).get('reason')
                      or detail.get(key, {}).get('issue', ''))}
    quests[base][field] = rec

# keep only quests with at least one changed field
out = []
for base in order:
    q = quests[base]
    nch = q['name']['changed'] if q['name'] else False
    dch = q['desc']['changed'] if q['desc'] else False
    if nch or dch:
        out.append(q)

json.dump(out, open('work/review_data.json', 'w'), ensure_ascii=False)
# also copy next to where the app will live
n_name = sum(1 for q in out if q['name'] and q['name']['changed'])
n_desc = sum(1 for q in out if q['desc'] and q['desc']['changed'])
print(f'review records (quests with diffs): {len(out)}')
print(f'  changed names: {n_name} | changed descs: {n_desc}')
