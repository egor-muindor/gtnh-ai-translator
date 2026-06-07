export const meta = {
  name: 'translate-round2',
  description: 'Haiku repair pass for 65 edge-case strings (proper nouns, titles, formatting)',
  phases: [{ title: 'Repair' }],
}

phase('Repair')
const SCHEMA = {
  type: 'object',
  required: ['results'],
  properties: {
    results: {
      type: 'array',
      items: {
        type: 'object',
        required: ['id', 'ru'],
        properties: { id: { type: 'string' }, ru: { type: 'string' } },
      },
    },
  },
}

const base = args.base
const count = args.count
const glossary = args.glossary
const idx = Array.from({ length: count }, (_, i) => i)

const prompt = (file) =>
  `You are a professional English→Russian localizer for the GregTech New Horizons Minecraft modpack questbook. ` +
  `These are EDGE CASES that a previous pass left untranslated or broke.\n\n` +
  `Read glossary ${glossary} (lines "EN => RU"), then read ${file} — array of {id, en, ctx, field, prev_attempt?}.\n\n` +
  `Translate each "en" into Russian. Register: informal «ты».\n\n` +
  `KEY RULES for short titles (field="name"):\n` +
  `- TRANSLATE the title to Russian whenever it has a sensible Russian form. Examples:\n` +
  `  "Snow Queen"→"Снежная королева", "Hydra"→"Гидра", "Naga"→"Нага", "Lich"→"Лич", "Yeti"→"Йети", ` +
  `"Knight Phantom"→"Призрачный рыцарь", "I'm Hungry"→"Я голоден", "A Casing"→"Корпус", ` +
  `"Power, So Much Power!"→"Сила, так много силы!", "Living Matter"→"Живая материя", ` +
  `"Superdense"→"Сверхплотный", "Convergence"→"Конвергенция", "Charms"→"Талисманы", ` +
  `"Dragon Essence"→"Драконья эссенция", "Double the Radius = Double the Fun!"→"Двойной радиус = двойное веселье!".\n` +
  `- KEEP IN LATIN (ru = exactly the en text) ONLY for: chemical formulas (C9H8O4...NaCl..., NaK), ` +
  `acronyms (BIOS, TFFT, MABS, IAADDS, RAM, HSS-G, HSS-S, P-507, D-O-B, N.N.Q.Q.N.Q.Q), ` +
  `mod names (Applied Energistics, Better Questing, Plague Inc.), Latin item names (Salis Mundus, Lapotron, Loonium), ` +
  `person/product names (Jeremy Fragrance, Nimbus 1999), and symbol-only titles (「 」).\n` +
  `- For Daft Punk reference "Harder, Better, Faster, Stronger... Pt 2 in UHV" → "Тяжелее, лучше, быстрее, сильнее... Часть 2 в UHV".\n` +
  `- Mixed name+acronym like "Rock Cutter LV" → "Каменорез LV".\n\n` +
  `ALL segments:\n` +
  `- Use glossary terms. Translate descriptions (field="desc") fully into fluent Russian; keep code snippets / ASCII reactor diagrams / single-letter legends verbatim.\n` +
  `- PRESERVE formatting EXACTLY with same counts: %n, %%, §x color codes (keep the SOURCE's codes — if source has §9§l, output starts §9§l), [note]/[warn]/[url]/[quest] tags; URL inside [url] byte-identical.\n` +
  `- Single-line output (%n for breaks).\n\n` +
  `Return {results:[{id, ru}]} for EVERY segment.`

const results = await parallel(idx.map((i) => () => {
  const file = `${base}/rt_${String(i).padStart(4, '0')}.json`
  return agent(prompt(file), { label: `rt:${i}`, phase: 'Repair', model: 'haiku', schema: SCHEMA })
    .then((r) => (r && r.results) ? r.results : [])
}))
const all = results.filter(Boolean).flat()
log(`round-2 produced ${all.length} translations`)
return { results: all }