# exercise 151: Concatenate Multiple Files

# the program prints the files passed through CLI but without printing their actual content

import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("you must pass at least one more argument in command line")
    quit()

# I set a path as a data folder
data_folder = Path("../files")

# for each argument passed through CLI, I add the argument to the path and try to open it
for el in sys.argv:
    file_to_open = data_folder / el
    try:
        inf = open(file_to_open, 'r')
        print(inf)
    except IOError:
        print('not existing file')
