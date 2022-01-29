# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:00:58 2022

@author: sarak
"""
"""
reduce(function, iterable[, initializer])

"""

def main():
    from functools import reduce
    numbers = [1, 2, 3, 4]
    
    print(reduce(lambda x,y: x+y, numbers))    # 10 = ((1+2)+3)+4
    print(reduce(lambda x,y: x*y, numbers))    # 24 = ((1*2)*3)*4
    print(reduce(lambda x,y: x/y, [8, 4, 2]))  # 1.0
    
    print(reduce(lambda x,y: x+y, [2])) # 2
    
    
    mysum = 0
    for num in numbers:
        mysum += num
    print(mysum)            # 10
    
    
    mymultiple = 1
    for num in numbers:
        mymultiple *= num
    print(mymultiple)       #24


if __name__ == '__main__':
    main()