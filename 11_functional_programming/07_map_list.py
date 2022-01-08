# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 08:32:57 2022

@author: sarak
"""

"""
map with list
Imagine a case where you apply several expensive (time consuming) transformations to some
"""

def main():
    def double(n):
        return 2 * n

    numbers = [1, 2, 3, 4]
    name = 'FooBar'

    double_numbers = list(map(double, numbers))
    print(double_numbers)    # [2, 4, 6, 8]

    double_letters = list(map(double, name))
    print(double_letters)    #  ['FF', 'oo', 'oo', 'BB', 'aa', 'rr']


if __name__ == '__main__':
    main()



