"""QA / placeholder-integrity checks for GTNH translations.

Validates that a translated target preserves the formatting contract of its
English source: %n newlines, §-color codes, [tag]...[/tag] markup, [url] bodies,
and %% literals. Also flags English leakage and untranslated/empty targets.

Importable (qa_segment) and runnable as CLI over work/pairs.json.
"""
import re, json, collections

# --- token extractors -------------------------------------------------------
RE_PCT_N   = re.compile(r'%n')
RE_PCT_PCT = re.compile(r'%%')
RE_COLOR   = re.compile(r'§.')
RE_TAG     = re.compile(r'\[/?[a-zA-Z][a-zA-Z0-9]*\]')
RE_URLBODY = re.compile(r'\[url\](.*?)\[/url\]', re.S)
RE_URL     = re.compile(r'https?://[^\s\]\[]+')
RE_CYR     = re.compile(r'[а-яёА-ЯЁ]')
RE_LATWORD = re.compile(r'\b[A-Za-z][A-Za-z\'-]{2,}\b')

# Proper nouns / technical tokens that may legitimately stay in Latin script.
WHITELIST = set('''
GTNH NEI GregTech GregTech5 GT5 GT6 Minecraft Discord Wiki CurseForge MultiMC Prism
Technic Java Forge IC2 IndustrialCraft EnderIO AE2 AE Thaumcraft Botania Forestry
Tinkers TiCon Construct Galacticraft Avaritia Draconic Evolution Gendustry Witchery
Blood Magic Astral Sorcery TCon RWG HV MV LV EV IV LuV ZPM UV UHV UEV UIV UMV UXV
EU RF FE GT TPS FPS XOR AND OR NOT URL HP XP UI HUD QnA FAQ TODO RNG AoE DPS LP
EMC UU OreDict NBT JSON OP AFK GUI WIP DIY CPU GPU RAM ID IDs Pam Harvestcraft
Stargate spreadsheet Tilde Coke LCR EBF Bricked Pyrolyse Pahoehoe CoAFC SoC PCB
TecTech AESU LSC IAPC PA CoAL DTPF UCFE Mk MK Tier url warn note quest img sic
'''.split())


def color_codes(s):  return collections.Counter(RE_COLOR.findall(s))
def tags(s):         return collections.Counter(RE_TAG.findall(s))
def url_bodies(s):   return [u.strip() for u in RE_URLBODY.findall(s)]
def bare_urls(s):    return collections.Counter(RE_URL.findall(s))


# English function / common words. Their presence as standalone Latin tokens in
# a Russian target is a RELIABLE signal of leaked untranslated prose (garbage MT)
# -- unlike proper nouns ("Not Enough Items", "Discord"), which are legitimate.
STOPWORDS = set('''
the a an is are was were be been being am to of in on at for with from by as into
onto than then this that these those it its you your yours we our ours they them
their he she his her him and or but not no nor if when while which who whom what
where why how will would can could shall should may might must do does did doing
done have has had having get gets got make makes made like just also only more
most some any all each every both either neither about after before over under
above below between through during without within across around want wants need
needs use uses using used consider doing another still want else such very much
many few little less least own same other another here there now still yet already
because so though although however therefore thus hence meanwhile otherwise
means meant going go goes went come comes came take takes took give gives gave
let lets allow allows enough almost nearly even ever never always often sometimes
once twice thing things way ways something nothing anything everything someone
'''.split())


def latin_leak(target):
    """Standalone Latin tokens in the target (excluding whitelist & markup).
    NOTE: noisy -- includes legitimate proper nouns. Use prose_leak for verdicts."""
    s = RE_COLOR.sub('', target)
    s = RE_TAG.sub(' ', s)
    s = RE_URL.sub(' ', s)
    s = s.replace('%n', ' ').replace('%%', '%')
    return [w for w in RE_LATWORD.findall(s) if w not in WHITELIST]


def prose_leak(target):
    """Lowercase English function words leaked into the target -- reliable
    garbage-MT signal. Lowercase-only avoids Title-Case proper nouns
    ('Not Enough Items', 'The Factory Must Grow')."""
    s = RE_COLOR.sub('', target)
    s = RE_TAG.sub(' ', s)
    s = RE_URL.sub(' ', s)
    s = s.replace('%n', ' ').replace('%%', '%')
    return [w for w in RE_LATWORD.findall(s) if w == w.lower() and w in STOPWORDS]


