# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:06:08 2022

@author: sarak
"""

"""
filter(function, iterable)

filter will return an iterable object that will return all the items of the original iterable that evaluate
the function to True.
This can have only one iterable!
"""

def main():

    numbers = [1, 3, 27, 10, 38]

    def big(n):
        return n > 10

    reduced = filter(big, numbers)
    print(reduced)    #  <filter object at 0x00000175BE361FA0>
    print(list(reduced))    #  [27, 38]

if __name__ == '__main__':
    main()


