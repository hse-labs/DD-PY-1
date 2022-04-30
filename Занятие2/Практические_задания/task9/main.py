def some_func(arg, kwarg=1):
    print(f"some_func(arg={arg}, kwarg={kwarg})")


if __name__ == "__main__":
    some_func({"arg": "value"})  # some_func(arg={'arg': 'value'}, kwarg=1)
    some_func(**{"arg": "value"})  # some_func(arg=value, kwarg=1)

    dict_kwargs = {  # важно что бы ключи совпадали с названием аргументов, иначе ошибка :(
        "kwarg": "new_value",
        "arg": 1,
    }
    some_func(**dict_kwargs)  # some_func(arg=1, kwarg=new_value)
