class StaticArray:
    def __init__(self, capacity):
        self._array = []
        self._capacity = capacity

    @property
    def array(self):
        return self._array

    @property
    def capacity(self):
        return self._capacity

    def add(self, element):
        if len(self.array) < self.capacity:
            self._array += [element]
        else:
            print("Добавление новых элементов невозможно!")

    def read(self):
        return self.array

    def insert(self, index, element):
        self._array = self.array[:index] + [element] + self.array[index:]
        del self.array[-1]

    def delete(self, index):
        del self.array[index]
