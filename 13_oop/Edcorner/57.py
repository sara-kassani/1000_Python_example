import math

class Point:

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    def reset(self):
        self.x=0
        self.y=0

    def calc_distance(self, other):
        return math.sqrt((self.x - other.x) **2 + (self.y - other.y)**2)
    
p1= Point(0, 3)
p2=Point(4, 0)

print(p1.calc_distance(p2))

"""
5.0
"""