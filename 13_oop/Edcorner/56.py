class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    def reset(self):
        self.x=0
        self.y=0

p=Point(4, 2)
print(p)

p.reset()
print(p)


"""
Point(x=4, y=2)
Point(x=0, y=0)
"""