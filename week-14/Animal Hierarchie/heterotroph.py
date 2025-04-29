from abc import ABCMeta

class Heterotroph(object, metaclass = ABCMeta):
    def __init__(self, legs = 0, fins = 0, wings = 0):
        self.wings = wings
        self.fins = fins
    def eat(self):
        print("I eat other organisms instead of producing food")
    def __repr__(self)->str:
        return f"This organism is a heterotroph, it is ...."
    
#print(Heterotroph())