# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:40:24 2022

@author: sarak
"""

def main():
    print(2 > 1) # True
    print(0 > 1) # False
    print()
    
    numbers = [2, 4]
    
    # compare each element with the scalar and then check if 'all' were True
    print(all(map(lambda x: x>1, numbers)))  # True
    print(all(map(lambda x: x>2, numbers)))  # False
    
if __name__ == '__main__':
    main()