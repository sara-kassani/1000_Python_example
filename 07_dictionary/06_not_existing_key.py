# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 04:28:26 2021

@author: sarak
"""

"""
Not existing key
If we try to fetch the value of a key that does not exist, we get an exception.
"""

def main():
    user = {
        'fname': 'Foo',
        'lname': 'Bar',
        }
    
    print(user['email'])
    
                # print(user['email'])
                # Traceback (most recent call last):
                
                #   File "C:\Users\sarak\AppData\Local\Temp/ipykernel_2664/2040631594.py", line 1, in <module>
                #     print(user['email'])
                
                # NameError: name 'user' is not defined   
    
if __name__ == '__main__':
    main()