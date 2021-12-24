# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:52:27 2021

@author: sarak
"""

# Exercise: Count words from file

def main():
    import sys
    filename = 'READMAE'

    if len(sys.argv) >1:
        filename = sys.argv[1]
    print(filename)


    count = {}
    with open(filename) as fh:
        for full_line in fh:
            line = full_line.rstrip("\n")
            line = line.lower()

    for word in line.split():
        if word == ' ':
            continue
        if word not in count:
            count[word] = 1

        count[word] += 1


    for word in sorted(count):
        print("{:13} {:>2}".format(word, count[word]))

if __name__ == '__main__':
    main()