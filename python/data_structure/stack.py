class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get(self):
        return {
            'value': self.value,
            'next': self.next
        }


class MyStack:
    # constructor
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        node = Node(value).get()

        if self.length == 0:
            self.top = self.bottom = node
        else:
            node['next'] = self.top
            self.top = node

        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.bottom = None

        self.top = self.top['next']
        self.length -= 1

    def isEmpty(self):
        if self.length == 0:
            return True

        return False

    def printStack(self):
        print('top: ' + str(self.top))
        print('bottom: ' + str(self.bottom))
        print('length: ' + str(self.length))


class MyStack2:
    # constructor
    def __init__(self):
        self.array = []

    def peek(self):
        return None if len(self.array) == 0 else self.array[0]

    def push(self, value):
        array = [value]

        for i in self.array:
            array.append(i)

        self.array = array

    def pop(self):
        self.array.pop()

    def isEmpty(self):
        return True if len(self.array) == 0 else False

    def printStack(self):
        print(self.array)


myStack = MyStack()
myStack.printStack()
myStack.push(1)
myStack.printStack()
myStack.pop()
myStack.printStack()
myStack.push(3)
myStack.printStack()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.printStack()
