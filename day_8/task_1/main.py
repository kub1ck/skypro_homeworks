from question import Question
from list_file import get_questions
from random import choice


def update_statistics(question: Question, is_correct: bool, scores: int, correct_answers: int) -> tuple[int, int]:
    """
    Обновляем статистику игрока, а именно сумму его баллов и количество верных ответов
    """

    if is_correct:
        scores += question.get_points()

    correct_answers += is_correct

    return scores, correct_answers


def main() -> None:
    questions = get_questions()  # Список вопросов
    total_questions = len(questions)  # Количество вопросов
    correct_answers = 0
    scores = 0

    print("Игра начинается!\n")

    # Итерируемся до тех пор, пока словарь не станет пустым
    while questions:
        # Выбираем случайный вопрос
        random_question = choice(questions)
        questions.remove(random_question)
        question = Question(random_question['question'], random_question['answer'], random_question['difficulty'])

        # Выводим вопрос в нормальной форме
        print(question.build_question())

        # Работа с ответом
        user_answer = input("Ваш ответ: ")
        is_correct = question.is_correct(user_answer)

        # Выводим комментарий на ответ пользователя
        print(question.build_feedback(is_correct))

        # Обновляем статистику
        scores, correct_answers = update_statistics(question, is_correct, scores, correct_answers)

    print(f"Вот и все!",
          f"Отвечено {correct_answers} из {total_questions}",
          f"Набрано баллов: {scores}",
          sep='\n')


if __name__ == "__main__":
    main()
