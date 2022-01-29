# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:56:31 2022

@author: sarak
"""
def main():
    numbers = [1, 7, 19, 5, 57, 23, 8]
    
    def big(x):
        print(f"filtering: {x}")
        return x > 10
    
    
    def double(y):
        print(f"double {y}")
        return 2 * y
        
    
    big_numbers = list(filter(big, numbers))
    print(big_numbers)
    
    doubles = list(map(double, big_numbers))
    print(doubles)
    
if __name__ == '__main__':
    main()