# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:47:51 2022

@author: sarak
"""

def main():
    def double(n):
        return 2*n
    
    numbers = [1,2,3,4]
    name = 'FooBar'
    
    double_numbers = [double(n) for n in numbers]
    print(double_numbers)    # [2, 4, 6, 8]
    
    
    double_chars = [double(c) for c in name]
    print(double_chars)    # ['FF', 'oo', 'oo', 'BB', 'aa', 'rr']
    
if __name__ == '__main__':
    main()