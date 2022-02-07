# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:08:14 2022

@author: sarak
"""

def main():
    fname = ['Graham', 'Eric', 'Terry', 'Terry', 'John', 'Michael']
    lname = ['Chapman', 'Idle', 'Gilliam', 'Jones', 'Cleese', 'Palin']
    born = ['8 January 1941', '29 March 1943', '22 November 1940', '1 February 1942', 
            '27 October 1939', '5 May 1943']
    
    for f_name, l_name, b_date in zip(fname, lname, born):
        print("{:10} {:10} was born on {}".format(f_name, l_name, b_date))
    
if __name__ == '__main__' :
    main()
    
            # Graham     Chapman    was born on 8 January 1941
            # Eric       Idle       was born on 29 March 1943
            # Terry      Gilliam    was born on 22 November 1940
            # Terry      Jones      was born on 1 February 1942
            # John       Cleese     was born on 27 October 1939
            # Michael    Palin      was born on 5 May 1943