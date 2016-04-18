import doctest

class MinStack(object):
    """
    >>> ms = MinStack()
    >>> ms.push(1)
    >>> ms.push(4)
    >>> ms.push(6)
    >>> ms.pop()
    6
    >>> ms.min()
    1
    """
    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.mintest = []

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if len(self.mintest) != 0:
            currentmin = self.mintest[-1]
            if number <= currentmin:
                self.mintest.append(number)
        else:
            self.mintest.append(number)

    def pop(self):
        # pop and return the top item in stack
        x = self.stack.pop()
        current = self.mintest[-1]
        if x == current:
            self.mintest.pop()
        return x

    def min(self):
        # return the minimum number in stack
        return self.mintest[-1]

doctest.testmod(verbose=1)