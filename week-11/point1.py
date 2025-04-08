class Point:
    def __init__(self): #self to refer to attributes of this class
        '''
        Create two dimensial point at(0,0)
        '''
        self.x = 0
        self.y = 0

########
# Main Program
p1 = Point() #all args except self
print(f'(x,y) coordinates of p1: ({p1.x, p1.y})')