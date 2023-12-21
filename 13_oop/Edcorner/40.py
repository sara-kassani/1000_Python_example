import math
class Circle:
    def __init__(self, radius):
        self.radius=radius
        self._area=None
        self._perimeter=None

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius=value
        self._area=None
        self._perimeter= None

    @property
    def area(self):
        if self._area is None:
            self._area=math.pi * self._radius * self._radius
            return self._area
        
    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter= 2* math.pi * self._radius
            return self._perimeter
        

circle=Circle(3)
print(f"{circle.perimeter: .4f}")

"""
 18.8496
"""