from __future__ import annotations
class Car:
    def __init__(self, brand='Toyota', year=2025, fuel_level=100)-> None:
        self.brand = brand
        self.year = year
        self.fuel_level = fuel_level
    def __repr__(self)-> None:
        return f'The car is a {self.brand} from {self.year} with {self.fuel_level}%'
    def refuel(self, fuel:int)-> None:
        if fuel + self.fuel_level > 100:
            self.fuel_level = 100
        else:
            self.fuel += fuel
    def drive(self,distance:int)-> tuple:
        if self.fuel_level - distance < 0:
            self.fuel_level = 0
            return (0, self.fuel_level)
        else:
            self.fuel_level -= distance
            return (self.fuel_level, distance)
    def __lt__(self, other_car: Car)->bool:
        return isinstance(other_car, Car) and self.year < other_car.year

    
        


        



