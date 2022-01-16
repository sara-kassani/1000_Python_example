# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 09:50:15 2022

@author: sarak
"""
"""
map for more than one iterable
Lets “add” together two lists of numbers.
Using + will just join the two lists together, but we can use the “map” function to add the values pair-wise.
"""

def main():
    v1 = [1, 3, 5, 9]
    v2 = [2, 6, 4, 8]

    v3 = v1 + v2
    print(v3)     # [1, 3, 5, 9, 2, 6, 4, 8]s

    sums = map(lambda x,y: x+y, v1, v2)
    print(sums)      # <map object at 0x0000018EF295A100>
    print(list(sums))     # [3, 9, 9, 17]

if __name__ == '__main__':
    main()

