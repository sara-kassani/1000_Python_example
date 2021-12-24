# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 04:56:43 2021

@author: sarak
"""

def main():
    english = set(['door', 'car', 'lunar', 'era'])
    spanish = set(['era', 'lunar', 'hola'])

    all_words = english.union(spanish)
    print(all_words)

            # {'door', 'car', 'hola', 'lunar', 'era'}

if __name__ == '__main__':
    main()