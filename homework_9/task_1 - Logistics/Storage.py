# Абстрактный класс
class Storage:
    def __init__(self, capacity: int = 0) -> None:
        self._items = {}
        self._capacity = capacity

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        self._capacity = capacity

    def add(self, product: str, amount: int) -> None:
        self._items.setdefault(product, 0)
        self._items[product] += amount
        self._capacity -= amount

    def get_items(self) -> dict:
        return self._items

    def get_unique_items_count(self) -> int:
        return len(self._items)
