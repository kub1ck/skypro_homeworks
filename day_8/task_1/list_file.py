import json


def get_questions() -> list:
    """
    Возвращаем список, который хранит информацию о вопросах из JSON файла
    """

    with open('questions.json') as file:
        return json.load(file)
