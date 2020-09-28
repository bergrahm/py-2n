class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()
    
    def __repr__(self):
        return "SortedList({!r})".format(self._items)


class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values.')

    def add(self, item):
        self._validate(item)
        super().add(item)
    
    def __repr__(self):
        return "IntList({!r})".format(list(self))

class SortIntegList(IntList, SortedList):
    def __repr__(self):
        return "SortIntList({!r})".format(list(self))

def main():
    simpList = SimpleList([10,20,30,20,10])
    print(simpList.__repr__)
    sortList = SortedList(simpList)
    print(sortList.__repr__)
    print(simpList.__repr__)
    simpList.add(20000)
    sortList.add(10000)
    print(sortList.__repr__)
    print(simpList.__repr__)
    integList = IntList(simpList)
    print(integList.__repr__)
    siList = SortIntegList(simpList)
    print( siList.__repr__)

if __name__ == "__main__":
    main()