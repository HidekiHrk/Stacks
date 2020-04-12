from stack.errors import (
        EmptyStackError,
        ItemNotFoundError
    )

class Stack:
    def __init__(self):
        self.__items = []

    def __next__(self):
        return self.pull()

    def __iter__(self):
        yield from map(lambda x: self.pull(), range(len(self.__items)))

    @property
    def items(self):
        return self.__items

    def __str__(self):
        return '\n'.join(
            map(lambda x: f"[\t{x}\t]",
                self.__items[::-1])
            )

    def pull(self):
        if not self.__items:
            raise EmptyStackError()
        return self.__items.pop(-1)

    def push(self, item):
        self.__items.append(item)
        return len(self.__items)

    def remove(self, item=None):
        if item == None:
            removed = self.__items
            del self.__items[:]
            return removed
        try:
            idx = self.__items[::-1].index(item) + 1
        except ValueError:
            return ItemNotFoundError()
        removed = self.__items[-idx:]
        del self.__items[-idx:]
        return removed