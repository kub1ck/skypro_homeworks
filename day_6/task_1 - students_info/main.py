import functions

# Удобные словари для работы
students = functions.get_students_dict()
professions = functions.get_professions_dict()


def check_fitness(student: dict, profession: list) -> dict:
    """
    Формируем словарь с информацией о пригодности студента на специальность.
    """

    student_has = set(profession).intersection(set(student['skills']))
    student_lacks = set(profession).difference(set(student['skills']))
    student_fitness = int(len(student_has) / len(profession) * 100)

    result = {
        "has": list(student_has),
        "lacks": list(student_lacks),
        "fit_percent": student_fitness
    }

    return result


def check_title(title: str) -> bool:
    """
    Проверяем, есть ли специальность по названию.
    """

    return title in professions.keys()


def check_pk(pk: int) -> bool:
    """
    Проверяем, имеется ли пользователь с таким номером.
    """

    return pk in students.keys()


def main() -> None:
    # Работа с информацией пользователя
    pk = int(input("Введите номер пользователя: "))

    if not check_pk(pk):
        print("У нас нет такого студента")
        quit()

    student_info = functions.get_student_by_pk(pk)
    student_skills = ", ".join(student_info['skills'])
    print(f"Студент {student_info['name']}",
          f"Знает: {student_skills}",
          sep='\n')

    # Работа с информацией специальностей
    title = input("\nВыберите специальность для оценки студента: ")

    if not check_title(title):
        print("У нас нет такой специальности")
        quit()

    profession_info = functions.get_profession_by_title(title)

    # Работа с пригодностью
    student_fitness = check_fitness(student_info, profession_info)
    student_has = ", ".join(student_fitness['has'])
    student_lacks = ", ".join(student_fitness['lacks'])

    print(f"\nПригодность: {student_fitness['fit_percent']}%",
          f"{student_info['name']} знает: {student_has}",
          f"{student_info['name']} не знает: {student_lacks}",
          sep='\n')


if __name__ == '__main__':
    main()
