def check_list_of_str(fn):
    def wrapper(list_of_str):
        incorrect_index_value = [  # собираем индексы, если значение по индексу не строка
            index
            for index, value in enumerate(list_of_str)
            if not isinstance(value, str)
        ]
        if incorrect_index_value:
            raise TypeError(f"Внутри списка по позициям {incorrect_index_value} не строки :(")

        return fn(list_of_str)

    return wrapper


@check_list_of_str
def get_text(list_: list[str]) -> str:
    return ",".join(list_)


if __name__ == "__main__":
    print(get_text(["a", "b", "c"]))

    print(get_text([1, "b", 10]))
