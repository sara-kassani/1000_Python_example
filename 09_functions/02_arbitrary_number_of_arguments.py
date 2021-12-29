# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 07:30:34 2021

@author: sarak
"""

# Arbitrary number of arguments

def main():
    def my_sum(*numbers):
        # The values arrive as tuple
        print(numbers)
        print(type(numbers))

        total = 0
        for s in numbers:
            total += s
        return total




    print(my_sum(1))
    print(my_sum(1, 2))
    print(my_sum(1, 2, 3))

    x = [1,2,3,4]
    print(my_sum(*x))

                    # (1,)
                    # <class 'tuple'>
                    # 1
                    # (1, 2)
                    # <class 'tuple'>
                    # 3
                    # (1, 2, 3)
                    # <class 'tuple'>
                    # 6
                    # (1, 2, 3, 4)
                    # <class 'tuple'>
                    # 10

if __name__ == '__main__':
    main()