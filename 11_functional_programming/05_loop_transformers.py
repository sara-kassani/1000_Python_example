# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 07:48:02 2022

@author: sarak
"""

"""
for loop with transformation
There are many cases when we have a list of some values and we need to apply some transformation
to each value.

very simple such transformation would be to double each value.
In this example we just double the values and use append to add each value to the list containing the results.
"""

def main():
    def double(n):
        return 2 * n

    numbers = [1, 2, 3, 4]
    name = 'FooBar'

    double_numbers = []

    for num in numbers:
        double_numbers.append(double(num))

    print(double_numbers)    # [2, 4, 6, 8]


    double_letters = []
    for ch in name:
        double_letters.append(double(ch))

    print(double_letters)    # ['FF', 'oo', 'oo', 'BB', 'aa', 'rr']

### There are better ways to do this. ###

if __name__ == '__main__':
    main()