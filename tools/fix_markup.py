"""Repair §-color-code and %% markup so translations match the English source.

Deterministic pass (safe):
  - NAME segments whose only problem is the leading §-code run: replace the
    translation's leading run with the source's, and align a trailing §r.
  - Any segment where, after that, the §-code multiset matches source -> fixed.
Whatever still mismatches is written to work/markup_llm_todo.json for an LLM round.

Produces work/markup_fixes.json (key -> corrected value) to merge into the
translation overrides, and reports what remains.
"""
import json, os, sys, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import langlib as L, qa

T = L.entries(L.parse('template.lang'))
cur = json.load(open('work/translations.json'))         # our overrides so far
base = L.entries(L.parse('ru_RU.original.lang'))                  # originals
segmeta = {s['key']: s for s in json.load(open('work/segments.json'))}

LEAD = re.compile(r'^(?:§.)+')
TRAIL = re.compile(r'(?:§.)+$')

def current_value(k):
    return cur.get(k, base.get(k))

def codes(s):
    return collections.Counter(qa.RE_COLOR.findall(s))

def fix_leading(src, tgt):
    """Replace tgt's leading §-run with src's leading §-run."""
    s_lead = (LEAD.match(src) or [''])[0] if LEAD.match(src) else ''
    s_lead = LEAD.match(src).group(0) if LEAD.match(src) else ''
    t_lead = LEAD.match(tgt).group(0) if LEAD.match(tgt) else ''
    body = tgt[len(t_lead):]
    return s_lead + body

fixes = {}
llm_todo = []
det = 0
for k in sorted(set(T) & (set(cur) | set(base))):
    src = T[k]
    tgt = current_value(k)
    if tgt is None:
        continue
    cs, ct = codes(src), codes(tgt)
    pct_ok = src.count('%%') == tgt.count('%%')
    if cs == ct and pct_ok:
        continue  # already fine
    field = segmeta.get(k, {}).get('field')
    new = tgt
    # deterministic: realign leading run (works for the common name case)
    if field == 'name':
        cand = fix_leading(src, tgt)
        # also align trailing §r if source ends with §r and candidate doesn't
        s_tr = TRAIL.search(src).group(0) if TRAIL.search(src) else ''
        if s_tr and not cand.endswith(s_tr) and '§r' in s_tr:
            cand = cand + '§r'
        if codes(cand) == cs:
            new = cand
    if codes(new) == cs and new.count('%%') == src.count('%%'):
        if new != tgt:
            fixes[k] = new
            det += 1
    else:
        llm_todo.append({'id': k, 'en': src, 'ru': tgt, 'field': field,
                         'problem': ('§codes' if cs != ct else '') + (' %%' if not pct_ok else '')})

json.dump(fixes, open('work/markup_fixes.json', 'w'), ensure_ascii=False)
json.dump(llm_todo, open('work/markup_llm_todo.json', 'w'), ensure_ascii=False)
print(f'deterministic markup fixes: {det}')
print(f'still need LLM repair: {len(llm_todo)}')
byf = collections.Counter(x['field'] for x in llm_todo)
print('llm_todo by field:', dict(byf))
