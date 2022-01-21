# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:49:10 2022

@author: sarak
"""

def main():

    people = [
        {
        'name': 'Foo',
        'phone': '123',
        },
        {
        'name': 'Bar',
        'phone': '456',
        },
        {
        'name': 'SnowWhite',
        'phone': '7-dwarfs',
        }
    ]

    names = map(lambda d: d['name'], people)
    print(names)    #  <map object at 0x00000175BE361220>
    print(list(names))    #  ['Foo', 'Bar', 'SnowWhite']

if __name__ == '__main__':
    main()