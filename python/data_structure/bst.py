import json
import pprint


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"(value: {self.value}, left: ({self.left}), right: ({self.right}))"

    def get(self):
        return {
            'value': self.value,
            'left': self.left,
            'right': self.right
        }


class MyBST:
    # constructor
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return

        if self.root.value == value:
            return

        current_node = self.root

        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = node
                    break
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = node
                    break
                current_node = current_node.right

    def lookup(self, value):
        current_node = self.root

        while current_node is not None:
            if value == current_node.value:
                break

            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return current_node

    def remove(self, value):
        # initial nodes
        parent_node = None
        target_node = self.root

        # current node is None
        if target_node is None:
            return

        # find the target node
        while target_node is not None:
            if value == target_node.value:
                break

            parent_node = target_node

            if value < target_node.value:
                target_node = target_node.left
            else:
                target_node = target_node.right

        # find the node for replacement

    def printBST(self):
        print(self.root)
        # print(json.dumps(self.root.__dict__))


myBST = MyBST()
myBST.insert(9)
myBST.insert(4)
myBST.insert(6)
myBST.insert(20)
myBST.insert(170)
myBST.insert(15)
myBST.insert(1)
myBST.insert(10)
myBST.insert(16)
myBST.insert(100)

myBST.printBST()
print(myBST.lookup(20))

# myBST.remove(20)
# myBST.printBST()
