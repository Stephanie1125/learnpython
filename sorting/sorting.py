__author__ = 'stephanie'
import doctest

def exch(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def less(a, b):
    return  a < b

def compexch(a, b): # if b < a, exchange
    if less(b, a):
        a, b = b, a

def selectionSort(lst):
    # O(n^2)
    # Compared: (N^2)/2
    # Exchange N times
    """
    >>> lst = [1, 3, 5, 2, 7]
    >>> selectionSort(lst)
    >>> lst
    [1, 2, 3, 5, 7]
    """
    for i in range(len(lst)):
        min = i
        for j in range(i+1, len(lst)):
            if less(lst[j], lst[min]):
                min = j
        exch(lst, min, i)

def insertionSort(lst):
    # O(n^2)
    # Compared: (N^2)/4 or (N^2)/2
    # Exchange (N^2)/4 or (N^2)/2 times
    """
    >>> lst = [1, 3, 5, 2, 7]
    >>> insertionSort(lst)
    >>> lst
    [1, 2, 3, 5, 7]
    """
    # for i in range(1, len(lst)):
    #     insert_item = lst[i]
    #     j = i - 1
    #     while (j >= 0) and (lst[j] > insert_item):
    #         lst[j + 1] = lst[j]
    #         j -= 1
    #     lst[j + 1] = insert_item

    for i in range(1, len(lst)):
        j = i
        while (j >= 0) and less(lst[j], lst[j-1]):
            exch(lst, j, j-1)
            j -= 1


doctest.testmod(verbose=1)