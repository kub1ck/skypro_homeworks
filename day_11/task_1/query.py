def filter_(list_: list, value: str) -> list:
    """
    Возвращаем список, в котором есть подстроки {value}
    """

    return [x for x in filter(lambda v: value in v, list_)]


def map_(list_: list, value: str) -> list:
    """
    Возвращаем список со столбцами {value}
    """

    return [x[int(value)] for x in map(lambda v: v.split(), list_)]


def unique(list_: list) -> list:
    """
    Возвращаем список без повторяющихся строк
    """

    return list(set(list_))


def limit(list_: list, value: str) -> list:
    """
    Возвращаем список, в котором {value} строк
    """

    return [list_[i] for i in range(int(value))]


def sort_(list_: list, value: str) -> list:
    """
    Возвращаем список, в котором происходит сортировка по {value}
    """

    reverse = False if value == 'asc' else True

    return sorted(list_, reverse=reverse)
