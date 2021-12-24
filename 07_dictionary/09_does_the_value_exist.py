# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:08:53 2021

@author: sarak
"""

def main():
    user = {
        'fname': 'Foo',
        'lname': 'Bar',
        }
    
    print('fname' in user.values())    #  False
    print('Foo' in user.values())    #  True
    
if __name__ == '__main__':
    main()