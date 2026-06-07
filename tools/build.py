"""Assemble the final ru_RU.original.lang.

Strategy: ru_RU.original.lang is the BASE (preserves existing order, comments, and the 16
obsolete keys). We (1) override values for reworked keys, (2) insert the 388
keys missing from ru at their template-adjacent positions, carrying their
English comment headers.

Inputs:
  work/translations.json : { key: new_target }  (reworked + missing translations)
Output:
  ru_RU.lang  (then promoted to ru_RU.original.lang by the caller after review)

Run: python3 work/build.py [out_path]
"""
import json, os, sys
import langlib as L

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def load_translations():
    try:
        return json.load(open('work/translations.json'))
    except FileNotFoundError:
        return {}

def build(out_path='ru_RU.lang', translations=None, placeholder_missing=False):
    if translations is None:
        translations = load_translations()
    ti = L.parse('template.lang')
    ri = L.parse('ru_RU.original.lang')
    R = L.entries(ri)
    Tk = [it['key'] for it in ti if it['kind'] == 'entry']
    ru_keys = set(R)
    missing = [k for k in Tk if k not in ru_keys]
    missing_set = set(missing)

    # --- Build insertion plan from template stream ---------------------------
    # For each missing entry, the anchor = previous template entry present in ru
    # (None => top). Group the comment/blank lead-in that belongs to missing
    # quests; trailing lead-ins that belong to the next shared entry are dropped.
    inserts = {}        # anchor_key (or '' for top) -> list of items to insert after it
    last_shared = ''    # '' == top of file
    buffer = []         # pending comment/blank items since last entry
    for it in ti:
        if it['kind'] in ('comment', 'blank'):
            buffer.append(it)
            continue
        # entry
        k = it['key']
        if k in missing_set:
            # this entry + its lead-in comments/blanks attach after last_shared
            payload = inserts.setdefault(last_shared, [])
            payload.extend(buffer)
            payload.append(it)
            buffer = []
            # last_shared stays (missing keys chain under same anchor)
        else:
            # shared entry: its lead-in comments already exist in ru -> drop buffer
            buffer = []
            last_shared = k

    # --- Emit: walk ru base, apply overrides, splice inserts -----------------
    out = []
    def emit_entry(it):
        k = it['key']
        if k in translations:
            out.append({'kind': 'entry', 'key': k, 'value': translations[k]})
        else:
            out.append(it)

    # top-of-file inserts
    if '' in inserts:
        for ins in inserts['']:
            if ins['kind'] == 'entry':
                key = ins['key']
                val = translations.get(key, ins['value'] if placeholder_missing else translations.get(key))
                if val is None:
                    val = ins['value']  # fallback: english (should not happen post-translation)
                out.append({'kind': 'entry', 'key': key, 'value': val})
            else:
                out.append(ins)

    for it in ri:
        if it['kind'] == 'entry':
            emit_entry(it)
            after = inserts.get(it['key'])
            if after:
                for ins in after:
                    if ins['kind'] == 'entry':
                        key = ins['key']
                        val = translations.get(key)
                        if val is None:
                            val = ins['value'] if placeholder_missing else ins['value']
                        out.append({'kind': 'entry', 'key': key, 'value': val})
                    else:
                        out.append(ins)
        else:
            out.append(it)

    text = L.serialize(out)
    open(out_path, 'w', encoding='utf-8').write(text)

    # --- verify ------------------------------------------------------------
    chk = L.parse(out_path)
    keys_out = [x['key'] for x in chk if x['kind'] == 'entry']
    return {
        'out': out_path,
        'entries_out': len(keys_out),
        'unique_keys': len(set(keys_out)),
        'expected_union': len(ru_keys | set(Tk)),
        'missing_inserted': len(missing),
        'overrides_applied': sum(1 for k in translations if k in ru_keys),
        'dupes': len(keys_out) - len(set(keys_out)),
    }

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'ru_RU.lang'
    res = build(out, placeholder_missing=True)
    for k, v in res.items():
        print(f'{k}: {v}')
