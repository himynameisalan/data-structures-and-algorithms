class MyArray:
    # constructor
    def __init__(self):
        self.length = 0
        self.data = dict()

    def get(self, index: int):
        if index < 0 or index >= self.length:
            return "Wrong index"
        elif self.length == 0:
            return "Empty array"

        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        if self.length < 1:
            return
        del self.data[self.length - 1]
        self.length -= 1

    def delete(self, index: int):
        if index >= self.length:
            print('Wrong index')
        elif self.length == 0:
            print('Empty array')
        else:
            self.shiftItems(index)
            self.length -= 1

    def shiftItems(self, index: int):
        for i in range(index, self.length):
            self.data[index] = self.data[index + 1]
        del self.data[self.length - 1]


def reverseString(string: str):
    temp = ''
    length = len(string)
    for i in range(length):
        temp += string[length - 1 - i]
    return temp


def reverseString2(string: str):
    return string[::-1]


def mergeSortedArrays(arr1: [], arr2: []):
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        print('Both inputs must be sorted array')
        return

    arr1Length = len(arr1)
    arr2Length = len(arr2)
    i = j = 0
    mergedArray = []

    while i < arr1Length and j < arr2Length:
        if arr1[i] < arr2[j]:
            mergedArray.append(arr1[i])
            i += 1
        else:
            mergedArray.append(arr2[j])
            j += 1

    while i < arr1Length:
        mergedArray.append(arr1[i])
        i += 1

    while j < arr2Length:
        mergedArray.append(arr2[j])
        j += 1

    return mergedArray


def mergeSortedArrays2(arr1: [], arr2: []):
    mergedArray = arr1 + arr2
    mergedArray.sort()
    return mergedArray


myArray = MyArray()
myArray.push('123')
myArray.push('456')
myArray.push('789')
myArray.delete(1)
print(myArray.data)

print(reverseString('how are you!'))

print(mergeSortedArrays([3, 4, 5], [6, 6, 7, 8, 9]))
