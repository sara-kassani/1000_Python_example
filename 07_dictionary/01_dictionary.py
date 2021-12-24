# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 05:41:01 2021

@author: sarak
"""

"""
What is a dictionary
• Unordered key-value pairs.
• Keys are immutables (numbers, strings, tuples).
• Values can be any object.
When to use dictionaries
• ID to Name mapping.
• Object to Count mapping.
• Name of a feature to value of the feature.
• Name of an attribute to value of the attribute.
Dictionary
"""

def main():
    user = {}
    user['name'] = 'foobar'
    user['email'] = 'foo@bar.com'
    
    print(user)    #  {'name': 'foobar', 'email': 'foo@bar.com'}
    
    the_name = user['name']
    print(the_name)
    
    
if __name__ == "__main__":
    main()
