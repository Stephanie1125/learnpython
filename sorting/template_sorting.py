__author__ = 'stephanie'
import doctest

def less(a, b):
    """
    >>> a = 5
    >>> b = 4
    >>> less(a, b)
    False
    >>> less(b, a)
    True
    """
    return  a < b

def exch(lst, i, j):
    """
    >>> lst1 = [1, 2, 4, 5]
    >>> exch(lst1, 0, 2)
    >>> lst1
    [4, 2, 1, 5]
    """
    lst[i], lst[j] = lst[j], lst[i]

def isSorted(lst):
    """
    >>> lst1 = [1, 2, 3, 4, 5]
    >>> isSorted(lst1)
    True
    >>> lst2 = [3, 5, 7, 1]
    >>> isSorted(lst2)
    False
    """
    if sorted(lst) == lst:
        return True
    return False

def compexch(a, b):
    """
    >>> a = 3
    >>> b = 5
    >>> compexch(a, b)
    >>> (a, b)
    (3, 5)
    >>> compexch(b, a)
    >>> (b, a)
    (5, 3)
    """
    if less(b, a):
        a, b = b, a

doctest.testmod(verbose=1)