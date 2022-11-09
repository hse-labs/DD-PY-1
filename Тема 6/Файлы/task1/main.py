filename = "input.txt"
with open(filename) as f:  # open(filename, "rt") режим "rt" по умолчанию, его можно опустить
    for line in f:  # файл умеет построчно возвращать свое содержимое 
        print(line, end="")  # end="", чтобы не задублировать символ переноса строки \n
