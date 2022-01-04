# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 05:51:52 2022

@author: sarak
"""

def main():
    import re
    line= 'There is a phone number 12345 in this row and an age: 23'
    match= re.search(r'(\w+): (\d+)', line)

    if match:
        print(match.group(0))   #  age: 23
        print(match.group(1))   #  age
        print(match.group(2))   #  23

        # print(match.group(3))   #  IndexError: no such group
        print(match.groups())   #  ('age', '23')
        print(len(match.groups()))   #  2


if __name__ == '__main__':
    main()