# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 06:57:38 2022

@author: sarak
"""

"""
Instead of returning the list of numbers (as it used to do in Python 2), now it returns a range object
that provides “the opportunity to go over
the specific series of numbers” without actually creating the list of numbers. Getting an object
instead of the whole list has a number of advantages.
One is space. In the next example we’ll see how much memory is needed for the object returned by
the range function and
how much would it take to have the corresponding list of numbers in memory. For now let’s see
how can we use it:

        • range(start, end, step)
        • range(start, end) - step defaults to 1
        • range(end) - start defaults to 0, step defaults to 1


"""
def main():
    rng = range(3, 9, 2)

    for num in rng:
        print(num)

    print(type(rng).__name__)

    print()

                    # 3
                    # 5
                    # 7
                    # range

if __name__ == '__main__':
    main()