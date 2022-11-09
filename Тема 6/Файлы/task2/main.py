filename = "output.txt"

with open(filename, "w") as f:  # "w" равносильно "wt"
    f.write("test" + "\n")  # вручную добавляем "\n"

with open(filename, "a", encoding="utf-8") as f:  # открываем файл в режиме дозаписи
    list_words = ["Один\n", "Два\n", "Три\n"]  # вручную добавляем "\n" к каждой строке
    f.writelines(list_words)  # записываем сразу много строк

with open(filename) as f:
    print(f.readlines())  # записываем сразу все строки из файла
