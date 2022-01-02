# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 13:23:55 2022

@author: sarak
"""

"""
What are Regular Expressions (aka. Regexes)?
• An idea on how to match some pattern in some text.
• Decide if a string is part of a larger string.
• Validate the format of some value (string) (e.g. is it a decimal number?, is it a hex?)
• Find if there are repetitions in a string.
• Analyze a string and fetch parts of if given some loose description.
• Cut up a string into parts.
• Change parts of a string.

"""

def main():

    import re
    txt = 'The black cat climbed.'
    match = re.search(r'lac', txt)

    if match:
        print('Matching')
        print(match.group(0))    #  lac

    else:
        print('Did not match')
        print(match)    #  None


if __name__ == '__main__':
    main()