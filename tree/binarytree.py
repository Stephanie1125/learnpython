import doctest

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.left = None
        self.right = None
        self.value = value

class BinaryTree(object):
    """
    >>> b = BinaryTree()
    >>> b.insert(0,1)
    >>> b.get(0)
    1
    """
    def __init__(self):
        self.root = None

    def __insert(self, node, key, val):
        if node is None:
            return Node(key, val)
        if key < node.key:
            node.left = self.__insert(node.left, key, val)
        elif key > node.key:
            node.right = self.__insert(node.right, key, val)
        else:
            node.value = val
        return node

    def insert(self, key, val):
        self.root = self.__insert(self.root, key, val)

    def __get(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self.__get(node.left, key)
        elif key > node.key:
            return self.__get(node.right, key)
        else:
            return node.value

    def get(self, key):
        return self.__get(self.root,key)


doctest.testmod(verbose=1)


