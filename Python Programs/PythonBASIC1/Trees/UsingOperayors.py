class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.data)


def preorder(tree):
    if tree is None:
        return
    print(tree.data)
    preorder(tree.left)
    preorder(tree.right)


def inorder(tree):
    if tree is None:
        return
    inorder(tree.left)
    print(tree.data)
    inorder(tree.right)


def postoder(tree):
    if tree is None:
        return
    postoder(tree.left)
    postoder(tree.right)
    print(tree.data)


# fisrt create nodes and objects then make the conections
# first connect left leaves and then Right
root = Node('+')
n2 = Node('-')
n3 = Node(2)
n4 = Node('+')
n5 = Node(7)
n6 = Node(5)
n7 = Node(9)
root.right = n3
root.left = n2
root.left.left = n4
root.left.left.left = n6
root.left.right = n5
root.left.left.right = n7
inorder(root)
