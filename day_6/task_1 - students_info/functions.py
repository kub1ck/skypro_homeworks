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


def get_students_dict() -> dict:
    """
    Переупаковываем словарь о студентах для удобной работы с ним
    """

    students = {}

    for student in load_students():
        students[student['pk']] = {
            'name': student['full_name'],
            'skills': student['skills']
        }

    return students


def get_professions_dict() -> dict:
    """
    Переупаковываем словарь о стеке технологий для удобной работы с ним
    """

    professions = {}

    for profession in load_professions():
        professions[profession['title']] = profession['skills']

    return professions


def get_student_by_pk(pk: int) -> dict:
    """
    Выводим информацию о студенте по его номеру.
    """

    return get_students_dict()[pk]


def get_profession_by_title(title: str) -> list:
    """
    Выводим стек-технологий из списка по его названию.
    """

    return get_professions_dict()[title]



