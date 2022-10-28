from typing import Any


def iss(obj_1: Any, obj_2: Any) -> None:
    """
        Принимает два аргумента и выводит результат их сравнения между собой на идентичность и по значению
    """

    ids = {
        True: 'Две переменные ссылаются на один и тот же адрес в памяти',
        False: 'Две переменные ссылаются на разные адреса в памяти'
    }

    values = {
        True: 'имеют одинаковые значения',
        False: 'имеют разные значения'
    }

    obj_1_id = id(obj_1)
    obj_2_id = id(obj_2)

    is_ids = obj_1_id == obj_2_id
    is_values = obj_1 == obj_2

    print('\n' + ids[is_ids] + ', ' + values[is_values])
    print('id первой переменной:', obj_1_id)
    print('id второй переменной:', obj_2_id)
    print('Значение первой переменной:', obj_1)
    print('Значение второй переменной:', obj_2)


def main() -> None:
    A = 'spam'
    B = A
    B = 'shrubbery'
    iss(A, B)

    A = ['spam']
    B = A
    B[0] = 'shrubbery'
    iss(A, B)

    A = ['spam']
    B = A[:]
    B[0] = 'shrubbery'
    iss(A, B)

    iss([], [])
    iss('', '')
    iss({}, {})

    x = y = [1, True, [1, 2]]
    y[2] = [-1, -2]
    iss(x, y)

    x = 5
    y = 5
    iss(x, y)


if __name__ == '__main__':
    main()
