# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 04:44:07 2021

@author: sarak
"""

"""
Get key
If we use the get method, we get None if the key does not exist.
** None will be interpreted as False, if checked as a boolean.
"""

def main():
    user = {
        'fname': 'Foo',
        'lname': 'Bar',
        'address': None,
        }
    print(user.get('fname'))
    print(user.get('lname'))
    print(user.get('address'))
    
    
    print(user.get('answer', 42))
    print(user.get('address', 23))
    
    print(user)
    
    
                    # Foo
                    # Bar
                    # None
                    # 42
                    # None
                    # {'fname': 'Foo', 'lname': 'Bar', 'address': None}
    
if __name__ == '__main__':
    main()