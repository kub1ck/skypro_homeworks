class User:
    def __init__(self, name):
        self._name = name
        self._total_score = 0
        self._is_answer_correct = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    def update_user_statistics(self, score: int, is_answer_correct: bool) -> None:
        """
        Изменяем количество очков и список с ответами пользователя
        """

        self._total_score += score
        self._is_answer_correct.append(is_answer_correct)

    def show_user_statistics(self) -> None:
        """
        Вывод статистику пользователя
        """

        print(f"Отвечено {self._is_answer_correct.count(True)} из {len(self._is_answer_correct)}",
              f"Набрано баллов: {self._total_score}",
              sep='\n')

    def __repr__(self) -> str:
        return f"Пользователь: {self._name}"
