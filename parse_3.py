import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count",
                        default=5,
                        type=int,
                        help="...")
    parser.add_argument("-name",
                        default="World",
                        type=str)
    # Namespace(count=5, name='test')

    namespace = parser.parse_args()
    print(namespace)

    for _ in range(namespace.count):
        print(f"Hello, {namespace.name}")
