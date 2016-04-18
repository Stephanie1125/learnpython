__author__ = 'stephanie'
import doctest

def Sum(L):
    """
    >>> L = [123, 2, 6]
    >>> Sum(L)
    131
    """
    total = 0
    for i in range(len(L)):
        total = total + L[i]
    return total

doctest.testmod(verbose = 1)