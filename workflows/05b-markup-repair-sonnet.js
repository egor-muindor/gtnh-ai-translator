export const meta = {
  name: 'markup-repair-sonnet',
  description: 'Sonnet fixes §-code/%% markup in 18 strings to exactly match the English source',
  phases: [{ title: 'Markup2' }],
}
phase('Markup2')
const SCHEMA = {
  type: 'object', required: ['results'],
  properties: { results: { type: 'array', items: {
    type: 'object', required: ['id', 'ru'],
    properties: { id: { type: 'string' }, ru: { type: 'string' } } } } },
}
const file = args.file
const prompt =
  `You are fixing ONLY text-markup tokens (not wording) in Russian Minecraft questbook strings. ` +
  `Read ${file} — array of {id, en (English source), cur (current Russian; KEEP its wording), fix (exactly which tokens are off)}.\n\n` +
  `For each item return ru = the SAME Russian wording as "cur", but with the §-color codes and %% adjusted so the token inventory EXACTLY matches "en":\n` +
  `- Match the §-codes of en exactly (same codes, same counts). Wrap the corresponding Russian words/phrases the way en wraps the matching English ones. ` +
  `If en wraps N separate segments with §x...§r, your output must have the same N §x...§r pairs around the equivalent Russian segments. ` +
  `For obfuscated §k...§r runs, reproduce the same number of §k...§r pairs around equivalent short Russian fragments.\n` +
  `- Match the %% count of en exactly: if en has more %% than yours, you dropped a percentage figure — restore it; if en has fewer, remove the extra literal %% you added (rephrase the number without a percent sign, keeping meaning).\n` +
  `- Do NOT change %n count, [note]/[warn]/[url]/[quest] tags, or [url] link text.\n` +
  `- Keep the Russian wording; only move/add/remove the markup tokens named in "fix".\n` +
  `- Single-line output (%n for breaks).\n\n` +
  `Return {results:[{id, ru}]} for ALL 18 items.`
const r = await agent(prompt, { label: 'markup2', phase: 'Markup2', model: 'sonnet', schema: SCHEMA })
return r || { results: [] }