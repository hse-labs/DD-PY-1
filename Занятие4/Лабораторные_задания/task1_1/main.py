import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r"""####\s+(?P<position>\d+)\.\s+\[(?P<book>.+?)\]\((?P<book_url>.+?)\)\s+by\s+(?P<author>.+?)\s+\((?P<recommended>\d{1,3}\.\d+%)\s+recommended\)\s+!\[.*?\]\((?P<cover_url>.+?)\)\s+\"(?P<description>.+?)\"\s+\[.*?\]\(.*?\)"""
OUTPUT_FILE = "output.txt"  # название файла для сохранения отсортированных книг

def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4, ensure_ascii=False))

    # list_books = [book for book in book_pattern.finditer(f.read())]
    # list_books = sorted(list_books, key=lambda book_dict: book_dict["position"])
    # with open(OUTPUT_FILE, "w") as f:
    #     json.dump(list_books, f, indent=4)


if __name__ == '__main__':
    task()
