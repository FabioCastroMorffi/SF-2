from __future__ import annotations
from animal import Animal
class Fish(Animal):
    def __init__(self):
        super().__init__(0)
        self.type = 'fish'
        self.colour = 'blue'
    def walk(self):
        print('they dont walk')
    def sleep(self):
        print('fish sleep like a lot')
    def __repr__(self):
        return f'Animal: {self.type} \nLegs: {self.legs}'
    def changeColour(self, new_colour: str)-> None:
        self.colour = new_colour
    def sameColour(self,other_fish:Fish)->bool:
        return other_fish.colour == self.colour

if __name__ == '__main__':
    fish = Fish()
    fish2 = Fish()
    print(fish.sameColour(fish2))
        