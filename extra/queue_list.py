from empty import Empty

class QueueList:
    '''FIFO queue implementation with a Python list as the underlying infrastructure'''

    def __init__(self):
        '''create an empty queue'''
        self.data = []
        self._size = 0
        self._front = 0
    
    def __len__(self):
        '''return number of elements in queue'''
        return self._size
    def isEmpty(self):
        return self._size
    
    def first(self):
        '''return (but not remove) element at the front of queue'''
        if self.isEmpty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        '''remove and return the first element in queue'''
        if self.isEmpty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None # to help garbage collection (none elements get removed after sometime)
        self._front += 1
        self._size -= 1
        return answer
    
    def enqueue(self, elem):
        self._data.append(elem)
        self._size += 1

    

