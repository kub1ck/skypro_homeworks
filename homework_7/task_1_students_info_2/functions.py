import json


def load_students() -> list:
    """
    Получаем список, который хранит информацию о студентах из JSON файла
    """

    with open('students.json') as students:
        return json.load(students)


def load_professions() -> list:
    """
    Получаем список, который хранит информацию о стеке технологий из JSON файла
    """

    with open('professions.json') as professions:
        return json.load(professions)




