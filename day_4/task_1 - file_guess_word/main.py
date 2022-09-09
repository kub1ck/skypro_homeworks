from random import sample


def create_file_word() -> None:
    """
    Формируем файл со словами
    """

    with open('words.txt', 'w') as file:
        file.write('python\n')
        file.write('squirrel\n')
        file.write('flask\n')
        file.write('cucumbers\n')


def get_words() -> list:
    """
    Формируем словарь слов из файла
    """

    words = []

    with open('words.txt') as file:
        for word in file:
            words.append(word.strip())

    return words


def get_word_random_letters(word: str) -> str:
    """
    Меняем местами буквы в слове
    """

    return ''.join(sample(word, len(word)))


def guess_words(words: list) -> int:
    """
    Пользователь пытается угадать слово.
    Формируем статистику, исходя верных ответов
    """

    total = 0  # Кол-во очков

    for word in words:
        word_random_letters = get_word_random_letters(word)

        print(f"\nУгадайте слово: {word_random_letters}")
        user_input = input("Ваш ответ: ")

        if user_input == word:
            print("Верно! Вы получаете 10 очков!")
            total += 10
        else:
            print(f"Неверно! Верный ответ – {word}")

    return total


def update_history(user_name: str, total: int) -> None:
    """
    Обновление истории
    """

    with open('history.txt', 'a') as file:
        file.write(f"{user_name} - {total}\n")


def get_stats() -> list:
    """
    Формирование статистики
    """

    total = 0  # Кол-во игр
    larger = 0  # Наибольший балл

    with open('history.txt') as file:
        for line in file:
            total += 1
            user_score = int(line.strip().split()[2])

            if user_score >= larger:
                larger = user_score

    return [total, larger]


def show_stats() -> None:
    """
    Вывод статистики
    """

    total_game, largest_score = get_stats()

    print(f"\nВсего игр сыгранно: {total_game}",
          f"Максимальный рекорд: {largest_score}",
          sep='\n')


def main() -> None:
    user_name = input("Введите ваше имя: ")

    create_file_word()
    words = get_words()

    total = guess_words(words)
    update_history(user_name, total)
    show_stats()


if __name__ == '__main__':
    main()
