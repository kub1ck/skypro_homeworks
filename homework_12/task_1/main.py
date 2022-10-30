from StaticArray import StaticArray


def main():
    # Объявление массива с длиной 10
    array = StaticArray(10)

    # Заполнение массива
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(10):
        array.add(i)

    array.add(1)  # Ошибка

    # Вставка элемента
    array.insert(5, 50)  # [0, 1, 2, 3, 4, 50, 5, 6, 7, 8]

    # Удаление элемента
    array.delete(5)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]

    array.add(9)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    main()
