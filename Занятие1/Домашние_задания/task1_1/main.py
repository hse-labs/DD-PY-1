def enumerate_(iterable_):
    return zip(range(len(iterable_)), iterable_)


if __name__ == "__main__":
    for index, value in enumerate_("abc"):
        print(index, value)
