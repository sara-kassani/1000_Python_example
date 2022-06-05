# exercise 128: Count the Elements

import random


def countRange(li, minval, maxval):
    counter = 0
    for el in li:
        if minval <= el <= maxval:
            counter += 1
    return counter


def main():
    t = []
    for i in range(100):
        t.append(random.randrange(1,100))

    # I can change the two integers to test the function
    print(countRange(t, 45, 55))


if __name__ == '__main__':
    main()

"""
the main() program populates an empty list with 100 random values between 1 and 100.
Once the list is created, the function that returns how many numbers in the list are
included within a min and a max range gets invoked
"""
