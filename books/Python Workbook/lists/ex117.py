# exercise 117: Only the Words

def words_in_string(s):
    # splitting string based on spaces
    base_list = s.split()
    # print(base_list)

    res_list = []

    # looping each element and removing, to the left and right, all specified characters
    for el in base_list:
        el = el.strip(", .?!-;:\"()")
        # adding that edited element to the results' list, only if it is not empty
        # note: a specific element might become empty if only made of the specified characters (e.g.  !!!)
        if el:
            # in the results' list there will only be words that start and end with a letter
            # words can have the specified characters in-between, but not to the sides
            res_list.append(el.lower())

    return res_list


def main():
    string = input('enter a string: ')
    print(words_in_string(string))


if __name__ == "__main__":
    main()
