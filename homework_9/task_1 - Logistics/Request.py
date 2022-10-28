class Request:
    def __init__(self, from_: str, to: str, amount: int, product: str):
        self._from_ = from_
        self._to = to
        self._amount = amount
        self._product = product

    def __repr__(self) -> str:
        return f'Курьер везет {self._amount} {self._product} со {self._from_} в {self._to}'
