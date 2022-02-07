# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:55:18 2022

@author: sarak
"""

def main():
    import sys
    
    numbers = [0, 1, 2, 3]
    
    sqrs = map(lambda n: n*n, numbers)
    print(list(sqrs))                   # [0, 1, 4, 9]
    print(sys.getsizeof(sqrs))          # 48
    print()
    
    squares = [n*n for n in numbers]
    print(squares)                      # [0, 1, 4, 9]
    print(sys.getsizeof(squares))       # 88

    
if __name__ == '__main__':
    main()