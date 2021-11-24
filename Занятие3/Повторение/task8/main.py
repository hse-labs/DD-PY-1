from typing import Iterator


def count(start: int = 1, step: int = 1) -> Iterator[int]:
    while True:
        yield start
        start += step


if __name__ == "__main__":
    for num in count():
        print(num)
