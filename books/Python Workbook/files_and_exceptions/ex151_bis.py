# exercise 151: Concatenate Multiple Files

import sys
from pathlib import Path


if len(sys.argv) < 2:
    print("you must pass at least one more argument in command line")
    quit()

data_folder = Path("../files")
# looping each of the argument passed through CLI, starting from index 1 since at index 0 is the script.py
for i in range(1, len(sys.argv)):
    print('\n')
    file_to_open = data_folder / sys.argv[i]
    try:
        # open the current file for reading
        inf = open(file_to_open, 'r')
        # display it
        for line in inf:
            print(line, end="")
        inf.close()

    except IOError:
        print("file {} indicated as {} was not found".format(i, file_to_open))
