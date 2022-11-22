class MyHashTable:
    # constructor
    def __init__(self, size):
        self.data = [None] * size

    def __hash_address(self, key):
        return hash(key) % len(self.data)

    def set(self, key, value):
        address = self.__hash_address(key)

        if not self.exist(key):
            self.data[address] = []

        self.data[address].append([key, value])

    def get(self, key):
        address = self.__hash_address(key)
        pairs = self.data[address]

        if pairs is None:
            return None

        for pair in pairs:
            if pair[0] is key:
                return pair[1]

    def exist(self, key):
        address = self.__hash_address(key)
        pairs = self.data[address]

        if pairs is None:
            return False

        for pair in pairs:
            if pair[0] is key:
                return True

        return False

    def keys(self):
        key_arr = []

        for item in self.data:
            if item is not None:
                if len(item) > 1:
                    for pair in item:
                        key_arr.append(pair[0])

                key_arr.append(item[0][0])

        return key_arr


myHashTable = MyHashTable(50)
myHashTable.set('gg', 321)
myHashTable.set('hh', 456)

print(myHashTable.data)
print(myHashTable.get('gg'))
print(myHashTable.keys())


def firstRecurringCharacters(text):
    arr = []
    print(text)

    for i in text:
        for j in arr:
            if i is j:
                return i
        arr.append(i)
        print(arr)

    return 'undefined'


def firstRecurringCharacters2(text):
    result = 'undefined'
    mp = MyHashTable(len(text))

    for i in text:
        if mp.exist(i):
            result = i
            break

        mp.set(i, i)

    print(mp.keys())
    return result


def firstRecurringCharacters3(text):
    result = 'undefined'
    dct = {}

    for i in text:
        if dct.get(i):
            result = i
            break

        dct[i] = 1

    print(dct.keys())
    return result


print(firstRecurringCharacters([0, 1, 1, 0, 2, 4, 3]))
