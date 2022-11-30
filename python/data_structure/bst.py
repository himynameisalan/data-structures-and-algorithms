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

    def bfs(self):
        current_node = self.root
        arr = list()
        q_arr = list()
        q_arr.append(current_node)

        while len(q_arr) > 0:
            current_node = q_arr.pop(0)
            arr.append(current_node.value)

            if current_node.left is not None:
                q_arr.append(current_node.left)

            if current_node.right is not None:
                q_arr.append(current_node.right)

        return arr

    def bfs_r(self, q_arr, arr):
        if len(q_arr) == 0:
            return arr

        current_node = q_arr.pop(0)
        arr.append(current_node.value)

        if current_node.left is not None:
            q_arr.append(current_node.left)

        if current_node.right is not None:
            q_arr.append(current_node.right)

        return self.bfs_r(q_arr, arr)

    def dfs_inorder(self, node, arr):
        if node.left is not None:
            self.dfs_inorder(node.left, arr)

        arr.append(node.value)

        if node.right is not None:
            self.dfs_inorder(node.right, arr)

        return arr

    def dfs_preorder(self, node, arr):
        arr.append(node.value)

        if node.left is not None:
            self.dfs_preorder(node.left, arr)

        if node.right is not None:
            self.dfs_preorder(node.right, arr)

        return arr

    def dfs_postorder(self, node, arr):
        if node.left is not None:
            self.dfs_postorder(node.left, arr)

        if node.right is not None:
            self.dfs_postorder(node.right, arr)

        arr.append(node.value)

        return arr

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
print(myBST.bfs())
print(myBST.bfs_r([myBST.root], []))
# myBST.remove(20)
# myBST.printBST()
print(myBST.dfs_inorder(myBST.root, []))
print(myBST.dfs_preorder(myBST.root, []))
print(myBST.dfs_postorder(myBST.root, []))
