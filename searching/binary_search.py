__author__ = 'stephanie'
import doctest

def binary_search(seq, key):
    """
    >>> seq1 = [0, 1, 2, 3, 4, 5]
    >>> binary_search(seq1, 5)
    5
    >>> seq2 = [0, 2, 3, 4, 7]
    >>> binary_search(seq2, 0)
    0
    >>> seq3 = [1, 2, 3, 4, 5]
    >>> binary_search(seq3, 5)
    4
    >>> seq4 = [1,2,3]
    >>> binary_search(seq4, 5)
    -1
    """
# begin/end /not exist

    begin = 0
    end = len(seq)-1
    while begin <= end:
        mid = (begin + end)//2
        tmp = seq[mid]
        if key == tmp:
            return mid
        elif key > tmp:
            begin = mid + 1
        else:
            end = mid - 1
    return -1


def binary_search(seq, key):
    """
    >>> seq1 = [0, 1, 2, 3, 4, 5]
    >>> binary_search(seq1, 5)
    5
    >>> seq2 = [0, 2, 3, 4, 7]
    >>> binary_search(seq2, 0)
    0
    >>> seq3 = [1, 2, 3, 4, 5]
    >>> binary_search(seq3, 5)
    4
    >>> seq4 = [1,2,3]
    >>> binary_search(seq4, 5)
    -1
    """
# begin/end /not exist

    begin = 0
    end = len(seq)-1
    while end - begin > 1:
        mid = (begin + end)//2
        if seq[mid] > key:
            end = mid
        else:
            begin = mid

    if seq[begin] == key:
        return begin
    if seq[end] == key:
        return end
    return -1

doctest.testmod(verbose=1)