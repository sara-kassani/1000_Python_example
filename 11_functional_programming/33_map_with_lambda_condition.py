# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 13:09:40 2022

@author: sarak
"""

numbers = [1, 2, 3, 4]

a = map(lambda n: 2*n if n % 2 else n, numbers)
print(list(a)) # [2, 2, 6, 4]