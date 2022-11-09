Дан список точек, найти самую удаленную точку от начала координат.  
Точки даны в формате кортежа (x, y).

Студент не знал про lambda функции, и записал функцию `get_distance`, которая нигде больше ни пригодилась.
Замените функцию `get_distance` на `lambda` функцию.

```python
def get_distance(point: tuple) -> int:
    return (point[0] ** 2 + point[1] ** 2) ** 0.5


def task(points: list) -> tuple:
    return max(points, key=get_distance)
```
