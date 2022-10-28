class Question:
    def __init__(self, question, answer, difficulty):
        self._question = question
        self._answer = answer
        self._difficulty = int(difficulty)
        self._point = 0

    def get_points(self, is_correct_answer: bool) -> int:
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """

        return self._difficulty * 10 if is_correct_answer else self._point

    def is_correct(self, answer: str) -> bool:
        """
        Возвращает True, если ответ пользователя совпадает с верным ответом иначе False.
        """

        return self._answer == answer

    def build_question(self) -> str:
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """

        return f"Вопрос: {self._question}\nСложность: {self._difficulty}/5"

    def build_feedback(self, is_correct: bool, score: int) -> str:
        """
        Возвращает одно из двух:
        Ответ верный, получено __ баллов
        Ответ неверный, верный ответ - ...
        """

        if is_correct:
            return f"Ответ верный, получено {score} баллов\n"

        return f"Ответ неверный, верный ответ - {self._answer}\n"

