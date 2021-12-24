# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:08:54 2021

@author: sarak
"""

# Exercise: Combine lists

def main():
    c = {}

    with open('file1.txt') as fh:
        for line in fh:
            k, v = line.rstrip("\n").split("=")
            for k in c:
                c[k] += int(v)
            else:
                c[k] = int(v)


    with open('file2.txt') as fh:
        for line in fh:
            k, v = line.rstrip("\n").split("=")
            for k in c:
                c[k] += int(v)
            else:
                c[k] = int(v)

    with open("out.txt") as fh:
        for k in sorted(c.keys()):
            fh.write("{} = {}\n".format(k, c[k]))


if __name__ == '__main__':
    main()