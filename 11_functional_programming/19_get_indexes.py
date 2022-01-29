# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:14:36 2022

@author: sarak
"""

"""
Get indexes of values
filter can help us get a sublist of values from an iterable, eg. from a list that match some condition.
In this example we see how to get all the names that are exactly 3 characters long.

What if, however if instead of the values themselves, you would like to know their location? 
The indexes of the places where these value can be found. 

In that case, you would run the filter on the indexes from 0 till the last valid index of the list. 

You can do that using the range function.
Finally there is another example that shows how to get the indexes of all the names that have an “e”
in them.
Just to show you that we can use any arbitray condition there.
"""

def main():
    names = ["Helen", "Ann", "Mary", "Harry", "Joe", "Peter"]
    names3 = filter(lambda w: len(w) == 3, names)
    
    print(list(names3))
            # ['Ann', 'Joe']


    loc3 = filter(lambda i: len(names[i]) ==3 , range(len(names)))
    print(list(loc3))
            # [1, 4]
            
    has_e = filter(lambda i: "e" in names[i], range(len(names)))
    print(list(has_e))
            # [0, 4, 5]

if __name__ == '__main__':
    main()