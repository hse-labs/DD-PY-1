from typing import Any


def remove(list_: list, value: Any) -> list:
    last_index_value = None  # не знаем есть ли значение в списке
    for i, current_value in enumerate(list_):
        if current_value == value:
            last_index_value = i

    if last_index_value is None:
        raise ValueError("Значение не найдено")
    else:
        return list_[:last_index_value] + list_[last_index_value + 1:]


print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
