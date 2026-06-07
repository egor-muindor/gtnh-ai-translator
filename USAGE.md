# Запуск и использование

Это руководство объясняет, как устроен конвейер, как его запускать и **как обновлять
перевод, когда выходит новая версия книги квестов или обновляется сборка**.

## Содержание
- [Архитектура](#архитектура)
- [Требования](#требования)
- [Файлы данных](#файлы-данных)
- [Сценарий обновления (новая версия квестов / сборки)](#сценарий-обновления)
- [Полный конвейер по шагам](#полный-конвейер-по-шагам)
- [Проверки качества](#проверки-качества)
- [Обновление viewer](#обновление-viewer)
- [Справочник по инструментам](#справочник-по-инструментам)

## Архитектура

Конвейер состоит из двух типов шагов:

1. **Детерминированные** (`tools/*.py`) — чистый Python 3, без зависимостей: парсинг
   `.lang`, QA-проверки, нарезка батчей, слияние, сборка итогового файла, отчёты.
2. **LLM-проходы** (`workflows/*.js`) — оркестрируются через
   [Claude Code Workflow](https://docs.claude.com/en/docs/claude-code): на каждый батч —
   один субагент, читает батч-файл и возвращает структурированный JSON. Распределение по
   моделям: **Haiku** — массовые операции, **Sonnet** — второй проход «валидация + правки»,
   **Opus** — сборка viewer.

Между LLM-проходами всегда стоит детерминированный **QA-гейт** (`tools/qa.py`): целостность
разметки (`%n`, `§`-коды, `[note]/[warn]/[url]/[quest]`), утечки английского, пустые/
непереведённые строки. Любой результат LLM, не прошедший гейт, откатывается к предыдущей
рабочей версии — качество не деградирует.

## Требования

- **Python 3.9+** (без внешних пакетов) — для всех детерминированных шагов.
- **Claude Code CLI** с доступом к моделям Haiku/Sonnet/Opus — только для LLM-проходов.
- `git`, `gh` (опционально) — для публикации/релизов.

Промежуточные данные складываются в `work/` (в репозиторий не коммитятся) и пересоздаются
скриптами.

## Файлы данных

| Файл | Роль |
|---|---|
| `template.lang` | Английский источник (вход) — берётся из новой версии книги квестов |
| `ru_RU.original.lang` | Текущий русский перевод (вход) — то, что улучшаем |
| `ru_RU.lang` | Итоговый перевод (выход) |
| `tools/glossary_seed.json` | Ручной глоссарий-затравка (приоритет при конфликте терминов) |
| `work/` | Все промежуточные данные (gitignored) |

## Сценарий обновления

Когда выходит **новая версия книги квестов** (новый `template.lang`) или **обновляется
сборка**, перевод обновляется так:

1. **Подготовь входы:**
   - Положи новый английский файл в `template.lang`.
   - В `ru_RU.original.lang` положи **текущий лучший перевод** — обычно это прошлый
     `ru_RU.lang` из этого репозитория (плюс, если у новой версии есть официальный
     ru-файл с новыми строками, можно взять его).

   > При обновлении меняются только часть строк: новые квесты появятся как «отсутствующие»
   > (будут переведены с нуля), изменённые английские тексты попадут в список на доработку,
   > а неизменные хорошие переводы останутся как есть. Порядок и комментарии сохраняются.

2. **Прогони конвейер** — см. [Полный конвейер по шагам](#полный-конвейер-по-шагам).
   Можно прогнать целиком; объём LLM-работы пропорционален числу реально изменившихся строк.

3. **Проверь и собери:**
   ```bash
   python3 tools/verify_final.py     # структура + QA
   python3 tools/markup_check.py      # сохранность разметки
   python3 tools/final_report.py      # обновит FINAL_SUMMARY.md
   ```

4. **Обнови viewer и опубликуй:**
   ```bash
   python3 tools/gen_review.py && cp work/review_data.json docs/review_data.json
   git add -A && git commit -S -m "feat: update translation for questbook <версия>"
   git push
   gh release create v<X.Y.Z> --notes-file <notes> ru_RU.lang   # новый релиз
   ```

## Полный конвейер по шагам

Все команды — из корня репозитория. LLM-шаги запускаются инструментом **Workflow** в Claude
Code со скриптом из `workflows/` и `args = { base, count, glossary }`, где `base` —
абсолютный путь к `work/batches`, `count` — число батчей (его печатает `tools/batch.py`),
`glossary` — абсолютный путь к `work/glossary_prompt.txt`. Результат каждого Workflow
сохраняется в указанный `work/*_results.json` (из поля `result` его output-файла).

```bash
# 0. Сегментация + автоматическая классификация качества (детерминированно)
python3 tools/prep.py            # -> work/segments.json, sets.json, tm.json

# 1. ГЛОССАРИЙ (Haiku)
python3 tools/batch.py glossary  # -> work/batches/gloss_* (печатает count)
#   Workflow: workflows/01-glossary-extract.js  -> сохранить terms в work/gloss_raw.json
python3 tools/agg_glossary.py    # -> tools/glossary.json/.md, work/glossary_prompt.txt

# 2. ВАЛИДАЦИЯ (Haiku)
python3 tools/batch.py validate  # -> work/batches/val_*
#   Workflow: workflows/02-validate-translations.js -> work/val_rework.json
python3 tools/build_rework.py    # -> work/rework_detail.json, rework_keys.json
python3 tools/agg_validation.py  # -> VALIDATION_REPORT (work/report.md)

# 3. ПЕРЕВОД проблемных + недостающих (Haiku)
python3 tools/batch.py translate # -> work/batches/tr_*
#   Workflow: workflows/03-translate-rework.js -> work/tr_results.json
python3 tools/finalize.py        # QA-гейт -> work/translations.json, tr_qa_fail.json; сборка
#   При наличии work/tr_qa_fail.json — раунды дочинки:
#     python3 tools/batch.py retry  ;  Workflow 03b -> work/tr_round2_results.json
#     (формат-фиксы)               ;  Workflow 03c -> work/tr_round3_results.json
#   затем повторно python3 tools/finalize.py

# 4. ДОРАБОТКА второй моделью (Sonnet)
python3 tools/batch.py sonnet    # -> work/batches/sn_* (≈60 сегм./батч, ~50 агентов)
#   Workflow: workflows/04-sonnet-validate-fix.js -> work/sonnet_results.json
python3 tools/sonnet_merge.py    # QA-gated слияние поверх Haiku-базы

# 5. ПОЧИНКА РАЗМЕТКИ (§-коды/%%)
python3 tools/fix_markup.py      # детерминированно -> work/markup_fixes.json + todo
#   при остатке: Workflow 05 (Haiku) и/или 05b (Sonnet) по work/batches/mk_*, mk2_*
#   результаты -> work/markup_haiku_results.json, work/markup_sonnet_results.json

# 6. ДЕТЕРМИНИРОВАННАЯ ФИНАЛЬНАЯ СБОРКА
python3 tools/reconstruct_final.py  # собирает финал из всех артефактов -> ru_RU.lang
python3 tools/verify_final.py       # проверки
python3 tools/markup_check.py       # разметка
python3 tools/final_report.py       # -> FINAL_SUMMARY.md
```

`reconstruct_final.py` детерминированно пересобирает итог из сохранённых артефактов
(Haiku-база → Sonnet-правки → починка разметки → нормализация `%`), так что финал
воспроизводим без повторного вызова LLM.

## Проверки качества

```bash
python3 tools/verify_final.py [файл]   # все ключи на месте, нет дублей, QA-ошибки
python3 tools/markup_check.py [файл]    # §-коды/%n/теги/url/% против источника
```

QA-гейт считает реальными дефектами только: сломанную разметку (`%n`/теги/url), «голый»
одиночный `%`, утечку английской прозы, пустые строки. Латинские имена собственные
(формулы, аббревиатуры, названия модов) и `%%`-расхождения дефектами **не** считаются.

## Обновление viewer

```bash
python3 tools/gen_review.py                       # -> work/review_data.json (изменённые квесты)
cp work/review_data.json docs/review_data.json    # docs/ публикуется на GitHub Pages
```

Viewer (`docs/`) статичен и читает `review_data.json` относительным путём — работает и
локально (`cd docs && python3 -m http.server 8765`), и на GitHub Pages.

## Справочник по инструментам

| Скрипт | Назначение |
|---|---|
| `tools/langlib.py` | Парсер/сериализатор `.lang` (идемпотентный; нормализует «битые» многострочные значения) |
| `tools/qa.py` | QA: целостность разметки + детектор машинного перевода (служебные слова vs имена собственные) |
| `tools/prep.py` | Строит сегменты, наборы (good/broken/suspect/missing), translation memory |
| `tools/scan.py` | Эвристический скан + выгрузка пар (диагностика) |
| `tools/batch.py` | Нарезка батчей по символьному бюджету: `glossary`/`validate`/`translate`/`sonnet`/`retry` |
| `tools/agg_glossary.py` | Сводит сырые термины в глоссарий (majority vote) + затравка |
| `tools/agg_validation.py` | Сводит вердикты валидации в отчёт |
| `tools/build_rework.py` | Определяет режим правки (fresh/fix) для каждой строки |
| `tools/finalize.py` | QA-гейт переводов + сборка |
| `tools/sonnet_merge.py` | QA-gated слияние правок Sonnet поверх Haiku |
| `tools/fix_markup.py` | Детерминированная починка §-кодов (ведущие коды у названий) |
| `tools/merge_markup_llm.py` | Слияние LLM-починки разметки по правилу «badness» |
| `tools/reconstruct_final.py` | Детерминированная финальная сборка из артефактов |
| `tools/build.py` | Ассемблер: патчит `ru_RU.original.lang`, вставляет недостающие на места |
| `tools/verify_final.py`, `tools/markup_check.py` | Проверки структуры и разметки |
| `tools/gen_review.py` | Генерирует данные для viewer |
| `tools/final_report.py` | Генерирует `FINAL_SUMMARY.md` |
| `workflows/*.js` | LLM-проходы для Claude Code Workflow (см. [`workflows/README.md`](workflows/README.md)) |
