def decorator(function):
    def inner(self, other):
        values = {
            '1': 1, 'один': 1,
            '2': 2, 'два': 2,
            '3': 3, 'три': 3,
            '4': 4, 'четыре': 4,
            '5': 5, 'пять': 5
        }

        if isinstance(other, int | float):
            return function(self, other)

        if isinstance(other, str):
            if other in values:
                value = values[other]
                return function(self, value)
            else:
                return 'TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 до 5.'

        return f"TypeError: unsupported operand type(s) for +: 'Int' and {str(type(other)).split()[1][:-1]}"

    return inner


class IntDec(int):
    @decorator
    def __add__(self, other):
        return super().__add__(other)

