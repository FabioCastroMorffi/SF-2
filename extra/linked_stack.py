class StackLinkedList
    
    #---------> nest Node class------------
    class _Node:
        '''lightweight non-public class for storing sll'''
        __slots__ = '_element', '_next' #class attributes

        def __init__(self,element, next):
            '''create a Node'''
            self._element = element
            self._next = next
    #--------------------------------------

    def push(self, elem):
        self._head = self._Node(elem, self._head)
        self._size += 1

    def top(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self._head._element
    
    def pop(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        