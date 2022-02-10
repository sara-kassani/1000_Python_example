# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:04:46 2022

@author: sarak
"""

def main():
    import sys
    
    numbers = [0,1,2,3,4,5,6]
    
    gn = (n*n for n in numbers)
    print(gn)                 # <generator object main.<locals>.<genexpr> at 0x000001490B2300B0>
    print(type(gn))           # <class 'generator'>
    print(sys.getsizeof(gn))  # 112
    print()
    
    
    for num in gn:
        print(num)
                        # 0
                        # 1
                        # 4
                        # 9
                        # 16
                        # 25
                        # 36
    print()
    
    gn = (n*n for n in numbers)
    squares = list(gn)
    print(squares)                  # [0, 1, 4, 9, 16, 25, 36]
    print(sys.getsizeof(squares))   # 120
    
    
    print(list(gn))                 # [] ==> the generator was already exhausted
if __name__ == '__main__':
    main()