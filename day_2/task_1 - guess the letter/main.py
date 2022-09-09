WORDS_LETTERS = {
    "mouse": 2,
    "difficult": 7,
    "surprise": 7
}

ANSWERS_STATS = {
    False: "не угадано!",
    True: "угадано!"
}

user_stats = {}


def input_name() -> str:
    """
    Ввод имени и проверка на корректность (цифры и пробелы в имени)
    """

    print("Привет, напиши, пожалуйста, имя!",
          "Оно должно быть без пробелов, цифр и заглавных букв.",
          sep='\n')

    while True:
        user_name = input("Имя: ")

        if ' ' in user_name:  # Пробелы
            print("\nКажется, в имени пользователя есть пробелы.")
        elif not user_name.isalpha():  # Цифры и спец символы
            print("\nКажется, в имени пользователя есть цифры или спец символы.")
        elif user_name != user_name.lower():
            print("\nИмя пользователя не может содержать заглавных букв.")
        else:
            print(f"\nОтлично, {user_name}, давай начнем тренировку!")
            return user_name


def game() -> None:
    """
    Формирование статистики игрока, исходя из введенных ответов
    """

    word_index = 1  # Номер слова

    for word, index in WORDS_LETTERS.items():
        word_with_hidden_letter = word.replace(word[index-1], '*')  # Получаем слово со звездочкой

        user_letter = input(f"\nВставьте пропущенную букву в слове {word_with_hidden_letter}: ")

        # Заполнение словаря статистики
        if user_letter == word[index-1]:
            print("Ответ верный")
            user_stats[word_index] = True
        else:
            print(f"Ответ неверный. Верный ответ – {word}")
            user_stats[word_index] = False

        word_index += 1


def show_stats(user_name: str) -> None:
    """
    Вывод статистики
    """

    index = 1  # Номер результата ответа игрока

    print(f"\nВот и все, {user_name}\n")

    for word in WORDS_LETTERS.keys():
        print(f"{index} - {word} - {ANSWERS_STATS[user_stats[index]]}")
        index += 1


def main():
    user_name = input_name()
    game()
    show_stats(user_name)


if __name__ == "__main__":
    main()
