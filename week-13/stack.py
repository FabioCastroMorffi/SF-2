from __future__ import annotations
from functools import total_ordering
import ansi_codes
#@total_ordering
class Empty(Exception):
    '''error attempting to access an element from empty container '''
    pass

class Stack:
    def __init__(self):
        self.__data = []
    def __len__(self):
        return len(self.data)
    def isEmpty(self) -> bool:
        return not(len(self.__data))
    def pop(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self.__data.pop()
    def push(self, elem:object): #most general type is object
        """add element to the top of the stack
        >>> s = Stack()
        >>> s.push(15)
        >>> s.push(17)
        >>> s.pop()
        1

        """
        self.__data.append(elem)
    def top(self)-> object:
        if self.isEmpty():
            raise Empty('hello')
        return self.__data[-1]
    def __repr__(self)-> str:
        string = ''
        if self.isEmpty():
            return ansi_codes.WHITE + '|    |\n------' + ansi_codes.RESET
        for item in range(len(self.__data)-1,-1,-1):
            
            if item == 0:
                string += f'|{str(self.__data[item]).center(4)}|\n------\n'
            else:
                string += f'|{str(self.__data[item]).center(4)}|\n'
        return string
        #return string
    
    def __lt__(self, other_stack: Stack)-> bool: #this
        pass
    def __eq__(self, other_stack: Stack)-> bool: #this
        pass
    
if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(6)
    s.push(8)
    print(s)
    # import doctest
    # doctest.testmod()
    # S = Stack()
    # S.push(5)
    # S.pop()
    # S.isEmpty()


        