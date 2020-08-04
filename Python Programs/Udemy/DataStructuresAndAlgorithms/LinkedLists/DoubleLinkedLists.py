'''
IN double linkes lists each node keeps the
refernce of node after in and before it unlike
single linked list keeps only reference after it.




'''


class DoublyLinkedNode:
    def __init__(self, value):
        self.value = value  # to store the value
        self.next_node = None  # to store the reference of the next node
        self.prev_node = None  # to store the reference of the previous node


if __name__ == '__main__':
    # Providing value
    a = DoublyLinkedNode(1)
    b = DoublyLinkedNode(2)
    c = DoublyLinkedNode(3)

    a.next_node = b
    b.prev_node = a

    b.next_node = c
    c.prev_node = b

    print(a.next_node.value, b.prev_node.value)
