# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:09:27 2021

@author: sarak
"""

def main():
    seq = 'ACTNGTGCTYGATRGTAGCYXGTN'
    count = {}

    for c in seq:
        if c not in count:
            count[c] = 0

        count[c] += 1

    for c in sorted(count.keys()):
        print("{} {} - {:>5.2f} %".format(c, count[c], 100*count[c] / len(seq)))

if __name__ == '__main__':
    main()