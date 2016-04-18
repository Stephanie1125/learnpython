import doctest

class Heapstructure():
    def __init__(self):
        self.heap = [0]

    def exch(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def sink(self, k):
        while 2*k <= len(self.heap)-1:
            x = 2*k
            if x < len(self.heap)-1 and self.heap[x+1] > self.heap[x]:
                x += 1 # exchange with the larger one
            if self.heap[k] > self.heap[x]:
                break
            self.exch(k,x)
            k = x

    def swim(self, k):
        while k > 1 and self.heap[k] > self.heap[ k//2]:
            self.exch(k, k//2)
            k = k//2

    def heapstructure(self, seq):
        """
        >>> h = Heapstructure()
        >>> h.heapstructure([4,2,1,7,8])
        >>> h.heapprint()
        [0, 8, 7, 1, 2, 4]
        """
        for i in seq:
            self.heap.append(i)
            self.swim(len(self.heap)-1)

    def heapprint(self):
        print(self.heap)

doctest.testmod(verbose=1)







