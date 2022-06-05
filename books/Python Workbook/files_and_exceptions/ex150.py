# exercise 15: Display the Tail of a File

import os.path
import sys


NUM_LINES = 10

# exactly 2 arguments will have to be passed from CLI: file.py file.txt
if len(sys.argv) != 2:
    print("you must provide the file name as a command line parameter")
    quit()

# showing the two arguments passed from CLI
print(sys.argv)

# the last element of the path to join is the second argument passed from CLI, namely the file name
file_to_open = os.path.join("..", "files", sys.argv[1])

try:
    inf = open(file_to_open, 'r')

    count = 0
    for line in reversed(inf.readlines()):
        print(line.rstrip())
        count += 1
        if count == NUM_LINES:
            break

except IOError:
    print('file not found')