import json


FILENAME = "input.json"


def task() -> dict:
    with open(FILENAME) as f:
        json_data = json.load(f)

    list_values = [item["contains_improvement_appeals"] for item in json_data]
    return sum(list_values)


print(task())
