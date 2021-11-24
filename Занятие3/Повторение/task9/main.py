from typing import Union


Number = Union[int, float]  # alias


def sum_(*args: Number) -> Number:
    total: Number = 0
    for arg in args:
        total += arg

    return total


if __name__ == "__main__":
    sum_(1, 2, 3.0, 5)  # OK
    sum_(1, 2, 3.0, "5")  # str не является ни int, ни float
