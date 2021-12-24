# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 01:39:44 2021

@author: sarak
"""

"""
immutable collection: tuple as dictionary key
"""

def main():
    points = {}
    p1 = (2,3)
    
    points[p1] = 'Joe'    #    p1 is the key, Joe is the value
    
    # print(p1)    #  (2, 3)
    # print(points)   #  {(2, 3): 'Joe'}
    
    points[(17, 5)] = 'Jane'

    print(points)    #  {(2, 3): 'Joe', (17, 5): 'Jane'}

    

    for k in points.keys() :
        print(k)
        print(k.__class__.__name__)
        print(points[k])
    
                    # (2, 3)
                    # tuple
                    # Joe
                    # (17, 5)
                    # tuple
                    # Jane
    
    
if __name__ == '__main__':
    main()