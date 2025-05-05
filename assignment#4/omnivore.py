from heterotroph import Heterotroph

class Omnivore(Heterotroph):
    def __repr__(self):
        text = ' This organism is an omnivore, it can feed on both plants and other animals.'
        return super().__repr__() + text
    def eat(self):
        super().eat()
        print('I eat anything.')
