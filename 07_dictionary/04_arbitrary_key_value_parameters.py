# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 08:16:07 2021

@author: sarak
"""

# Arbitrary key-value pairs in parameters **

def main():
    def f(**kw):
        print(kw)
        print(type(kw))

    f(a= 23, b= 12)

                    # {'a': 23, 'b': 12}
                    # <class 'dict'>

if __name__ == '__main__':
    main()