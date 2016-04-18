__author__ = 'stephanie'
import doctest
import math

# prime number test
def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    >>> is_prime(-5)
    True
    """

    n = abs(int(n))
    if n <= 1: return False
    elif n == 2: return True
    elif n % 2 == 0: return False # filter(remain odd numbers)
    else:
        for i in range(3,int(n**0.5)+1): # test n range start from 3 until int(sqr(n)+1)
            if n % i == 0:    # bound to find at least one factor of n
                return False  # because if n=a*b and a<=b then a*a <= a*b == n == sqr(n)**2
        return True

# happy number test
def happy_convert(n):
    n_string = str(n)
    res1 = 0
    for chr in n_string:
        res1 += int(chr) ** 2
    return res1

def is_happy(n):
    num_set = set()
    while True:
        num_set.add(n)
        n = happy_convert(n)
        if n == 1:
            return True
        if n in num_set:
            return False


# triangular test
def is_triangular(n):
    if n < 0: return False
    x = 1
    while True:
        n -= x
        x += 1
        if n == 0: return True
        if n < 0: return False


print(is_triangular(5))

def square(n):
    if n < 0: return False
    x = 1
    while True:
        n -= x
        x += 2
        if n == 0: return True
        if n < 0: return False

def is_squared(n):
    """
    >>> is_squared(25)
    True
    >>> is_squared(24)
    False
    """
    if n < 0: return False
    x = int(n**0.5)
    if x*x == n: return True
    else:
        return False

def is_smug(n):
    """
    >>> is_smug(8)
    True
    >>> is_smug(10)
    True
    >>> is_smug(4)
    True

    """

    if n < 0: return False
    for a in range(int(math.sqrt(n)) + 1):
        first = a ** 2
        second = n - first
        if is_squared(second):
            return True
    return False

def is_honest(n):
    '''
    >>> is_honest(5)
    False
    >>> is_honest(4)
    True
    >>> is_honest(1)
    True
    '''

    if n < 0: return False
    if is_squared(n): return True
    for k in range(1, int(math.sqrt(n))):
        k = n//k
        if k*k != n: return False
        else: return True

doctest.testmod(verbose=True)
