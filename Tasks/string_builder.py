class StringBuilder:

    def __init__(self, data):
        self.string = list(data)

    def append(self, elem: str):
        self.string.extend(list(elem))

    def __str__(self):
        return ''.join(self.string)

    def insert(self, elem: str, ind: int = 0):
        if ind > len(self.string):
            raise IndexError('Index out of range')
        self.string.insert(ind, elem)

    def __getitem__(self, key: int or slice):
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self.string))
            return ''.join(str(i) for i in self.string[start:stop:step])
        if isinstance(key, int):
            if key > len(self.string):
                raise IndexError('Index out of range')
            if key < 0:
                key += len(self.string)
            return ''.join(str(i) for i in self.string)[key]
        else:
            raise TypeError('Invalid type')

    def __setitem__(self, key: int, value: str):
        self.string.insert(key, value)

    def __len__(self):
        return len(''.join(self.string))

    def clear(self):
        self.string = []

    def __iadd__(self, other: str):
        for i in other:
            self.string.append(i)
        return self


if __name__ == '__main__':
    s = StringBuilder('')
    s.append('ABCDE')
    print(s[0])
    print(s[:2])
