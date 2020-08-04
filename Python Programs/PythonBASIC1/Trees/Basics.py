class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.data)


# fisrt create nodes and objects then make the conections
# first connect left leaves and then Right
root = Node(23)
n2 = Node(15)
n3 = Node(25)
n4 = Node(8)
n5 = Node(17)
n6 = Node(5)
n7 = Node(9)
root.right = n3
root.left = n2
root.left.left = n4
root.left.left.left = n6
root.left.right = n5
root.left.left.right = n7
print(root.left.left.right.right)
