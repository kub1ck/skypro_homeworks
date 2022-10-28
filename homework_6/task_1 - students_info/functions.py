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


def get_student_by_pk(pk: int, student: list) -> dict:
    """
    Получаем информацию о студенте по его номеру.
    """

    return student[pk-1]


def get_profession_by_title(title: str, titles: dict, profession: list) -> dict:
    """
    Получаем стек-технологий из списка по его названию.
    """

    return profession[titles[title]-1]



