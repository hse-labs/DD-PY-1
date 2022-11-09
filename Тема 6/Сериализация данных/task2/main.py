import json

OUTPUT_FILE = "output.json"


python_obj = {
    "русские слова": "c ними беда :(("
}
print(json.dumps(python_obj))
print(json.dumps(python_obj, ensure_ascii=False))  # ensure_ascii корректно отображает русский язык
print(json.dumps(python_obj, indent=4, ensure_ascii=False))  # indent форматирует отступы

with open(OUTPUT_FILE, "w") as f:
    json.dump(python_obj, f, indent=4, ensure_ascii=False)  # пишет строку сразу в файл

with open(OUTPUT_FILE) as f:
    python_obj_from_json_file = json.load(f)  # считываем json строку из файла и сразу преобразуем в python объект
    print(python_obj_from_json_file)
