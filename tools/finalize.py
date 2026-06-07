"""Turn translation results into the final file, with a QA gate.

Merges round-1 (tr_results.json) + round-2 (tr_round2_results.json, if present).
A "legitimately Latin" source (chemical formula / acronym / curated mod name)
is allowed to stay untranslated instead of failing the QA gate forever.

Output: work/translations.json, work/tr_qa_fail.json, ru_RU.lang
"""
import json, os, sys, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import qa, build

segs = {s['key']: s for s in json.load(open('work/segments.json'))}

# curated sources that correctly stay in Latin (match on source minus §codes)
KEEP_LATIN = {
    'C9H8O4...NaCl...H2O...', 'NaK', 'HSS-G', 'HSS-S', 'P-507', 'N.N.Q.Q.N.Q.Q',
    'TFFT', 'MABS', 'BIOS', 'IAADDS', 'D-O-B', 'RAM', 'Applied Energistics',
    'Salis Mundus', 'Plague Inc.', 'Loonium', 'Nimbus 1999', 'Jeremy Fragrance',
    'Lapotron', 'Better Questing?', '「 」',
}
def strip_codes(s): return re.sub(r'§.', '', s).strip()
def legit_latin(src):
    s = strip_codes(src)
    if s in KEEP_LATIN:
        return True
    # pure uppercase acronym / formula / symbols, no lowercase latin letters
    if re.fullmatch(r'[A-Z0-9 .\-_/「」,!?()]+', s) and len(s) <= 12:
        return True
    return False

if __name__ == '__main__':
    # merge results: round-1 then round-2/3 (later wins)
    trans = {}
    for path in ['work/tr_results.json', 'work/tr_round2_results.json',
                 'work/tr_round3_results.json']:
        if os.path.exists(path):
            for r in json.load(open(path)):
                if r.get('id') in segs and r.get('ru'):
                    trans[r['id']] = r['ru']

    # QA gate
    passed, failed = {}, []
    for k, ru in trans.items():
        src = segs[k]['src']
        issues = qa.qa_segment(src, ru)
        errs = [i for i in issues if i['severity'] == 'error']
        # allow untranslated/no-cyrillic when the source legitimately stays Latin
        if errs and set(i['code'] for i in errs) <= {'UNTRANSLATED', 'NO_CYRILLIC'} and legit_latin(src):
            passed[k] = ru
            continue
        if errs:
            failed.append({'id': k, 'ru': ru, 'issues': [i['code'] for i in errs]})
        else:
            passed[k] = ru

    json.dump(passed, open('work/translations.json', 'w'), ensure_ascii=False)
    json.dump(failed, open('work/tr_qa_fail.json', 'w'), ensure_ascii=False)

    print(f'merged unique translations: {len(trans)}')
    print(f'QA passed: {len(passed)} | QA failed: {len(failed)}')
    print('failure codes:', dict(collections.Counter(c for f in failed for c in f['issues'])))

    res = build.build('ru_RU.lang')
    print('--- build ---')
    for k, v in res.items():
        print(f'  {k}: {v}')
