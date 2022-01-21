# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:26:27 2022

@author: sarak
"""

def main():
    numbers = [1, 3, 10, 27, 38]

    reduced = filter(lambda n: n>10, numbers)
    print(reduced)    #  <filter object at 0x00000175BE361040>
    print(list(reduced))    #  [27, 38]


if __name__ == '__main__':
    main()