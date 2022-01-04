# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 13:38:24 2022

@author: sarak
"""
"""
Use raw strings for regular expression: r’a\d’.
    • \d matches a digit.
    • + is a quantifier and it tells \d to match one or more digits.
It matches the first occurrence.
"""


def main():
    import re
    line = ' There is a phone number 12345 in this line and an age of 23'

    match = re.search(r'\d+', line)

    if match:
        print('Found Match')
        print(match.group(0))

    else:
        print('No match')

if __name__ == '__main__':
    main()