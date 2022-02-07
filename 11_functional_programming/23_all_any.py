# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:22:38 2022

@author: sarak
"""

"""
all, any
• all(iterable) - returns True if all the elements of iterable return True
• any(iterable) - returns True if any of the elements in iterable return True
"""

def main():
    a = [True, True]
    b = [True, False]
    c = [False, False]
    
    print(all(a))    # True
    print(all(b))    # False
    print(all(c))    # False
    
    
    print(any(a))    # True
    print(any(b))    # True
    print(any(c))    # False
    
    
if __name__ == '__main__':
    main()