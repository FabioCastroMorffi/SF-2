from __future__ import annotations
import math

class Point:
    #methods
    def __init__(self, x: int, y: int): #init creates an object, linked to name of class
        '''
        Creates two-dimensial Point at (x,y)
        '''
        self.x = x
        self.y = y
    def translate(self, dx: int, dy: int):
        '''
        Move point dx horizontally and dy vertically
        '''
        self.x += dx
        self.y += dy
    def distance(self, other_point: Point) -> float:
        '''
        Return distance between this (ie. self) point and point given as argument
        '''
        a = (other_point.x - self.x) ** 2
        b = (other_point.y - self.y) ** 2
        return math.sqrt(a+b)
    def __repr__(self) -> str: # print directly connected to that
        '''
        Return x,y coordinates of Point (x,y)
        '''
        return f'({self.x}, {self.y})'
    def __lt__(self, other_point: Point) -> bool: #relates to '<' (less than)
        '''
        return True if this Point and other_point are of type Point and x, y coordinates of this point 
        < x, y coordinates of other_point
        '''
        return isinstance(other_point, Point) and self.x < other_point.x and self.y < other_point.y
    def __equal__(self, other_point: Point) -> bool: 
        return isinstance(other_point, Point) and self.x == other_point.x and self.y == other_point.y
    

########
# Main Program
p1 = Point(2,5) #all args except self
print(f'(x,y) coordinates of p1: ({p1.x, p1.y})')
p1.translate(2,5)

p2 = Point(2,4)
print(p1.distance(p2))
#print(p1.x)

print(p1<2)