# exercise 185: Run-length Decoding

def decode(data):
    # BASE CASE
    if len(data) == 0:
        return []
    # RECURSIVE CASE
    else:
        current = list(data[0] * data[1])
        return current + decode(data[2:])

    # the output list will be a list where each letter appears as many times as the number just after it
    # the 'current' output list is made by multiplying the first element of the sublist by the second one
    # the current lists obtained through sub-lists will be added in order to return a single list
    # the recursion stops when the next sublist will be empty


def main():
    # specifying the compressed list I will use as a parameter
    # It can be changed to test the function for different parameters
    mylist = ['A', 3, 'B', 2, 'C', 6, 'D', 1, 'E', 5]
    print(decode(mylist))


if __name__ == '__main__':
    main()
