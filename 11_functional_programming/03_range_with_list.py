# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 07:02:10 2022

@author: sarak
"""

"""
Using the list function we can tell the range object to generate the whole list immediately.
Either using the variable that holds the range object, or wrapping the range() call in a list() call.

The sys.getsizeof() function returns the size of a Python object in the memory.
As you can see the size of the range object is only 48 bytes while the size of the 3-element list is already 112 bytes.

It seems the range object is better than even such a short lists.
"""

def main():
    import sys
    rng = range(3, 9, 2)
    print(rng)                      # range(3, 9, 2)s
    numbers = list(rng)
    print(numbers)                  # [3, 5, 7]

    others = list(range(3, 9, 2))
    print(others)                   # [3, 5, 7]


    print(sys.getsizeof(rng))       #  48
    print(sys.getsizeof(numbers))   #  80
    print(sys.getsizeof(others))    #  80


if __name__ == '__main__':
    main()
