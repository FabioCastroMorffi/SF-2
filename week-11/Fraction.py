from __future__ import annotations
import math

def reduceFraction(denominator:int, numerator: int):
    while math.gcd(int(denominator), int(numerator)) != 1:
            gcd = int(math.gcd(denominator, numerator))
            denominator /= gcd
            numerator /= gcd
    return numerator, denominator

class Fraction: 
    def __init__(self, numerator=0, denominator=1, sign='Positive'):
        
        if denominator==0:
            raise ZeroDivisionError("no zero division")
        if numerator == 0:
            denominator = 1
            numerator = 0
        if sign != 'Positive':
            self.sign = 'Negative'
        
        self.numerator, self.denominator = reduceFraction(denominator, numerator)
        print(type(self.denominator))
    def __add__(self,other_fraction: Fraction)-> Fraction:
        new_numerator = self.numerator * other_fraction.denominator + self.denominator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        added_fraction = Fraction(new_numerator,new_denominator)
        return added_fraction
    def __repr__(self):
        return f'({self.numerator} / {self.denominator}) '
    
fraction = Fraction(8,12)


        
        
    