import queue

L = queue.Queue(maxsize=6)
L.put(5)
L.put(8)
L.put(9)
L.put(2)
L.put(7)
L.put(1)
print(L.full())  # returns true if all the elemaents are full
print(L.get())  # returns 1st element
print(L.get())  # returns 2nd element
print(L.get())  # returns 3rd element
print(L.full())
print(L.empty())  # checks if empty
