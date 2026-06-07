"""Aggregate validation verdicts + deterministic QA into the rework list & report.

Input : work/val_rework.json  ([{id,severity,category,reason}] from validation wf)
        work/sets.json, work/segments.json
Output: work/rework_keys.json (keys to (re)translate, excluding the 388 missing)
        work/report.md          (human-readable validation report)
"""
import json, os, collections
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

val_rework = json.load(open('work/val_rework.json'))
sets = json.load(open('work/sets.json'))
segs = {s['key']: s for s in json.load(open('work/segments.json'))}

qa_broken = set(sets['qa_broken'])
missing = set(sets['missing'])
reviewed = set(sets['good']) | set(sets['suspect'])

# llm rework, filtered to actually-reviewed ids
llm = {r['id']: r for r in val_rework if r['id'] in reviewed}
llm_rework = set(llm)

# full rework set = deterministic-broken ∪ llm-flagged  (missing handled separately)
rework = (qa_broken | llm_rework)
json.dump(sorted(rework), open('work/rework_keys.json', 'w'), ensure_ascii=False)

# --- report -------------------------------------------------------------
cat = collections.Counter()
sev = collections.Counter()
for k in llm_rework:
    cat[llm[k].get('category', 'other')] += 1
    sev[llm[k].get('severity', 'major')] += 1

with open('work/report.md', 'w') as f:
    f.write('# GTNH ru_RU.lang — Validation Report\n\n')
    f.write('## Summary\n\n')
    f.write(f'- Total segments (template): {len(segs)}\n')
    f.write(f'- Good (passed automated QA): {len(sets["good"])}\n')
    f.write(f'- Suspect (QA warnings, sent to LLM review): {len(sets["suspect"])}\n')
    f.write(f'- Auto-flagged broken by deterministic QA: {len(qa_broken)}\n')
    f.write(f'- LLM-reviewed (good+suspect): {len(reviewed)}\n')
    f.write(f'  - kept: {len(reviewed) - len(llm_rework)}\n')
    f.write(f'  - flagged for rework: {len(llm_rework)}\n')
    f.write(f'- **Total to (re)translate: {len(rework)}** + {len(missing)} missing = {len(rework)+len(missing)}\n\n')
    f.write('### LLM rework by category\n\n')
    for c, n in cat.most_common():
        f.write(f'- {c}: {n}\n')
    f.write('\n### LLM rework by severity\n\n')
    for c, n in sev.most_common():
        f.write(f'- {c}: {n}\n')

    f.write('\n## Rework list (LLM-flagged)\n\n')
    f.write('| key | sev | category | reason |\n|---|---|---|---|\n')
    for k in sorted(llm_rework, key=lambda k: (llm[k].get('severity','') != 'major', k)):
        r = llm[k]
        reason = (r.get('reason') or '').replace('|', '/').replace('\n', ' ')[:120]
        f.write(f"| {k.split('betterquesting.')[-1]} | {r.get('severity','')} | {r.get('category','')} | {reason} |\n")

    f.write('\n## Rework list (deterministic QA — auto)\n\n')
    f.write('| key | QA issues |\n|---|---|\n')
    for k in sorted(qa_broken):
        f.write(f"| {k.split('betterquesting.')[-1]} | {','.join(segs[k]['issues'])} |\n")

print(f'rework total: {len(rework)} (qa_broken {len(qa_broken)} + llm {len(llm_rework)}, '
      f'overlap {len(qa_broken & llm_rework)})')
print(f'+ missing to translate: {len(missing)}')
print(f'grand total to translate: {len(rework | missing)}')
print('report -> work/report.md')
print('LLM rework by category:', dict(cat))
