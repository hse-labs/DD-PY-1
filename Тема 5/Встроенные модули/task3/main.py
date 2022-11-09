from random import randint

start = -100
stop = 100
count = 50
list_numbers = [randint(start, stop) for _ in range(count)]

negative_numbers = [num for num in list_numbers if num < 0]
print(len(negative_numbers))
