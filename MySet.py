class MySet:
    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.add(value)

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True

    def delete(self, value):
        if self.has(value):
            del self.dictionary[value]

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()

    def __str__(self):
        return f"MySet: {{{', '.join(map(str, self.dictionary.keys()))}}}"