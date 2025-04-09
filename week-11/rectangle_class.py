from __future__ import annotations
class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width
    def calculate_area(rectangle: Rectangle) -> int | bool:
        return rectangle.length * rectangle.width if isinstance(rectangle, Rectangle) else False 
    def __repr__(self) -> None: 
        return f'Rectangle dimensions: {self.length, self.width} have an area of {Rectangle.calculate_area(self)}'
rectangle = Rectangle(3,4)
rectangulito = Rectangle(9,0)
print(rectangulito)