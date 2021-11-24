from typing import Tuple, List, Dict


def get_tuple() -> Tuple[int, str]:  # кортеж из двух элементов
    return 1, "2"


def get_tuple_ints() -> Tuple[int, ...]:  # кортеж произвольной длины
    return 1, 2, 3, 4


def get_list() -> List[int]:  # внутри все значения типа int
    return [1, 2, 3, 4, 5]


def get_dict() -> Dict[int, list]:  # пара тип ключа - тип значения
    return {1: [2]}
