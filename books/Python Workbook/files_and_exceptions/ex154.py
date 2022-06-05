# exercise 154: Letter Frequencies

import sys
from pathlib import Path


lower_limit = 97
upper_limit = 122

if len(sys.argv) != 2:
    print("you must provide the file name as a command line parameter")
    quit()

data_folder = Path("../files")
file_to_open = data_folder / sys.argv[1]
try:
    # opening a file passed through CLI and creating a dictionary with frequencies for each letter of the file
    inf = open(file_to_open, 'r')
    d = dict()
    for line in inf:
        for ch in line:
            if 97 <= ord(ch.lower()) <= 122:
                if ch.lower() not in d:
                    d[ch.lower()] = 1
                else:
                    d[ch.lower()] += 1
    print(d)

    # creating a reversed dictionary, where keys are frequencies and values are letters
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)

    # what is left is sorting the dictionary based on frequency, that now I have as a valueù
    # and printing letters based on that
    for key in reversed(sorted(inverse)):
        print(inverse[key], '>', key)

    inf.close()

except IOError:
    print('file not found')


