def endless_geom_progression(start, step):
    while True:
        yield start
        start *= step


if __name__ == "__main__":
    iterator = endless_geom_progression(1, 10)
    for _ in range(10):
        print(next(iterator))
