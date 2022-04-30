import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers",
                        type=int,
                        nargs="+",
                        help="Набор чисел")

    namespace = parser.parse_args()

    print(namespace.numbers)
    print(sum(namespace.numbers))
