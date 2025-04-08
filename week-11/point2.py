class Point:
    def __init__(self): #self to refer to attributes of this class
        '''
        Create two dimensial point at(0,0)
        '''
        self.x = 0
        self.y = 0
    def __init__(self, x: int, y: int): #init creates an object
        '''
        Creates two-dimensial Point at (x,y)
        '''
        self.x = x
        self.y = y


########
# Main Program
p1 = Point() #all args except self
print(f'(x,y) coordinates of p1: ({p1.x, p1.y})')