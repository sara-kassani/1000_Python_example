# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 09:38:42 2022

@author: sarak
"""

def main():
    numbers = [1, 2, 3, 4]

    pairs = map(lambda n: (n, n *2), numbers)
    print(pairs)    #  <map object at 0x0000018EF294EA00>


    for pair in pairs:
        print(pair)

        # (1, 2)
        # (2, 4)
        # (3, 6)
        # (4, 8)

# lambda with two parameters: A lambda-function can have more than one parameters:

    add = lambda x,y: x+y
    print(add(2, 3))      # 5


if __name__ == '__main__':
    main()