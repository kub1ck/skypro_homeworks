import functions

STUDENTS = functions.load_students()
PROFESSIONS = functions.load_professions()


def check_fitness(student: dict, profession: dict) -> dict:
    """
    Формируем словарь с информацией о пригодности студента на специальность.
    """

    student_has = set(profession['skills']).intersection(set(student['skills']))
    student_lacks = set(profession['skills']).difference(set(student['skills']))
    student_fitness = int(len(student_has) / len(profession['skills']) * 100)

    result = {
        "has": list(student_has),
        "lacks": list(student_lacks),
        "fit_percent": student_fitness
    }

    return result


def main() -> None:
    # Работа с информацией пользователя
    pks = []

    for student in STUDENTS:
        pks.append(student['pk'])

    pk = int(input("Введите номер пользователя: "))

    if pk not in pks:
        print("У нас нет такого студента")
        quit()

    student_info = functions.get_student_by_pk(pk, STUDENTS)
    student_skills = ", ".join(student_info['skills'])
    print(f"Студент {student_info['full_name']}",
          f"Знает: {student_skills}",
          sep='\n')

    # Работа с информацией специальностей
    titles = {}

    for i in range(len(PROFESSIONS)):
        titles[PROFESSIONS[i]['title']] = i + 1

    title = input("\nВыберите специальность для оценки студента: ")

    if title not in titles.keys():
        print("У нас нет такой специальности")
        quit()

    profession_info = functions.get_profession_by_title(title, titles, PROFESSIONS)

    # Работа с пригодностью
    student_fitness = check_fitness(student_info, profession_info)
    student_has = ", ".join(student_fitness['has'])
    student_lacks = ", ".join(student_fitness['lacks'])

    print(f"\nПригодность: {student_fitness['fit_percent']}%",
          f"{student_info['full_name']} знает: {student_has}",
          f"{student_info['full_name']} не знает: {student_lacks}",
          sep='\n')


if __name__ == '__main__':
    main()
