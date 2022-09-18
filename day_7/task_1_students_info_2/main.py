from functions import load_students, load_professions
from re import search

STUDENTS: list = load_students()
PROFESSIONS: list = load_professions()


def check_fitness(student: dict, profession: dict) -> dict:
    """
    Формируем словарь с информацией о пригодности студента на специальность.
    """

    student_has: set = set(profession['skills']).intersection(set(student['skills']))
    student_lacks: set = set(profession['skills']).difference(set(student['skills']))
    student_fitness: int = int(len(student_has) / len(profession['skills']) * 100)

    result = {
        "has": list(student_has),
        "lacks": list(student_lacks),
        "fit_percent": student_fitness
    }

    return result


def check_login(student: dict) -> bool:
    """
    Проверка логина на корректность
    """

    student_login: str = student['login']

    # 1 группа: хотя бы одна цифра
    # 2 группа: хотя бы одна заглавная
    # 3 группа: хотя бы одна строчная
    # 4 группа: хотя бы один специальный символ
    # 5 группа: начинается не с заглавной
    # 6 группа: заканчивается не на специальный символ
    pattern: str = r'(?=.*\d)(?=.+[A-Z])(?=.*[a-z])(?=.*[\W|_])(?=^[^A-Z])(?=.+[a-zA-Z\d]$).{4,}'

    return bool(search(pattern, student_login))


def get_profession_by_title(title: str, titles: dict, profession: list) -> dict:
    """
    Получаем стек-технологий из списка по его названию.
    """

    return profession[titles[title]-1]


def get_student_by_pk(pk: int, student: list) -> dict:
    """
    Получаем информацию о студенте по его номеру.
    """

    return student[pk-1]


def main() -> None:
    # Работа с информацией пользователя
    pks: list = []

    for student in STUDENTS:
        pks.append(student['pk'])

    pk: int = int(input("Введите номер пользователя: "))

    if pk not in pks:
        print("У нас нет такого студента")
        quit()

    student_info: dict = get_student_by_pk(pk, STUDENTS)
    student_skills: str = ", ".join(student_info['skills'])
    print(f"Студент {student_info['full_name']}",
          f"Знает: {student_skills}",
          sep='\n')

    # Работа с проверкой логина
    if not check_login(student_info):
        print("\nЛогин данного студента некорректный!")
        quit()

    # Работа с информацией специальностей
    titles: dict = {}

    for i in range(len(PROFESSIONS)):
        titles[PROFESSIONS[i]['title']] = i + 1

    title = input("\nВыберите специальность для оценки студента: ")

    if title not in titles.keys():
        print("У нас нет такой специальности")
        quit()

    profession_info: dict = get_profession_by_title(title, titles, PROFESSIONS)

    # Работа с пригодностью
    student_fitness: dict = check_fitness(student_info, profession_info)
    student_has: str = ", ".join(student_fitness['has'])
    student_lacks: str = ", ".join(student_fitness['lacks'])

    print(f"\nПригодность: {student_fitness['fit_percent']}%",
          f"{student_info['full_name']} знает: {student_has}",
          f"{student_info['full_name']} не знает: {student_lacks}",
          sep='\n')


if __name__ == '__main__':
    main()
