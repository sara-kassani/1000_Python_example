# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 09:01:52 2022

@author: sarak
"""
"""
Lambda creates simple anonymous function. It is simple because it can only have one statement in
its body. It is anonymous because usually it does not have a name.
"""
def main():
    numbers = [1, 2, 3, 4]
    name = 'FooBar'

    double_numbers = list(map(lambda x: x *2, numbers))  #
    print(double_numbers)    #  [2, 4, 6, 8]

    double_letters = list(map(lambda x: x *2, name))
    print(double_letters)    #  ['FF', 'oo', 'oo', 'BB', 'aa', 'rr']

if __name__ == '__main__':
    main()