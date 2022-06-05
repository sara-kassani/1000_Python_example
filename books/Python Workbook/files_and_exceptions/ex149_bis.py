import sys
from pathlib import Path


NUM_LINES = 10

if len(sys.argv) != 2:
    print("you must provide the file name as a command line parameter")
    quit()

try:
    # open the file in reading mode
    # sys.argv[1] means that the file to read will be indicated as second parameter
    # (in command line, in addition to the .py file)
    data_folder = Path("../files")
    file_to_open = data_folder / sys.argv[1]
    inf = open(file_to_open, 'r')

    # reading the first line
    line = inf.readline()

    count = 0
    # keep reading until the 10th line
    while count < NUM_LINES and line != "":
        line = line.rstrip()
        count = count + 1
        # display the line
        print(line)
        # read the next line
        line = inf.readline()

    inf.close()

except IOError:
    print('file not found')