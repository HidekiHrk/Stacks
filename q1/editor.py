from stack import Stack

class Editor(Stack):
    def __init__(self, string:str = ""):
        super().__init__()
        if string:
            self.read(string)

    def read(self, string:str):
        for char in string:
            self.push(char)

    @property
    def text(self):
        return ''.join(self._Stack__items).strip()

    @property
    def numeratedLines(self):
        nstr = []
        txt = self.text.split('\n')
        tsize = len(str(len(txt)))
        for num in range(len(txt)):
            ts = ' ' * (tsize - len(str(num+1)))
            nstr.append(f"{num+1}{ts}| {txt[num]}")
        return '\n'.join(nstr)

    def removeLines(self, number):
        for x in range(number):
            self.remove('\n')

    def save(self, filename:str):
        with open(filename, 'w', encoding='utf-8') as fp:
            fp.write(self.text)
        return True