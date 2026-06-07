"""Bin segments into char-budgeted batch files under work/batches/.

Usage:
  python3 work/batch.py glossary   # good pairs -> glossary extraction batches
  python3 work/batch.py validate   # good+suspect -> validation batches
  python3 work/batch.py translate  # (after validation) rework set -> translate batches
"""
import json, os, sys, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def clear(prefix):
    for f in glob.glob(f'work/batches/{prefix}_*.json'):
        os.remove(f)

def write_batches(prefix, items, char_budget, max_items):
    """items: list of dicts already shaped for the agent. Bin by cumulative
    source+target chars; flush at char_budget or max_items."""
    clear(prefix)
    batches, cur, cur_chars = [], [], 0
    def size(it):
        return sum(len(str(v)) for v in it.values())
    for it in items:
        s = size(it)
        if cur and (cur_chars + s > char_budget or len(cur) >= max_items):
            batches.append(cur); cur, cur_chars = [], 0
        cur.append(it); cur_chars += s
    if cur:
        batches.append(cur)
    paths = []
    for i, b in enumerate(batches):
        p = f'work/batches/{prefix}_{i:04d}.json'
        json.dump(b, open(p, 'w'), ensure_ascii=False)
        paths.append({'file': os.path.abspath(p), 'n': len(b)})
    json.dump(paths, open(f'work/batches/{prefix}_index.json', 'w'), ensure_ascii=False)
    print(f'{prefix}: {len(items)} items -> {len(batches)} batches '
          f'(avg {len(items)//max(1,len(batches))}/batch); index at work/batches/{prefix}_index.json')
    return paths


def main(mode):
    segs = json.load(open('work/segments.json'))
    by = {}
    for s in segs:
        by.setdefault(s['qa_status'], []).append(s)

    if mode == 'glossary':
        good = by['good']
        # All good NAMEs (short, term-dense titles) + richest good DESCs.
        names = [s for s in good if s['field'] == 'name']
        descs = sorted([s for s in good if s['field'] == 'desc'],
                       key=lambda s: -(len(s['src']) + len(s['tgt'])))[:900]
        chosen = names + descs
        items = [{'id': s['key'], 'en': s['src'], 'ru': s['tgt']} for s in chosen]
        write_batches('gloss', items, char_budget=40000, max_items=90)

    elif mode == 'validate':
        review = by['good'] + by['suspect']
        # stable order by key for reproducibility
        review = sorted(review, key=lambda s: s['key'])
        items = [{'id': s['key'], 'en': s['src'], 'ru': s['tgt'],
                  'ctx': s['ctx'], 'hint': ','.join(s['issues'])} for s in review]
        write_batches('val', items, char_budget=14000, max_items=40)

    elif mode == 'translate':
        detail = json.load(open('work/rework_detail.json'))
        segmap = {s['key']: s for s in segs}
        items = []
        for k in sorted(detail):
            s = segmap[k]
            d = detail[k]
            it = {'id': k, 'en': s['src'], 'ctx': s['ctx'], 'field': s['field'],
                  'mode': d['mode']}
            if d['mode'] == 'fix':
                it['ru'] = s['tgt']          # existing translation to minimally fix
                it['issue'] = d['issue']     # what to fix
            items.append(it)
        write_batches('tr', items, char_budget=6000, max_items=18)

    elif mode == 'sonnet':
        # Sonnet second-tier validate+fix over every Haiku-produced translation.
        trans = json.load(open('work/translations.json'))
        detail = json.load(open('work/rework_detail.json'))
        segmap = {s['key']: s for s in segs}
        items = []
        for k in sorted(trans):
            if k not in segmap:
                continue
            s = segmap[k]
            items.append({'id': k, 'en': s['src'], 'ru': trans[k],
                          'ctx': s['ctx'], 'field': s['field']})
        # large batches -> ~50 agents (cuts per-agent glossary-read overhead)
        write_batches('sn', items, char_budget=40000, max_items=80)

    elif mode == 'retry':
        # round-2: re-fix translations that failed the QA gate
        fails = json.load(open('work/tr_qa_fail.json'))
        segmap = {s['key']: s for s in segs}
        QA_HELP = {
            'PCT_N': 'число %n должно ТОЧНО совпадать с английским источником',
            'TAGS': 'теги [note]/[warn]/[url]/[quest] должны совпадать с источником по числу и парности',
            'URL': 'ссылка внутри [url]...[/url] должна быть БАЙТ-в-байт как в источнике',
            'GARBAGE_MT': 'в переводе остались английские слова — переведи их полностью на русский',
            'NO_CYRILLIC': 'перевод должен быть на русском языке',
            'UNTRANSLATED': 'нужен полноценный русский перевод, не копия английского',
            'EMPTY': 'нужен перевод',
        }
        items = []
        for f in fails:
            k = f['id']; s = segmap[k]
            note = '; '.join(QA_HELP.get(c, c) for c in f['issues'])
            items.append({'id': k, 'en': s['src'], 'ctx': s['ctx'],
                          'field': s['field'], 'mode': 'fix', 'ru': f['ru'],
                          'issue': 'QA: ' + note})
        write_batches('rt', items, char_budget=6000, max_items=15)

    else:
        print('unknown mode', mode); sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'validate')
