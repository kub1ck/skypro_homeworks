from Store import Store


class Shop(Store):
    def __init__(self, capacity: int = 20) -> None:
        super().__init__()
        self.capacity = capacity

    def add(self, product: str, amount: int) -> None:
        if self.get_unique_items_count() < 5:
            super().add(product, amount)
        else:
            print("В магазине не может быть больше 5 разных продуктов!")
