# exercise 93: Center a String in the Terminal Window

def center_it(s, w):
    len_of_str = len(s)
    if len_of_str > w:
        res = 'not enough space for that string'
        return res
    elif len_of_str == w:
        return s

    # computing space to the left that is necessary to center the string based on the width of the terminal
    spaces = (w - len_of_str) // 2
    # result is the number of spaces that are necessary to center, plus the string itself
    res = ' ' * spaces + s
    return res


def main(s, w):
    print(center_it(s, w))


if __name__ == '__main__':
    main('A Famous Story', 80)
    main('By', 80)
    main('Tarantino', 80)
    main('...', 80)
    main('Take a seat', 80)

# note: in this program, if the remaining space is odd, I approximate towards left the beginning of string


# alternative code, longer (it is not necessary to add spaces to both left and right)
""" 
    tot_spaces = w - len_of_str
    side_spaces = tot_spaces // 2
    res = ' '*(side_spaces) + s + ' '*(side_spaces)
    return res
"""
