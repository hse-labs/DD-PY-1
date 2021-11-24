from traceback import print_exc


def concat_str_without_typing(word1, word2):
    return word1 + word2


def concat_str_with_output_typing(word1, word2) -> str:
    return word1 + word2


if __name__ == "__main__":
    result_str_without_typing = concat_str_without_typing("word1", "word2")
    result_str_without_typing

    result_int_without_typing = concat_str_without_typing(1, 2)
    result_int_without_typing

    result_str_with_output_typing = concat_str_with_output_typing("word1", "word2")
    result_str_with_output_typing

    result_int_with_output_typing = concat_str_with_output_typing(1, 2)  # incorrect
    try:
        result_int_with_output_typing.lower()
    except AttributeError:
        print_exc()
