import doctest

def power1(x, n): # O(logn) faster
    """
    >>> power1(2,3)
    8
    """
    s = x ** n
    return s

def power2(x, n): # O(n) faster in small n
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

doctest.testmod(verbose=1)

