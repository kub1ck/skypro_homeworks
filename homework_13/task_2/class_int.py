class Int(int):
    def __add__(self, other):
        values = {
            '1': 1, 'один': 1,
            '2': 2, 'два': 2,
            '3': 3, 'три': 3,
            '4': 4, 'четыре': 4,
            '5': 5, 'пять': 5
        }

        if isinstance(other, int | float):
            return super().__add__(other)

        if isinstance(other, str):
            if other in values:
                value = values[other]
                return super().__add__(value)
            else:
                raise TypeError('TypeError: справа от знака "+" непонятный текст. ',
                                'Если что, я понимаю текстом цифры с 1 до 5.')

        return super().__add__(other)
