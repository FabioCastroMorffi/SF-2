from bird import Bird
from pet import Pet
from omnivore import Omnivore

class Parrot(Bird, Omnivore, Pet):
    def __init__(self, legs = 2, wings = 2, colour = 'Yellow'):
        
        super().__init__(legs)
        self.colour = colour

    def __repr__(self):
        text = '\nSpecies: Parrot'
        return Bird.__repr__(self)  + text +'\n'+ Pet.__repr__(self) + '\n\n' + Omnivore.__repr__(self)

    def reproduce(self):
        text = 'Parrots often take a few days to lay a full clutch \
of eggs. This can be as many as three to four eggs.'
        print(super().reproduce())
        print(text)
    
    def move(self):
        print('I can move in various ways. I can fly, walk, climb and even \
use a unique method called "beakiation" to traverse \
narrow branches')

    def sleep(self):
        print("Parrots sleep around 10 to 12 hours each night, often \
tucked under their wings. They may also take naps during \
the day.")

    def eat(self):
        #.eat(self)
        Omnivore.eat(self)
        print('I eat both plant and animal matter. My natural diet includes \
a variety of foods like seeds, nuts, fruits, vegetables, \
flowers, buds, and insects.')
    
    
    
if __name__ == '__main__':
    b1 = Parrot()
    print(b1)


    
    b1.reproduce()

    print()

    b1.move()
    print()
    b1.eat()
    print()
    print(b1.pet())

