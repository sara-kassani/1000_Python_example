# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 06:09:38 2022

@author: sarak
"""
"""
Functional programming
Iterators (Iterables)
You already know that there are all kinds of objects in Python that you can iterate over using the
for in construct.
For example you can iterate over the characters of a string, or the elements of a list, or whatever
range() returns.
You can also iterate over the lines of a file
and you have probably seen the for in construct in other cases as well. The objects that can be
iterated over are collectively called


• A few data type we can iterate over using the for … in … construct. (strings, files, tuples, lists,
list comprehension)
"""

def main():
    numbers= [101, 2, 3, 42]

    for num in numbers:
        print(num)

    print(numbers)
                # 101
                # 2
                # 3
                # 42
                # [101, 2, 3, 42]

    print()

    name= 'FooBar'
    print(name)
    for ch in name:
        print(ch)

                # FooBar
                # F
                # o
                # o
                # B
                # a
                # r

    print()

    rng= range(3, 9, 2)
    print(rng)

    for num in rng:
        print(num)

                # range(3, 9, 2)
                # 3
                # 5
                # 7

if __name__ == '__main__':
    main()