# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 05:03:42 2021

@author: sarak
"""

# set relative complement

def main():
    english = set(['door', 'car', 'lunar', 'era'])
    spanish = set(['era', 'lunar', 'hola'])

    eng = english - spanish
    spa = spanish - english

    print(eng)    # {'door', 'car'}
    print(spa)    #  {'hola'}

if __name__ == '__main__':
    main()