# LLM Workflow-скрипты

Это скрипты для оркестратора [Claude Code Workflow](https://docs.claude.com/en/docs/claude-code)
(один субагент на батч-файл). Каждый агент читает свой `work/batches/<prefix>_NNNN.json`
(и при необходимости глоссарий), и возвращает структурированный JSON. Результат сохраняется
в `work/*_results.json` для последующего детерминированного слияния скриптами из `tools/`.

| Скрипт | Этап | Модель | Вход → выход |
|---|---|---|---|
| `01-glossary-extract.js` | термбаза | Haiku | `gloss_*` → `{terms}` → `work/gloss_raw.json` |
| `02-validate-translations.js` | валидация | Haiku | `val_*` → `{rework[]}` → `work/val_rework.json` |
| `03-translate-rework.js` | перевод | Haiku | `tr_*` + глоссарий → `{results}` → `work/tr_results.json` |
| `03b-translate-round2.js` | дочинка | Haiku | `rt_*` → `work/tr_round2_results.json` |
| `03c-translate-round3-fmt.js` | формат | Haiku | `r3_*` → `work/tr_round3_results.json` |
| `04-sonnet-validate-fix.js` | доработка | **Sonnet** | `sn_*` + глоссарий → `{results}` → `work/sonnet_results.json` |
| `05-markup-repair-haiku.js` | разметка | Haiku | `mk_*` → `work/markup_haiku_results.json` |
| `05b-markup-repair-sonnet.js` | разметка | **Sonnet** | `mk2_*` → `work/markup_sonnet_results.json` |

Аргументы (`args`) передаются при запуске Workflow, например:
`{ "base": "<abs>/work/batches", "count": <N>, "glossary": "<abs>/work/glossary_prompt.txt" }`

Полный порядок запуска и сценарий обновления — в [`../USAGE.md`](../USAGE.md).
