# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:35:03 2021

@author: sarak
"""
# Set order of keys in dictionary - OrderedDict

def main():
    from collections import OrderedDict
    d= {}
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    d['d'] = 4
    print(d)

    planned_order = ('b', 'c', 'd', 'a')
    e = OrderedDict(sorted(d.items(), key= lambda x: planned_order.index(x[0])))
    print(e)


    print('---------')
    # create index to value mapping dictionary from a list of values
    planned_order = ('b', 'c', 'd', 'a')
    plan = dict(zip(planned_order, range(len(planned_order))))
    print(plan)

    f = OrderedDict(sorted(d.items(), key = lambda x: plan[x[0]]))
    print(f)

                # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
                # OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])
                # ---------
                # {'b': 0, 'c': 1, 'd': 2, 'a': 3}
                # OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])

if __name__ == '__main__':
    main()
