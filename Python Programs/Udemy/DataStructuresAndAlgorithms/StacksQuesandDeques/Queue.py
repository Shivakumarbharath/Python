'''

A Queue is a collection of items where the addition
ofitems takes place at the end called the rear and removal takes place at the
front

Same as the normally in the queue
Its FIFO
first in first out principle

Enqueue describes when we add an an item in a queue

Dequeue describes when an item is removed from the other end


'''


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
