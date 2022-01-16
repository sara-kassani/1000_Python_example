# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 07:57:02 2022

@author: sarak
"""

"""
• map(function, iterable, ...)

The map function applies a function to every item in an iterable and returns an iterator that can be used 
to iterate over the results.

"""

def main():
    def double(n):
        return 2 * n



    numbers = [1, 2, 3, 4]
    name = 'FooBar'

    double_numbers = map(double, numbers)
    double_letters= map(double, name)

    print(double_numbers)    #  <map object at 0x0000018EF28F5BE0>
    print(double_letters)    #  <map object at 0x0000018EF28F5B50>

    for num in double_numbers:
        print(num)
        # 2
        # 4
        # 6
        # 8

    for ch in double_letters:
        print(ch)
        # FF
        # oo
        # oo
        # BB
        # aa
        # rr

if __name__ == '__main__':
    main()