```python
# импортируем модуль JSON
import json
```

Основные методы:
- `json.dumps(obj)` – преобразует объект в строку формата JSON
- `json.loads(str)` – преобразует строку формата JSON в объект языка Python (выдает `ValueError`, если строка неверная)

Имейте в виду результат декодирования не всегда эквивалентен исходному объекту. Например, кортежи сериализуются в списки.
