class DLL:
    class _Node:
        __slots__ = '_element', '_prev', '_next' #size fixed

        def __init__(self, elem, prev, next):
            self._element = elem
            self._prev = prev
            self._next = next
    
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        pass

    def isEmpty(self):
        pass
    def insertBetween(self, elem, predecessor, successor):
        pass
    def deleteNode(self, node):
        pass