__author__ = 'stephanie'
import doctest

class Node(object):

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Link(object):
    """
    >>> l = Link([1,2,3])
    >>> head = l.get_head()
    >>> while head is not None:
    ...     print(head.data)
    ...     head = head.next
    1
    2
    3
    """

    def __init__(self, seq):
        self.dummy_head = Node()
        self.tail = self.dummy_head
        self.seq = seq
        self.add_node()

    def add_node(self):
        for n in self.seq:
            self.tail.next = Node(n)
            self.tail = self.tail.next
        return self.dummy_head.next

    def get_head(self):
        return self.dummy_head.next







doctest.testmod(verbose=True)

















