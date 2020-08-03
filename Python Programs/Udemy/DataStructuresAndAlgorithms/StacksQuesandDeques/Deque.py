'''
Deque is also known as Double- Ended queue
is an orderd collection of items similar to queue

The difference in queue and deque
is New items can be added either in front or
rear

Stacks and queues  in a single data structure







'''


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def AddFront(self, item):
        self.items.append(item)

    def AddRear(self, item):
        self.items.insert(0, item)

    def RemoveaRear(self):
        return self.items.pop(0)

    def RemiceFront(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
