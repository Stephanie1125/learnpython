import doctest

class Heap(object):
    """
    >>> h = Heap()
    >>> h.push(3)
    >>> h.push(7)
    >>> h.push(6)
    >>> h.print()
    [0, 7, 3, 6]
    """
    def __init__(self):
        self.heap = [0]

    def exch(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]


    def swim(self, k):
        while k > 1 and self.heap[k//2] < self.heap[k]:
            self.exch(k, k//2)
            k = k//2

    def push(self, value):
        self.heap.append(value)
        self.swim(len(self.heap)-1)

    def print(self):
        print(self.heap)

doctest.testmod(verbose=1)

