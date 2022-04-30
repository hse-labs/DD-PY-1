def min_list_items(fn):
    def wrapper(list_arg):
        if not isinstance(list_arg, list):
            raise TypeError(f"Аргумент функции {fn.__name__} должен быть списком.")

        if not list_arg:  # если список пустой
            raise ValueError(f"Минимальное количество элементов в списке = 1.")

        return fn(list_arg)

    return wrapper


@min_list_items
def return_list(list_: list):
    return []


@min_list_items
def return_tuple(str_: str):
    return ""


if __name__ == "__main__":
    return_list([1, 2, 3])
    return_tuple("123")
