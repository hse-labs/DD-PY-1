import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("first_num",
                        type=int,
                        help="Первое число")
    parser.add_argument("second_num",
                        type=int,
                        help="Второе число")

    namespace = parser.parse_args()

    print(namespace)
    print(namespace.first_num)
    print(namespace.second_num)
