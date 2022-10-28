from class_int import Int
from decorator import IntDec


def main():
    x = Int(5)
    y = IntDec(10)

    # x
    print(x + 2)  # 7
    print(x + 2.5)  # 7.5
    print(x + '5')  # 10
    print(x + 'четыре')  # 9
    print(x + 'шесть')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    print(x + 'a')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    print(x + [1])  # TypeError: unsupported operand type(s) for +: 'Int' and 'list'

    # y
    print(y + 5)  # 15
    print(y + 5.5)  # 15.5
    print(y + '3')  # 13
    print(y + 'четыре')  # 14
    print(y + 'шесть')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    print(y + 'a')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    print(y + {1})  # TypeError: unsupported operand type(s) for +: 'Int' and 'set'


if __name__ == '__main__':
    main()
