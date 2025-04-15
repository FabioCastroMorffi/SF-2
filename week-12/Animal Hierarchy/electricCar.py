from __future__ import annotations
from car import Car

class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        self.battery = 40
    def __repr__(self):
        
