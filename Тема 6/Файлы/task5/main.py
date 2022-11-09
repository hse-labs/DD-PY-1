INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, "r") as input_file:
        with open(OUTPUT_FILE, "w") as output_file:
            for line in input_file:
                output_file.write(line.upper())


task()

with open(OUTPUT_FILE) as file:
    for line in file:
        print(line, end="")
