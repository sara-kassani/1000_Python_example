# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 08:53:33 2021

@author: sarak
"""

# Recursive factorial
def main():
        # n! = n * (n-1) ... * 1
        # 0! = 1
        # n! = n * (n-1)!


    # f(0) = 1
    # f(n) = n* f(n-1)

    def f(n):
        if n == 0:
            return 1
        return n * f(n-1)

    print(f(5))
                    # 120

if __name__ == '__main__':
    main()