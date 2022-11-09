from typing import Any


def index(list_: list, value: Any) -> int:
    for i, current_value in enumerate(list_):
        if current_value == value:
            return i

    raise ValueError("Значение не найдено")


list_items = [1, 2, "3", 1]
print(index(list_items, 1) == list_items.index(1))  # True
