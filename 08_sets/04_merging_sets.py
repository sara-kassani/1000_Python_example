# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 03:59:44 2021

@author: sarak
"""

# Merging one set into another set (update)
def main():
    # set(['Mars', 'Neptun'])

    objects = set(['Mars', 'Jupiter', 'Neptun'])
    internal = set(['Mercury', 'Venus', 'Earth', 'Mars'])

    print(objects)
    print(internal)

    print(' ')

    objects.update(internal)
    print(objects)    #  {'Mercury', 'Neptun', 'Earth', 'Venus', 'Mars', 'Jupiter'}
    print(internal)    #  {'Mars', 'Venus', 'Mercury', 'Earth'}


if __name__ == '__main__':
    main()