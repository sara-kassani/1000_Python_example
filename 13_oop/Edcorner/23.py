"""
Implement a class named Vector that takes any number of n-dimensional vector coordinates as arguments
when creating an instance (without any validation) and assign to instance attribute named components. 
Then create two instances with following coordinates:
• (1, 2)
• (4, 5, 2)
and assign to variables v7 and v2 respectively.
- Print the value of the components attribute for v1 and v2 instance
"""

class Vector:
    def __init__ (self, *components):
        self.components=components

V1= Vector(1, 2)
V2=Vector(4, 5, 2)

print(f"v1 ->{V1.components}")
print(f"v2 -> {V2.components}")

"""
v1 ->(1, 2)
v2 -> (4, 5, 2)
"""