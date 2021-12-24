# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 01:57:45 2021

@author: sarak
"""

def main():
    number = {
        23 : "Twenty three",
        17: "Seventeen",
        3.14 : "Three dot fourteen",
        42 : "The answer",
        }
    
    print(number)
    print(number[42])
    print(number[3.14])
    
        # {23: 'Twenty three', 17: 'Seventeen', 3.14: 'Three dot fourteen', 42: 'The answer'}
        # The answer
        # Three dot fourteen
    
if __name__ == '__main__':
    main()