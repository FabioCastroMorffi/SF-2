from heterotroph import Heterotroph

class Carnivore(Heterotroph):
    def eat(self):
        super().eat()
        print("I eat meat")
    def __repr__(self)