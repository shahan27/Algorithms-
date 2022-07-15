# basic funtions for a tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def insert(self, data):
        # check if parent node exist
        if self.data:
            if self.data < data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif self.data > data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # inOrder tranversal goes from left subtree -> root -> right subtree
    def inOrder(self, root):
        tree = []
        if root:
            tree = self.inOrder(root.left)
            tree.append(root.data)
            tree = tree + self.inOrder(root.right)
        return tree


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(7)
root.insert(13)
root.insert(18)
print(root.inOrder(root))
