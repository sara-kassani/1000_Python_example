# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:15:10 2022

@author: sarak
"""

def main():
    import sys 
    
    text = ['aaaa', 'bb', 'ccc ccc']
    length_1 = map(lambda x: len(x), text)
    print(list(length_1))           # [4, 2, 7]
    
    length_2 = map(len, text)
    print(list(length_2))           # [4, 2, 7]
    
    length_3 = [len(s) for s in text]
    print(length_3)           # [4, 2, 7]
    
    
    print()
    print(sys.getsizeof(length_1))  # 48
    print(sys.getsizeof(length_2))  # 48
    print(sys.getsizeof(length_3))  # 88
    
    
if __name__ == '__main__':
    main()