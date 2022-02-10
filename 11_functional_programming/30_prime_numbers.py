# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:58:03 2022

@author: sarak
"""

def main():
    n = 50
    
    nums = range(2, n)
    for i in range(2, 1+int(n ** 0.5)):
        nums = filter(lambda x: x == i or x % i, nums)
    
    print(nums)
    
    
if __name__ == '__main__':
    main()