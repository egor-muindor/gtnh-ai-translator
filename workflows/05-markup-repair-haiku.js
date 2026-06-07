export const meta = {
  name: 'markup-repair',
  description: 'Haiku fixes ONLY §-codes/%% in 23 descriptions to match the English source exactly',
  phases: [{ title: 'Markup' }],
}
phase('Markup')
const SCHEMA = {
  type: 'object', required: ['results'],
  properties: { results: { type: 'array', items: {
    type: 'object', required: ['id', 'ru'],
    properties: { id: { type: 'string' }, ru: { type: 'string' } } } } },
}
const file = args.file
const prompt =
  `You fix ONLY text-markup, not wording, in Russian questbook strings. Read ${file} — array of ` +
  `{id, en (English source), cur (current Russian — KEEP its wording), problems}.\n\n` +
  `For each item, return ru = the SAME Russian wording as "cur", but with markup corrected so it EXACTLY matches "en":\n` +
  `- §-color/format codes: the output must contain exactly the SAME §-codes as en (same set, same count), wrapping the corresponding translated words/segments in the same structural positions. Do not add or drop any §code. (e.g. if en colors a term §2word§r, color the matching Russian term the same way.)\n` +
  `- %% literal percent: the output must contain exactly the same number of %% as en.\n` +
  `- Keep %n count, [note]/[warn]/[url]/[quest] tags, and [url] link text identical to en (do not change them).\n` +
  `- Do NOT translate, rephrase, or otherwise alter the Russian wording — only move/restore markup tokens.\n` +
  `- Single-line output (%n for breaks).\n\n` +
  `Return {results:[{id, ru}]} for ALL items.`
const r = await agent(prompt, { label: 'markup', phase: 'Markup', model: 'haiku', schema: SCHEMA })
return r || { results: [] }