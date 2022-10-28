from Store import Store
from Shop import Shop
from Request import Request


def add_items_to_store(store_1: Store) -> None:
    """
    Добавление продуктов на склад
    """

    while True:
        print(f"Вместимость на складе: {store_1.capacity}")

        product = input("\nВведите продукт: ")

        # Выход из цикла по стоп слову
        if product.strip().lower() == 'stop':
            break

        amount = int(input(f"Введите количество {product}: "))
        store_1.add(product, amount)

        print("\nСписок товаров на складе: ")
        print(store_1.get_items())

        # Выход из цикла, если вместимость склада закончилась
        if not store_1.capacity:
            break


def add_items_from_store_to_shop(store_1: Store, shop_1: Shop) -> None:
    while True:
        print("\nСписок товаров на складе: ")
        print(store_1.get_items())

        print(f"Вместимость в магазине: {shop_1.capacity}")

        product = input("\nВведите продукт: ")

        # Выход из цикла по стоп слову
        if product.strip().lower() == 'stop':
            break

        amount = int(input(f"Введите количество {product}: "))

        if store_1.is_product(product):
            print("\nДанный продукт присутствует на складе.")

            if store_1.is_amount(product, amount):
                print("\nНужное количество есть на складе.")

                if shop_1.is_add(amount):
                    request = Request('склад', 'магазин', amount, product)

                    store_1.remove(product, amount)
                    print(f"Курьер забрал {amount} {product} со склад")
                    print(request)

                    shop_1.add(product, amount)
                    print(f"Курьер доставил {amount} {product} в магазин")

                else:
                    print("В магазин недостаточно места, попробуйте что то другое")
            else:
                print("Не хватает на складе, попробуйте заказать меньше")
                continue
        else:
            print("Такого продукта на складе нет!")
            continue

        print("\nСписок товаров в магазине: ")
        print(shop_1.get_items())

        # Выход из цикла если не осталось товаров на складе или закончилась вместимость магазина
        if not store_1.get_items() or not shop_1.capacity:
            break


def main() -> None:
    store_1 = Store()
    shop_1 = Shop()

    print("Добавление товаров на склад:")
    add_items_to_store(store_1)

    print("\nПеремещение товаров со склада в магазин:")
    add_items_from_store_to_shop(store_1, shop_1)


if __name__ == '__main__':
    main()
