def hash_func(key: str) -> int:
    hash_value = 0
    table_size = 1000

    for symbol in key:
        hash_value += ord(symbol)

    hash_value %= table_size

    return hash_value


def main():
    print(hash_func('Яблоко'))
    print(hash_func('Яблоки'))
    print(hash_func('Апельсин'))
    print(hash_func('Абрикос'))


if __name__ == '__main__':
    main()
