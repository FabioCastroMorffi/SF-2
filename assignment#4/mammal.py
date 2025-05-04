from animal import Animal
#no need to repeat abstract stuff (inheriting)
class Mammal(Animal): #inheritance
    def reproduce(self):
        result = ' Mammals give birth to live young and raise them until they can be independent'
        print(super().reproduce() + result)
        
    def __repr__(self):
        text = '\nClass: Mammal'
        return super().__repr__() + text
