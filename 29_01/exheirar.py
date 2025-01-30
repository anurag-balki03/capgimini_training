class shape:
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    
    def circle_a(self):
        return 3.14*(self.radius**2)
    
class square(shape):
    def __init__(self,side):
        self.side=side
    
    def square_a(self):
        return self.side*self.side

cir=circle(3)
squ=square(4)
print(cir.circle_a())
print(squ.square_a())