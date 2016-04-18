import doctest

class Node(object):
    """
    >>> n = Node(4)
    >>> n.data
    4
    """
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

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
        self.top = None
        self.min_number = None

    def push(self, number):
        new = Node(number)
        if self.top is None and self.min_number is None:
            self.top = new
            self.min_number = new
        new.next = self.top
        new.next = self.min_number
        self.top = new
        self.min_number = new

    def pop(self):
        last = self.top.data
        self.top = self.top.next
        self.min_number = self.min_number.next
        return last

    # XX 這個死循環了 有空再想 沒空的話 min function 你要自立自強 自行修復 乖
    def min(self):
        l =[]
        while self.min_number is not None:
            data = self.min_number.data
            l.append(data)
            self.min_number = self.min_number.next
        sort_l = sorted(l)
        return sort_l[0]

doctest.testmod(verbose=1)