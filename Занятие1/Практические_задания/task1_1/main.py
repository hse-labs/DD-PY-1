def get_distance(point: tuple) -> int:  # 5. Подставляем отдельный point из списка points, который имеет значение из pts
    return (point[0] ** 2 + point[1] ** 2) ** 0.5


def task(points: list) -> list:  # 3. в аргумент points передается значение pts
    return list(map(get_distance, points))  # 4. В get_distance будут подставляться кортежи из points


if __name__ == "__main__":
    pts = [  # 1. глобальная переменная
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    print(task(pts))  # 2. передаем в функцию значение глобальной переменной
