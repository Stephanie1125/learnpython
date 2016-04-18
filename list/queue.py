__author__ = 'stephanie'

import doctest

class Node(object):
    """
    >>> n = Node()
    """
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Queue(object):
    """
    >>> que = Queue()
    >>> que.enque(5)
    >>> que.enque(6)
    >>> que.deque()
    5
    >>> que.deque()
    6
    """
    def __init__(self):
        self.tail = None
        self.head = None

    def enque(self, x):
        new = Node(x)
        if self.tail is None and self.head is None:
            self.tail = new
            self.head = new
        self.tail.next = new
        self.tail = self.tail.next

    def deque(self):
        first_data = self.head.data
        self.head = self.head.next
        return first_data


doctest.testmod(verbose=1)


