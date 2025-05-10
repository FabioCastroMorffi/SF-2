class Progression:
    '''
    iterator producing a generic progression

    default iterator produces the whole number
    '''
    def __init__(self, start = 0):
        self._current= start

    def _advance(self):
        '''
        update self._current to a new value
        '''
        self._current += 1

    def __next__(self):
        '''
        return the next element or raise stop
        '''
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer
    def __iter__(self):
        '''by convention an iterator returns itself as an iterator'''
        return self
    def printProgression(self, num):
        '''Print next n values of the progression'''
        print(' '.join(str(next(self)) for _ in range(num)))
    def lstProgression(self, num):
        return [int(next(self)) for _ in range(num)]
    
if __name__ == '__main__':
    print('Default progression')
    Progression().printProgression(10)

    #for values in Progression().lstProgression(10):
    #   print(values * 2)
