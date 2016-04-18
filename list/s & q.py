import doctest

class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Queue(object): #FIFO
    """
    >>> q =Queue()
    >>> q.push_queue(4)
    >>> q.push_queue(5)
    >>> q.pop_queue()
    4
    >>> q.pop_queue()
    5
    """
    def __init__(self):
        self.head = None
        self.tail = None
    def push_queue(self, num):
        new = Node(num)
        if self.head is None and self.tail is None:
            self.head = new
            self.tail = new
        self.tail.next = new
        self.tail = self.tail.next
    def pop_queue(self):
        first = self.head.data
        self.head = self.head.next
        return first

class Stack(object): #LIFO
    """
    >>> s =Stack()
    >>> s.push_stack(3)
    >>> s.push_stack(7)
    >>> s.pop_stack()
    7
    >>> s.pop_stack()
    3
    """
    def __init__(self):
        self.top = None
    def push_stack(self, num):
        newpush = Node(num)
        # if self.top is None:
        #     self.top = newpush
        newpush.next = self.top
        self.top = newpush
    def pop_stack(self):
        last = self.top.data
        self.top = self.top.next
        return last

doctest.testmod(verbose=1)


