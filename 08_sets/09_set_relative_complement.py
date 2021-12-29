# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 05:03:42 2021

@author: sarak
"""

# set relative complement

def main():
    fruits1 = set(["apple", "banana", "cherry", "apricot"])
    fruits2 = set(["orange", "apricot", "cherry"])

    diff1 = fruits1 - fruits2
    diff2 = fruits2 - fruits1

    print(diff1)    # {'banana', 'apple'}
    print(diff2)    #  {'orange'}

if __name__ == '__main__':
    main()