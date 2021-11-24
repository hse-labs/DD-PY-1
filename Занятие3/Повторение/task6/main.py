from typing import Union


def set_int_or_float(num: Union[int, float]):
    return num


def set_int(int_number: int):
    return int_number


def set_float(float_number: float):
    return float_number


if __name__ == "__main__":
    set_int_or_float(1)  # OK
    set_int_or_float(1.0)  # OK

    set_int(1)  # OK
    set_int(1.0)  # int не ожидает float

    set_float(1)  # OK float ожидает int
    set_float(1.0)  # OK
