# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:11:29 2022

@author: sarak
"""

def main():
    import re
    line1 = 'There is a phone number 12345 in this row and another 42 number'

    numbers1 = re.findall(r'\d+', line1)
    print(numbers1)     #  ['12345', '42']

    line2 = 'There is no mumber in this row.'
    numbers2 = re.findall(r'd+', line2)
    print(numbers2)    #  []


if __name__ == '__main__':
    main()


