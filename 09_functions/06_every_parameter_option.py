# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 08:29:00 2021

@author: sarak
"""

# Every parameter option

def main():
    def f(op, count= 0, *things, **kw):
        print(op)
        print(count)
        print(things)
        print(kw)
        print(type(things))
        print(type(kw))


    f(2, 3, 4, 5, a= 23, b= 12)

                # 2
                # 3
                # (4, 5)
                # {'a': 23, 'b': 12}
                # <class 'tuple'>
                # <class 'dict'>

if __name__ == '__main__':
    main()