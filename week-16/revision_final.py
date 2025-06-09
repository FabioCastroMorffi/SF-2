from __future__ import annotations
from functools import total_ordering
'''Galactic Explorer's Map'''

class CelestialBody:
    def __init__(self, name: str, position:int):
        self.name_pos = (name, position)
    def describe(self):
        return f"{self.name_pos[0]} at position {self.name_pos[1]}"
class Star(CelestialBody):
    def __init__(self,name:str, position:int,  temperature:int):
        super().__init__(name, position)
        self.temperature = temperature
    def describe(self):
        return f"{super().describe()}, a star with temperature {self.temperature} K"

class Planet(CelestialBody):
    def __init__(self, name, position, gravity, moons:list[str]):
        super().__init__(name,position)
        self.gravity = gravity
        self.moons = moons
    def describe(self):
        return f"{super().describe()}, a planet with gravity {self.gravity} m/s^2 and moons: {self.moons if self.moons else []}."

class Galaxy:
    def __init__(self, name, lst:list[CelestialBody]):
        self.name = name
        self.CelestialList = lst
        self.start = 0
        self.end = len(lst) -1
    def find_planet(name)-> CelestialBody:
        pass
    def __iter__(self):
        return self
    def _advance(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            self.start += 1
            return self.start

def readFile(file_name):
    d = {}
    try:
        input_file = open(file_name, 'r')
    except FileNotFoundError:
        print('File is not in here')
    else:
        lst_lines = (input_file.readlines())
        flag = False
        for chars in lst_lines:
            print(chars)

# What are the contents of book.txt assuming the file did not exist before?
# What prints?

# How many lines are output by this nested loop?

# What is the output of this code?

num1 = 2

num2 = 3

num3 = 12

print('S = ', num1+num2+num3)

d

if '__main__' == __name__:
    Sun = Star('Sun', 3000, 10000)
    print(Sun.describe())

