class Vector:
    def __init__(self, *components):
        self.components=components

    def __repr__(self):
        return f"Vector{self.components}"
    
    def __str__(self):
        return f"{self.components}"

    def __len__(self):
        return len(self.components)
    
    def __add__(self, other):
        components= tuple(x+y for x, y in zip(self.components + other.components))
        return Vector(*components)

    def __sub__(self, other):
        components= tuple(x-y for x, y in zip(self.componentss, other.components))
        return Vector(*components)
    
    def __mul__(self, other):
        components=tuple(x*y for x, y in zip(self.components, other.components))
        return Vector(*components)
    
    def __truediv__(self, other):
        components=tuple(x/y for x, y in zip(self.components, other.components))
        return Vector(*components)
    
    def __floordiv__(self, other):
        components=tuple(x//y for x,y in zip(self.components, other.components))
        return Vector(*components) 


v1=Vector(4, 2)
v2=Vector(-1, 4)

print(v1 // v2)

"""
(-4, 0)
"""
