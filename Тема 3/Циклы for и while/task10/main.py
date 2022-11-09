list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

count_even = 0  # количество четных чисел
count_odd = 0  # количество нечетных чисел

for value in list_:  # перебираем все числа
    if value % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

if count_even > count_odd:
    print('Четных чисел больше')
elif count_even < count_odd:
    print('Нечетных чисел больше')
else:
    print('Четных и нечетных одинаковое количество')
