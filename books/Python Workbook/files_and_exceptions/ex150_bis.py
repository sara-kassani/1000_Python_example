# exercise 15: Display the Tail of a File

import sys
import os.path


if len(sys.argv) != 2:
    print("you must provide the file name as a command line parameter")
    quit()

file_to_open = os.path.join("..", "files", sys.argv[1])
try:
    inf = open(file_to_open, 'r')
    # creating a list where I will put every line of the file
    line_list = []
    # start reading the first line
    line = inf.readline()
    # keep reading lines until they end
    # before reading a new line, push the previous in the list
    while line != "":
        line_list.append(line)
        line = inf.readline()
    # once the list of lines is ready, I have to print 10 of them starting from the end
    # i will use an index from the last element
    j = len(line_list)-1
    # printing 10 times the element of the list and their index, decreasing it at each iteration
    for i in range(10):
        print(line_list[j])
        j -= 1

except IOError:
    print('file not found')