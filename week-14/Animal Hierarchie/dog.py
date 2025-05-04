from pet import Pet
from mammal import Mammal
from omnivore import Omnivore

class Dog(Mammal, Omnivore, Pet):
    def __init__(self, legs=4, ears = 2):
        super().__init__(legs)
        self.ears = ears
    def __repr__(self):
        text = '\nSpecies: Dog\n'
        return super().__repr__() + text + Pet.__repr__(self) + '\n\n' + Omnivore.__repr__(self)
    def reproduce(self):
        text = 'Dogs can have 1 or more litters of puppies per year'
        super().reproduce() 
        print(text)
    def eat(self):
        Omnivore.eat(self)
    def move(self):
        print('Dogs move by walking, running, or jumping using their four legs.')
    def sleep(self):
        print('Dogs sleep by lying down, often curling up or stretching out, and they can sleep for 12 to 14 hours a day.')

if __name__ == '__main__':
    doggy = Dog()
    print(doggy)
    print(doggy.reproduce())
    print(doggy.move)
    doggy.eat()