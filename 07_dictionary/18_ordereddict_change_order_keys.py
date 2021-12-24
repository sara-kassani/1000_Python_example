# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:10:24 2021

@author: sarak
"""
# Change order of keys in dictionary - OrderedDict

def main():
    from collections import OrderedDict

    d = OrderedDict()
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    d['d'] = 4

    print(d)
    d.move_to_end('a')

    print(d)
    d.move_to_end('d', last= False)

    print(d)

    for key in d.keys():
        print(key)


            # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
            # OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])
            # OrderedDict([('d', 4), ('b', 2), ('c', 3), ('a', 1)])
            # d
            # b
            # c
            # a

if __name__ == '__main__':
    main()
