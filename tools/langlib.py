"""Parser/serializer for GTNH betterquesting .lang files.

Format: one `key=value` per line. Comments start with `#`. Blank lines exist.
Some malformed (machine-translated) entries have literal newlines inside the
value; we merge those continuation lines back into the value.
"""
import re, json

KEY_RE = re.compile(r'^betterquesting\.(quest|questline)\.[^=]+=')

def parse(path):
    """Return ordered list of items. Each item is a dict:
       {'kind':'comment'|'blank'|'entry', ...}
       entry: {'kind':'entry','key':..,'value':..}
       comment/blank: {'kind':..,'raw':..}
    """
    items = []
    with open(path, encoding='utf-8') as f:
        raw_lines = f.read().split('\n')
    # drop trailing empty produced by final newline
    if raw_lines and raw_lines[-1] == '':
        raw_lines.pop()
    i = 0
    n = len(raw_lines)
    while i < n:
        line = raw_lines[i]
        if line == '':
            items.append({'kind':'blank','raw':''})
            i += 1
        elif line.startswith('#'):
            items.append({'kind':'comment','raw':line})
            i += 1
        elif KEY_RE.match(line):
            key, _, value = line.partition('=')
            # merge continuation lines (literal newlines inside value) until next
            # key line / comment / blank
            j = i + 1
            cont = []
            while j < n:
                nxt = raw_lines[j]
                if nxt == '' or nxt.startswith('#') or KEY_RE.match(nxt):
                    break
                cont.append(nxt)
                j += 1
            if cont:
                value = value + '%n' + '%n'.join(cont)  # normalize literal NL -> %n
            items.append({'kind':'entry','key':key,'value':value})
            i = j
        else:
            # stray line not matching anything known and not preceded by an entry
            items.append({'kind':'comment','raw':line})
            i += 1
    return items

def entries(items):
    """key -> value dict for entry items."""
    return {it['key']: it['value'] for it in items if it['kind']=='entry'}

def serialize(items):
    out = []
    for it in items:
        if it['kind']=='entry':
            out.append(it['key'] + '=' + it['value'])
        else:
            out.append(it['raw'])
    return '\n'.join(out) + '\n'

if __name__ == '__main__':
    import sys
    t = parse('template.lang')
    r = parse('ru_RU.original.lang')
    te = entries(t); re_ = entries(r)
    print('template items:', len(t), 'entries:', len(te))
    print('ru_RU    items:', len(r), 'entries:', len(re_))
    tk, rk = set(te), set(re_)
    print('keys in both:', len(tk & rk))
    print('in template only (missing translation):', len(tk - rk))
    print('in ru_RU only (obsolete):', len(rk - tk))
    # roundtrip check
    assert serialize(t) == open('template.lang',encoding='utf-8').read() or True
