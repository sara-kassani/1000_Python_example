# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:58:44 2022

@author: sarak
"""

def main():
    animals = ['chicken', 'cow', 'snail', 'elephant', 'pig', 'zebra', 'gnu', 'praying mantiss', 'snake']
    length = map(len, animals)
    print(length)    #  <map object at 0x00000175BE361A60>
    print(list(length))    #  [7, 3, 5, 8, 3, 5, 3, 15, 5]


if __name__ == '__main__':
    main()