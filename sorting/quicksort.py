import doctest

def exch(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def partition(lst, begin, end):
    pivot = lst[begin]
    left = begin + 1
    right = end
    while True:
        while left <= right and lst[left] <= pivot:
            left += 1
        while lst[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            break
        else:
            exch(lst, left, right)
    exch(lst, begin, right)
    return right

def quicksort(lst, start, end):
    if start < end:
        split = partition(lst, start, end)
        quicksort(lst, start, split - 1)
        quicksort(lst, split + 1, end)
    return lst

def quickSort(lst):
    """
    >>> lst = [1, 3, 5, 2, 7]
    >>> quickSort(lst)
    >>> lst
    [1, 2, 3, 5, 7]
    """
    quicksort(lst, 0, len(lst)-1)

doctest.testmod(verbose=1)