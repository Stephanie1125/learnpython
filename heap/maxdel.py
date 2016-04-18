import doctest

class Heap(object):
    """
    >>> h = Heap()
    >>> h.push(3)
    >>> h.push(7)
    >>> h.push(6)
    >>> h.print()
    [0, 7, 3, 6]
    >>> h.maxdel()
    >>> h.print()
    [0, 6, 3]
    """
    def __init__(self):
        self.heap = [0]

    def exch(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    def sink(self, k):
        while 2*k <= len(self.heap)-1:
            x = 2*k
            if x < len(self.heap)-1 and self.heap[x] < self.heap[x+1]:
                x += 1
            if self.heap[k] > self.heap[x]:
                break
            self.exch(k, x)
            k = x

    def swim(self, k):
        while k > 1 and self.heap[k // 2] < self.heap[k]:
            self.exch(k, k // 2)
            k = k // 2

    def push(self, value):
        self.heap.append(value)
        self.swim(len(self.heap) - 1)

    def print(self):
        print(self.heap)

    def maxdel(self):
        self.exch(1, len(self.heap)-1)
        self.heap.pop()
        self.sink(1)

doctest.testmod(verbose=1)

