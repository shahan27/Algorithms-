# basic funtions for a tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def printTree(self):
        print(self.data)


root = Node(20)
root.printTree()
