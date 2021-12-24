# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 02:15:09 2021

@author: sarak
"""

def main():
    people = {
        'Foo': '123',
        'Bar': '456',
        'qux': '789'
        }
    
    for name, uid in people.items():
        print("{} => {}".format(name, uid))
        
                                            # Foo => 123
                                            # Bar => 456
                                            # qux => 789
                                            
                                            
    for t in people.items():    #  returns tuples
        # print("{} => {}".format(t[0], t[1]))
        print("{} => {}".format(*t))
                
                                            # Foo => 123
                                            # Bar => 456
                                            # qux => 789
                                         
if __name__ == '__main__':
    main()