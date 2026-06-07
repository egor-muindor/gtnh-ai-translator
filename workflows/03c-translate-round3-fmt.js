export const meta = {
  name: 'translate-round3',
  description: 'Haiku formatting-repair for 4 strings with %n/tag count mismatches',
  phases: [{ title: 'FixFmt' }],
}
phase('FixFmt')
const SCHEMA = {
  type: 'object', required: ['results'],
  properties: { results: { type: 'array', items: {
    type: 'object', required: ['id', 'ru'],
    properties: { id: { type: 'string' }, ru: { type: 'string' } } } } },
}
const file = args.file
const prompt =
  `You are a Russian localizer fixing FORMATTING errors. Read ${file} — array of ` +
  `{id, en (English source), field, prev_attempt (current Russian, GOOD wording but broken formatting), qa_problem, src_newlines}.\n\n` +
  `For each: keep the good Russian wording of prev_attempt, but FIX the formatting so it EXACTLY matches the English source "en":\n` +
  `- The output MUST contain EXACTLY src_newlines occurrences of the %n marker, placed at the SAME structural positions (paragraph/line breaks) as in en. Count them carefully.\n` +
  `- Preserve ALL tags from en with identical count: [note][/note], [warn][/warn], [url][/url], [quest][/quest], and [sic]. If en has [sic], the output must include [sic] in the matching place.\n` +
  `- Keep §color codes, %% literals, and [url] link text byte-identical to en.\n` +
  `- Output a single-line value (real line breaks expressed only as %n).\n\n` +
  `Return {results:[{id, ru}]} for all items.`
const r = await agent(prompt, { label: 'fixfmt', phase: 'FixFmt', model: 'haiku', schema: SCHEMA })
return r || { results: [] }