import ctypes

class Mer0list:
    def __init__(self):
        self.size = 1
        self.dataCount = 0
        self._block = self.__makelist(self.size)

    def __makelist(self, capacity):
        return (ctypes.py_object * capacity)()

    def __len__(self):
        return self.dataCount

    def __str__(self):
        result = ""
        for i in range(self.dataCount):
            result += str(self._block[i]) + ','
        return result[:-1]

    def __getitem__(self, index):
        if index >= self.dataCount or (-index - 1) >= self.dataCount:
            raise IndexError
        return self._block[index]

    def __setitem__(self, index, item):
        if index >= self.dataCount or (-index - 1) >= self.dataCount:
            raise IndexError
        self._block[index] = item

    def _resize(self, newcapacity):
        if self.dataCount == self.size - 1:
            newarray = self.__makelist(newcapacity)
            for i in range(self.dataCount):
                newarray[i] = self._block[i]
            self._block = newarray
            self.size = newcapacity

    def append(self, item):
        if self.size - 1 == self.dataCount:
            self._resize(2 * self.size)
        self._block[self.dataCount] = item
        self.dataCount += 1

    def insertitem(self, item, index):
        if self.size - 1 == self.dataCount:
            self._resize(2 * self.size)
        if index > self.dataCount or (-index - 1) > self.dataCount:
            raise IndexError
        for i in range(self.dataCount, index, -1):
            self._block[i] = self._block[i - 1]
        self._block[index] = item
        self.dataCount += 1
        self.size += 1

    def delitem(self, index):
        if index >= self.dataCount or (-index - 1) >= self.dataCount:
            raise IndexError
        a = self._block[index]
        for i in range(index, self.dataCount - 1):
            self._block[i] = self._block[i + 1]
        self.dataCount -= 1
        self.size -= 1
        return a