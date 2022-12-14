import pprint


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def get(self):
        return {
            'value': self.value,
            'next': self.next,
            'previous': self.previous
        }


class MyDoubleLinedList:
    # constructor
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None,
            'previous': None
        }

        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value).get()

        new_node['previous'] = self.tail
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value).get()
        new_node['next'] = self.head
        self.head['previous'] = new_node
        self.head = new_node
        self.length += 1

    def get_node(self, index):
        if self.length <= 1:
            return None

        if index >= self.length:
            return None

        node = self.head

        counter = 0

        while counter < index:
            node = node['next']
            counter += 1

        return node

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        elif 0 < index < self.length:
            # create new node
            new_node = Node(value).get()
            # find previous node
            previous_node = self.get_node(index - 1)
            # find next node
            next_node = self.get_node(index)
            # set the next & previous of new node
            new_node['next'] = next_node
            new_node['previous'] = previous_node
            # point the next of previous node to new node, point the previous node of next node to new node
            previous_node['next'] = new_node
            next_node['previous'] = new_node

        else:
            return

        self.length += 1

    def print_list(self):
        current_node = self.head
        node_list = []

        while current_node is not None:
            node_list.append(current_node)
            current_node = current_node['next']

        print(node_list)

    def remove(self, index):
        if index == 0:
            next_node = self.head['next']
            next_node['previous'] = None
            self.head = next_node
        elif index == self.length - 1:
            # get the previous node of the tail node
            previous_node = self.get_node(self.length - 2)
            previous_node['next'] = None
        elif 0 < index < self.length - 1:
            # get the previous node of the index node
            previous_node = self.get_node(index - 1)
            # get the index node
            next_node = self.get_node(index + 1)
            # point the previous node to the next node of the index node
            previous_node['next'] = next_node
            next_node['previous'] = previous_node

        else:
            return

        self.length -= 1


myLinkedList = MyDoubleLinedList(10)
myLinkedList.append(5)
myLinkedList.prepend(4)
myLinkedList.insert(2, 16)
myLinkedList.print_list()

myLinkedList.remove(2)
myLinkedList.print_list()

# pprint.pprint(myLinkedList.head)
