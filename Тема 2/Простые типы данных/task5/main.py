speed = 4096  # скорость передачи данных в байтах/cек
time = 120  # время в минутах затраченное на скачивание игры
cost = 0.125  # стоимость за один килобайт

speed_in_kb_in_sec = speed / 1024
time_in_sec = time * 60

free_traffic = 500  # количество бесплатного трафика
file_size = time_in_sec * speed_in_kb_in_sec  # размер файла
total_coast = (file_size - free_traffic) * cost  # стоимость файла

print('Размер файла в килобайтах =', file_size)
print('За трафик придется заплатить:', total_coast)
