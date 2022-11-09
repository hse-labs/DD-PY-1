import json


FILENAME = "input.json"


def task() -> list[dict]:
    with open(FILENAME) as f:
        json_data = json.load(f)

    return sorted(json_data, key=lambda item: item["id"])


data = task()
print(json.dumps(data, indent=4))
