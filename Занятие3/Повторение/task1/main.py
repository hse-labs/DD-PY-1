def concat_str_without_typing(word1, word2):
    return word1 + word2


def concat_str_with_typing(word1: str, word2: str):
    return word1 + word2


if __name__ == "__main__":
    concat_str_without_typing("word1", "word2")
    concat_str_without_typing(1, 2)

    concat_str_with_typing("word1", "word2")
    concat_str_with_typing(1, 2)
