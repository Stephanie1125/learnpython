__author__ = 'stephanie'
import doctest

class Node(object):
    """
    >>> n = Node()
    """
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Stack(object):
    """
    >>> stk = Stack()
    >>> stk.push(5)
    >>> stk.push(6)
    >>> stk.pop()
    6
    >>> stk.pop()
    5
    """
    def __init__(self):
        self.top = None

    def push(self, x):
        new_push = Node(x)
        new_push.next = self.top
        self.top = new_push

    def pop(self):
        y = self.top.data
        self.top = self.top.next
        return y

doctest.testmod(verbose=1)

