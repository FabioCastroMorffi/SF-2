from progression import Progression

class ArithmeticProgression(Progression):
    ''' iterator producing arithmetic progression '''

    def __init__(self, increment = 1, start = 0):
        # i dont need to repeat self._current cause its in parent class
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment

    
if __name__ == '__main__':
    print('Arithmetic Progression')
    ArithmeticProgression(7,8).printProgression(12)

