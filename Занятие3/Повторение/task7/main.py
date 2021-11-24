from typing import Optional, Union


def get_index(list_: list[int], value: int) -> Optional[int]:  # Union[int, None] индекс или None
    for index, current_value in enumerate(list_):
        if current_value == value:
            return index
    return None


def get_bool_or_none() -> Optional[bool]:  # None тоже может быть воспринят как False
    ...
