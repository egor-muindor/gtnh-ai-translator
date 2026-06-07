import re, json
import langlib as L
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

t = L.entries(L.parse('template.lang'))
r = L.entries(L.parse('ru_RU.original.lang'))
both = sorted(set(t) & set(r))
only_t = sorted(set(t) - set(r))
only_r = sorted(set(r) - set(t))

# size distribution of russian values for shared keys
sizes = sorted(len(r[k]) for k in both)
tot = sum(sizes)
print(f"shared={len(both)} missing_in_ru={len(only_t)} obsolete_in_ru={len(only_r)}")
print(f"total RU chars (shared) = {tot:,}")
print(f"value len: min={sizes[0]} median={sizes[len(sizes)//2]} p90={sizes[int(len(sizes)*0.9)]} max={sizes[-1]} mean={tot//len(sizes)}")

# Heuristic breakage detectors (0-token pre-filter / cross-check)
CYR = re.compile(r'[а-яёА-ЯЁ]')
LAT_WORD = re.compile(r'\b[A-Za-z]{3,}\b')
# Known proper nouns / tokens to ignore when counting "english leakage"
WHITELIST = set('''GTNH NEI GregTech Minecraft Discord Wiki CurseForge MultiMC Prism Technic
Java IC2 EnderIO AE2 Thaumcraft Botania Forestry Tinkers Construct TiCon HV MV LV EV IV LuV ZPM UV UHV UEV UIV UMV UXV
url warn note item img EU RF FE GT TPS FPS XOR AND OR NOT ID HP XP UI HUD QnA FAQ OK TODO DNA RNG AoE DPS
Pam Harvestcraft Stargate spreadsheet download announcements role select Tilde'''.split())

def latin_leak(val):
    # remove formatting tokens, urls, color codes, bracket tags
    s = re.sub(r'§.', '', val)
    s = re.sub(r'\[/?[a-zA-Z]+\]', ' ', s)
    s = re.sub(r'https?://\S+', ' ', s)
    s = s.replace('%n',' ').replace('%%','%')
    words = LAT_WORD.findall(s)
    leak = [w for w in words if w not in WHITELIST]
    return leak

flags = {'untranslated':[], 'mixed_lang':[], 'no_cyrillic':[], 'fmt_mismatch':[], 'empty':[]}
for k in both:
    en, ru = t[k], r[k]
    if not ru.strip():
        flags['empty'].append(k); continue
    if ru.strip() == en.strip():
        flags['untranslated'].append(k); continue
    if not CYR.search(ru):
        flags['no_cyrillic'].append(k); continue
    leak = latin_leak(ru)
    if len(leak) >= 4:
        flags['mixed_lang'].append((k,len(leak)))
    # formatting token preservation
    def toks(s):
        return (s.count('%n'), len(re.findall(r'§.',s)), s.count('[url]'), s.count('[/url]'))
    if toks(en)[0] and toks(ru)[0]==0 and toks(en)[0]>1:
        flags['fmt_mismatch'].append(k)

for kf,v in flags.items():
    print(f"  heuristic {kf}: {len(v)}")

# save the paired dataset for the workflow
data = []
for k in both:
    data.append({'key':k,'en':t[k],'ru':r[k]})
json.dump(data, open('work/pairs.json','w'), ensure_ascii=False)
json.dump({'missing_in_ru':only_t,'obsolete_in_ru':only_r}, open('work/keysets.json','w'), ensure_ascii=False)
# also dump missing english
miss = [{'key':k,'en':t[k]} for k in only_t]
json.dump(miss, open('work/missing.json','w'), ensure_ascii=False)
print("wrote work/pairs.json, work/keysets.json, work/missing.json")

# show some examples of clearly-broken ones
print("\n--- sample mixed_lang (worst) ---")
for k,n in sorted(flags['mixed_lang'], key=lambda x:-x[1])[:5]:
    print(f"[{n} leaks] {k}\n   RU: {r[k][:160]}")
