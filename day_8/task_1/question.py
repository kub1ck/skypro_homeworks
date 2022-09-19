class Question:
    def __init__(self, question, answer, difficulty):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty
        self.point = int(self.difficulty) * 10
        self.is_question = False
        self.is_answer = None

    def get_points(self) -> int:
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """

        return self.point

    def is_correct(self, answer: str) -> bool:
        """
        Возвращает True, если ответ пользователя совпадает с верным ответом иначе False.
        """

        return self.answer == answer

    def build_question(self) -> str:
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """

        return f"Вопрос: {self.question}\nСложность: {self.difficulty}/5"

    def build_feedback(self, is_correct: bool) -> str:
        """
        Возвращает одно из двух:
        Ответ верный, получено __ баллов
        Ответ неверный, верный ответ - ...
        """

        if is_correct:
            return f"Ответ верный, получено {self.get_points()} баллов\n"

        return f"Ответ неверный, верный ответ - {self.answer}\n"

