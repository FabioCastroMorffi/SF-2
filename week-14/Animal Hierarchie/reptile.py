from animal import Animal

class Reptile(Animal):
    def __repr__(self):
        text = '\nClass: Reptile'
        return super().__repr__() + text
    def reproduce(self):
        text = ' Reptiles reproduce by laying eggs, typically on land rather than water.'
        print(super().reproduce() + text)

