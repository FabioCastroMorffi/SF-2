from mammal import Mammal
from pet import Pet
from herbivore import Herbivore

class Bunny(Mammal, Herbivore, Pet):
    def __init__(self, legs = 4, ears = 2):
        # Mammal.__init__(self, legs)
        super().__init__(legs)
        self.ears = ears

    def __repr__(self):
        text = '\nSpecies: Bunny'
        return Mammal.__repr__(self)  + text +'\n'+ Pet.__repr__(self) + '\n\n' + Herbivore.__repr__(self)

    def reproduce(self):
        super().reproduce()
        print("Bunnies can produce multiple litters per year potentially having 3-8 kits per litter")
    
    def move(self):
        print("I move by hopping and I can see behind me...")

    def sleep(self):
        print("Bunnies are nocturnal animals, typically sleep around 12 to 14 hours a day in short, intermittent periods.")

    def eat(self):
        #.eat(self)
        Herbivore.eat(self)
        print('I mostly eat fresh hat and grass, with some leafy greens and a few pellets. I should only be given fruit and root vegetables, like carrots, as an occasional treat. ')
    
    
    
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

