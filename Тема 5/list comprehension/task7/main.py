def task(num: int) -> bool:
    list_digits = [int(digit) for digit in str(abs(num))]
    return 10 <= sum(list_digits) <= 99


print(task(12))
print(task(555))
print(task(-12))
print(task(-149))
