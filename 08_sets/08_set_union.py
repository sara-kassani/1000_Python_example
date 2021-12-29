# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 04:56:43 2021

@author: sarak
"""

def main():
    fruits1 = set(["apple", "banana", "cherry", "apricot"])
    fruits2 = set(["orange", "apricot", "cherry"])

    all_fruits = fruits1.union(fruits2)
    print(all_fruits)

            # {'cherry', 'banana', 'apple', 'orange', 'apricot'}

if __name__ == '__main__':
    main()