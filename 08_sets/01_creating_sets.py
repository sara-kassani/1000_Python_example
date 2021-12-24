# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 02:48:10 2021

@author: sarak
"""
"""
Set operations
    • set
    • issubset
    • intersection
    • symmetric difference
    • union
    • relative complement
"""

def main():
    things = set(['table', 'door', 'chair', 'book', 'chair', 'chair'])

    print(things)
    print(type(things))    #  <class 'set'>


    if 'table' in things:
        print('has table')

    other = {'table', 'door', 'chair'}    #  a {} without keys is a set
    print(type(other))    #  <class 'set'>

if __name__ == '__main__':
    main()
