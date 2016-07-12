import doctest

def binary(dec):
    """
    >>> dec = 16
    >>> binary(dec)
    1 0 0 0 0
    """
    if dec > 1:
        binary(dec//2)
    print(dec % 2),


def decimal(bin):
    """
    >>> bin = 10000
    >>> decimal(bin)
    16
    """
    dec = 0
    factor = 1
    while(bin > 0):
       if( (bin % 10) == 1):
          dec += factor
       bin /= 10
       factor = factor * 2
    print(dec)


def b_to_d(b):
    """
    >>> bin = 10000
    >>> b_to_d(bin)
    16
    """
    binary = '0b' + str(b)
    print(int(binary, 2))


def d_to_b(d):
    """
    >>> dec = 16
    >>> d_to_b(dec)
    10000
    """
    print(bin(d)[2:])




doctest.testmod(verbose=1)


