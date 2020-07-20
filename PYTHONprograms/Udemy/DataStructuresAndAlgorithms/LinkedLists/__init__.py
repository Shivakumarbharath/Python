class Node:
    def __init__(self, value):
        self.value = value  # to store the value
        self.nextnode = None  # to store the reference of the next node


class DoublyLinkedNode:
    def __init__(self, value):
        self.value = value  # to store the value
        self.next_node = None  # to store the reference of the next node
        self.prev_node=None# to store the reference of the previous node
