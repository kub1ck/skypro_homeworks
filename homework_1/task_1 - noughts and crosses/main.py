users_answers = {
    1: [],
    2: []
}

users_mark = {
    1: "X",
    2: "O"
}


def print_board() -> None:
    """
    Вывод поля
    """

    print('\n-------------')

    for i in range(9):
        if i+1 in users_answers[1]:
            print("| X", end=' ')
        elif i+1 in users_answers[2]:
            print("| O", end=' ')
        else:
            print(f"| {i+1}", end=' ')

        if (i+1) % 3 == 0:
            print("|")
            print('-------------')


def take_input() -> int:
    """
    Принимаем ввод, а также проверяем на корректность
    """

    while True:
        user_input = input("Ваш ответ: ")

        # Проверяем, введена ли цифра
        if user_input.isdigit():
            user_input = int(user_input)

            # Проверяем, входит ли цифра в интервал и ее уникальность
            if 0 < user_input < 10 and user_input not in users_answers[1] and user_input not in users_answers[2]:
                return user_input
            else:
                print(f"\nНужно ввести число от 1 до 9, кроме {*users_answers[1], *users_answers[2]}")
        else:
            print("\nНужно ввести цифру!")


def check_victory(turn_order: int) -> bool:
    """
    Определяем победителя
    """

    # Всевозможные выигрышные комбинации
    win_combinations = ((1, 2, 3), (4, 5, 6), (7, 8, 9),  # Выигрыш по горизонтали
                        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Выигрыш по вертикали
                        (1, 5, 9), (3, 5, 7))             # Выигрыш по диагонали

    # Проверяем, есть ли выигрышная комбинация у игрока
    for combination in win_combinations:
        if set(combination).issubset(users_answers[turn_order]):
            return True

    return False


def main():
    users_name = {
        1: input("Имя первого игрока: ").strip().capitalize(),
        2: input("Имя второго игрока: ").strip().capitalize()
    }
    turn_order = 1  # Очередь игрока

    print_board()

    while True:
        print(f"\nХодит игрок {users_name[turn_order]}",
              f"Куда ставить {users_mark[turn_order]}?",
              sep='\n')

        users_answers[turn_order].append(take_input())
        print_board()

        if check_victory(turn_order):
            print(f"\nПобедил {users_name[turn_order]}")
            break

        if len(users_answers[1]) + len(users_answers[2]) == 9:
            print("\nНичья")
            break

        # Смена очереди
        turn_order = 2 if turn_order == 1 else 1


if __name__ == '__main__':
    main()
