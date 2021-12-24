# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 04:35:16 2021

@author: sarak
"""

# set subset

def main():
    english = set(['door', 'car', 'lunar', 'era'])
    spanish = set(['era', 'luna', 'hola'])

    words = set(['door', 'lunar'])

    print('issubset: ', words.issubset(english))
    print('issubset: ', words.issubset(spanish))

                # issubset:  True
                # issubset:  False

if __name__ ==  '__main__':
    main()