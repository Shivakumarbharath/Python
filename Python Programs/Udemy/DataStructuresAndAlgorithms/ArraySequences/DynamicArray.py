import ctypes
import sys


class DynamicArray:
    '''
    To create an own dynamic array...

    '''

    def __init__(self, capacity=1):  # optional argument
        self.n = 0  # for indexing
        self.capacity = capacity  # to maintain the capacity
        self.A = self.make_array(self.capacity)  # actual array

    def __str__(self):
        # return the values entered
        k = []
        for i in range(self.n):
            k.append(self.A[i])
        return str(k)

    def __len__(self):
        return self.n  # return actual lenth used in the array

    def __getitem__(self, item):

        if not 0 <= item < self.n:
            return IndexError('Number is not bound to array')

        return self.A[item]  # to get the item by indexing

    def append(self, ele):

        if self.n == self.capacity:
            self._resize(2 * self.capacity)  # double the size if needed

        self.A[self.n] = ele  # assign the value
        self.n += 1  # increace the index number

    def _resize(self, cap):

        B = self.make_array(cap)  # create another array of double the size

        for i in range(self.n):
            B[i] = self.A[i]  # copy the content of size

        self.A = B  # rename the array for future use
        self.capacity = cap  # store the capacity

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()  # memory allocation

    def size(self):
        return sys.getsizeof(self.A)


k = DynamicArray()

k.append(5)
k.append(6)
k.append(7)
k.append(8)
print(k)
print(k.size())
