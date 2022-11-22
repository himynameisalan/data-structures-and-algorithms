class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get(self):
        return {
            'value': self.value,
            'next': self.next
        }


class MyQueue:
    # constructor
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, value):
        node = Node(value).get()

        if self.length == 0:
            self.first = self.last = node
        else:
            self.last['next'] = node
            self.last = node

        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.last = None

        self.first = self.first['next']
        self.length -= 1

    def isEmpty(self):
        if self.length == 0:
            return True

        return False

    def printQueue(self):
        print('first: ' + str(self.first))
        print('last: ' + str(self.last))
        print('length: ' + str(self.length))


class MyQueue2:
    # constructor
    def __init__(self):
        self.array = []

    def peek(self):
        return None if len(self.array) == 0 else self.array[0]

    def enqueue(self, value):
        self.array.append(value)

    def dequeue(self):
        if len(self.array) > 0:
            self.array.remove(self.array[0])

    def isEmpty(self):
        return True if len(self.array) == 0 else False

    def printQueue(self):
        print(self.array)


myQueue = MyQueue2()
myQueue.printQueue()
myQueue.enqueue(1)
myQueue.printQueue()
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.printQueue()
myQueue.dequeue()
myQueue.printQueue()
myQueue.dequeue()
myQueue.printQueue()
myQueue.dequeue()
myQueue.printQueue()
