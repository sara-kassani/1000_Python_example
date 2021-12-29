# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 08:25:35 2021

@author: sarak
"""

def main():
    def f(name, **kw):
        print(name)
        print(kw)
        print(type(kw))


    f(name= 'Foo', a= 23, b= 12)
                # Foo
                # {'a': 23, 'b': 12}
                # <class 'dict'>

if __name__ == '__main__':
    main()