def sub_list_gen(src_list: list, k: int):
    for i in range(len(src_list) // k + 1):
        yield src_list[k * i: k * (i + 1)]


if __name__ == "__main__":
    for sub_list in sub_list_gen([1, 2, 3, 4, 5, 6, 7, 8], 3):
        print(sub_list)
