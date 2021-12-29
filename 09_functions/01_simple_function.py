# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 05:09:12 2021

@author: sarak
"""

# Functions (subroutines)
#  The parameters of every function can be passed either as positional parameters or as named parameters.


def main():
    def add(x, y):
        z = x+y
        return z

    d = add(3, 4)
    print(d)

if __name__ == '__main__':
    main()