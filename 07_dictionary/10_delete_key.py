# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:13:54 2021

@author: sarak
"""

def main():
    user = {
        'fname': 'Foo',
        'lname': 'Bar',
        'email': 'foo@bar.com',
        }
    
    print(user)    #  {'fname': 'Foo', 'lname': 'Bar', 'email': 'foo@bar.com'}
    
    fname = user['fname']
    print(fname)    #  Foo
    
    del user['fname']
    print(user)    #  {'lname': 'Bar', 'email': 'foo@bar.com'}
    
    lname_was = user.pop('lname')
    print(lname_was)    #  Bar
    print(user)    #  {'email': 'foo@bar.com'}
    
if __name__ == '__main__':
    main()