# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 09:28:46 2022

@author: sarak
"""

def main():
    def dbl(n):
        return 2*n

    double = lambda n: 2*n

    print(dbl(3))       # 6
    print(double(3))    # 6


# lambda returning tuple
# A lambda function can return complex data structures as well. e.g. a tuple.

    dbl = lambda n: (n, n*2)
    answer = dbl(3)
    print(answer)           #  (3, 6)
    print(type(answer))     #  <class 'tuple'>


if __name__ == '__main__':
    main()