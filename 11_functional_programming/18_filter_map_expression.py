# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:11:15 2022

@author: sarak
"""

def main():
    
    numbers = [1, 7, 19, 5, 57, 23, 8]
    
    def big(x):
        return x>10
    
    def double(y):
        return 2*y
    
    for num in map(double, filter(big, numbers)):
        print(num)
        
if __name__ == '__main__':
    main()
    
    # 38
    # 114
    # 46