# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 04:49:17 2021

@author: sarak
"""

# set symmetric difference
# • Symmetric difference contains all the elements in either one of the sets, but not in both. “the ears of the elephant”.


def main():
    fruits1 = set(["apple", "banana", "cherry", "apricot"])
    fruits2 = set(["orange", "apricot", "cherry"])

    diff = fruits1.symmetric_difference(fruits2)
    print(diff)

            # {'banana', 'apple', 'orange'}

if __name__ == '__main__':
    main()