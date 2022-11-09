import json

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"


def task() -> None:
    with open(INPUT_FILE) as f:
        json_data = json.load(f)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)


task()

with open(OUTPUT_FILE) as output_f:
    for line in output_f:
        print(line, end="")
