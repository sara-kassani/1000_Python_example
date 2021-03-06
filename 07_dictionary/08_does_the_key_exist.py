# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:10:08 2021

@author: sarak
"""

def main():
    user = {
        'fname': 'Foo',
        'lname': 'Bar',
        }
    
    print('fname' in user)    #  True
    print('email' in user)    #  False
    print('Foo' in user)    # False
    
    
    for k in ['fname', 'email', 'lname']:
        if k in user:
            print("{} => {}".format(k, user[k]))
                            
                            # fname => Foo
                            # lname => Bar
    
if __name__ == '__main__':
    main()