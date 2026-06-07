export const meta = {
  name: 'validate-translations',
  description: 'Haiku fleet reviews each RU translation; returns the rework list with reasons',
  phases: [{ title: 'Review', detail: 'one Haiku reviewer per batch of segments' }],
}

phase('Review')
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
          verdict: { type: 'string', enum: ['keep', 'rework'] },
          severity: { type: 'string', enum: ['ok', 'minor', 'major'] },
          category: {
            type: 'string',
            enum: ['fluency', 'mistranslation', 'terminology', 'untranslated',
                   'mixed_language', 'formatting', 'register', 'other'],
          },
          reason: { type: 'string', description: 'short Russian explanation (only if rework)' },
        },
      },
    },
  },
}

const base = args.base
const count = args.count
const idx = Array.from({ length: count }, (_, i) => i)

const results = await parallel(idx.map((i) => () => {
  const file = `${base}/val_${String(i).padStart(4, '0')}.json`
  const prompt =
    `You are a senior Russian localization reviewer for the GregTech New Horizons (GTNH) Minecraft modpack questbook. ` +
    `Read the JSON file ${file} — an array of segments {id, en (English source), ru (current Russian translation), ` +
    `ctx (English quest title for context), hint (automated QA flags)}.\n\n` +
    `For EACH segment, judge the Russian translation:\n` +
    `- verdict "rework" if: it is machine-translated/garbled; English PROSE is left untranslated; it mistranslates the source; ` +
    `broken grammar; wrong or nonsensical terminology; or formatting tokens (%n, §color-codes, [tags], [url]) are damaged/lost.\n` +
    `- verdict "keep" if: it is fluent, correct Russian that conveys the source meaning. ` +
    `Keeping proper nouns / mod names in English (e.g. "Not Enough Items", "Discord", "GregTech", channel names like #announcements) is FINE — do NOT flag those as untranslated.\n\n` +
    `Be strict about garbled machine translation, but do NOT flag a good translation over minor stylistic taste. ` +
    `When rework: set severity (minor/major), category, and a short reason in Russian. When keep: severity "ok", omit reason.\n` +
    `Return {results:[{id, verdict, severity, category, reason}]} covering EVERY segment in the file.`
  return agent(prompt, { label: `val:${i}`, phase: 'Review', model: 'haiku', schema: SCHEMA })
    .then((r) => (r && r.results) ? r.results : [])
}))

const all = results.filter(Boolean).flat()
const rework = all.filter((r) => r.verdict === 'rework')
const keep = all.filter((r) => r.verdict === 'keep')
log(`reviewed ${all.length}: keep ${keep.length}, rework ${rework.length}`)
return { rework, keep_count: keep.length, reviewed: all.length }