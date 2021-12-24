# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 15:24:58 2021

@author: sarak
"""

def main():
    people = [
        {
            'name': 'Foo Bar',
            'email': 'foo@bar.com',
            },
        
        {
            'name': 'Qux Bar',
            'email': 'quex@bar.com',
            'address': 'Brog, Country',
            'children': [
                'Alpha',
                'Beta',
                ]
            
            }
        
        ]
    
    
    print(people)
    print(people[0]['name'])
    print(people[1]['children'][0])
    
                    # [{'name': 'Foo Bar', 'email': 'foo@bar.com'}, {'name': 'Qux Bar', 'email': 'quex@bar.com', 'address': 'Brog, Country', 'children': ['Alpha', 'Beta']}]
                    # Foo Bar
                    # Alpha
    
if __name__ == '__main__':
    main()