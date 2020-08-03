'''

A stack is an ordered collection of items where
the addition and removal of items take place at the same end
This end is known as top of the stack
The opposite end is called the base

The stack ordering is LIFO
Last in first out

STACK METHODS AND ATTRIBUTES
1.Stack()-Creates a empty stack with no parameters
2.push()-adds an item to the top of the stack it needs
the item and returns nothing
3.pop()-removes the item from the top of the stack
it takes nothing and returns the item
4.peek() returns the item at the top but does not remove from the stack
5.isEmpty()-checks weather the stack is empty returns a boolean value
6.size()-returns the number of items in the stack
'''


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
