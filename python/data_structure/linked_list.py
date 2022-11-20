import pprint


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get(self):
        return {
            'value': self.value,
            'next': self.next
        }


class MyLinedList:
    # constructor
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }

        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value).get()

        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value).get()
        new_node['next'] = self.head
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
            # point the next of new node to the node at the index
            new_node['next'] = previous_node['next']
            # point the previous node of the index to the new node
            previous_node['next'] = new_node
        else:
            return

        self.length += 1

    def print_list(self):
        current_node = self.head
        node_list = []

        while current_node is not None:
            # node_list.append(current_node)
            node_list.append(current_node['value'])
            current_node = current_node['next']

        print(node_list)

    def remove(self, index):
        if index == 0:
            self.head = self.head['next']
        elif index == self.length - 1:
            # get the previous node of the tail node
            previous_node = self.get_node(self.length - 2)
            previous_node['next'] = None
        elif 0 < index < self.length - 1:
            # get the previous node of the index node
            previous_node = self.get_node(index - 1)
            # get the index node
            index_node = previous_node['next']
            # point the previous node to the next node of the index node
            previous_node['next'] = index_node['next']
        else:
            return

        self.length -= 1

    def reverse(self):
        current_node = self.head
        reverseLinkedList = MyLinedList(current_node['value'])
        current_node = current_node['next']

        while current_node is not None:
            reverseLinkedList.prepend(current_node['value'])
            current_node = current_node['next']

        reverseLinkedList.print_list()

    def reverse2(self):
        prev_node = None
        head_node = self.head
        self.tail = head_node

        while head_node:
            next_node = head_node['next']
            head_node['next'] = prev_node
            prev_node = head_node
            head_node = next_node

        self.head = prev_node
        self.tail['next'] = None
        self.print_list()


myLinkedList = MyLinedList(10)
myLinkedList.append(5)
myLinkedList.prepend(4)
myLinkedList.insert(2, 16)
myLinkedList.print_list()

# myLinkedList.remove(3)
myLinkedList.print_list()
myLinkedList.reverse2()

# pprint.pprint(myLinkedList.head)
