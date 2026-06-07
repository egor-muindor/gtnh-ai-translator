export const meta = {
  name: 'sonnet-validate-fix',
  description: 'Sonnet second-tier pass (50 agents): validate every Haiku translation vs source and rewrite any that fall short',
  phases: [{ title: 'Refine', detail: 'one Sonnet reviewer/fixer per large batch' }],
}

phase('Refine')
const SCHEMA = {
  type: 'object',
  required: ['results'],
  properties: {
    results: {
      type: 'array',
      items: {
        type: 'object',
        required: ['id', 'verdict'],
        properties: {
          id: { type: 'string' },
          verdict: { type: 'string', enum: ['keep', 'improve'] },
          ru: { type: 'string', description: 'improved Russian (required when verdict=improve)' },
          note: { type: 'string', description: 'short reason when improved' },
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
  `You are a SENIOR Russian game-localization editor doing a second-tier quality pass over a junior translator's work for the GregTech New Horizons (GTNH) Minecraft modpack questbook.\n\n` +
  `Read the glossary file ${glossary} (lines "EN => RU"; RU equal to EN means the term stays in Latin). ` +
  `Then read the batch file ${file} — an array of {id, en (English source), ru (junior translation to review), ctx (quest title), field}. ` +
  `The batch may contain ~60 segments; you MUST return a result for EVERY single one.\n\n` +
  `For EACH segment, critically compare ru against en:\n` +
  `- verdict "keep" if the translation is accurate, fluent, idiomatic, uses correct terminology, and preserves formatting. Do NOT change good translations.\n` +
  `- verdict "improve" if you can make it meaningfully better: fix mistranslation, awkward/unnatural phrasing, wrong or inconsistent terminology, missed nuance, wrong register, or formatting problems. Provide the corrected Russian in "ru" and a short "note".\n\n` +
  `Standards for any rewrite:\n` +
  `- Register: informal «ты».\n` +
  `- Terminology: follow the glossary; keep mod names, proper nouns, Latin glossary-terms, channel names (#x), commands (!x) and URLs unchanged. Do NOT over-russify.\n` +
  `- Natural, idiomatic Russian — never a word-for-word calque.\n` +
  `- PRESERVE every formatting token EXACTLY with the SAME COUNT as en: %n, %%, §x color codes (e.g. §9 §l §r), [note]/[warn]/[url]/[quest] tags; the text inside [url]…[/url] must be byte-identical to en. Pay special attention to §-color codes: keep exactly the same codes as en.\n` +
  `- Single-line output (%n for line breaks, never real newlines).\n` +
  `- Leave intentionally-Latin titles (chemical formulas, acronyms, mod/brand names) as they are.\n\n` +
  `Be a discerning editor: improve what genuinely needs it, keep what is already good. Work through ALL segments in the file. Return {results:[{id, verdict, ru?, note?}]} for EVERY segment.`

const results = await parallel(idx.map((i) => () => {
  const file = `${base}/sn_${String(i).padStart(4, '0')}.json`
  return agent(prompt(file), { label: `sn:${i}`, phase: 'Refine', model: 'sonnet', schema: SCHEMA })
    .then((r) => (r && r.results) ? r.results : [])
}))

const all = results.filter(Boolean).flat()
const improved = all.filter((r) => r.verdict === 'improve')
log(`reviewed ${all.length}: improved ${improved.length}, kept ${all.length - improved.length}`)
return { results: all, improved_count: improved.length, reviewed: all.length }