from progression import Progression

class EvenProgression(Progression):
    def __init__(self, start):
        super().__init__(start)
        if self.start % 2 != 0:
            start += 1
    def _advance(self):
        self.start += 2
    def __iter__(self):
        return self
    def __next__(self):
        self.
    def printProgression(self, num):
        return super().printProgression(num)
    def lstProgression(self, num):
        return super().lstProgression(num)
    
Progression(9).printProgression(99)