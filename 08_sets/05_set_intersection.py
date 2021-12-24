# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 04:30:19 2021

@author: sarak
"""

# set intersection
def main():
    english = set(['door', 'car', 'lunar', 'era'])
    spanish = set(['era', 'luna', 'hola'])

    both = english.intersection(spanish)
    print(both)

                # {'era'}


if __name__ == '__main__':
    main()