# GTNH ru_RU.lang — Validation Report

## Summary

- Total segments (template): 7586
- Good (passed automated QA): 4833
- Suspect (QA warnings, sent to LLM review): 1607
- Auto-flagged broken by deterministic QA: 742
- LLM-reviewed (good+suspect): 6440
  - kept: 4353
  - flagged for rework: 2087
- **Total to (re)translate: 2829** + 388 missing = 3217

### LLM rework by category

- mistranslation: 957
- formatting: 584
- fluency: 186
- untranslated: 154
- terminology: 121
- mixed_language: 67
- register: 11
- other: 7

### LLM rework by severity

- major: 1219
- minor: 868

## Rework list (LLM-flagged)

| key | sev | category | reason |
|---|---|---|---|
| quest.-1GoIXIXR029oc0Ge6sRGg.name | major | mistranslation | Незавершённый перевод: English слова 'Something' и 'Nothing' оставлены без перевода и смешаны с русским текстом вместо п |
| quest.-HJY3n4bQaiGgzsmFcVd6A.desc | major | mistranslation | Тяжёлый машинный перевод: смешаны английские и русские слова ('various carefully picked материалы', 'managed к создать') |
| quest.-HJY3n4bQaiGgzsmFcVd6A.name | major | mistranslation | 'Capturing Light' неправильно переведено как 'Capturing лёгкий' - 'лёгкий' означает 'лёгкий' в смысле веса, а не света;  |
| quest.-wpUfFlVT5GytSWoT6QAdg.desc | major | mistranslation | Тяжёлый машинный перевод: множество неиспользуемых английских слов ('stop', 'Given', 'malleable', 'Combing'), сломанная  |
| quest.0YrjX7i4QfeSo98gSE0SWg.desc | major | mistranslation | Тяжёлый машинный перевод с множеством неиспользуемых английских слов ('quantities', 'regions', 'space', 'exotic', 'matte |
| quest.3SzKMSj0StOAOzVmInDjZQ.name | major | mistranslation | Перевод не передает смысл оригинала. 'Варочная машина' вместо 'пивоварня', 'здоровенная' - неправильный тон. Должно быть |
| quest.3yz1WCEzQ_KQxW8p7_29-Q.desc | major | mistranslation | Текст наполнен английскими словами и фрагментами: 'struggling', 'keep up', 'infinity demand', 'Not к worry'. Это явная м |
| quest.49YfyyG5R8KKRRUKePOqfQ.desc | major | mistranslation | Машинный перевод с обилием английских фрагментов: 'acts just', 'expect', 'inject', 'crafted', 'большой накуада реактор'. |
| quest.4MzUrkH5QsWnE_4APuHhNg.desc | major | mistranslation | Машинный перевод: 'optical assembly является второй optical схема'. Должно быть полностью на русском: 'Оптическая сборка |
| quest.4v3YtOxvT8aWIwy7NEJNhw.desc | major | mistranslation | Машинный перевод с англоязычными вставками: 'Once вы managed к aquire', 'очень первый незерит', 'к создать rest'. Требуе |
| quest.52Yelo6KSLGumzXo-_F5DQ.desc | major | mistranslation | Машинный перевод: 'для short', 'primary материал', 'tricky к сделать', 'endgame материалы следует быть', 'coat Eternity  |
| quest.5rc45iPDSmqLbuvcioFDEQ.desc | major | mistranslation | Полностью неразборчивый машинный перевод. Оставлены нетранслируемые английские слова (situations, quantity, dedicated, a |
| quest.5vAyoCzxQkSRpjzlDNwtrw.desc | major | mistranslation | Машинный перевод с оставленными английскими словами (simultaneously, parallels). Грамматические ошибки ('для каждый' дол |
| quest.5vAyoCzxQkSRpjzlDNwtrw.name | major | untranslated | Слово 'Guzzling' полностью не переведено. Требуется полноценный перевод как 'Проглатывающий массивные объёмы газа' или а |
| quest.65KbJVn1T1CSpCdnGfBSqQ.desc | major | mistranslation | Грубый машинный перевод с множеством оставленных английских слов (subzero, ideal, substitute, billions, Helium, faster). |
| quest.6pH9sRoUSbCDG8eWqXS_ow.name | major | untranslated | Слова 'Smoke' и 'Warp Away' оставлены на английском. Полностью сломана грамматика. Требуется полный перевод. |
| quest.6rzcSbH2QY2cpChT2zLC_g.desc | major | mistranslation | Машинный перевод с оставленными английскими фразами (penultimate, Hopefully, know, checked out, wireless). Текст практич |
| quest.7YjYGaWnQ4uXqUOfMA0C9Q.desc | major | mistranslation | Машинный перевод с оставленными английскими фрагментами (Semifluid, запустить это через). Грамматически и синтаксически  |
| quest.8JcG3DR5QU6_FbhIWHm05g.name | major | mistranslation | 'Ultimate Voltages' не переведено, грамматическая ошибка ('требовать' вместо 'требуют'). Требуется полный переперевод на |
| quest.8OMu4RdgQhyZqXRid6n-Wg.desc | major | mistranslation | Машинный перевод с оставленными английскими фразами (super stable, completely indestructible, pour, infinity). Грамматик |
| quest.8OMu4RdgQhyZqXRid6n-Wg.name | major | untranslated | 'Another' и 'Steel' оставлены на английском. Требуется полный перевод как 'Ещё один тип стали' или аналогичный. |
| quest.AAAAAAAAAAAAAAAAAAAA4A.desc | major | mistranslation | Использован неправильный глагол 'сшить' (сшивать) вместо 'создать/скрафтить' для создания одежды; весь перевод содержит  |
| quest.AAAAAAAAAAAAAAAAAAAA4A.name | major | mistranslation | Переводит 'Witchy (Wo)man' как 'Очаровательная персона' - неправильно, должно быть 'Ведьма' или 'Ведьма (женщина)' |
| quest.AAAAAAAAAAAAAAAAAAAA5A.desc | major | mistranslation | Оставлены английские слова 'Reinforced Slates' и 'sigils' без перевода; разрушена грамматика: 'новый sigils' имеет ошибк |
| quest.AAAAAAAAAAAAAAAAAAAA5Q.desc | major | fluency | Дублирование 'ты когда ты построишь'; неловкие конструкции 'выращивать осколки' вместо 'растить' или 'выращивать'; общая |
| quest.AAAAAAAAAAAAAAAAAAAA6Q.desc | major | mistranslation | Искажает исходный смысл: переводит 'However you obtained them' как 'Вижу ты добыл' вместо 'Как бы ты их ни получил' или  |
| quest.AAAAAAAAAAAAAAAAAAAA7w.desc | major | mistranslation | Ошибочно переведено 'MV PLE' как 'MV Лазерный гравировщик'. Оригинальный текст говорит о нужде в MV PLE, а в переводе ук |
| quest.AAAAAAAAAAAAAAAAAAAA8g.name | major | formatting | Название содержит намеренно перевёрнутый текст (Balanced Shards sdrahS decnalaB). Перевод создаёт нечитаемую кашу (ллатс |
| quest.AAAAAAAAAAAAAAAAAAAACg.desc | major | mistranslation | Потеря смысла: 'It's GLOPPing time!' переведено как 'Время подкрепиться!', что теряет специфический термин и контекст. |
| quest.AAAAAAAAAAAAAAAAAAAACg.name | major | mistranslation | Грубая ошибка перевода: 'Rest in Pieces' (каламбур) переведено как 'Пакуйтесь с миром', что является бессмысленным и не  |
| quest.AAAAAAAAAAAAAAAAAAAADg.desc | major | mistranslation | Критическая ошибка: 'you can go to the Coins tab and buy them' переведено как 'Торговый автомат в Каменном веке' (торгов |
| quest.AAAAAAAAAAAAAAAAAAAAFg.name | major | formatting | Цветовой код изменён с §2 на §a (форматирование нарушено) |
| quest.AAAAAAAAAAAAAAAAAAAAFw.name | major | formatting | Цветовой код изменён с §2 на §a (форматирование нарушено) |
| quest.AAAAAAAAAAAAAAAAAAAAGA.name | major | formatting | Цветовой код изменён с §2 на §a (форматирование нарушено) |
| quest.AAAAAAAAAAAAAAAAAAAAGg.name | major | formatting | Цветовой код изменён с §2 на §a (форматирование нарушено) |
| quest.AAAAAAAAAAAAAAAAAAAAGw.name | major | formatting | Цветовой код изменён с §2 на §a (форматирование нарушено) |
| quest.AAAAAAAAAAAAAAAAAAAAHA.name | major | formatting | Цветовой код изменён с §2 на §a (форматирование нарушено) |
| quest.AAAAAAAAAAAAAAAAAAAAHQ.name | major | formatting | Цветовой код изменён с §2 на §a (форматирование нарушено) |
| quest.AAAAAAAAAAAAAAAAAAAAHg.name | major | formatting | Цветовой код изменён с §2 на §a (форматирование нарушено) |
| quest.AAAAAAAAAAAAAAAAAAAAHw.name | major | formatting | Цветовой код изменён с §2 на §a (форматирование нарушено) |
| quest.AAAAAAAAAAAAAAAAAAAAIA.name | major | formatting | Цветовой код изменён с §2 на §a (форматирование нарушено) |
| quest.AAAAAAAAAAAAAAAAAAAAIQ.name | major | formatting | Цветовой код изменён с §2 на §a (форматирование нарушено) |
| quest.AAAAAAAAAAAAAAAAAAAAIg.name | major | formatting | Цветовой код изменён с §2 на §a (форматирование нарушено) |
| quest.AAAAAAAAAAAAAAAAAAAAIw.name | major | formatting | Цветовой код изменён с §2 на §a (форматирование нарушено) |
| quest.AAAAAAAAAAAAAAAAAAAAJA.name | major | formatting | Цвет-код изменен: §2 (dark green) замещен на §a (light green). Это нарушает исходное форматирование и может изменить вне |
| quest.AAAAAAAAAAAAAAAAAAAAJQ.name | major | formatting | Цвет-код изменен: §2 (dark green) замещен на §a (light green). Нарушает исходное форматирование. |
| quest.AAAAAAAAAAAAAAAAAAAAJg.desc | major | mistranslation | Неправильный перевод 'bronze' - дважды переведено как 'бронза', но в исходном англ. первый раз упоминается 'Brass' (лату |
| quest.AAAAAAAAAAAAAAAAAAAAJg.name | major | formatting | Цвет-код изменен: §2 (dark green) замещен на §a (light green). Нарушает исходное форматирование. |
| quest.AAAAAAAAAAAAAAAAAAAAJw.desc | major | fluency | Ошибка в слове 'пожиток' - это устаревшее/редкое слово. Должно быть 'имущество', 'вещи', 'товары' или 'предметы'. Фраза  |
| quest.AAAAAAAAAAAAAAAAAAAAJw.name | major | formatting | Цвет-код изменен: §2 (dark green) замещен на §a (light green). Нарушает исходное форматирование. |
| quest.AAAAAAAAAAAAAAAAAAAAKA.desc | major | fluency | Фраза 'ты можешь перейти на следующий этап развития' должна быть 'ты можешь перейти на следующий уровень/ярус'. Также 'н |
| quest.AAAAAAAAAAAAAAAAAAAAKA.name | major | formatting | Цвет-код изменен: §3 (dark cyan) остался §c (red) в переводе. Нарушает исходное форматирование (должно быть §3, а не §c) |
| quest.AAAAAAAAAAAAAAAAAAAAKQ.desc | major | mistranslation | Неправильный перевод 'Baubles ring slots' - переведено как 'Baubles ячейки для колец', что неправильно. 'Baubles' - это  |
| quest.AAAAAAAAAAAAAAAAAAAAKQ.name | major | formatting | Цвет-код изменен: §2 (dark green) замещен на §a (light green). Нарушает исходное форматирование. |
| quest.AAAAAAAAAAAAAAAAAAAAKg.desc | major | mistranslation | Перевод 'cow trophy' некорректен - в контексте это не просто 'коровий трофей', это специальный игровой предмет из Minecr |
| quest.AAAAAAAAAAAAAAAAAAAAKg.name | major | formatting | Цвет-код изменен: §2 (dark green) замещен на §a (light green). Нарушает исходное форматирование. |
| quest.AAAAAAAAAAAAAAAAAAAAKw.name | major | formatting | Цвет-код изменен: §2 (dark green) замещен на §a (light green). Нарушает исходное форматирование. |
| quest.AAAAAAAAAAAAAAAAAAAALA.desc | major | fluency | Множество стилистических ошибок: 'ты хорошо справляешься' - неудачный перевод 'well done so far', 'нажёг' вместо 'накопи |
| quest.AAAAAAAAAAAAAAAAAAAALA.name | major | formatting | Цвет-код изменен: §3 (dark cyan) остался §c (red) в переводе. Нарушает исходное форматирование (должно быть §3, а не §c) |
| quest.AAAAAAAAAAAAAAAAAAAALQ.desc | major | mistranslation | Неправильный перевод 'creosote' - переведено как 'креозот', что верно, но контекст 'that you have accumulated' - 'что ты |
| quest.AAAAAAAAAAAAAAAAAAAALg.desc | major | mistranslation | Ошибка в переводе 'mold' - переведено как 'форма' (верно), но контекст '(you can make a nugget mold as well)' требует ут |
| quest.AAAAAAAAAAAAAAAAAAAALg.name | major | formatting | Цвет-код изменен: §3 (dark cyan) остался §c (red) в переводе. Нарушает исходное форматирование (должно быть §3, а не §c) |
| quest.AAAAAAAAAAAAAAAAAAAALw.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAMA.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAMQ.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAMg.desc | major | mistranslation | Ошибка перевода: 'за долговечность' неправильно - в оригинале 'no-durability' значит отсутствие износа, не долговечность |
| quest.AAAAAAAAAAAAAAAAAAAAMg.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAMw.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAANA.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAANQ.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAANg.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAANw.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAOA.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAOQ.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAOg.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAOw.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAPA.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAPQ.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAPg.desc | major | terminology | Неправильный термин 'кальцифицируется' для описания отложения минералов на бойлере. Следует использовать 'обрастает мине |
| quest.AAAAAAAAAAAAAAAAAAAAPg.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAPw.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAQA.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAQQ.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAQg.name | major | formatting | Цветовой код изменен с §3 (синий) на §c (красный), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAAQw.name | major | formatting | Код цвета повреждён: §3 изменён на §c. Кроме того, перевод 'Путаница с проводами' слабо передаёт суть оригинального кала |
| quest.AAAAAAAAAAAAAAAAAAAARA.name | major | formatting | Код цвета повреждён: §3 изменён на §c |
| quest.AAAAAAAAAAAAAAAAAAAARQ.name | major | formatting | Код цвета повреждён: §3 изменён на §c |
| quest.AAAAAAAAAAAAAAAAAAAARg.name | major | formatting | Код цвета повреждён: §3 изменён на §c |
| quest.AAAAAAAAAAAAAAAAAAAARw.name | major | formatting | Код цвета повреждён: §3 изменён на §c |
| quest.AAAAAAAAAAAAAAAAAAAASA.name | major | formatting | Код цвета повреждён: §3 изменён на §c |
| quest.AAAAAAAAAAAAAAAAAAAASQ.name | major | formatting | Код цвета повреждён: §3 изменён на §c |
| quest.AAAAAAAAAAAAAAAAAAAAUQ.desc | major | mistranslation | Начало предложения «...вселенная застынет» не соответствует английскому оригиналу «...with this great invention!». Перев |
| quest.AAAAAAAAAAAAAAAAAAAAUg.desc | major | terminology | Аббревиатуры КДП и КПД неясны и неправильны. КПД означает коэффициент полезного действия, а не доменную печь. Нужны прав |
| quest.AAAAAAAAAAAAAAAAAAAAVA.name | major | formatting | Цветовой код изменён с §3 (англ.) на §c (рус.), что нарушает оригинальное форматирование. Должен быть сохранён исходный  |
| quest.AAAAAAAAAAAAAAAAAAAAWA.name | major | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAWg.name | major | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAWw.name | major | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAXA.name | major | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAXQ.name | major | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAXg.name | major | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAXw.name | major | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAYA.name | major | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAYQ.name | major | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAYg.name | major | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAZA.name | major | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAZQ.name | major | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAZw.desc | major | mistranslation | "MV электролизер" - ошибка, имеется в виду машина-пила или кусачка, не электролизер; "твоих текущих колец" - бессмыслица |
| quest.AAAAAAAAAAAAAAAAAAAA_A.desc | major | mistranslation | "созданием магических предметов и наполнением их аспектами" - неточно; в оригинале говорится о слабой и сильной инфузии, |
| quest.AAAAAAAAAAAAAAAAAAAA_g.desc | major | mistranslation | "перегонный куб" - неверный перевод; в оригинале "essentia filter", не куб; "баночная бирка" - странный перевод "Label"; |
| quest.AAAAAAAAAAAAAAAAAAAA_w.desc | major | mistranslation | "греть им своей тигель" - грамматически неправильно и неточно; исходный текст "You can use it under your crucible" означ |
| quest.AAAAAAAAAAAAAAAAAAAAaA.desc | major | mistranslation | Перевод полностью переписан и не соответствует оригиналу; в оригинале нет упоминания о "первой вкладке" и квесте "Что эт |
| quest.AAAAAAAAAAAAAAAAAAAAfQ.name | major | mistranslation | 'Upgrading Intensifies' (интернет-мем) неправильно переведён как 'Трясёт от несовершенства?' — потеряна суть |
| quest.AAAAAAAAAAAAAAAAAAAAgw.desc | major | mistranslation | 'диод соответствующего проводу напряжения' неправильно переведено; должно быть 'ядро механизма соответствующего напряжен |
| quest.AAAAAAAAAAAAAAAAAAAAhA.desc | major | formatting | Ошибка в таблице: 'Хутч' строка содержит '36' вместо '360' (RF/mb) — повреждение формата таблицы |
| quest.AAAAAAAAAAAAAAAAAAAAiQ.desc | major | terminology | Использовано слово 'трубы' вместо 'кондуиты'. В исходном тексте говорится о conduits, а не о pipes. |
| quest.AAAAAAAAAAAAAAAAAAAAiw.desc | major | mistranslation | Опущена важная часть смысла 'unlock powerful features' - в переводе только 'её можно улучшить' без упоминания о раскрыти |
| quest.AAAAAAAAAAAAAAAAAAAAjA.desc | major | mistranslation | The Ender переведён как 'Тёмный меч', но это инструмент для увеличения выпадения черепов иссушителей и жемчуга Эндера -  |
| quest.AAAAAAAAAAAAAAAAAAAAjQ.name | major | formatting | Код цвета изменён с §9 (синий) на §5 (фиолетовый) - нарушение форматирования. |
| quest.AAAAAAAAAAAAAAAAAAAAkA.name | major | formatting | Код цвета изменён с §9 (синий) на §5 (фиолетовый) - нарушение форматирования. |
| quest.AAAAAAAAAAAAAAAAAAAAkg.name | major | formatting | Код цвета изменён с §9 (синий) на §5 (фиолетовый) - нарушение форматирования. |
| quest.AAAAAAAAAAAAAAAAAAAAlw.name | major | formatting | Код цвета изменён с §9 (синий) на §5 (фиолетовый) - нарушение форматирования. |
| quest.AAAAAAAAAAAAAAAAAAAApg.desc | major | mistranslation | Названию модуля Soularium неправильно дана русская интерпретация 'призрачный сплав'. Названия модов и сплавов должны ост |
| quest.AAAAAAAAAAAAAAAAAAAApg.name | major | mistranslation | Названию модуля Soularium неправильно дана русская интерпретация 'призрачный сплав'. Названия модов и сплавов должны ост |
| quest.AAAAAAAAAAAAAAAAAAAArQ.name | major | mistranslation | "Tier 3 Base" переведено как "Основание турели 3 уровня" (base of turret), вместо "База 3-го уровня" (base tier 3) |
| quest.AAAAAAAAAAAAAAAAAAAAsA.name | major | formatting | Код цвета изменен с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAAtA.desc | major | mistranslation | Перепутаны числа: "2032 стака 63-х различных предметов" вместо "1040 стаков 63 различных предметов" |
| quest.AAAAAAAAAAAAAAAAAAAAtQ.desc | major | mistranslation | Перевод полностью не соответствует исходному тексту. Вместо объяснения о крафте кристаллов дан какой-то случайный текст  |
| quest.AAAAAAAAAAAAAAAAAAAAuQ.desc | major | mistranslation | В переводе добавлена информация, отсутствующая в исходном тексте: "ножей из истинного кварца/кварца Нижнего мира" не упо |
| quest.AAAAAAAAAAAAAAAAAAAAug.name | major | formatting | Код цвета изменен с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAAuw.name | major | formatting | Код цвета изменен с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAAvA.name | major | formatting | Код цвета изменен с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAAvQ.name | major | formatting | Код цвета изменен с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAAxg.desc | major | mistranslation | Критическая ошибка: русский текст содержит английские слова, вперемешку с русским, в явно неправильной форме ("They're т |
| quest.AAAAAAAAAAAAAAAAAAAB-Q.desc | major | mistranslation | Механический перевод с английскими словами: 'scanning' и 'analyzing' не переведены; неправильная грамматика ('вы можете' |
| quest.AAAAAAAAAAAAAAAAAAAB0A.desc | major | mistranslation | Сильно повреждённый машинный перевод: смешивание англ/рус ('Yes', 'schematic', 'perfect', 'Whatever alien civilization', |
| quest.AAAAAAAAAAAAAAAAAAAB4g.desc | major | terminology | Слово 'лагучих' не существует в русском языке - должно быть что-то вроде 'лагоёмких' или описание способа уменьшения лаг |
| quest.AAAAAAAAAAAAAAAAAAAB4w.desc | major | mistranslation | Слово 'мотыготопор' - бессмысленное сочетание. 'Mattock' должен быть переведен как 'кирка' или 'мотыга', но не как гибри |
| quest.AAAAAAAAAAAAAAAAAAAB6g.name | major | mistranslation | Смешанный язык - 'Obscenely Dangerous ядерный топливо: Core'. Неправильный падеж ('топливо' вместо 'топлива'), английско |
| quest.AAAAAAAAAAAAAAAAAAABBQ.name | major | untranslated | Смешанные английский и русский языки. Должно быть: 'Потрясающий магический проводник' или подобное полностью русское наз |
| quest.AAAAAAAAAAAAAAAAAAABBw.desc | major | mistranslation | Крайне низкое качество машинного перевода: множество нетранслирированных английских слов, нарушена грамматика и синтакси |
| quest.AAAAAAAAAAAAAAAAAAABBw.name | major | mistranslation | Неправильно составленное название. Правильный вариант: 'Серебряный жезл наконец' или 'Наконец-то серебряный жезл'. |
| quest.AAAAAAAAAAAAAAAAAAABCQ.name | major | untranslated | Смешанный язык (строчное 'создание' с 'Better' и 'жезл'). Должно быть: 'Создание лучшего жезла'. |
| quest.AAAAAAAAAAAAAAAAAAABCg.desc | major | mistranslation | Массивный машинный перевод: множество нетранслирированных слов (stainless, steel, screws, vis, energies, alloy и т.д.),  |
| quest.AAAAAAAAAAAAAAAAAAABCg.name | major | untranslated | Полностью нетранслировано и смешано с английским. Должно быть: 'Энергичные винты для завершения нового жезла'. |
| quest.AAAAAAAAAAAAAAAAAAABEg.desc | major | untranslated | Нетранслированное английское слово 'stuff', нарушена грамматика. Должно быть: 'Этот материал интересен... Может быть, я  |
| quest.AAAAAAAAAAAAAAAAAAABEg.name | major | mistranslation | Неправильный порядок слов и склонение. Должно быть: 'Материал реактора' или 'Реакторный материал'. |
| quest.AAAAAAAAAAAAAAAAAAABEw.desc | major | mistranslation | Массивный машинный перевод: множество нетранслирированных английских слов, нарушена грамматика и синтаксис. Требует полн |
| quest.AAAAAAAAAAAAAAAAAAABFA.name | major | untranslated | Полностью нетранслировано. Должно быть: 'Доведи это до конца' или 'Прнеси домой'. |
| quest.AAAAAAAAAAAAAAAAAAABFQ.name | major | untranslated | Смешанный язык. 'Automated' и 'Recharging' не переведены. Должно быть: 'Автоматическая зарядка жезла'. |
| quest.AAAAAAAAAAAAAAAAAAABFg.desc | major | untranslated | Множество нетранслирированных английских слов (totally, yourself, centi-vis, things, transport). Нарушена грамматика. |
| quest.AAAAAAAAAAAAAAAAAAABGA.desc | major | mistranslation | Множество нетранслирированных английских слов (Eyes, spidery, Nasty, Eldritch). Нарушена грамматика и смысл из-за машинн |
| quest.AAAAAAAAAAAAAAAAAAABGQ.desc | major | mistranslation | Массивный машинный перевод: множество нетранслирированных слов (Fools, book, guide, precious, bookstore, occasionally, f |
| quest.AAAAAAAAAAAAAAAAAAABGw.desc | major | mistranslation | Множество нетранслирированных слов (No, nooo, key, keeey, tablet, door, precious) и нарушена грамматика ('они иметь скры |
| quest.AAAAAAAAAAAAAAAAAAABHQ.desc | major | mistranslation | Множество нетранслирированных английских слов (reason, decided, infuse, darkness, promising, research, warp) и нарушена  |
| quest.AAAAAAAAAAAAAAAAAAABHg.desc | major | mistranslation | Обширная утечка английских слов: metal, appealing, feel comfortable, holding, go wrong, protect. Явные признаки машинног |
| quest.AAAAAAAAAAAAAAAAAAABHw.desc | major | mistranslation | Множество необработанных английских слов: Now, call, storage, weird, sounds, nothing. Грамматические ошибки, явные призн |
| quest.AAAAAAAAAAAAAAAAAAABIA.desc | major | mistranslation | Утечка английских слов: Mortals, Pah, know, REAL, advance, food. Неправильное использование 'энергия' вместо 'power'. Гр |
| quest.AAAAAAAAAAAAAAAAAAABIQ.desc | major | mistranslation | Обширная утечка английского текста во всем описании при частичном переводе. Грамматические ошибки, нарушенная структура  |
| quest.AAAAAAAAAAAAAAAAAAABJA.desc | major | mistranslation | Утечка английских слов: somewhat, better, straw, considered weak, ideal, little cutie, farms. Явные признаки машинного п |
| quest.AAAAAAAAAAAAAAAAAAABJQ.desc | major | mistranslation | Множество необработанных английских слов: break, bones, guys, hard, rock, Insert audience laugh, protect, claim. Граммат |
| quest.AAAAAAAAAAAAAAAAAAABJg.desc | major | mistranslation | Утечка английских слов: Highly durable, carry, considered, chisel, thaumium, right kind. Неправильное использование 'тир |
| quest.AAAAAAAAAAAAAAAAAAABKA.desc | major | mistranslation | Отсутствует начало фразы 'Of course'. Утечка английских слов: know, Right?. Неполный перевод. |
| quest.AAAAAAAAAAAAAAAAAAABKw.desc | major | mistranslation | Обширная утечка английских слов: Manually, checking, jars, tedious, infuse, bunch, Luckily, locus, monitors, targeted, c |
| quest.AAAAAAAAAAAAAAAAAAABLA.desc | major | mistranslation | Множество необработанных английских слов: removing, flux, generated, Shovel, Purifier, help, must-have, concept, doing.  |
| quest.AAAAAAAAAAAAAAAAAAABLQ.desc | major | mistranslation | Обширная утечка английских слов по всему тексту: play, magic, warned, fires, dangerous, patch, snow, spread, disabled, c |
| quest.AAAAAAAAAAAAAAAAAAABLQ.name | major | mistranslation | Неправильный перевод с неправильным порядком слов и необработанным 'Not'. Должно быть 'Просто не возможно...' или аналог |
| quest.AAAAAAAAAAAAAAAAAAABMA.desc | major | mistranslation | Множество необработанных английских слов: finally, device, actually, choose, which, enchantments, Powered, vis, powerful |
| quest.AAAAAAAAAAAAAAAAAAABMw.desc | major | mistranslation | Утечка английских слов: pearl, interesting, effects, Not только, voices, almost, gone, somehow, expanded, perception, fe |
| quest.AAAAAAAAAAAAAAAAAAABNg.desc | major | mistranslation | Машинный перевод: 'к сделать использовать' неправильно, 'к fullest extent' - английский не переведён, 'unleash его скрыт |
| quest.AAAAAAAAAAAAAAAAAAABNw.desc | major | mistranslation | Целое предложение на смешанном языке: 'это будет never break' - английское 'never break' не переведено, грамматические о |
| quest.AAAAAAAAAAAAAAAAAAABOA.desc | major | mistranslation | Те же проблемы машинного перевода: 'к сделать использовать', 'к full extent' - английский не переведён, 'скрытый энергия |
| quest.AAAAAAAAAAAAAAAAAAABOQ.desc | major | mistranslation | Грамматическая ошибка: 'они будет' (неверное согласование числа), 'never break' не переведено. |
| quest.AAAAAAAAAAAAAAAAAAABOg.desc | major | mistranslation | Повторяющиеся проблемы: 'к сделать использовать', 'к full extent' - английский не переведён, грамматические ошибки. |
| quest.AAAAAAAAAAAAAAAAAAABOw.desc | major | mistranslation | 'это будет never break' - смешанный язык, английское 'never break' не переведено. |
| quest.AAAAAAAAAAAAAAAAAAABPQ.desc | major | mistranslation | Повторяющиеся ошибки машинного перевода во всём тексте. |
| quest.AAAAAAAAAAAAAAAAAAABPg.desc | major | mistranslation | 'они будет never break' - грамматическая ошибка и untranslated английский. |
| quest.AAAAAAAAAAAAAAAAAAABQA.desc | major | mistranslation | Массивный машинный перевод: 'через combining ichor' - untranslated, 'something новый' - смешанный язык, 'его магия condu |
| quest.AAAAAAAAAAAAAAAAAAABRA.desc | major | mistranslation | Повторяющиеся ошибки: 'к сделать использовать', 'к full extent' - не переведено. |
| quest.AAAAAAAAAAAAAAAAAAABRQ.desc | major | mistranslation | Повторяющиеся ошибки машинного перевода. |
| quest.AAAAAAAAAAAAAAAAAAABRg.desc | major | mistranslation | Повторяющиеся ошибки машинного перевода. |
| quest.AAAAAAAAAAAAAAAAAAABRw.desc | major | mistranslation | Повторяющиеся ошибки машинного перевода. |
| quest.AAAAAAAAAAAAAAAAAAABSg.desc | major | mistranslation | Множество ошибок: 'этот можно используется' - неправильная грамматика, 'к go back' - смешанный язык, 'leftmost один' - u |
| quest.AAAAAAAAAAAAAAAAAAABUA.name | major | mistranslation | Смешанный язык: 'Usable' и 'Soup' оставлены на английском без попытки перевода; получилось 'вероятно Usable для Soup' вм |
| quest.AAAAAAAAAAAAAAAAAAABUw.desc | major | mistranslation | Сильно повреждено машинным переводом: 'для circle магия, вы нужно... circle, obviously' - остались целые слова на англий |
| quest.AAAAAAAAAAAAAAAAAAABVA.desc | major | mistranslation | Явно машинный перевод с повреждениями: 'через infusing stone с fiery магия' - смешанный английский; 'эти stones можно ис |
| quest.AAAAAAAAAAAAAAAAAAABVQ.desc | major | mistranslation | Машинный перевод: 'вы tried, это не fly' - смешанный язык; 'не сделать любой OINK sounds' - неправильная грамматика и ло |
| quest.AAAAAAAAAAAAAAAAAAABVg.desc | major | mistranslation | Смешанный язык: 'Not как хороший' оставлено на английском; '2000\'ish model' - неправильно передано; 'но всё ещё "someho |
| quest.AAAAAAAAAAAAAAAAAAABWQ.desc | major | mistranslation | Машинный перевод: 'кто нужно antidote?' - неправильная грамматика и смешанный язык; 'Now с free fertilizer' не переведен |
| quest.AAAAAAAAAAAAAAAAAAABXQ.desc | major | mistranslation | Машинный перевод: 'Sometimes это можно troublesome' - смешанный язык и неправильная грамматика; 'вы получить настроить д |
| quest.AAAAAAAAAAAAAAAAAAABXQ.name | major | mistranslation | Смешанный язык: оставлены 'Vampire' и 'Dress Like Fancy Person' без перевода; должно быть полностью на русском |
| quest.AAAAAAAAAAAAAAAAAAABXg.desc | major | mistranslation | Машинный перевод: 'naquadria пчела. Это bit tricky' - смешанный язык; 'и до вы ask' неправильно; 'линия к refine это' -  |
| quest.AAAAAAAAAAAAAAAAAAABXw.desc | major | mistranslation | Машинный перевод: 'manganese пчела. Not очень полезный' - смешанный язык; 'один step closer' не переведено; 'больше inte |
| quest.AAAAAAAAAAAAAAAAAAABYQ.desc | major | mistranslation | Машинный перевод: 'iridium пчела' не переведено; 'малый объём pure osmium' неправильно; 'с эти соты и уран один' - нелог |
| quest.AAAAAAAAAAAAAAAAAAABYg.desc | major | mistranslation | Машинный перевод: 'enderium пчела' не переведено; 'в particularly interesting' неправильная грамматика; 'blinding скорос |
| quest.AAAAAAAAAAAAAAAAAAABZA.desc | major | mistranslation | Машинный перевод: 'Arid пчела species. Useless вы say?' - смешанный язык, не переведено |
| quest.AAAAAAAAAAAAAAAAAAAB_Q.desc | major | mistranslation | Машинный перевод с множеством оставленных английских терминов (random trait, empty gene sample, labware), нарушена грамм |
| quest.AAAAAAAAAAAAAAAAAAAB_w.desc | major | mistranslation | Машинный перевод: не переведены ключевые термины (inject, alter, aspect, pristine, ignoble), нарушена грамматика (с этот |
| quest.AAAAAAAAAAAAAAAAAAABaA.desc | major | untranslated | Оставлены непереведённые английские фразы (Desolate species, Maybe), смешанный язык |
| quest.AAAAAAAAAAAAAAAAAAABaQ.desc | major | mistranslation | Машинный перевод: неверная грамматика (является extremely полезный, являются в ZPM, может help вы с тот) |
| quest.AAAAAAAAAAAAAAAAAAABag.desc | major | mistranslation | Машинный перевод с грамматическими ошибками (remarkable пчела, thought americium может только быть получено из термояд) |
| quest.AAAAAAAAAAAAAAAAAAABbA.desc | major | mistranslation | Машинный перевод: смешанный язык (вы не like fighting, play на peaceful), грамматические ошибки |
| quest.AAAAAAAAAAAAAAAAAAABbw.desc | major | mistranslation | Неверная грамматика (эти сделать), не переведено слово 'fiery' |
| quest.AAAAAAAAAAAAAAAAAAABcA.desc | major | mistranslation | Машинный перевод: оставлены английские слова (magical, below apiary), грамматические ошибки (к быть bred) |
| quest.AAAAAAAAAAAAAAAAAAABcQ.desc | major | mistranslation | Машинный перевод: смешанный язык (я не know), неправильные конструкции (way к делать это) |
| quest.AAAAAAAAAAAAAAAAAAABcg.desc | major | untranslated | Английская часть 'It's not much steel' оставлена непереведённой в начале предложения |
| quest.AAAAAAAAAAAAAAAAAAABcw.desc | major | mistranslation | Машинный перевод: смешанный язык (к быть honest), не переведено 'particularly strong' |
| quest.AAAAAAAAAAAAAAAAAAABdA.desc | major | mistranslation | Машинный перевод: грамматические ошибки (bit misnamed, даёт вы является) |
| quest.AAAAAAAAAAAAAAAAAAABeg.desc | major | mistranslation | Machine-translated with extensive untranslated English mixed into Russian (Given fact, kind, plug, out, something, fit,  |
| quest.AAAAAAAAAAAAAAAAAAABfg.desc | major | mistranslation | Machine-translated garbled text with untranslated English (Really, awesome является тот, just к быть sure); broken gramm |
| quest.AAAAAAAAAAAAAAAAAAABfw.desc | major | mistranslation | Machine-translated with untranslated English; grammatical errors (что в мир является, containment материал, червоточина  |
| quest.AAAAAAAAAAAAAAAAAAABgA.desc | major | mistranslation | Garbled machine translation with untranslated English (course, condenser, didn't think тот); incomplete sentence |
| quest.AAAAAAAAAAAAAAAAAAABhg.desc | major | mistranslation | Machine-translated with untranslated English (multiplies все источник через 3x, пчела является доступный - wrong gender  |
| quest.AAAAAAAAAAAAAAAAAAABhw.desc | major | mistranslation | Machine-translated with untranslated English (Quite interesting пчела, integrate это, osmium обработка); broken grammar |
| quest.AAAAAAAAAAAAAAAAAAABiw.desc | major | mistranslation | Machine-translated with untranslated English (много effort, к получить, quite handy, hypogen, late game); broken grammar |
| quest.AAAAAAAAAAAAAAAAAAABlg.desc | major | fluency | Грамматическая ошибка: 'Эти действительно полезные' неправильно. Должно быть 'Они действительно полезны' или 'Это действ |
| quest.AAAAAAAAAAAAAAAAAAABmQ.desc | major | mistranslation | Полностью переведено машиной с английскими словами в русском тексте. Требуется полная переработка. |
| quest.AAAAAAAAAAAAAAAAAAABmw.desc | major | mistranslation | Смешанный английский и русский языки, машинный перевод с английскими словами. Требуется полная переработка. |
| quest.AAAAAAAAAAAAAAAAAAABng.desc | major | mistranslation | Полностью переведено машиной с английскими словами, разбитая грамматика. Требуется полная переработка. |
| quest.AAAAAAAAAAAAAAAAAAABnw.desc | major | mistranslation | Смешанный английский и русский языки, машинный перевод. Требуется полная переработка. |
| quest.AAAAAAAAAAAAAAAAAAABog.desc | major | mistranslation | Смешанный английский и русский языки, машинный перевод с ошибками грамматики. Требуется полная переработка. |
| quest.AAAAAAAAAAAAAAAAAAABqQ.desc | major | mistranslation | Машинный перевод, много английского текста оставлено нетронутым. 'Necessary', 'rituals', 'technically', 'just', 'diviner |
| quest.AAAAAAAAAAAAAAAAAAABqg.desc | major | mistranslation | Плохой машинный перевод. Много английского осталось ('Poking', 'slates', 'runes', 'sacrificial', 'gain', 'mobs', 'yourse |
| quest.AAAAAAAAAAAAAAAAAAABqw.desc | major | mistranslation | Машинный перевод. Английское слово 'rune' не переведено. Грамматические ошибки ('увеличить я/O', 'являются always'). Оче |
| quest.AAAAAAAAAAAAAAAAAAABrA.name | major | mistranslation | Машинный перевод — 'Rituals' не переведено, 'Easy' не переведено. Должно быть 'Ритуалы легко' или 'Простые ритуалы'. |
| quest.AAAAAAAAAAAAAAAAAAABrQ.desc | major | mistranslation | Машинный перевод. Много английского и перепутанных предлогов ('к go', 'effort'). Плохая грамматика. |
| quest.AAAAAAAAAAAAAAAAAAABrg.desc | major | mistranslation | Машинный перевод. Много английского ('Enable', 'shift-ПКМing', 'slay', 'enemies', 'shards', 'ton'). Граммат. ошибки и не |
| quest.AAAAAAAAAAAAAAAAAAABrw.desc | major | mistranslation | Машинный перевод. Много английского ('assemble', 'craft', 'таблица', 'connect', 'sides'). Грамматические ошибки и плохая |
| quest.AAAAAAAAAAAAAAAAAAABsA.desc | major | mistranslation | Машинный перевод. Много английского ('emeralds', 'store LP', 'crystallized souls'). Грамматические ошибки ('являются мож |
| quest.AAAAAAAAAAAAAAAAAAABsg.desc | major | mistranslation | Машинный перевод. Английское 'stone', 'bound инструменты', 'лава' вместо 'в лаву'. Граммат. ошибки. Теги [note] потеряны |
| quest.AAAAAAAAAAAAAAAAAAABtA.desc | major | mistranslation | Машинный перевод. Английское 'axe', 'clear out', 'wood', 'area'. Грамматические ошибки ('пока activated', 'может suffer  |
| quest.AAAAAAAAAAAAAAAAAAAByQ.desc | major | mistranslation | Преимущественно машинный перевод с разбросанными английскими словами. Фразы вроде 'энергия Infuser является tech answer' |
| quest.AAAAAAAAAAAAAAAAAAAByw.desc | major | mistranslation | Смысл переведён неверно. В оригинале говорится о комбинировании с ацетоном ИЛИ метилацетатом, а перевод содержит 'с поли |
| quest.AAAAAAAAAAAAAAAAAAABzg.desc | major | mistranslation | Машинный перевод с англицизмами. Фразы типа 'Wyverns являются rare dragons тот может walk', 'Researching ваш Draconic Co |
| quest.AAAAAAAAAAAAAAAAAAABzw.desc | major | mistranslation | Грубый машинный перевод с множеством нетранслируемых слов и грамматических ошибок: 'скорость rune является только тир 2  |
| quest.AAAAAAAAAAAAAAAAAAAC1A.desc | major | fluency | Сломанная грамматика: 'возникнет желает загрузить' - неправильное использование глаголов и склонения. Должно быть что-то |
| quest.AAAAAAAAAAAAAAAAAAAC2w.desc | major | fluency | Дублирование слова: 'ты ты тратишь' вместо 'ты тратишь'. Также опечатка повлияла на смысл фразы. |
| quest.AAAAAAAAAAAAAAAAAAAC3A.desc | major | mistranslation | Неправильный перевод объекта: 'Раздроби полученную биомассу' вместо 'Раздроби plantballs'. Исходный текст говорит о дроб |
| quest.AAAAAAAAAAAAAAAAAAAC6w.desc | major | fluency | Фрагмент 'рецепты через вафли... даже рецепты где из вафли создаётся по одному диоду' звучит неестественно и путанно. Ор |
| quest.AAAAAAAAAAAAAAAAAAACAQ.desc | major | mistranslation | Явная машинная переводка: сломанная грамматика, смешивание языков (mutatron, drone, princess, must-have не переведены),  |
| quest.AAAAAAAAAAAAAAAAAAACBQ.desc | major | mistranslation | Машинная переводка: смешивание языков (say, breakfast, meal, raw meat, scratch не переведены), сломанная грамматика (пре |
| quest.AAAAAAAAAAAAAAAAAAACBg.name | major | mistranslation | Сломанный перевод: 'There Shall быть лёгкий' смешивает английский и русский, неправильная форма глагола (быть), неправил |
| quest.AAAAAAAAAAAAAAAAAAACBw.desc | major | mistranslation | Машинная переводка: untranslated English phrases (way, awesome, traits, jubilant), сломанная грамматика (вы придётся col |
| quest.AAAAAAAAAAAAAAAAAAACCQ.desc | major | mistranslation | Машинная переводка: untranslated English (way, awesome, traits, everywhere, producing stuff), сломанная грамматика (вы п |
| quest.AAAAAAAAAAAAAAAAAAACCg.desc | major | mistranslation | Машинная переводка: untranslated English (way, awesome, traits), сломанная грамматика (вы придётся collect). |
| quest.AAAAAAAAAAAAAAAAAAACCw.desc | major | mistranslation | Машинная переводка: untranslated English (way, awesome, traits), сломанная грамматика (вы придётся collect). |
| quest.AAAAAAAAAAAAAAAAAAACDA.desc | major | mistranslation | Машинная переводка: untranslated English (way, awesome, traits, Buzz buzz buzz, working hard, really buzzing), сломанная |
| quest.AAAAAAAAAAAAAAAAAAACDQ.desc | major | mistranslation | Машинная переводка: untranslated English (way, awesome, traits), сломанная грамматика (вы придётся collect). |
| quest.AAAAAAAAAAAAAAAAAAACDg.desc | major | mistranslation | Машинная переводка: untranslated English (way, awesome, traits, Beekeeping, rain, covered), сломанная грамматика (к keep |
| quest.AAAAAAAAAAAAAAAAAAACDw.desc | major | mistranslation | Машинная переводка: untranslated English (way, awesome, traits, working, all night, all day long), смешивание языков (пч |
| quest.AAAAAAAAAAAAAAAAAAACEA.desc | major | mistranslation | Машинная переводка: untranslated English (way, awesome, traits, Cave, covered), сломанная грамматика (с Cave может работ |
| quest.AAAAAAAAAAAAAAAAAAACIQ.name | major | terminology | Цветовой код изменён с §5 на §2, и 'Suction Device' неправильно переведено как 'Сосатель' (вульгарное/неформальное) вмес |
| quest.AAAAAAAAAAAAAAAAAAACKw.desc | major | mistranslation | Изменено значение hint "COLOR" в тексте. Текст содержит форматирование §o и §r, которые не совпадают с исходным предложе |
| quest.AAAAAAAAAAAAAAAAAAACKw.name | major | mistranslation | Заголовок полностью переведён неправильно. Текст 'N-Азот... Кажется, должно быть наоборот? или нет?' не соответствует см |
| quest.AAAAAAAAAAAAAAAAAAACLQ.desc | major | mistranslation | Переводчик искажает смысл: в оригинале речь о том, что HOG — другой путь развития, требующий переделки цепочек; в перево |
| quest.AAAAAAAAAAAAAAAAAAACMA.desc | major | mistranslation | В переводе добавлены комбинации размеров (2х3х2, 3х2х3, 3х4х3), которых нет в оригинале; изменено количество уровней с 1 |
| quest.AAAAAAAAAAAAAAAAAAACQQ.desc | major | mistranslation | Потеря ключевой информации: оригинал указывает, что это эквивалент машинного корпуса Forestry, а перевод просто описывае |
| quest.AAAAAAAAAAAAAAAAAAACQw.desc | major | mistranslation | Средний абзац полностью искажён — текст о капсулах объёмом 144л вместо оригинального про использование fluid canner вмес |
| quest.AAAAAAAAAAAAAAAAAAACVA.name | major | formatting | Код цвета изменён с §3§l (cyan) на §c§l (red) - повреждена форматирующая последовательность. |
| quest.AAAAAAAAAAAAAAAAAAACVQ.name | major | formatting | Код цвета изменён с §5§l (purple) на §2§l (green) - повреждена форматирующая последовательность. |
| quest.AAAAAAAAAAAAAAAAAAACVg.name | major | formatting | Код цвета изменён с §5§l (purple) на §2§l (green) - повреждена форматирующая последовательность. |
| quest.AAAAAAAAAAAAAAAAAAACVw.name | major | formatting | Код цвета изменён с §5§l (purple) на §2§l (green) - повреждена форматирующая последовательность. |
| quest.AAAAAAAAAAAAAAAAAAACWg.desc | major | mistranslation | Сломанный машинный перевод - смешение английского и русского: «вы detected weird disturbance в воздух». Требуется полный |
| quest.AAAAAAAAAAAAAAAAAAACWw.desc | major | mistranslation | Сломанный машинный перевод - смешение английского и русского: «Вы heard rumors, тот endermen имел построено laboratories |
| quest.AAAAAAAAAAAAAAAAAAACXA.desc | major | mistranslation | Фраза 'энергии из посланного пакета улетит в молоко' — явно ошибка машинного перевода. Источник говорит о потере энергии |
| quest.AAAAAAAAAAAAAAAAAAACYw.desc | major | mistranslation | Переведено как 'Кадмиевые и кислотные' вместо 'Ртутные и кислотные'. В источнике 'Mercury' (ртуть), а не кадмий. |
| quest.AAAAAAAAAAAAAAAAAAACZA.desc | major | mistranslation | Переведено как 'Кадмиевые и кислотные' вместо 'Ртутные и кислотные'. В источнике 'Mercury' (ртуть), а не кадмий. |
| quest.AAAAAAAAAAAAAAAAAAACaQ.desc | major | terminology | Ошибочный термин 'расконсерватор' вместо правильного, неловкие формулировки в некоторых местах |
| quest.AAAAAAAAAAAAAAAAAAACaw.desc | major | mistranslation | Грамматические ошибки и неправильная терминология ('кабеля загорятся' вместо 'провода сгорят'), неловкие конструкции |
| quest.AAAAAAAAAAAAAAAAAAACbQ.desc | major | terminology | Неправильный термин 'Талькохлорит' - должно быть 'мыльный камень' или 'мыльный сланец' |
| quest.AAAAAAAAAAAAAAAAAAACfQ.desc | major | mistranslation | Неправильный перевод 'bread' как 'тесто' - источник говорит о ХЛЕБЕ. Фраза 'Не используй рецепт "NEI"' искажает смысл -  |
| quest.AAAAAAAAAAAAAAAAAAACfQ.name | major | mistranslation | 'Do'h!' - это игра слов (Do + dough/тесто), русский перевод 'Тесто!' потеряет смысл. 'Do'h' - восклицание из Симпсонов,  |
| quest.AAAAAAAAAAAAAAAAAAACgw.desc | major | fluency | Текст содержит орфографические ошибки и странные конструкции: 'паровой крекинг(расщепление)' - скобки в неправильном мес |
| quest.AAAAAAAAAAAAAAAAAAACiQ.desc | major | fluency | Текст содержит серьезные грамматические ошибки и неловкие конструкции: 'высота полета этого ранца' вместо 'ранца'; 'умен |
| quest.AAAAAAAAAAAAAAAAAAACiw.desc | major | fluency | Текст содержит множество грамматических ошибок и неловких конструкций: 'Для подзарядки на ходу, ты можешь использовать з |
| quest.AAAAAAAAAAAAAAAAAAAClg.name | major | formatting | Цветовой код отличается от оригинала: в исходном §5§l, в переводе §2§l. Токены форматирования повреждены. |
| quest.AAAAAAAAAAAAAAAAAAAClw.name | major | formatting | Цветовой код отличается от оригинала: в исходном §5§l, в переводе §2§l. Токены форматирования повреждены. |
| quest.AAAAAAAAAAAAAAAAAAACoQ.desc | major | mistranslation | Слово 'капсулы' неправильно переводит 'fluid cells' - должно быть 'ячейки для жидкостей' или 'жидкостные контейнеры' |
| quest.AAAAAAAAAAAAAAAAAAACow.desc | major | fluency | Грамматическая ошибка в согласовании: 'который' должно быть вместо 'которой', и сложная структура предложения делает его |
| quest.AAAAAAAAAAAAAAAAAAACpA.desc | major | mistranslation | Опечатка 'Ralicraft' вместо 'Railcraft'; неточный перевод 'сцепки вагонеток' вместо правильного значения о скорости движ |
| quest.AAAAAAAAAAAAAAAAAAACvA.desc | major | mistranslation | Сломанный машинный перевод с английскими словами среди русского текста: 'как dark может один быть? You're sure face в то |
| quest.AAAAAAAAAAAAAAAAAAACvA.name | major | mistranslation | Сломанный машинный перевод, смешивание английского и русского: 'как Dark может вы Go?' |
| quest.AAAAAAAAAAAAAAAAAAACvg.desc | major | mistranslation | Машинный перевод с необработанными английскими словами и сломанной грамматикой: 'как много больше я может store' |
| quest.AAAAAAAAAAAAAAAAAAACvw.desc | major | mistranslation | Машинный перевод с английскими словами среди русского текста: 'demons summoned являются довольно strong' |
| quest.AAAAAAAAAAAAAAAAAAACwA.desc | major | mistranslation | Машинный перевод: 'slates' не переведено, фраза 'получение закрыть' сломана |
| quest.AAAAAAAAAAAAAAAAAAACwg.desc | major | mistranslation | Машинный перевод с необработанными английскими словами: 'Top тир chalk, для fancy wall paintings' |
| quest.AAAAAAAAAAAAAAAAAAACww.name | major | mistranslation | Слово 'Orb' не переведено, непроверенное 'их' вместо полного перевода: 'Archmage Orb. Let их Come!' |
| quest.AAAAAAAAAAAAAAAAAAACxA.name | major | mistranslation | Слово 'Master' не переведено, фраза 'получение закрыть' сломана |
| quest.AAAAAAAAAAAAAAAAAAACxQ.desc | major | mistranslation | Машинный перевод с английскими словами: 'к write "darker" runes чем вы используется к' |
| quest.AAAAAAAAAAAAAAAAAAACxg.desc | major | mistranslation | Машинный перевод с необработанными английскими словами и сломанной грамматикой: 'Runes Superior Capacity увеличить алтар |
| quest.AAAAAAAAAAAAAAAAAAACxw.desc | major | mistranslation | Машинный перевод с необработанными английскими словами: 'финальный frontier: Есть not много runes доступный' |
| quest.AAAAAAAAAAAAAAAAAAACyA.desc | major | mistranslation | Машинный перевод с английскими словами среди русского текста: 'больше powerful rituals требовать dusk runes' |
| quest.AAAAAAAAAAAAAAAAAAACyQ.desc | major | mistranslation | Машинный перевод с английским словом 'diviner' и 'far' в тексте: 'последний diviner поэтому far' |
| quest.AAAAAAAAAAAAAAAAAAACyw.desc | major | mistranslation | Машинный перевод с английским словом 'shards' в середине русского текста: 'с эти новый shards вы можете скрафтить' |
| quest.AAAAAAAAAAAAAAAAAAACyw.name | major | untranslated | Слово 'Imbued' не переведено: 'Imbued Spell улучшения' |
| quest.AAAAAAAAAAAAAAAAAAACzQ.desc | major | mistranslation | Неправильная передача смысла: 'всё нужно' должно быть 'всему нужно' или 'для всех нужен'. Фраза о неправильной интерпрет |
| quest.AAAAAAAAAAAAAAAAAAACzg.desc | major | mistranslation | Неправильный перевод 'Crop Sticks' как 'жёрдочки' (это не соответствует механике мода). Также неправильно переведено 'Fi |
| quest.AAAAAAAAAAAAAAAAAAACzw.desc | major | mistranslation | Неправильный перевод 'Filing Cabinets' как 'шкафы из Extra Utilities' - неверное название мода/блока. |
| quest.AAAAAAAAAAAAAAAAAAAD2g.desc | major | untranslated | Явно машинный перевод с огромным количеством оставленного английского текста - полностью разборчивое предложение превращ |
| quest.AAAAAAAAAAAAAAAAAAAD2g.name | major | untranslated | Название почти полностью осталось на английском, только слова переставлены - это не перевод. |
| quest.AAAAAAAAAAAAAAAAAAAD4A.desc | major | mistranslation | Текст полностью разбит машинным переводом, содержит смешанные английские слова, неправильную грамматику и отсутствует но |
| quest.AAAAAAAAAAAAAAAAAAAD4A.name | major | mistranslation | Название разбито машинным переводом, содержит неправильный порядок слов и английский текст в начале |
| quest.AAAAAAAAAAAAAAAAAAAD8w.name | major | formatting | Цветовой код изменён с §9 на §5, что неправильно |
| quest.AAAAAAAAAAAAAAAAAAAD9A.name | major | formatting | Цветовой код изменён с §9 на §5 |
| quest.AAAAAAAAAAAAAAAAAAAD9Q.name | major | untranslated | Название переведено неполно: 'SMD-диоды' вместо 'SMD-компоненты схемы' или подобного, потеря смысла компонентов |
| quest.AAAAAAAAAAAAAAAAAAAD9g.desc | major | mistranslation | Переведено 'Микроконтроллер' вместо 'Рабочая станция' - это разные вещи в контексте игры |
| quest.AAAAAAAAAAAAAAAAAAAD9w.desc | major | fluency | Описание технического процесса переведено путано и неточно, не соответствует ясности источника |
| quest.AAAAAAAAAAAAAAAAAAADAA.name | major | formatting | Добавлен цветовой код §5 которого нет в источнике |
| quest.AAAAAAAAAAAAAAAAAAADAQ.name | major | formatting | Добавлен цветовой код §5 которого нет в источнике |
| quest.AAAAAAAAAAAAAAAAAAADAw.name | major | formatting | Цветовой код §2 не соответствует §5 в источнике |
| quest.AAAAAAAAAAAAAAAAAAADBA.name | major | formatting | Добавлен цветовой код §5 которого нет в источнике |
| quest.AAAAAAAAAAAAAAAAAAADCQ.desc | major | mixed_language | Критическая ошибка: английский текст не переведён, перемешан с русским ('Don't burn yourself' остался, смешаны языки) |
| quest.AAAAAAAAAAAAAAAAAAADDA.desc | major | mistranslation | Процесс описан неправильно - 'получается сжиманием' не соответствует смыслу источника о сжимании и запеканию в печи |
| quest.AAAAAAAAAAAAAAAAAAADDg.desc | major | mistranslation | Критические ошибки: 'monocrystalline silicon boules' переведено как 'монокристалл кремния' (потеря термина 'boules'). 's |
| quest.AAAAAAAAAAAAAAAAAAADDg.name | major | mistranslation | Неполный перевод: 'Boules' полностью потеряно. Переведено как 'Монокристалл кремния' в единственном числе вместо множест |
| quest.AAAAAAAAAAAAAAAAAAADDw.desc | major | terminology | Множественные технические ошибки: 'optimal fuel efficiency' переведено как 'максимальная эффективность' (should be оптим |
| quest.AAAAAAAAAAAAAAAAAAADGw.name | major | formatting | Неверный цветовой код: §5 (в английском) заменён на §2 (зелёный вместо пурпурного) |
| quest.AAAAAAAAAAAAAAAAAAADIA.desc | major | mistranslation | Процесс описан в обратном порядке: 'комбинируем стальные пластины с нано-поножами', а не наоборот как в переводе |
| quest.AAAAAAAAAAAAAAAAAAADJA.desc | major | mistranslation | Полностью повреждённый машинный перевод: 'Ideal для ваш Implosion Compressor' - смешанный английский/русский, сломанная  |
| quest.AAAAAAAAAAAAAAAAAAADJQ.name | major | formatting | Неверный цветовой код: §a (в английском, зелёный) заменён на §8 (чёрный) |
| quest.AAAAAAAAAAAAAAAAAAADKA.name | major | mistranslation | Цвет изменен с §9 (синий) на §5 (фиолетовый), текст полностью переведен как 'HV миксер' вместо 'Mixing at HV Level' - эт |
| quest.AAAAAAAAAAAAAAAAAAADKg.desc | major | mistranslation | Фраза 'a few stacks of TNT' переведена как 'нескольких пачек динамита' - неправильно, в квесте речь о TNT блоках, а не о |
| quest.AAAAAAAAAAAAAAAAAAADLA.desc | major | mistranslation | Термин 'heavy duty plates' переведен как 'сверхпрочное покрытие' - это неверный перевод, должно быть 'тяжелые пластины'  |
| quest.AAAAAAAAAAAAAAAAAAADLA.name | major | mistranslation | Текст содержит неверный перевод 'Сверхпрочное покрытие' вместо правильного наименования части ракеты - должны быть 'плас |
| quest.AAAAAAAAAAAAAAAAAAADLg.desc | major | mistranslation | 'Rocket fins' переведено как 'ракетный стабилизатор' - неправильно, fins это плавники/крылья ракеты, а не стабилизатор;  |
| quest.AAAAAAAAAAAAAAAAAAADLg.name | major | mistranslation | Неправильный перевод 'Rocket Fins' как 'Ракетный стабилизатор' - должны быть 'ракетные плавники' или 'крылья ракеты' |
| quest.AAAAAAAAAAAAAAAAAAADMA.desc | major | mistranslation | Фраза 'a second seat for a Moon buggy' переведена неправильно и с искажением смысла - говорится о сидении для багги, но  |
| quest.AAAAAAAAAAAAAAAAAAADMQ.desc | major | mistranslation | Перевод полностью неправильный - оригинал просто говорит что сиденье - это часть посадочного модуля, а перевод говорит ч |
| quest.AAAAAAAAAAAAAAAAAAADMg.desc | major | mistranslation | Текст содержит неясные и неправильно переведенные участки: 'надеть в соответствующую ячейку' - неправильный оборот; 'отс |
| quest.AAAAAAAAAAAAAAAAAAADNA.desc | major | mistranslation | Множество ошибок: 'молнии, вызываемые эффектами от искажения' - бессмыслица вместо 'lightning warp'; 'воздушный фильтр/о |
| quest.AAAAAAAAAAAAAAAAAAADNQ.desc | major | mistranslation | Множество неточностей: 'зелёная точка' и 'жёлтый кружок' неправильно описывают стороны; 'страдать с капсулами' - грубый  |
| quest.AAAAAAAAAAAAAAAAAAADOA.desc | major | mistranslation | Перевод содержит множество ошибок: 'вмещает в себя до 1000 единиц воздуха' неправильный оборот; 'нет кислорода' оборвано |
| quest.AAAAAAAAAAAAAAAAAAADOQ.desc | major | mistranslation | Неправильный перевод инструкции - 'нажми на саму руду в NEI и пролистай до вкладки' - неясно и неправильно; также 'как ' |
| quest.AAAAAAAAAAAAAAAAAAADOg.desc | major | mistranslation | Перевод содержит неточности: 'учитывая насколько они распространены' - неправильный оборот; 'так что добудь немного руды |
| quest.AAAAAAAAAAAAAAAAAAADXQ.name | major | mistranslation | Tungstensteel (вольфрамовая сталь) — это сплав, который в модах часто называют вольфрам-стальным сплавом. Перевод 'вольф |
| quest.AAAAAAAAAAAAAAAAAAADYw.name | major | terminology | Color code изменён с §3 (бирюзовый) на §c (красный), нарушая форматирование. Кроме того, 'Лазуритит' — странный термин;  |
| quest.AAAAAAAAAAAAAAAAAAADZQ.desc | major | mistranslation | 'Цинк для фильтров' неверно; в тексте речь идёт о 'малых цинковых рудах'. 'кремния' вместо 'кремня/кремния' неправильно  |
| quest.AAAAAAAAAAAAAAAAAAADZw.desc | major | mistranslation | 'электронные лампы' вместо 'вакуумные трубки' — это грубая ошибка перевода. Vacuum tubes — это вакуумные трубки, не элек |
| quest.AAAAAAAAAAAAAAAAAAADbA.desc | major | mistranslation | Много проблем: 'маленькими капсулами' вместо 'cells' неправильно; 'Большой химический реактор' правильно, но 'через шлюз |
| quest.AAAAAAAAAAAAAAAAAAADbQ.desc | major | terminology | Ошибка в переводе термина: 'primal charm' переведено как 'сингулярный амулет', что неверно. Должно быть 'первобытный аму |
| quest.AAAAAAAAAAAAAAAAAAADbg.desc | major | terminology | Термин 'primal charm' снова ошибочно переведен как 'сингулярный амулет' вместо правильного перевода. |
| quest.AAAAAAAAAAAAAAAAAAADbw.desc | major | terminology | Ошибка в переводе: 'primal charm' переведено как 'сингулярный амулет' - неверная терминология, должно быть корректное об |
| quest.AAAAAAAAAAAAAAAAAAADbw.name | major | terminology | Неверный перевод 'Primal Charm' как 'Сингулярный амулет'. Требуется корректный перевод этого термина. |
| quest.AAAAAAAAAAAAAAAAAAADgQ.desc | major | mistranslation | Значительное сокращение текста: опущена информация 'which is still a pain to craft' (что всё ещё болезненно/сложно в кра |
| quest.AAAAAAAAAAAAAAAAAAADnQ.desc | major | untranslated | Отсутствует второе предложение с английским текстом: 'If you want to §oreally§r prove yourself though, head on over to t |
| quest.AAAAAAAAAAAAAAAAAAADng.desc | major | mistranslation | Гарнирована машинным переводом. Текст содержит смесь английского и русского с нарушенным порядком слов: 'к сделать ваш а |
| quest.AAAAAAAAAAAAAAAAAAADnw.desc | major | mistranslation | Явная машинная переводимость: смешанный язык (like, pillars out, na top), грамматические ошибки (к сделать, четыре блоки |
| quest.AAAAAAAAAAAAAAAAAAADoA.desc | major | mistranslation | Механический перевод: смешанный язык (like, way, через adept thaumaturgy), грамматические ошибки (иметь вместо имеют, и  |
| quest.AAAAAAAAAAAAAAAAAAADoQ.desc | major | mistranslation | Машинный перевод: смешанный язык (highest тир, на top), грамматические ошибки (вы нужно, блоки высокий), неправильное сл |
| quest.AAAAAAAAAAAAAAAAAAADrA.desc | major | mistranslation | В [note]: оригинал говорит 'don't need to be in a cleanroom', а перевод ошибочно говорит 'позволяют делать рецепты, кото |
| quest.AAAAAAAAAAAAAAAAAAADrg.name | major | formatting | Цветовой код изменен с §3 на §c. Также перевод неполный/неграмотный: 'делать её тебе' - нужно 'делать её должен ты' или  |
| quest.AAAAAAAAAAAAAAAAAAADsw.desc | major | mistranslation | 'punji sticks' (специальные колышки) ошибочно переведено как 'бамбука'. Это разные предметы/механики. |
| quest.AAAAAAAAAAAAAAAAAAAE0g.name | major | mistranslation | Empty Epoxid Board переведено как Продвинутая печатная плата - теряется смысл Empty (пустая) |
| quest.AAAAAAAAAAAAAAAAAAAE2g.name | major | formatting | Цвет изменён с §a (зелёный) на §8 (тёмно-серый), нарушена целостность форматирования оригинального сегмента |
| quest.AAAAAAAAAAAAAAAAAAAE2w.name | major | formatting | Цвет изменён с §a (зелёный) на §8 (тёмно-серый), нарушена целостность форматирования |
| quest.AAAAAAAAAAAAAAAAAAAE3A.desc | major | mistranslation | Текст начинается с 'Ты можешь и несколько других рудных жил' - неполное предложение, пропущен глагол; правильно должно б |
| quest.AAAAAAAAAAAAAAAAAAAE3A.name | major | formatting | Цвет изменён с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAE3Q.name | major | formatting | Цвет изменён с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAE3g.name | major | formatting | Цвет изменён с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAE3w.name | major | formatting | Цвет изменён с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAE4A.name | major | formatting | Цвет изменён с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAE4Q.desc | major | mistranslation | Перевод неправильно переструктурирован и переписан; оригинал говорит 'NanoCPU Wafer is made out of a CPU Wafer with carb |
| quest.AAAAAAAAAAAAAAAAAAAE4Q.name | major | mistranslation | Неправильно переведено; 'Нанокомпонентный центральный процессор' не соответствует 'NanoCPU Wafer and Chip' - должно быть |
| quest.AAAAAAAAAAAAAAAAAAAE4g.name | major | formatting | Цвет изменён с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAE4w.name | major | formatting | Цвет изменён с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAE5A.name | major | formatting | Цвет изменён с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAE5Q.desc | major | mistranslation | Текст обрезан: 'с ячейкой руке' вместо 'с ячейкой в руке'; смысл неправильный - описание ME хранилища размером 16k, а не |
| quest.AAAAAAAAAAAAAAAAAAAE5w.desc | major | mistranslation | 'саннариевых акуумуляторов' - неправильный перевод, это ME Storage Cell, не батареи; 'акуумуляторов' - опечатка (должно  |
| quest.AAAAAAAAAAAAAAAAAAAE6A.desc | major | mistranslation | Текст идентичен 16k Component переводу, но описывает 64k - копипаста ошибки; упоминание '256К компонентов' неправильно д |
| quest.AAAAAAAAAAAAAAAAAAAE7Q.name | major | formatting | Цвет изменён с §a (зелёный) на §8 (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAE7w.name | major | mistranslation | Цвет кода изменен: §8 (серый) вместо §a (зеленый). 'Blue Steel' ошибочно переведен как 'Синяя сталь' - должна быть синяя |
| quest.AAAAAAAAAAAAAAAAAAAE8A.desc | major | mistranslation | Неправильный перевод 'Lapotrons' - переведено как 'лазутроновые кристаллы', а должно быть 'Лапотроны' (сохранение мод-ме |
| quest.AAAAAAAAAAAAAAAAAAAE8Q.desc | major | mistranslation | 'Mash your old ones together' переведено как 'свяжи' - неправильно. Должно быть 'сломай в прессе' или 'переработай вмест |
| quest.AAAAAAAAAAAAAAAAAAAE8g.desc | major | mistranslation | Множественные ошибки: 'понижающим' vs 'понижающем' (склонение), 'большая точка' неясно (должно быть 'большой квадрат' ил |
| quest.AAAAAAAAAAAAAAAAAAAECw.desc | major | mistranslation | 'поставь эту удобную насадку для душа на дно резервуара' - искажение смысла. 'Shower head' - это визуальный элемент над  |
| quest.AAAAAAAAAAAAAAAAAAAEHw.desc | major | fluency | Почти целиком машинный перевод - англиские слова смешаны с русским. 'после несколько forbidden researches' вместо полног |
| quest.AAAAAAAAAAAAAAAAAAAELg.desc | major | mistranslation | 'Магическое перо' неправильно - нужно 'Магический фокус карты'. 'факелонт' неясно - должно быть 'факельные ягоды' или 'T |
| quest.AAAAAAAAAAAAAAAAAAAELw.desc | major | mistranslation | 'магическое перо' - ошибка (вверху уже исправлено как фокус). 'ECS-Достижения' неправильно - должно быть просто 'вкладка |
| quest.AAAAAAAAAAAAAAAAAAAEPA.name | major | formatting | Цветовой код изменён с §5 на §2, что меняет цвет текста с фиолетового на зеленый |
| quest.AAAAAAAAAAAAAAAAAAAEPQ.name | major | formatting | Цветовой код изменён с §2 на §a, что меняет цвет текста |
| quest.AAAAAAAAAAAAAAAAAAAEQg.name | major | formatting | Цветовой код изменён с §5 на §2, что меняет цвет текста с фиолетового на зеленый |
| quest.AAAAAAAAAAAAAAAAAAAEQw.name | major | formatting | Цветовой код изменён с §5 на §2, что меняет цвет текста с фиолетового на зеленый |
| quest.AAAAAAAAAAAAAAAAAAAERA.name | major | formatting | Цветовой код изменён с §3 на §c, что меняет цвет текста с голубого на красный |
| quest.AAAAAAAAAAAAAAAAAAAERg.name | major | formatting | Цветовой код изменён с §5 на §2, что меняет цвет текста с фиолетового на зеленый |
| quest.AAAAAAAAAAAAAAAAAAAESA.desc | major | mistranslation | Перевод не соответствует исходному тексту; содержит неправильный перевод процесса исследования и структуры предложений |
| quest.AAAAAAAAAAAAAAAAAAAESQ.desc | major | mistranslation | Сильно поврежденный машинный перевод с смешиванием английского и русского языков; множество непереведённых английских сл |
| quest.AAAAAAAAAAAAAAAAAAAESQ.name | major | untranslated | Название почти не переведено; три из четырех слов на английском (Bathing, Warp, Away) |
| quest.AAAAAAAAAAAAAAAAAAAESg.desc | major | mistranslation | Сильно поврежденный машинный перевод; смешивание английского и русского (Bathing в spa, removing warp эффекты); множеств |
| quest.AAAAAAAAAAAAAAAAAAAESg.name | major | untranslated | Название практически не переведено; только одно предлог 'в' переведён, остальное на английском |
| quest.AAAAAAAAAAAAAAAAAAAESw.desc | major | mistranslation | Критически повреждённый машинный перевод; хаотичное смешивание английского и русского (этот soap является очень особый,  |
| quest.AAAAAAAAAAAAAAAAAAAETg.desc | major | mistranslation | Полностью машинный перевод с перемешанным английским и сломанной грамматикой. Текст непонятен и требует полного переделк |
| quest.AAAAAAAAAAAAAAAAAAAEVg.name | major | mistranslation | Сломанный машинный перевод с перемешанным английским и неправильной грамматикой. 'Purge все ваш Warp' не является русски |
| quest.AAAAAAAAAAAAAAAAAAAEWw.desc | major | terminology | Некорректные термины в таблицах и описаниях характеристик деревьев: 'Область посадки' должна быть 'Толщина' (girth), 'Жи |
| quest.AAAAAAAAAAAAAAAAAAAEXA.name | major | mistranslation | Слово 'cultivated' оставлено на английском языке, грамматическая ошибка в конструкции ('несколько cultivated пчёлы'). До |
| quest.AAAAAAAAAAAAAAAAAAAEXQ.name | major | mistranslation | Слово 'common' оставлено на английском языке, грамматическая ошибка ('несколько common пчёлы'). Должно быть: 'Вывести не |
| quest.AAAAAAAAAAAAAAAAAAAEXg.desc | major | mixed_language | Текст покрыт машинным переводом с множественными английскими словами и фразами, перемешанными с русским ('Cross', 'commo |
| quest.AAAAAAAAAAAAAAAAAAAEXg.name | major | mistranslation | Неправильная грамматика и построение предложения ('разводить несколько noble пчёлы'). Должно быть: 'Вывести нескольких б |
| quest.AAAAAAAAAAAAAAAAAAAEXw.desc | major | mixed_language | Машинный перевод с английскими словами ('noble', 'dripping') и неправильной грамматикой ('производить' вместо 'производя |
| quest.AAAAAAAAAAAAAAAAAAAEYA.name | major | mistranslation | Слово 'majestic' оставлено на английском, грамматическая ошибка. Должно быть: 'Вывести нескольких величественных пчёл'. |
| quest.AAAAAAAAAAAAAAAAAAAEYQ.name | major | mistranslation | Слово 'imperial' оставлено на английском, грамматическая ошибка. Должно быть: 'Вывести нескольких царских пчёл'. |
| quest.AAAAAAAAAAAAAAAAAAAE_w.desc | major | mistranslation | Множество неточностей и ошибок: "глубоких океанах лавы" - неправильный термин (должно быть "глубокие слои лавы"), "вмест |
| quest.AAAAAAAAAAAAAAAAAAAEaA.desc | major | mistranslation | Запутанный и неточный перевод. Неправильно переведены части про инженерную станцию и верстак - в оригинале говорится о " |
| quest.AAAAAAAAAAAAAAAAAAAEaQ.desc | major | mistranslation | Неточный перевод - источник говорит "Crafting Station" из Tinker's Construct, а перевод переводит как "верстак из Tinker |
| quest.AAAAAAAAAAAAAAAAAAAEcQ.desc | major | mistranslation | Множество ошибок перевода: неправильное объяснение про "вход" генератора, путаница в описании размещения и ротора, непон |
| quest.AAAAAAAAAAAAAAAAAAAEdA.desc | major | mistranslation | Слово 'автомазитированно' - машинный перевод-гибрид; неправильно передана информация о прочности иридиевого ротора; необ |
| quest.AAAAAAAAAAAAAAAAAAAEeQ.desc | major | mistranslation | Технические цифры в переводе (57/512, 57/2048) не соответствуют исходнику (97EU); неправильно передана техническая специ |
| quest.AAAAAAAAAAAAAAAAAAAEgQ.desc | major | mistranslation | Фраза 'остроту кварцем' неверна — должно быть 'наносить кварц на арбалет' (urge/damage upgrade). 'остроту' — неправильны |
| quest.AAAAAAAAAAAAAAAAAAAEng.desc | major | other | Добавлен контент, отсутствующий в английском оригинале: '(Хотя кто мешает перевозить капсулы/резервуары с нефтью в вагон |
| quest.AAAAAAAAAAAAAAAAAAAEog.desc | major | fluency | 'а не активированные ты можешь использоваться' — грубая грамматическая ошибка. 'использоваться' — рефлексивный глагол, н |
| quest.AAAAAAAAAAAAAAAAAAAEpA.name | major | mistranslation | 'с защитой и криперов' — критическая грамматическая ошибка. Должно быть 'от криперов', а не 'и криперов'. Меняет смысл. |
| quest.AAAAAAAAAAAAAAAAAAAErQ.name | major | mistranslation | «Больше, лучше, взрывоопаснее» — неправильный перевод слова «Fusor». Это название игровой механики, должно быть «Больше, |
| quest.AAAAAAAAAAAAAAAAAAAEsg.name | major | mistranslation | «Я ставлю слияние в твое слияние так что ты можешь слиять пока ты слияешься» — неверно переведена поговорка (Xzibit мем) |
| quest.AAAAAAAAAAAAAAAAAAAExA.name | major | mistranslation | Tubes переведено как 'лампы' вместо 'трубы' - неправильное слово |
| quest.AAAAAAAAAAAAAAAAAAAExg.desc | major | mistranslation | Workstation circuits переведено как 'микроконтроллеры' - неправильная терминология |
| quest.AAAAAAAAAAAAAAAAAAAEyw.desc | major | fluency | Опечатка в 'пероксодисульфатаа' (двойное а), нарушена грамматика в 'Это кислота не просто' |
| quest.AAAAAAAAAAAAAAAAAAAF-g.desc | major | mistranslation | Io - спутник Юпитера, а не Луны. Текст 'спутник Луны - Ио' - грубая ошибка |
| quest.AAAAAAAAAAAAAAAAAAAF0A.desc | major | mistranslation | Infusion altar переведено как 'алтаря насыщения' - должно быть 'алтаря насыщения' (infusion), неверная терминология |
| quest.AAAAAAAAAAAAAAAAAAAF0g.desc | major | mistranslation | Sensors переведено как 'приёмники' вместо 'датчики' - неправильная техническая терминология |
| quest.AAAAAAAAAAAAAAAAAAAF1A.desc | major | mistranslation | Solar Grade Silicon переведено как 'поликристаллический кремний' - неверная терминология; также неловкая перефразировка  |
| quest.AAAAAAAAAAAAAAAAAAAF1Q.name | major | formatting | Код цвета изменен с §c§l (красный) на §d§l (пурпурный). Необходимо восстановить исходный код цвета. |
| quest.AAAAAAAAAAAAAAAAAAAF2A.name | major | formatting | Код цвета изменен с §2§l (зеленый) на §a§l (светло-зеленый). Необходимо восстановить исходный код цвета. |
| quest.AAAAAAAAAAAAAAAAAAAF2Q.name | major | formatting | Код цвета изменен с §2§l (зеленый) на §a§l (светло-зеленый). Необходимо восстановить исходный код цвета. |
| quest.AAAAAAAAAAAAAAAAAAAF2w.name | major | formatting | Код цвета изменен с §5§l (пурпурный) на §2§l (зеленый). Необходимо восстановить исходный код цвета. |
| quest.AAAAAAAAAAAAAAAAAAAF3Q.desc | major | mistranslation | Отсутствует закрывающий символ в пути файла; 'Торговом автомате' неправильный перевод 'Coins tab'; 'баганные' некорректн |
| quest.AAAAAAAAAAAAAAAAAAAF6w.name | major | mistranslation | Английские слова Buzzing и Screaming оставлены непереведёнными, русский текст грамматически некорректен (являются пчёлы  |
| quest.AAAAAAAAAAAAAAAAAAAF7A.desc | major | mistranslation | Текст полностью разбит машинным переводом: английские слова разбросаны по тексту (soul frame, too long, taste, destroy,  |
| quest.AAAAAAAAAAAAAAAAAAAF7A.name | major | mistranslation | Garbled machine translation: английские слова Buzzing и Beyond оставлены непереведёнными, русская часть неполна. Требует |
| quest.AAAAAAAAAAAAAAAAAAAF7w.desc | major | mistranslation | Вторая часть предложения неправильно передает смысл оригинала. 'даже в BC цистерны' искажает значение 'other than' - дол |
| quest.AAAAAAAAAAAAAAAAAAAF7w.name | major | formatting | Код цвета изменен с §5 (фиолетовый) на §2 (зеленый). Нужно сохранить оригинальный формат. |
| quest.AAAAAAAAAAAAAAAAAAAF8Q.name | major | formatting | Код цвета изменен с §9 (синий) на §5 (фиолетовый). Нужно сохранить оригинальный формат. |
| quest.AAAAAAAAAAAAAAAAAAAF8g.name | major | formatting | Код цвета изменен с §b (голубой) на §9 (синий). Нужно сохранить оригинальный формат. |
| quest.AAAAAAAAAAAAAAAAAAAF9w.desc | major | mistranslation | 'даже снизу' неправильно передает 'other than the bottom'. Должно быть 'кроме нижней стороны' - шипы НЕ наносят урон сни |
| quest.AAAAAAAAAAAAAAAAAAAFDg.desc | major | mistranslation | Ошибка в названии компонента: 'истинный кварц' некорректно передаёт 'certus quartz' (должно быть 'кварц Сертус'). Также  |
| quest.AAAAAAAAAAAAAAAAAAAFEA.desc | major | mistranslation | Опечатка в структуре перевода: 'Чистые версии изменчивых кристаллов и кристаллов истинного кварца и нижнего мира' — непр |
| quest.AAAAAAAAAAAAAAAAAAAFFQ.desc | major | mistranslation | Ошибка в переводе: 'Gates all network I/O' переведено как 'Они нужны для всех операций загрузки/выгрузки в/из МЭ сети',  |
| quest.AAAAAAAAAAAAAAAAAAAFLQ.desc | major | mistranslation | Машинный перевод с огромным количеством ошибок: неправильное введение слов (Time к получить), оставлены без перевода анг |
| quest.AAAAAAAAAAAAAAAAAAAFQQ.desc | major | fluency | Ошибка согласования: 'наполнение твоих крылья' неправильно, должно быть 'наполнение твоих крыльев' (генитив) |
| quest.AAAAAAAAAAAAAAAAAAAFQg.desc | major | mixed_language | Машинный перевод: текст содержит нетранслюцированные английские выражения и неправильные депренеприативы |
| quest.AAAAAAAAAAAAAAAAAAAFQg.name | major | untranslated | Полностью не переведено - оставлено на английском: 'Dropped в Asgard, Fallen к Earth' |
| quest.AAAAAAAAAAAAAAAAAAAFQw.desc | major | mixed_language | Машинный перевод со смешанным языком и грубыми грамматическими ошибками |
| quest.AAAAAAAAAAAAAAAAAAAFQw.name | major | untranslated | Полностью не переведено - 'Repaired это!' должно быть 'Ототчинено!' |
| quest.AAAAAAAAAAAAAAAAAAAFRA.desc | major | mixed_language | Машинный перевод со смешанным языком и неправильными стройками |
| quest.AAAAAAAAAAAAAAAAAAAFSQ.desc | major | mixed_language | Машинный перевод со смешанным языком и деструктивными ошибками |
| quest.AAAAAAAAAAAAAAAAAAAFSg.name | major | terminology | 'Перезаряжаемая чернильница с пером' не соответствует 'Rechargeable Scribing Tools' - неправильно выбранна |
| quest.AAAAAAAAAAAAAAAAAAAFVQ.desc | major | mistranslation | 'Призыватель молний' не соответствует 'LS' из английского текста - неправильное толкование |
| quest.AAAAAAAAAAAAAAAAAAAFVQ.name | major | mistranslation | 'Призыватель молний' не соответствует 'Trigger: Ballthingy' - интерпретация текста |
| quest.AAAAAAAAAAAAAAAAAAAFVw.name | major | mistranslation | Неполный перевод: 'Upgrade Your Forestry Backpack' переведено как 'Улучши свои рюкзаки', теряется модификатор 'Forestry' |
| quest.AAAAAAAAAAAAAAAAAAAFWQ.desc | major | mistranslation | 'жиле руды кристаллов' неточный перевод - скорее 'Thaumcraft Infused Stone' это конкретный тип руды; 'чутка' - простореч |
| quest.AAAAAAAAAAAAAAAAAAAFWg.desc | major | fluency | 'дополнительные источники света, которые работают как факела' - неправильное согласование (факелы, не факела); 'Они созд |
| quest.AAAAAAAAAAAAAAAAAAAFWw.desc | major | mistranslation | Многие ошибки: 'перелей его в жидкостный наполнитель' - неверно переведено, должно быть 'в бак/резервуар'; инструкции к  |
| quest.AAAAAAAAAAAAAAAAAAAFXA.desc | major | mistranslation | Перевод полностью испорчен: смешивание русского и английского ('жезл фокус: Fire является базовый жезл фокус тот являетс |
| quest.AAAAAAAAAAAAAAAAAAAFXA.name | major | mistranslation | 'I Don't Want to Set the World on Fire' переведено как 'я Don't хотите к настроить мир на Fire' - граммарически неверно, |
| quest.AAAAAAAAAAAAAAAAAAAFYg.desc | major | mistranslation | Смешивание языков: 'жезл фокус: Portable дыра будет создать temporary 3x3x32 дыра' - неправильный порядок слов, неправил |
| quest.AAAAAAAAAAAAAAAAAAAFYg.name | major | mistranslation | 'Keep это Away из Bags Holding' - неправильный перевод на русский, смешивание английского и русского, потеря значения 'o |
| quest.AAAAAAAAAAAAAAAAAAAFaA.desc | major | mistranslation | Смешивание языков: 'жезл фокус: Efreet's Flame shoots beam similar к жезл фокус: Excavation тот smelts блоки like Furnac |
| quest.AAAAAAAAAAAAAAAAAAAFag.desc | major | mistranslation | Перевод испорчен: 'жезл фокус: Mending является жезл фокус тот будет slowly mend caster's wounds' - смешивание языков, г |
| quest.AAAAAAAAAAAAAAAAAAAFaw.desc | major | mistranslation | Смешивание языков: 'жезл фокус: Uprising propels его caster forward' - неправильный порядок слов, грамматические ошибки, |
| quest.AAAAAAAAAAAAAAAAAAAFbA.desc | major | mistranslation | Смешивание языков: 'жезл фокус: Distortion protects caster из "ordinary" projectiles' - неправильный порядок слов, 'пока |
| quest.AAAAAAAAAAAAAAAAAAAFbQ.desc | major | mistranslation | Смешивание языков: 'жезл фокус: Ender Rift открыть ваш vanilla Personal Ender Chest' - неправильный порядок слов и грамм |
| quest.AAAAAAAAAAAAAAAAAAAFbg.desc | major | mistranslation | Явно машинный перевод со сломанной грамматикой. Смешана русская и английская речь: 'жезл фокус тот может move nearby dro |
| quest.AAAAAAAAAAAAAAAAAAAFbg.name | major | mistranslation | Неправильный перевод. 'это Can't Bend Spoons' - буквально переведено с ошибкой и смешано с английским. Должно быть перев |
| quest.AAAAAAAAAAAAAAAAAAAFbw.desc | major | mistranslation | Машинный перевод с перемешанными английским и русским: 'жезл фокус тот Experience Drain будет drain игрок experience'. М |
| quest.AAAAAAAAAAAAAAAAAAAFbw.name | major | mistranslation | Неправильный перевод 'Knowledge is Power' как 'Knowledge является энергия'. 'Knowledge' не переведено, и структура предл |
| quest.AAAAAAAAAAAAAAAAAAAFcA.desc | major | mistranslation | Машинный перевод с бессмысленными конструкциями: 'shoots beam dark энергия', 'travels о 40 блоки', 'делает о 100 урон'.  |
| quest.AAAAAAAAAAAAAAAAAAAFcg.desc | major | mistranslation | Грубая ошибка машинного перевода: 'caster будет unможете использовать' - такого слова нет. 'Enlarge§r: увеличить radius  |
| quest.AAAAAAAAAAAAAAAAAAAFdA.desc | major | mistranslation | Машинный перевод: 'Dark материя позволяет его wielder к shoot', 'не будет gain warp из используя'. Перемешаны языки, неп |
| quest.AAAAAAAAAAAAAAAAAAAFdA.name | major | mistranslation | 'Taste их Own Medicine' - неполный перевод с пропущенным 'A'. Должно быть 'Попробуй сам свою медицину' или похожее идиом |
| quest.AAAAAAAAAAAAAAAAAAAFdQ.desc | major | mistranslation | Машинный перевод с грамматическими ошибками: 'можно используется к move', 'будет настроить time', 'unможете использовать |
| quest.AAAAAAAAAAAAAAAAAAAFdQ.name | major | mistranslation | Плохой перевод 'So Take Me Back in Time...' как 'поэтому взять мне Back в Time...'. Английский текст не переведен, струк |
| quest.AAAAAAAAAAAAAAAAAAAFdg.desc | major | mistranslation | Машинный перевод: 'можно используется к начать', 'на будет' - явная ошибка вместо 'по желанию'. Грамматика сломана по вс |
| quest.AAAAAAAAAAAAAAAAAAAFdg.name | major | mistranslation | 'может вы Feel Sunshine?' - неправильный перевод. 'Feel' не переведено, грамматика неправильна. Должно быть 'Чувствуешь  |
| quest.AAAAAAAAAAAAAAAAAAAFdw.desc | major | mistranslation | Машинный перевод: 'можно equipped через любой', 'кристалл кровь like когда killed с кристалл Dagger'. Смешаны языки, неп |
| quest.AAAAAAAAAAAAAAAAAAAFeA.desc | major | mistranslation | Машинный перевод со сломанной грамматикой: 'позволяет его user к teleport', 'как long как', 'это можно используется к tr |
| quest.AAAAAAAAAAAAAAAAAAAFeA.name | major | mistranslation | 'Walking является Too Hard...' - неправильный перевод. 'Walking' и 'Too Hard' не переведены. Должно быть что-то вроде 'Х |
| quest.AAAAAAAAAAAAAAAAAAAFeQ.desc | major | mistranslation | Машинный перевод: 'Try к add Potency', 'на уровень 3 вы можете add Chain Lightning'. Полностью не переведено на русский, |
| quest.AAAAAAAAAAAAAAAAAAAFgA.desc | major | mistranslation | "капли экономии энергии" неправильно переводит "save a little power", должно быть "того, чтобы сэкономить энергию". Такж |
| quest.AAAAAAAAAAAAAAAAAAAFgw.name | major | terminology | "тира" - это транслитерация английского "tier", должно быть "уровня" или "яруса" |
| quest.AAAAAAAAAAAAAAAAAAAFhQ.name | major | fluency | "Тебе это не понравится, уж поверь, и на IV тоже 1-4" - запутанный и неправильный порядок слов, смысл исказился |
| quest.AAAAAAAAAAAAAAAAAAAFiA.name | major | mistranslation | "Mallard Rust Smelly" переведено как "Плавильная доменная печь" - полная ошибка, перевод не соответствует исходному текс |
| quest.AAAAAAAAAAAAAAAAAAAFiQ.desc | major | fluency | "Платину также можно добыть промыв" - грамматическая ошибка, "промыв" должно быть "промыв или промыв" + "никелевую руду" |
| quest.AAAAAAAAAAAAAAAAAAAFig.name | major | mistranslation | "EU packets" переведено как "электрические заряды", должно быть "пакеты EU" или "единицы энергии". Также есть лишний про |
| quest.AAAAAAAAAAAAAAAAAAAFjg.desc | major | mistranslation | "...очищенная руда мутится" полностью неправильно переводит "all the live long day" - идиоматическое выражение совсем по |
| quest.AAAAAAAAAAAAAAAAAAAFmA.desc | major | mistranslation | Значительное искажение смысла: 'Moon lander' переведено как 'посадочный модуль 1-го уровня' (неправильно добавлена ступе |
| quest.AAAAAAAAAAAAAAAAAAAFmg.desc | major | fluency | 'Moving faster on the Moon' переведено неправильно с грамматическими ошибками и неловкой конструкцией 'Рассекать на нём  |
| quest.AAAAAAAAAAAAAAAAAAAFmw.desc | major | mistranslation | В примечании: 'turn it back into a schematic in a PLE' переведено как 'конвертировать в новые схемы с помощью лазерного  |
| quest.AAAAAAAAAAAAAAAAAAAFoA.desc | major | fluency | Грамматически неловкий текст: 'принимает собираемый кислородным сборщиком кислород' неправильное построение; повторение  |
| quest.AAAAAAAAAAAAAAAAAAAFoQ.desc | major | mistranslation | Значительное расширение текста; 'claim and unclaim chunks' переведено с лишними объяснениями об отключении спавна, котор |
| quest.AAAAAAAAAAAAAAAAAAAFpQ.desc | major | mistranslation | Третий абзац существенно сокращен и переделан; отсутствуют ключевые фразы 'Full moon is the start of the moon day, new ( |
| quest.AAAAAAAAAAAAAAAAAAAFtw.name | major | formatting | Опечатка в русском слове: 'космосме' должно быть 'космосе' |
| quest.AAAAAAAAAAAAAAAAAAAFxA.name | major | formatting | Код цвета §2 (зеленый) заменен на §a (светло-зеленый), что не соответствует исходному коду |
| quest.AAAAAAAAAAAAAAAAAAAFyA.name | major | formatting | Код цвета §a (светло-зеленый) заменен на §8 (темно-серый), что существенно меняет внешний вид |
| quest.AAAAAAAAAAAAAAAAAAAFyw.desc | major | mistranslation | Неправильный перевод инструкций: 'После того как ты освоишься' неверно передает смысл 'After you've mastered'; 'набери ж |
| quest.AAAAAAAAAAAAAAAAAAAFzA.desc | major | mistranslation | Критическая ошибка: 'отлей специальную форму' означает 'отлить/изготовить форму', а не 'используй форму'; правильно долж |
| quest.AAAAAAAAAAAAAAAAAAAFzQ.name | major | formatting | Код цвета §5 (фиолетовый) заменен на §2 (зеленый), что не соответствует исходному тону |
| quest.AAAAAAAAAAAAAAAAAAAG-g.desc | major | mistranslation | Неправильный перевод 'excessive Blub' как 'утопление'; следует перевести как 'чрезмерное количество пузырьков' или анало |
| quest.AAAAAAAAAAAAAAAAAAAG-w.desc | major | mistranslation | Машинный перевод с англицизмами и разломанной грамматикой. 'holds 4 data sticks' оставлен на английском, случайные англи |
| quest.AAAAAAAAAAAAAAAAAAAG0w.desc | major | mistranslation | Машинный перевод с грубыми ошибками грамматики и пропущенными английскими словами. Фразы типа 'через магия technology',  |
| quest.AAAAAAAAAAAAAAAAAAAG1A.desc | major | mistranslation | Смешивание английского и русского: 'Arithmetic Logic схемы', 'numerous parts', 'typically в groups 8-16'. Много англициз |
| quest.AAAAAAAAAAAAAAAAAAAG1Q.name | major | mistranslation | Полностью разломанный перевод: 'все ваш Card являются Belong к Us'. Это смесь неправильного русского и английского. Долж |
| quest.AAAAAAAAAAAAAAAAAAAG1g.desc | major | mistranslation | Машинный перевод с англицизмами: 'Gotta получить', 'essentially temporary storage', 'rapidly accessed via'. Много неправ |
| quest.AAAAAAAAAAAAAAAAAAAG2A.desc | major | mistranslation | Машинный перевод с грамматическими ошибками: 'поэтому controlling', 'берёт HV схема к скрафтить', 'их поставить'. Требуе |
| quest.AAAAAAAAAAAAAAAAAAAG2Q.desc | major | mistranslation | Машинный перевод: 'Cache мне outside', 'будет essentially быть как fast', 'процессы data'. Много англицизмов и неправиль |
| quest.AAAAAAAAAAAAAAAAAAAG2w.desc | major | mistranslation | Машинный перевод: 'screwdriver и wrench в один', 'Not really necessary инструмент', 'я suggest referring к ваш'. Смешива |
| quest.AAAAAAAAAAAAAAAAAAAG3w.desc | major | mistranslation | Машинный перевод: 'Congratulations, мы иметь parts', 'к начать создание', 'Let's начать с базовый'. Требуется полный пер |
| quest.AAAAAAAAAAAAAAAAAAAG8g.desc | major | other | Грамматическая ошибка в строке «Откладывайте яйца» — неверная глагольная форма. Должно быть существительное или причасти |
| quest.AAAAAAAAAAAAAAAAAAAG9Q.desc | major | mistranslation | В списке предметов добавлены «перчатки», которых нет в английском оригинале. Также «смотреть вдаль» не совсем корректно  |
| quest.AAAAAAAAAAAAAAAAAAAGAA.name | major | formatting | Коды цветов повреждены: оригинальный §3§l (голубой) изменён на §c§l (красный). Необходимо сохранить точные коды форматир |
| quest.AAAAAAAAAAAAAAAAAAAGAQ.name | major | formatting | Цветовой код изменён неверно (§5 на §2), и название бренда «Black and Decker» частично переведено — правильно либо остав |
| quest.AAAAAAAAAAAAAAAAAAAGBQ.desc | major | mistranslation | Значительные добавления и переделки текста, не присутствующие в исходнике: добавлены объяснения про Side Inventory Key,  |
| quest.AAAAAAAAAAAAAAAAAAAGEw.name | major | untranslated | Полуобработанный машинный перевод: 'Mutate ваш Saplings' содержит английские слова прямо в русском тексте. Должно быть ' |
| quest.AAAAAAAAAAAAAAAAAAAGFA.name | major | mistranslation | Mouthwash переведён как 'освежитель воздуха', но это неправильно - мouthwash это полоскание для рта. Должно быть 'Исполь |
| quest.AAAAAAAAAAAAAAAAAAAGFQ.desc | major | untranslated | Сильно искажённый машинный перевод с англо-русской мешаниной: 'эти saplings может initially быть acquired только через и |
| quest.AAAAAAAAAAAAAAAAAAAGHA.name | major | mixed_language | Английское слово 'Spirit' оставлено нетранслитерированным и смешано с русским 'мир' с малой буквы. Должно быть: 'Мир дух |
| quest.AAAAAAAAAAAAAAAAAAAGHg.name | major | untranslated | Английская фраза 'Early Bird получает...Nightmare?' не переведена. Должно быть полностью на русском. |
| quest.AAAAAAAAAAAAAAAAAAAGHw.desc | major | mistranslation | Текст машинно переведён и содержит смешанный разбитый английский с русским ('ваш второй visit hopefully went немного bet |
| quest.AAAAAAAAAAAAAAAAAAAGJg.desc | major | mistranslation | Машинный перевод с обильным смешанным английским текстом ('является ingredient сделано через distilling diamond в distil |
| quest.AAAAAAAAAAAAAAAAAAAGKA.desc | major | mistranslation | Полностью машинно переведённый текст с смешанным английским ('установка ваш Dream Weaver Nightmares закрыть к где вы sle |
| quest.AAAAAAAAAAAAAAAAAAAGKA.name | major | mixed_language | Английские слова 'Spirit' и 'Dream' не переведены. Должно быть: 'Мир духов - Мечта' или 'Мир духов - Кошмар'. |
| quest.AAAAAAAAAAAAAAAAAAAGKQ.desc | major | mistranslation | Машинный перевод с обильным нетранслитерированным английским ('в daytime вы можете найти несколько wispy cotton'). Полно |
| quest.AAAAAAAAAAAAAAAAAAAGKQ.name | major | untranslated | Смешанный английский и русский ('Wake мне Up Later'). Должно быть полностью переведено. |
| quest.AAAAAAAAAAAAAAAAAAAGKg.desc | major | mistranslation | Машинный перевод с смешанным английским ('Fanciful Thread является spun из Wispy Cotton'). Требует полного переперевода. |
| quest.AAAAAAAAAAAAAAAAAAAGLA.desc | major | mistranslation | Машинный перевод с нетранслитерированным английским ('Dream Weaver Iron Arm будет add mining скорость boost'). Невразуми |
| quest.AAAAAAAAAAAAAAAAAAAGLQ.desc | major | mistranslation | Машинный перевод со смешанным английским ('Dream Weaver Fleet Foot будет add скорость boost'). Требует переработки. |
| quest.AAAAAAAAAAAAAAAAAAAGLg.desc | major | mistranslation | Машинный перевод со смешанным английским ('Dream Weaver Fasting будет add boost'). Полностью нуждается в переводе. |
| quest.AAAAAAAAAAAAAAAAAAAGLw.desc | major | mistranslation | Явный машинный перевод. Английское прозаическое содержание не переведено. Структура разрушена: 'ingredient используется  |
| quest.AAAAAAAAAAAAAAAAAAAGMA.desc | major | mistranslation | Явный машинный перевод с разрушенной структурой. Много английского текста оставлено: 'captures essence Spirit мир', 'bre |
| quest.AAAAAAAAAAAAAAAAAAAGMA.name | major | mistranslation | Название не соответствует исходному. 'Brew of Flowing Spirit' должно быть 'Настой текучего духа' или подобное, а не 'Нас |
| quest.AAAAAAAAAAAAAAAAAAAGMg.desc | major | mistranslation | Явный машинный перевод. Строчная буква в начале предложения 'вы вероятно' (должно 'Вы вероятно' или 'Ты вероятно'), 'Dis |
| quest.AAAAAAAAAAAAAAAAAAAGMw.desc | major | mistranslation | Явный машинный перевод. Грамматика разрушена: 'мы иметь' (неправильное спряжение), 'мы может' (неправильное согласование |
| quest.AAAAAAAAAAAAAAAAAAAGNQ.desc | major | mistranslation | Перевод не соответствует исходному. Исходное 'Selling wispy cotton for coins' переведено как 'Я готов купить у тебя тонк |
| quest.AAAAAAAAAAAAAAAAAAAGNg.desc | major | mistranslation | Явный машинный перевод. Английский текст перемешан с русским: 'Go и найти', 'brew несколько', 'plant несколько', 'Gravel |
| quest.AAAAAAAAAAAAAAAAAAAGNw.desc | major | mistranslation | Явный машинный перевод. 'для later использовать делать' — нарушена грамматика. Английское 'later' оставлено. Правильно:  |
| quest.AAAAAAAAAAAAAAAAAAAGNw.name | major | mistranslation | Неполный перевод. 'Exhale of the Dreaming Horned One' переведено как 'Exhale Dreaming Horned один' — фактически не перев |
| quest.AAAAAAAAAAAAAAAAAAAGOA.desc | major | mistranslation | Явный машинный перевод. 'для все ваш offerings' — нарушена грамматика, неправильное согласование. 'spinning wheel нужно  |
| quest.AAAAAAAAAAAAAAAAAAAGOA.name | major | mistranslation | Неполный перевод. 'Offerings в ваш Dreams' — смешанный англо-русский текст. Требуется полный перевод: 'Подношения в ваши |
| quest.AAAAAAAAAAAAAAAAAAAGOQ.desc | major | mistranslation | Явный машинный перевод. 'kettle нужно в spirit мир too' — английский текст не переведён. Должно быть: 'Чайник также нуже |
| quest.AAAAAAAAAAAAAAAAAAAGOQ.name | major | mistranslation | Неполный перевод. 'Kettle для Spirit мир' — смешанный англо-русский текст. Должно быть полное прозаическое название на р |
| quest.AAAAAAAAAAAAAAAAAAAGOg.desc | major | mistranslation | Явный машинный перевод. 'вы нужно spinning wheel' — нарушена грамматика (неправильное спряжение), 'к наконец' — неправил |
| quest.AAAAAAAAAAAAAAAAAAAGOg.name | major | mistranslation | Неполный перевод. 'Spinning ваш Dreams' — смешанный англо-русский. Должно быть 'Прядём свои мечты' или подобное. |
| quest.AAAAAAAAAAAAAAAAAAAGOw.desc | major | mistranslation | Явный машинный перевод. 'является spun из', 'Это ingredient используется к сделать', 'этот можно brewed' — смешанный анг |
| quest.AAAAAAAAAAAAAAAAAAAGPA.desc | major | mistranslation | Явный машинный перевод. 'для later использовать делать' — нарушена грамматика, неправильный порядок слов. Английское 'la |
| quest.AAAAAAAAAAAAAAAAAAAGPA.name | major | mistranslation | Неполный перевод. 'Odour Purity в Dreams' — смешанный англо-русский. Должно быть полное название на русском: 'Аромат чис |
| quest.AAAAAAAAAAAAAAAAAAAGRg.desc | major | untranslated | Оставлено английское "Sugar beet" - следует "свёкла сахарная" |
| quest.AAAAAAAAAAAAAAAAAAAGWQ.desc | major | mistranslation | Полностью машинный перевод - английские слова смешаны с русским, нарушена грамматика и смысл. Требует полной переделки |
| quest.AAAAAAAAAAAAAAAAAAAGWQ.name | major | untranslated | "Interacting с Stuff" - смешанный язык. Должно быть полностью на русском |
| quest.AAAAAAAAAAAAAAAAAAAGWg.desc | major | mistranslation | Полностью машинный перевод - английские слова смешаны с русским буквально, нарушена грамматика и структура. Требует полн |
| quest.AAAAAAAAAAAAAAAAAAAGWw.desc | major | mistranslation | Полностью машинный перевод - английские слова смешаны с русским буквально, нарушена грамматика и структура. Требует полн |
| quest.AAAAAAAAAAAAAAAAAAAGXA.name | major | mistranslation | "предмет Overflow Chip" - смешанный язык и неправильный порядок слов |
| quest.AAAAAAAAAAAAAAAAAAAGXQ.name | major | mistranslation | "Dynamic предмет Responder" - смешанный язык и неправильный порядок слов |
| quest.AAAAAAAAAAAAAAAAAAAGXg.desc | major | mistranslation | Машинный перевод с обильными утечками английских слов (chip, inventory, pipes, responder), сломанная грамматика, текст н |
| quest.AAAAAAAAAAAAAAAAAAAGYg.desc | major | mistranslation | Машинный перевод с англицизмами и сломанной грамматикой (этот труба lets, тот являются, тот можно crafted) - текст непра |
| quest.AAAAAAAAAAAAAAAAAAAGZQ.desc | major | mistranslation | Смешанный перевод с англицизмами (поставить к store, we'll использовать, filled это, sulfuric лёгкий топливо) и граммати |
| quest.AAAAAAAAAAAAAAAAAAAGZQ.name | major | untranslated | Слово 'Storing' остаётся полностью не переведено в названии |
| quest.AAAAAAAAAAAAAAAAAAAGZw.desc | major | mistranslation | Обильный машинный перевод с англицизмами во всём тексте (Now это time, chemical реактор, fill это, interface труба, extr |
| quest.AAAAAAAAAAAAAAAAAAAGZw.name | major | untranslated | Слово 'Desulfurizing' не переведено и остаётся в названии |
| quest.AAAAAAAAAAAAAAAAAAAGaA.desc | major | mistranslation | Машинный перевод с множеством англицизмов (Hook up chemical реактор, Distill тот diluted, иметь completely automatic) и  |
| quest.AAAAAAAAAAAAAAAAAAAGbg.desc | major | mistranslation | Машинный перевод с англицизмами и сломанной грамматикой (Spinning hay в gold sounds, с ваш новый magical, может try tric |
| quest.AAAAAAAAAAAAAAAAAAAGbw.desc | major | mistranslation | Машинный перевод с неправильной грамматикой и англицизмами (к сделать appropriate, вам понадобится к сделать, с ваш diam |
| quest.AAAAAAAAAAAAAAAAAAAGcw.desc | major | mistranslation | Машинный перевод с англицизмами и грамматическими ошибками (path laden с энергия, Behold mortal, и быть terrified) - сме |
| quest.AAAAAAAAAAAAAAAAAAAGdA.name | major | formatting | Цветовой код изменен со §a на §8 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGdQ.name | major | formatting | Цветовой код изменен с §5 на §2 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGdw.desc | major | mistranslation | Невразумительная передача "CCC tab" как 'вкладке "Монеты, монеты, монеты''" - неправильные кавычки и непонятное значение |
| quest.AAAAAAAAAAAAAAAAAAAGdw.name | major | formatting | Цветовой код изменен со §a на §8 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGeA.name | major | mistranslation | Текст переведен как 'Яйцо Эндера' вместо 'Мутация яйца' - полное искажение смысла; также неправильный цветовой код §8 вм |
| quest.AAAAAAAAAAAAAAAAAAAGeQ.name | major | formatting | Цветовой код изменен со §a на §8 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGeg.name | major | formatting | Цветовой код изменен со §a на §8 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGew.name | major | formatting | Цветовой код изменен со §a на §8 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGfA.name | major | formatting | Цветовой код изменен с §9 на §5 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGfQ.name | major | formatting | Цветовой код изменен с §9 на §5 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGfg.name | major | formatting | Цветовой код изменен с §9 на §5 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGfw.name | major | formatting | Цветовой код изменен с §9 на §5 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGgA.name | major | formatting | Цветовой код изменен с §9 на §5 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGgg.name | major | formatting | Цветовой код изменен со §b на §9 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGgw.name | major | formatting | Цветовой код изменен со §b на §9 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGhQ.name | major | formatting | Цветовой код изменен со §b на §9 - форматирование поломано |
| quest.AAAAAAAAAAAAAAAAAAAGjQ.name | major | mistranslation | Заголовок переведен как 'Более продвинутые печатные платы' вместо 'Пустая печатная плата армированная стекловолокном' -  |
| quest.AAAAAAAAAAAAAAAAAAAGpw.name | major | mistranslation | 'Potassium Nitrate' переведен как 'Нитрат натрия' (натрий вместо калия) - критическая ошибка. Должно быть 'Нитрат калия' |
| quest.AAAAAAAAAAAAAAAAAAAGrw.desc | major | mistranslation | Название химического соединения 'Tetraindiumditindibariumtitaniumheptacoppertetrakaidekaoxide' некорректно переведено ка |
| quest.AAAAAAAAAAAAAAAAAAAGrw.name | major | mistranslation | Сверхпроводник (singular) вместо сверхпроводников (plural). Источник говорит Superconductors (multiple) |
| quest.AAAAAAAAAAAAAAAAAAAGsA.desc | major | mistranslation | EV circuit assembler переведён как «IV сборщика электросхем», что ошибка тира - должен быть EV (не IV) |
| quest.AAAAAAAAAAAAAAAAAAAGsg.desc | major | mistranslation | «они годятся только как замена ULV электросхемам» неправильно - в источнике сказано что нельзя использовать для создания |
| quest.AAAAAAAAAAAAAAAAAAAGxw.name | major | formatting | Цветовой код изменён с §3 на §c |
| quest.AAAAAAAAAAAAAAAAAAAGyA.desc | major | mistranslation | Фраза 'Более трубы высокого тира' некорректна, должно быть 'Для труб высокого уровня' |
| quest.AAAAAAAAAAAAAAAAAAAGyQ.name | major | mistranslation | Название переведено неверно: 'More Red, Less Wheat' должно быть 'Больше красного, меньше пшеницы' |
| quest.AAAAAAAAAAAAAAAAAAAGyg.name | major | formatting | Цветовой код изменён с §2 на §a |
| quest.AAAAAAAAAAAAAAAAAAAGyw.name | major | formatting | Цветовой код изменён с §9 на §5 |
| quest.AAAAAAAAAAAAAAAAAAAGzQ.name | major | formatting | Цветовой код изменён с §3 на §c |
| quest.AAAAAAAAAAAAAAAAAAAH0Q.desc | major | mistranslation | Текст почти полностью на английском с вкраплениями русского. Машинный перевод с разрывом фраз. Требуется полный пересказ |
| quest.AAAAAAAAAAAAAAAAAAAH0g.desc | major | mistranslation | Смешанный английский и русский текст, нарушена грамматика. Множество недопереводов: 'setting', 'inside face', 'block', ' |
| quest.AAAAAAAAAAAAAAAAAAAH0w.desc | major | mistranslation | Сломанный синтаксис, английский текст не переведён ('Transforming', 'change', 'collision box', 'door', 'whatever'). Маши |
| quest.AAAAAAAAAAAAAAAAAAAH1A.desc | major | mistranslation | Недопереводы: 'Advanced', 'add/remove'. Грамматические ошибки: 'может add/remove предметы' вместо 'может добавлять/удаля |
| quest.AAAAAAAAAAAAAAAAAAAH2Q.desc | major | mistranslation | Английский текст перемешан с русским: 'Sign Updater', 'MIM', 'update external' не переведены. Грамматика нарушена ('позв |
| quest.AAAAAAAAAAAAAAAAAAAH2g.desc | major | mistranslation | Тяжёлый машинный перевод: множество недопереводов ('Item', 'Valve', 'factory manager', 'suck', 'dropped', 'push', 'direc |
| quest.AAAAAAAAAAAAAAAAAAAH2w.desc | major | mistranslation | Недопереводы основных слов: 'Rapid', 'Item', 'Valves', 'pick up', 'delays' оставлены на английском. Грамматика нарушена  |
| quest.AAAAAAAAAAAAAAAAAAAH2w.name | major | untranslated | Заголовок остался на английском 'Rapid Item Valve'. Должен быть переведён как 'Быстрый предметный клапан' или аналогично |
| quest.AAAAAAAAAAAAAAAAAAAH3Q.desc | major | mistranslation | Машинный перевод с перемешиванием английского текста: 'act как Inventory cable, extending range' - английский текст не п |
| quest.AAAAAAAAAAAAAAAAAAAH3w.desc | major | mistranslation | Неполный перевод: 'reads redstone signals на каждый его 6 faces' - английский текст смешан с русским |
| quest.AAAAAAAAAAAAAAAAAAAH4A.desc | major | mistranslation | Машинный перевод: 'может break, pickup' - глаголы не переведены, неполный перевод |
| quest.AAAAAAAAAAAAAAAAAAAH4Q.desc | major | mistranslation | Машинный перевод: 'позволяет ваш MIM к detect когда блок update occurs' - грамматически некорректно, английский не перев |
| quest.AAAAAAAAAAAAAAAAAAAH5A.desc | major | mistranslation | Тяжёлый машинный перевод: множество английских слов смешано с русским текстом, грамматика нарушена |
| quest.AAAAAAAAAAAAAAAAAAAH5g.desc | major | mistranslation | Машинный перевод: 'Instead chest', 'how о', 'pouch вы можете' - англо-русское перемешивание, грамматические ошибки |
| quest.AAAAAAAAAAAAAAAAAAAH5g.name | major | mistranslation | 'тот Chest является Too большой' - неправильная грамматика и смешивание языков |
| quest.AAAAAAAAAAAAAAAAAAAH9A.name | major | mistranslation | Переводит собственное имя 'Hephaestus' как 'Божественная версия', теряя смысл названия |
| quest.AAAAAAAAAAAAAAAAAAAH9Q.name | major | mistranslation | Теряет смысл игры слов 'Spools and spools' (повтор), переводя как просто 'клубок проводов' |
| quest.AAAAAAAAAAAAAAAAAAAHAA.name | major | mistranslation | Цвет изменён с §5 на §2; теряется смысл пуна 'Inkjet' переводом как просто 'принтер' |
| quest.AAAAAAAAAAAAAAAAAAAHBA.desc | major | fluency | Множественные ошибки: 'Есть ещё' грамматически неверно; 'Удваивай' должно быть 'Размножай'; 'Пятицентовик' неправильный  |
| quest.AAAAAAAAAAAAAAAAAAAHCw.desc | major | mistranslation | 'хэви-металл группы' неуместен (в англ. 'cover band'); 'Пятицентовик' неправильный перевод для 'Nickelback'; путаная стр |
| quest.AAAAAAAAAAAAAAAAAAAHDw.desc | major | mistranslation | Полное несоответствие исходному тексту. Источник говорит об альтернативе добыче листьев стали вместо поиска в Сумеречном |
| quest.AAAAAAAAAAAAAAAAAAAHJw.desc | major | mistranslation | «механизм» неправильно передаёт «item» (предмет); «Найди себе одну штучку» невероятно неформально и непрофессионально дл |
| quest.AAAAAAAAAAAAAAAAAAAHLg.desc | major | fluency | «Побродив пару минут» неуклюже; «Найди одну штучку» слишком неформально; «совершить грешок» неправильное выражение (долж |
| quest.AAAAAAAAAAAAAAAAAAAHMA.name | major | formatting | Неправильно добавлены цветовые коды §2§l§n, которых нет в оригинале (English: просто текст без кодов); форматирование по |
| quest.AAAAAAAAAAAAAAAAAAAHMQ.desc | major | mistranslation | Фраза «беги как черт от ладана» — неправильная/перепутанная идиома, не имеет смысла в контексте; должно быть «беги изо в |
| quest.AAAAAAAAAAAAAAAAAAAHNQ.name | major | formatting | Коды цвета повреждены: §3 (исходный) изменён на §c |
| quest.AAAAAAAAAAAAAAAAAAAHNg.name | major | formatting | Коды цвета повреждены: §5 (исходный) изменён на §2 |
| quest.AAAAAAAAAAAAAAAAAAAHNw.name | major | formatting | Коды цвета повреждены: §a (исходный) изменён на §8 |
| quest.AAAAAAAAAAAAAAAAAAAHPQ.name | major | mistranslation | Исходная фраза 'Moron's Manual for Effective EBFing' переведена только как 'Электрическая Доменная Печь для чайников', п |
| quest.AAAAAAAAAAAAAAAAAAAHPg.desc | major | mistranslation | В описании мода сказано 'Ground Gardens' (конкретное место в моде), но переведено как 'Земляные кусты' - неправильное на |
| quest.AAAAAAAAAAAAAAAAAAAHQQ.desc | major | mistranslation | Фраза 'пока ты ждёшь, когда аромат самой вкусной еды выветрится' - неверный перевод. В оригинале 'while you wait for the |
| quest.AAAAAAAAAAAAAAAAAAAHSQ.desc | major | mistranslation | Фраза 'полученную в результате его страданий жидкость отлей в слепок сковорады' - неверный перевод и странный стиль. В о |
| quest.AAAAAAAAAAAAAAAAAAAHTw.desc | major | mistranslation | Опущена последняя часть предложения 'anything someone wanted to make harder to make' — существенный смысловой элемент ут |
| quest.AAAAAAAAAAAAAAAAAAAHTw.name | major | formatting | Цвет изменён со §9 (синий) на §5 (фиолетовый) — форматирующий код повреждён |
| quest.AAAAAAAAAAAAAAAAAAAHUw.desc | major | formatting | В оригинале нет форматирующих кодов §l и §o, но они добавлены в переводе — форматирование повреждено и не соответствует  |
| quest.AAAAAAAAAAAAAAAAAAAHVA.name | major | formatting | Цвет изменён со §9 (синий) на §5 (фиолетовый) — форматирующий код повреждён |
| quest.AAAAAAAAAAAAAAAAAAAHVQ.name | major | formatting | Цвет изменён со §9 (синий) на §5 (фиолетовый) — форматирующий код повреждён |
| quest.AAAAAAAAAAAAAAAAAAAHVg.name | major | formatting | Цвет изменён со §a (зелёный) на §8 (серый) — форматирующий код повреждён |
| quest.AAAAAAAAAAAAAAAAAAAHVw.name | major | formatting | Цвет изменён со §a (зелёный) на §8 (серый) — форматирующий код повреждён |
| quest.AAAAAAAAAAAAAAAAAAAHWA.name | major | formatting | Цвет изменён со §a (зелёный) на §8 (серый) — форматирующий код повреждён |
| quest.AAAAAAAAAAAAAAAAAAAHXw.name | major | formatting | Цвет изменён со §5 (фиолетовый) на §2 (тёмный зелёный) — форматирующий код повреждён |
| quest.AAAAAAAAAAAAAAAAAAAHYA.name | major | formatting | Цвет изменён со §3 (циан) на §c (красный) — форматирующий код повреждён |
| quest.AAAAAAAAAAAAAAAAAAAHYg.name | major | formatting | Цвет изменён со §b (голубой) на §9 (синий) — форматирующий код повреждён |
| quest.AAAAAAAAAAAAAAAAAAAHYw.name | major | formatting | Цвет изменён со §a (зелёный) на §8 (серый) — форматирующий код повреждён |
| quest.AAAAAAAAAAAAAAAAAAAH_w.name | major | fluency |  |
| quest.AAAAAAAAAAAAAAAAAAAHaA.name | major | mistranslation |  |
| quest.AAAAAAAAAAAAAAAAAAAHaw.name | major | fluency |  |
| quest.AAAAAAAAAAAAAAAAAAAHbA.name | major | fluency |  |
| quest.AAAAAAAAAAAAAAAAAAAHbQ.name | major | fluency |  |
| quest.AAAAAAAAAAAAAAAAAAAHcQ.name | major | mistranslation | Полностью испорченный машинный перевод. Текст 'большой нагреть Exchanger - Fermat's последний' содержит ошибки грамматик |
| quest.AAAAAAAAAAAAAAAAAAAHeQ.desc | major | mistranslation | Множество ошибок: 'форма' вместо 'пластина' в контексте печати; 'LootBag' оставлен на английском без объяснения; 'парочк |
| quest.AAAAAAAAAAAAAAAAAAAHfg.name | major | formatting | Неправильный цвет: в оригинале §5 (фиолетовый), а в переводе §2 (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAHfw.name | major | formatting | Неправильный цвет: в оригинале §3 (голубой), а в переводе §c (красный) |
| quest.AAAAAAAAAAAAAAAAAAAHgQ.name | major | formatting | Неправильный цвет: в оригинале §9 (синий), а в переводе §5 (фиолетовый) |
| quest.AAAAAAAAAAAAAAAAAAAHhQ.name | major | formatting | Неправильный цвет: в оригинале §a (зелёный), а в переводе §8 (серый) |
| quest.AAAAAAAAAAAAAAAAAAAHhg.name | major | formatting | Неправильный цвет: в оригинале §2 (тёмно-зелёный), а в переводе §a (светло-зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAHiQ.desc | major | mistranslation | Переведено неправильно: оригинал говорит про Reactoria leaves и 4x Pitchblende ore, а перевод расширивает это на несколь |
| quest.AAAAAAAAAAAAAAAAAAAHlQ.desc | major | mistranslation | Переводит "custom stair" как "обычные ступеньки" (ordinary stairs). Также "написать в NEI" вместо "поискать в NEI". |
| quest.AAAAAAAAAAAAAAAAAAAHoQ.desc | major | mistranslation | Переводит название вкладки как "Пчеловодство" (Beekeeping), но оригинал указывает "How to Be(e)" tab. Неверное название  |
| quest.AAAAAAAAAAAAAAAAAAAHog.desc | major | mistranslation | Запутанное объяснение с повтором слова "анализатор"; "для анализа одного человека" вместо "одного образца" (specimen). Н |
| quest.AAAAAAAAAAAAAAAAAAAHrg.desc | major | mistranslation | Ошибка перевода: 'с помощью ПКМ' неправильно - в оригинале нет упоминания о ПКМ. 'Sneak' значит крад/присед, не ПКМ. Так |
| quest.AAAAAAAAAAAAAAAAAAAHsQ.desc | major | fluency | Множество проблем: неправильный перевод 'One plus/minus' как 'Единственный плюс/минус', неестественно звучит 'они не пад |
| quest.AAAAAAAAAAAAAAAAAAAHug.desc | major | fluency | Множество проблем: 'ПКМ рукой' - неправильно, should be 'shift + ПКМ'; 'Используй ключ' - неправильный перевод 'wrench'; |
| quest.AAAAAAAAAAAAAAAAAAAHuw.desc | major | fluency | Множество грамматических и стилистических ошибок: 'единица RF занимает весь пакет EU' неправильный перевод; 'ПКМ рукой'  |
| quest.AAAAAAAAAAAAAAAAAAAHxg.desc | major | mistranslation | Грубая машинная переводка с кодированием English-ru: 'Ever finished wonderful program и затем realized ваш Manager нужно |
| quest.AAAAAAAAAAAAAAAAAAAHyA.desc | major | mistranslation | Машинная переводка: 'Thaumic Machina offers жезл Augmentations. эти полезный modifications...' - оставлены английские сл |
| quest.AAAAAAAAAAAAAAAAAAAHyA.name | major | untranslated | 'жезл Enhancements' - оставлено английское слово 'Enhancements'; должно быть 'Улучшения жезла' или подобное |
| quest.AAAAAAAAAAAAAAAAAAAHyQ.desc | major | mistranslation | 'зарядить Buffer augmentation к ваш жезл позволяет это к hold 25 percent больше vis' - грубая машинная переводка, наруше |
| quest.AAAAAAAAAAAAAAAAAAAHyQ.name | major | untranslated | 'зарядить Buffer' - оставлено английское слово; должно быть 'Буфер заряда' или подобное |
| quest.AAAAAAAAAAAAAAAAAAAHzw.desc | major | mistranslation | Машинная переводка: 'Redstone Emitter sends redstone signals на каждый его 6 faces...' - оставлены английские фразы и на |
| quest.AAAAAAAAAAAAAAAAAAAI-Q.name | major | formatting | Код цвета повреждён: §a§l (зелёный) изменён на §8§l (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAI-g.name | major | formatting | Код цвета повреждён: §a§l (зелёный) изменён на §8§l (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAI-w.name | major | formatting | Код цвета повреждён: §a§l (зелёный) изменён на §8§l (тёмно-серый) |
| quest.AAAAAAAAAAAAAAAAAAAI0g.desc | major | mistranslation | Машинный перевод с утечкой английского текста: оставлены непереведёнными фразы 'Aromatic Lumps', 'twice as effective', ' |
| quest.AAAAAAAAAAAAAAAAAAAI3Q.desc | major | mistranslation | Машинный перевод с утечкой английского текста: остаются непереведёнными 'Magenta пчёлы', 'Fastest production', 'come с', |
| quest.AAAAAAAAAAAAAAAAAAAI3g.desc | major | mistranslation | Машинный перевод: утечка английского текста ('Pink princesses provide pink dye'), грамматические ошибки ('они также имет |
| quest.AAAAAAAAAAAAAAAAAAAI3w.desc | major | mistranslation | Машинный перевод: утечка английского текста ('White пчёлы provide white dye'), недоделанный перевод ('разводить их из Wi |
| quest.AAAAAAAAAAAAAAAAAAAI4A.desc | major | mistranslation | Сильно нарушенный машинный перевод: неправильно оформленные фразы ('Dye пчёлы obviously', 'полезный для их traits'), сме |
| quest.AAAAAAAAAAAAAAAAAAAI4Q.desc | major | mistranslation | Машинный перевод: 'Blue princesses будет provide' - нарушено образование предложения, неправильное скручивание грамматик |
| quest.AAAAAAAAAAAAAAAAAAAI4g.desc | major | mistranslation | Разобранный машинный перевод: 'Batty пчёлы будет spawn', смешивание английского и русского, неправильная грамматика на в |
| quest.AAAAAAAAAAAAAAAAAAAI4w.desc | major | mistranslation | Сильный машинный перевод: 'Ghastly пчёлы будет spawn', 'иметь 1 fertility', 'к убедитесь' - неправильная грамматика и си |
| quest.AAAAAAAAAAAAAAAAAAAI5A.desc | major | mistranslation | Массивный машинный перевод: 'Smouldering drones будет spawn', неправильная терминология ('стержни' вместо 'стержни'), 'к |
| quest.AAAAAAAAAAAAAAAAAAAI5w.desc | major | mistranslation | Машинный перевод: 'Oily пчела', 'его соты производить самый масло', 'не является тот thrilling', 'используется up' - нар |
| quest.AAAAAAAAAAAAAAAAAAAI6Q.desc | major | mistranslation | Машинный перевод: 'Ancient пчёлы являются первый step', 'масло пчёлы в game' - неправильное склонение существительных и  |
| quest.AAAAAAAAAAAAAAAAAAAI6g.desc | major | mistranslation | Машинный перевод: 'Ocean пчела можно hard', 'вода Creepers' вместо названия существа, 'Vending машина' - неправильный ко |
| quest.AAAAAAAAAAAAAAAAAAAI7A.desc | major | mistranslation | Машинный перевод: 'Miry пчёлы не являются too полезный', 'They'll открыть up', 'к найти biome' - нарушена грамматика, см |
| quest.AAAAAAAAAAAAAAAAAAAI7Q.desc | major | mistranslation | Машинный перевод: 'Elastic пчела будет на самом деле производить', 'No больше smelly Sulfur' - неправильная грамматика и |
| quest.AAAAAAAAAAAAAAAAAAAI7g.desc | major | mistranslation | Машинный перевод: 'master beekeeper нужно master registry', 'Убедитесь вы не получить любой tears' - неправильная грамма |
| quest.AAAAAAAAAAAAAAAAAAAI7w.desc | major | mistranslation | Машинный перевод: 'Agrarian пчёлы являются supposed', 'эффект не является really тот noticeable', 'You'll придётся быть' |
| quest.AAAAAAAAAAAAAAAAAAAI8A.desc | major | mistranslation | Машинный перевод: 'Like самый farmers', 'seem к spend', 'на самом деле doing много' - нарушена грамматика повсеместно. |
| quest.AAAAAAAAAAAAAAAAAAAI8Q.desc | major | mistranslation | Машинный перевод: 'sudo сделать мне sandwich', 'тот делает sandwich parts' - неправильная грамматика, пропущены предлоги |
| quest.AAAAAAAAAAAAAAAAAAAI8g.desc | major | mistranslation | Машинный перевод: 'Fertilizer пчела будет сделать', 'как well', смешивание английского и русского на всей длине. |
| quest.AAAAAAAAAAAAAAAAAAAI8w.desc | major | mistranslation | Машинный перевод: 'Apatite пчела требует', 'beneath это к разводить', 'семя масло', 'как well' - неправильная грамматика |
| quest.AAAAAAAAAAAAAAAAAAAI9A.desc | major | mistranslation | Машинный перевод: 'пчела к сделать', 'что insanity является этот', 'на least', 'к pay Незер visit' - полная разборка гра |
| quest.AAAAAAAAAAAAAAAAAAAIAw.desc | major | mistranslation | Грамматическая ошибка в начале: неправильное использование союзов (должна быть структура "Если..., то"). Также неточная  |
| quest.AAAAAAAAAAAAAAAAAAAIBA.desc | major | fluency | Неестественный перевод с запутанной структурой; фраза "путём установки 2 энерговводов" кажется скопированной из другого  |
| quest.AAAAAAAAAAAAAAAAAAAIBA.name | major | untranslated | Неполный перевод названия: переведено только "Не подходит для употребления в пищу", упущены остальные слова из оригинала |
| quest.AAAAAAAAAAAAAAAAAAAIDw.desc | major | mistranslation | "Клинки ПКМ" - ошибка (должно быть "Кликни ПКМ"); также несогласованное использование гифенации "сенти-вис" в разных мес |
| quest.AAAAAAAAAAAAAAAAAAAIEA.desc | major | mistranslation | Смешанный машинный перевод с английскими словами: 'nodes', 'unjarring', 'captured', 'cause', 'help', 'recharge' вставлен |
| quest.AAAAAAAAAAAAAAAAAAAIFA.desc | major | mistranslation | Машинный перевод с ошибками: 'если вы найдено' (неправильное согласование), смешанные английские слова 'book', 'enchantm |
| quest.AAAAAAAAAAAAAAAAAAAIIg.name | major | mistranslation | Повреждённый машинный перевод: 'создание пчёлы больше Comfortable' - смешанный регистр, неправильная грамматика, слово ' |
| quest.AAAAAAAAAAAAAAAAAAAIKQ.name | major | mistranslation | Машинный перевод: 'пчёлы через Millions' - должно быть 'Миллионы пчёл' или 'Пчёлы в миллионах' |
| quest.AAAAAAAAAAAAAAAAAAAILA.name | major | mistranslation | Машинный перевод: англ. слова 'Busy' и 'Buzzing Boldly' не переведены, фраза 'Busy пчёлы Buzzing Boldly' - бессмыслица |
| quest.AAAAAAAAAAAAAAAAAAAILQ.desc | major | mistranslation | Сильный машинный перевод: множество англ. слов оставлено непереведённым (Supporting, electron tubes, provides, functions |
| quest.AAAAAAAAAAAAAAAAAAAILg.desc | major | mistranslation | Машинный перевод: 'vastly accelerate' не переведено, 'bred' не переведено, 'allows' пропущен, смешано много англ. слов,  |
| quest.AAAAAAAAAAAAAAAAAAAILg.name | major | mistranslation | Машинный перевод: англ. части 'Say X-Bee' не переведены, получилось 'или следует я Say X-Bee?' - неграмотно |
| quest.AAAAAAAAAAAAAAAAAAAIMw.desc | major | mistranslation | Машинный перевод: 'Discovered genes являются logged' - неправильная грамматика, множество англ. слов не переведено (hand |
| quest.AAAAAAAAAAAAAAAAAAAINA.desc | major | mistranslation | Машинный перевод: 'Lab Stand является блок', 'placed через ПКМing', 'attaching это', 'accessed через ПКМing' - ненатурал |
| quest.AAAAAAAAAAAAAAAAAAAINg.desc | major | mistranslation | Машинный перевод: 'Registry объединить' (неправильная форма), 'existing четыре databases', 'sleek browser', 'позволить p |
| quest.AAAAAAAAAAAAAAAAAAAINw.desc | major | mistranslation | Машинный перевод: 'финальный step является inoculation', множество англ. слов не переведено (vastly, capable, organisms, |
| quest.AAAAAAAAAAAAAAAAAAAIPA.desc | major | mistranslation | Машинный перевод: 'этот database keeps track everything пчела' - англ. слова не переведены, грамматика нарушена, должно  |
| quest.AAAAAAAAAAAAAAAAAAAIPA.name | major | mistranslation | Машинный перевод: 'пчела больше Knowledgeable' - неправильная грамматика и смысл, должно быть 'Больше знаний о пчёлах' и |
| quest.AAAAAAAAAAAAAAAAAAAIPQ.desc | major | mistranslation | Машинный перевод: 'этот database tracks все ваш knowledge butterflies' - неправильная грамматика ('все ваш' вместо 'всё  |
| quest.AAAAAAAAAAAAAAAAAAAIQA.desc | major | mistranslation | Mistranslation: 'внутренний резервуар' should be 'встроенные резервуары' (plural); 'паровой и вертолётный ранцы' should  |
| quest.AAAAAAAAAAAAAAAAAAAIQw.desc | major | mistranslation | Critical error: 'рюкзак свинозомби' (zombie pigman backpack) is mistranslated from 'Pigman'; should be 'Pig' or 'Свиной  |
| quest.AAAAAAAAAAAAAAAAAAAISg.desc | major | mistranslation | Multiple errors: 'анализатор деревьев' should be 'Treealyzer' (proper noun); 'Для начала своих экспериментов со скрещива |
| quest.AAAAAAAAAAAAAAAAAAAIVw.desc | major | mistranslation | Blue Mahoe это не гибискус (гибискус), а древесный вид. 'Сочный вкус' неверно - должно быть 'сочность' (sappiness) |
| quest.AAAAAAAAAAAAAAAAAAAIVw.name | major | mistranslation | Blue Mahoe это не гибискус - неверное определение вида |
| quest.AAAAAAAAAAAAAAAAAAAIWg.desc | major | mistranslation | 'Шкафы' (cabinets) неверный перевод - в контексте речь идёт о машинах (machines), не о шкафах |
| quest.AAAAAAAAAAAAAAAAAAAIZA.desc | major | mistranslation | "IV тира" неправильная форма - должно быть "IV уровня" или "IV tier". "лазутроновых кристаллов" неточен - в оригинале "L |
| quest.AAAAAAAAAAAAAAAAAAAIZA.name | major | mistranslation | "лазутроновые чипы" неправильный перевод. Lapotron - это батарея из мода GregTech, не чип. Должно быть "Гравированные ла |
| quest.AAAAAAAAAAAAAAAAAAAIZg.desc | major | other | Большое количество ошибок: 1) "ЭХПФ" - необъяснённый акроним, должно быть расшифровано или оставлено как "AFSU"; 2) "ПКМ |
| quest.AAAAAAAAAAAAAAAAAAAI_A.desc | major | mistranslation | Значительные отклонения от оригинала: 1) "Сделай несколько капсул" неточно - речь идёт о "Cells" (ячейках), а не просто  |
| quest.AAAAAAAAAAAAAAAAAAAIaQ.desc | major | mistranslation | Явная машинная кальки и нарушение грамматики: "Fruity пчёлы будет сделать", "их fruit faster", "разводить их используя"  |
| quest.AAAAAAAAAAAAAAAAAAAIcA.desc | major | other | Множественные ошибки перевода: 1) "Shit+ПКМ" вместо "Shift+ПКМ" - явная ошибка; 2) Некорректные сокращения (ПКМ/Shift ми |
| quest.AAAAAAAAAAAAAAAAAAAIdg.desc | major | mistranslation | Машинный перевод, смешивание английского и русского. "Never having к использовать treetap again?" - прямое перемешивание |
| quest.AAAAAAAAAAAAAAAAAAAIdw.desc | major | mistranslation | Сильно повреждённый машинный перевод. "наконец, чёрный Gold. масло пчела, с proper... encouragement..." - смешивание язы |
| quest.AAAAAAAAAAAAAAAAAAAIew.desc | major | mistranslation | Сильный машинный перевод с множественными ошибками. "Blooming пчела будет bonemeal nearby saplings. этот может definitel |
| quest.AAAAAAAAAAAAAAAAAAAIfQ.desc | major | mistranslation | Машинный перевод с глубокими ошибками. "Certus Quartz пчела. Hmm, делает это иметь любой разведение requirements?" - сме |
| quest.AAAAAAAAAAAAAAAAAAAIfw.desc | major | mistranslation | Машинный перевод с серьёзными нарушениями. "Hermitic пчёлы иметь тот же no-entities requirement как Secluded..." - смеши |
| quest.AAAAAAAAAAAAAAAAAAAIgg.desc | major | mistranslation | Сильно повреждена машинным переводом: смешаны английские слова (another, attentive, Apiarist, inflict, Watch) с неполным |
| quest.AAAAAAAAAAAAAAAAAAAIhA.desc | major | mistranslation | Массовая утечка английского текста: 'Another пчела тот требует attentive beekeeper', 'inflict', 'Watch', неправильная гр |
| quest.AAAAAAAAAAAAAAAAAAAIhQ.desc | major | mistranslation | Машинный перевод с утечками: 'пчела не иметь' (неправильная грамматика), 'direct использовать' (неполный перевод), 'part |
| quest.AAAAAAAAAAAAAAAAAAAIhg.desc | major | untranslated | Не переведены 'Obviously' и 'right?', оставлены в виде: 'Obviously, блок Redstone Alloy требуется, right?' Неполный маши |
| quest.AAAAAAAAAAAAAAAAAAAIhw.desc | major | mistranslation | Слово 'princess' оставлено без перевода ('Red Alloy princess будет требовать'), неловкая конструкция, неполный машинный  |
| quest.AAAAAAAAAAAAAAAAAAAIiA.desc | major | mistranslation | 'princess' оставлен без перевода, неловкая грамматическая конструкция, неполный машинный перевод с английскими утечками |
| quest.AAAAAAAAAAAAAAAAAAAIig.desc | major | mistranslation | Развалена грамматика: 'наконец' без заглавной (в начале предложения), 'long, hazardous road' оставлены в английском, 'Gr |
| quest.AAAAAAAAAAAAAAAAAAAIiw.desc | major | untranslated | 'of course' оставлено без перевода ('Energetic Alloy будет требовать блок Energetic Alloy, course'), неловкая конструкци |
| quest.AAAAAAAAAAAAAAAAAAAIjg.desc | major | untranslated | 'go deep' оставлено в английском, 'эти пчёлы' неловко (должно быть 'этих пчёл'), неполный машинный перевод с английскими |
| quest.AAAAAAAAAAAAAAAAAAAIjw.desc | major | mistranslation | Английские слова смешаны с русским: 'для early Chrome, Ruby пчела является great источник' - не переведены 'early', оста |
| quest.AAAAAAAAAAAAAAAAAAAIkQ.desc | major | mistranslation | Развалена грамматика и множество английских утечек: 'пчёлы как ресурс не является тот большой deal', 'поэтому много stuf |
| quest.AAAAAAAAAAAAAAAAAAAIlA.desc | major | mistranslation | Машинный перевод с утечками: 'Lead будет necessary' (не переведено), 'quantities' (английское), 'создание ядерный реакто |
| quest.AAAAAAAAAAAAAAAAAAAIlQ.desc | major | mistranslation | Развалена структура: 'Silver является клавиша metal' (неправильно, 'клавиша' - неправильное слово), 'на HV и up' (англий |
| quest.AAAAAAAAAAAAAAAAAAAIlw.desc | major | mistranslation | Смешанный английский и русский, пропущено начало предложения. Неправильная грамматика и нарушена структура текста (напри |
| quest.AAAAAAAAAAAAAAAAAAAImA.desc | major | mistranslation | Множество невпереводов ('Ah yes'), неверное согласование ('очень полезный пчела' - мужской род к женскому), смешанный ко |
| quest.AAAAAAAAAAAAAAAAAAAImQ.desc | major | mistranslation | Неправильная грамматика ('будет сделать'), невпереводы ('breeze', 'я rhymed'), испорченные слова ('башняs'), смешанный к |
| quest.AAAAAAAAAAAAAAAAAAAImg.desc | major | mistranslation | Невпереводы ('necessary ingredient', 'Better', 'having к deal'), неправильный падеж и предлоги ('к разводить' вместо 'дл |
| quest.AAAAAAAAAAAAAAAAAAAImw.desc | major | mistranslation | Множественные невпереводы ('decent aid', 'well как slow'), неправильный падеж ('к ваш platline'), смешанный английский и |
| quest.AAAAAAAAAAAAAAAAAAAInQ.desc | major | mistranslation | Множество невпереводов ('metal тот represents epitome', 'Never existing в universe до man'), неправильный падеж ('вокруг |
| quest.AAAAAAAAAAAAAAAAAAAIng.desc | major | mistranslation | Невпереводы ('Hatred distilled', 'Keep away'), смешанный код, неполный перевод первого предложения. |
| quest.AAAAAAAAAAAAAAAAAAAIpA.desc | major | mistranslation | Явная машинная пятна: 'из Arcane пчёлы используются к создать' - неправильный порядок слов и грамматика; 'это имеет high |
| quest.AAAAAAAAAAAAAAAAAAAIpg.desc | major | mistranslation | Грубая машинная переводе: 'что иметь те два brothers gotten в now?' - совершенно потеряна структура; 'keystone Magical b |
| quest.AAAAAAAAAAAAAAAAAAAIrA.desc | major | mistranslation | Машинный перевод с потерей грамматики: 'Aqua требует вода кристалл Cluster' - неправильный падеж и порядок; 'это будет п |
| quest.AAAAAAAAAAAAAAAAAAAIrQ.desc | major | mistranslation | Машинная ошибка: 'Firey пчёлы должен быть bred на top лава' - 'лава' без предлога, 'bred' не переведён; неправильное сог |
| quest.AAAAAAAAAAAAAAAAAAAIrg.desc | major | mistranslation | Машинный перевод: 'Earthen пчёлы должен быть bred на top Bricks' - 'bred' не переведён; неправильное согласование 'пчёлы |
| quest.AAAAAAAAAAAAAAAAAAAIrw.desc | major | mistranslation | Машинный перевод: 'Windy пчёлы должен быть bred на top Oak leaves' - неправильное согласование; 'bred' и 'Oak leaves' не |
| quest.AAAAAAAAAAAAAAAAAAAIsA.desc | major | mistranslation | Машинная ошибка: 'для Aer пчёлы к appear' - неправильная конструкция; 'вы должны поместить воздух кристалл Cluster benea |
| quest.AAAAAAAAAAAAAAAAAAAIsQ.desc | major | mistranslation | Машинный перевод: 'Solum пчёлы требовать Earth кристалл Clusters' - неправильное согласование глагола; смешанный язык; ' |
| quest.AAAAAAAAAAAAAAAAAAAIsg.desc | major | mistranslation | Машинный перевод: 'Ignis пчёлы требовать Fire кристалл Clusters beneath пчела housing' - неправильное согласование; смеш |
| quest.AAAAAAAAAAAAAAAAAAAIsw.desc | major | mistranslation | Машинный перевод: 'Watery пчёлы должен быть bred over вода' - неправильное согласование 'пчёлы должен'; 'bred' не переве |
| quest.AAAAAAAAAAAAAAAAAAAItA.desc | major | mistranslation | Машинный перевод: 'Not много к say о этот пчела' - 'Not' левый на английском; неправильная конструкция 'много к say'; см |
| quest.AAAAAAAAAAAAAAAAAAAItQ.desc | major | mistranslation | Машинный перевод: 'Spirit пчела является первый пчела' - неправильная грамматика; 'к дать вы Soul' - неправильная констр |
| quest.AAAAAAAAAAAAAAAAAAAItg.desc | major | mistranslation | Машинный перевод: 'Soul пчела имеет highest шанс создание Soul' - неправильная конструкция 'создание'; смешанный язык 'h |
| quest.AAAAAAAAAAAAAAAAAAAItw.desc | major | mistranslation | Грубая машинная ошибка: 'require' переведено 'требовать' (инфинитив вместо правильного спряжения), 'пчёлы требовать' неп |
| quest.AAAAAAAAAAAAAAAAAAAIuA.desc | major | mistranslation | Массовая оставлена английского текста (Ordered Crystal Clusters, Order Infused пыль), неправильная грамматика ('пчёлы тр |
| quest.AAAAAAAAAAAAAAAAAAAIuA.name | major | mistranslation | "Праекантатио" - явная чушь, машинная ошибка. Никакого отношения к 'Ordered'. Требуется настоящий перевод. |
| quest.AAAAAAAAAAAAAAAAAAAIuQ.desc | major | mistranslation | Много английского не переведено, разломанная грамматика ('vis пчёлы lead', 'они требовать'), неправильный порядок слов,  |
| quest.AAAAAAAAAAAAAAAAAAAIug.desc | major | mistranslation | Много английского текста оставлено непереведённым (bred within, node), неправильная грамматика ('должен быть bred' - неп |
| quest.AAAAAAAAAAAAAAAAAAAIvg.desc | major | mistranslation | Много английского оставлено непереведённым (easy, enormous quantities, block, разводить), неправильная грамматика ('this |
| quest.AAAAAAAAAAAAAAAAAAAIvw.desc | major | mistranslation | Много английского текста не переведено (Skulking, core, mob, проверить out rest рецепты, too много), неправильная грамма |
| quest.AAAAAAAAAAAAAAAAAAAIwA.desc | major | mistranslation | Много английского не переведено (Watch out, trait, полезный эффекты - неправильная грамматика), смешание языков ('Watch  |
| quest.AAAAAAAAAAAAAAAAAAAIwQ.desc | major | mistranslation | Много английского не переведено (giving, shard propolis, имеет шанс), неправильная грамматика ('пчела имеет', 'это будет |
| quest.AAAAAAAAAAAAAAAAAAAIwg.desc | major | mistranslation | Много английского не переведено (Tired все effort, trouble free, creating все), неправильная грамматика (сложная структу |
| quest.AAAAAAAAAAAAAAAAAAAIww.desc | major | mistranslation | Много английского не переведено (ethot один берёт, You'll придётся найти, causing урон), неправильная грамматика, наруше |
| quest.AAAAAAAAAAAAAAAAAAAIxA.desc | major | mistranslation | Много английского не переведено (purchased, found, where вы можете), смешанные языки, неправильная грамматика ('можно pu |
| quest.AAAAAAAAAAAAAAAAAAAIxg.desc | major | mistranslation | Много английского не переведено (пыли нужный, recreate, используя магия), неправильная грамматика ('пчела требуется чтоб |
| quest.AAAAAAAAAAAAAAAAAAAIxw.desc | major | mistranslation | Много английского не переведено (let вы генерировать, skulls, Незер звезда пыль - неправильный перевод), смешанные языки |
| quest.AAAAAAAAAAAAAAAAAAAIyQ.desc | major | mistranslation | Много английского не переведено (sheer disdain показать, awe inspiring, Don't walk вокруг), смешанные языки, нарушена гр |
| quest.AAAAAAAAAAAAAAAAAAAIyg.desc | major | mistranslation | Много английского не переведено (feel waves, radiating out, Don't даже think, получение закрыть), смешанные языки, наруш |
| quest.AAAAAAAAAAAAAAAAAAAIyw.desc | major | mistranslation | Много английского не переведено (может быть thinking к yourself, sure является easy, destructive lightning strikes), неп |
| quest.AAAAAAAAAAAAAAAAAAAIzA.desc | major | mistranslation | Много английского не переведено (fun пчела, useful products, fun эффект, constant fireworks), много грамматических ошибо |
| quest.AAAAAAAAAAAAAAAAAAAIzg.desc | major | mistranslation | Машинный перевод с английскими словами внутри (deadly, little, princess, perfect). Грамматически разломанный текст (буде |
| quest.AAAAAAAAAAAAAAAAAAAIzw.desc | major | mistranslation | Машинный перевод с множеством оставленных английских слов (frame, let, longer, territory, help, tree). Грамматика разлом |
| quest.AAAAAAAAAAAAAAAAAAAIzw.name | major | mistranslation | Незавершённый/поломанный перевод. Keep Calm остался на английском и смешан с нарушенной русской грамматикой (пчела на вм |
| quest.AAAAAAAAAAAAAAAAAAAJ-w.name | major | mistranslation | Неправильный перевод bedrock как бедроком (тазовая кость). Правильно: подземные жидкости, жидкости под землёй, или жидко |
| quest.AAAAAAAAAAAAAAAAAAAJ1g.desc | major | mistranslation | Неполный перевод. Оригинальный текст содержит подробные инструкции, но русский перевод обрывается после первого предложе |
| quest.AAAAAAAAAAAAAAAAAAAJ4g.desc | major | mistranslation | Точка с запятой перед 'капсулы' нарушает грамматику ('вёдер.' вместо 'вёдер.'); неточный перевод 'капсулы вместо вёдер'  |
| quest.AAAAAAAAAAAAAAAAAAAJ5g.desc | major | mistranslation | Ошибка в переводе формулы: 'вместо умножается на 4^(число апгрейдов)' - сбита структура, нужно 'умножается на 4^(число у |
| quest.AAAAAAAAAAAAAAAAAAAJ5w.name | major | mistranslation | Полностью неправильный перевод названия квеста. Оригинал использует аллитерацию 'Singular Singularities Signify Somethin |
| quest.AAAAAAAAAAAAAAAAAAAJ7A.name | major | mistranslation | Переведено содержание описания вместо названия; должно быть что-то вроде 'Торговля Жидкостями' или 'Торговля Жидкостью' |
| quest.AAAAAAAAAAAAAAAAAAAJ8w.desc | major | mistranslation | 'одежда с бонусами на скидку вис' неправильно переводит 'vis discount gear' — должно быть 'снаряжение' или 'предметы', а |
| quest.AAAAAAAAAAAAAAAAAAAJ9A.desc | major | mistranslation | 'одежда с бонусами на скидку вис' неправильно переводит 'vis discount gear'; также множество неточностей и неловких фраз |
| quest.AAAAAAAAAAAAAAAAAAAJAA.name | major | formatting | Код цвета изменён с §b (синий) на §9 (тёмно-синий), что нарушает форматирование |
| quest.AAAAAAAAAAAAAAAAAAAJAQ.name | major | formatting | Код цвета изменён с §b на §9, нарушены форматирование |
| quest.AAAAAAAAAAAAAAAAAAAJAg.name | major | formatting | Код цвета изменён с §b на §9 |
| quest.AAAAAAAAAAAAAAAAAAAJAw.name | major | formatting | Код цвета изменён с §b на §9 |
| quest.AAAAAAAAAAAAAAAAAAAJBA.name | major | formatting | Код цвета изменён с §b на §9 |
| quest.AAAAAAAAAAAAAAAAAAAJBQ.name | major | formatting | Код цвета изменён с §b на §9 |
| quest.AAAAAAAAAAAAAAAAAAAJCA.desc | major | mistranslation | Перевод неполный, опущена фраза 'но мы добираемся к концу', искажен смысл текста |
| quest.AAAAAAAAAAAAAAAAAAAJCQ.desc | major | mistranslation | 'остаток металлического иридия' некорректно - должно быть про остаток из осадка, не про металлический иридий. Перевод за |
| quest.AAAAAAAAAAAAAAAAAAAJEA.desc | major | mistranslation | Указана высота 56 блоков вместо 61 блока - ошибка в переводе числовых данных |
| quest.AAAAAAAAAAAAAAAAAAAJHg.desc | major | mistranslation | Машинный перевод с английскими словами, смешанными с русским текстом. Грамматика сломана, структура предложения нарушена |
| quest.AAAAAAAAAAAAAAAAAAAJJA.desc | major | mistranslation | Полностью сломан машинным переводом: английские слова смешаны с русским, неправильное использование 'является', граммати |
| quest.AAAAAAAAAAAAAAAAAAAJJg.desc | major | mistranslation | Машинный перевод с английскими словами в русском тексте. Нарушена структура, 'является' используется неправильно. |
| quest.AAAAAAAAAAAAAAAAAAAJJw.desc | major | mistranslation | Машинный перевод: английские слова не переведены, 'является' неправильно использован, грамматика разрушена. |
| quest.AAAAAAAAAAAAAAAAAAAJKA.name | major | untranslated | Большая часть названия оставлена на английском: 'Seer Stone' и 'Summon' не переведены. |
| quest.AAAAAAAAAAAAAAAAAAAJLQ.desc | major | mistranslation | Полностью разрушен машинным переводом: английский и русский смешаны в хаотичном порядке, неправильные формы слов. |
| quest.AAAAAAAAAAAAAAAAAAAJLw.desc | major | mistranslation | Машинный перевод: 'к создать' вместо 'чтобы создать', множество английских слов не переведено, грамматика разрушена. |
| quest.AAAAAAAAAAAAAAAAAAAJLw.name | major | mixed_language | Смешана английская и русская речь в неправильном порядке: 'Essence алтарь Dragon Infused' вместо полностью русского пере |
| quest.AAAAAAAAAAAAAAAAAAAJMA.name | major | mixed_language | Смешана английская и русская речь: 'Essence алтарь' должно быть полностью на русском или полностью на английском |
| quest.AAAAAAAAAAAAAAAAAAAJMw.desc | major | mistranslation | Полностью машинный перевод с англицизмами; основная часть текста оставлена на английском языке. Текст нечитаем на русско |
| quest.AAAAAAAAAAAAAAAAAAAJNA.desc | major | mistranslation | Машинный перевод с множеством английских слов в русском тексте; грамматически неправильно и нечитаемо |
| quest.AAAAAAAAAAAAAAAAAAAJNQ.desc | major | mistranslation | Машинный перевод; текст содержит множество английских слов и неправильной грамматики, нечитаем |
| quest.AAAAAAAAAAAAAAAAAAAJNw.desc | major | mistranslation | Крайне плохой машинный перевод с множеством английских слов; текст практически нечитаем на русском |
| quest.AAAAAAAAAAAAAAAAAAAJOA.desc | major | mistranslation | Машинный перевод с множеством английских слов и неправильной грамматикой; нечитаемо |
| quest.AAAAAAAAAAAAAAAAAAAJOg.desc | major | mistranslation | Смешанный машинный перевод с английскими словами: 'используется solely к создать higher уровень' неграмотен |
| quest.AAAAAAAAAAAAAAAAAAAJPA.desc | major | mistranslation | Крайне плохой машинный перевод с множеством англицизмов и неправильной грамматики; абсолютно нечитаемо |
| quest.AAAAAAAAAAAAAAAAAAAJPQ.desc | major | mistranslation | Машинный перевод с англицизмами и неправильной грамматикой; нечитаемо |
| quest.AAAAAAAAAAAAAAAAAAAJPg.desc | major | mistranslation | Машинный перевод с англицизмами и грамматическими ошибками; нечитаемо |
| quest.AAAAAAAAAAAAAAAAAAAJQA.desc | major | mistranslation | Машинный перевод с англицизмами и неправильной грамматикой; нечитаемо |
| quest.AAAAAAAAAAAAAAAAAAAJQg.desc | major | mistranslation | Машинный перевод с англицизмами; структура нарушена, нечитаемо |
| quest.AAAAAAAAAAAAAAAAAAAJQw.desc | major | mistranslation | Машинный перевод с множеством англицизмов и неправильной грамматикой; нечитаемо |
| quest.AAAAAAAAAAAAAAAAAAAJRA.desc | major | mistranslation | Машинный перевод с аппаратными сбоями: смешанный английский и русский, неправильная грамматика, невозможно понять смысл |
| quest.AAAAAAAAAAAAAAAAAAAJRA.name | major | untranslated | Частично переведено: 'Living материя' - смешана английская и русская части, нужна либо полная локализация, либо полность |
| quest.AAAAAAAAAAAAAAAAAAAJRQ.desc | major | mistranslation | Машинный перевод: нарушена грамматика, смешаны языки, нарушена структура предложений |
| quest.AAAAAAAAAAAAAAAAAAAJRg.desc | major | mistranslation | Машинный перевод: нарушена грамматика, смешаны английский и русский языки, невозможно понять содержание |
| quest.AAAAAAAAAAAAAAAAAAAJSQ.desc | major | mistranslation | Машинный перевод: нарушена грамматика, смешаны языки, неправильная структура предложений |
| quest.AAAAAAAAAAAAAAAAAAAJSg.desc | major | mistranslation | Машинный перевод с ошибками: смешаны языки, нарушена грамматика, неправильное использование предлогов |
| quest.AAAAAAAAAAAAAAAAAAAJTg.desc | major | mistranslation | Машинный перевод: нарушена грамматика, смешаны языки, использован интернет-сленг (ПКМ вместо 'щелчок правой кнопкой мыши |
| quest.AAAAAAAAAAAAAAAAAAAJUA.desc | major | mistranslation | Машинный перевод: нарушена грамматика, смешаны языки, неправильное использование предлогов |
| quest.AAAAAAAAAAAAAAAAAAAJUQ.desc | major | mistranslation | Машинный перевод: нарушена грамматика, смешаны языки, неправильная структура предложений |
| quest.AAAAAAAAAAAAAAAAAAAJZQ.name | major | terminology | «Медитативное занятие» теряет смысл фразы-ссылки на Karate Kid из оригинала «Wax On, Wax Off» - название должно отражать |
| quest.AAAAAAAAAAAAAAAAAAAJaA.desc | major | mistranslation | "контроллера ящиков" непоследовательно переведён в разных местах; 'Forestry' не переведён (правильно), но "Мультифермы F |
| quest.AAAAAAAAAAAAAAAAAAAJaQ.desc | major | mistranslation | "измельчённую редкоземельную (I) руду" - неправильно, должно быть 'Crushed Rare Earth (I)' - это не руда, а переработанн |
| quest.AAAAAAAAAAAAAAAAAAAJbQ.desc | major | mistranslation | Текст содержит смешанный английский и русский язык с множественными грамматическими ошибками. Машинный перевод, не отред |
| quest.AAAAAAAAAAAAAAAAAAAJdA.name | major | mistranslation | Начинается со строчной буквы, английские слова 'Hearts' и 'Valentines' оставлены без перевода. Garbled machine translati |
| quest.AAAAAAAAAAAAAAAAAAAJdQ.desc | major | mistranslation | Сильно размешанный machine translation: неправильный предлог 'к', untranslated English words (arrange, cardinal, directi |
| quest.AAAAAAAAAAAAAAAAAAAJdQ.name | major | fluency | Полностью garbled: неправильный глагол 'являются', untranslated слова 'Grassping', 'Telling'. Бессмысленный результат. |
| quest.AAAAAAAAAAAAAAAAAAAJeQ.name | major | untranslated | Четыре английских слова оставлены untranslated: 'Greenhouses на Mountains, Hell на Earth'. Заголовок должен быть полност |
| quest.AAAAAAAAAAAAAAAAAAAJlA.desc | major | mistranslation | Сильно размешанный machine translation: 'работает тот же как обычный один', untranslated слова (works, cause, bleed), не |
| quest.AAAAAAAAAAAAAAAAAAAJlQ.desc | major | mistranslation | Garbled: строчная начальная буква, untranslated слова (stone, rituals, such), неправильная грамматика 'позволяет вы к со |
| quest.AAAAAAAAAAAAAAAAAAAJlg.desc | major | mistranslation | Сильный машинный перевод с смешанием английского и русского. Множество синтаксических ошибок и неправильных структур: 'W |
| quest.AAAAAAAAAAAAAAAAAAAJmQ.desc | major | mistranslation | Сильный машинный перевод с нарушением порядка слов и смешением языков: 'вы нужно этот', 'больше сложный rituals', 'к исп |
| quest.AAAAAAAAAAAAAAAAAAAJmg.desc | major | mistranslation | Машинный перевод с нарушениями: 'Don't хотите к использовать', 'все тот space', 'к снизить их'. Нужен корректный русский |
| quest.AAAAAAAAAAAAAAAAAAAJmw.desc | major | mistranslation | Машинный перевод с смешением языков и ошибками: 'They're seriously questionable', 'этот time', 'not try к получить', 'кр |
| quest.AAAAAAAAAAAAAAAAAAAJrQ.desc | major | mistranslation | "тире" вместо "уровне" (ошибка слова); неформальное "тебе решать" неуместно для документации модпака; "дешевле" некоррек |
| quest.AAAAAAAAAAAAAAAAAAAJsg.desc | major | mistranslation | "млн" вместо "МЛ" (единицы объема жидкости); "Есть также 1К ячейки, которые могут хранить несколько типов" не соответств |
| quest.AAAAAAAAAAAAAAAAAAAJsw.desc | major | mistranslation | "млн" вместо "МЛ" (единицы объема) |
| quest.AAAAAAAAAAAAAAAAAAAJtA.desc | major | mistranslation | "млн" вместо "МЛ" (единицы объема) |
| quest.AAAAAAAAAAAAAAAAAAAJtQ.desc | major | mistranslation | "млн" вместо "МЛ" (единицы объема) |
| quest.AAAAAAAAAAAAAAAAAAAJtw.desc | major | mistranslation | "Для создания ячеек" (для создания) не соответствует "You need to use this" (нужно использовать); смысл слова меняется |
| quest.AAAAAAAAAAAAAAAAAAAJvA.desc | major | mistranslation | "млн" вместо "МЛ" (единицы объема) |
| quest.AAAAAAAAAAAAAAAAAAAJvQ.desc | major | mistranslation | "Гигалитров" неправильное сокращение/написание; должно быть "Гл" или "гигалитров" |
| quest.AAAAAAAAAAAAAAAAAAAJvg.desc | major | mistranslation | "Гигалитров" неправильное сокращение/написание; должно быть "Гл" или "гигалитров" |
| quest.AAAAAAAAAAAAAAAAAAAJvw.desc | major | mistranslation | Неправильное имя вкладки Таумономикона "Энергетика" (должно быть другое имя); дополнительная информация о исследованиях  |
| quest.AAAAAAAAAAAAAAAAAAAK0A.desc | major | mistranslation | Машинный перевод с ошибками грамматики и структуры; неправильное использование падежей и порядка слов; должно быть «Заче |
| quest.AAAAAAAAAAAAAAAAAAAK0A.name | major | mistranslation | Машинный перевод; смешивание русского и английского текста; неполный перевод названия; должно быть полностью переведено  |
| quest.AAAAAAAAAAAAAAAAAAAK0Q.desc | major | mistranslation | Неправильное понимание механики: '2 очка можно получить, если растение видит небо' искажает исходный смысл 'no opaque bl |
| quest.AAAAAAAAAAAAAAAAAAAK1Q.desc | major | mistranslation | Явный случай машинного перевода, не отредактированный. Текст содержит смешанную неправильную грамматику на англо-русском |
| quest.AAAAAAAAAAAAAAAAAAAKAg.name | major | formatting | Неправильный цветовой код: §a (зелёный) заменён на §8 (тёмно-серый). Также 'Глубокая переработка' - неточный перевод 'Ad |
| quest.AAAAAAAAAAAAAAAAAAAKBQ.name | major | formatting | Код цвета изменён с §9§l на §5§l без причины |
| quest.AAAAAAAAAAAAAAAAAAAKBg.name | major | formatting | Код цвета изменён с §9§l на §5§l без причины |
| quest.AAAAAAAAAAAAAAAAAAAKBw.name | major | formatting | Код цвета изменён с §9§l на §5§l без причины |
| quest.AAAAAAAAAAAAAAAAAAAKCA.name | major | formatting | Добавлены коды форматирования §5§l§n которых нет в оригинале |
| quest.AAAAAAAAAAAAAAAAAAAKDA.name | major | formatting | Добавлены коды форматирования §6§l§n которых нет в оригинале |
| quest.AAAAAAAAAAAAAAAAAAAKDQ.name | major | formatting | Добавлены коды форматирования §6§l§n которых нет в оригинале |
| quest.AAAAAAAAAAAAAAAAAAAKDg.name | major | formatting | Добавлены коды форматирования §6§l§n которых нет в оригинале |
| quest.AAAAAAAAAAAAAAAAAAAKDw.name | major | formatting | Добавлены коды форматирования §6§l§n которых нет в оригинале |
| quest.AAAAAAAAAAAAAAAAAAAKEA.name | major | formatting | Добавлены коды форматирования §6§l§n которых нет в оригинале |
| quest.AAAAAAAAAAAAAAAAAAAKEQ.name | major | formatting | Добавлены коды форматирования §5§l§n которых нет в оригинале |
| quest.AAAAAAAAAAAAAAAAAAAKEg.name | major | formatting | Добавлены коды форматирования §5§l§n которых нет в оригинале |
| quest.AAAAAAAAAAAAAAAAAAAKEw.name | major | formatting | Добавлены коды форматирования §5§l§n которых нет в оригинале |
| quest.AAAAAAAAAAAAAAAAAAAKFA.name | major | formatting | Добавлены коды форматирования §5§l§n которых нет в оригинале |
| quest.AAAAAAAAAAAAAAAAAAAKFQ.name | major | formatting | Добавлены коды форматирования §5§l§n которых нет в оригинале |
| quest.AAAAAAAAAAAAAAAAAAAKFg.desc | major | mistranslation | Машинный перевод с английским текстом внутри: 'infinity going forward', 'быть prepared', 'emotional trauma' не переведен |
| quest.AAAAAAAAAAAAAAAAAAAKFw.name | major | untranslated | Слова 'Galaxy' и 'Bottle' оставлены на английском, добавлены коды форматирования |
| quest.AAAAAAAAAAAAAAAAAAAKGA.desc | major | mistranslation | Тяжёлый машинный перевод с английским языком: 'Here это', 'к процесс это', 'к сделать', неправильная грамматика |
| quest.AAAAAAAAAAAAAAAAAAAKGQ.desc | major | mistranslation | Машинный перевод с английским: 'Provides absurd quantity vis storage', 'это также fills как soon' - смешанный язык и неп |
| quest.AAAAAAAAAAAAAAAAAAAKHA.name | major | mistranslation | Смесь английского и русского: 'Well этот посмотреть... Shiny?' - неправильная грамматика, пропущены слова. Должно быть п |
| quest.AAAAAAAAAAAAAAAAAAAKHg.desc | major | mistranslation | Явная машинная переводная ошибка: 'вы know как этот работает. Prepare для everything к стоимость большой объём infinity. |
| quest.AAAAAAAAAAAAAAAAAAAKHg.name | major | mistranslation | Неправильный перевод названия: 'вы Know Drill' - смесь языков. Правильнее: 'Ты знаешь как это работает' или похожее полн |
| quest.AAAAAAAAAAAAAAAAAAAKIQ.desc | major | mistranslation | Грубая машинная ошибка: 'Congratulations, вы beaten самый pack! Here мы иметь несколько absolutely outrageous финальный  |
| quest.AAAAAAAAAAAAAAAAAAAKMg.desc | major | mistranslation | Тяжёлый случай машинного перевода - английский текст перемешан с разбитым русским ('Speaking ZPM, сделал вы know name яв |
| quest.AAAAAAAAAAAAAAAAAAAKNA.desc | major | mistranslation | Машинный перевод - английский текст перемешан с русским в начале и в теге [note] |
| quest.AAAAAAAAAAAAAAAAAAAKNA.name | major | mistranslation | Машинный перевод - английские слова не переведены: 'вы Can't получить Enough этот Pt 2 в ZPM' |
| quest.AAAAAAAAAAAAAAAAAAAKNQ.desc | major | mistranslation | Машинный перевод - английский текст перемешан с русским ('пока called Ultimate Voltage, этот имеет become far...') |
| quest.AAAAAAAAAAAAAAAAAAAKNg.desc | major | mistranslation | Машинный перевод - английский текст не переведён и перемешан с русским ('являются вы okay? Playing этот много...') |
| quest.AAAAAAAAAAAAAAAAAAAKNg.name | major | mistranslation | Машинный перевод - английские слова оставлены без перевода в названии |
| quest.AAAAAAAAAAAAAAAAAAAKNw.name | major | mistranslation | Машинный перевод - английские слова оставлены без перевода в названии |
| quest.AAAAAAAAAAAAAAAAAAAKOQ.name | major | untranslated | Английский текст названия не переведён - оставлен как 'Harder, Better, Faster, Stronger...' с добавлением русского 'в UH |
| quest.AAAAAAAAAAAAAAAAAAAKOg.desc | major | mistranslation | Машинный перевод - английский текст перемешан с русским ('Remember к взять break once hour') |
| quest.AAAAAAAAAAAAAAAAAAAKOg.name | major | untranslated | Английский текст названия не переведён - оставлен как 'Harder, Better, Faster, Stronger...' |
| quest.AAAAAAAAAAAAAAAAAAAKPg.desc | major | mistranslation | Машинный перевод - английский текст не переведён и перемешан с русским ('почему являются они circles anyway?') |
| quest.AAAAAAAAAAAAAAAAAAAKQQ.desc | major | mistranslation | Машинный перевод - английский текст оставлен без перевода и перемешан с русским ('Like previous тир, вы нужно same-tier  |
| quest.AAAAAAAAAAAAAAAAAAAKQg.desc | major | mistranslation | машинный перевод: смешанная английская и русская речь (haven't, progress, yet, You'll), сломанная грамматика (иметь вы с |
| quest.AAAAAAAAAAAAAAAAAAAKRA.desc | major | mistranslation | неправильный падеж (этот вместо это), незаконченный перевод (further осталось на английском), ошибки в грамматике |
| quest.AAAAAAAAAAAAAAAAAAAKRg.desc | major | mistranslation | машинный перевод: неправильная грамматика (эти boules, больше efficient), незаконченный перевод (wafers, boules), искажё |
| quest.AAAAAAAAAAAAAAAAAAAKRw.desc | major | untranslated | множество английских слов остались без перевода (Piko, Solars, transformers, cut wafers), неправильно переведена аббреви |
| quest.AAAAAAAAAAAAAAAAAAAKSA.desc | major | mistranslation | неправильный падеж (вы нужно вместо вам нужны), незаконченный перевод (Solars, transformers, cut) |
| quest.AAAAAAAAAAAAAAAAAAAKSQ.desc | major | mistranslation | неправильный падеж (вы нужно), незаконченный перевод (cut wafers), неловкая фраза (к на самом деле) |
| quest.AAAAAAAAAAAAAAAAAAAKSw.desc | major | mistranslation | сломанная грамматика (к сделать вместо Чтобы сделать, вы нужно вместо вам нужно), незаконченный перевод (either) |
| quest.AAAAAAAAAAAAAAAAAAAKTA.desc | major | mistranslation | неправильная грамматика (к сделать, вы нужно вместо вам нужно) |
| quest.AAAAAAAAAAAAAAAAAAAKTQ.desc | major | mistranslation | незаконченный перевод (с higher voltage), сломанная грамматика, смешанный английский |
| quest.AAAAAAAAAAAAAAAAAAAKWQ.desc | major | mistranslation | машинный перевод: неправильная грамматика (превратить вместо превратите, let's делать), незаконченный перевод (stemcells |
| quest.AAAAAAAAAAAAAAAAAAAKWw.name | major | untranslated | Английские слова 'Not' и 'Cheese' оставлены нетранслированными; грамматическая ошибка 'как вы сделать' (должно быть 'как |
| quest.AAAAAAAAAAAAAAAAAAAKXA.desc | major | mixed_language | Обширная машинная трансляция с англ. словами (Another, Wetware, Assembly); разбросанный латинский и кириллица; грамматич |
| quest.AAAAAAAAAAAAAAAAAAAKXw.desc | major | mixed_language | Массовый code-switching: англ. 'Wetware', 'TecTech', 'Quantum Computer', 'continuing', 'go back', 'skipped' нетранслиров |
| quest.AAAAAAAAAAAAAAAAAAAKYA.desc | major | mixed_language | Нетранслированные англ. слова: 'Wetware', 'Mainframe', 'Assembly', 'there's'; ошибка согласования 'финальный' (должно бы |
| quest.AAAAAAAAAAAAAAAAAAAKYg.desc | major | mixed_language | Грамматическая ошибка 'первый вы нужно' (должно быть 'сначала вы должны'); нетранслированные 'T6 rocket', 'T4'; неловкая |
| quest.AAAAAAAAAAAAAAAAAAAKYw.desc | major | mixed_language | Массовый code-switching: 'Now let's', 'up', 'Raw', 'just', 'Chemical' нетранслированы; ошибочная конструкция 'к сделать' |
| quest.AAAAAAAAAAAAAAAAAAAKYw.name | major | mixed_language | Code-switching с англ. 'Telling', 'Not', 'Mold'; строчное 'я' вместо заглавного; нарушен порядок слов |
| quest.AAAAAAAAAAAAAAAAAAAKaQ.desc | major | mixed_language | 'first', 'game', 'truly', 'well done' не переведены; нарушена структура и смысл предложений |
| quest.AAAAAAAAAAAAAAAAAAAKbA.name | major | mixed_language | Английский 'Something' и 'Nothing' оставлены без перевода, смешаны с русским. Должно быть полностью переведено на русски |
| quest.AAAAAAAAAAAAAAAAAAAKbg.desc | major | mistranslation | Текст сильно машинно-переведен: смешаны английские слова (haven't, go, check out, working) с неполным русским переводом. |
| quest.AAAAAAAAAAAAAAAAAAAKbg.name | major | mixed_language | Слово 'Doctor' оставлено без перевода. Должно быть 'Какой доктор? ДОКТОР' или аналогично. |
| quest.AAAAAAAAAAAAAAAAAAAKcQ.name | major | mixed_language | Английское 'Neutrons' и 'Space' оставлены без перевода. Должно быть 'Нейтроны из космоса'. |
| quest.AAAAAAAAAAAAAAAAAAAKcg.name | major | mixed_language | Английское 'Compressing' не переведено, русское 'звезда' в неправильном падеже. Должно быть 'Сжатие ядра звезды'. |
| quest.AAAAAAAAAAAAAAAAAAAKcw.name | major | mixed_language | Английское 'Infinite' оставлено без перевода, неправильная капитализация русского. Должно быть 'Один слиток, бесконечная |
| quest.AAAAAAAAAAAAAAAAAAAKiA.name | major | formatting | Исходный текст не содержит цветовых кодов (§4§l§n), они были ошибочно добавлены при переводе. Требуется удалить |
| quest.AAAAAAAAAAAAAAAAAAAKiQ.name | major | formatting | Цветовой код изменён с §5 (золотой) на §2 (зелёный), нужно восстановить исходный код |
| quest.AAAAAAAAAAAAAAAAAAAKig.name | major | formatting | Цветовой код изменён с §b (голубой) на §9 (синий), нужно восстановить исходный код |
| quest.AAAAAAAAAAAAAAAAAAAKiw.desc | major | mistranslation | Множество ошибок перевода: 'коэффициент избытка вольтажа' - очень неловкий перевод 'overvolt', должно быть 'перенапряжен |
| quest.AAAAAAAAAAAAAAAAAAAKlw.desc | major | mistranslation | Полностью машинный перевод с английским текстом. Примеры: 'let's say вы сделано', 'kind culture', 'per Vat', 'they're co |
| quest.AAAAAAAAAAAAAAAAAAAKlw.name | major | untranslated | Заголовок остался на английском: 'Copying Cultures' - должно быть переведено на русский |
| quest.AAAAAAAAAAAAAAAAAAAKmA.desc | major | mistranslation | Полностью машинный перевод смешанный с английским: 'к copy cultures', 'вам понадобится к сделать', 'много эти иметь', 'в |
| quest.AAAAAAAAAAAAAAAAAAAKmA.name | major | untranslated | Заголовок остался на английском: 'DNA Samples для Copying Cultures' - 'Copying Cultures' должно быть переведено |
| quest.AAAAAAAAAAAAAAAAAAAKmQ.desc | major | mistranslation | Машинный перевод с остатками английского: 'после получение ваш sample' (неправильная грамматика), 'вы нужно encode' (оши |
| quest.AAAAAAAAAAAAAAAAAAAKmQ.name | major | untranslated | Заголовок остался на английском: 'Data Orbs для Copying Cultures' - 'Copying Cultures' должно быть переведено |
| quest.AAAAAAAAAAAAAAAAAAAKmg.desc | major | mistranslation | Сильно машинный перевод. Перемешана русская и английская речь, множество неправильных конструкций (к copy culture, chang |
| quest.AAAAAAAAAAAAAAAAAAAKmg.name | major | untranslated | Английское слово 'Copying' оставлено непереведённым в русской фразе. Должно быть либо полностью на русском, либо полност |
| quest.AAAAAAAAAAAAAAAAAAAKng.desc | major | mistranslation | Нарушена грамматика русского языка ('По крайней очень похоже на то?' - неправильная конструкция). Исходный смысл искажён |
| quest.AAAAAAAAAAAAAAAAAAAKnw.desc | major | untranslated | Оставлены непереведёнными английские слова и конструкции: 'Creative компоненты', 'Depending на что это', 'there's также  |
| quest.AAAAAAAAAAAAAAAAAAAKnw.name | major | untranslated | Англоязычная фраза почти полностью оставлена непереведённой: 'для все Artists Out There'. Грамматически также неправильн |
| quest.AAAAAAAAAAAAAAAAAAAKpg.desc | major | untranslated | Оставлены непереведёнными английские слова и фразы: 'now сделать', 'go ahead', 'делать поэтому'. Машинный переводчик исп |
| quest.AAAAAAAAAAAAAAAAAAAKpw.desc | major | untranslated | Оставлены непереведёнными английские слова: 'tie' вместо перевода, 'посмотреть nicer' вместо 'выглядят красивее' или под |
| quest.AAAAAAAAAAAAAAAAAAAKqA.desc | major | untranslated | Оставлены непереведёнными: 'non-endgame/creative', 'There's також Scepter version'. Неполный перевод технических термино |
| quest.AAAAAAAAAAAAAAAAAAAKsA.name | major | mistranslation | "Башка трещит" переводит шутку неправильно. Оригинал о похмелье (hangover), а не о боли в голове. Нужен перевод в контек |
| quest.AAAAAAAAAAAAAAAAAAAKvA.desc | major | fluency | Машинный перевод с артефактами: "для те кто" (грамматически неверно), неперевёденный английский "love Forestry trees" |
| quest.AAAAAAAAAAAAAAAAAAAKvA.name | major | fluency | Машинный перевод: "только лучший" (неверно), "Tree разведение" (смешан английский и русский), нужно "только лучшее: разв |
| quest.AAAAAAAAAAAAAAAAAAAKvQ.desc | major | fluency | Машинный перевод: "для те кто" (грамматически неверно), неперевёденный английский "like flowers или trees" |
| quest.AAAAAAAAAAAAAAAAAAAKvQ.name | major | untranslated | В основном неперевёденный английский: "только Worst: Trees Suck!", нужен полный перевод названия |
| quest.AAAAAAAAAAAAAAAAAAAKxw.desc | major | mistranslation | Первое предложение не соответствует английскому источнику. 'Поэтому...' не отражает смысл 'For when your ABS isn't the r |
| quest.AAAAAAAAAAAAAAAAAAAKyA.desc | major | mistranslation | Машинный перевод с большим количеством неперевёденных английских слов и фрагментов (addition, деhydrator, мультиблок, Fu |
| quest.AAAAAAAAAAAAAAAAAAAKyg.name | major | untranslated | Английское слово 'Not' оставлено без перевода. Неправильная грамматика 'как вы получить в Space'. Должно быть: 'Это не т |
| quest.AAAAAAAAAAAAAAAAAAAKzQ.desc | major | mistranslation | Машинный перевод с неперевёденными английскими словами (bunch, modular, tier, storage, capacity, QT, multi, hatch, fluid |
| quest.AAAAAAAAAAAAAAAAAAAL0A.desc | major | mistranslation | Серьёзное смешение английского и разломанного русского языка - машинный перевод с огромным количеством необработанного а |
| quest.AAAAAAAAAAAAAAAAAAAL0A.name | major | mistranslation | Смешение английского и русского языков - должна быть полная русификация |
| quest.AAAAAAAAAAAAAAAAAAAL3g.desc | major | mistranslation | Смешение английского и русского с необработанным английским текстом, грамматические ошибки ('к построить' неправильно) |
| quest.AAAAAAAAAAAAAAAAAAAL3w.name | major | mistranslation | Неправильный перевод - 'Ядро группы' не соответствует 'Ground Unit', должно быть 'Наземный блок' |
| quest.AAAAAAAAAAAAAAAAAAAL5A.name | major | mistranslation | 'Watery Mud' переведено как 'Мутим воду' (неправильное значение), должно быть 'Грязная вода' или 'Мутная вода' |
| quest.AAAAAAAAAAAAAAAAAAAL6Q.desc | major | mistranslation | Источник говорит 'react your zirconia with some hydrochloric acid', но русский текст говорит 'tetrachloride hafnium' - э |
| quest.AAAAAAAAAAAAAAAAAAALCg.desc | major | mistranslation | Полностью машинный перевод с серьёзными ошибками: смешение русского и английского ('previous', 'time', 'chews', 'too'),  |
| quest.AAAAAAAAAAAAAAAAAAALDQ.name | major | mistranslation | Грамматическая ошибка: неправильная форма прилагательного. Должно быть 'Более продвинутые реакторы' или 'Продвинутые реа |
| quest.AAAAAAAAAAAAAAAAAAALDw.desc | major | mistranslation | Грамматическая ошибка: 'Ты также получите' (смешение личных форм). Технические неточности: 'цистерна края' вместо четког |
| quest.AAAAAAAAAAAAAAAAAAALDw.name | major | mistranslation | 'Модули' не передает значение 'Covering Up' - это каламбур о покрытиях (covers). Должно быть 'Прикрытие' или 'Закрывая б |
| quest.AAAAAAAAAAAAAAAAAAALEA.desc | major | mistranslation | Машинный перевод, не соответствует источнику. 'Fluffy and red, I'm so sad' превратилось в бессмысленное 'Пушистое создан |
| quest.AAAAAAAAAAAAAAAAAAALGQ.desc | major | mistranslation | Hollow Hills переведено как Высокогорье - неправильное название локации, должно быть Полые холмы |
| quest.AAAAAAAAAAAAAAAAAAALGg.desc | major | mistranslation | Hollow Hills неправильно переведено как Высокогорье вместо Полые холмы; грамматика в начале неправильная (запятая вместо |
| quest.AAAAAAAAAAAAAAAAAAALGw.desc | major | mistranslation | Hollow Hills неправильно переведено как высокогорье, должно быть Полые холмы |
| quest.AAAAAAAAAAAAAAAAAAALHA.desc | major | mistranslation | slimy projectiles переведено как огненные сгустки - полная ошибка (должно быть слизистые снаряды); Hollow Hills переведе |
| quest.AAAAAAAAAAAAAAAAAAALHQ.desc | major | mistranslation | Hollow Hills переведено как Высокогорье, должно быть Полые холмы; Hedge Mazes переведено странно |
| quest.AAAAAAAAAAAAAAAAAAALHg.desc | major | mistranslation | Hollow Hills переведено как Высокогорье вместо Полые холмы - системная ошибка |
| quest.AAAAAAAAAAAAAAAAAAALHw.desc | major | mistranslation | Hollow Hills переведено как Высокогорье вместо Полые холмы |
| quest.AAAAAAAAAAAAAAAAAAALIQ.name | major | formatting | Цветовой код §2 вместо §5 - повреждено форматирование заголовка |
| quest.AAAAAAAAAAAAAAAAAAALIg.name | major | formatting | Цветовой код §2 вместо §5 - повреждено форматирование заголовка |
| quest.AAAAAAAAAAAAAAAAAAALJw.desc | major | mistranslation | Критически повреждено машинным переводом - английский текст смешан с ломаной русской грамматикой (send essentia, разные  |
| quest.AAAAAAAAAAAAAAAAAAALKQ.desc | major | mistranslation | Источник говорит о 'glass' (стекле), но перевод использует 'зеркало' (зеркало); также 'способно на такие вещи как' - нет |
| quest.AAAAAAAAAAAAAAAAAAALLA.desc | major | mistranslation | Переводчик добавил 'изумрудные трубы', которых нет в источнике; неточный перевод инструкций по использованию труб |
| quest.AAAAAAAAAAAAAAAAAAALQg.desc | major | mistranslation | Перемешанный англо-русский текст, неполные предложения, машинный перевод. Требуется полный переводя с нуля |
| quest.AAAAAAAAAAAAAAAAAAALRQ.desc | major | mistranslation | Огромное количество английского текста оставлено непереведённым, смешанный язык, нарушена грамматика. Требуется полный п |
| quest.AAAAAAAAAAAAAAAAAAALRQ.name | major | mistranslation | Английские слова непереведены (Really, Out), нарушен порядок слов, неграмотный перевод |
| quest.AAAAAAAAAAAAAAAAAAALRw.name | major | mistranslation | Английские слова непереведены (Not, Back), неправильная грамматическая структура |
| quest.AAAAAAAAAAAAAAAAAAALSA.desc | major | mistranslation | Перемешанный текст на англо-русском, английские фразы непереведены (somehow manage, connect, aspect points, become God), |
| quest.AAAAAAAAAAAAAAAAAAALTw.desc | major | mistranslation | Множество ошибок: 'помощника при готовке' неловко; 'Столешницы будут искать шкафы над собой' неправильно (ищут вверх); ' |
| quest.AAAAAAAAAAAAAAAAAAALYg.desc | major | mistranslation | Путаница руда/пыль: 'кобальтиновую пыль' должно быть 'кобальтитовую руду'; также 'кобальтовой руды' позже противоречит п |
| quest.AAAAAAAAAAAAAAAAAAALaQ.desc | major | formatting | Потеря форматирования: '[warn]IЕсли' содержит лишний символ 'I' перед 'Если' (опечатка); пробел вместо закрывающего тега |
| quest.AAAAAAAAAAAAAAAAAAALdA.desc | major | mistranslation | Ошибка перевода: исходный текст означает 'можешь переработать титан и вернуть плавиковую кислоту', а не 'переработать ег |
| quest.AAAAAAAAAAAAAAAAAAALeg.desc | major | fluency | Машинный перевод с утечками: английские слова не переведены ('accelerate', 'connect', 'keep'), сломана грамматика и стру |
| quest.AAAAAAAAAAAAAAAAAAALew.desc | major | fluency | Машинный перевод: английские слова не переведены ('failed', 'meet', 'recycle'), нарушена грамматика и логика |
| quest.AAAAAAAAAAAAAAAAAAALjA.desc | major | mistranslation | Тяжёлое машинное смешивание языков: 'Cheapest один', 'используется для накуада топливо' - полностью разрушена структура  |
| quest.AAAAAAAAAAAAAAAAAAALjA.name | major | mistranslation | Смешивание языков: 'ядерный Based топливо' - должно быть 'Ядерное топливо на основе' |
| quest.AAAAAAAAAAAAAAAAAAALjQ.desc | major | untranslated | Текст не переведен: 'Provides' и 'lasting' оставлены на английском, прерывистая структура |
| quest.AAAAAAAAAAAAAAAAAAALjQ.name | major | mistranslation | Смешивание языков: 'ядерный Based топливо' - неправильная структура |
| quest.AAAAAAAAAAAAAAAAAAALjg.desc | major | untranslated | Текст не переведен: 'Provides' и 'lasting' оставлены на английском |
| quest.AAAAAAAAAAAAAAAAAAALjw.desc | major | mistranslation | Массивное смешивание языков и грамматические ошибки: 'этот insane машина', 'к сделать', 'higher тир', разломанная структ |
| quest.AAAAAAAAAAAAAAAAAAALkQ.desc | major | mistranslation | Смешивание языков: 'lasting' не переведено, 'для плазма энергия' неправильная грамматика, 'Possibly viable alternative'  |
| quest.AAAAAAAAAAAAAAAAAAALkg.desc | major | mistranslation | Смешивание и ошибки: 'lasting' не переведено, 'way' и 'out' на английском, 'получение' неправильная форма, 'вы может' гр |
| quest.AAAAAAAAAAAAAAAAAAALkw.desc | major | mistranslation | Смешивание и грамматика: 'lasting' не переведено, 'Prepare к сделать' разломано, 'много этот' неправильная грамматика, ' |
| quest.AAAAAAAAAAAAAAAAAAALlA.desc | major | mistranslation | Массивное смешивание языков: 'lasting' не переведено, 'Now накуада топлива', 'к получить', 'really хороший' - разломанна |
| quest.AAAAAAAAAAAAAAAAAAALlQ.desc | major | mistranslation | Смешивание языков: 'per liter' не переведено, 'Sourcing', 'radox' на английском, 'может prove' смешано, 'until later' не |
| quest.AAAAAAAAAAAAAAAAAAALow.desc | major | mistranslation | 'Double Aluminium Plates' неправильно переведено как '2хАлюминиевую пластину' (неверное число и форма), правильно: 'Двой |
| quest.AAAAAAAAAAAAAAAAAAALsA.desc | major | mistranslation | Ошибка при переводе 'your old generators' как 'твои паровые турбины'. В источнике говорится о старых генераторах вообще, |
| quest.AAAAAAAAAAAAAAAAAAALsQ.desc | major | other | Повторение слова 'поэтому' в одном предложении (дубль ошибка). Также неправильный перевод в подсказке: 'нефтяного газа с |
| quest.AAAAAAAAAAAAAAAAAAALsg.desc | major | fluency | Запутанный и повторяющийся перевод инструкций. Фраза о 'выбрав запрограммированную схему с нужным номером' повторяется д |
| quest.AAAAAAAAAAAAAAAAAAALyg.desc | major | fluency | Полностью машинный перевод, сломанная грамматика, слова в неправильных падежах, английский текст смешан с русским, текст |
| quest.AAAAAAAAAAAAAAAAAAALzA.name | major | mistranslation | Смешанный английский и русский текст: 'Largest масло Drain' содержит английское слово 'масло' вместо полного русского пе |
| quest.AAAAAAAAAAAAAAAAAAAM1g.desc | major | mistranslation | Наивный/машинный перевод с перемешиванием языков. Текст содержит английские фразы 'not psychedelic drug kicking в', 'cor |
| quest.AAAAAAAAAAAAAAAAAAAM2A.name | major | untranslated | Английский текст 'Focusing Science и Mystery' с частичным переводом. Должно быть полностью переведено на русский, наприм |
| quest.AAAAAAAAAAAAAAAAAAAM2g.desc | major | fluency | Ломаная грамматика: 'Как и для манипуляторов второго тира, для также требуется' - неправильная конструкция. Должно быть: |
| quest.AAAAAAAAAAAAAAAAAAAM2w.desc | major | fluency | Грамматические ошибки: 'для также требуется' (неправильная конструкция) и опечатка 'композитй' вместо 'композит'. |
| quest.AAAAAAAAAAAAAAAAAAAM3A.desc | major | mistranslation | Грубый машинный перевод с английским текстом, оставленным без перевода (Consider pushing, finальный form, через replacin |
| quest.AAAAAAAAAAAAAAAAAAAM3A.name | major | terminology | Неправильный формат: 'тир 4 Shielding' вместо 'Щиты 4-го тира' или подобного. Смешение языков и неправильный регистр. |
| quest.AAAAAAAAAAAAAAAAAAAMBw.name | major | mistranslation | Потеря словесной игры: 'You Can't Be Cerious!' - это каламбур (can't be serious/cerium). Перевод 'Готовый церий' полност |
| quest.AAAAAAAAAAAAAAAAAAAMCQ.desc | major | mistranslation | Неполный перевод: вторая часть 'and some of the rarer rare earths' отсутствует в русском варианте. |
| quest.AAAAAAAAAAAAAAAAAAAMFQ.name | major | mixed_language | Перемешанные языки: 'углерод, Chemically' - английское слово Chemically не переведено. Должно быть 'Углерод химически' и |
| quest.AAAAAAAAAAAAAAAAAAAMFg.name | major | mixed_language | Перемешанные языки: 'Burning углерод' - английское Burning не переведено. Должно быть 'Сжигание углерода'. |
| quest.AAAAAAAAAAAAAAAAAAAMFw.name | major | mixed_language | Перемешанные языки и ошибка грамматики: 'Sourcing ваш дерево' - Sourcing не переведено, неправильный падеж. Должно быть  |
| quest.AAAAAAAAAAAAAAAAAAAMGA.name | major | mixed_language | Перемешанные языки: 'Faster древесный уголь' - английское Faster не переведено. Должно быть 'Быстрый древесный уголь'. |
| quest.AAAAAAAAAAAAAAAAAAAMGQ.name | major | mixed_language | Перемешанные языки и ошибка согласования: 'два большой Ovens' - английское Ovens не переведено, неправильное согласовани |
| quest.AAAAAAAAAAAAAAAAAAAMGg.name | major | mistranslation | Частичный перевод и ошибка: 'Benzene тир' - Benzene не переведено, 'тир' означает 'тир для стрельбы', а не 'tier'. Должн |
| quest.AAAAAAAAAAAAAAAAAAAMHA.name | major | mixed_language | Перемешанные языки: 'два Alcohols' - английское Alcohols не переведено. Должно быть 'Два спирта' или 'Два вида спиртов'. |
| quest.AAAAAAAAAAAAAAAAAAAMHQ.name | major | fluency | Грамматическая ошибка и неполный перевод: 'извлечение масло' - неправильный падеж (должно быть 'масла'). Должно быть 'До |
| quest.AAAAAAAAAAAAAAAAAAAMIw.name | major | mixed_language | Смешанный английский и русский, неправильная капитализация, неполный перевод |
| quest.AAAAAAAAAAAAAAAAAAAMJQ.name | major | mixed_language | Неправильный смешанный перевод: английское слово Sapling оставлено без перевода |
| quest.AAAAAAAAAAAAAAAAAAAMKQ.name | major | mixed_language | Английский притяжательный падеж Toluene's оставлен без перевода |
| quest.AAAAAAAAAAAAAAAAAAAMKg.name | major | mixed_language | Смешанный английский и русский: Further и Distillation не переведены |
| quest.AAAAAAAAAAAAAAAAAAAMKw.name | major | mixed_language | Английские слова Vinegar и Acetone не переведены, использовано неправильное в русском структурирование |
| quest.AAAAAAAAAAAAAAAAAAAMLg.name | major | mixed_language | Английские слова Green и Nitric не переведены, только слово кислота переведено |
| quest.AAAAAAAAAAAAAAAAAAAMMg.name | major | mixed_language | Смешанный перевод: Free, для все (неправильная грамматика), Fertilizer не переведены |
| quest.AAAAAAAAAAAAAAAAAAAMNQ.name | major | mixed_language | Неправильный смешанный перевод: английское слово Skipped оставлено, структура нарушена |
| quest.AAAAAAAAAAAAAAAAAAAMOw.desc | major | fluency | Сильно повреждённый машинный перевод, множество грамматических ошибок, нарушена структура предложений |
| quest.AAAAAAAAAAAAAAAAAAAMOw.name | major | mixed_language | Английские слова Nitric и Sulfuric не переведены |
| quest.AAAAAAAAAAAAAAAAAAAMQA.name | major | mixed_language | Английское слово Super и Boiling не переведены |
| quest.AAAAAAAAAAAAAAAAAAAMQw.name | major | mixed_language | Ошибка согласования рода, английское слово Loose не переведено |
| quest.AAAAAAAAAAAAAAAAAAAMSA.name | major | mistranslation | Оставлен английский 'Too' без перевода, смешано с русским 'много'. Должно быть 'Слишком много Indium?' |
| quest.AAAAAAAAAAAAAAAAAAAMTQ.desc | major | mistranslation | Машинный перевод, фрагментированный текст. Смешаны английские и русские слова в неправильном порядке, нарушена грамматик |
| quest.AAAAAAAAAAAAAAAAAAAMTQ.name | major | mistranslation | Машинный перевод без капитализации, неправильный порядок слов. Должно быть 'Постройте сначала линию сборки' |
| quest.AAAAAAAAAAAAAAAAAAAMUA.name | major | mistranslation | Неполный перевод, английское слово 'Path' не переведено, отсутствует заглавная буква. Должно быть 'Путь к термоядерному  |
| quest.AAAAAAAAAAAAAAAAAAAMUQ.name | major | mistranslation | Неправильный падеж, отсутствует заглавная буква. Должно быть 'Строительство реактора' |
| quest.AAAAAAAAAAAAAAAAAAAMUg.name | major | mistranslation | Неправильное согласование, отсутствует заглавная буква. Должно быть 'Жидкостные ядерные реакторы' |
| quest.AAAAAAAAAAAAAAAAAAAMUw.name | major | mistranslation | Неправильная грамматика, отсутствует заглавная буква. Должно быть 'Торий как топливо для размножения' |
| quest.AAAAAAAAAAAAAAAAAAAMVA.name | major | mistranslation | Неправильное слово 'нагреть' (глагол вместо прилагательного), английское слово 'Infrastructure' не переведено. Должно бы |
| quest.AAAAAAAAAAAAAAAAAAAMVQ.name | major | mistranslation | Неправильная грамматика, отсутствует заглавная буква. Должно быть 'Автоматизация подачи топлива' |
| quest.AAAAAAAAAAAAAAAAAAAMVg.name | major | mistranslation | Смешаны английские и русские слова, неправильная грамматика, отсутствует заглавная буква. Должно быть 'Фокус на генераци |
| quest.AAAAAAAAAAAAAAAAAAAMWA.name | major | mistranslation | Смешаны английские и русские слова, отсутствует заглавная буква. Должно быть 'Первая половина размножения в ЖФТР' |
| quest.AAAAAAAAAAAAAAAAAAAMWg.name | major | mistranslation | Отсутствует заглавная буква. Должно быть 'Термоядерный Европий' |
| quest.AAAAAAAAAAAAAAAAAAAMWw.name | major | mistranslation | Неправильная грамматика, отсутствует заглавная буква. Должно быть 'Сколько энергии из одного реактора?' |
| quest.AAAAAAAAAAAAAAAAAAAMXA.name | major | mistranslation | Отсутствует заглавная буква, неполный перевод. Должно быть 'Опциональный уровень 1 термоядерного синтеза' |
| quest.AAAAAAAAAAAAAAAAAAAMXQ.name | major | mistranslation | Смешаны английские и русские буквы. Должно быть 'Энергия УФ на одну турбину' или аналогично |
| quest.AAAAAAAAAAAAAAAAAAAMXg.name | major | mistranslation | Английское слово 'Powering-up' не переведено, неправильная грамматика. Должно быть 'Питание жидкостных ядерных реакторов |
| quest.AAAAAAAAAAAAAAAAAAAMXw.name | major | mistranslation | Отсутствует заглавная буква, неправильный падеж. Должно быть 'Вакуумные ядерные реакторы' |
| quest.AAAAAAAAAAAAAAAAAAAMYQ.name | major | mistranslation | Отсутствует заглавная буква, неправильная грамматика. Должно быть 'Ураниевые базовые ядерные реакторы' |
| quest.AAAAAAAAAAAAAAAAAAAMYg.name | major | mistranslation | Смешаны английские и русские слова. Должно быть 'Дальнейший потенциал ядерных реакторов IC2' |
| quest.AAAAAAAAAAAAAAAAAAAMYw.name | major | mistranslation | Смешаны английские и русские слова, неправильная грамматика. Должно быть 'Вакуумные ядерные реакторы высокой плотности' |
| quest.AAAAAAAAAAAAAAAAAAAMZQ.name | major | mixed_language | Английское слово 'Excited' не переведено; неправильный порядок слов. Должно быть 'Возбужденные ядерные реакторы на жидко |
| quest.AAAAAAAAAAAAAAAAAAAMZg.name | major | untranslated | Английское 'Summarized' не переведено. Должно быть 'ядерные реакторы - кратко' или 'Обзор ядерных реакторов' |
| quest.AAAAAAAAAAAAAAAAAAAMaA.name | major | fluency | Грамматическая ошибка: 'ядерный топливо' - неправильное согласование. Должно быть 'ядерное топливо обработка' или 'обраб |
| quest.AAAAAAAAAAAAAAAAAAAMag.name | major | mixed_language | Английские слова 'Steps' и 'Reprocessing' не переведены. Должно быть 'первые шаги в переработке' или 'начало переработки |
| quest.AAAAAAAAAAAAAAAAAAAMaw.name | major | mixed_language | Английское 'Half' не переведено. Должно быть 'вторая половина разведения LFTR' |
| quest.AAAAAAAAAAAAAAAAAAAMbg.name | major | mixed_language | Английские слова 'Temperature' и 'Gas-cooled' не переведены. Должно быть 'высокотемпературный газоохлаждаемый реактор' |
| quest.AAAAAAAAAAAAAAAAAAAMbw.name | major | mixed_language | Английские слова 'Exciting' и 'Nuking' не переведены, неправильный порядок. Должно быть 'возбужденные ядерные реакторы н |
| quest.AAAAAAAAAAAAAAAAAAAMdQ.name | major | mixed_language | Английское 'Fusing' не переведено. Должно быть 'Синтез америция и тритана' |
| quest.AAAAAAAAAAAAAAAAAAAMdg.name | major | mixed_language | Английские слова 'Bismuth' и 'Soldering' не переведены. Должно быть 'Плазма висмута для пайки' |
| quest.AAAAAAAAAAAAAAAAAAAMeA.name | major | fluency | 'Бесконечность турбин' - грамматическая ошибка. Должно быть 'Бесконечные турбины' |
| quest.AAAAAAAAAAAAAAAAAAAMeg.name | major | mixed_language | Английские слова 'Smaller' и 'Bigger' не переведены, машинный перевод слово-в-слово. Должно быть 'Меньше значит больше'  |
| quest.AAAAAAAAAAAAAAAAAAAMfw.desc | major | mistranslation | Массивный машинный перевод с множеством необработанных английских слов ('looked', 'Particularly', 'kinds'), нарушенной г |
| quest.AAAAAAAAAAAAAAAAAAAMfw.name | major | fluency | Грамматическая ошибка согласования: 'жидкость ядерные'. Должно быть 'Автоматизация ядерных реакторов на жидком топливе'  |
| quest.AAAAAAAAAAAAAAAAAAAMhg.name | major | untranslated | Английское 'Establishment' не переведено. Должно быть 'Установка синтеза' или 'Создание синтеза' |
| quest.AAAAAAAAAAAAAAAAAAAMiA.name | major | mixed_language | Английские слова 'options' и 'core' не переведены. Должно быть 'Столько вариантов для ядра!' или 'Так много вариантов яд |
| quest.AAAAAAAAAAAAAAAAAAAMkA.desc | major | untranslated | Множество английских слов оставлены нетранслитерированными (now, optical, beyond, Maybe, all). Грамматика разломана и бе |
| quest.AAAAAAAAAAAAAAAAAAAMmQ.desc | major | untranslated | Полностью искажено машинным переводом. Множество английских слов оставлены (flowers, everywhere, limited, specific, walk |
| quest.AAAAAAAAAAAAAAAAAAAMmw.desc | major | untranslated | Жестко искажено машинным переводом. Много английских слов (catalysts, Alchemical, change, related, prismarine, researche |
| quest.AAAAAAAAAAAAAAAAAAAMmw.name | major | untranslated | Только частичный перевод. Полностью нетранслитерированные английские слова 'Glimpse' и 'Watery Future'. |
| quest.AAAAAAAAAAAAAAAAAAAMng.desc | major | untranslated | Искажено машинным переводом. Нетранслитерированные слова (speak, portal, realm, filled). Отсутствует слово 'of'. Граммат |
| quest.AAAAAAAAAAAAAAAAAAAMnw.desc | major | untranslated | Множество английских слов оставлены (pylons, beacon, summon, Guardian). Неправильный гибридный синтаксис с 'shift-ПКМ'.  |
| quest.AAAAAAAAAAAAAAAAAAAMoQ.desc | major | untranslated | Множество нетранслитерированных слов (Go, further, value, sanity). Неправильное использование 'вы' вместо 'ты'. Граммати |
| quest.AAAAAAAAAAAAAAAAAAAMoQ.name | major | untranslated | Нетранслитерированное слово 'Worthy'. Неверные коды цвета (§c вместо ожидаемого). Неправильная грамматика 'вы являются'. |
| quest.AAAAAAAAAAAAAAAAAAAMpg.desc | major | untranslated | Жестко искажено машинным переводом. Много английских слов (industrious, step, giant, beekind, starting, related, Maybe,  |
| quest.AAAAAAAAAAAAAAAAAAAMqQ.desc | major | untranslated | Множество нетранслитерированных английских слов (Gaia, Spirit, killing, guardian, pylons, beacon, summon). Грамматика ра |
| quest.AAAAAAAAAAAAAAAAAAAMsQ.name | major | untranslated | Английский текст 'Wait, PBI wasn't' не переведен, 'plastic' оставлено на английском. Смешанный язык. |
| quest.AAAAAAAAAAAAAAAAAAAMsw.desc | major | mistranslation | Сильно поврежденный машинный перевод с обилием английских слов: 'Thanks к ваш help я иметь managed', 'ultimate энергия и |
| quest.AAAAAAAAAAAAAAAAAAAMtQ.name | major | untranslated | 'Moron's Manual', 'Manufacture' и 'Manipulation' оставлены на английском. Неполный перевод названия. |
| quest.AAAAAAAAAAAAAAAAAAAMtw.desc | major | mistranslation | Сильно поврежденный машинный перевод: 'мана является blue', 'There's correlation', 'hydroangea превратить'. Множество ан |
| quest.AAAAAAAAAAAAAAAAAAAMuQ.desc | major | mistranslation | Сильно поврежденный машинный перевод: 'endoflame сжечь combustible', 'efficiently потреблять', 'any burn time beyond это |
| quest.AAAAAAAAAAAAAAAAAAAMuw.desc | major | mistranslation | Сильно поврежденный машинный перевод с множеством английских слов: 'ring magnetization', 'tired having', 'взять это off' |
| quest.AAAAAAAAAAAAAAAAAAAMvA.desc | major | mistranslation | Сильно поврежденный машинный перевод: 'dreadthorne является similar', 'kills adult animals', 'helpful для farming'. Обил |
| quest.AAAAAAAAAAAAAAAAAAAMwA.name | major | mistranslation | 'наполнитель' (filler) неправильный перевод 'canning machine'. Должно быть 'консервная машина' или 'аппарат укупорки'. |
| quest.AAAAAAAAAAAAAAAAAAAMwg.desc | major | mistranslation | Сильно поврежденный машинный перевод: 'иметь вы ever seen', 'я бы love к eat', 'narslimmus имеет'. Обилие английских сло |
| quest.AAAAAAAAAAAAAAAAAAAMxg.desc | major | mistranslation | Сильно поврежденный машинный перевод: 'есть no way', 'beegonia не know', 'gladly eat up'. Множество английских слов, нар |
| quest.AAAAAAAAAAAAAAAAAAAMyA.desc | major | mistranslation | Сильно нарушена машинным переводом: английские слова перемешаны с русским текстом (Well, idea, since, stopped, golems, b |
| quest.AAAAAAAAAAAAAAAAAAAMyA.name | major | untranslated | Оставлены untranslated английские слова 'Ignore' и 'Eyes'. Должно быть 'Игнорируй сияние в их глазах'. |
| quest.AAAAAAAAAAAAAAAAAAAMzQ.name | major | mistranslation | 'Thermosink Radiator' переведено как 'Башня жидкостного охлаждения 2-го тира', что означает 'Liquid Cooling Tower Tier 2 |
| quest.AOBApHluTUurGwTeOzxj4g.desc | major | mistranslation | Машинный перевод: перемешаны английский и русский ('вы thought you'd быть done с термояд'), грамматика нарушена, смысл п |
| quest.AQMaWAiIRo6vNTAxqopS_Q.desc | major | mistranslation | Машинный перевод с перемешиванием языков. Английские слова не переведены (You'll notice, Prismarine Precipitates, recycl |
| quest.Avz75EgSTdG48xI3HPGUMA.name | major | mistranslation | 'Excavation Upgrade' переведено как 'Excavation улучшить' - половина на английском, грамматически неправильно. Должно бы |
| quest.BFpBG-zDQSCr3DieB6Cw5g.name | major | untranslated | Оставлены untranslated английские слова: 'Something', 'From', 'Nothing', 'Part'. Должно быть полностью переведено: 'Что- |
| quest.DPl-UUZfTAa-ezdD_m8Huw.name | major | untranslated | Английское слово 'Conclusion' оставлено без перевода. Должно быть 'Заключение' или другой подходящий перевод |
| quest.DVLahVNUQ-CvjYwmvkUn-Q.desc | major | mistranslation | Критически искажённая машинная переводимость: множество английских слов оставлены без перевода (knew, artificial, core,  |
| quest.FYOm8b1PRTKsyVjFdpBqjg.name | major | untranslated | English слово 'Requestin' не переведено; должно быть что-то типа 'Запрашиваю рецепт' или 'Прошу рецепт' |
| quest.FiNzfQEmSlOHb8fuC-FWBw.desc | major | mistranslation | Явно машинный перевод: 'peak все Incenses' - бессмыслица, 'из §92400§r к §93500§r' - неправильная грамматика. Должно быт |
| quest.GHobGJFEQzK1q96l6oC8wQ.desc | major | mistranslation | Грубая машинная ошибка: 'это имеет' вместо 'этот модуль имеет'; 'supports higher тир' - неправильное смешивание языков;  |
| quest.GR94tIXOQvC2w5SttlezrQ.desc | major | mistranslation | Сломанный перевод: 'мне жидкость' вместо 'резервуар жидкости'; 'напрямую к ваш' - неправильное согласование; 'equivalent |
| quest.GslQBIW9QKaCz7FFpkrv6g.name | major | mistranslation | Неправильный перевод 'мой Beloved' - должно быть 'мой любимый'; цветовой код изменён с §b на §9 |
| quest.H_S9zi1_SUKG7JkEYgJIiA.desc | major | mistranslation | Грубая машинная ошибка: 'можно используется к сделать' - грамматически ломано; 'lapotron orbs' - не переведено; 'raw ком |
| quest.Hn_igsosSbKsnATeYgvPgw.name | major | mistranslation | Неполный перевод с ошибками: 'I'll teach вы' - смешивание языков; 'к Praise' - неправильное согласование; 'Praise солнце |
| quest.IGVryoMbRu28q08v4uwSuw.desc | major | mistranslation | Массивные ошибки машинного перевода: 'как вы noticed' - англицизм; 'extremely дорогой' - смешивание; 'raw Stellar плазма |
| quest.Ix6qrScZQPGnl3jEm9P2Ag.desc | major | mistranslation | Грубо сломанный перевод: 'Sometimes, рецепт' - начало не переведено; 'extra выходы' - смешивание языков; множество не пе |
| quest.Ix6qrScZQPGnl3jEm9P2Ag.name | major | untranslated | Полностью не переведено, остался английский текст: 'There является Extra Stuff...' |
| quest.J2ok3rFLS7quyIlHPaN0FQ.desc | major | mistranslation | Машинный перевод с ошибками: 'на UV вы разблокировать' - неправильное согласование; 'к automatically refill' - неправиль |
| quest.J9eklidSTbyHgMgImYT3-g.desc | major | mistranslation | Машинный перевод низкого качества: 'после вы managed к grab' - неправильный синтаксис; 'к процесс это' - неверный перево |
| quest.JyVKlIbSSiaXjYfQ2FFLhQ.desc | major | mistranslation | Путаница терминов: 'заражение' и 'порча' используются непоследовательно для Flux и Taint, что создает неясность |
| quest.KGBrxQRsSneYMzNHBll9Bg.desc | major | mistranslation | Машинный перевод с множественными ошибками: 'очищенный вода' (неправильный род), английские слова не переведены (caps, C |
| quest.KfgATF33ToiE0aYS4pp04Q.desc | major | mistranslation | 'вмещает в два раза больше' означает 'вдвое больше', а источник говорит 'as many as' (одинаково) |
| quest.KlI9Fbh9SsK4ckVNMJqGFA.desc | major | mistranslation | Машинный перевод: разломанная грамматика ('улучшить будет позволить вы'), английские слова не переведены (faster, altern |
| quest.KlI9Fbh9SsK4ckVNMJqGFA.name | major | terminology | 'тира' - это не русское слово, должно быть 'уровня' или '4-го уровня' |
| quest.LIZCdBLfQquQpULGmFDixw.desc | major | mistranslation | Машинный перевод: английские слова не переведены (caps, better), неправильная грамматика, должно быть 'Эти колпачки даже |
| quest.M7CE2a0uSOSZZsyNloB0zg.desc | major | mistranslation | Машинный перевод: английские слова не переведены (passive, generating, flower, never-ending, torrent), разломанная грамм |
| quest.MFGBdpO5TH6jRZXJSQistA.desc | major | mistranslation | Неправильная грамматика: 'будет увеличить' вместо 'увеличит'; неправильные предлоги: 'из...к' вместо 'с...до'; английско |
| quest.MFGBdpO5TH6jRZXJSQistA.name | major | mixed_language | Смешанный текст: английские слова 'Smelling' и 'Better' оставлены без перевода в русском контексте. |
| quest.MiGXZ65sRwiAdpsCrVB0Eg.desc | major | mixed_language | Машинный перевод: английские слова 'bad boi', 'handle', 'modules', 'once' оставлены без перевода в русском тексте. |
| quest.MiGXZ65sRwiAdpsCrVB0Eg.name | major | mixed_language | Смешанный текст: английское название 'Yet Another Space Elevator' смешано с русским 'улучшить' в одной строке. |
| quest.MwRByyNxQt-LfGgUqm8QDQ.desc | major | mixed_language | Машинный перевод с густым смешением английских слов: 'Remote запрос', 'always convenient', 'как long как', 'запрос труба |
| quest.N8isBrjBRNe-3f-IHVymDg.name | major | mistranslation | Неправильная грамматика и конструкция: 'получить те машины к работать' - неправильное управление. Должно быть что-то вро |
| quest.NKKa001sQ9qXBPAUEV4Vrg.desc | major | mixed_language | Машинный перевод: 'материя Manipulator', 'why not сделать это better', 'quality life improvements', 'Pay attention к app |
| quest.NzynzD7HQrmEAf7BFd2A2w.desc | major | mixed_language | Машинный перевод: 'не является как picky как her peers', 'Есть no разведение requirements', 'species будучи Gold и Redst |
| quest.OEBBeZOSSRGu80s3RPeiVA.desc | major | mistranslation | Тяжёлое машинное переводное искажение с английскими словами внутри текста. Untranslated: 'Contained', 'Surely', 'opposit |
| quest.Oh_EQhvBQUqHeVcUyifCXQ.desc | major | mistranslation | Значительное машинное переводное искажение. Untranslated: 'Furnace' остаётся как есть. Garbled: 'можно сделано из' (непр |
| quest.P_nO8frbRM2c-MLKAaJUkw.desc | major | mistranslation | Машинный перевод с критическими ошибками. 'можно сделано из' (грамматически неверно), Untranslated: 'Macerating', 'newly |
| quest.Q10xj-OrTE67wsWuTNCAAQ.desc | major | mistranslation | Машинный перевод с переписыванием смысла. Оригинальный текст полностью отличается от перевода: 'кабель подключится при з |
| quest.Qjg1J4kuS-6937dCEUqHUw.desc | major | mistranslation | Сильная машинная гарнир с перемешиванием английского и русского: 'как additional rings являются placed closer' - полност |
| quest.Qjg1J4kuS-6937dCEUqHUw.name | major | formatting | Неправильный код цвета (§c вместо §b) и ломанный английский 'имеет Hit' вместо полного русского перевода названия. |
| quest.RFgYQ7LAQD-p1gHMaeg5Sg.name | major | mistranslation | 'Insane Voltage Multiblocks' частично переведено - отсутствует 'Insane Voltage', остался только 'IV Мультиблоки'. Нужен  |
| quest.S8Z31Xp-RrSdc2A6rOvUzg.name | major | mistranslation | 'Early Scribing Tools' неправильно переведено как 'Чернильница с пером'. Должно быть примерно 'Ранние инструменты письма |
| quest.SIqmtgRmTj-EsZlXpCdyWQ.desc | major | mistranslation | Множество ошибок: 'в этапа' - грамматически неверно; 'борную кислоту' - неправильный перевод (Borax должен остаться как  |
| quest.SoOmxNJvRcqY-ofFsWbyoQ.desc | major | mistranslation | Сильная машинная гарнир с левыми английскими словами: 'Once вы получить', 'easily duplicate', 'поэтому быть cautious' -  |
| quest.SoOmxNJvRcqY-ofFsWbyoQ.name | major | mistranslation | Сильно ломанный перевод с смешиванием английского и русского: 'получение больше Out ваш Hypogen' - бессмысленный текст.  |
| quest.TBMfXgORRHuggrozS7vsVA.desc | major | mistranslation | Критическая машинная гарнир со смешиванием английского и русского: 'Don't хотите', 'этот устройство может significantly' |
| quest.TBMfXgORRHuggrozS7vsVA.name | major | mistranslation | Смешивание английского и русского в одном названии: 'проверить ваш Warp для Free!' - неправильное смешивание языков и ни |
| quest.TvVeFhtYQCSmlekVCdADaQ.desc | major | mistranslation | «Pech» — название существа из мода Thaumcraft, переведено как «гном», что создает путаницу с примечанием, где упоминаетс |
| quest.U12vBo4fQjOyzJ67qH7gUA.name | major | fluency | Смешаная англо-русская галиматья: «No, это not Typo» — должно быть либо полностью на английском, либо полностью на русск |
| quest.U7Ta5d7PSii76sbIPbltlw.name | major | fluency | Смешаная англо-русская галиматья: «Magnetic Monopole материя» — должно быть полностью на русском (например, «Магнитный м |
| quest.UVG21mYSQJex90gQWdkpIw.name | major | fluency | Смешаная англо-русская галиматья: «Assembling на Space Steroids» — должно быть полностью на русском |
| quest.V76lvP8lSsewcKfwxHirPw.desc | major | fluency | Полная машинная ерунда со смешением английских и русских слов: «easily automatable version обычный», «much like мана Fou |
| quest.VH7nGtkWRp-riK1I3cq5yw.desc | major | fluency | Полностью испорченный машинный перевод с перемешанными английскими и русскими словами, синтаксически неправильный |
| quest.VH7nGtkWRp-riK1I3cq5yw.name | major | untranslated | Английское выражение 'Time to Request' оставлено непереведённым, смешано с русским словом |
| quest.VISeokU3R-efeF88FwLGLw.name | major | untranslated | Слово 'Time' оставлено на английском, должно быть полностью на русском |
| quest.VoQgq6UvTZmo3tpUIZs4Rg.desc | major | fluency | Полностью испорченный машинный перевод с неправильным порядком слов и перемешанными английскими словами |
| quest.VplPMJ0DThWiBNH_Hx5SQA.desc | major | fluency | Испорченный машинный перевод с перемешанными английскими словами и неправильной грамматикой |
| quest.VplPMJ0DThWiBNH_Hx5SQA.name | major | untranslated | Английское 'Light' оставлено непереведённым, форматирование нарушено, вся фраза неправильная |
| quest.WIx0jq8hS8ifWxZWTmC5yA.desc | major | fluency | Испорченный машинный перевод со смешанными английскими и русскими словами, неправильный порядок |
| quest.WIx0jq8hS8ifWxZWTmC5yA.name | major | untranslated | Английское 'Eyes Hurt' оставлено непереведённым в названии |
| quest.WJ-SykCeTr2B-3SHz0mXZg.desc | major | fluency | Испорченный машинный перевод со смешанными английскими словами и неправильной грамматикой |
| quest.WLuCkspyTZqFuqlVVxgyzQ.desc | major | fluency | Полностью испорченный машинный перевод со смешанными английскими словами и фразами, неправильная грамматика |
| quest.WLuCkspyTZqFuqlVVxgyzQ.name | major | untranslated | Названия 'Crayon' и 'Melon' оставлены на английском, должны быть переведены |
| quest.WNC6mX67QGG5gpjX0YkvDw.desc | major | fluency | Испорченный машинный перевод с перемешанными английскими словами и неправильной синтаксисом |
| quest.WPoaCPPwTBSyn2dmh5DcBA.name | major | untranslated | Фраза 'Holy Water' оставлена на английском, форматирование нарушено |
| quest.WqDynhbQQ4GdNMKm0BlbcQ.desc | major | fluency | Испорченный машинный перевод со смешанными английскими словами и неправильной грамматикой |
| quest.XDZFjGB9RlWlrW0mHFoL0g.desc | major | mistranslation | Текст сильно замешан с английским - множество английских слов оставлены без перевода, нарушена грамматика русского языка |
| quest.YVlqGPZBS8qCkkHlu1BDpg.desc | major | mistranslation | Текст полностью замешан с английским языком - множество английских слов оставлены без перевода (Blazing, quantities, thi |
| quest.YxYz1jL6RSWHCxMlTHeJFw.name | major | mistranslation | Английское слово 'Real' оставлено без перевода в середине русского текста. Нарушена грамматика и смысл: должно быть 'Нак |
| quest.Yxrhi0z7SUuvUT3BrsENww.desc | major | mistranslation | Текст замешан с английским языком - множество англоязычных слов оставлены без перевода (living, efficient, wetware, proc |
| quest.ZS2_l5v3R2-gh69ESL-FNQ.name | major | register | Потеря стиля оригинала: "It's DA BEST" - это стилизованный, разговорный текст с капслоком, а перевод "ЭТО САМОЕ ЛУЧШЕЕ"  |
| quest.ZXyJX8zNTQW6swu0OsE03Q.desc | major | mistranslation | "Осади ионы самария" - неправильное повелительное наклонение; "смешай его с соляной кислотой" должно быть "промойте окса |
| quest._Cwgzi_VR5ChWJSIIrzUvg.name | major | fluency | Серьёзно испорченный машинный перевод: "что делать я использовать этот Stuff на?" - грамматически неверно, неправильный  |
| quest._XiSkFhJQ8-WjqujCxBtlw.desc | major | fluency | Крайне испорченный машинный перевод с остатками английского текста: "Logistics трубы иметь автоматизация capability в по |
| quest._XiSkFhJQ8-WjqujCxBtlw.name | major | mixed_language | Смешанный англо-русский язык: "Preparin' для Requestin'" - нарушает целостность локализации. Должно быть либо полностью  |
| quest._hHt1iRERrywJiRVFpOnxw.desc | major | mistranslation | Машинный перевод: текст содержит перемешанный английский и русский языки ('Another тир, overclock ваш линияs к UIV volta |
| quest.a59175-ZS16kxwUW_BCuEQ.desc | major | mistranslation | Машинный перевод: весь текст содержит перемешанный английский и русский ('Congratuations на ваш первый EBF', 'вы будет e |
| quest.aXAQD7T1SnGCAu0L4iV64w.desc | major | fluency | Грамматическая ошибка: 'даёт удваивает' - неправильное согласование глаголов. Должно быть 'даёт удвоенные' или 'удваивае |
| quest.afDCORKvSI-Vk_Mh2-rnZw.name | major | formatting | Цветовой код изменён с §c§l (красный) на §d§l (пурпурный), что нарушает исходное форматирование. |
| quest.b47jlBoHTFGGB3j7nq60Zw.name | major | formatting | Цветовой код изменён с §5§l (пурпурный) на §2§l (зелёный), нарушая исходное форматирование. |
| quest.bGdFghCeQfuBhAeMWxJJ8A.desc | major | mistranslation | Тяжелый машинный перевод, смешение английских и русских слов: 'жезл фокус: Flux Scrubber является incredibly полезный',  |
| quest.bHFEDKAiTwGxaiyZEsmdjg.desc | major | mistranslation | Тяжелый машинный перевод с смешением английского и русского: 'финальный external structural', 'требует самый продвинутый |
| quest.bHFEDKAiTwGxaiyZEsmdjg.name | major | untranslated | Английское слово 'Rule' не переведено, должно быть 'Правило трёх' вместо '§4§l§nRule три'. |
| quest.bNVzOxCORxuo_lhAh13r0A.desc | major | mistranslation | Сильный машинный перевод со смешанным английским. Текст полностью разбор: 'вы к создать вода тот является pure', 'out по |
| quest.bQCnuxrTTBe4ubytZPfl-g.desc | major | mistranslation | Машинный перевод с осколками английского текста: 'иметь storage system тот contains', 'Here comes', 'assigns inventory s |
| quest.cejGOPB2QiuW5833Z5ontA.desc | major | mistranslation | Машинный перевод с грамматическими ошибками: 'мана для все ваш нужно' (неправильное окончание и порядок слов), 'endless  |
| quest.dYvLkQ-xRnWL8Egy_MnoIg.desc | major | mistranslation | Текст содержит смешанный русский и английский код, явные следы машинного перевода: 'perform multiple tasks на once', 'бу |
| quest.eEJocLDBTkmdsCKo7Qhegw.desc | major | mistranslation | Явный машинный перевод, смешанный англо-русский текст: 'только самый продвинутый memory chips будет делать когда working |
| quest.eur7SqfIT8GEE_NxscJj8Q.desc | major | mistranslation | Значение «20 водорослей» переведено как «30 водорослей», что изменяет игровые механики и может ввести игроков в заблужде |
| quest.fVoSLYPcSmKd-gLhBJHK9A.desc | major | mistranslation | Машинный перевод с обширным смешиванием английского текста и русского, нарушена грамматика и логика предложений. Примеры |
| quest.fj2VzJf2Rgev7uY-h3CkJQ.desc | major | mistranslation | Машинный перевод: остатки английского текста без перевода, разломанная грамматика. Примеры: «ваш attempts к улучшить», « |
| quest.g0oiNbRuQpWrzFOS8l-DtA.desc | major | mistranslation | Машинный перевод с обширным повреждением: неправильная грамматика, остатки английского текста. Примеры: «с проект наконе |
| quest.gKMT2pblSg69VL5tAtlfxA.desc | major | mistranslation | Completely garbled machine translation. Mixed English and Russian words throughout ('Arrange Nanites в P-507', 'label их |
| quest.hHjJCOZtR-GM69bGHq845w.desc | major | mistranslation | Heavily machine-translated with mixed English and Russian ('самый powerfull version Laputa shard', 'Maybe вместо использ |
| quest.hUEbNbngSA6JxT_Pjq8DNw.desc | major | mistranslation | Severely garbled machine translation. Mixed English and broken Russian throughout ('Transcendent nanite имеет требуется  |
| quest.hWXZi-whQfmgWO0EII7g2g.desc | major | mistranslation | Garbled machine translation with extensive English left untranslated ('SpaceTime является quite challenge', 'Component A |
| quest.hybMIjq9Q9mxxWKEE8gBWQ.desc | major | mistranslation | Severely garbled machine translation with excessive English retained ('охлаждение exotic слитки proves', 'reinforcing не |
| quest.iO7VxrxPTbutGjRtrcoAxw.desc | major | mistranslation | Garbled machine translation with mixed English and Russian ('используя ваш новый optically enhanced boards', 'что посмот |
| quest.jvKBzB6tRpCQGlnboQxSAA.desc | major | mistranslation | Критическая ошибка: смешанный англо-русский текст, машинный перевод. Английские слова остаются нетранслированными (pleth |
| quest.k0ryGOkkSBOgYUcVY-J4rw.desc | major | mistranslation | Машинный перевод с англо-русским смешением: 'Like его predecessor', 'запустить на once', 'этот time'. Английские слова н |
| quest.k9PA3buhTvK1EJpPfA8ZAg.desc | major | mistranslation | Машинный перевод: смешанный англо-русский текст. 'Welcome к Extremely', 'started создание', 'scaling up', 'infinity'. Мн |
| quest.kazCPEWoSmiZhR4bkHlEBQ.name | major | untranslated | Английский текст остался нетранслированным: 'Eye' и 'End Time' должны быть на русском. Правильно: 'Око в Конце Времени'  |
| quest.kvqtI5rrRrOhi5jhPR-s4A.desc | major | mistranslation | Машинный перевод с англо-русским смешением: 'Didn't expect Rhugnor', 'как usual', 'mix', 'blast', 'form', 'wires', 'supe |
| quest.l4q7oG79RfCZjnE_Ys57DA.desc | major | mistranslation | Машинный перевод: сильно повреждён англо-русским смешением. 'жезл фокус', 'будет fix', 'problems', 'Maintenance люк', 'a |
| quest.lBuQcNYjQ8-YsMFqW6U1tQ.desc | major | mistranslation | Машинный перевод: тяжёлое англо-русское смешение. 'Wireless Computation является similar', 'Server люки send', 'screwdri |
| quest.lBuQcNYjQ8-YsMFqW6U1tQ.name | major | untranslated | Значительная часть текста остаётся на английском: 'Storing Computation'. Должно быть полностью на русском: 'Хранение выч |
| quest.lMDEhTDISSG1u2HYaZVg9w.name | major | untranslated | Английский текст остаётся нетранслированным: 'Came Up' и другие слова. Должно быть 'Кто это назвал??' или 'Кто придумал  |
| quest.m5N5Q9QEREyzF1B4eObk0Q.desc | major | mistranslation | Неправильный перевод: слово 'металл' (metal) ошибочно. Текст о стекле, а не о металле. Должно быть 'Transcendent стекло' |
| quest.msIxGO5gQCWJPmEyp_JhtQ.desc | major | mistranslation | Машинный перевод с множественными необработанными английскими словами (currently, game, assembler, assembly) и нарушенно |
| quest.msIxGO5gQCWJPmEyp_JhtQ.name | major | untranslated | Слово 'Time' остаётся на английском в конце перевода вместо полного перевода 'Один последний раз' |
| quest.n8PKF63sSSi0y8ZBb2RIKQ.desc | major | mistranslation | Машинный перевод с множественными необработанными английскими словами (automating, slowly, rate) и критическими граммати |
| quest.o8_pX-OSRJKBGzDsGujvNw.desc | major | mistranslation | Машинный перевод с необработанными английскими словами (helper, fun) и нарушенной грамматикой. Требует полной переработк |
| quest.pLCgOVmqTUCudSXZusnceg.name | major | untranslated | Слово "Kryptonite" осталось на английском, также использован неправильный адрес ("ваш" вместо "твой") |
| quest.pMGI_sXdQSKWWFFxTunqvA.name | major | untranslated | Слово "Purifying" осталось на английском, неправильный падеж "с плазма" вместо "с плазмой" |
| quest.pXRqb1HyQYSjtHp9dt1xZg.name | major | terminology | "энеровводы" - неправильный/испорченный технический термин, должно быть "энергетические вводы" или похожее |
| quest.pbLvv9tvQaKGp2Y2usPMSw.desc | major | terminology | "тир" - неправильный перевод (тир это тир для стрельбы), должно быть "уровень" или "ярус" |
| quest.q5Gvvfe5Tm2gxZfi7VIgpg.desc | major | mistranslation | Явно машинный перевод - английский текст перемешан с русским, слова не согласованы, ломаная грамматика. Примеры: 'Hurrah |
| quest.q6WN7XY8Qf6PNgWTy7RrBA.desc | major | mistranslation | Машинный перевод - неправильная грамматика и структура. 'bit дорогой' вместо 'Немного дороговато', 'worth QoL предметы'  |
| quest.q9PTMZlaR-GCnyoGNoO8Pw.desc | major | mistranslation | Машинный перевод с перемешанным английским и русским. Примеры: "Let's face это", 'collect nodes', 'eat nodes placed', 'n |
| quest.qp3SFb9oSXKi5Yio_VwgEw.desc | major | mistranslation | Машинный перевод - перемешанный английский и русский. Примеры: 'Automating крафт таблица рецепты', 'крафт logistics труб |
| quest.qp3SFb9oSXKi5Yio_VwgEw.name | major | untranslated | Заголовок остался на английском - 'Automating крафт таблица рецепты' это машинный микс. Должно быть полностью на русском |
| quest.r3fKz87vRk23Tv2TRGarvg.desc | major | mistranslation | Машинный перевод - перемешанный английский и русский. Примеры: 'этот flower использует', 'randomly производить', 'это мо |
| quest.rKrpOyRHRvSF7TeFSskG_A.name | major | mistranslation | Lapotron — имя мода/предмета, следует транслитерировать как 'Лаптрон', а не переводить в 'Лазуротроновая' |
| quest.rZCrzZ3QTni28BdPZf2-0w.desc | major | mistranslation | Машинный перевод низкого качества: смешанный английский и русский, разломанная грамматика ('каждый улучшить previous тир |
| quest.rdpQZW1YQ92vgnjgHVW8Jg.desc | major | mistranslation | Машинный перевод: англоязычные слова оставлены ('unlocking', 'может now'), разломанный синтаксис, непонятная структура |
| quest.rdpQZW1YQ92vgnjgHVW8Jg.name | major | fluency | Неправильная грамматика: 'к производить' — неправильная конструкция, должно быть 'для производства' |
| quest.sHI1n7unRWecpNcyBAgUfw.desc | major | mistranslation | Машинный перевод: смешанный английский и русский ('Dehydrating', 'Composite'), разломанная грамматика ('этот будет prove |
| quest.smCKxKkMSeyIAUeFInS4hQ.desc | major | mistranslation | Машинный перевод: смешанный английский и русский ('вы хотите к rush'), разломанная грамматика, непонятное значение |
| quest.tQecVBhjRRyfR3sqeNBrtA.name | major | fluency | Машинный перевод: неправильный род ('один' вместо правильного), неправильная форма ('жидкость' вместо 'жидкостной'), раз |
| quest.tT0NrRMyTqePf1jeIx7krw.desc | major | mistranslation | Полностью машинный перевод с рассыпанным английским текстом. Нужно переводить связно по-русски: 'Многие рецепты требуют  |
| quest.tT0NrRMyTqePf1jeIx7krw.name | major | mistranslation | Абсолютно неправильный перевод. Должно быть 'Мне это нужно!!!!!!' или 'Мне это просто необходимо!!!!!!!' |
| quest.tu5Lk_jKQR-qgTYD1o3sLg.desc | major | mistranslation | Неверный перевод: 'перегони его вместе с лантановой пылью через Ректификационную колонну' неправильно. Должно быть 'восс |
| quest.uP_FwHb_QTyAPaoZ80u74A.desc | major | mistranslation | В конце примечания неполный текст: 'количество принимаемой энергии от этого НЕ поменяется - оно всё также привязано к ис |
| quest.u_-8t2IvRnydvmUx_qdYuA.desc | major | mistranslation | 'измельчённой самариевой руды (возможно, пока что ты можешь её добывать)' - неправильно. Должно быть 'или измельченной с |
| quest.v-1MbhJWRuiGFBX8KEvsUg.desc | major | mistranslation | Неправильный машинный перевод с перемешанным английским. Должно быть: 'Если вы хотите разводить пчел на пути к пчелам Ла |
| quest.v5GltE2BTW-Me_rEqy5uFg.desc | major | mistranslation | Машинный перевод с огромным количеством ошибок. Должно быть: 'С этого момента вы будете иметь дело с чрезвычайно медленн |
| quest.vLnSpTweSki3BaorBNQhxQ.desc | major | mistranslation | Машинный перевод. Должно быть: 'После того как вы увидите, как долго создается Шираборон, вы, возможно, захотите модерни |
| quest.w4JcJ33CSWGlsKrmyHxnXA.desc | major | mistranslation | Машинный перевод. Должно быть: 'Изготовление кристаллических SoC с помощью LuAG намного быстрее, чем прямое гравирование |
| quest.wGq5FvuuROyyMPbT_SkMYg.desc | major | mistranslation | Машинный перевод низкого качества: смешаны английский и русский языки, множество нетранслюцированного английского текста |
| quest.xQE-vyLyTeCn0SEIHjbkNQ.desc | major | mistranslation | Тяжелый машинный перевод: смешанный текст на английском и русском, обширное нетранслюцированное содержимое, грубые грамм |
| quest.y2mOWnXvRe2xWrdvVS297w.name | major | untranslated | Частичный перевод: ключевые слова Satellites и Orbit оставлены на английском, что нарушает языковую целостность названия |
| quest.ydavD3O5QcKvxk2wIDtakw.desc | major | mistranslation | Критический машинный перевод: смешаны английский и русский, множество нетранслюцированных фраз, нарушена структура предл |
| quest.ykz6BsyOTl2m_xfS28ofXA.desc | major | mistranslation | Машинный перевод с грубыми ошибками: смешанные языки, нетранслюцированные английские слова, грамматические нарушения (не |
| quest.yo1cuNvYSU2JAczbJLAfjg.desc | major | mistranslation | Полностью машинный перевод с грамматическими ошибками и смешиванием языков. Требуется полная переработка. |
| quest.ysj8avl1SESH2ibGOS3qjQ.desc | major | mistranslation | Разрушенный машинный перевод: смешивание языков, нарушение грамматики и времён глаголов. |
| quest.zb1nbwNuSFKuSEyW3mVj-Q.desc | major | mistranslation | Критическая ошибка машинного перевода: оставлены английские слова, нарушена грамматика, бессмысленные конструкции типа ' |
| questline.AAAAAAAAAAAAAAAAAAAAGg.desc | major | mistranslation | Серьезная поломка в переводе - смешаны английские слова (series, dedicated, fission, both) с русским текстом. Требуется  |
| questline.AAAAAAAAAAAAAAAAAAAAHA.desc | major | mistranslation | Полностью разломанный перевод с огромным количеством английских слов (когда, just, cover, pay, к, делать, вы, scare, peo |
| questline.AAAAAAAAAAAAAAAAAAAAHQ.desc | major | mistranslation | Машинный перевод с перемешиванием английского и русского текста - 'Collection endgame objectives' не переведено, 'luck'  |
| questline.AAAAAAAAAAAAAAAAAAAAHg.desc | major | mistranslation | Глубокое перемешивание английского и русского; некорректное управление временами ('вы завершено', 'сделано это'); 'assli |
| questline.l37V2WvbSHGZQ5oMgAfBuw.desc | major | mistranslation | Машинный перевод с перемешиванием английского и русского: 'Maybe взять break каждый now и затем' - текст на английском н |
| questline.ytf2QCzUSk6ihcYeRbwblw.desc | major | mistranslation | Машинный перевод с перемешиванием: 'Enjoying pack поэтому far' - английский текст не переведён; 'Anyways here's ваш roug |
| quest.0J3hYoBeTpe_OnXMU9zRDA.desc | minor | mistranslation | Опущено число '4096' из исходного текста: английский текст упоминает '256k, 1024k, 4096 and 16384k', а русский перевод с |
| quest.0fzaxas8R8OJzvYvqX5d9w.name | minor | mistranslation | Пропущено слово 'Raw' (сырой/необработанный) из названия - 'Raw Carbon Fiber' переведено только как 'Углеволокно', упуст |
| quest.13PWs3MhTUOgkIQq8EKhaQ.desc | minor | mistranslation | 'With the EU transfer rates!' переведено как 'И передавать EU ещё быстрее!' - смысл немного искажен, не совсем отражает  |
| quest.3r7tJ7_bTuePzsh-B_jyIQ.name | minor | terminology | Собственное имя (Marie Curium) должно быть 'Мари Кюри' с прописной буквой, а не 'Мари кюри' |
| quest.3wK8pIDKSOii1__bwf6Ycw.name | minor | formatting | Заголовок должен начинаться с прописной буквы: 'Улучшения', а не 'улучшения' |
| quest.49YfyyG5R8KKRRUKePOqfQ.name | minor | untranslated | 'люк' не полностью переведен. Либо оставить полностью английским, либо полностью перевести на русский |
| quest.4HoSq97QT3G63VJFeV_0ZQ.name | minor | terminology | 'Турбопаровая турбина' - нестандартный термин. Либо оставить английским, либо переводить как 'турбина на перегретом паре |
| quest.4MzUrkH5QsWnE_4APuHhNg.name | minor | untranslated | 'Eyes' должно быть переведено на русский: 'Мои глаза болят! #2' |
| quest.4g20EVdxSWyOUMhZXkcIWQ.desc | minor | fluency | 'листай ниже' неправильно. Должно быть 'листай вниз', 'прокрути вниз' или 'смотри ниже' |
| quest.53iZp0DzRzidBo4-kUsWGg.name | minor | formatting | Код цвета изменен с §5 (фиолетовый) на §2 (зеленый). Это изменяет внешний вид оригинала. Также 'Bo$$' должен быть сохран |
| quest.55XTBx8LRN2Ol_42LS6Mwg.name | minor | formatting | Код цвета изменен с §9 (голубой) на §5 (фиолетовый), что изменяет внешний вид оригинала |
| quest.5EdKBIyDTYa7xhnSCUZmiQ.name | minor | formatting | В оригинале нет форматирования, а в переводе добавлен цветовой код §a§l. Форматирование должно совпадать с оригиналом |
| quest.5bnuPY-USBW37JbkO5VzOw.desc | minor | untranslated | 'lootbag' - игровой термин, оставленный без перевода. Должен быть переведен или объяснен в контексте |
| quest.5mcwk7dYSBydA9KRHbW59A.name | minor | untranslated | 'everytime' и 'Transistors' не переведены. Должно быть 'Это всегда эти транзисторы' |
| quest.5rc45iPDSmqLbuvcioFDEQ.name | minor | untranslated | Слово 'Filtering' оставлено на английском. Должно быть 'Фильтрация по типам' или подобное. |
| quest.8CwALDydSAaz9GGQm5tB-g.name | minor | untranslated | Слово 'Demand' оставлено на английском, 'крафт' написано со строчной буквы. Должно быть 'Крафт по заказу' или подобное. |
| quest.9dt9i3MYRa-NB6KROtAYFA.name | minor | formatting | Код цвета изменен с §c (красный) на §d (розовый), что нарушает оригинальное оформление |
| quest.A4rEQOAXQsaa26Ib_nzkHg.name | minor | terminology | Использована 'тира' вместо 'уровня' или 'T2', что звучит неловко; также добавлен неправильный цветовой код §9 |
| quest.AAAAAAAAAAAAAAAAAAAA-w.desc | minor | fluency | 'вис энергия' - перевод неправильный, следует 'вис' или отдельно 'энергию', так как это разные игровые ресурсы |
| quest.AAAAAAAAAAAAAAAAAAAA0Q.name | minor | register | Формальное 'Занимайтесь' не соответствует неформальному тону остального текста, написанного на 'ты' |
| quest.AAAAAAAAAAAAAAAAAAAA1A.name | minor | formatting | Код цвета изменен с §a (зелёный) на §8 (тёмно-серый), что нарушает оригинальное оформление |
| quest.AAAAAAAAAAAAAAAAAAAA1Q.name | minor | formatting | Код цвета изменен с §b на §9, хотя оба синие, но оригинальный цвет должен быть сохранён |
| quest.AAAAAAAAAAAAAAAAAAAA1g.desc | minor | fluency | 'Поздравлю!' - ошибка, должно быть 'Поздравляю!' |
| quest.AAAAAAAAAAAAAAAAAAAA3w.name | minor | mistranslation | Не переведено вторую часть названия 'What Else' - должно быть 'Рельсотроны, что ещё' или подобное |
| quest.AAAAAAAAAAAAAAAAAAAA4g.desc | minor | fluency | Неловкие конструкции: 'кристаллов, что ты нашел' и 'кристаллы начинают вибрировать, при приближении' - нужна правка пунк |
| quest.AAAAAAAAAAAAAAAAAAAA5A.name | minor | terminology | 'Сигилы 2 тира' - неправильное слово 'тира', должно быть 'Сигилы 2-го уровня' или 'Сигилы уровня 2' |
| quest.AAAAAAAAAAAAAAAAAAAA7g.desc | minor | fluency | Дублирование союза 'если если' вместо одного; неловкие фразы 'есть нечто, что может наполнять' - нужна правка |
| quest.AAAAAAAAAAAAAAAAAAAA7g.name | minor | mistranslation | 'Наааполнение' не передаёт пунскую природу оригинала 'Fuuuuuu...(sion)!' - должно быть что-то наподобие 'Блииииин' или ' |
| quest.AAAAAAAAAAAAAAAAAAAA8Q.desc | minor | fluency | 'Ни закидывай' - ошибка в форме отрицания, должно быть 'Не закидывай' |
| quest.AAAAAAAAAAAAAAAAAAAABg.desc | minor | fluency | Неловкое словоупотребление: 'Давай я обменяю' звучит странно в контексте инструкции; 'долистать вниз, чтобы найти её' -  |
| quest.AAAAAAAAAAAAAAAAAAAACQ.name | minor | mistranslation | Неправильный перевод названия квеста; 'Пакуйтесь с миром' не отражает каламбур 'Rest in Pieces' (игра слов на 'Rest in P |
| quest.AAAAAAAAAAAAAAAAAAAADw.name | minor | formatting | Неправильный код цвета: английское '§2§l' изменено на '§a§l' в русском переводе. |
| quest.AAAAAAAAAAAAAAAAAAAAEA.name | minor | formatting | Неправильный код цвета: английское '§3§l' изменено на '§c§l' в русском переводе. |
| quest.AAAAAAAAAAAAAAAAAAAAEQ.name | minor | formatting | Неправильный код цвета: английское '§2§l' изменено на '§a§l' в русском переводе. |
| quest.AAAAAAAAAAAAAAAAAAAAEg.name | minor | formatting | Неправильный код цвета: английское '§2§l' изменено на '§a§l' в русском переводе. |
| quest.AAAAAAAAAAAAAAAAAAAAEw.name | minor | formatting | Неправильный код цвета: английское '§2§l' изменено на '§a§l' в русском переводе. |
| quest.AAAAAAAAAAAAAAAAAAAAFA.name | minor | formatting | Неправильный код цвета: английское '§2§l' изменено на '§a§l' в русском переводе. |
| quest.AAAAAAAAAAAAAAAAAAAAFQ.name | minor | formatting | Неправильный код цвета: английское '§2§l' изменено на '§a§l' в русском переводе. |
| quest.AAAAAAAAAAAAAAAAAAAAUw.desc | minor | fluency | Грамматическая ошибка в конструкции «не будет вырабатывать». Нужно «не будет вырабатываться» или переформулировать фразу |
| quest.AAAAAAAAAAAAAAAAAAAAVQ.name | minor | formatting | В русском переводе добавлены коды §5§l (фиолетовый + жирный), которых нет в английском оригинале. Форматирование должно  |
| quest.AAAAAAAAAAAAAAAAAAAAZg.name | minor | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный); требуется сохранить исходный код |
| quest.AAAAAAAAAAAAAAAAAAAAZw.name | minor | formatting | Цветовой код изменён с §5 на §2; требуется сохранить исходный код |
| quest.AAAAAAAAAAAAAAAAAAAA_Q.desc | minor | mistranslation | "эссенции Aqua" и "Sano" - в оригинале это модальные названия (aqua, sano), не переводятся; они должны остаться без пере |
| quest.AAAAAAAAAAAAAAAAAAAAaA.name | minor | formatting | Цветовой код изменён с §5 на §2; требуется сохранить исходный код |
| quest.AAAAAAAAAAAAAAAAAAAAaQ.desc | minor | mistranslation | "столкнешься ты с ними попозже" - неправильная грамматика; должно быть "столкнёшься с ними позже" или аналогично; в цело |
| quest.AAAAAAAAAAAAAAAAAAAAaQ.name | minor | formatting | Цветовой код изменён с §5 на §2; точка в конце названия (§2§lЭкономия металла с помощью гибки.) должна быть удалена как  |
| quest.AAAAAAAAAAAAAAAAAAAAag.desc | minor | mistranslation | "здоровая" - странный выбор слова; в контексте имеется в виду "большая" или "серьёзная" задача; "конструктор вагонеток"  |
| quest.AAAAAAAAAAAAAAAAAAAAaw.desc | minor | mistranslation | "угольным двигателем" - в оригинале "coal engine", правильнее было бы "угольный двигатель" или "двигатель на угле"; допу |
| quest.AAAAAAAAAAAAAAAAAAAAbw.desc | minor | mistranslation | "из-за схода с рельс" - неправильное выражение; должно быть "со схода с рельс" или просто "при сходе с рельс"; в остальн |
| quest.AAAAAAAAAAAAAAAAAAAAcQ.name | minor | formatting | Цветовой код изменён с §5 на §2; требуется сохранить исходный код |
| quest.AAAAAAAAAAAAAAAAAAAAcg.name | minor | formatting | Неверный код цвета: §5 заменён на §2 |
| quest.AAAAAAAAAAAAAAAAAAAAcw.name | minor | formatting | Неверный код цвета: §5 заменён на §2 |
| quest.AAAAAAAAAAAAAAAAAAAAdA.name | minor | formatting | Неверный код цвета: §5 заменён на §2 |
| quest.AAAAAAAAAAAAAAAAAAAAdQ.name | minor | formatting | Неверный код цвета: §5 заменён на §2 |
| quest.AAAAAAAAAAAAAAAAAAAAdg.desc | minor | fluency | Грамматическая ошибка: 'раздражают' (множественное число) вместо 'раздражает' (единственное); неловкое выражение 'познак |
| quest.AAAAAAAAAAAAAAAAAAAAdg.name | minor | formatting | Неверный код цвета: §5 заменён на §2 |
| quest.AAAAAAAAAAAAAAAAAAAAdw.name | minor | formatting | Неверный код цвета: §3 заменён на §c |
| quest.AAAAAAAAAAAAAAAAAAAAeg.desc | minor | fluency | Неловкое выражение 'на неком основании'; лучше 'на основание турели' |
| quest.AAAAAAAAAAAAAAAAAAAAew.desc | minor | fluency | Диалектная ошибка: 'Дак' вместо 'Так' |
| quest.AAAAAAAAAAAAAAAAAAAAfA.desc | minor | fluency | Неправильное слово: 'чутка' вместо 'чуть-чуть' или 'очень мало' |
| quest.AAAAAAAAAAAAAAAAAAAAfQ.desc | minor | fluency | Диалектная ошибка: 'дак' вместо 'так' |
| quest.AAAAAAAAAAAAAAAAAAAAhQ.desc | minor | fluency | Неловкое выражение: 'встань на якорь и нажми Shift, смотря на якорь' смешивает инструкции; должно быть разделено более я |
| quest.AAAAAAAAAAAAAAAAAAAAjQ.desc | minor | terminology | Добавлены неправомерные детали 'из EnderIO', которых нет в исходном тексте. |
| quest.AAAAAAAAAAAAAAAAAAAAjw.desc | minor | fluency | Перевод 'НЕ ПОЗВОЛЯЕТ' вместо простого 'не' изменяет структуру предложения и звучит неестественно. |
| quest.AAAAAAAAAAAAAAAAAAAAmA.name | minor | formatting | Цветовой код изменён: источник §9§l (синий), перевод §5§l (магента) |
| quest.AAAAAAAAAAAAAAAAAAAAoA.name | minor | formatting | Цветовой код изменён: источник §9§l (синий), перевод §5§l (магента) |
| quest.AAAAAAAAAAAAAAAAAAAAog.name | minor | formatting | Цветовой код изменён: источник §9§l (синий), перевод §5§l (магента) |
| quest.AAAAAAAAAAAAAAAAAAAAow.name | minor | formatting | Цветовой код изменён: источник §9§l (синий), перевод §5§l (магента) |
| quest.AAAAAAAAAAAAAAAAAAAApQ.name | minor | formatting | Цветовой код изменён: источник §9§l (синий), перевод §5§l (магента) |
| quest.AAAAAAAAAAAAAAAAAAAApw.desc | minor | mistranslation | Фраза 'в каменном веке' добавлена переводчиком, её нет в оригинале. Оригинал был умышленно неясным |
| quest.AAAAAAAAAAAAAAAAAAAApw.name | minor | formatting | Цветовой код изменён: источник §9§l (синий), перевод §5§l (магента) |
| quest.AAAAAAAAAAAAAAAAAAAAqQ.name | minor | formatting | Цветовой код изменён: источник §9§l (синий), перевод §5§l (магента) |
| quest.AAAAAAAAAAAAAAAAAAAAqg.name | minor | formatting | Цветовой код изменён: источник §9§l (синий), перевод §5§l (магента) |
| quest.AAAAAAAAAAAAAAAAAAAAuw.desc | minor | register | Использовано "вам" (формальное обращение) вместо "тебе" (личное), что нарушает консистентность с остальным текстом |
| quest.AAAAAAAAAAAAAAAAAAAAvg.name | minor | formatting | Неправильный цветовой код: §8 (серый) вместо §a (зелёный), как в исходном тексте |
| quest.AAAAAAAAAAAAAAAAAAAAwQ.desc | minor | mistranslation | "they're even can recycle them to get" - в русском нарушена структура: "В дальнейшем, их даже можно переработать" звучит |
| quest.AAAAAAAAAAAAAAAAAAAAwQ.name | minor | formatting | Неправильный цветовой код: §8 (серый) вместо §a (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAwg.name | minor | formatting | Неправильный цветовой код: §8 (серый) вместо §a (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAww.name | minor | formatting | Неправильный цветовой код: §8 (серый) вместо §a (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAxA.name | minor | formatting | Неправильный цветовой код: §8 (серый) вместо §a (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAxQ.name | minor | formatting | Неправильный цветовой код: §8 (серый) вместо §a (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAxw.name | minor | formatting | Неправильный цветовой код: §8 (серый) вместо §a (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAyA.name | minor | formatting | Неправильный цветовой код: §8 (серый) вместо §a (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAAAyQ.name | minor | formatting | Неправильный цветовой код: §d (светло-пурпурный) вместо §c (красный) |
| quest.AAAAAAAAAAAAAAAAAAAAyg.name | minor | formatting | Неправильный цветовой код: §d (светло-пурпурный) вместо §c (красный) |
| quest.AAAAAAAAAAAAAAAAAAAAyw.name | minor | terminology | Отсутствует 'АЭ' в переводе названия; должно быть 'Объединённые каналы АЭ' или 'Связанные каналы Applied Energistics' |
| quest.AAAAAAAAAAAAAAAAAAAAzg.name | minor | mistranslation | 'Охлаждение' не передаёт смысл 'Venting the Heat'; должно быть 'Отвод тепла' или 'Вентиляция тепла' |
| quest.AAAAAAAAAAAAAAAAAAAB2A.name | minor | mistranslation | Неверная цветовая кодировка: en имеет §2 (зелёный), а ru имеет §a (зелёный лайм). Также единственное число "инструменты" |
| quest.AAAAAAAAAAAAAAAAAAAB2Q.name | minor | mistranslation | Неверная цветовая кодировка: en имеет §2, ru имеет §a. Также нарушена грамматика: 'Делаем меч получше' звучит неловко; б |
| quest.AAAAAAAAAAAAAAAAAAAB2g.name | minor | mistranslation | Неверная цветовая кодировка: en имеет §2, ru имеет §a |
| quest.AAAAAAAAAAAAAAAAAAAB3g.name | minor | mistranslation | Неверная цветовая кодировка: en имеет §3, ru имеет §c. Также перевод неполный/неточный: 'Огниво' - это только один из дв |
| quest.AAAAAAAAAAAAAAAAAAAB3w.name | minor | mistranslation | Неверная цветовая кодировка: en имеет §3, ru имеет §c |
| quest.AAAAAAAAAAAAAAAAAAAB4A.name | minor | mistranslation | Неверная цветовая кодировка: en имеет §2, ru имеет §a |
| quest.AAAAAAAAAAAAAAAAAAAB4Q.name | minor | mistranslation | Неверная цветовая кодировка: en имеет §2, ru имеет §a |
| quest.AAAAAAAAAAAAAAAAAAAB4g.name | minor | formatting | Код цвета изменён с §2 на §a - должен сохраняться как в источнике |
| quest.AAAAAAAAAAAAAAAAAAAB4w.name | minor | formatting | Код цвета изменён с §2 на §a |
| quest.AAAAAAAAAAAAAAAAAAAB5g.name | minor | formatting | Код цвета изменён с §2 на §a |
| quest.AAAAAAAAAAAAAAAAAAAB5w.name | minor | formatting | Код цвета изменён с §2 на §a |
| quest.AAAAAAAAAAAAAAAAAAAB6A.name | minor | formatting | Код цвета изменён с §2 на §a |
| quest.AAAAAAAAAAAAAAAAAAAB6Q.name | minor | formatting | Код цвета изменён с §2 на §a |
| quest.AAAAAAAAAAAAAAAAAAAB6w.name | minor | formatting | Код цвета изменён с §2 на §a |
| quest.AAAAAAAAAAAAAAAAAAAB7A.name | minor | formatting | Код цвета изменён с §2 на §a |
| quest.AAAAAAAAAAAAAAAAAAAB7Q.name | minor | formatting | Код цвета изменён с §3 на §c |
| quest.AAAAAAAAAAAAAAAAAAAB7g.name | minor | formatting | Код цвета изменён с §2 на §a |
| quest.AAAAAAAAAAAAAAAAAAAB7w.name | minor | formatting | Код цвета изменён с §3 на §c |
| quest.AAAAAAAAAAAAAAAAAAAB8A.name | minor | formatting | Код цвета изменён с §3 на §c |
| quest.AAAAAAAAAAAAAAAAAAAB8Q.name | minor | formatting | Код цвета изменён с §3 на §c |
| quest.AAAAAAAAAAAAAAAAAAAB8g.name | minor | formatting | Код цвета изменён с §2 на §a |
| quest.AAAAAAAAAAAAAAAAAAABAg.desc | minor | mistranslation | Недопустимое искажение терма 'centi-vis' -> 'санти-вис' нарушает форматирование и корректность модовского контента. |
| quest.AAAAAAAAAAAAAAAAAAABGA.name | minor | mistranslation | Грамматическая ошибка: 'мен' вместо 'меня'. Должно быть: 'Они видят меня, они наблюдают за мной'. |
| quest.AAAAAAAAAAAAAAAAAAABJw.name | minor | untranslated | Полностью необработанные английские слова 'Essentia' и 'Storage'. Название должно быть полностью переведено на русский. |
| quest.AAAAAAAAAAAAAAAAAAABMA.name | minor | terminology | 'Зачаровывая как про' - неправильно. 'про' - сленг, не подходит. Должно быть 'Чарование как профессионал' или 'Зачаровыв |
| quest.AAAAAAAAAAAAAAAAAAABNA.desc | minor | untranslated | Необработанные английские слова 'Barren' и 'Not'. Должно быть полностью переведено: 'Бесплодная пчела. Не намного лучше. |
| quest.AAAAAAAAAAAAAAAAAAABNg.name | minor | untranslated | Слово 'Unleashed' оставлено на английском, должно быть 'Раскрытая энергия - Cowl' или аналог. |
| quest.AAAAAAAAAAAAAAAAAAABOA.name | minor | untranslated | 'Unleashed' оставлено на английском, требуется перевод. |
| quest.AAAAAAAAAAAAAAAAAAABOg.name | minor | untranslated | 'Unleashed' не переведено. |
| quest.AAAAAAAAAAAAAAAAAAABPQ.name | minor | untranslated | 'Unleashed' и 'Boots' не переведены полностью. |
| quest.AAAAAAAAAAAAAAAAAAABRA.name | minor | untranslated | 'Unleashed' не переведено. |
| quest.AAAAAAAAAAAAAAAAAAABRQ.name | minor | untranslated | 'Unleashed' не переведено. |
| quest.AAAAAAAAAAAAAAAAAAABRg.name | minor | untranslated | 'Unleashed' не переведено. |
| quest.AAAAAAAAAAAAAAAAAAABRw.name | minor | untranslated | 'Unleashed' не переведено. |
| quest.AAAAAAAAAAAAAAAAAAABSA.desc | minor | mixed_language | 'Hermione's первый years bag' - смешанный язык, должно быть полностью на русском. |
| quest.AAAAAAAAAAAAAAAAAAABSA.name | minor | untranslated | 'Hold' не переведено полностью в контексте названия. |
| quest.AAAAAAAAAAAAAAAAAAABSQ.desc | minor | mistranslation | 'Это вероятно better not к ask' - смешанный язык и грамматические ошибки. |
| quest.AAAAAAAAAAAAAAAAAAABSQ.name | minor | mistranslation | 'где делать предметы Go?' - неправильная грамматика и структура, 'Go' не переведено. |
| quest.AAAAAAAAAAAAAAAAAAABSw.name | minor | untranslated | 'Why Walk' не полностью переведено, отсутствует идиоматический перевод заголовка. |
| quest.AAAAAAAAAAAAAAAAAAABTg.name | minor | fluency | Странное выражение 'котелок побулькивает' звучит неестественно; должно быть 'Котелок булькает' или 'Кипящий котелок' |
| quest.AAAAAAAAAAAAAAAAAAABVQ.name | minor | terminology | 'Мазь полета' не отражает оригинальный пун 'Flying OINKment' (OINK + ointment); лучше оставить узнаваемым переводом игры |
| quest.AAAAAAAAAAAAAAAAAAABVw.desc | minor | fluency | 'творить свои злые делишки' - странный перевод; должно быть 'зло' или 'чёрную магию', а не 'делишки' |
| quest.AAAAAAAAAAAAAAAAAAABWQ.name | minor | terminology | 'Плетёные ботинки' не соответствует 'Seeping Shoes'; 'Seeping' означает просачивание/поливание, а не плетение |
| quest.AAAAAAAAAAAAAAAAAAABZQ.desc | minor | terminology | 'торий пчела' - должно быть 'Ториевая пчела' с заглавной буквы для согласования с названием квеста |
| quest.AAAAAAAAAAAAAAAAAAABaw.name | minor | untranslated | Английское слово 'Gassy' оставлено непереведённым в заголовке |
| quest.AAAAAAAAAAAAAAAAAAABdw.name | minor | formatting | Добавлены цветовые коды (§b§l) которых нет в исходном английском тексте |
| quest.AAAAAAAAAAAAAAAAAAABeA.desc | minor | mistranslation | Ошибка времени глагола (Я работал = прошедшее время вместо настоящего), неестественное звучание |
| quest.AAAAAAAAAAAAAAAAAAABeA.name | minor | formatting | Добавлены цветовые коды (§b§l) которых нет в исходном английском тексте |
| quest.AAAAAAAAAAAAAAAAAAABeQ.name | minor | formatting | Добавлены цветовые коды (§b§l) которых нет в исходном английском тексте |
| quest.AAAAAAAAAAAAAAAAAAABhg.name | minor | untranslated | Incomplete translation - should be Индиевая пчела or just Индий, not Индиевая alone |
| quest.AAAAAAAAAAAAAAAAAAABhw.name | minor | untranslated | Incomplete translation - should be Осмиевая пчела or just Осмий, not Осмиевая alone |
| quest.AAAAAAAAAAAAAAAAAAABiA.desc | minor | mistranslation | Mistranslates the meaning - about compact crafting CPU, not CPU load reduction |
| quest.AAAAAAAAAAAAAAAAAAABig.name | minor | formatting | Color code changed from §a§l (green) to §8§l (dark gray); should preserve original color |
| quest.AAAAAAAAAAAAAAAAAAABkA.desc | minor | mistranslation | Pronoun mismatch - uses он (male) for dragon which should be она (female); slight inconsistency with English source |
| quest.AAAAAAAAAAAAAAAAAAABlg.name | minor | terminology | Слово 'тира' не используется в русском языке. Следует использовать 'уровня' или 'Уровня 3'. |
| quest.AAAAAAAAAAAAAAAAAAABlw.name | minor | terminology | Слово 'тира' не используется в русском языке. Следует использовать 'уровня' или 'Уровня 1'. |
| quest.AAAAAAAAAAAAAAAAAAABnA.name | minor | fluency | Смешанный язык: 'простой Alchemical Things'. Должно быть 'Простые Алхимические Вещи' с правильной капитализацией. |
| quest.AAAAAAAAAAAAAAAAAAABnw.name | minor | untranslated | Английское слово 'Potion' не переведено. Должно быть 'Зелье: Режим полёта'. |
| quest.AAAAAAAAAAAAAAAAAAABoA.desc | minor | fluency | Смешанный английский и русский языки с грамматическими ошибками. Должна быть полностью на русском. |
| quest.AAAAAAAAAAAAAAAAAAABoQ.desc | minor | untranslated | Английское слово 'Paradigms' не переведено. Должно быть 'Парадигмы определяют вашу магию' или аналогично. |
| quest.AAAAAAAAAAAAAAAAAAABow.desc | minor | mistranslation | Смешанный английский и русский, слова не переведены. 'LOT' и 'internet' должны быть на русском. |
| quest.AAAAAAAAAAAAAAAAAAABpA.desc | minor | fluency | Грамматическая ошибка и смешанный язык: 'являются они полезный? Maybe.' Должно быть 'Полезны ли они? Может быть.' |
| quest.AAAAAAAAAAAAAAAAAAABpA.name | minor | terminology | Слово 'тира' не используется в русском языке. Следует использовать 'уровня'. |
| quest.AAAAAAAAAAAAAAAAAAABpQ.desc | minor | fluency | Грамматическая ошибка: 'больше кровь' неправильно. Должно быть 'больше крови' (родительный падеж). |
| quest.AAAAAAAAAAAAAAAAAAABpQ.name | minor | terminology | Слово 'тира' не используется в русском языке. Следует использовать 'уровня'. |
| quest.AAAAAAAAAAAAAAAAAAABpg.desc | minor | mistranslation | Смешанный английский и русский: 'вы нужно MOOORE. Imbue несколько slates'. Требуется полный перевод на русский. |
| quest.AAAAAAAAAAAAAAAAAAABpg.name | minor | terminology | Неправильное слово — 'тира' вместо 'уровня'. Должно быть 'Плитки 2 уровня' или 'Плитки второго уровня'. |
| quest.AAAAAAAAAAAAAAAAAAABpw.name | minor | mistranslation | 'Кровавый' (bloody) неправильно. 'Apprentice Orb' — 'Сфера ученика' или 'Шар ученика'. Слово 'кровавый' добавляет неправ |
| quest.AAAAAAAAAAAAAAAAAAABqA.name | minor | mistranslation | Неправильный эпитет 'Кровавый'. Должно быть 'Сфера мага' или 'Шар мага', без добавления смысла. |
| quest.AAAAAAAAAAAAAAAAAAABqw.name | minor | terminology | 'тира' вместо 'уровня' — ошибка в написании. Должно быть 'Руны 3 уровня'. |
| quest.AAAAAAAAAAAAAAAAAAABsg.name | minor | mistranslation | Смешанный русский и английский. 'Bound инструменты' — должно быть 'Связанные инструменты' (как в других похожих quests). |
| quest.AAAAAAAAAAAAAAAAAAABtA.name | minor | mistranslation | Смешанный текст. 'Bound инструменты' — должно быть 'Связанные инструменты' (как в BsW.name). Слово 'Axe' не переведено. |
| quest.AAAAAAAAAAAAAAAAAAABtg.name | minor | mistranslation | 'сложный Spell System' — 'Spell' не переведено. Первое слово не капитализировано. Должно быть 'Сложная система заклинани |
| quest.AAAAAAAAAAAAAAAAAAABuQ.name | minor | formatting | Цветовые коды §c§l добавлены в русский перевод, но их не было в исходном названии. Должно быть 'Базовый > Обмен на Steam |
| quest.AAAAAAAAAAAAAAAAAAAC-w.name | minor | formatting | Лишний пробел в начале строки перед 'Промышленный динамит' (§6§l пробел после кода форматирования). |
| quest.AAAAAAAAAAAAAAAAAAAC0Q.name | minor | mistranslation | Неловкая фраза 'Больше НЕ неизвестные семена' звучит странно. Более естественно: 'Неизвестных семян больше нет' или 'Сем |
| quest.AAAAAAAAAAAAAAAAAAAC1g.name | minor | formatting | Цветовой код изменён с §5 на §2 - повреждение форматирования оригинала. |
| quest.AAAAAAAAAAAAAAAAAAAC1w.name | minor | formatting | Цветовой код изменён с §2 на §a - повреждение форматирования оригинала. |
| quest.AAAAAAAAAAAAAAAAAAAC2A.name | minor | formatting | Цветовой код изменён с §2 на §a - повреждение форматирования оригинала. |
| quest.AAAAAAAAAAAAAAAAAAAC2Q.name | minor | formatting | Цветовой код изменён с §2 на §a - повреждение форматирования оригинала. |
| quest.AAAAAAAAAAAAAAAAAAAC2g.desc | minor | fluency | Опечатка: 'биомасссе' содержит три буквы 'с' вместо одной. |
| quest.AAAAAAAAAAAAAAAAAAAC3w.desc | minor | fluency | Грамматическая ошибка: 'дистиллированную воды' - неправильное согласование рода и падежа (должно быть 'дистиллированную  |
| quest.AAAAAAAAAAAAAAAAAAAC5Q.name | minor | formatting | Цветовой код изменён с §3 на §c - повреждение форматирования оригинала. |
| quest.AAAAAAAAAAAAAAAAAAAC5g.name | minor | terminology | Слово 'шахты' излишне и изменяет смысл - источник о добыче в целом, не о шахтах. Должно быть просто 'Копать по одному бл |
| quest.AAAAAAAAAAAAAAAAAAAC5w.name | minor | mistranslation | 'log by log' - это деревянные блоки-бревна, не просто блоки. Фраза потеряла специфику оригинала. Должно быть 'бревно за  |
| quest.AAAAAAAAAAAAAAAAAAAC6g.name | minor | terminology | 'Solar Grade' - это название уровня в моде, переведено как научный термин 'очищенного поликристаллического кремния'. Дол |
| quest.AAAAAAAAAAAAAAAAAAAC7g.name | minor | mistranslation | 'Molten' (расплавленный) потеряно в переводе. Должно быть 'Расплавленный полиэтилен' вместо просто 'Полиэтилен' |
| quest.AAAAAAAAAAAAAAAAAAAC7w.name | minor | mistranslation | 'Mixing at MV level' - общее определение уровня прогресса, переведено узко как 'MV миксер'. Теряется контекст достижения |
| quest.AAAAAAAAAAAAAAAAAAACBA.name | minor | mistranslation | Строчная буква в начале, 'Cruel Disposal' не переведено. Должно быть 'Довольно жестокое избавление' или аналогично. |
| quest.AAAAAAAAAAAAAAAAAAACDA.name | minor | mistranslation | Строчная буква в начале, 'Blinding' не переведено. Должно быть 'Только лучшее: ослепляющая скорость'. |
| quest.AAAAAAAAAAAAAAAAAAACEQ.name | minor | formatting | Неправильный код цвета: §5§l (пурпурный) изменён на §2§l (зелёный). Должен оставаться §5§l. |
| quest.AAAAAAAAAAAAAAAAAAACEg.name | minor | formatting | Неправильный код цвета: §5§l (пурпурный) изменён на §2§l (зелёный). Должен оставаться §5§l. |
| quest.AAAAAAAAAAAAAAAAAAACEw.name | minor | formatting | Неправильный код цвета: §5§l (пурпурный) изменён на §2§l (зелёный). Также перевод 'Сканировать пчёл, культуры и т.д.' не |
| quest.AAAAAAAAAAAAAAAAAAACFA.name | minor | formatting | Неправильный код цвета: §5§l (пурпурный) изменён на §2§l (зелёный). Должен оставаться §5§l. |
| quest.AAAAAAAAAAAAAAAAAAACFQ.name | minor | formatting | Неправильный код цвета: §5§l (пурпурный) изменён на §2§l (зелёный). Должен оставаться §5§l. |
| quest.AAAAAAAAAAAAAAAAAAACFg.name | minor | formatting | Цветовой код изменён с §3 на §c без причины — должен быть сохранён оригинальный формат |
| quest.AAAAAAAAAAAAAAAAAAACFw.name | minor | formatting | Цветовой код изменён с §2 на §a — должен быть сохранён оригинальный формат |
| quest.AAAAAAAAAAAAAAAAAAACGA.name | minor | formatting | Цветовой код изменён с §3 на §c — должен быть сохранён оригинальный формат |
| quest.AAAAAAAAAAAAAAAAAAACGg.name | minor | formatting | Цветовой код изменён с §5 на §2 — должен быть сохранён оригинальный формат |
| quest.AAAAAAAAAAAAAAAAAAACGw.name | minor | formatting | Цветовой код изменён с §5 на §2 — должен быть сохранён оригинальный формат |
| quest.AAAAAAAAAAAAAAAAAAACHA.name | minor | formatting | Цветовой код изменён с §5 на §2 — должен быть сохранён оригинальный формат |
| quest.AAAAAAAAAAAAAAAAAAACHQ.name | minor | formatting | Цветовой код изменён с §5 на §2 — должен быть сохранён оригинальный формат |
| quest.AAAAAAAAAAAAAAAAAAACHg.name | minor | formatting | Цветовой код изменён с §5 на §2 — должен быть сохранён оригинальный формат |
| quest.AAAAAAAAAAAAAAAAAAACIA.name | minor | formatting | Цветовой код изменён с §5 на §2 — должен быть сохранён оригинальный формат |
| quest.AAAAAAAAAAAAAAAAAAACIg.name | minor | formatting | Цветовой код изменён с §5 на §2 (синий на зелёный). Необходимо использовать корректный цветовой код согласно источнику. |
| quest.AAAAAAAAAAAAAAAAAAACIw.name | minor | formatting | Цветовой код изменён с §5 на §2 (синий на зелёный). Необходимо использовать корректный цветовой код согласно источнику. |
| quest.AAAAAAAAAAAAAAAAAAACJA.name | minor | formatting | Цветовой код изменён с §5 на §2 (синий на зелёный). Необходимо использовать корректный цветовой код согласно источнику. |
| quest.AAAAAAAAAAAAAAAAAAACJQ.name | minor | formatting | Цветовой код изменён с §5 на §2 (синий на зелёный). Необходимо использовать корректный цветовой код согласно источнику. |
| quest.AAAAAAAAAAAAAAAAAAACJg.name | minor | formatting | Цветовой код изменён с §5 на §2 (синий на зелёный). Необходимо использовать корректный цветовой код согласно источнику. |
| quest.AAAAAAAAAAAAAAAAAAACJw.name | minor | formatting | Цветовой код изменён с §5 на §2 (синий на зелёный). Необходимо использовать корректный цветовой код согласно источнику. |
| quest.AAAAAAAAAAAAAAAAAAACKA.name | minor | formatting | Цветовой код изменён с §5 на §2 (синий на зелёный). Необходимо использовать корректный цветовой код согласно источнику. |
| quest.AAAAAAAAAAAAAAAAAAACKg.name | minor | formatting | Цветовой код изменён с §5 на §2 (синий на зелёный). Необходимо использовать корректный цветовой код согласно источнику. |
| quest.AAAAAAAAAAAAAAAAAAACLA.desc | minor | terminology | «чутка» — разговорный стиль для формального контекста; «глицеринтринитрата» требует лучшего форматирования (пробел или д |
| quest.AAAAAAAAAAAAAAAAAAACLQ.name | minor | formatting | Цветовой код изменён с §9 (синий) на §5 (магента), потеря исходного форматирования |
| quest.AAAAAAAAAAAAAAAAAAACLg.name | minor | formatting | Цветовой код изменён с §3 (голубой) на §c (красный), потеря исходного форматирования |
| quest.AAAAAAAAAAAAAAAAAAACMw.desc | minor | terminology | «черепушку» — чрезмерно разговорный/сленговый термин; следует использовать «череп» или «черепа» |
| quest.AAAAAAAAAAAAAAAAAAACQA.desc | minor | formatting | Mod-name «Pam`s HarvestCraft» заключён в обратные кавычки, которых нет в исходном тексте, нарушает форматирование |
| quest.AAAAAAAAAAAAAAAAAAACQQ.name | minor | fluency | «Основной блок в Forestry» — неестественное построение; лучше «Основной блок Forestry» или «Базовый блок Forestry» |
| quest.AAAAAAAAAAAAAAAAAAACQw.name | minor | formatting | Цветовой код изменён с §5§l (фиолетовый) на §2§l (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAACRQ.desc | minor | mistranslation | "апатитовые электронные лампы" неправильно — должны быть "апатитовые стержни", которые позже становятся лампами |
| quest.AAAAAAAAAAAAAAAAAAACRQ.name | minor | terminology | "Набор ламп" не передаёт английскую идиому "A Series of Tubes" |
| quest.AAAAAAAAAAAAAAAAAAACRg.desc | minor | fluency | Грамматическая ошибка: "Ты также использовать разные режимы" — пропущено "можешь" |
| quest.AAAAAAAAAAAAAAAAAAACRw.desc | minor | mistranslation | "Чем лучше плата, тем больше областей" не передаёт смысл "For each circuit tier, you can configure 1/4 more" (прогрессив |
| quest.AAAAAAAAAAAAAAAAAAACSg.name | minor | formatting | Цветовой код изменён с §3§l (голубой) на §c§l (красный) |
| quest.AAAAAAAAAAAAAAAAAAACSw.desc | minor | formatting | Форматирование §oneed§r потеряно в переводе — подчёркивание не сохранено |
| quest.AAAAAAAAAAAAAAAAAAACSw.name | minor | formatting | Цветовой код изменён с §5§l (фиолетовый) на §2§l (зелёный) |
| quest.AAAAAAAAAAAAAAAAAAACTg.desc | minor | terminology | «вентилей» архаичный термин для farm valves; должен быть «клапаны». «ёмкостями с водой» vs «капсулами» - противоречие в  |
| quest.AAAAAAAAAAAAAAAAAAACTw.desc | minor | fluency | «поля работы фермы» грамматически неловко; должно быть «участков фермы» или «областей фермы». |
| quest.AAAAAAAAAAAAAAAAAAACUQ.desc | minor | terminology | «плата» архаичный для circuit; должно быть «схема» или контекстно зависит. «области работы» неловко. |
| quest.AAAAAAAAAAAAAAAAAAACUg.desc | minor | terminology | «плата» архаичный для circuit; должно быть «схема». «области работы» неловко. |
| quest.AAAAAAAAAAAAAAAAAAACVQ.desc | minor | fluency | «Ну, из последнего можно получить сурьму» - неловко. «в Аду на высоте» неточно для Y уровней; должно быть «на уровне Y». |
| quest.AAAAAAAAAAAAAAAAAAACWA.name | minor | fluency | «Голода Больше нет» неловко; должно быть «Голода больше нет» (lowercase) или лучше «Конец голоду». |
| quest.AAAAAAAAAAAAAAAAAAACYA.name | minor | formatting | Код цвета изменён с §5 (фиолетовый) на §2 (зелёный). Должен остаться §5§l в начале строки. |
| quest.AAAAAAAAAAAAAAAAAAACYQ.name | minor | formatting | Код цвета изменён с §5 (фиолетовый) на §2 (зелёный). Должен остаться §5§l в начале строки. |
| quest.AAAAAAAAAAAAAAAAAAAC_w.name | minor | formatting | Цветовой код изменён с §5 на §2, что нарушает исходное форматирование |
| quest.AAAAAAAAAAAAAAAAAAACaA.name | minor | formatting | Цветовой код изменён с §5 на §2, что нарушает исходное форматирование |
| quest.AAAAAAAAAAAAAAAAAAACaQ.name | minor | formatting | Цветовой код изменён с §5 на §2, что нарушает исходное форматирование |
| quest.AAAAAAAAAAAAAAAAAAACag.name | minor | formatting | Цветовой код изменён с §5 на §2, что нарушает исходное форматирование |
| quest.AAAAAAAAAAAAAAAAAAACbA.name | minor | formatting | Цветовой код изменён с §5 на §2, что нарушает исходное форматирование |
| quest.AAAAAAAAAAAAAAAAAAACbQ.name | minor | formatting | Цветовой код изменён с §5 на §2, что нарушает исходное форматирование |
| quest.AAAAAAAAAAAAAAAAAAACbg.name | minor | formatting | Цветовой код изменён с §5 на §2, что нарушает исходное форматирование |
| quest.AAAAAAAAAAAAAAAAAAACbw.name | minor | formatting | Цветовой код изменён с §5 на §2, что нарушает исходное форматирование |
| quest.AAAAAAAAAAAAAAAAAAACcA.name | minor | formatting | Цветовой код изменён с §5 на §2, что нарушает исходное форматирование |
| quest.AAAAAAAAAAAAAAAAAAACcQ.desc | minor | fluency | Неловкие формулировки, потеря товарного знака (™), фраза 'сложить её в транспортное положение' звучит неестественно |
| quest.AAAAAAAAAAAAAAAAAAACcQ.name | minor | formatting | Цветовой код изменён с §3 на §c, что нарушает исходное форматирование |
| quest.AAAAAAAAAAAAAAAAAAACcg.name | minor | formatting | Цветовой код изменён с §5 на §2, что нарушает исходное форматирование |
| quest.AAAAAAAAAAAAAAAAAAACfg.desc | minor | mistranslation | 'Smelt your bread' - неправильный перевод как 'Пожарь'. 'Smelt' = плавить/переплавлять, а в контексте - готовить в печи/ |
| quest.AAAAAAAAAAAAAAAAAAACfw.name | minor | formatting | Цветовые коды изменены: источник '§5§l' (фиолетовый+жирный) переведен на '§2§l' (зеленый+жирный). Коды форматирования до |
| quest.AAAAAAAAAAAAAAAAAAACgQ.desc | minor | fluency | Фраза 'Из сернистой нафты ты можешь получить нафту' звучит неловко - получается из нафты получить нафту. Также 'капрон ( |
| quest.AAAAAAAAAAAAAAAAAAACgQ.name | minor | formatting | Цветовые коды изменены: источник '§5§l' переведен на '§2§l'. Коды форматирования должны совпадать. |
| quest.AAAAAAAAAAAAAAAAAAACgg.name | minor | formatting | Цветовые коды изменены: источник '§5§l' переведен на '§2§l'. Коды форматирования должны совпадать. |
| quest.AAAAAAAAAAAAAAAAAAACgw.name | minor | formatting | Цветовые коды изменены: источник '§5§l' переведен на '§2§l'. Коды форматирования должны совпадать. |
| quest.AAAAAAAAAAAAAAAAAAAChA.name | minor | formatting | Цветовые коды изменены: источник '§5§l' переведен на '§2§l'. Коды форматирования должны совпадать. |
| quest.AAAAAAAAAAAAAAAAAAAChQ.desc | minor | fluency | Фраза 'Если по какой-то причине, то хочешь разбежаться' содержит грамматическую ошибку - неправильное использование 'то' |
| quest.AAAAAAAAAAAAAAAAAAAChg.name | minor | formatting | Цветовые коды изменены: источник '§5§l' переведен на '§2§l'. Коды форматирования должны совпадать. |
| quest.AAAAAAAAAAAAAAAAAAAChw.desc | minor | fluency | Фраза 'облепленный 4 батарейками, заправленными электротином' звучит неловко - смешивание 'облеплено' и 'заправлено'. Пр |
| quest.AAAAAAAAAAAAAAAAAAACiA.desc | minor | fluency | 'разряжается в мгновение ока' - неправильное выражение, должно быть 'разряжается в считанные секунды' или 'быстро разряж |
| quest.AAAAAAAAAAAAAAAAAAACig.desc | minor | fluency | Фраза 'Выкинутые на землю предметы разлетятся во все стороны, так как твои вертолетные лопасти их сдувают' неловка и неп |
| quest.AAAAAAAAAAAAAAAAAAACig.name | minor | terminology | 'Не сколько реактивный' - ошибка в написании ('сколько' вместо 'столько'). Правильно: 'Не столько реактивный, а скорее в |
| quest.AAAAAAAAAAAAAAAAAAACjw.desc | minor | formatting | Отсутствует пробел после двоеточия в разделе горячих клавиш: 'Графический интерфейс:Gravi Display HUD' должно быть 'Граф |
| quest.AAAAAAAAAAAAAAAAAAACnA.desc | minor | terminology | Лексическая ошибка: 'резиновых пластин резины' содержит избыточное повторение слова резина. Также 'палки доски' должно б |
| quest.AAAAAAAAAAAAAAAAAAACoQ.name | minor | formatting | Код цвета изменён с §5 (фиолетовый) на §2 (зелёный), что не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAACtQ.name | minor | formatting | Код цвета изменён с §2 (тёмно-зелёный) на §a (ярко-зелёный), что не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAACtg.name | minor | formatting | Цветовой код изменён со §3 на §c, не совпадает с английским оригиналом |
| quest.AAAAAAAAAAAAAAAAAAACuw.desc | minor | mistranslation | Опечатка в названии мода: 'GregTecg' вместо 'GregTech' |
| quest.AAAAAAAAAAAAAAAAAAACwQ.name | minor | formatting | Цветовой код изменён со §3 на §c, не совпадает с английским оригиналом |
| quest.AAAAAAAAAAAAAAAAAAACzA.name | minor | formatting | Цветовой код изменён со §5 на §2, не совпадает с английским оригиналом |
| quest.AAAAAAAAAAAAAAAAAAACzQ.name | minor | formatting | Цветовой код изменён с §5§l (фиолетовый) на §2§l (зелёный), что отличается от исходного. |
| quest.AAAAAAAAAAAAAAAAAAACzg.name | minor | formatting | Цветовой код изменён, отличается от исходного. |
| quest.AAAAAAAAAAAAAAAAAAAD-A.desc | minor | mistranslation | Буква 'И' должна быть 'И' (§o§r - italic formatting), но в переводе это неправильно передано как 'И', и общий перевод за |
| quest.AAAAAAAAAAAAAAAAAAAD-A.name | minor | formatting | Цветовой код изменён с §9§l (синий) на §5§l (фиолетовый). |
| quest.AAAAAAAAAAAAAAAAAAAD-Q.name | minor | mistranslation | Неправильный перевод 'Processor Assembly' как 'Кластер процессоров' - более правильно 'Сборка процессора' или 'Процессор |
| quest.AAAAAAAAAAAAAAAAAAAD-g.desc | minor | mistranslation | Неправильный перевод 'соответствующих вафлей' - должно быть конкретнее 'вафли центрального процессорного устройства'. |
| quest.AAAAAAAAAAAAAAAAAAAD-g.name | minor | formatting | Цветовой код изменён с §9§l (синий) на §5§l (фиолетовый). |
| quest.AAAAAAAAAAAAAAAAAAAD-w.name | minor | formatting | Цветовой код изменён с §9§l (синий) на §5§l (фиолетовый). |
| quest.AAAAAAAAAAAAAAAAAAAD2w.name | minor | formatting | Цветовой код изменён с §9§l (синий) на §5§l (фиолетовый). |
| quest.AAAAAAAAAAAAAAAAAAAD3A.name | minor | formatting | Цветовой код изменён с §9§l (синий) на §5§l (фиолетовый). |
| quest.AAAAAAAAAAAAAAAAAAAD3Q.name | minor | formatting | Цветовой код изменён с §9§l (синий) на §5§l (фиолетовый). |
| quest.AAAAAAAAAAAAAAAAAAAD3g.name | minor | formatting | Цветовой код изменен с §9 на §5, что не соответствует исходному английскому тексту |
| quest.AAAAAAAAAAAAAAAAAAAD5g.name | minor | formatting | Цветовой код изменен с §9 на §5, что не соответствует исходному английскому тексту |
| quest.AAAAAAAAAAAAAAAAAAAD5w.name | minor | formatting | Цветовой код изменен с §9 на §5, что не соответствует исходному английскому тексту |
| quest.AAAAAAAAAAAAAAAAAAAD6A.name | minor | formatting | Цветовой код изменен с §9 на §5, что не соответствует исходному английскому тексту |
| quest.AAAAAAAAAAAAAAAAAAAD6Q.name | minor | formatting | Цветовой код изменен с §9 на §5, что не соответствует исходному английскому тексту |
| quest.AAAAAAAAAAAAAAAAAAAD7Q.name | minor | formatting | Цветовой код изменен с §a на §8, что не соответствует исходному английскому тексту |
| quest.AAAAAAAAAAAAAAAAAAAD8A.name | minor | formatting | Цветовой код изменен с §3 на §c, что не соответствует исходному английскому тексту |
| quest.AAAAAAAAAAAAAAAAAAAD8w.desc | minor | mistranslation | Текст добавляет деталь про Луну которой нет в источнике ('падают из космоса на поверхность Луны' вместо 'fall out of the |
| quest.AAAAAAAAAAAAAAAAAAAD9A.desc | minor | fluency | Слово 'рудопереботки' неправильно написано, должно быть 'переработки руды' |
| quest.AAAAAAAAAAAAAAAAAAAD9w.name | minor | untranslated | Потеряно слово 'Empty' - должно быть 'Пустая пластиковая печатная плата' или подобное |
| quest.AAAAAAAAAAAAAAAAAAADAg.name | minor | formatting | Отсутствует пробел перед '3' и добавлен цветовой код §5 которого нет в источнике |
| quest.AAAAAAAAAAAAAAAAAAADBQ.name | minor | untranslated | Потеряно 'Raw' - должно быть 'Сырая углеткань' вместо просто 'Углеткань' |
| quest.AAAAAAAAAAAAAAAAAAADCg.desc | minor | fluency | 'Проверь вкладку квестов \"...без смерти\"' не соответствует источнику, который просто говорит о главе про броню |
| quest.AAAAAAAAAAAAAAAAAAADEA.desc | minor | terminology | 'Bronze Pipe Casings' неправильно передано как 'бронзовыми полыми корпусами' (hollow casings вместо pipe casings). Непра |
| quest.AAAAAAAAAAAAAAAAAAADEQ.name | minor | mistranslation | 'Transistor' (единственное число) переведено как 'Транзисторы' (множественное число). Должно быть в единственном числе:  |
| quest.AAAAAAAAAAAAAAAAAAADFQ.desc | minor | fluency | Неполный перевод 'energium dust'; 'вырасти из неё' грамматически неправильно для контекста создания кристаллов |
| quest.AAAAAAAAAAAAAAAAAAADFw.desc | minor | fluency | Неловкий порядок слов в 'нужен MV Точный лазерный гравировщик'; должно быть 'лазерный гравировщик уровня MV' |
| quest.AAAAAAAAAAAAAAAAAAADGQ.desc | minor | fluency | 'перечень электросхем в NEI' неловко, 'ради квестов' неестественно; требуется переформулировка |
| quest.AAAAAAAAAAAAAAAAAAADHA.desc | minor | fluency | 'Очкам ночного зрения для работы нужны особые линзы' звучит неловко; переформулировать для естественности |
| quest.AAAAAAAAAAAAAAAAAAADHQ.desc | minor | fluency | 'нужен' должно быть 'нужны' (множественное число для 'goggles') |
| quest.AAAAAAAAAAAAAAAAAAADHg.desc | minor | fluency | 'по следующему квесту' неловко; должно быть 'в следующем квесте' или аналогично |
| quest.AAAAAAAAAAAAAAAAAAADHw.desc | minor | fluency | 'устраивать глубокие заплывы' чрезмерно многословно и меняет смысл; должно быть 'нырять' или 'нырять в нём' |
| quest.AAAAAAAAAAAAAAAAAAADHw.name | minor | mistranslation | 'плавать' неточно передаёт 'dive'; должно быть 'нырять' или 'нырять в нём' |
| quest.AAAAAAAAAAAAAAAAAAADIQ.desc | minor | fluency | 'пару резиновых и нано-ботинок' неловко; должно быть 'резиновые ботинки и нано-ботинки' или 'резиновые и нано-ботинки' |
| quest.AAAAAAAAAAAAAAAAAAADJQ.desc | minor | fluency | Название вкладки может быть неточным переводом; 'ради квестов' неестественная фраза |
| quest.AAAAAAAAAAAAAAAAAAADJg.desc | minor | fluency | 'новенького' слишком неформально; использовать 'новый' |
| quest.AAAAAAAAAAAAAAAAAAADJw.desc | minor | fluency | 'в EV точном лазерном гравировщике' неловко; переформулировать: 'точном лазерном гравировщике уровня EV' |
| quest.AAAAAAAAAAAAAAAAAAADMw.desc | minor | mistranslation | Перевод добавляет уточнение 'маленьких' которого нет в оригинале; '2 маленьких канистры' при том что контекст уже говори |
| quest.AAAAAAAAAAAAAAAAAAADNw.desc | minor | fluency | Фраза 'Кислородная маска эта часть системы' - грамматическая ошибка, пропущена запятая; должно быть 'Кислородная маска - |
| quest.AAAAAAAAAAAAAAAAAAADOQ.name | minor | terminology | Цвет код изменен с §2 на §a - оба это варианты зеленого, но должно быть сохранено точное соответствие |
| quest.AAAAAAAAAAAAAAAAAAADOg.name | minor | terminology | Цвет код изменен с §2 на §a - оба это варианты зеленого, но должно быть сохранено точное соответствие оригиналу |
| quest.AAAAAAAAAAAAAAAAAAADPQ.desc | minor | fluency | Грамматическая ошибка: 'входу с синим кольцо' должно быть 'входу с синим кольцом' (неправильный падеж). Пропозиция требу |
| quest.AAAAAAAAAAAAAAAAAAADQQ.name | minor | mistranslation | 'Purge Your Warp' переведено нечётко и некорректно. 'Purge' в контексте означает очистить/удалить, а 'Warp' должен иметь |
| quest.AAAAAAAAAAAAAAAAAAADQg.name | minor | formatting | Цветовой код изменён: источник §3§l (синий), перевод §c§l (красный). Коды форматирования повреждены. |
| quest.AAAAAAAAAAAAAAAAAAADQw.name | minor | formatting | Цветовой код изменён: источник §3§l (синий), перевод §c§l (красный). Коды форматирования повреждены. |
| quest.AAAAAAAAAAAAAAAAAAADRA.name | minor | formatting | Цветовой код изменён: источник §5§l (фиолетовый), перевод §2§l (зелёный). Коды форматирования повреждены. |
| quest.AAAAAAAAAAAAAAAAAAADRw.name | minor | formatting | Цветовой код изменён: источник §5§l (фиолетовый), перевод §2§l (зелёный). Коды форматирования повреждены. |
| quest.AAAAAAAAAAAAAAAAAAADSA.name | minor | formatting | Цветовой код изменён: источник §5§l (фиолетовый), перевод §2§l (зелёный). Коды форматирования повреждены. |
| quest.AAAAAAAAAAAAAAAAAAADSQ.name | minor | formatting | Код цвета изменён с §9 (синий) на §5 (фиолетовый). Должен остаться исходный формат. |
| quest.AAAAAAAAAAAAAAAAAAADUw.name | minor | formatting | Код цвета изменён с §9 (синий) на §5 (фиолетовый). Должен остаться исходный формат. |
| quest.AAAAAAAAAAAAAAAAAAADVQ.name | minor | formatting | Код цвета изменён с §9 (синий) на §5 (фиолетовый). Должен остаться исходный формат. |
| quest.AAAAAAAAAAAAAAAAAAADVg.name | minor | formatting | Код цвета изменён с §9 (синий) на §5 (фиолетовый). Должен остаться исходный формат. |
| quest.AAAAAAAAAAAAAAAAAAADVw.name | minor | formatting | Код цвета изменён с §9 (синий) на §5 (фиолетовый). Должен остаться исходный формат. |
| quest.AAAAAAAAAAAAAAAAAAADWw.name | minor | formatting | Код цвета изменён с §a (зелёный) на §8 (тёмно-серый). Должен остаться исходный формат. |
| quest.AAAAAAAAAAAAAAAAAAADXA.name | minor | formatting | Код цвета изменён с §9 (синий) на §5 (фиолетовый). Должен остаться исходный формат. |
| quest.AAAAAAAAAAAAAAAAAAADXg.name | minor | terminology | Color code изменён с §2 (зелёный тёмный) на §a (светло-зелёный), что нарушает форматирование и стиль. |
| quest.AAAAAAAAAAAAAAAAAAADXw.desc | minor | terminology | 'запас на всего 7 бросков' неточен; следовало 'всего 7 использований' или 'запас на 7 бросков'. Также 'пополнить запас б |
| quest.AAAAAAAAAAAAAAAAAAADXw.name | minor | terminology | Color code изменён с §2 на §a, нарушая форматирование. |
| quest.AAAAAAAAAAAAAAAAAAADYA.name | minor | formatting | Color code изменён с §2 на §a, нарушая форматирование. |
| quest.AAAAAAAAAAAAAAAAAAADYg.desc | minor | terminology | 'ж/д' — неправильное сокращение в контексте. Должно быть 'железной дороги' или 'ж.д.'. Фраза 'отметить символической зак |
| quest.AAAAAAAAAAAAAAAAAAADYw.desc | minor | terminology | 'кирпичную доменную печь' логичнее как 'кирпичную доменную печь'. Но главная ошибка: 'ради содержащегося в ней кальцита' |
| quest.AAAAAAAAAAAAAAAAAAADZA.desc | minor | terminology | 'фуллеровой землей' неправильно; должно быть 'фуллеровой земле' или 'фуллеровой глине'. Структура предложения громоздка; |
| quest.AAAAAAAAAAAAAAAAAAADZA.name | minor | formatting | Color code изменён с §3 на §c, нарушая форматирование. |
| quest.AAAAAAAAAAAAAAAAAAADZQ.name | minor | formatting | Color code изменён с §5 (пурпурный) на §2 (тёмно-зелёный), нарушая форматирование. |
| quest.AAAAAAAAAAAAAAAAAAADZg.desc | minor | terminology | 'С щепоткой стали' — неправильный перевод 'With a bit of steel'; должно быть 'С небольшим количеством стали' или 'потрат |
| quest.AAAAAAAAAAAAAAAAAAADZg.name | minor | formatting | Color code изменён с §6 (золотистый) на §c (красный), нарушая форматирование. |
| quest.AAAAAAAAAAAAAAAAAAADZw.name | minor | formatting | Color code изменён с §3 (бирюзовый) на §c (красный), нарушая форматирование. |
| quest.AAAAAAAAAAAAAAAAAAADaw.desc | minor | terminology | 'Гевея' правильно, но 'в небесах' звучит архаично; лучше 'в небе'. 'сгустки слизи' правильно, но 'листья слизи' неточно  |
| quest.AAAAAAAAAAAAAAAAAAADaw.name | minor | formatting | Color code изменён с §3 (бирюзовый) на §c (красно-оранжевый), нарушая форматирование. |
| quest.AAAAAAAAAAAAAAAAAAADbA.name | minor | formatting | Color code §5 (пурпурный) добавлен в русский перевод, но в оригинале его нет — нарушает форматирование. |
| quest.AAAAAAAAAAAAAAAAAAADeg.name | minor | formatting | Цветовой код не совпадает: английский текст использует '§3§l' (голубой), русский '§c§l' (красный). Должны совпадать цвет |
| quest.AAAAAAAAAAAAAAAAAAADew.name | minor | formatting | Цветовой код не совпадает: английский '§5§l' (фиолетовый), русский '§2§l' (зелёный). Коды должны совпадать. |
| quest.AAAAAAAAAAAAAAAAAAADhQ.desc | minor | terminology | 'minoshroom' переведено как 'грибные кентавры', что слишком креативная интерпретация. Лучше транслитерировать как 'грибо |
| quest.AAAAAAAAAAAAAAAAAAADhw.desc | minor | fluency | Ошибка пунктуации и грамматики: 'пока он не загадал' требует запятую перед ним. Правильно: 'Останови его, пока он не заг |
| quest.AAAAAAAAAAAAAAAAAAADiA.name | minor | mistranslation | 'Who Ya Gonna Call?' - известная цитата из 'Охотников за привидениями'. Переведено как 'Вызывай экзорциста!' - слишком в |
| quest.AAAAAAAAAAAAAAAAAAADig.name | minor | formatting | Неверное форматирование: 'О(т)пусти' содержит странную скобку. Должно быть просто 'Отпусти' или если это вариант перевод |
| quest.AAAAAAAAAAAAAAAAAAADrQ.desc | minor | mistranslation | 'accept 128 EU/t' неправильно переведено как 'заряжается от 128 EU/t' (charges from) вместо 'принимает/воспринимает 128  |
| quest.AAAAAAAAAAAAAAAAAAADrw.name | minor | formatting | Цветовой код изменен с §9 (синий) на §5 (пурпурный/магента). |
| quest.AAAAAAAAAAAAAAAAAAADsQ.name | minor | formatting | Цветовой код изменен с §2 на §a. Также 'Chad' (название) переведено как 'Пульпа' вместо сохранения игровой терминологии. |
| quest.AAAAAAAAAAAAAAAAAAADsw.name | minor | formatting | Цветовой код изменен с §2 на §a. |
| quest.AAAAAAAAAAAAAAAAAAADuQ.desc | minor | terminology | потинов - неправильная форма слова, должно быть потиновых труб |
| quest.AAAAAAAAAAAAAAAAAAADug.desc | minor | mistranslation | fused quartz glass - это кварцевое стекло, а не расплавленный кварц |
| quest.AAAAAAAAAAAAAAAAAAAE-A.desc | minor | terminology | wheaty juice - это пшеничный сок, а не настойка; настойка подразумевает брожение |
| quest.AAAAAAAAAAAAAAAAAAAE-A.name | minor | terminology | wheaty juice - пшеничный сок, а не пшеничная настойка |
| quest.AAAAAAAAAAAAAAAAAAAE3Q.desc | minor | terminology | Вместо 'конвейеры' должно быть 'конвейерные модули'; непродуманный перевод 'роборуки' вместо 'робототехнические рычаги'  |
| quest.AAAAAAAAAAAAAAAAAAAE3g.desc | minor | mistranslation | 'приёмники' неправильно - 'sensors' это датчики, а не приёмники; 'создания сканеров' - 'analyzer' это анализатор, а не с |
| quest.AAAAAAAAAAAAAAAAAAAE4A.desc | minor | mistranslation | 'четыре тира' - неправильно, должно быть 'четыре уровня' или 'четыре типа'; 'мейнфрейма' - лучше 'главная плата' или ост |
| quest.AAAAAAAAAAAAAAAAAAAE4g.desc | minor | mistranslation | 'Нано кластер' - неточный перевод 'Nano Assembly'; должно быть 'Нано сборка' или 'Нано узел' |
| quest.AAAAAAAAAAAAAAAAAAAE5g.desc | minor | mistranslation | 'вычислительной мощности' неправильно; в контексте ME это должно быть просто 'хранения' или 'памяти', не 'вычислительной |
| quest.AAAAAAAAAAAAAAAAAAAE6Q.desc | minor | mistranslation | 'вычислительной мощности' неправильно; должно быть просто 'памяти' или 'хранения' как в контексте ME систем |
| quest.AAAAAAAAAAAAAAAAAAAE6w.desc | minor | mistranslation | 'Как шина экспорта, но для жидкостей' - неполный перевод; должно быть 'Шина экспорта для жидкостей' или 'Шина заполнения |
| quest.AAAAAAAAAAAAAAAAAAAE7w.desc | minor | mistranslation | 'саннариевых акуумуляторов' - неправильно; текст на английском говорит о 'Sunnarium batteries', но в контексте это может |
| quest.AAAAAAAAAAAAAAAAAAAE8w.desc | minor | terminology | 'тире вольтажа повыше' неправильная грамматика. Должно быть 'на один уровень выше по вольтажу' или 'на ступень выше' |
| quest.AAAAAAAAAAAAAAAAAAAE9A.desc | minor | mistranslation | 'потреблять до 4A MV' - неправильно. Должно быть 'принимать 4A MV' или 'входное напряжение 4A MV' |
| quest.AAAAAAAAAAAAAAAAAAAE9Q.desc | minor | mistranslation | 'На, а если' - неловкое начало. 'сверхмощный трансформатор' должно соответствовать названию 'Power Transformer'. 'перегн |
| quest.AAAAAAAAAAAAAAAAAAAE9w.desc | minor | mistranslation | 'вольфрамовой стали' - неправильный перевод 'Tungstensteel'. Это отдельный материал в моде, не 'вольфрамовая сталь'. Дол |
| quest.AAAAAAAAAAAAAAAAAAAEMA.desc | minor | mistranslation | 'несколько других компонентов' неточно - оригинал не упоминает 'другие компоненты'. Опечатка смысла английского оригинал |
| quest.AAAAAAAAAAAAAAAAAAAEOQ.desc | minor | mistranslation | '2х, 3х и более сжатые пластины' - неправильная терминология. 'Compressed plates' должно быть 'двойные, тройные пластины |
| quest.AAAAAAAAAAAAAAAAAAAEUw.name | minor | formatting | Неверный цветовой код §c вместо §3, что изменит цвет с голубого на красный. |
| quest.AAAAAAAAAAAAAAAAAAAEVA.name | minor | formatting | Неверный цветовой код §c вместо §3, что изменит цвет с голубого на красный. |
| quest.AAAAAAAAAAAAAAAAAAAEZg.desc | minor | mistranslation | В исходном тексте упоминается 'zinc' (цинк), но в переводе ошибочно вставлено 'алюминий'. Должно быть: 'смешав обсидиан, |
| quest.AAAAAAAAAAAAAAAAAAAEZw.desc | minor | mistranslation | Неточный перевод - "пластины" неправильно передает смысл. Говорится о создании пластин из обсидиана, которые добавляют м |
| quest.AAAAAAAAAAAAAAAAAAAEZw.name | minor | formatting | Цветовой код изменен с §3 (голубой) на §c (красный) - это нарушает форматирование оригинала |
| quest.AAAAAAAAAAAAAAAAAAAEaA.name | minor | formatting | Цветовой код изменен с §3 (голубой) на §c (красный) - это нарушает форматирование оригинала |
| quest.AAAAAAAAAAAAAAAAAAAEag.name | minor | formatting | Цветовой код изменен с §3 (голубой) на §c (красный) - это нарушает форматирование оригинала |
| quest.AAAAAAAAAAAAAAAAAAAEaw.name | minor | formatting | Цветовой код изменен с §5 (фиолетовый) на §2 (зеленый) - это нарушает форматирование оригинала |
| quest.AAAAAAAAAAAAAAAAAAAEbA.desc | minor | mistranslation | Неточный перевод - "истинного кварца" неправильный термин (Certus quartz - правильный перевод), "обычного" тоже неточный |
| quest.AAAAAAAAAAAAAAAAAAAEbA.name | minor | formatting | Цветовой код изменен с §3 (голубой) на §c (красный) - это нарушает форматирование оригинала |
| quest.AAAAAAAAAAAAAAAAAAAEbg.name | minor | formatting | Цветовой код изменен с §5 (фиолетовый) на §2 (зеленый) - это нарушает форматирование оригинала |
| quest.AAAAAAAAAAAAAAAAAAAEcA.name | minor | formatting | Цветовой код изменен с §5 (фиолетовый) на §2 (зеленый) - это нарушает форматирование оригинала |
| quest.AAAAAAAAAAAAAAAAAAAEcQ.name | minor | formatting | Цветовой код изменен с §9 (бирюзовый) на §5 (фиолетовый) - это нарушает форматирование оригинала |
| quest.AAAAAAAAAAAAAAAAAAAEcg.name | minor | formatting | Цветовой код изменен с §9 на §5, не соответствует исходнику |
| quest.AAAAAAAAAAAAAAAAAAAEcw.name | minor | formatting | Цветовой код изменен с §9 на §5, не соответствует исходнику |
| quest.AAAAAAAAAAAAAAAAAAAEdA.name | minor | formatting | Цветовой код изменен с §9 на §5, не соответствует исходнику |
| quest.AAAAAAAAAAAAAAAAAAAEdQ.name | minor | formatting | Цветовой код изменен с §9 на §5, не соответствует исходнику |
| quest.AAAAAAAAAAAAAAAAAAAEdg.name | minor | terminology | Множественное число в исходнике 'Buffers' не отражено; должно быть 'Аккумуляторные буферы' или подобное |
| quest.AAAAAAAAAAAAAAAAAAAEdw.name | minor | terminology | Форма 'корпусов' неправильна для множественного числа; нужно 'корпусы' или 'корпуса' |
| quest.AAAAAAAAAAAAAAAAAAAEeQ.name | minor | formatting | Цветовой код изменен с §9 на §5, не соответствует исходнику |
| quest.AAAAAAAAAAAAAAAAAAAEeg.name | minor | formatting | Цветовой код изменен с §2 на §a, не соответствует исходнику |
| quest.AAAAAAAAAAAAAAAAAAAEew.name | minor | formatting | Цветовой код изменен с §3 на §c, не соответствует исходнику |
| quest.AAAAAAAAAAAAAAAAAAAEfQ.name | minor | formatting | Цветовой код изменён с §5 (фиолетовый) на §2 (зелёный), не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAEfg.name | minor | formatting | Цветовой код изменён с §5 на §2, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAEgA.name | minor | formatting | Цветовой код изменён с §5 на §2, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAEgQ.name | minor | formatting | Цветовой код изменён с §5 на §2, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAEgg.name | minor | formatting | Цветовой код изменён с §5 на §2, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAEgw.name | minor | formatting | Цветовой код изменён с §5 на §2, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAEhA.name | minor | formatting | Цветовой код изменён с §3 на §c, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAEhQ.name | minor | formatting | Цветовой код изменён с §3 на §c, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAEiA.name | minor | formatting | Цветовой код изменён с §5 на §2, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAEjA.name | minor | formatting | Цветовой код изменён с §9 на §5, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAEjg.name | minor | formatting | Цветовой код изменён с §5 на §2, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAEjw.name | minor | formatting | Цветовой код изменён с §5 на §2, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAEkA.name | minor | formatting | Цветовой код изменён с §5 на §2, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAElA.name | minor | formatting | Цветовой код изменён с §5 на §2, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAEmw.desc | minor | mistranslation | Неточно передано различие между сканером и информационной панелью; 'GT набор с дистанционным датчиком' неловко — должно  |
| quest.AAAAAAAAAAAAAAAAAAAEnA.desc | minor | terminology | 'MV гибочный станок' — неудачный выбор слова; лучше 'MV гибочная машина' или 'MV загибатель'. |
| quest.AAAAAAAAAAAAAAAAAAAEnQ.desc | minor | fluency | 'иметь портативный верстак' звучит неловко; лучше переформатировать или использовать 'переносной'. |
| quest.AAAAAAAAAAAAAAAAAAAEnw.desc | minor | fluency | 'Вагонетка с печью, это дешевая версия' — неправильная пунктуация, должно быть тире. Грамматические недочеты. |
| quest.AAAAAAAAAAAAAAAAAAAEoA.desc | minor | mistranslation | '(Ты не можешь кататься напрямую на поезде...)' неточен — оригинал говорит о том, что ты сидишь В вагонетке, а не на лок |
| quest.AAAAAAAAAAAAAAAAAAAEow.desc | minor | fluency | 'на вагонетках' (множественное число) должно быть 'на вагонетке' (единственное число) — вы едите на одной вагонетке. |
| quest.AAAAAAAAAAAAAAAAAAAEpA.desc | minor | fluency | 'пролистай чутка в право' — 'чутка' — сленг, должно быть 'немного' или 'несколько'. |
| quest.AAAAAAAAAAAAAAAAAAAEpQ.desc | minor | fluency | 'чутка в право' — 'чутка' должна быть заменена на 'немного'. |
| quest.AAAAAAAAAAAAAAAAAAAEpw.desc | minor | terminology | «поспитр» — неестественный машинный перевод составного слова (staff+scepter). Лучше: «посох-скипетр» или просто оставить |
| quest.AAAAAAAAAAAAAAAAAAAEpw.name | minor | terminology | «Поспитр» — тот же проблемный перевод. Рекомендуется: «Посох-скипетр» или оставить в кавычках англ. термин. |
| quest.AAAAAAAAAAAAAAAAAAAEsA.desc | minor | terminology | «LuV Энерговывод [Буферизованный]» — странное оформление. Лучше: «LuV буферизированный энерговывод» или «LuV Buffered Dy |
| quest.AAAAAAAAAAAAAAAAAAAEsA.name | minor | formatting | Цвет изменён с §c (красный) на §d (пурпурный), нарушен оригинальный форматирующий токен. |
| quest.AAAAAAAAAAAAAAAAAAAEsQ.name | minor | formatting | Цвет изменён с §c (красный) на §d (пурпурный), нарушен оригинальный форматирующий токен. |
| quest.AAAAAAAAAAAAAAAAAAAEtA.desc | minor | mistranslation | «расширить сетку крафта вещей до 3x3» — неточно. Источник: создать 3x3 верстак (не расширить существующий). Надо: «созда |
| quest.AAAAAAAAAAAAAAAAAAAEtQ.desc | minor | mistranslation | «воронка должна располагаться сверху целевого места загрузки» — искажено. Источник: «hopper must be beneath its source i |
| quest.AAAAAAAAAAAAAAAAAAAEtQ.name | minor | formatting | Цвет изменён с §3 (голубой) на §c (красный), нарушен оригинальный форматирующий токен. |
| quest.AAAAAAAAAAAAAAAAAAAEvQ.name | minor | formatting | Цвет изменён с §c (красный) на §d (пурпурный), нарушен оригинальный форматирующий токен. |
| quest.AAAAAAAAAAAAAAAAAAAEvg.desc | minor | mistranslation | «Генерации RF энергии вращением ручки» — неясно. Должно быть: «Генерирование RF энергии вручную» (производство вручную). |
| quest.AAAAAAAAAAAAAAAAAAAEvw.desc | minor | mistranslation | «Генерация RF энергии с помощью лавы» — источник не упоминает лаву напрямую. Должно быть: «Генерация RF энергии с помощь |
| quest.AAAAAAAAAAAAAAAAAAAF3A.desc | minor | formatting | Color codes §r неправильно размещены внутри ссылок и команд; должны быть вокруг текста, а не вставлены внутрь |
| quest.AAAAAAAAAAAAAAAAAAAF3g.name | minor | formatting | Код цвета изменён с §9§l на §5§l (синий на фиолетовый), не совпадает с оригиналом |
| quest.AAAAAAAAAAAAAAAAAAAF3w.name | minor | fluency | 'Никто не хочет взорваться' звучит неестественно; должно быть 'Никто не хочет взрыва' или 'Никто не хочет, чтобы был взр |
| quest.AAAAAAAAAAAAAAAAAAAF4A.name | minor | formatting | Код цвета изменён с §2§l на §a§l, не совпадает с оригиналом |
| quest.AAAAAAAAAAAAAAAAAAAF8Q.desc | minor | terminology | 'камни' неправильный перевод для 'gems'. Должно быть 'драгоценные камни' или 'кристаллы'. |
| quest.AAAAAAAAAAAAAAAAAAAFAQ.desc | minor | register | 'Вкуснятина' слишком сленговый. Должно быть 'Вкусно!' или 'Нам нужен ром!' |
| quest.AAAAAAAAAAAAAAAAAAAFDw.desc | minor | fluency | Фраза 'И в отличии от' содержит грамматическую ошибку — правильно 'в отличие от' (без мягкого знака). Также конструкция  |
| quest.AAAAAAAAAAAAAAAAAAAFEg.desc | minor | fluency | Переключение между 'ты' и 'твоей' при обращении к игроку непоследовательно — в некоторых местах используется официальный |
| quest.AAAAAAAAAAAAAAAAAAAFFA.desc | minor | fluency | Неправильное согласование в 'Беспроводной терминал имеет встроенный аккумулятор' — следует проверить контекст, но более  |
| quest.AAAAAAAAAAAAAAAAAAAFFg.desc | minor | fluency | Фраза 'Ты можешь менять его форму просто в сетке крафта' неточна — правильнее 'путём крафта' или 'в сетке крафта'. Также |
| quest.AAAAAAAAAAAAAAAAAAAFIg.desc | minor | formatting | Пропущена предлог 'в' в фразе 'ячейкой руке' - должно быть 'ячейкой в руке' |
| quest.AAAAAAAAAAAAAAAAAAAFJA.desc | minor | formatting | 'ae/t' должно быть 'AE/t' (заглавные буквы для аббревиатуры) |
| quest.AAAAAAAAAAAAAAAAAAAFJQ.desc | minor | formatting | Пропущена предлог 'в' в фразе 'ячейкой руке' - должно быть 'ячейкой в руке' |
| quest.AAAAAAAAAAAAAAAAAAAFSg.desc | minor | register | Тональное несоответствие: переключение с неформального на формальный |
| quest.AAAAAAAAAAAAAAAAAAAFTA.name | minor | terminology | 'Единение' неправильно передает 'Combine' - должно 'Объединение' |
| quest.AAAAAAAAAAAAAAAAAAAFUA.desc | minor | fluency | 'защищёны от взрыва' - ошибка согласования, должно 'защита от взрывов' |
| quest.AAAAAAAAAAAAAAAAAAAFWw.name | minor | mistranslation | 'LOX and Bagels' переведено как 'Жидкий кислород' - потеряна часть названия (Bagels) |
| quest.AAAAAAAAAAAAAAAAAAAFYQ.name | minor | fluency | 'Magical база Defense' - 'база' неправильно согласовано; должно быть 'базовая защита' или 'защита базы'; английские слов |
| quest.AAAAAAAAAAAAAAAAAAAFZQ.name | minor | untranslated | 'Mesmerizing' оставлено нетранслитерированным; должно быть 'Очаровательно' или 'Завораживающе' |
| quest.AAAAAAAAAAAAAAAAAAAFZg.name | minor | fluency | 'Pimp ваш жезл фокус' - смешивание английского сленга с русским; неправильный порядок слов |
| quest.AAAAAAAAAAAAAAAAAAAF_Q.name | minor | formatting | Неправильный цветовой код: оригинал §b§l (синий+жирный), переведено §9§l (другой оттенок синего); коды должны совпадать |
| quest.AAAAAAAAAAAAAAAAAAAF_g.name | minor | formatting | Неправильный цветовой код: оригинал §b§l (синий+жирный), переведено §9§l (другой оттенок синего); коды должны совпадать |
| quest.AAAAAAAAAAAAAAAAAAAFaw.name | minor | mistranslation | 'Fly High!' переведено как 'Fly высокий!' - неправильный порядок слов и грамматика; должно быть 'Летай высоко!' или 'Лет |
| quest.AAAAAAAAAAAAAAAAAAAFcA.name | minor | mistranslation | 'Wand Focus' должно быть переведено как 'Фокус жезла' или 'Фокус руны', а не 'жезл фокус'. |
| quest.AAAAAAAAAAAAAAAAAAAFdw.name | minor | mistranslation | 'Battlemage's лучший Friend' - пропущен артикль 'A'. Должно быть полный перевод как 'Лучший друг боевого мага' или похож |
| quest.AAAAAAAAAAAAAAAAAAAFeQ.name | minor | mistranslation | 'Infuse ваш фокус' - 'Infuse' не переведено. Должно быть 'Наполни свой фокус' или похожее. |
| quest.AAAAAAAAAAAAAAAAAAAFfQ.name | minor | formatting | Неправильный цветовой код. В исходном '§9' (синий), в переводе '§5' (пурпурный). Форматирование повреждено. |
| quest.AAAAAAAAAAAAAAAAAAAFfg.name | minor | formatting | Неправильный цветовой код. В исходном '§a' (зелёный), в переводе '§8' (серый). Форматирование повреждено. |
| quest.AAAAAAAAAAAAAAAAAAAFfw.name | minor | formatting | Цветовой код изменён с §a (зелёный) на §8 (тёмно-серый), должен остаться исходный |
| quest.AAAAAAAAAAAAAAAAAAAFgA.name | minor | terminology | "Сверхпроводник" в единственном числе, должно быть "Сверхпроводники" во множественном |
| quest.AAAAAAAAAAAAAAAAAAAFgQ.name | minor | formatting | Цветовой код изменён с §b (голубой) на §9 (тёмно-голубой), должен остаться исходный |
| quest.AAAAAAAAAAAAAAAAAAAFgg.desc | minor | fluency | "нужен для, например" - неправильная грамматика, должно быть "нужен, например, для" |
| quest.AAAAAAAAAAAAAAAAAAAFhA.name | minor | formatting | Отсутствует цветовой код, должен быть §6§l |
| quest.AAAAAAAAAAAAAAAAAAAFhg.desc | minor | terminology | "излучатели и приёмники" неточны (должны быть "эмиттеры и датчики"), "сборщик электросхем" неловко, должно быть "сборщик |
| quest.AAAAAAAAAAAAAAAAAAAFig.desc | minor | formatting | "....в моих снах" - четыре точки вместо правильного эллипсиса |
| quest.AAAAAAAAAAAAAAAAAAAFiw.name | minor | fluency | "болячку" - разговорное и неловкое, слово звучит странно в контексте. Лучше "рак" или "опасное заболевание" |
| quest.AAAAAAAAAAAAAAAAAAAFjQ.desc | minor | terminology | "чипа улучшения дробителя" неловко, должно быть "чипа улучшения" или конкретного названия механизма |
| quest.AAAAAAAAAAAAAAAAAAAFjg.name | minor | formatting | Отсутствует цветовой код §8§l |
| quest.AAAAAAAAAAAAAAAAAAAFjw.name | minor | formatting | Отсутствует цветовой код §8§l |
| quest.AAAAAAAAAAAAAAAAAAAFkw.desc | minor | terminology | "раздробить эндерняк или блоки с поверхности Луны" - неточно, источник специально упоминает "end stone" и "end stone dus |
| quest.AAAAAAAAAAAAAAAAAAAFmQ.name | minor | terminology | 'Dungeon' переведено как 'сокровищница', что не совсем корректно; лучше 'подземелье' |
| quest.AAAAAAAAAAAAAAAAAAAFmw.name | minor | terminology | 'Moon Buggy Schematic' переведено как 'Схема для постройки багги' - неловко; упущено 'Луны/лунного' |
| quest.AAAAAAAAAAAAAAAAAAAFnQ.desc | minor | fluency | Повторение слова 'баллон' в одном предложении; 'воздуха' вместо 'кислорода' хотя контекст говорит об oxygen tank |
| quest.AAAAAAAAAAAAAAAAAAAFnw.desc | minor | formatting | 'Dream 2018 н.э.' - ошибочный формат; 'н.э.' неместно здесь; должно быть просто '(с) Dream 2018' |
| quest.AAAAAAAAAAAAAAAAAAAFog.name | minor | formatting | Непоследовательная капитализация 'Броня из Сжатой Стали' - неправильное использование заглавных букв |
| quest.AAAAAAAAAAAAAAAAAAAFow.desc | minor | terminology | Модное имя 'Desh' переведено как 'дэш' в описании, но как 'деш' в названии - несогласованность; должно быть единообразно |
| quest.AAAAAAAAAAAAAAAAAAAFow.name | minor | terminology | Непоследовательность: 'деш' вместо единообразного 'дэш' или оставить английское Desh |
| quest.AAAAAAAAAAAAAAAAAAAFpA.name | minor | formatting | Непоследовательная капитализация 'Броня из Сжатого Титана' |
| quest.AAAAAAAAAAAAAAAAAAAFpg.desc | minor | fluency | 'накопал все нужные ресурсы, требуемые по квестам' - неловко и повторяемо; должно быть проще |
| quest.AAAAAAAAAAAAAAAAAAAFpg.name | minor | terminology | 'Dungeon' переведено как 'сокровищница' вместо более точного 'подземелья' |
| quest.AAAAAAAAAAAAAAAAAAAFvg.desc | minor | mistranslation | Опечатка: 'отправление' вместо 'отравление' (dispatch вместо poisoning). Нарушает ясность текста. |
| quest.AAAAAAAAAAAAAAAAAAAG1w.name | minor | mistranslation | 'Rad' означает 'крутой/потрясающий', а не 'красный'. 'Красная графика' - неправильный перевод. Должно быть 'Вау, крутая  |
| quest.AAAAAAAAAAAAAAAAAAAG2w.name | minor | mistranslation | 'Scrench' - портманто 'screwdriver' и 'wrench'. 'Мой маленький ключ' не передаёт этого. Лучше 'Мой маленький скрёнч' или |
| quest.AAAAAAAAAAAAAAAAAAAG4A.desc | minor | untranslated | 'Маст хэв!' - оставленный без перевода английский сленг. Должен быть переведён как 'Необходимо!' или 'Обязательно нужен! |
| quest.AAAAAAAAAAAAAAAAAAAG4w.name | minor | mistranslation | 'Mounting ваш HDD' - смешивание языков. Должно быть 'Монтирование вашего жёсткого диска' или 'Установка жёсткого диска'. |
| quest.AAAAAAAAAAAAAAAAAAAG5A.name | minor | mistranslation | 'базовый энергия показать' - неправильная грамматика и смешивание языков. Должно быть 'Базовый дисплей питания' или 'Про |
| quest.AAAAAAAAAAAAAAAAAAAG8w.desc | minor | fluency | Пропущена запятая после «ботинки» в начале предложения. Должно быть «Поршневые ботинки, это подпружиненная пара обуви» и |
| quest.AAAAAAAAAAAAAAAAAAAGAA.desc | minor | fluency | Фраза «падали навстречу смерти» звучит неестественно. Лучше: «падали и умирали» или просто «падали вниз». Также «Верхний |
| quest.AAAAAAAAAAAAAAAAAAAGBQ.name | minor | mistranslation | «Анализируй свои семена» неточно передаёт «Analyze Your Crops» — «crops» это культуры/растения в целом, а не только семе |
| quest.AAAAAAAAAAAAAAAAAAAGCg.name | minor | formatting | Цветовой код изменён с §2 (тёмно-зелёный) на §a (ярко-зелёный). Нужно восстановить исходный код §2§lРедкие руды |
| quest.AAAAAAAAAAAAAAAAAAAGEQ.name | minor | mistranslation | Detector Rail переведён как 'нажимные рельсы' (pressure rails), но это неправильно. Должно быть 'рельсы-детекторы' или ' |
| quest.AAAAAAAAAAAAAAAAAAAGNQ.name | minor | mistranslation | 'Wispy Cotton' неправильно переведено. 'Wispy' — воздушный, лёгкий, а не тонкий. Должно быть 'Воздушный хлопок' или 'Лёг |
| quest.AAAAAAAAAAAAAAAAAAAGPQ.name | minor | mistranslation | Неправильная грамматика и порядок слов. 'больше энергия Now!' — должно быть 'Больше энергии!' (или 'Больше мощности!').  |
| quest.AAAAAAAAAAAAAAAAAAAGPg.name | minor | formatting | Повреждено форматирование: '§6§lМстители, сбор!2' — цветовой код сохранен, но отсутствует пробел перед '2'. Должно быть  |
| quest.AAAAAAAAAAAAAAAAAAAGPw.name | minor | formatting | Повреждено форматирование цветового кода. Исходное '§5§l' (фиолетовый) заменено на '§2§l' (зелёный). Должно быть '§5§lУл |
| quest.AAAAAAAAAAAAAAAAAAAGTA.desc | minor | mistranslation | §o управления скрыты кодом форматирования - должно быть "...можно§r добывать..." |
| quest.AAAAAAAAAAAAAAAAAAAGTA.name | minor | formatting | Цвет изменён с §9§l (синий) на §5§l (фиолетовый) |
| quest.AAAAAAAAAAAAAAAAAAAGTg.name | minor | mistranslation | "Дегидратор" - неполный перевод. Должно быть "Химический дегидратор" |
| quest.AAAAAAAAAAAAAAAAAAAGTw.name | minor | formatting | Цвет изменён с §9§l (синий) на §5§l (фиолетовый) |
| quest.AAAAAAAAAAAAAAAAAAAGUQ.name | minor | formatting | Цвет изменён с §9§l (синий) на §5§l (фиолетовый) |
| quest.AAAAAAAAAAAAAAAAAAAGVA.name | minor | formatting | Цвет изменён с §9§l (синий) на §5§l (фиолетовый) |
| quest.AAAAAAAAAAAAAAAAAAAGVQ.name | minor | formatting | Цвет изменён с §c§l (красный) на §d§l (малиновый) |
| quest.AAAAAAAAAAAAAAAAAAAGVg.name | minor | formatting | Цвет изменён с §9§l (синий) на §5§l (фиолетовый) |
| quest.AAAAAAAAAAAAAAAAAAAGZA.name | minor | untranslated | Слово 'Desulfurizing' не переведено и остаётся в начале названия без капитализации |
| quest.AAAAAAAAAAAAAAAAAAAG_Q.name | minor | formatting | Цветовой код изменен с §3 (голубой) на §c (красный), что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAG_g.name | minor | formatting | Цветовой код изменен с §2 на §a, хотя оба зелёные, изменение форматирования не должно было быть |
| quest.AAAAAAAAAAAAAAAAAAAG_w.name | minor | formatting | Цветовой код изменен с §5 (фиолетовый) на §2 (зелёный), нарушено оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGaA.name | minor | terminology | Слово 'робота' неправильно использовано (означает работу/труд); должно быть 'работа с', 'имеющем дело с' или аналогичное |
| quest.AAAAAAAAAAAAAAAAAAAGcw.name | minor | fluency | Неловкая фраза 'путь чтобы пропутешествовать вниз' - должно быть более естественное выражение типа 'тёмный путь впереди' |
| quest.AAAAAAAAAAAAAAAAAAAGeQ.desc | minor | mistranslation | 'жидкость края' должна быть 'жидкий эндер' - неточная передача 'molten ender' |
| quest.AAAAAAAAAAAAAAAAAAAGhg.name | minor | formatting | Цветовой код изменен с §b на §9, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAGhw.name | minor | formatting | Цветовой код изменен с §b на §9, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAGiw.name | minor | formatting | Цветовой код изменен с §a на §8, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAGjA.name | minor | formatting | Цветовой код изменен с §a на §8, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAGlg.desc | minor | fluency | Ошибка в глаголе: 'когда ты продвинутся' должно быть 'когда ты продвинулся' или 'дошёл' - неправильная форма глагола |
| quest.AAAAAAAAAAAAAAAAAAAGmw.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGnA.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGnQ.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGng.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGnw.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGoA.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, и отсутствует предлог 'на' (должно быть 'на IV этапе') |
| quest.AAAAAAAAAAAAAAAAAAAGoQ.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGog.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGow.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGpA.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGpQ.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGpg.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGqA.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGqQ.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGqg.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGqw.name | minor | formatting | Цветовой код изменен с §b§l на §9§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGrA.name | minor | formatting | Цветовой код изменен с §c§l на §d§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGrQ.name | minor | formatting | Цветовой код изменен с §c§l на §d§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGrg.name | minor | formatting | Цветовой код изменен с §c§l на §d§l, что нарушает оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAGsQ.desc | minor | mistranslation | «использовать её» неправильно - её относится к СоС (женский род в русском), но контекст требует «их» или переструктуриро |
| quest.AAAAAAAAAAAAAAAAAAAGxQ.desc | minor | fluency | Опечатка в тексте 'Он этом' вместо 'Об этом' |
| quest.AAAAAAAAAAAAAAAAAAAH1A.name | minor | untranslated | 'Inventory Relay' должно быть переведено как 'Реле инвентаря'. 'продвинутый' требует капитализации 'Продвинутое'. |
| quest.AAAAAAAAAAAAAAAAAAAH4A.name | minor | terminology | Неудачный перевод названия: 'блок Gate' звучит неловко, должно быть 'Врата блоков' или подобное |
| quest.AAAAAAAAAAAAAAAAAAAH4Q.name | minor | terminology | 'блок Detector' неловко, должно быть 'Детектор блоков' |
| quest.AAAAAAAAAAAAAAAAAAAH4g.name | minor | formatting | Цветовой код изменён: §a на §8, что меняет оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAH4w.name | minor | terminology | 'базовый SFM' неполный перевод названия, должно быть 'Основы SFM' |
| quest.AAAAAAAAAAAAAAAAAAAH5w.name | minor | formatting | Цветовой код изменён: §a на §8, что меняет оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAH6A.name | minor | formatting | Цветовой код изменён: §c на §d, что меняет оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAH6g.name | minor | formatting | Цветовой код изменён: §3 на §c, что меняет оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAH7A.name | minor | formatting | Цветовой код добавлен (§8§l), хотя в оригинале его нет |
| quest.AAAAAAAAAAAAAAAAAAAH7Q.name | minor | formatting | Цветовой код добавлен (§d§l), хотя в оригинале его нет |
| quest.AAAAAAAAAAAAAAAAAAAH7g.name | minor | formatting | Цветовой код добавлен (§9§l), хотя в оригинале его нет |
| quest.AAAAAAAAAAAAAAAAAAAH7w.name | minor | formatting | Цветовой код добавлен (§9§l), хотя в оригинале его нет |
| quest.AAAAAAAAAAAAAAAAAAAH8A.name | minor | formatting | Цветовой код добавлен (§9§l), хотя в оригинале его нет |
| quest.AAAAAAAAAAAAAAAAAAAH8g.name | minor | formatting | Цветовой код добавлен (§9§l), хотя в оригинале его нет |
| quest.AAAAAAAAAAAAAAAAAAAH8w.name | minor | formatting | Цветовой код добавлен (§9§l), хотя в оригинале его нет |
| quest.AAAAAAAAAAAAAAAAAAAH9w.desc | minor | fluency | 'закрытия всех потребностей в упаковке' звучит неловко, лучше 'удовлетворения всех потребностей' |
| quest.AAAAAAAAAAAAAAAAAAAH9w.name | minor | fluency | Грамматическая ошибка: 'тобою' архаично, 'гордился' неправильно согласовано; должно быть 'был бы тобой горд' или 'гордил |
| quest.AAAAAAAAAAAAAAAAAAAHAA.desc | minor | fluency | 'залей их в принтер' неточно; должно быть 'залей их в емкость принтера'; 'жилах' неправильно использовано |
| quest.AAAAAAAAAAAAAAAAAAAHAg.desc | minor | fluency | 'жёрдочки' диалектно; 'паразитирует' пишется с 'з'; общая структура запутанна |
| quest.AAAAAAAAAAAAAAAAAAAHBA.name | minor | formatting | Цвет изменён с §5 на §2, что не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAAHEA.desc | minor | formatting | Опечатка в слове 'Foresrty' вместо 'Forestry'. Повреждено форматирование/имя мода. |
| quest.AAAAAAAAAAAAAAAAAAAHEg.desc | minor | fluency | Опечатка/грамматическая ошибка: 'как та уже сам' вместо 'как ты уже сам'. |
| quest.AAAAAAAAAAAAAAAAAAAHEw.name | minor | formatting | Цветовой код изменён: §9 (синий) на §5 (фиолетовый). Должен быть сохранён оригинальный код. |
| quest.AAAAAAAAAAAAAAAAAAAHFA.name | minor | formatting | Цветовой код изменён: §9 (синий) на §5 (фиолетовый). |
| quest.AAAAAAAAAAAAAAAAAAAHFQ.name | minor | formatting | Цветовой код изменён: §9 (синий) на §5 (фиолетовый). |
| quest.AAAAAAAAAAAAAAAAAAAHFg.name | minor | formatting | Цветовой код изменён: §9 (синий) на §5 (фиолетовый). |
| quest.AAAAAAAAAAAAAAAAAAAHFw.name | minor | formatting | Цветовой код изменён: §9 (синий) на §5 (фиолетовый). |
| quest.AAAAAAAAAAAAAAAAAAAHHQ.name | minor | formatting | Цветовой код изменён: §5 (фиолетовый) на §2 (тёмно-зелёный). |
| quest.AAAAAAAAAAAAAAAAAAAHHg.desc | minor | mistranslation | Наименование мода: 'TechTech' вместо 'TecTech'. Также 'Manual Dynamo' переведено как 'ручной трансформатор' - несоответс |
| quest.AAAAAAAAAAAAAAAAAAAHIA.name | minor | formatting | Цветовой код изменён: §9 (синий) на §5 (фиолетовый). |
| quest.AAAAAAAAAAAAAAAAAAAHIw.desc | minor | fluency | Грамматическая ошибка: 'больше выход' - некорректный синтаксис. Должно быть 'больше выходной мощности' или подобное. |
| quest.AAAAAAAAAAAAAAAAAAAHJQ.desc | minor | mistranslation | «нажми крестик» неправильно передаёт смысл «check the box» (отметь флажок); отсутствует уточнение к слову «корпусов» (LE |
| quest.AAAAAAAAAAAAAAAAAAAHJg.desc | minor | mistranslation | «ткнуть на крестик» неправильно передаёт «check the box» (отметить флажок); фраза очень неформальна и некорректна |
| quest.AAAAAAAAAAAAAAAAAAAHJw.name | minor | formatting | Цветовой код изменён с §2 на §a без оснований (также этап §n неуместен); оригинал использует §2§l |
| quest.AAAAAAAAAAAAAAAAAAAHKQ.desc | minor | terminology | «энерговвода» неправильное или опечатка; должно быть что-то вроде «энергохода» или «энерговвода» |
| quest.AAAAAAAAAAAAAAAAAAAHOw.name | minor | formatting | Коды цвета изменены: §2 на §a (оба зелёные, но разные оттенки) |
| quest.AAAAAAAAAAAAAAAAAAAHPA.name | minor | formatting | Коды цвета изменены: §2 на §a (оба зелёные, но разные оттенки) |
| quest.AAAAAAAAAAAAAAAAAAAHQg.name | minor | formatting | Цветовой код изменён с §9 (светлый синий) на §5 (пурпурный), что нарушает исходное форматирование текста. |
| quest.AAAAAAAAAAAAAAAAAAAHRw.name | minor | formatting | Цветовой код изменён с §5 (пурпурный) на §2 (тёмный зелёный), что нарушает исходное форматирование. |
| quest.AAAAAAAAAAAAAAAAAAAHSA.name | minor | formatting | Цветовой код изменён с §2 на §a (оба - зелёные, но разных оттенков), что нарушает точное форматирование исходного текста |
| quest.AAAAAAAAAAAAAAAAAAAHSQ.name | minor | formatting | Цветовой код изменён с §5 (пурпурный) на §2 (тёмный зелёный), нарушая исходное форматирование. |
| quest.AAAAAAAAAAAAAAAAAAAHSg.name | minor | formatting | Цветовой код изменён с §2 на §a, нарушая точное форматирование исходного текста. |
| quest.AAAAAAAAAAAAAAAAAAAHUg.desc | minor | terminology | Фраза 'подложек печатных плат' неловка и искажает смысл 'plastic circuit boards' — должно быть 'пластиковые печатные пла |
| quest.AAAAAAAAAAAAAAAAAAAHUw.name | minor | mistranslation | Фраза 'A Soul-ution For Warp' — это каламбур, но главное 'warp' здесь означает искажение/порчу, а не 'искажение' в общем |
| quest.AAAAAAAAAAAAAAAAAAAHVA.desc | minor | terminology | 'UU-Amplifier' переведён как 'катализатор материи', что неточно для технического мода — нужна более буквальная передача  |
| quest.AAAAAAAAAAAAAAAAAAAHXw.desc | minor | mistranslation | Добавлена фраза 'или паровая' которой нет в оригинале; искажает смысл исходного туманного описания |
| quest.AAAAAAAAAAAAAAAAAAAHYg.desc | minor | terminology | Фраза 'IV Сборочная машина необходима' грамматически неловка; следует 'Для этого требуется сборочная машина IV уровня' и |
| quest.AAAAAAAAAAAAAAAAAAAHbg.name | minor | mistranslation | Неправильный цвет: источник говорит '§a§l' (зеленый), а перевод содержит '§8§l' (серый). Названию должна соответствовать |
| quest.AAAAAAAAAAAAAAAAAAAHbw.name | minor | mistranslation | Неправильный цвет: источник '§9§l' (синий), перевод '§5§l' (пурпурный). Цветовые коды должны совпадать. |
| quest.AAAAAAAAAAAAAAAAAAAHcg.desc | minor | mistranslation | Неточный перевод. Текст 'катализатора материи' неправильный - в оригинале это 'UU-Amplifier to make UU-Matter'. Также '1 |
| quest.AAAAAAAAAAAAAAAAAAAHcg.name | minor | mistranslation | Неправильный цвет: источник '§9§l' (синий), перевод '§5§l' (пурпурный). |
| quest.AAAAAAAAAAAAAAAAAAAHcw.desc | minor | fluency | Начало фразы 'Или на 4 млн?' не имеет смысла без контекста. Должно быть 'А может на 4 млн?' или аналогичное. Текст обрыв |
| quest.AAAAAAAAAAAAAAAAAAAHdA.desc | minor | mistranslation | Неточный перевод. Оригинал говорит о 'Blast Furnaces', а перевод просто 'железные печки'. 'Nether dust' - 'пыль адского  |
| quest.AAAAAAAAAAAAAAAAAAAHdA.name | minor | mistranslation | Неправильный цвет: источник '§3§l' (бирюзовый), перевод '§c§l' (красный). |
| quest.AAAAAAAAAAAAAAAAAAAHdQ.name | minor | mistranslation | Неправильный цвет: источник '§9§l' (синий), перевод '§5§l' (пурпурный). |
| quest.AAAAAAAAAAAAAAAAAAAHdw.desc | minor | mistranslation | Неточный перевод. '192к' должно быть '192k' (буква k латиница, как в оригинале). Также структура фразы немного неловкая. |
| quest.AAAAAAAAAAAAAAAAAAAHdw.name | minor | mistranslation | Неправильный цвет: источник '§5§l' (фиолетовый), перевод '§2§l' (зеленый). |
| quest.AAAAAAAAAAAAAAAAAAAHeg.desc | minor | mistranslation | 'Нет' обрезано в начале. 'Взамен чутка изумрудов' - странное употребление 'чутка'. 'LootBag' оставлен без перевода. Пунк |
| quest.AAAAAAAAAAAAAAAAAAAHew.name | minor | mistranslation | Неправильный цвет: источник '§3§l' (бирюзовый), перевод '§c§l' (красный). Также 'маску для лица' - странный выбор слова  |
| quest.AAAAAAAAAAAAAAAAAAAHnw.desc | minor | fluency | Неясное объяснение роли рудных ягод. Оригинал говорит о них как о сырье для выращивания, а перевод звучит так, будто яго |
| quest.AAAAAAAAAAAAAAAAAAAHqA.desc | minor | register | Неправильно выбран регистр. 'ты хочешь' (неформальное обращение) не соответствует остальному тексту; нужно либо 'ты хоче |
| quest.AAAAAAAAAAAAAAAAAAAHqQ.desc | minor | register | Смешивание форм обращения: 'тебе', 'сделай', 'ты' - неправильно выбран уровень формальности. Должна быть единообразная ф |
| quest.AAAAAAAAAAAAAAAAAAAHsA.desc | minor | terminology | 'Прикольно' - сленговое выражение, не подходит для технического описания. Лучше 'красивые', 'декоративные' или 'элегантн |
| quest.AAAAAAAAAAAAAAAAAAAHsA.name | minor | terminology | 'Прикольная древесина' - сленг, не профессиональный перевод. Должно быть 'Красивая древесина', 'Элегантная древесина' ил |
| quest.AAAAAAAAAAAAAAAAAAAHsw.desc | minor | terminology | 'Прикольно выглядящие фонари' - сленг вместо профессионального тона. Плюс 'обычного или пчелиного воска' - грамматически |
| quest.AAAAAAAAAAAAAAAAAAAHsw.name | minor | terminology | 'Прикольные фонари' - сленг. Должно быть 'Элегантные фонари', 'Красивые фонари' или 'Декоративные фонари'. |
| quest.AAAAAAAAAAAAAAAAAAAHtQ.desc | minor | mistranslation | Неправильный перевод: 'Обычным версиям ламп нужен сигнал красного камня для включения. Инверторным лампам наоборот, сигн |
| quest.AAAAAAAAAAAAAAAAAAAHtg.desc | minor | terminology | 'прикольных ламп' - сленг вместо 'изощренных', 'сложных' или 'декоративных'. |
| quest.AAAAAAAAAAAAAAAAAAAHtg.name | minor | terminology | 'Прикольное' - сленг. Должно быть 'Изощренное', 'Сложное' или 'Декоративное' освещение. |
| quest.AAAAAAAAAAAAAAAAAAAHww.name | minor | formatting | Коды цвета изменены: §3§l (голубой+полужирный) переведены как §c§l (красный+полужирный), что нарушает исходный стиль офо |
| quest.AAAAAAAAAAAAAAAAAAAHxA.name | minor | formatting | Коды цвета изменены: §3§l (голубой+полужирный) переведены как §c§l (красный+полужирный), что нарушает исходный стиль офо |
| quest.AAAAAAAAAAAAAAAAAAAHxQ.name | minor | formatting | Первое слово 'машина' не капитализировано; должно быть 'Машина Inventory Manager' или полностью переведено |
| quest.AAAAAAAAAAAAAAAAAAAI-A.name | minor | formatting | Коды цвета изменены: §a§l (зелёный+полужирный) переведены как §8§l (тёмно-серый+полужирный), что нарушает исходный стиль |
| quest.AAAAAAAAAAAAAAAAAAAI9w.name | minor | formatting | Неправильный цветовой код: в источнике §9 (синий), в переводе §5 (фиолетовый) |
| quest.AAAAAAAAAAAAAAAAAAAIBQ.name | minor | formatting | В переводе добавлены цветовые коды (§9§l), которых нет в исходном тексте |
| quest.AAAAAAAAAAAAAAAAAAAIBg.name | minor | formatting | В переводе добавлены цветовые коды (§b§l), которых нет в исходном тексте |
| quest.AAAAAAAAAAAAAAAAAAAICA.name | minor | formatting | Неправильный цветовой код: в источнике §3 (голубой), в переводе §c (красный) |
| quest.AAAAAAAAAAAAAAAAAAAICw.desc | minor | mistranslation | "Можно добыть из гоблинов-рыцарей" неточен - источник говорит о крепостях, а не о самих гоблинах |
| quest.AAAAAAAAAAAAAAAAAAAIDQ.desc | minor | register | "Чутка увеличивает" - слишком разговорный слэнг для технического описания; должен быть более формальный тон |
| quest.AAAAAAAAAAAAAAAAAAAIFw.name | minor | formatting | Изменён код цвета с §c на §d - должен быть §c§l по исходному тексту. |
| quest.AAAAAAAAAAAAAAAAAAAIJw.name | minor | formatting | Неправильный цветовой код §c вместо §3 - должен соответствовать оригиналу |
| quest.AAAAAAAAAAAAAAAAAAAIOA.desc | minor | untranslated | Слова 'various' и 'supplies' оставлены непереведёнными, должны быть 'различные инструменты' и 'материалы' |
| quest.AAAAAAAAAAAAAAAAAAAIOA.name | minor | fluency | Отсутствует заглавная буква в начале 'инструменты', правильно 'Инструменты для генетика' |
| quest.AAAAAAAAAAAAAAAAAAAIQA.name | minor | mistranslation | Title is awkwardly worded; original is direct statement, Russian version adds unnecessary phrasing 'с рюкзаком нам ничег |
| quest.AAAAAAAAAAAAAAAAAAAIQQ.desc | minor | terminology | Inconsistent terminology: 'ночное зрение это отличная функция в ранце' should use 'способность' not 'функция'; also shou |
| quest.AAAAAAAAAAAAAAAAAAAIQg.desc | minor | mistranslation | Significant meaning shift: 'если ты любишь исследовать морские глубины' (if you like to explore sea depths) changes 'if  |
| quest.AAAAAAAAAAAAAAAAAAAIRA.desc | minor | fluency | Sentence structure issues: 'Кошачий рюкзак будет отпугивать криперов. Отличная защита против криперов-утопцев Но не подх |
| quest.AAAAAAAAAAAAAAAAAAAIRg.desc | minor | mistranslation | Awkward phrasing: 'требует яйцо дракона' should be 'требует яйцо дракона для крафта' is redundant since that's already s |
| quest.AAAAAAAAAAAAAAAAAAAISQ.desc | minor | terminology | Inconsistent terminology: 'обычных садовых ножей из Forestry' (common garden scissors) is imprecise; should be 'графтеро |
| quest.AAAAAAAAAAAAAAAAAAAITA.desc | minor | terminology | Terminology issues: 'Липа пушистая' is incorrect - 'Silver Lime' is not 'fuzzy linden'; should be more literal or check  |
| quest.AAAAAAAAAAAAAAAAAAAITA.name | minor | terminology | Tree name translation: 'Липа пушистая' is questionable - verify against Forestry mod database. Likely should be simplifi |
| quest.AAAAAAAAAAAAAAAAAAAITw.desc | minor | terminology | Attribute terminology: '"Быстрая зрелость"' should use consistent term for in-game attribute; verify if Russian mod comm |
| quest.AAAAAAAAAAAAAAAAAAAIUQ.desc | minor | mistranslation | Term error: 'Мировая лиственница' (World Larch) is incorrect - 'Mundane' means ordinary/common, not 'world'. Should be ' |
| quest.AAAAAAAAAAAAAAAAAAAIUQ.name | minor | mistranslation | Tree name mistranslation: 'Мировая лиственница' should be 'Обычная лиственница' or 'Простая лиственница' (Mundane = ordi |
| quest.AAAAAAAAAAAAAAAAAAAIUg.desc | minor | terminology | Tree name consistency: 'Жёлтая сосна' (Yellow Pine) - verify this is correct for 'Bull Pine' in Forestry mod. Also verif |
| quest.AAAAAAAAAAAAAAAAAAAIUg.name | minor | terminology | Tree name verification needed: 'Жёлтая сосна' for 'Bull Pine' needs confirmation against Forestry mod terminology databa |
| quest.AAAAAAAAAAAAAAAAAAAIUw.desc | minor | fluency | Grammar error: 'Вывед его скрестив' is incorrect - should be 'Выведи его скрестив' (imperative mood agreement). Also 'фр |
| quest.AAAAAAAAAAAAAAAAAAAIVA.desc | minor | fluency | Неверное согласование рода: 'Он имеет' должно быть 'Она имеет' (Слива - женский род) |
| quest.AAAAAAAAAAAAAAAAAAAIVg.desc | minor | formatting | Пропущена запятая или тире: 'Кокоболо красивое' должно быть 'Кокоболо — красивое' |
| quest.AAAAAAAAAAAAAAAAAAAIXA.desc | minor | mistranslation | Фраза 'crazy like a fox' полностью потеряна - переведена как 'Или гений?' вместо сохранения смысла идиомы |
| quest.AAAAAAAAAAAAAAAAAAAIXA.name | minor | formatting | Код цвета изменён: §3 (синий) заменён на §c (красный) - повреждено форматирование |
| quest.AAAAAAAAAAAAAAAAAAAIXg.name | minor | formatting | Код цвета изменён: §5 (фиолетовый) заменён на §2 (зелёный) - повреждено форматирование |
| quest.AAAAAAAAAAAAAAAAAAAIXw.name | minor | formatting | Код цвета изменён: §5 (фиолетовый) заменён на §2 (зелёный) - повреждено форматирование |
| quest.AAAAAAAAAAAAAAAAAAAIZQ.desc | minor | mistranslation | "IV тира" - неправильная грамматика. Должно быть "IV уровня" или "IV tier". "до 100 млн EU" - странная единица измерения |
| quest.AAAAAAAAAAAAAAAAAAAI_A.name | minor | formatting | Colour code изменён с §a (зелёный) на §8 (тёмный серый) - нарушена исходная форматирование и читаемость. |
| quest.AAAAAAAAAAAAAAAAAAAI_Q.name | minor | formatting | Colour code изменён с §a (зелёный) на §8 (тёмный серый) - нарушена форматирование. |
| quest.AAAAAAAAAAAAAAAAAAAI_g.name | minor | formatting | Colour code изменён с §a (зелёный) на §8 (тёмный серый) - нарушена форматирование. |
| quest.AAAAAAAAAAAAAAAAAAAI_w.name | minor | formatting | Colour code изменён с §b (голубой) на §9 (тёмный голубой) - нарушена форматирование. |
| quest.AAAAAAAAAAAAAAAAAAAIbQ.desc | minor | mistranslation | "Breed them with Diligent and Cultivated" переведено как "Выведи их из", что неточно. Более правильный перевод: "Выведи  |
| quest.AAAAAAAAAAAAAAAAAAAIbg.desc | minor | mistranslation | "Прорастающие пчёлы" - неудачный выбор слова. Оригинал "Growing" в контексте разведения означает развивающиеся, а не про |
| quest.AAAAAAAAAAAAAAAAAAAIcQ.name | minor | formatting | Цветовой код изменён с §3 (голубой) на §c (красный), что нарушает исходное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAIsQ.name | minor | terminology | 'Солим' неправильный перевод Solum; должно быть 'Солум' или другой подходящий вариант |
| quest.AAAAAAAAAAAAAAAAAAAIvg.name | minor | mistranslation | "Таум-металл" неточен для 'Thaumium Dust' (Thaumium - эссенция/материал, не просто металл, и это пыль). Должно быть 'Тау |
| quest.AAAAAAAAAAAAAAAAAAAIwA.name | minor | terminology | "Паучая" - неправильный род, должно быть "Паучья" (со склонением); также грамматически некорректно согласование с сущест |
| quest.AAAAAAAAAAAAAAAAAAAJ4w.name | minor | fluency | Фраза 'Форматирование газа, то есть эссенции' неловкая; лучше 'Форматирование газовых ячеек, эссенция' или оставить близ |
| quest.AAAAAAAAAAAAAAAAAAAJ6A.desc | minor | fluency | Опечатка: 'подключить одно из 4 Квантовых колец к Сети помощью' - должно быть 'при помощи', а не 'помощью'. |
| quest.AAAAAAAAAAAAAAAAAAAJ6Q.desc | minor | fluency | Опечатка: 'при открытом интерфейса' - нарушение согласования падежей, должно быть 'при открытом интерфейсе'. |
| quest.AAAAAAAAAAAAAAAAAAAJ6g.desc | minor | fluency | Опечатка: 'при открытом интерфейса' - должно быть 'при открытом интерфейсе'. |
| quest.AAAAAAAAAAAAAAAAAAAJ8w.name | minor | register | 'штук' — слишком разговорное; лучше 'Автокрафт магических предметов' или 'Создание магических предметов' |
| quest.AAAAAAAAAAAAAAAAAAAJMQ.name | minor | fluency | Начинается со строчной буквы 'найти' вместо прописной; 'в End' неловко звучит, лучше 'в Краю' |
| quest.AAAAAAAAAAAAAAAAAAAJNQ.name | minor | terminology | Неправильное согласование рода: 'энергия жезл' (женский род + мужской род); должно быть 'Жезл энергии' или 'Энергетическ |
| quest.AAAAAAAAAAAAAAAAAAAJPg.name | minor | mixed_language | Смешана русская и английская речь; слово 'продвинутый' должно быть с прописной буквы; должно быть 'Продвинутое улучшение |
| quest.AAAAAAAAAAAAAAAAAAAJQQ.name | minor | mixed_language | Смешана русская и английская речь: 'горячий Puzzle' должно быть полностью на русском или полностью на английском |
| quest.AAAAAAAAAAAAAAAAAAAJRQ.name | minor | untranslated | Частично переведено: 'Silverfish кровь' - правильно на русском будет 'Кровь Серебрянки' или оставить 'Silverfish Blood' |
| quest.AAAAAAAAAAAAAAAAAAAJTg.name | minor | untranslated | Частично переведено: 'Infused алтарь' - смешана английская и русская части, нужна либо полная локализация, либо полность |
| quest.AAAAAAAAAAAAAAAAAAAJVQ.name | minor | formatting | Неправильный код цвета: используется §c вместо §3 |
| quest.AAAAAAAAAAAAAAAAAAAJVg.name | minor | formatting | Неправильный код цвета: используется §8 вместо §a |
| quest.AAAAAAAAAAAAAAAAAAAJVw.name | minor | formatting | Неправильный код цвета: используется §8 вместо §a |
| quest.AAAAAAAAAAAAAAAAAAAJWQ.name | minor | formatting | Неправильный код цвета: используется §2 вместо §5 |
| quest.AAAAAAAAAAAAAAAAAAAJXg.name | minor | formatting | Цветовой код изменён с §9 на §5, повреждено оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAJXw.name | minor | formatting | Цветовой код изменён с §3 на §c, повреждено оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAJYg.name | minor | formatting | Цветовой код изменён с §2 на §a, повреждено оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAJYw.name | minor | formatting | Цветовой код изменён с §5 на §2, повреждено оригинальное форматирование |
| quest.AAAAAAAAAAAAAAAAAAAJZw.name | minor | formatting | §3 (синий цвет) изменён на §c (красный цвет) в переводе - цветовой код не соответствует оригиналу |
| quest.AAAAAAAAAAAAAAAAAAAJaA.name | minor | formatting | §9 (голубой) изменён на §5 (пурпурный) - цветовой код не соответствует оригиналу |
| quest.AAAAAAAAAAAAAAAAAAAJbQ.name | minor | mistranslation | Потеряны артикль и предлог: 'Darkness Choice' вместо 'Darkness of Choice'. Форматирование повреждено и выглядит неправил |
| quest.AAAAAAAAAAAAAAAAAAAJdw.name | minor | fluency | Неправильная грамматика: 'является лучший' должно быть 'лучшей наукой'. Английские слова 'Mad Science' оставлены untrans |
| quest.AAAAAAAAAAAAAAAAAAAJeA.name | minor | fluency | Начинается со строчной буквы 'наконец'. Английские слова 'Binding Familiar' untranslated в заголовке. |
| quest.AAAAAAAAAAAAAAAAAAAJmA.name | minor | mistranslation | 'Demon кровь Shards' — неправильное смешение языков. Должно быть 'Осколки крови демона' или 'Демонические осколки крови' |
| quest.AAAAAAAAAAAAAAAAAAAJmQ.name | minor | mistranslation | 'Starter клавиша' неправильно. 'Starter Key' в контексте ритуалов — 'Ключ запуска' или 'Пусковой ключ'. |
| quest.AAAAAAAAAAAAAAAAAAAJmw.name | minor | terminology | 'Сигилы 5 тира' — неправильное использование слова 'тира'. Должно быть 'Сигилы 5-го уровня' или 'Сигилы уровня 5'. |
| quest.AAAAAAAAAAAAAAAAAAAJng.desc | minor | mistranslation | 'использовать этот к quickly dismantle ritual' — смешение языков и неправильная грамматика. Должно быть 'Используй это,  |
| quest.AAAAAAAAAAAAAAAAAAAJoA.desc | minor | mistranslation | Перевод неполный. 'Работают так же, как предыдущие, но вмещают больше' пропускает важную часть 'once you make it into so |
| quest.AAAAAAAAAAAAAAAAAAAJpw.desc | minor | fluency | Смешение форм обращения: 'тебе нужно больше хранилища, используйте'. Нужна единообразная форма вежливости либо 'тебе'/'и |
| quest.AAAAAAAAAAAAAAAAAAAJqA.desc | minor | mistranslation | '262144 байта вычислительной мощности' неправильно. 'Bytes of storage' — это объем хранилища, не мощность. Должно быть ' |
| quest.AAAAAAAAAAAAAAAAAAAJqQ.desc | minor | mistranslation | '1048576 байта вычислительной мощности' — той же ошибки как JqA. Должно быть 'байта памяти для создания' или 'байта хран |
| quest.AAAAAAAAAAAAAAAAAAAJqg.desc | minor | mistranslation | '4194304 байта вычислительной мощности' — той же ошибки. Должно быть 'байта памяти для создания' или 'байта хранилища дл |
| quest.AAAAAAAAAAAAAAAAAAAJqw.desc | minor | mistranslation | '16777216 байта вычислительной мощности' — той же ошибки. Должно быть 'байта памяти для создания' или 'байта хранилища д |
| quest.AAAAAAAAAAAAAAAAAAAJrg.name | minor | terminology | "жидкостный компонент хранения" лучше как "компонент хранения жидкости" |
| quest.AAAAAAAAAAAAAAAAAAAJrw.name | minor | terminology | "жидкостный компонент хранения" лучше как "компонент хранения жидкости" |
| quest.AAAAAAAAAAAAAAAAAAAJsA.name | minor | terminology | "жидкостный компонент хранения" лучше как "компонент хранения жидкости" |
| quest.AAAAAAAAAAAAAAAAAAAJsQ.name | minor | terminology | "жидкостный компонент хранения" лучше как "компонент хранения жидкости" |
| quest.AAAAAAAAAAAAAAAAAAAJwA.desc | minor | fluency | "Предназначен для создания ячеек" звучит неловко; лучше "Это корпус для создания ячеек хранения эссенции" |
| quest.AAAAAAAAAAAAAAAAAAAJxQ.desc | minor | fluency | Дублирование слова «сделать сделать» вместо одного; неправильное использование слова «тира» (должно быть «уровня»); проб |
| quest.AAAAAAAAAAAAAAAAAAAKIQ.name | minor | mistranslation | Неполный перевод: 'Welcome к Hell!' - английское слово 'Welcome' не переведено. Должно быть 'Добро пожаловать в Ад!' или |
| quest.AAAAAAAAAAAAAAAAAAAKIg.desc | minor | mistranslation | Неточный перевод смысла: исходный текст говорит 'may not actually store any energy but it'll still be useful' (может не  |
| quest.AAAAAAAAAAAAAAAAAAAKLA.name | minor | formatting | Неправильный код цвета - §c§l (красный) заменён на §d§l (пурпурный) |
| quest.AAAAAAAAAAAAAAAAAAAKLQ.name | minor | formatting | Неправильный код цвета - §c§l (красный) заменён на §d§l (пурпурный) |
| quest.AAAAAAAAAAAAAAAAAAAKLg.name | minor | formatting | Неправильный код цвета - §c§l (красный) заменён на §d§l (пурпурный) |
| quest.AAAAAAAAAAAAAAAAAAAKLw.name | minor | formatting | Неправильный код цвета - §c§l (красный) заменён на §d§l (пурпурный) |
| quest.AAAAAAAAAAAAAAAAAAAKMA.name | minor | formatting | Неправильный код цвета - §c§l (красный) заменён на §d§l (пурпурный) |
| quest.AAAAAAAAAAAAAAAAAAAKMQ.name | minor | other | Опечатка: 'Таинственнный' вместо 'Таинственный' (лишняя буква н) |
| quest.AAAAAAAAAAAAAAAAAAAKSw.name | minor | untranslated | Assemble! осталось на английском языке |
| quest.AAAAAAAAAAAAAAAAAAAKTA.name | minor | untranslated | Assembling остался на английском языке в заголовке |
| quest.AAAAAAAAAAAAAAAAAAAKWA.name | minor | untranslated | Frontier остался на английском языке, ошибка в капитализации (финальный) |
| quest.AAAAAAAAAAAAAAAAAAAKXA.name | minor | untranslated | Английское слово 'Intelligent' оставлено нетранслированным; должно быть 'Интеллектуальные схемы' |
| quest.AAAAAAAAAAAAAAAAAAAKXw.name | minor | untranslated | 'Supercomputers' не переведено; должно быть 'Суперкомпьютеры' |
| quest.AAAAAAAAAAAAAAAAAAAKZA.name | minor | mistranslation | 'Mutations' не переведено; 'хороший' должно быть 'хорошие' (соответствие по роду и числу) |
| quest.AAAAAAAAAAAAAAAAAAAKZQ.name | minor | untranslated | 'Self-Aware' не переведено; должно быть 'Самосознающие' или аналогично |
| quest.AAAAAAAAAAAAAAAAAAAKZg.name | minor | untranslated | 'Please' и 'Over' не переведены; неловкое смешивание англ. и русск. частей фразы |
| quest.AAAAAAAAAAAAAAAAAAAKZw.desc | minor | mistranslation | Ошибка числа: 'второй Bio схема' должно быть 'вторая Bio схема' или с согласованием 'вторая схема' |
| quest.AAAAAAAAAAAAAAAAAAAKZw.name | minor | untranslated | 'Bio' и 'Biological Boogaloo' не переведены |
| quest.AAAAAAAAAAAAAAAAAAAKaA.desc | minor | mistranslation | 'third' не переведено; множественное число не согласовано: 'третья Bio схема' (должно быть согласованным или 'три схемы' |
| quest.AAAAAAAAAAAAAAAAAAAKaA.name | minor | mistranslation | 'Supercomputers' не переведено; неправильный падеж 'с ячейки' (должно быть 'с клетками') |
| quest.AAAAAAAAAAAAAAAAAAAKaQ.name | minor | untranslated | 'Master' не переведено; должно быть 'Мастер' с правильным падежом |
| quest.AAAAAAAAAAAAAAAAAAAKdQ.desc | minor | mistranslation | 'Auto Maintenance Hatch' неправильно переведено как 'Полу-автоматический люк'. Должно быть 'Автоматический люк обслужива |
| quest.AAAAAAAAAAAAAAAAAAAKgA.desc | minor | formatting | Первый символ в слове 'Смешай' - неправильный символ (выглядит как машинные артефакты), требуется исправление на обычный |
| quest.AAAAAAAAAAAAAAAAAAAKlQ.desc | minor | fluency | 'солнечным системам' - грамматическая ошибка, должно быть 'солнечных систем'; 'крутые ускорители' - сленговое/неформальн |
| quest.AAAAAAAAAAAAAAAAAAAKng.name | minor | mistranslation | Потеря важного смысла - пропущено 'Even', что меняет тон вопроса. Перевод неполный. |
| quest.AAAAAAAAAAAAAAAAAAAKrg.desc | minor | formatting | Двойная точка в конце (8.1 трлн EU..) и добавлено "и выше" которого нет в исходном тексте |
| quest.AAAAAAAAAAAAAAAAAAAKrw.desc | minor | formatting | Двойная точка в конце (81 трлн EU..) и добавлено "и выше" которого нет в исходном тексте |
| quest.AAAAAAAAAAAAAAAAAAAKuw.name | minor | formatting | Потеряны форматирующие токены §oyawn§r в названии |
| quest.AAAAAAAAAAAAAAAAAAAKyA.name | minor | fluency | Неправильный порядок слов и грамматика: 'что даже является этот?' должно быть 'Что это вообще?' или 'Что здесь происходи |
| quest.AAAAAAAAAAAAAAAAAAAL0Q.name | minor | mistranslation | Смешение английского и русского - должно быть полностью переведено на русский |
| quest.AAAAAAAAAAAAAAAAAAAL1A.name | minor | mistranslation | Смешение английского и русского - 'Hyperheated' не переведено |
| quest.AAAAAAAAAAAAAAAAAAAL4g.desc | minor | formatting | Опечатка: 'не получишь ничего не выходе' → должно быть 'не получишь ничего на выходе' |
| quest.AAAAAAAAAAAAAAAAAAAL4w.name | minor | formatting | Код цвета повреждён: §b должен быть §b, но переведено как §9 |
| quest.AAAAAAAAAAAAAAAAAAAL5Q.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL5g.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL5w.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL6A.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL6Q.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL6g.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL6w.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL7A.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL7Q.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL7g.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL7w.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL8A.desc | minor | terminology | 'кек' - интернет-сленг, неподходящий в техническом контексте; должно быть 'осадок' или 'шлам' |
| quest.AAAAAAAAAAAAAAAAAAAL8A.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL8Q.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL8g.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL8w.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL9A.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL9Q.desc | minor | mistranslation | 'do get' (усиление) переведено как 'надеюсь' (надежда) - неправильное значение |
| quest.AAAAAAAAAAAAAAAAAAAL9Q.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL9g.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAAL9w.name | minor | formatting | Код цвета повреждён: §b → §9 |
| quest.AAAAAAAAAAAAAAAAAAALDg.name | minor | formatting | Неправильный цветовой код: исходник использует §b (синий), а перевод использует §9 (тёмный синий). Форматирующие токены  |
| quest.AAAAAAAAAAAAAAAAAAALKQ.name | minor | mistranslation | Пропущено слово 'Glass' из названия; должно быть что-то типа 'Магическое зеркальное стекло' |
| quest.AAAAAAAAAAAAAAAAAAALLg.desc | minor | mistranslation | 'Mundane Larch' переведено как 'Мировая лиственница', но 'mundane' означает 'обычный', не 'мировой' |
| quest.AAAAAAAAAAAAAAAAAAALMQ.desc | minor | register | 'Both Height and Girth, Get!' - использовано формальное множественное число 'получите' вместо неформального единственног |
| quest.AAAAAAAAAAAAAAAAAAALPA.name | minor | formatting | Неверный код цвета: §2 (тёмно-зелёный) в исходнике, §a (ярко-зелёный) в переводе |
| quest.AAAAAAAAAAAAAAAAAAALPg.name | minor | formatting | Неверный код цвета: §b (голубой) в исходнике, §9 (синий) в переводе |
| quest.AAAAAAAAAAAAAAAAAAALPw.name | minor | formatting | Неверный код цвета: §b (голубой) в исходнике, §9 (синий) в переводе |
| quest.AAAAAAAAAAAAAAAAAAALQA.name | minor | formatting | Неверный код цвета: §b (голубой) в исходнике, §9 (синий) в переводе |
| quest.AAAAAAAAAAAAAAAAAAALQQ.name | minor | formatting | Неверный код цвета: §b (голубой) в исходнике, §9 (синий) в переводе |
| quest.AAAAAAAAAAAAAAAAAAALQw.name | minor | formatting | Неверный код цвета: §b (голубой) в исходнике, §9 (синий) в переводе |
| quest.AAAAAAAAAAAAAAAAAAALRA.name | minor | formatting | Неверный код цвета: §b (голубой) в исходнике, §9 (синий) в переводе |
| quest.AAAAAAAAAAAAAAAAAAALSQ.name | minor | formatting | Неверный код цвета: §a (ярко-зелёный) в исходнике, §8 (тёмно-серый) в переводе |
| quest.AAAAAAAAAAAAAAAAAAALSg.name | minor | formatting | Неверный код цвета: §a (ярко-зелёный) в исходнике, §8 (тёмно-серый) в переводе |
| quest.AAAAAAAAAAAAAAAAAAALSw.name | minor | formatting | Неверный код цвета: §5 (фиолетовый) в исходнике, §2 (тёмно-зелёный) в переводе |
| quest.AAAAAAAAAAAAAAAAAAALTg.name | minor | terminology | Lapotronic - модное/техническое имя, его не нужно переводить; оставить как есть или транслитерировать |
| quest.AAAAAAAAAAAAAAAAAAALUQ.name | minor | formatting | Неправильный код цвета: изменён с §2 на §a; должен остаться §2§lДелаем рапиру |
| quest.AAAAAAAAAAAAAAAAAAALXg.name | minor | formatting | Неправильный код цвета: изменён с §3 на §c; должен остаться §3§lУлучшения для бочек уровень 3 |
| quest.AAAAAAAAAAAAAAAAAAALXw.name | minor | formatting | Неправильный код цвета: изменён с §3 на §c; должен остаться §3§lУлучшения для бочек уровень 4 |
| quest.AAAAAAAAAAAAAAAAAAALYA.name | minor | formatting | Неправильный код цвета: изменён с §3 на §c; должен остаться §3§lУлучшения для бочек уровень 5 |
| quest.AAAAAAAAAAAAAAAAAAALYw.desc | minor | fluency | Неловкая фраза 'один из прочнейших материалов, который ты можешь получить на данном этапе .' (лишний пробел перед точкой |
| quest.AAAAAAAAAAAAAAAAAAAL_A.desc | minor | fluency | Фраза 'Сделай чутка' звучит неестественно и просторечно. Лучше: 'Сделай немного' или 'Создай небольшое количество'. |
| quest.AAAAAAAAAAAAAAAAAAAL_g.desc | minor | fluency | Фраза 'ускоряющих производство' непонятна в контексте 'выгоды от использования хороших нагревательных катушек'. Нужна яс |
| quest.AAAAAAAAAAAAAAAAAAALbw.desc | minor | fluency | Фраза 'для растворения твоей пыли смеси оксида наквадаха' неловкая. Лучше: 'для растворения пыли смеси оксидов наквадаха |
| quest.AAAAAAAAAAAAAAAAAAALlg.desc | minor | untranslated | Остаутся англицизмы: 'overclock', 'alternative', 'Wait', 'going' не переведены, создает смешивание языков |
| quest.AAAAAAAAAAAAAAAAAAALng.name | minor | formatting | Цветовой код изменён с §9 (синий) на §5 (пурпурный), что не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAALoA.name | minor | formatting | Цветовой код изменён с §9 на §5, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAALoQ.name | minor | formatting | Цветовой код изменён с §9 на §5, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAALog.desc | minor | fluency | Грамматическая ошибка: 'в термальная центрифуге' должно быть 'в термальной центрифуге' (творительный падеж) |
| quest.AAAAAAAAAAAAAAAAAAALog.name | minor | formatting | Цветовой код изменён с §9 на §5, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAALow.name | minor | formatting | Цветовой код изменён с §5 на §2, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAALpA.name | minor | formatting | Цветовой код изменён с §a на §8, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAALpw.desc | minor | other | Добавлено информации сверх исходного текста: 'LV улучшенный сейсморазведчик' не упоминается в английском источнике |
| quest.AAAAAAAAAAAAAAAAAAALpw.name | minor | formatting | Цветовой код изменён с §5 на §2, не соответствует исходному |
| quest.AAAAAAAAAAAAAAAAAAALqg.desc | minor | fluency | Redundant 'полезных полезных' в фразе 'получения полезных полезных побочных продуктов' - одно слово лишнее |
| quest.AAAAAAAAAAAAAAAAAAALqw.desc | minor | terminology | Использование слешей 'буровой установки для нефти/жидкости/газа' невразумительно; название машины должно быть однозначны |
| quest.AAAAAAAAAAAAAAAAAAALqw.name | minor | terminology | Слеши в названии 'для нефти/газа/жидкостей' создают путаницу вместо чёткого названия квеста |
| quest.AAAAAAAAAAAAAAAAAAALrg.desc | minor | fluency | Несколько стилистических ошибок: неправильное размещение 'конечно', неловкие конструкции ('если тебе, конечно, не надо б |
| quest.AAAAAAAAAAAAAAAAAAALwg.name | minor | mixed_language | Английское слово 'Superpowered' оставлено нетронутым и смешано с русским 'топливо', что нарушает консистентность: либо п |
| quest.AAAAAAAAAAAAAAAAAAALww.name | minor | mixed_language | Английские слова 'Boiler' и 'Super' оставлены нетронутыми и смешаны с русским 'и топливо', создавая неконсистентный пере |
| quest.AAAAAAAAAAAAAAAAAAALxw.name | minor | mixed_language | Английские слова 'Pushing' и 'Anti-Knock Agent' оставлены нетронутыми и смешаны с русским предлогом 'с', нарушая консист |
| quest.AAAAAAAAAAAAAAAAAAALyA.name | minor | mixed_language | Английские слова 'Zooming' и 'Nitrous' оставлены нетронутыми и смешаны с русским предлогом 'с', нарушая консистентность  |
| quest.AAAAAAAAAAAAAAAAAAALyQ.name | minor | mixed_language | Английские слова 'Speeding' и 'Octane' оставлены нетронутыми и смешаны с русским предлогом 'с', нарушая консистентность  |
| quest.AAAAAAAAAAAAAAAAAAAM3g.desc | minor | formatting | Опечатка в названии мода: 'Мод Сatwalks' - лишний пробел внутри слова 'Catwalks' (должно быть 'Mod Catwalks' без разрыва |
| quest.AAAAAAAAAAAAAAAAAAAMAA.desc | minor | mistranslation | Неточный перевод: 'улучшить твою Электрическую доменную печь' не соответствует 'make some more' в оригинале. Должно быть |
| quest.AAAAAAAAAAAAAAAAAAAMAQ.desc | minor | fluency | Грамматическая ошибка: 'больше, чем 8 пылек' - неправильная форма числительного. Должно быть 'пыли' (в генитиве множеств |
| quest.AAAAAAAAAAAAAAAAAAAMAg.name | minor | formatting | Неправильный цветовой код: оригинал использует §a (зелёный), а перевод имеет §8 (тёмно-серый). Должно быть §a§l для сохр |
| quest.AAAAAAAAAAAAAAAAAAAMDA.name | minor | mistranslation | 'The Other Part' переведено как 'Следующий шаг' (Next Step), что не совпадает с оригинальным смыслом. |
| quest.AAAAAAAAAAAAAAAAAAAMPw.name | minor | terminology | Неправильная капитализация и неверный перевод: магия должна быть магический |
| quest.AAAAAAAAAAAAAAAAAAAMQg.name | minor | fluency | Ошибка согласования падежей: должно быть больше пара для топлива |
| quest.AAAAAAAAAAAAAAAAAAAMSg.name | minor | formatting | Отсутствует заглавная буква. Должно быть 'Фокус на разведение' |
| quest.AAAAAAAAAAAAAAAAAAAMcg.name | minor | mixed_language | Английское 'Tin' не переведено. Должно быть 'Плазма олова из T2' |
| quest.AAAAAAAAAAAAAAAAAAAMdw.name | minor | fluency | 'Опциональный' - неестественный выбор слова. Лучше 'Дополнительный' или 'Необязательный'; 'тир' следует перевести как 'у |
| quest.AAAAAAAAAAAAAAAAAAAMeQ.name | minor | fluency | 'Опциональный' - неестественный выбор слова; 'тир' следует перевести как 'уровень' |
| quest.AAAAAAAAAAAAAAAAAAAMew.name | minor | untranslated | 'Tetrafluoride' не переведено. Должно быть 'Тетрафторид тория и топливо 3' |
| quest.AAAAAAAAAAAAAAAAAAAMgg.name | minor | untranslated | 'Max' не переведено. Должно быть 'Максимально опасные ядерные реакторы' |
| quest.AAAAAAAAAAAAAAAAAAAMhQ.name | minor | fluency | 'дорогой' - неправильное согласование (должно быть множественное число). Лучше 'Реакторы дорого обходятся!' или 'Реактор |
| quest.AAAAAAAAAAAAAAAAAAAMkg.name | minor | formatting | Неверные коды цвета: §9§l§n вместо §6§l. Перевод текста правильный, но форматирование повреждено. |
| quest.AAAAAAAAAAAAAAAAAAAMkw.name | minor | formatting | Неверные коды цвета: §9§l§n вместо §6§l. Перевод текста правильный, но форматирование повреждено. |
| quest.AAAAAAAAAAAAAAAAAAAMoA.name | minor | mistranslation | Неполный перевод. Отсутствует артикль 'A' в начале. Следует: 'Соглашение с Alfar Industries' или подобное полное русское |
| quest.AAAAAAAAAAAAAAAAAAAMow.name | minor | formatting | Неверные коды цвета (§9§l§n). Перевод текста приемлем, но форматирование повреждено. |
| quest.AAAAAAAAAAAAAAAAAAAMpA.name | minor | formatting | Неверные коды цвета (§5§l§n вместо ожидаемого). Перевод правильный, но форматирование повреждено. |
| quest.AAAAAAAAAAAAAAAAAAAMpQ.name | minor | untranslated | Неверные коды цвета (§9§l§n). Нетранслитерированная аббревиатура 'pt.2' должна быть либо переведена, либо полностью согл |
| quest.AAAAAAAAAAAAAAAAAAAMpw.name | minor | formatting | Неверные коды цвета (§5§l§n вместо ожидаемого). Перевод 'Тессеракт' правильный, но форматирование повреждено. |
| quest.AAAAAAAAAAAAAAAAAAAMtw.name | minor | untranslated | 'Hydrobotanic' оставлено на английском, смешанный язык. |
| quest.AAAAAAAAAAAAAAAAAAAMuQ.name | minor | untranslated | 'Combustion Generator' оставлено на английском, неловкая фраза 'является этот'. |
| quest.AAAAAAAAAAAAAAAAAAAMug.name | minor | untranslated | 'Botanist's' и 'Friend' оставлены на английском. |
| quest.AAAAAAAAAAAAAAAAAAAMvA.name | minor | untranslated | 'Violence' и 'Blue' оставлены на английском. |
| quest.AAAAAAAAAAAAAAAAAAAMvQ.name | minor | untranslated | 'Roses' и 'Blood-Red' оставлены на английском. |
| quest.AAAAAAAAAAAAAAAAAAAMxA.name | minor | untranslated | 'Obligatory' оставлено на английском. |
| quest.AAAAAAAAAAAAAAAAAAAMxQ.desc | minor | untranslated | 'chicken-related' и 'including entire' оставлены на английском, неполный перевод. |
| quest.AAAAAAAAAAAAAAAAAAAMxg.name | minor | untranslated | 'According', 'Known Laws', 'Generation' оставлены на английском, неполный перевод. |
| quest.AlYEP7f4T-KHgH8vicSXdg.desc | minor | formatting | Повреждены форматирующие коды: 'Очищенная вода 1-го классаr§r' (лишний 'r'), 'наночастицы незеритаs' (лишний 's'). |
| quest.B0XRo_S1RveAsKZSXms9vg.name | minor | mistranslation | 'Energium' переведено как 'Энергетическая' (женский род прилагательного). Должно быть 'Энергий' или 'Энергиум' (согласно |
| quest.CW9oIeA0ShWo7euZXUx72A.name | minor | formatting | Код цвета изменён с §b (синий) на §9 (тёмно-синий) |
| quest.D0JaazeIQ8qctaMx9xTqEw.name | minor | formatting | Первое слово должно быть заглавным: 'Продвинутый' вместо 'продвинутый' |
| quest.D6AFvlXcQbqDncL9y2HXEw.name | minor | formatting | Код цвета изменён с §c (красный) на §d (магента) |
| quest.DVLahVNUQ-CvjYwmvkUn-Q.name | minor | formatting | Добавлены коды форматирования (§c§l§n), которых нет в исходном тексте. Следует убрать или согласовать с исходником |
| quest.H_S9zi1_SUKG7JkEYgJIiA.name | minor | mistranslation | Неполный перевод: 'Assembling в Space' - 'Assembling' остался на английском, должно быть полностью на русском |
| quest.IGVryoMbRu28q08v4uwSuw.name | minor | mistranslation | Частичный перевод: 'Fabricating Solar Systems... в Parallel' - 'Fabricating' и 'Parallel' не переведены, должны быть на  |
| quest.II3sjr1cSPOMXaSG70S_eg.name | minor | mistranslation | Неправильное согласование: 'звезда топливо и Dark материя' - должно быть 'Звездное топливо и тёмная материя'; цветовой к |
| quest.JRrD8MoLRuCHCD-fFpeNvQ.desc | minor | fluency | Неправильное согласование: 'различный объемов входных материалов' должно быть 'различные объемы входных материалов' |
| quest.JRrD8MoLRuCHCD-fFpeNvQ.name | minor | formatting | Изменен цветовой код: должен быть §5§l, а не §2§l |
| quest.JejpWZ7ATZq-0uomP4c7UA.name | minor | terminology | Использована кириллица 'К' вместо латиницы 'k', добавлено слово 'хранения' которого нет в источнике |
| quest.JkWQZxq_TECWjHhjywrZZA.name | minor | formatting | Изменен цветовой код: должен быть §a§l, а не §8§l |
| quest.Jna1jgAySNSs8nS0YMXpLw.name | minor | formatting | Изменен цветовой код: должен быть §a§l, а не §8§l |
| quest.JyVKlIbSSiaXjYfQ2FFLhQ.name | minor | fluency | Неправильная конструкция: 'Предупреждение о заражении порчей' должно быть 'Предупреждение о Порче' |
| quest.KGBrxQRsSneYMzNHBll9Bg.name | minor | formatting | Изменен цветовой код: должен быть §c§l, а не §d§l |
| quest.KHL_yx4XTKOtsHHZ60ZZpg.name | minor | terminology | Добавлено слово 'Жидкое' которого нет в источнике, должно быть просто 'Топливо на основе наквадаха' |
| quest.LIZCdBLfQquQpULGmFDixw.name | minor | fluency | Неловкая конструкция '...или являются они?' должна быть '...а может быть, нет?' или '...или нет?' |
| quest.LSqzsH4oS7OQrZyolb7C0A.name | minor | mixed_language | Смешанный английский и русский: 'Celestial Tungsten плазма' и 'Mk3 Finale' должны быть полностью переведены или оставлен |
| quest.LaLMF5rFQ0SxAZ5o-C-r5Q.name | minor | fluency | 'Больше радиус' неправильно согласовано, должно быть 'Больше радиуса' или 'Удвойте радиус' |
| quest.LzCq9t0cT4-_TizIr_Iq_A.name | minor | formatting | Заголовок начинается со строчной буквы 'извлечь', должна быть прописная 'Извлечь' |
| quest.MwRByyNxQt-LfGgUqm8QDQ.name | minor | mixed_language | Английское слово 'Remote' оставлено без перевода; должно быть полностью на русском. |
| quest.PFguzsBlTrKLXNv9miH-xg.name | minor | terminology | Некорректная терминология. 'Dynamism Tablets' переведены как 'Динамические дощечки', но в контексте мода это должны быть |
| quest.RAH2M4DoTTaX5a2Sj4hRcQ.name | minor | formatting | Неправильный код цвета (§9 вместо сохранения исходного стиля) и лишние модификаторы §l§n нарушают оригинальное форматиро |
| quest.SDGKHP7fQx-c3gUBv4DwuQ.desc | minor | formatting | Нарушено форматирование в 'The §cСигнулярное' - смешано английское слово 'The' с русским переводом. Также отсутствует фо |
| quest.SIqmtgRmTj-EsZlXpCdyWQ.name | minor | formatting | Неправильный код цвета (§9 вместо §b) нарушает оригинальное форматирование. |
| quest.SmLW-ht6TrKSmAUDyDoNqg.name | minor | formatting | Неправильный код цвета (§d вместо §c) нарушает оригинальное форматирование. |
| quest.Tfb8JzstRNuiSV6CKgTNRQ.name | minor | terminology | «Синтез бора» неточно передает «Boronic Fusion» — термин относится к органической химии (борные соединения), а не просто |
| quest.TvVeFhtYQCSmlekVCdADaQ.name | minor | mistranslation | «Pechuliar» — каламбур (Pech + peculiar), переведено как простой «Гном-торговец», теряется игра слов |
| quest.U4zxsdwqTUKsbTATYEJirg.desc | minor | fluency | Грамматическая ошибка: «ты готовы» — неверное согласование (должно быть «ты готов» или «вы готовы») |
| quest.UVG21mYSQJex90gQWdkpIw.desc | minor | fluency | Отсутствует пунктуация; неудачный синтаксис: «дорого содержать но оно того стоит» — нужна запятая и переформулировка |
| quest.V9BupH47RI6RWX6vff5dpw.name | minor | formatting | Неправильный код цвета: §2 заменён на §c (зелёный на красный) |
| quest.VoQgq6UvTZmo3tpUIZs4Rg.name | minor | mistranslation | Неполный перевод, отсутствует 'пчела' или подобное существительное |
| quest.WTIyEmzLR_mlw__SXY_iwA.name | minor | mistranslation | Герундиальная форма 'Вставляя' звучит неестественно для названия, лучше использовать глагол в инфинитиве |
| quest.YVlqGPZBS8qCkkHlu1BDpg.name | minor | terminology | Неправильная форма слова - должно быть 'Пиротеум' (существительное), а не 'Пиротеумная' (прилагательное). |
| quest.Yxrhi0z7SUuvUT3BrsENww.name | minor | untranslated | Слово 'Cheaper' оставлено на английском языке. Должно быть переведено как 'Дешёвые' или 'Более дешёвые'. |
| quest.ZS2_l5v3R2-gh69ESL-FNQ.desc | minor | formatting | Отсутствует пробел после вопросительного знака ("Да?Ну"), непправильное согласование (мужской род "ты уверен" вместо ней |
| quest.ZXyJX8zNTQW6swu0OsE03Q.name | minor | formatting | Цветовой код изменен (§b на §9), хотя контент верен |
| quest.Zza5BrD7TduqKby_b3wQsQ.desc | minor | mistranslation | Отсутствует упоминание о "Crystalline Pink Slime" в переводе; первое предложение неполно - потеряна ключевая информация  |
| quest._bEWg1FHSmKu9MNhlbDlwA.desc | minor | fluency | Повторение слова "необходимость" - "что убирает необходимость необходимость копировать". Должно быть "что убирает необхо |
| quest.aXAQD7T1SnGCAu0L4iV64w.name | minor | mistranslation | 'Пояса ускорения' неточно передаёт 'Speed up with the Sash' - неправильно указан тип предмета. |
| quest.aZbgSe36TnSB3O4ZwkSlJw.desc | minor | register | Неконсистентное использование форм обращения: 'Убедитесь' (вежливая форма) и 'ты хорошо экипирован' (неформальная). |
| quest.auchuNiGTH6NWh_cz8XxcQ.desc | minor | mistranslation | 'новый корпус' слишком просто и неточно передаёт смысл оригинала 'housing for advanced fluid components'. |
| quest.b47jlBoHTFGGB3j7nq60Zw.desc | minor | fluency | Опечатка: 'Хооошее' с тройной буквой 'о', должно быть 'Хорошее'. |
| quest.bMKIeFhNQluRks9YzpqEGQ.desc | minor | fluency | Несколько неточностей: 'не добавят жилу' следует 'не откроет жилу', 'будь одурачен' звучит архаично, фраза про NEI неясн |
| quest.bQCnuxrTTBe4ubytZPfl-g.name | minor | mistranslation | 'Это получает polymorphic' — неправильное управление и оставленное английское слово. Должно быть что-то вроде 'Полиморфи |
| quest.bfrxXr1iSpGQS8iV95nJeA.name | minor | fluency | 'Получше' — диалектизм и неправильная форма. Должно быть 'Понимаем процесс получения жезлов' или 'Постижение развития же |
| quest.bz_RazGFSl6k7fUkEt1Lzw.name | minor | fluency | Неловкий порядок слов. Лучше: 'Паровая турбина SC XL Турбо' или 'XL Паровая турбина SC Турбо'. |
| quest.cQkx83QYT4m3mwovgZIKvA.name | minor | untranslated | Слово 'Skip' не переведено. Должно быть: 'Триггер: Пропуск Бутадиен-стирольной резины' или аналогично. |
| quest.dYvLkQ-xRnWL8Egy_MnoIg.name | minor | untranslated | Название содержит английское слово 'Cheaper' и техническое обозначение 'ZPM' без перевода. Требуется перевести 'Cheaper' |
| quest.eEJocLDBTkmdsCKo7Qhegw.name | minor | untranslated | Название содержит английское 'Download' и 'RAM' без перевода. Фраза 'Download больше RAM' выглядит как незавершённый пер |
| quest.eWOxG-reT9ewlW0CNXgQNQ.desc | minor | mistranslation | Ошибка в слове 'мыль' (должно быть 'мысль'). Также описание 'Можно также посадить её на смешанный кристальный блок!' не  |
| quest.eZADH1WASo6NLBUTKjLNGQ.name | minor | mistranslation | Название переведено как 'Суперклей', но оригинал 'Relentless Glue' имеет другой смысл (неумолимый, неустанный клей). 'Су |
| quest.g0oiNbRuQpWrzFOS8l-DtA.name | minor | mistranslation | Неправильный перевод: пропущено начало фразы, должно быть что-то вроде «Ещё Более Мега EBF» или «Тем более Мега EBF», а  |
| quest.hB5tvfilRVi42OpLLhCwlw.desc | minor | mistranslation | "Навигационная панель" (navigation panel) is imprecise - should be "Навигационная консоль" to match "Navigation Console" |
| quest.hEsmeH74S4aOOrROI1AHxQ.name | minor | mistranslation | §3§l (cyan/blue color) changed to §c§l (red color), altering original formatting intent. Word "Revolution" should keep " |
| quest.hWXZi-whQfmgWO0EII7g2g.name | minor | mistranslation | Awkward phrasing 'Экономя на пространство-времени' - should be more natural like 'Экономия пространства-времени' or 'Сох |
| quest.hybMIjq9Q9mxxWKEE8gBWQ.name | minor | mistranslation | Should use "Охлаждение подпространства" or similar - 'Subspace охлаждение' mixes English and Russian awkwardly. |
| quest.iwN50p7pSyyCHDkM-O-D7w.name | minor | fluency | Неправильный порядок слов и граммтика. Должно быть 'Ячейка хранения эссенции 16384К' или похожее. |
| quest.jvKBzB6tRpCQGlnboQxSAA.name | minor | fluency | Форма 'Золотая' (женский род) неправильна для названия. Должно быть 'Золото' (именительный падеж, средний род). |
| quest.kQL8JceoSMSLDU_2AFjoqw.name | minor | formatting | Код цвета изменен с §a (зелёный) на §8 (тёмно-серый). Должен быть восстановлен исходный цвет. |
| quest.kR1YVSq2R4WFu9KNM9lCZQ.name | minor | formatting | Код цвета изменен с §2 (тёмно-зелёный) на §a (зелёный). Должен быть восстановлен исходный код цвета. |
| quest.kvqtI5rrRrOhi5jhPR-s4A.name | minor | fluency | Единственное число 'Сверхпроводник' может быть неправильным. Проверить контекст - вероятно, должно быть 'Сверхпроводники |
| quest.l26l6_loSeyuxQYps9XbbA.name | minor | untranslated | Слово 'Modular' остаётся на английском. Должно быть 'Модульные улучшения'. |
| quest.l4q7oG79RfCZjnE_Ys57DA.name | minor | untranslated | Слово 'Magical' остаётся на английском. Должно быть 'Волшебный'. Также странное начало 'но' вместо 'Но'. |
| quest.n8PKF63sSSi0y8ZBb2RIKQ.name | minor | untranslated | 'Stabilized Baryonic' остаются на английском - должно быть полностью на русском |
| quest.ne_onBK6TP2F_ySPabM7Lw.name | minor | formatting | Неправильный цветовой код (§c вместо §2) из-за COLOR хинта - нарушена визуальная согласованность |
| quest.njE33db1TxaiJhEBA16E4A.name | minor | formatting | Неправильный цветовой код (§2 вместо §5) из-за COLOR хинта |
| quest.nx7KEyhlTc6qYVM1vImkBA.name | minor | formatting | Неправильный цветовой код (§d вместо §c) из-за COLOR хинта |
| quest.pKSx6HEUS0WkL6qkwo742g.name | minor | untranslated | "High Voltage" опущено в переводе, остались только "HV Мультиблоки" вместо полной фразы |
| quest.qnXgpGxbRc-nHbshgUs1jA.desc | minor | terminology | Слово 'бесконечность' в скобках без пробела '(11)' должно быть 'Infinity (11)' или русский аналог. Форматирование наруше |
| quest.sHI1n7unRWecpNcyBAgUfw.name | minor | untranslated | 'Composite Sheet' частично не переведено — следует перевести как 'Лист композита' или аналогично |
| quest.sIP_FoxIRaeE08GesBwYcQ.name | minor | mistranslation | Потеряно слово 'Skip' из исходного текста — перевод неполный |
| quest.u-2IsyxKTLiZuTY417qWKw.name | minor | formatting | Строчная буква 'тир' должна быть заглавной 'Тир'. Исправить на '§c§l§nТир 4 QFT Catalysts' |
| quest.vV8Pw_lTTSiMmWOLqkyIWg.name | minor | formatting | Неправильный код цвета: §2 (зеленый) вместо §5 (пурпурный/фиолетовый). Исправить на '§5§lТочный лазерный гравировщик' |

## Rework list (deterministic QA — auto)

| key | QA issues |
|---|---|
| quest.-1GoIXIXR029oc0Ge6sRGg.desc | GARBAGE_MT |
| quest.01C00SMsRUyKUD2zJht8tA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.07lxVb9wQWSSoZRcvIswZQ.desc | PCT_N,COLOR |
| quest.0YrjX7i4QfeSo98gSE0SWg.name | NO_CYRILLIC,COLOR |
| quest.0fzaxas8R8OJzvYvqX5d9w.desc | TAGS |
| quest.1PpNSMRMR_-6fCQnguQX-A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.1PpNSMRMR_-6fCQnguQX-A.name | UNTRANSLATED,NO_CYRILLIC |
| quest.1W0BrWncRuWbeTrPDVV99w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.1W0BrWncRuWbeTrPDVV99w.name | NO_CYRILLIC |
| quest.21tDEYptRuOgSJym30Watg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.2TXAUm6oQ0OhtMK79tC5cw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.3r7tJ7_bTuePzsh-B_jyIQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.3wK8pIDKSOii1__bwf6Ycw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.3yz1WCEzQ_KQxW8p7_29-Q.name | NO_CYRILLIC,COLOR |
| quest.4HoSq97QT3G63VJFeV_0ZQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.4LY2S8QsSw-JdMGrF8FUsQ.desc | PCT_N |
| quest.5EdKBIyDTYa7xhnSCUZmiQ.desc | PCT_N,TAGS |
| quest.5RrDJZBfTligyX8_wR-EDA.desc | EMPTY |
| quest.5mcwk7dYSBydA9KRHbW59A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.6OibD9bRQwq_hBPWz-y9xQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.6pH9sRoUSbCDG8eWqXS_ow.desc | PCT_N,LATIN_DENSE |
| quest.7_AtC62nTAKG1nTYoyS-8g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.7_AtC62nTAKG1nTYoyS-8g.name | UNTRANSLATED,NO_CYRILLIC |
| quest.7wI7VuLKRe6lqAJpuYKKJg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.8CwALDydSAaz9GGQm5tB-g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.8JcG3DR5QU6_FbhIWHm05g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.8zpQos1hR1CbwmWldvxSpg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.9CIs8MP4TBuyRgn8lDu3Mg.desc | PCT_N,LEAK_MINOR,LATIN_DENSE |
| quest.9dt9i3MYRa-NB6KROtAYFA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.9j1Iwd3KRG6jqLI9m6YDKQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.9j1Iwd3KRG6jqLI9m6YDKQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.A462Q2yHRleMxFZCeNzhuA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAA7Q.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAAoQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAAow.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAAtw.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAAvw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAAwA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAB-Q.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAB-g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAB-w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAB-w.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAB5Q.desc | PCT_N,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAB6g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAB9g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABBQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABCQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABEQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABEw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABFA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABFQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABFg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABFw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABGg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABHA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABIQ.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABIw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABJw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABKg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABLw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABMQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABMg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABNw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABPA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABPA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABPw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABQQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABQg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABQw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABSg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABSw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABTQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABTw.desc | GARBAGE_MT |
| quest.AAAAAAAAAAAAAAAAAAABTw.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABUA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABUg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABVg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABWg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABWg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABYA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABYw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABZg.desc | GARBAGE_MT |
| quest.AAAAAAAAAAAAAAAAAAABZw.desc | GARBAGE_MT |
| quest.AAAAAAAAAAAAAAAAAAAB_A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABaw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABdw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABeQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABew.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABfA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABgQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABhA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABhA.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAABlw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABmg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABnA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABog.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABqQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABqg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABrA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABrQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABsA.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABsQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABsQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABsw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABtQ.desc | GARBAGE_MT |
| quest.AAAAAAAAAAAAAAAAAAABtQ.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAABtg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAABuA.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAByg.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAABzQ.desc | PCT_N,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAC8w.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAACAA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAACAg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAACAw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAACBA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAACBQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAACBg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAACCA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAACCg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAACCw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAACDQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAACHw.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAACWg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAC_w.desc | PCT_N,PCT_PCT |
| quest.AAAAAAAAAAAAAAAAAAACcw.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAACdA.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAACdQ.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAACgA.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAACvQ.desc | GARBAGE_MT |
| quest.AAAAAAAAAAAAAAAAAAACvQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAACwg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAACxQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAACyQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAACyg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAADCA.desc | PCT_N,TAGS |
| quest.AAAAAAAAAAAAAAAAAAADEQ.desc | PCT_N,TAGS |
| quest.AAAAAAAAAAAAAAAAAAADQQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAD_Q.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAADag.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAADrw.desc | PCT_N,COLOR,TAGS |
| quest.AAAAAAAAAAAAAAAAAAADtA.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAEKw.desc | PCT_N,COLOR,TAGS |
| quest.AAAAAAAAAAAAAAAAAAAESw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAETg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAEUQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAEVQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAEVQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAEVg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAEWg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAEWg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAEXA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAEXQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAEYA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAEYQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAEYg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAEYw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAEYw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAEhA.desc | PCT_N,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAErQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAErg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAErw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAEsQ.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAEsg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAEsw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAEvA.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAF0w.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAF3A.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAF3w.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAF6w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAFMA.desc | PCT_N,PCT_PCT,TAGS |
| quest.AAAAAAAAAAAAAAAAAAAFMg.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAFSQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAFTA.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAFXQ.desc | PCT_N,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAFXg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAFXg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAFXw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAFYA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAFYA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAFYQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAFZA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAFZA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAFZQ.desc | PCT_N,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAFZg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAFZw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAF_w.desc | PCT_N,TAGS |
| quest.AAAAAAAAAAAAAAAAAAAFaA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAFaQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAFaQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAFag.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAFbA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAFcQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAFcQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAFcw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAFcw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAFhA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAFiA.desc | TAGS |
| quest.AAAAAAAAAAAAAAAAAAAFiw.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAFlQ.desc | PCT_N,TAGS |
| quest.AAAAAAAAAAAAAAAAAAAFmQ.desc | PCT_N,TAGS |
| quest.AAAAAAAAAAAAAAAAAAAFqg.desc | TAGS |
| quest.AAAAAAAAAAAAAAAAAAAFrg.desc | PCT_N,TAGS |
| quest.AAAAAAAAAAAAAAAAAAAG1Q.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAG1w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAG2A.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAG2g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAG3g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAG3g.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAG4Q.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAG4g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAG4w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAG5A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGEw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGGg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGGw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGHA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGHg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGHw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAGIA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGIg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGIw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGJA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGJA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAGKw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGKw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAGMQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGMg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAGMw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAGNg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAGPQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGWA.desc | GARBAGE_MT |
| quest.AAAAAAAAAAAAAAAAAAAGWA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAGXA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGXQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGXw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGYA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGYQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGYw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGZA.desc | GARBAGE_MT |
| quest.AAAAAAAAAAAAAAAAAAAGZg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGag.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGbg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAGbw.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAGcA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAGgQ.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAGgw.desc | PCT_N,TAGS |
| quest.AAAAAAAAAAAAAAAAAAAGpw.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAGvg.desc | PCT_N,TAGS |
| quest.AAAAAAAAAAAAAAAAAAAH0A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAH0A.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAH0g.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAH0w.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAH2A.desc | TAGS |
| quest.AAAAAAAAAAAAAAAAAAAH3A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAH3A.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAH4w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAH5A.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAH5Q.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAH5Q.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAH7g.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAH8A.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAHFA.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAHHA.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAHMA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAHaA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAHaQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAHcQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAHhQ.desc | PCT_N,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAHog.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAHxQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAHxg.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAHxw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAHxw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAI2w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAI3A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAI5Q.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAI5g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAI6w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIEg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIFA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAIIg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIKA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIKQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIKg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIKw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIKw.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAILA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAILQ.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAILw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIMA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIMQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIMg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIPQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAIYQ.desc | PCT_N,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIbw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIdQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIeA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIgw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIjA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIjQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAInA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAInw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIoA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIuw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIvQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAIwg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAIyA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJ4Q.desc | PCT_N,TAGS,URL,BARE_URL |
| quest.AAAAAAAAAAAAAAAAAAAJ6w.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAJGQ.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAJHw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJIA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJIQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJIQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJIg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJIw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJJQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJKA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJKw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJLA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJLQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJLg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJMA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJMQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJMg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJMg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJMw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJNA.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJNg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJNg.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJNw.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJOA.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJOQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJOQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJOw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJPA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJPQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJPw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJQA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJQQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJQg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJQw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJRg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJRw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJRw.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJSA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJSA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJSQ.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJSg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJSw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJSw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJTA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJTA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJTQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJTQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJTw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJTw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJUA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJUQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJUw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJaw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJcA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJcA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJdA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJdg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJdw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJeA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJeQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJkw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJlw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJlw.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAJmA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAJmg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAJnA.desc | GARBAGE_MT |
| quest.AAAAAAAAAAAAAAAAAAAKFg.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAKFw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKGQ.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAKHA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKNw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKOA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKPw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKQg.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAKSg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKUA.desc | PCT_N,COLOR,TAGS |
| quest.AAAAAAAAAAAAAAAAAAAKUg.desc | PCT_N,TAGS |
| quest.AAAAAAAAAAAAAAAAAAAKVA.desc | PCT_N,TAGS |
| quest.AAAAAAAAAAAAAAAAAAAKVg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKVw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKWA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKWg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKWw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKZA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKbA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKcQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKcg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKcw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKdA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKdA.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAKdw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKdw.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAKeQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKeQ.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAKeg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKew.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKiA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKmw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKnQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKnQ.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAKpg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAKpw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAKrA.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAKww.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAKyg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAKzQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAL0Q.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAL0g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAL0g.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAL0w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAL0w.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAL1A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAL1Q.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAL3g.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAL3w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAL4w.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAL5A.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAL5Q.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAL7g.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAALCw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALDQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALQg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAALRw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALSA.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAALVA.desc | EMPTY |
| quest.AAAAAAAAAAAAAAAAAAALdw.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAALeA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALeQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALhA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALhg.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAALhg.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAALlw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALlw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAALpQ.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAALwg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALww.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALxA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALxQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALxg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALxw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALyA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALyQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALyw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALzA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALzQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALzQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAALzg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALzw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAALzw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAM0A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAM0g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAM1A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAM1A.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAM1Q.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAM1g.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAM2A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAM2Q.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAM2Q.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMBw.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAMFA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMFQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMFg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMFw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMGA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMGQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMGg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMGw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMGw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMHA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMHQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMHg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMHg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMHw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMIA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMIQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMIg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMIw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMJQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMJg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMJg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMJw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMKA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMKA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMKQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMKg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMKw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMLA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMLQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMLg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMLw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMMA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMMA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMMQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMMg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMMw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMMw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMNA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMNA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMNQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMNg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMOA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMOg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMPA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMPA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMPQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMPg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMPw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMQA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMQg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMQw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMRQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMRQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMRg.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAMSA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMSg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMSw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMTg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMTg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMTw.desc | PCT_N,TAGS,URL,BARE_URL |
| quest.AAAAAAAAAAAAAAAAAAAMUA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMUQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMUg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMUw.desc | PCT_N,TAGS,URL,BARE_URL,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMVA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMVQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMVg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMVw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMWA.desc | PCT_N,TAGS,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMWQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMWg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMWw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMXA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMXQ.desc | PCT_N,TAGS |
| quest.AAAAAAAAAAAAAAAAAAAMXg.desc | PCT_N,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMXw.desc | PCT_N,TAGS,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMYA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMYQ.desc | PCT_N,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMYg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMYw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMZA.desc | TAGS,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMZQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMZg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMZw.desc | PCT_N,PCT_PCT,TAGS,URL,BARE_URL,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMaA.desc | PCT_N,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMaQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMag.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMaw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMbA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMbA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMbg.desc | PCT_N,COLOR,TAGS,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMbw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMcA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMcA.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMcQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMcg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMcw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMdA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMdA.name | NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMdQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMdg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMdw.desc | PCT_N,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMeA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMeQ.desc | TAGS,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMeg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMew.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMfA.desc | PCT_N,TAGS,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMfQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMfQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMfg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMfg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMgA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMgQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMgg.desc | PCT_N,PCT_PCT,TAGS,URL,BARE_URL,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMgw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMhQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMhg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMhw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMiA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMkA.name | NO_CYRILLIC,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAMkQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMkg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMkw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMmQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMnA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMnA.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMnQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMoA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMow.desc | PCT_N,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAMrg.desc | GARBAGE_MT |
| quest.AAAAAAAAAAAAAAAAAAAMsA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMsQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMtA.desc | PCT_N,COLOR |
| quest.AAAAAAAAAAAAAAAAAAAMtQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMtg.desc | PCT_N |
| quest.AAAAAAAAAAAAAAAAAAAMug.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMvQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMvw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMvw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMwA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMwQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMwQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMwg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMww.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMww.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMxA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMxQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.AAAAAAAAAAAAAAAAAAAMyg.desc | COLOR,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMzQ.desc | COLOR,TAGS,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMzg.desc | COLOR,GARBAGE_MT,LATIN_DENSE |
| quest.AAAAAAAAAAAAAAAAAAAMzw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.AQMaWAiIRo6vNTAxqopS_Q.name | NO_CYRILLIC,COLOR |
| quest.AVth34rQQ3iuYeQaKrsSQg.desc | COLOR,TAGS |
| quest.Avz75EgSTdG48xI3HPGUMA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.B0XRo_S1RveAsKZSXms9vg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.BFpBG-zDQSCr3DieB6Cw5g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.D0JaazeIQ8qctaMx9xTqEw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.D6AFvlXcQbqDncL9y2HXEw.desc | PCT_N,COLOR,GARBAGE_MT,LATIN_DENSE |
| quest.DPl-UUZfTAa-ezdD_m8Huw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.EP-xPjNWRnKCWRJjGzySvQ.desc | PCT_N,GARBAGE_MT,LATIN_DENSE |
| quest.EfJnTMxuTMKc5VhvNOxrYQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.EfJnTMxuTMKc5VhvNOxrYQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.FYOm8b1PRTKsyVjFdpBqjg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.FiNzfQEmSlOHb8fuC-FWBw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.GslQBIW9QKaCz7FFpkrv6g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.GvlZG9IESmW2qsEMw-hkIw.desc | PCT_N |
| quest.H3Tvy4ZKSyiQGT16Og90bA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.HF-prjNuRP-RUOYzn170cQ.desc | PCT_N |
| quest.Hn_igsosSbKsnATeYgvPgw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.II3sjr1cSPOMXaSG70S_eg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.JVZjTR4hRSaeaoXPvBcG9w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.JhZaTiUfTH2AfBcHulTMVA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.Jk9jZtb6SXSLNX9SND_J0A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.Jl453zbkSfC4pl9kglgy6A.desc | PCT_N,GARBAGE_MT,LATIN_DENSE |
| quest.K0_-BjVuR3qh_GZt19SReQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.KGDOhsZGQv2QqDzGdI_YTg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.KHL_yx4XTKOtsHHZ60ZZpg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.KM9gm3HCTa2OGPWlHHl4fw.desc | PCT_N |
| quest.KNM9ICNAQIa8NaFoXwCC9g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.Ko5ln-tKSFiZZWtAmSWv8w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.LSqzsH4oS7OQrZyolb7C0A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.LzCq9t0cT4-_TizIr_Iq_A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.MJgg4KT4Q1Gi-2hgQ9Sz6w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.Mf1D7e-LTaW3rbBRYmxBAQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.N8isBrjBRNe-3f-IHVymDg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.Ng5Ldnf3TZCefB4Mr3u-rQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.Ng5Ldnf3TZCefB4Mr3u-rQ.name | UNTRANSLATED,NO_CYRILLIC |
| quest.OCv5OWo6Q9KDfqe1w0ET9w.desc | PCT_N,GARBAGE_MT,LATIN_DENSE |
| quest.OEBBeZOSSRGu80s3RPeiVA.name | GARBAGE_MT |
| quest.PFguzsBlTrKLXNv9miH-xg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.QO1gudFvTtKgWe9942dW3Q.desc | GARBAGE_MT,LATIN_DENSE |
| quest.Qrjs7uh5TcSveEbaFnXFog.desc | GARBAGE_MT,LATIN_DENSE |
| quest.SmLW-ht6TrKSmAUDyDoNqg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.SsBfuluoR5m5D-dEuoKgsg.desc | EMPTY |
| quest.TakFzrg7Rfew3UivxIIzvw.desc | EMPTY |
| quest.Tfb8JzstRNuiSV6CKgTNRQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.U12vBo4fQjOyzJ67qH7gUA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.U7Ta5d7PSii76sbIPbltlw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.V76lvP8lSsewcKfwxHirPw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.VISeokU3R-efeF88FwLGLw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.WPoaCPPwTBSyn2dmh5DcBA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.WTIyEmzLR_mlw__SXY_iwA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.XKKP2E5ORG-ju42dSDd3sw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.X_rOgp6GRKiyGzwRV_p7GA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.XoEzTtuPQjyeHTyqp9eY8Q.desc | GARBAGE_MT,LATIN_DENSE |
| quest.XoEzTtuPQjyeHTyqp9eY8Q.name | NO_CYRILLIC,COLOR |
| quest.Y4bRCOWFTgyxdTJXWXjFfA.desc | COLOR,GARBAGE_MT,LATIN_DENSE |
| quest.YO0JcMSOQVa3-WoWP1l78Q.desc | GARBAGE_MT,LATIN_DENSE |
| quest.YxYz1jL6RSWHCxMlTHeJFw.desc | COLOR,GARBAGE_MT,LATIN_DENSE |
| quest.ZM4oSqeWQRW1Y-zoE01ivg.desc | PCT_N,LATIN_DENSE |
| quest._Cwgzi_VR5ChWJSIIrzUvg.desc | GARBAGE_MT,LATIN_DENSE |
| quest._O6stWM3RR-qJdcvs0i-Mw.desc | TAGS,GARBAGE_MT,LATIN_DENSE |
| quest._O6stWM3RR-qJdcvs0i-Mw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.a-g__0y_SGyed_E6IkIrsg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.afDCORKvSI-Vk_Mh2-rnZw.desc | GARBAGE_MT |
| quest.bGdFghCeQfuBhAeMWxJJ8A.name | UNTRANSLATED,NO_CYRILLIC |
| quest.bNVzOxCORxuo_lhAh13r0A.name | NO_CYRILLIC,COLOR |
| quest.bNiieqPgSFqwFpC2DZkj-g.desc | GARBAGE_MT,LATIN_DENSE |
| quest.bPYTUdlkSCiRi0eDHHw7tw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.bz_RazGFSl6k7fUkEt1Lzw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.cejGOPB2QiuW5833Z5ontA.name | NO_CYRILLIC |
| quest.eon8hLumTS-E7MYJ4TFT3w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.fVoSLYPcSmKd-gLhBJHK9A.name | NO_CYRILLIC,COLOR |
| quest.fc7Q6J-BThCf_NbvM0ki2Q.desc | GARBAGE_MT,LATIN_DENSE |
| quest.fnDuNiloR6iXAea0Lhjgtg.desc | GARBAGE_MT |
| quest.gKMT2pblSg69VL5tAtlfxA.name | NO_CYRILLIC,COLOR |
| quest.hEsmeH74S4aOOrROI1AHxQ.desc | PCT_N,COLOR |
| quest.hNdNrT_aSKaYi_TnT7cowA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.hNdNrT_aSKaYi_TnT7cowA.name | NO_CYRILLIC,COLOR |
| quest.h_PK8qnyR9CBUoOhT9nwzA.desc | PCT_N |
| quest.hmQlN9vLSEOyCnCSOOXz7Q.desc | PCT_N,COLOR,LATIN_DENSE |
| quest.iO7VxrxPTbutGjRtrcoAxw.name | NO_CYRILLIC,COLOR |
| quest.jZURYQZlSuitTiiasN4J8A.desc | COLOR,GARBAGE_MT,LATIN_DENSE |
| quest.jlXvqqgIQ_Crha2tW0gEQg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.jreOZVXRQa2sGXViV7-3Gg.desc | PCT_N,COLOR |
| quest.k0ryGOkkSBOgYUcVY-J4rw.name | NO_CYRILLIC,COLOR |
| quest.kBjBqQR5Q-GWh4olyHmXXg.desc | PCT_N |
| quest.kR1YVSq2R4WFu9KNM9lCZQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.kazCPEWoSmiZhR4bkHlEBQ.desc | PCT_N,GARBAGE_MT,LATIN_DENSE |
| quest.l26l6_loSeyuxQYps9XbbA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.lMDEhTDISSG1u2HYaZVg9w.desc | PCT_N,LEAK_MINOR,LATIN_DENSE |
| quest.mr9r3y_kQbWxO2Gm_RvEIg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.n2AqI9hGSEegVf6hfygemQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.nghPgh6-TuSKXUlzGXGrpw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.nghPgh6-TuSKXUlzGXGrpw.name | NO_CYRILLIC,COLOR |
| quest.nx7KEyhlTc6qYVM1vImkBA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.pLCgOVmqTUCudSXZusnceg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.pMGI_sXdQSKWWFFxTunqvA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.r3fKz87vRk23Tv2TRGarvg.name | UNTRANSLATED,NO_CYRILLIC |
| quest.rKrpOyRHRvSF7TeFSskG_A.desc | GARBAGE_MT,LATIN_DENSE |
| quest.rZCrzZ3QTni28BdPZf2-0w.name | UNTRANSLATED,NO_CYRILLIC |
| quest.rdzpjzaCS2epgavzZr6L9A.desc | GARBAGE_MT |
| quest.rlVdurFlSbuoWZAIUG0-aA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.s4B77B7FSamWlvHY8hfqqA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.s6BLu9oMS86AXyR1FQ1imA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.sB_lbhZZRnmZNjJiF8-1Hg.desc | GARBAGE_MT,LATIN_DENSE |
| quest.sB_lbhZZRnmZNjJiF8-1Hg.name | NO_CYRILLIC,COLOR |
| quest.sKLPeimGTFS6_hIyc-SOXA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.tQecVBhjRRyfR3sqeNBrtA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.tXVcSBqQQnS4tF8VoMqr6Q.desc | GARBAGE_MT,LATIN_DENSE |
| quest.u-1Y-eQ-TLyw-WGi5EEnVA.desc | GARBAGE_MT,LATIN_DENSE |
| quest.u-2IsyxKTLiZuTY417qWKw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.uXczmEsfT2uRCSnx8Vm4RQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.vK1Ed8HPTTms4QxfaA_P8Q.desc | GARBAGE_MT,LATIN_DENSE |
| quest.vv296Z3mSUqkQEaiJqQcOw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.vv296Z3mSUqkQEaiJqQcOw.name | UNTRANSLATED,NO_CYRILLIC |
| quest.wLYoO7hsT_SOuJGzbgDMhg.name | NO_CYRILLIC,COLOR |
| quest.x79CeO4ORDWIbPLtdtp1wQ.desc | GARBAGE_MT,LATIN_DENSE |
| quest.y2mOWnXvRe2xWrdvVS297w.desc | GARBAGE_MT,LATIN_DENSE |
| quest.yDY1ALr9QdG8zTbEszNaMw.desc | GARBAGE_MT,LATIN_DENSE |
| quest.ydavD3O5QcKvxk2wIDtakw.name | NO_CYRILLIC,COLOR |
| quest.zIDk7MniRMGE9u_1Slo2qg.desc | GARBAGE_MT,LATIN_DENSE |
| questline.AAAAAAAAAAAAAAAAAAAAIw.name | UNTRANSLATED,NO_CYRILLIC |
| questline.AAAAAAAAAAAAAAAAAAAALQ.desc | GARBAGE_MT,LATIN_DENSE |
| questline.D_aFb1hFQH2PDkN0_KvAEQ.desc | GARBAGE_MT |
