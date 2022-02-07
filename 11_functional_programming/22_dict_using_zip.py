# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:15:18 2022

@author: sarak
"""

def main():
    names = ['Jan', 'Feb', 'Mar', 'Apr']
    days = [31, 28, 31, 30]
    
    pairs = zip(names, days)
    print(list(pairs))
    # [('Jan', 31), ('Feb', 28), ('Mar', 31), ('Apr', 30)]
    
    month = dict(zip(names, days))
    print(month)
    # {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30}
    
    months = dict(pairs)
    print(months)
    # {}
    
if __name__ == '__main__':
    main()