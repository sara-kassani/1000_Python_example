# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 04:49:17 2021

@author: sarak
"""

# set symmetric difference
# • Symmetric difference contains all the elements in either one of the sets, but not in both. “the ears of the elephant”.


def main():
    english = set(['door', 'car', 'lunar', 'era'])
    spanish = set(['era', 'luna', 'hola'])

    diff = english.symmetric_difference(spanish)
    print(diff)

            # {'door', 'car', 'hola', 'luna', 'lunar'}

if __name__ == '__main__':
    main()