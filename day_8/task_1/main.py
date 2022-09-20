from Question import Question
from User import User
from list_file import get_questions
from random import shuffle


def main() -> None:
    print("Добро пожаловать в игру!")
    user_name = input("Ваше имя: ")

    user = User(user_name)
    questions = [
        Question(question['question'], question['answer'], question['difficulty']) for question in get_questions()
    ]

    shuffle(questions)  # Перемешиваем вопросы

    print("Игра начинается!\n")

    for question in questions:
        # Выводим вопрос в нормальной форме
        print(question.build_question())

        # Работа с ответом
        user_answer = input("Ваш ответ: ")
        is_correct = question.is_correct(user_answer)
        score = question.get_points(is_correct)

        # Обновляем статистику пользователя
        user.update_user_statistics(score, is_correct)

        # Выводим комментарий на ответ пользователя
        print(question.build_feedback(is_correct, score))

    print(f"Вот и все!")
    user.show_user_statistics()


if __name__ == "__main__":
    main()
