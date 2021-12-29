# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 04:30:19 2021

@author: sarak
"""

# set intersection
def main():
    fruits1 = set(["apple", "banana", "cherry", "apricot"])
    fruits2 = set(["orange", "apricot", "cherry"])

    both = fruits1.intersection(fruits2)
    print(both)

                # {'cherry', 'apricot'}


if __name__ == '__main__':
    main()