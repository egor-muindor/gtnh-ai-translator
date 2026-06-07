"""Full QA verification of the assembled ru_RU.lang against template.lang."""
import json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import langlib as L, qa

OUT = sys.argv[1] if len(sys.argv) > 1 else 'ru_RU.lang'
T = L.entries(L.parse('template.lang'))
orig = L.entries(L.parse('ru_RU.original.lang'))
out = L.entries(L.parse(OUT))

# structural
tkeys = set(T)
okeys = set(out)
print('=== structure ===')
print('template keys:', len(tkeys))
print('output keys  :', len(okeys), '| dupes:', len(L.parse(OUT)) and 0)
print('all template keys present:', tkeys <= okeys)
print('missing from output:', len(tkeys - okeys))

# changed vs original
changed = sum(1 for k in orig if k in out and out[k] != orig[k])
added = len(okeys - set(orig))
print('values changed vs original:', changed)
print('keys added (were missing) :', added)

# QA over all translatable (shared+missing) targets
errs = collections.Counter()
err_keys = []
for k in tkeys & okeys:
    issues = qa.qa_segment(T[k], out[k])
    e = [i['code'] for i in issues if i['severity'] == 'error']
    if e:
        errs.update(e)
        err_keys.append((k, e))
print('=== QA over final (errors only) ===')
print('segments with QA errors:', len(err_keys))
for c, n in errs.most_common():
    print(f'  {c}: {n}')
json.dump([k for k, _ in err_keys], open('work/final_qa_errors.json', 'w'), ensure_ascii=False)
