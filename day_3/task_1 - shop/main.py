user_coins = [1, 1, 2, 5, 5, 5]
user_products = []
shop_coins = [1, 1, 2, 2, 2, 1]
shop_products = {
    'Молоко': 2,
    'Хлеб': 1,
    'Вафли': 2,
    'Лосось': 5,
    'Свинина': 3,
    'Курица': 3,
    'Масло': 2,
    'Вода': 1,
    'Шоколад': 1
}


def print_shop_info() -> None:
    """
    Вывод информации о товарах и монетах магазина
    """

    print("-" * 40)
    print("Доступные товары и их цена:")

    for product, value in shop_products.items():
        print(f"{product} - {value}м.")

    print(f"\nМонеты в кассе: {shop_coins}")
    print("-" * 40)


def print_user_info() -> None:
    """
    Вывод информации о монетах пользователя и списке купленных продуктов
    """

    print(f"У вас в кошельке монет: {user_coins}")

    if user_products:
        print(f"Вы купили: {user_products}")


def check(user_input: str) -> None:
    """
    Проверка на продукт, монеты и возможность выдачи сдачи
    """

    # Проверяем наличие продукта
    if user_input in shop_products:
        shop_coin = shop_products[user_input]

        # Проверяем наличие монетки, равной цене продукта 1 в 1
        if shop_coin in user_coins:
            user_coins.remove(shop_coin)
            user_products.append(user_input)
            del shop_products[user_input]
        else:
            for coin in user_coins:
                if shop_coin < coin:
                    delta = coin - shop_coin  # Сдача

                    if delta in shop_coins:
                        user_coins.remove(coin)
                        user_coins.append(delta)
                        user_products.append(user_input)

                        shop_coins.remove(delta)
                        del shop_products[user_input]
                        break
                    else:
                        print("Магазин не может выдать сдачу.")
            else:
                print("Нет денег")

    else:
        print("К сожалению, такого товара нет.")


def main() -> None:
    while True:
        print_shop_info()
        print_user_info()

        # Выходим, если у пользователя закончились деньги
        if not user_coins:
            break

        user_input = input("Что хотите купить?\nВаш выбор: ")

        # Выходим, если пользователь написал stop
        if user_input == 'stop':
            break

        check(user_input)


if __name__ == '__main__':
    main()
