# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:00:29 2021

@author: sarak
"""

def main():
    filename = 'files/apache_access.log'
    count = {}

    with open(filename) as fh:
        for line in fh:
            space = line.index(' ')
            ip = line[0:space]

            if ip in count:
                count[ip] += 1
            else:
                count[ip] = 1

    for ip in count:
        print("{:16} {:>3}".format(ip, count[ip]))

if __name__ == '__main__':
    main()