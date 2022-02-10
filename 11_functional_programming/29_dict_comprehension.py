# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:29:25 2022

@author: sarak
"""

def main():
    people = {
    'Foo': 123,
    'Bar': 456,
    'SnowWhite': 7,
    }
    
    doubles = {k: v*2 for (k, v) in people.items()}
    print(doubles)
    
            # {'Foo': 246, 'Bar': 912, 'SnowWhite': 14}

if __name__ == '__main__':
    main()