import doctest

class Heap():
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
        for i in seq:
            self.heap.append(i)
            self.swim(len(self.heap)-1)

    def heapsort(self, seq):
        """
        >>> h = Heap()
        >>> h.heapsort([4,6,1,3,2])
        [6, 4, 3, 2, 1]
        """
        self.heapstructure(seq)
        sorted_seq = []
        while len(self.heap) > 1:
            self.exch(1, len(self.heap) - 1)
            max = self.heap.pop()
            sorted_seq.append(max)
            self.sink(1)
        return sorted_seq


doctest.testmod(verbose=1)








