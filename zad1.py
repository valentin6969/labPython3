#zadanie 1
import math as m

class DList:
    class Element:
        def __init__(self, value, next = None, prev = None):
            self.__value = value
            self.next = None
            self.prev = None

        @property
        def value(self):
            return self.__value

    def __init__(self, args):
        self.__root = None
        self.__end = None
        for i in args:
            self.insert(i)

    def insert(self, value):
        element = DList.Element(value)
        if self.__root is None:
            self.__root = element
            self.__end = element
            return
        else:
            prev = self.__root
            while not (prev.next is None):
                if prev.next.value > value:
                    next = prev.next
                    prev.next = element
                    next.prev = element
                    element.prev = prev
                    element.next = next
                    return
                else:
                    prev = prev.next
            if prev.next is None:
                self.__end = element
                element.prev = prev
                prev.next = element

    def __iter__(self):
        curr = self.__root
        while not (curr is None):
            yield curr.value
            curr = curr.next

    def __reversed__(self):
        curr = self.__end
        while not (curr is None):
            yield curr.value
            curr = curr.prev
        pass

    def __contains__(self, value):
        curr = self.__root
        assert not m.isnan(value), 'Obecny kod nie jest wstanie wyszukac NaN w liscie'
        while not (curr is None):
            assert type(value) == type(curr.value), 'Poszukiwana wartość posiada inny typ danych'
            if curr.value == value:
                return True
            elif curr.value > value:
                return False
            else:
                curr = curr.next
        return False

dlista = DList([2.0, 3.0, 4.0, 5.0, float('nan') ])
for i in dlista:
    print(i)

5 in dlista
print(float('nan') in dlista)

