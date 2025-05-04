from animal import Animal

class Amphibian(Animal):
    def __repr__(self):
        text = '\nClass: Amphibian'
        return super().__repr__() + text
    def reproduce(self):
        text = 'Amphibians reproduce by laying soft eggs in water.'
        print(super().reproduce() + text)