'''
A Singly Linked lists is a collection of nodes
that ollectivly form a linear sequence

Each node consists of a reference to an objectsthat is an
element of sequence,as well as reference to  next node of lists

The list instance maintains a member known as head that identifies the
first node of the list





'''


class Node:
    def __init__(self, value):
        self.value = value  # to store the value
        self.nextnode = None  # to store the reference of the next node


if __name__ == '__main__':
    # Providing value
    a = Node(1)
    b = Node(2)
    c = Node(3)

    # Linking the nodes
    a.nextnode = b
    b.nextnode = c

    print(a.value)
    print(a.nextnode.value)
    print(a.nextnode.nextnode.value)
