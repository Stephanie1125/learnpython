import doctest

def binary(dec):
    """
    >>> dec = 16
    >>> binary(dec)
    10000
    """
    if dec > 1:
        binary(dec//2)
    print(dec % 2, end = '')

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

doctest.testmod(verbose=1)


