import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._area = None  # Resetting _area to None when radius changes

    def calculate_area(self):
        if self._area is None:
            self._area = math.pi * self._radius ** 2
        return self._area

    @property
    def area(self):
        return self.calculate_area()

circle = Circle(3)
print(f"{circle.area:.4f}")  # Accessing the area using the area property


"""
28.2743
"""