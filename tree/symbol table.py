import doctest

class Sym_Node(object):
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

class Sym_Search(object):
    """
    >>> s = Sym_Search()
    >>> s.put('S',0)
    >>> s.put('E',1)
    >>> s.put('A',2)
    >>> s.put('R',3)
    >>> s.get('E')
    1
    """
    def __init__(self):
        self.first = None
        self.pointer = None

    def get(self, key):
        self.pointer = self.first
        while self.pointer is not None:
            if key == self.pointer.key:
                return self.pointer.value
            self.pointer = self.pointer.next
        return None

    def put(self, key, value):
        self.pointer = self.first
        while self.pointer is not None:
            if key == self.pointer.key:
                self.pointer.value = value
                return
            self.pointer = self.pointer.next
        self.first = Sym_Node(key, value, self.first)

doctest.testmod(verbose = 1)