def qa_segment(source, target):
    """Return list of QA issue dicts: {code, severity, detail}. Empty == clean."""
    issues = []
    if target is None or target.strip() == '':
        return [{'code': 'EMPTY', 'severity': 'error', 'detail': 'empty target'}]
    if target.strip() == source.strip():
        issues.append({'code': 'UNTRANSLATED', 'severity': 'error',
                       'detail': 'target identical to source'})
    if not RE_CYR.search(target) and RE_CYR.search('а'):  # target has no Cyrillic
        if not RE_CYR.search(target):
            issues.append({'code': 'NO_CYRILLIC', 'severity': 'error',
                           'detail': 'no Cyrillic letters in target'})
    # %n newline count
    sn, tn = len(RE_PCT_N.findall(source)), len(RE_PCT_N.findall(target))
    if sn != tn:
        issues.append({'code': 'PCT_N', 'severity': 'error',
                       'detail': f'%n count {tn} != source {sn}'})
    # %% literal
    sp, tp = len(RE_PCT_PCT.findall(source)), len(RE_PCT_PCT.findall(target))
    if sp != tp:
        issues.append({'code': 'PCT_PCT', 'severity': 'warn',
                       'detail': f'%% count {tp} != source {sp}'})
    # color codes (multiset)
    sc, tc = color_codes(source), color_codes(target)
    if sc != tc:
        issues.append({'code': 'COLOR', 'severity': 'warn',
                       'detail': f'§-codes {dict(tc)} != source {dict(sc)}'})
    # markup tags balance & preservation
    stg, ttg = tags(source), tags(target)
    if stg != ttg:
        issues.append({'code': 'TAGS', 'severity': 'error',
                       'detail': f'tags {dict(ttg)} != source {dict(stg)}'})
    # url bodies must be byte-identical and order-preserved
    su, tu = url_bodies(source), url_bodies(target)
    if su != tu:
        issues.append({'code': 'URL', 'severity': 'error',
                       'detail': f'url bodies {tu} != source {su}'})
    # bare url preservation (outside [url] tags)
    sb, tb = bare_urls(source), bare_urls(target)
    if sb != tb:
        issues.append({'code': 'BARE_URL', 'severity': 'warn',
                       'detail': f'urls {dict(tb)} != source {dict(sb)}'})
    # english PROSE leakage == garbage-MT signal, gated by DENSITY so that a few
    # code keywords / proper nouns in a long Cyrillic text don't false-positive.
    prose = prose_leak(target)
    clean = RE_COLOR.sub('', target)
    clean = RE_TAG.sub(' ', clean).replace('%n', ' ').replace('%%', '%')
    n_cyr_words = len(re.findall(r'[а-яёА-ЯЁ]+', clean))
    n_lat_words = len(RE_LATWORD.findall(clean))
    total_words = max(1, n_cyr_words + n_lat_words)
    density = len(prose) / total_words
    if len(prose) >= 2 and (density > 0.07 or n_cyr_words < 3):
        issues.append({'code': 'GARBAGE_MT', 'severity': 'error',
                       'detail': f'{len(prose)} english function words (density {density:.2f}): {prose[:8]}'})
    elif len(prose) >= 1:
        issues.append({'code': 'LEAK_MINOR', 'severity': 'warn',
                       'detail': f'english function word(s): {prose[:5]}'})
    # advisory: other latin tokens (may be proper nouns -> let LLM judge)
    other = [w for w in latin_leak(target) if w.lower() not in STOPWORDS]
    if len(other) >= 6:
        issues.append({'code': 'LATIN_DENSE', 'severity': 'warn',
                       'detail': f'{len(other)} latin tokens: {other[:8]}'})
    return issues


def classify(source, target):
    """Coarse status from QA: clean | broken | suspect."""
    iss = qa_segment(source, target)
    if any(i['severity'] == 'error' for i in iss):
        return 'broken', iss
    if iss:
        return 'suspect', iss
    return 'clean', iss


if __name__ == '__main__':
    import sys
    data = json.load(open('work/pairs.json'))
    counts = collections.Counter()
    bycode = collections.Counter()
    for d in data:
        st, iss = classify(d['en'], d['ru'])
        counts[st] += 1
        for i in iss:
            bycode[i['code']] += 1
    print('=== QA status over shared segments ===')
    for k, c in counts.most_common():
        print(f'  {k}: {c}')
    print('=== issue codes ===')
    for k, c in bycode.most_common():
        print(f'  {k}: {c}')
