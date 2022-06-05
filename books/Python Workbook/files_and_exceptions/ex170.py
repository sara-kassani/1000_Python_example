# exercise 170: Missing Comments

"""
program to launch through CLI from the root directory by typing command:
python -m files_and_exceptions.ex170 section/script1.py section/script2.py ... ... ...
for example:
python -m files_and_exceptions.ex170 functions/ex85.py recursion/ex173.py lists/ex110.py
the command above will launch this script and search missing comments among functions that are
inside the 3 specified scripts
"""

import sys

print('Displaying functions with missing comments:')
print()


for script in sys.argv[1:]:

    try:
        inf = open(script, 'r')

    except:
        print('ERROR -----> a problem occured: file "%s" not found' % script)
        quit()

    # every time I open a new file, line_num and previous_line will start from scratch again
    line_num = 0
    previous_line = ' '

    for line in inf:
        # counting each line number
        line_num += 1
        current_line = line
        # whenever I encounter def followed by a space it means that line begins with a function definiton
        if current_line[:4] == 'def ':
            # in that case, I have to check if the previous line begins with a #
            if not previous_line[0] == '#':
                # if not, then that function is missing a comment, and I indicate the name of function, line and file
                # to find the function name, I take a substring that ends before the :
                f_name = current_line[4:current_line.index(':')]
                print()
                print('file %s' % script)
                print('function "%s"' % f_name)
                print('line %d' % line_num)
        # whenever I finish reading a line, I assign it to previous_line before reading the following one
        previous_line = current_line

inf.close()
