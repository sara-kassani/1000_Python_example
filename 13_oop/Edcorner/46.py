class Doc:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __add__(self, other):
        if isinstance(other, Doc):
            return Doc(self.string + ' ' + other.string)
        return NotImplemented

    def __str__(self):
        return self.string

doc1 = Doc("Python")
doc2 = Doc("3.15")

print(doc1 + doc2)

"""
Python 3.15
"""
