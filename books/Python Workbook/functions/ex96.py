# exercise 96: Does a String Represent an Integer?

"""info
ord('0') = 48
ord('9') = 57
"""


def isInteger(s):
    s = s.strip()
    first = s[0]
    # if string only has one element, that element will have to be a number between 0 and 9
    if len(s) == 1 and (ord(first) < 48 or ord(first) > 57):
        return False
    # when string has more elements, the first element may be even a + or -
    # note: if I moved to the left the conditions that are to the right of 'and', it would not work properly
    if first != '+' and first != '-' and (ord(first) < 48 or ord(first) > 57):
        return False

    for i in range(1, len(s)):
        # making it possible to have a space after + or - before the actual integer
        if i == 1 and (s[0] == '+' or s[0] == '-') and s[1] == ' ':
            i += 1
        if ord(s[i]) < 48 or ord(s[i]) > 57:
            return False
    return True


def main():
    s = input('enter string: ')
    if isInteger(s):
        print("it's an integer")
    else:
        print("Not an integer")


if __name__ == "__main__":
    main()

# alternatively I can use isdigit() in the first if to make it shorter, without using ord()

""" explanation
first thing is ignoring spaces.
In the first if, I use initially the or operator because I have to exclude
two alternative cases, namely when the character code is < 48 and when is > 57, they are two
alternative cases because if I used the and operator, the code below wouldn't be ever executed
because there is no character with code both <48 and >57.
After analyzing first character and understanding it is a number (by exclusion), I loop the
remaining character staarting from index 1 (second) and return False at the first not-number case,
namely also when encountering + or - because they cannot be found in-between a number.
If none of the False cases applies, then I return True: the string is a number
"""

""" detail about first condition
if I put or in the place of the second and, it would not work 
"""
