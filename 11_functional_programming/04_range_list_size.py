# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 07:16:36 2022

@author: sarak
"""

def main():
    import sys

    for ix in range(21):
        rng = range(ix)
        lst = list(rng)
        print(f'ix: {ix :>3}, rng size: {sys.getsizeof(rng) :>3}, lst size: {sys.getsizeof(lst) :>4}')

                # ix:   0, rng size:  48, lst size:   56
                # ix:   1, rng size:  48, lst size:   64
                # ix:   2, rng size:  48, lst size:   72
                # ix:   3, rng size:  48, lst size:   80
                # ix:   4, rng size:  48, lst size:   88
                # ix:   5, rng size:  48, lst size:   96
                # ix:   6, rng size:  48, lst size:  104
                # ix:   7, rng size:  48, lst size:  112
                # ix:   8, rng size:  48, lst size:  120
                # ix:   9, rng size:  48, lst size:  128
                # ix:  10, rng size:  48, lst size:  136
                # ix:  11, rng size:  48, lst size:  144
                # ix:  12, rng size:  48, lst size:  152
                # ix:  13, rng size:  48, lst size:  160
                # ix:  14, rng size:  48, lst size:  168
                # ix:  15, rng size:  48, lst size:  176
                # ix:  16, rng size:  48, lst size:  184
                # ix:  17, rng size:  48, lst size:  192
                # ix:  18, rng size:  48, lst size:  200
                # ix:  19, rng size:  48, lst size:  208
                # ix:  20, rng size:  48, lst size:  216

#####################################################################

    # for ix in range(21):
    #     rng = range(ix)
    #     print(f'ix is {ix}, rng is {rng}')

        # ix is 0, rng is range(0, 0)
        # ix is 1, rng is range(0, 1)
        # ix is 2, rng is range(0, 2)
        # ix is 3, rng is range(0, 3)
        # ix is 4, rng is range(0, 4)
        # ix is 5, rng is range(0, 5)
        # ix is 6, rng is range(0, 6)
        # ix is 7, rng is range(0, 7)
        # ix is 8, rng is range(0, 8)
        # ix is 9, rng is range(0, 9)
        # ix is 10, rng is range(0, 10)
        # ix is 11, rng is range(0, 11)
        # ix is 12, rng is range(0, 12)
        # ix is 13, rng is range(0, 13)
        # ix is 14, rng is range(0, 14)
        # ix is 15, rng is range(0, 15)
        # ix is 16, rng is range(0, 16)
        # ix is 17, rng is range(0, 17)
        # ix is 18, rng is range(0, 18)
        # ix is 19, rng is range(0, 19)
        # ix is 20, rng is range(0, 20)

#####################################################################

    # for ix in range(21):
    #     rng = range(ix)
    #     lst = list(rng)
    #     print(f'ix: {ix}, rng: {rng}, list: {lst}')

# ix: 0, rng: range(0, 0), list: []
# ix: 1, rng: range(0, 1), list: [0]
# ix: 2, rng: range(0, 2), list: [0, 1]
# ix: 3, rng: range(0, 3), list: [0, 1, 2]
# ix: 4, rng: range(0, 4), list: [0, 1, 2, 3]
# ix: 5, rng: range(0, 5), list: [0, 1, 2, 3, 4]
# ix: 6, rng: range(0, 6), list: [0, 1, 2, 3, 4, 5]
# ix: 7, rng: range(0, 7), list: [0, 1, 2, 3, 4, 5, 6]
# ix: 8, rng: range(0, 8), list: [0, 1, 2, 3, 4, 5, 6, 7]
# ix: 9, rng: range(0, 9), list: [0, 1, 2, 3, 4, 5, 6, 7, 8]
# ix: 10, rng: range(0, 10), list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ix: 11, rng: range(0, 11), list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ix: 12, rng: range(0, 12), list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# ix: 13, rng: range(0, 13), list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# ix: 14, rng: range(0, 14), list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# ix: 15, rng: range(0, 15), list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# ix: 16, rng: range(0, 16), list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# ix: 17, rng: range(0, 17), list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# ix: 18, rng: range(0, 18), list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# ix: 19, rng: range(0, 19), list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
# ix: 20, rng: range(0, 20), list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


if __name__ == '__main__':
    main()