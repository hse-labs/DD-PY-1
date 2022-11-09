PI = 3.14


def square_circle(r):
    return PI * r ** 2


def length_circle(r):
    return 2 * PI * r


radius = 8  # радиус круга
square = square_circle(radius)
length = length_circle(radius)

print("Площадь равна =", square)
print("Длина окружности равна =", length)
