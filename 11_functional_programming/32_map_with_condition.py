# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 13:03:22 2022

@author: sarak
"""

numbers = [1, 2, 3, 4]

def cond_double(n):
    if n % 2:
        return 2*n
    else:
        return n

cd = map(cond_double, numbers)
print(list(cd)) # [2, 2, 6, 4]