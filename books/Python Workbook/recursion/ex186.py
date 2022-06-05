# exercise 186: Run-length Encoding

def encode(data):
    # BASE CASE
    if len(data) == 0:
        return []

    # RECURSION
    index = 1
    while index < len(data) and data[index] == data[index - 1]:
        index += 1

    current = [data[0], index]

    return current + encode(data[index:])

    # index always starts at 1 and is incremented when the two conditions are met
    # when exiting the while loop, the current list is made by the first element followed by the index
    # the function call itself on a sublist which starts from the element at the specified index, until the end
    # when base case is reached, it is because the last recursion was made on an empty sublist


def main():
    mystring = 'aaaaabbccdddefgg'
    mylist = ['H', 'H', 'H', 'I', 'J', 'J', 'K']
    print(encode(mystring))
    print(encode(mylist))


if __name__ == '__main__':
    main()
