def task(words: list) -> list:
    return [word.upper() for word in words]


list_words = [
    "Goldenrod",
    "Purple",
    "Salmon",
    "Turquoise",
    "Cyan"
]

print(task(list_words))
