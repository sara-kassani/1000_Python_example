# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 07:48:57 2021

@author: sarak
"""

# Fixed parmeters before the others
# The *numbers argument can be preceded by any number of regular arguments

def main():

    def num_op(op, *numbers):

        print(numbers)
        if op == '*':
            total = 1
        elif op == '+':
            total = 0
        else:
            raise Exception('invalid operator {}'.format(op))


        for s in numbers:
            if op == '+':
                total += s
            elif op == '*':
                total *= s

        return total




    print(num_op('+', 5))
    print(num_op('+', 1, 2, 3))
    print(num_op('*', 1, 2, 3))

if __name__ == '__main__':
    main()