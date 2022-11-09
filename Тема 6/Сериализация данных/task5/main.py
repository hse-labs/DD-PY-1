import json


FILENAME = "input.json"


def task() -> dict:
    with open(FILENAME) as f:
        json_data = json.load(f)

    return max(json_data, key=lambda item: item["score"])


print(task())
