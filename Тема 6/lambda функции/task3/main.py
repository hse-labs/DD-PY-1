def task(points: list) -> tuple:
    return max(points, key=lambda point: (point[0] ** 2 + point[1] ** 2) ** 0.5)


pts = [
    (4.5, 3),
    (2.1, -1),
    (6.8, -3),
    (1.4, 2.9)
]

print(task(pts))
