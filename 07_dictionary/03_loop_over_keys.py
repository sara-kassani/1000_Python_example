# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 06:02:56 2021

@author: sarak
"""

def main():
    user = {
        'fname': 'Foo',
        'lname': 'Bar',
        }
    
    for k in user.keys():
        print(k)
                        # fname
                        # lname
    for k in user.keys():
        print("{} -> {}".format(k, user[k]))
        
                        # fname -> Foo
                        # lname -> Bar
    
if __name__ == '__main__':
    main()