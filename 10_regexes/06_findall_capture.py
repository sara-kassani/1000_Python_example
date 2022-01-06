# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:23:53 2022

@author: sarak
"""

def main():
    import re
    line = 'There is a phone number 12345 in this row and a number 45.'
    match = re.search(r'\w+ \d+', line)
    if match:
        print(match.group(0))    #  number 12345


    match = re.search(r'\w+ (\d+)', line)
    if match:
        print(match.group(0))    #  number 12345
        print(match.group(1))    #  12345

    matches = re.findall(r'\w+ \d+', line)
    if matches:
        print(matches)     #  ['number 12345', 'number 45']

    matches = re.findall(r'\w+ (\d+)', line)
    if matches:
        print(matches)     # ['12345', '45']

if __name__ == '__main__':
    main()