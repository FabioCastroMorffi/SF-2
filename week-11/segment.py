from __future__ import annotations
from point import Point


class Segment:
    '''
    Line segments
    '''
    def __init__(self, p1: Point, p2: Point):
        '''
        Create Segment between p1 and p2
        '''
        self.p1 = p1
        self.p2 = p2
    def translate(self, dx: int, dy: int) -> None:
        '''
        Move Segment by dx hor. and dy vertically
        '''
        self.p1.translate((dx,dy))
        self.p2.translate((dx,dy))
    def length(self) -> float:
        '''Return length of Segment'''
        return self.p1.distance(self.p2)
    def __lt__(self, other_segment: Segment) -> bool:
        return isinstance(other_segment, Segment) and self.length() < other_segment.length()
# Main
p1 = Point(3,4)
p2 = Point(0,0)
line_seg = Segment(p1,p2)
#line_seg.translate(4,0)
length1 = line_seg.length()

p3 = Point(2,3)
p4 = Point(7,8)
line_seg1 = Segment(p3,p4)
print(line_seg < line_seg1)