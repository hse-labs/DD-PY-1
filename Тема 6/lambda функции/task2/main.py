def task() -> str:
    list_words = [
        "Blue",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return max(list_words, key=len)


print(task())
