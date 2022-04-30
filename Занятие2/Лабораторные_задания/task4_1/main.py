def float_range(*args):
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError

    start = 0  # по умолчанию начинаем с 0
    stop = None  # нет значения по умолчанию
    step = 1  # по умолчанию с шагом 1

    if len(args) == 1:
        stop, = args  # указана только правая граница
    elif len(args) == 2:
        start, stop = args  # указана левая и правая граница
    elif len(args) == 3:
        start, stop, step = args  # указана левая и правая граница и шаг
    else:
        raise ValueError("Неверное количество аргументов. Аргументов может быть от 1 до 3")

    while start < stop:
        yield start
        start += step


if __name__ == '__main__':
    for num in float_range(5):
        print(num)

    for num in float_range(5.5, 10):
        print(num)

    for num in float_range(1, 10, 1.5):
        print(num)
