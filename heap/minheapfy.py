import doctest

def heapify(seq):
    """
    >>> heapify([4, 2, 1, 7, 8])
    [1, 2, 4, 7, 8]
    """
    minheap = [0] + seq
    for i in range(len(seq)//2, 0, -1): #len(seq)//2 -= 1 to index 1
        minHeapify(minheap, i, seq)
    seq[:] = minheap[1:]
    return seq

def minHeapify(heap, k, seq):
    if k > len(seq)//2:
        return
    if k * 2 + 1 > len(seq) or heap[k * 2] < heap[k * 2 + 1]:
        minChild = k * 2
        if heap[k] > heap[minChild]:
            exch(heap, k,minChild)
        minHeapify(heap, k * 2, seq)
    else:
        minChild = k * 2 + 1
        if heap[k] > heap[minChild]:
            exch(heap, k, minChild)
        minHeapify(heap, k * 2 + 1, seq)

def exch(seq, a, b):
    seq[a], seq[b] = seq[b], seq[a]


doctest.testmod(verbose=1)