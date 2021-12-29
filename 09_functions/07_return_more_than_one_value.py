# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 08:41:43 2021

@author: sarak
"""

# Return more than one value
def main():
    def calc(x, y):
        a= x+y
        b= x*y
        return a, b

    t = calc(3, 4)
    print(t)
                    # (7, 12)


if __name__ == '__main__':
    main()