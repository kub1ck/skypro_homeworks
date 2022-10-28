from Storage import Storage


class Store(Storage):
    def __init__(self, capacity: int = 100) -> None:
        super().__init__()
        self._capacity = capacity

    def add(self, product: str, amount: int) -> None:
        if self.is_add(amount):
            super().add(product, amount)
        else:
            print("Вы ввели кол-во продуктов больше, чем вместимость")

    def is_add(self, amount: int) -> bool:
        return self._capacity >= amount

    def remove(self, product: str, amount: int) -> None:
        if amount == self._items[product]:
            del self._items[product]
        else:
            self._items[product] -= amount

    def is_product(self, product: str) -> bool:
        return product in self._items

    def is_amount(self, product: str, amount: int) -> bool:
        return 0 < amount <= self._items[product]
