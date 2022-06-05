# exercise 158: Remove Comments

"""
note that in this exercise file to open must be specified as file_paths
"""

# read and open the input file
try:
    in_name = input('enter name of a Python file: ')
    inf = open(in_name, 'r')
except:
    print('a problem occured while opening input file')
    quit()

# read and open the output file
try:
    out_name = input('enter the output file name: ')
    outf = open(out_name, 'w')
except:
    print('a problem occured while opening output file')
    quit()

try:
    # looping each line of the file opened in read mode
    for line in inf:
        # finding the index of character # (if not present it will be -1)
        pos = line.find('#')

    # if a comment exists, it will have an index higher than -1
        # in that case the program edits the line by counting all characters until that index (excluded)
        if pos > -1:
            line = line[0 : pos]
            line = line + '\n'
        # adding the line (potentially edited) to the new file
        outf.write(line)

    inf.close()
    outf.close()

except:
    print('problem while processing the file')
