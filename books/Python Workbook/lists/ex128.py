# exercise 128: Count the Elements

# function counts how many elements of a list are within a min-max range
def countRange(data, minval, maxval):
    counter = 0
    for el in data:
        if minval <= el < maxval:
            counter += 1
    return counter


def main():
    mydata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print('counting the elements in [1...10] that are between 5 and 7')
    print('Result: %d, Expected: 2' % countRange(mydata, 5, 7))

    print('counting the elements in [1...10] that are between 0 and 10')
    print('Result: %d, Expected: 10' % countRange(mydata, 0, 100))

    # testing with different data parameters
    print('counting the elements in [] that are between 0 and 10')
    print('Result: %d, Expected: 0' % countRange([], 0, 1000))


if __name__ == '__main__':
    main()
