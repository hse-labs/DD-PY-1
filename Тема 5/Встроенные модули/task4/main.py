from random import randint


def get_random_number() -> int:
    random_digits = [randint(0, 9) for _ in range(3)]
    str_number = "".join([str(digit) for digit in random_digits])

    return int(str_number)


print(get_random_number())
