import doctest

def heapify(seq):
    """
    >>> heapify([4, 2, 1, 7, 8])
    [8, 7, 1, 4, 2]
    """
    maxheap = [0] + seq
    for i in range(len(seq) // 2, 0, -1):  # len(seq)//2 -= 1 to index 1
        maxHeapify(maxheap, i, seq)
    seq[:] = maxheap[1:]
    return seq

def maxHeapify(heap, k, seq):
    if k > len(seq)//2:
        return
    if k * 2 + 1 > len(seq) or heap[k * 2] < heap[k * 2 + 1]:
        maxChild = k * 2 + 1
        if heap[k] < heap[maxChild]:
            heap[k], heap[maxChild] = heap[maxChild], heap[k]
        maxHeapify(heap, k * 2 + 1, seq)
    else:
        maxChild = k * 2
        if heap[k] < heap[maxChild]:
            heap[k], heap[maxChild] = heap[maxChild], heap[k]
        maxHeapify(heap, k * 2, seq)


doctest.testmod(verbose=1)