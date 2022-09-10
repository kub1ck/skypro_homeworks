from random import choice

letters_total_dict = {
    "а": 8, "б": 2, "в": 4, "г": 2, "д": 4, "е": 8, "ё": 1, "ж": 1, "з": 2, "и": 5, "й": 1, "к": 4,
    "л": 4, "м": 3, "н": 5, "о": 10, "п": 4, "р": 5, "с": 5, "т": 5, "у": 4, "ф": 1, "х": 1, "ц": 1,
    "ч": 1, "ш": 1, "щ": 1, "ъ": 1, "ы": 2, "ь": 2, "э": 1, "ю": 1, "я": 2
}


def show_winner(users_name: dict, users_score: dict) -> None:
    """
    Вывод итога игры
    """

    if users_score[0] > users_score[1]:
        print(f"\nВыигрывает: {users_name[0]}")
    elif users_score[0] < users_score[1]:
        print(f"\nВыигрывает: {users_name[1]}")
    else:
        print("\nНичья")

    print(f"Счет {users_score[0]}:{users_score[1]}")


def get_score(score: int) -> int:
    """
    Получение очков
    """

    return score if score <= 3 else score + 2


def remove_letters(user_letters: list, used_letters: list) -> None:
    """
    Удаляем из списка, использованные буквы
    """

    for letter in used_letters:
        user_letters.remove(letter)


def check_word(user_word: str, words: list) -> bool:
    """
    Проверяем, имеется ли введенное слово в файле
    """

    return user_word in words


def get_words() -> list:
    """
    Возвращаем список возможных слов
    """

    with open('russian_word.txt', encoding='utf-8') as file:
        return file.read().split()


def check_letters(user_word: str, user_letters: list) -> bool:
    """
    Проверяем, используемые буквы из введенного слова в списке
    """

    temp_letters = user_letters.copy()

    for letter in user_word:
        if letter in temp_letters:
            temp_letters.remove(letter)
        else:
            return False
    else:
        return True


def get_letter() -> str:
    """
    Получение случайной буквы из словаря
    """

    random_letter = choice(list(letters_total_dict))
    letters_total_dict[random_letter] -= 1

    if not letters_total_dict[random_letter]:
        del letters_total_dict[random_letter]

    return random_letter


def add_user_letters(total_letters=7) -> list:
    """
    Добавление букв в список пользователя
    """

    new_letters = []

    if sum(letters_total_dict.values()) < total_letters:
        total_letters = sum(letters_total_dict.values())

    for _ in range(total_letters):
        new_letters.append(get_letter())

    return new_letters


def main():
    print("Привет.\nМы начинаем играть в Scrabble")

    user_name_1 = input("\nКак зовут первого игрока?\nИмя: ")
    user_name_2 = input("\nКак зовут второго игрока?\nИмя: ")

    print(f"\n{user_name_1} vs {user_name_2}\n\n(раздаю случайные буквы...)")
    user_letters_1 = add_user_letters()
    user_letters_2 = add_user_letters()

    print(f"{user_name_1} - буквы: {user_letters_1}",
          f"{user_name_2} - буквы: {user_letters_2}",
          sep='\n')

    users_name = {
        0: user_name_1,
        1: user_name_2
    }

    users_letters = {
        0: user_letters_1,
        1: user_letters_2
    }

    users_score = {
        0: 0,
        1: 0
    }

    turn_order = 0  # Очередь
    used_words = []
    words = get_words()

    # Основной цикл игры
    while True:
        print(f"\nХодит {users_name[turn_order]}")
        print(f"Буквы: {users_letters[turn_order]}")
        user_word = input("Ваш ответ: ").lower().strip()

        # Завершение игры, если введено слово 'stop'
        if user_word == 'stop':
            break

        # Проверяем, введены ли только буквы из списка возможных букв пользователя
        if check_letters(user_word, users_letters[turn_order]):

            # Проверяем, есть ли введенное слово в искомом файле и не вводили ли его ранее
            if check_word(user_word, words):
                print("\nТакое слово есть.")
                words.remove(user_word)

                # Получение и начисление очков
                score = get_score(len(user_word))
                users_score[turn_order] += score

                # Удаление букв
                total_letters = len(user_word) + 1
                remove_letters(users_letters[turn_order], list(user_word))

            else:
                score = 0
                total_letters = 1
                print("\nТакого слова нет")

            print(f"{users_name[turn_order]} получает {score} баллов.")

            # Добавление букв
            new_letters = add_user_letters(total_letters)
            users_letters[turn_order].extend(new_letters)
            print(f"Добавляю буквы: {new_letters}")

            # Если у кого-то заканчиваются буквы, а также словарь пусть, то конец игры
            if not users_letters[turn_order]:
                break

        else:
            print("\nСлово нужно составлять только из тех букв, которые есть в Вашем списке!")
            continue

        turn_order = 1 if not turn_order else 0  # Смена очереди

    show_winner(users_name, users_score)


if __name__ == '__main__':
    main()
