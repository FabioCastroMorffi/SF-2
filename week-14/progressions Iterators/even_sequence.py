from progression import Progression

class EvenProgression(Progression):
    def __init__(self, start):
        if start % 2 != 0:
            start += 1
        super().__init__(start)
        
    def _advance(self):
        self._current += 2
    
    
    
    
if __name__ == '__main__':
    
    EvenProgression(9).printProgression(99)