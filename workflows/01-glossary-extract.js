export const meta = {
  name: 'glossary-extract',
  description: 'Haiku fleet extracts EN->RU termbase from professionally-translated GTNH pairs',
  phases: [{ title: 'Extract', detail: 'one Haiku agent per batch of good pairs' }],
}

phase('Extract')
const SCHEMA = {
  type: 'object',
  required: ['terms'],
  properties: {
    terms: {
      type: 'array',
      items: {
        type: 'object',
        required: ['en', 'ru'],
        properties: {
          en: { type: 'string', description: 'English term, base form' },
          ru: { type: 'string', description: 'Established Russian equivalent; empty if kept in Latin' },
        },
      },
    },
  },
}

const base = args.base
const count = args.count
const idx = Array.from({ length: count }, (_, i) => i)

const results = await parallel(idx.map((i) => () => {
  const file = `${base}/gloss_${String(i).padStart(4, '0')}.json`
  const prompt =
    `You are building a bilingual terminology glossary (termbase) for the Russian translation of the ` +
    `GregTech New Horizons (GTNH) Minecraft modpack questbook. ` +
    `Read the JSON file ${file} — an array of {en, ru} pairs that are PROFESSIONALLY TRANSLATED (high quality). ` +
    `Extract the recurring, reusable TERMS and their established Russian equivalents:\n` +
    `- game mechanics (e.g. smelting, overclock, multiblock, tier, recipe)\n` +
    `- machine / block / item / material names\n` +
    `- mod names and proper nouns\n` +
    `- recurring multi-word domain phrases\n` +
    `Rules:\n` +
    `- Only output a term if it has a CLEAR, consistent Russian equivalent visible in the pairs.\n` +
    `- For proper nouns / mod names that are kept in Latin script (e.g. GregTech, Not Enough Items, Discord), set ru to the SAME Latin text.\n` +
    `- Normalize to base/nominative singular form. Lowercase common nouns; keep proper-noun casing.\n` +
    `- SKIP generic words, full sentences, and anything without a stable equivalent.\n` +
    `Return {terms:[{en, ru}]} (aim for the 15-40 most useful terms in this batch).`
  return agent(prompt, { label: `gloss:${i}`, phase: 'Extract', model: 'haiku', schema: SCHEMA })
    .then((r) => r || { terms: [] })
}))

const terms = results.filter(Boolean).flatMap((r) => r.terms || [])
log(`extracted ${terms.length} raw term pairs from ${count} batches`)
return { terms }