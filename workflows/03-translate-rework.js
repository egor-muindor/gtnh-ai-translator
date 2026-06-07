export const meta = {
  name: 'translate-rework',
  description: 'Haiku fleet translates/fixes flagged GTNH strings using the glossary, ты register, formatting preserved',
  phases: [{ title: 'Translate', detail: 'one Haiku localizer per batch' }],
}

phase('Translate')
const SCHEMA = {
  type: 'object',
  required: ['results'],
  properties: {
    results: {
      type: 'array',
      items: {
        type: 'object',
        required: ['id', 'ru'],
        properties: {
          id: { type: 'string' },
          ru: { type: 'string', description: 'final Russian value, single line, %n for breaks' },
        },
      },
    },
  },
}

const base = args.base
const count = args.count
const glossary = args.glossary
const idx = Array.from({ length: count }, (_, i) => i)

const prompt = (file) =>
  `You are a professional English→Russian game localizer for the GregTech New Horizons (GTNH) Minecraft modpack questbook.\n\n` +
  `STEP 1: Read the glossary file ${glossary} — lines "EN => RU". Use these established Russian equivalents for consistency. When RU equals EN, that term stays in Latin script.\n\n` +
  `STEP 2: Read the batch file ${file} — a JSON array of segments. Each has: id, en (English source), ctx (English quest title, context only), field ("name"=short title, "desc"=description), mode ("fresh" or "fix"). "fix" segments also include ru (current translation) and issue (what is wrong).\n\n` +
  `For each segment produce the Russian translation "ru":\n` +
  `- mode "fresh": translate en into natural fluent Russian from scratch.\n` +
  `- mode "fix": the existing ru is mostly good but has the problem in "issue". Fix ONLY that problem; keep the rest of the good wording.\n\n` +
  `RULES (all segments):\n` +
  `- Register: informal «ты» (ты/тебя/твой/тебе).\n` +
  `- Terminology: follow the glossary. Keep mod names, proper nouns, glossary Latin-terms, channel names (#announcements), commands (!download) and URLs UNCHANGED. Do NOT over-russify.\n` +
  `- Translate idiomatically, never word-for-word. E.g. "One step closer to your goal" → "Ещё на шаг ближе к твоей цели".\n` +
  `- PRESERVE every formatting token EXACTLY, same COUNT as en, correct place:\n` +
  `  · %n (line break) — same number as source · %% (literal percent)\n` +
  `  · §x color/format codes (e.g. §9 §l §r) — keep the source's codes\n` +
  `  · [note]…[/note], [warn]…[/warn], [url]…[/url], [quest]…[/quest] — keep tags; text inside [url]…[/url] must be byte-identical to source.\n` +
  `- field "name": concise title; preserve leading §-codes from source.\n` +
  `- Output a SINGLE-LINE value (use %n for breaks, never real newlines).\n\n` +
  `Return {results:[{id, ru}]} for EVERY segment in the file.`

const results = await parallel(idx.map((i) => () => {
  const file = `${base}/tr_${String(i).padStart(4, '0')}.json`
  return agent(prompt(file), { label: `tr:${i}`, phase: 'Translate', model: 'haiku', schema: SCHEMA })
    .then((r) => (r && r.results) ? r.results : [])
}))

const all = results.filter(Boolean).flat()
log(`translated ${all.length} segments across ${count} batches`)
return { results: all }