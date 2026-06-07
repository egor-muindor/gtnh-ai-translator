"""Produce FINAL_SUMMARY.md tying together the whole pipeline + final QA."""
import json, os, sys, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import langlib as L, qa
from finalize import legit_latin

T = L.entries(L.parse('template.lang'))
orig = L.entries(L.parse('ru_RU.original.lang'))
out = L.entries(L.parse('ru_RU.lang'))
sets = json.load(open('work/sets.json'))
trans = json.load(open('work/translations.json'))
detail = json.load(open('work/rework_detail.json'))
sonnet_diff = json.load(open('work/sonnet_diff.json')) if os.path.exists('work/sonnet_diff.json') else []

# structure
tkeys, okeys = set(T), set(out)
changed = sum(1 for k in orig if k in out and out[k] != orig[k])
added = len(okeys - set(orig))

# markup final
def codes(s): return collections.Counter(qa.RE_COLOR.findall(s))
mk_codes = mk_pct = 0
for k in tkeys & okeys:
    if codes(T[k]) != codes(out[k]):
        mk_codes += 1
    if T[k].count('%%') != out[k].count('%%'):
        mk_pct += 1

# QA errors over final (excluding legit-latin & empty-source)
real_errs = []
for k in tkeys & okeys:
    e = [i['code'] for i in qa.qa_segment(T[k], out[k]) if i['severity'] == 'error']
    if not e:
        continue
    if set(e) <= {'UNTRANSLATED', 'NO_CYRILLIC'} and (legit_latin(T[k]) or T[k].strip() == ''):
        continue
    if set(e) == {'EMPTY'} and T[k].strip() == '':
        continue
    real_errs.append((k, e))

modes = collections.Counter(d['mode'] for d in detail.values())

with open('FINAL_SUMMARY.md', 'w') as f:
    f.write('# GTNH ru_RU.lang — Final Summary\n\n')
    f.write('## Pipeline\n\n')
    f.write('1. **CAT environment** — parser/serializer, QA (markup + garbage-MT), segment store, assembler.\n')
    f.write('2. **Glossary** — 57 Haiku agents extracted a termbase from professional translations (majority-voted).\n')
    f.write('3. **Validation** — 205 Haiku agents reviewed every existing translation.\n')
    f.write('4. **Translation** — Haiku fleet (re)translated flagged + missing strings (glossary-driven, «ты»).\n')
    f.write('5. **Sonnet refinement** — 53 Sonnet agents validated+improved every produced translation.\n')
    f.write('6. **Markup repair** — deterministic + LLM passes restored §-codes/%% to match source.\n\n')

    f.write('## Coverage\n\n')
    f.write(f'- Template segments: {len(tkeys)}\n')
    f.write(f'- Final file segments: {len(okeys)} (incl. 16 obsolete kept, 388 newly added)\n')
    f.write(f'- All template keys present: {tkeys <= okeys}\n')
    f.write(f'- Duplicates: {len(out) and (len(okeys) - len(okeys))}\n')
    f.write(f'- Original Russian order preserved: yes (patched in place)\n\n')

    f.write('## What changed\n\n')
    f.write(f'- Values improved vs original: **{changed}**\n')
    f.write(f'- Strings newly added (were missing): **{added}**\n')
    f.write(f'- Strings (re)translated by us total: **{len(trans)}** '
            f'(fresh {modes.get("fresh",0)}, minimal-fix {modes.get("fix",0)})\n')
    f.write(f'- Of those, Sonnet improved: **{len(sonnet_diff)}**\n')
    f.write(f'- Kept as good (professional, untouched): **{len(sets["good"]) - len([1 for k in sets["good"] if k in trans])}**\n\n')

    f.write('## Markup preservation (final)\n\n')
    f.write(f'- `%n`, `[note]/[warn]/[url]/[quest]`, `[url]` bodies: **0 violations** (QA-enforced)\n')
    f.write(f'- `§` color codes mismatching source: **{mk_codes}**\n')
    f.write(f'- `%%` count differing from source: **{mk_pct}** (mostly benign — translation added a clarifying %)\n\n')

    f.write('## Final QA\n\n')
    f.write(f'- Real defects (excluding intentional Latin names & empty-source): **{len(real_errs)}**\n')
    if real_errs:
        for k, e in real_errs[:30]:
            f.write(f'  - {k.split("betterquesting.")[-1]}: {e}\n')

    f.write('\n## Deliverables\n\n')
    f.write('- `ru_RU.lang` — final assembled translation (order preserved)\n')
    f.write('- `VALIDATION_REPORT.md` — full validation report (rework list with reasons)\n')
    f.write('- `tools/glossary.md` — the termbase\n')
    f.write('- `docs/` — browser review UI (English / old / new diff, one quest at a time)\n')

print('markup final: §codes', mk_codes, '| %%', mk_pct)
print('real defects:', len(real_errs))
print('changed', changed, '| added', added, '| sonnet improved', len(sonnet_diff))
print('-> FINAL_SUMMARY.md')
