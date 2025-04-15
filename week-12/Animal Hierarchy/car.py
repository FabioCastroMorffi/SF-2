from __future__ import annotations

class Car:
    def __init__(self, make='tungsteno', model='Toyota', year=1998, odometer_reading=0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading
    def __repr__(self):
        return f'{self.make} {self.model}'.title()
    def changeOdometer(self,new_val:int):
        self.odometer_reading = new_val
    
car = Car()
print(car)