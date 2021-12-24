# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 01:26:14 2021

@author: sarak
"""

def main():
    people = [
        {
            'name': 'Foo',
            'id': '1',            
            },
        
        {
            'name': 'Bar',
            'id': '2'
            },
        {
            'name': 'Moo',
            'id': '3'
            },
        ]
    
    by_name = {}
    by_id ={}
    
    for p in people:
        by_name[p['name']] = p
        by_id[p['id']] = p
        
        
    print(by_name)
    print(by_id)
    
            # {'Foo': {'name': 'Foo', 'id': '1'}, 'Bar': {'name': 'Bar', 'id': '2'}, 'Moo': {'name': 'Moo', 'id': '3'}}
            # {'1': {'name': 'Foo', 'id': '1'}, '2': {'name': 'Bar', 'id': '2'}, '3': {'name': 'Moo', 'id': '3'}}
    
    print(by_id['1'])    #  {'name': 'Foo', 'id': '1'}
    print(by_name['Foo'])    #  {'name': 'Foo', 'id': '1'}
    
    
    by_name['Foo']['email'] = 'foo@mail.com'
    print(by_name['Foo'])    #  {'name': 'Foo', 'id': '1', 'email': 'foo@mail.com'}
    
    
if __name__ == '__main__':
    main()