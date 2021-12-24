# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 03:37:00 2021

@author: sarak
"""

"""
values
• Values are returned in the same random order as the keys are.
"""


def main():
    user = {
        'fname': 'Foo',
        'lname': 'Bar'
        }
    
    
    print(user)    #  {'fname': 'Foo', 'lname': 'Bar'}
    print(user.keys())    #  dict_keys(['fname', 'lname'])
    print(user.values())    #  dict_values(['Foo', 'Bar'])
    
if __name__ == '__main__':
    main()