class EmptyStackError(Exception):
    def __init__(self):
        super().__init__("The stack is empty :(")


class ItemNotFoundError(Exception):
    def __init__(self):
        super().__init__("item not found in the stack")