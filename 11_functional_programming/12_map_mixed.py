# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:44:28 2022

@author: sarak
"""

"""
map works on any iterable, so we might end up passing one list and one string to it.
"""
def main():
    v1 = ['foo', 'bar', 'baz']
    v2 = 'abc'

    result = map(lambda x,y: x+y, v1, v2)
    print(result)    #  <map object at 0x00000175BC996D90>
    print(list(result))    #  ['fooa', 'barb', 'bazc']

if __name__ == '__main__':
    main()





