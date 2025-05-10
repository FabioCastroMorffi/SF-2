from progression import Progression

class Fibonacci(Progression):
    def __init__(self, f0 = 0, f1 = 1):
        super().__init__(f0)
        self._prev = f1 - f0
    
    def _advance(self):
        self._current, self._prev = self._prev + self._current, self._current

if __name__ == '__main__':
    Fibonacci(2,5).printProgression(9)