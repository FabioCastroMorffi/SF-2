from mammal import Mammal
from pet import Pet
from herbivore import Herbivore

class Bunny(Mammal, Herbivore, Pet):
    def __init__(self, legs = 4, ears = 2):
        # Mammal.__init__(self, legs)
        super().__init__(legs)
        self.ears = ears

    def __repr__(self):
        text = '\nThis animal is a bunny'
        return Mammal.__repr__(self)  +'\n'+ Pet.__repr__(self) + Herbivore.__repr__(self)+text

    def reproduce(self):
        super().reproduce()
        print("Bunnies can produce multiple litters per year\
              potentially having 3-8 kits per litter")
    def move(self):
        print("it moves a lot")

    def sleep(self):
        print("They sleep a lot idk")

    def eat(self):
        Herbivore.eat(self)
        print('I mostly eat whatever')

if __name__ == '__main__':
    b1 = Bunny()
    print(b1)


    print()
    b1.reproduce()

    print()

    b1.move()
    print()
    b1.eat()
    print()
    print(b1.pet())

