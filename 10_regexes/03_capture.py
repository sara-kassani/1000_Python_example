# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 05:29:43 2022

@author: sarak
"""

"""
Parentheses in the regular expression can enclose any sub-expression.
Whatever this sub-expression matches will be saved and can be accessed using the group() method.
"""


def main():
    import re
    line = 'There is a phone number 12345 in this line and an age: 30.'

    match= re.search(r'age: \d+', line)
    if match:
        print(match.group(0))   # age: 30


    match= re.search(r'age: (\d+)', line)
    if match:
        print(match.group(0))    # age: 30
        print(match.group(1))    # 30


        print(match.groups())   # ('30',)
        print(len(match.groups()))   #  1

if __name__ == '__main__':
    main()