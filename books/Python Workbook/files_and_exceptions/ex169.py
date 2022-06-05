# exercise 169: Redacting Text in a File

"""
- the program does not perform any error checking
- the program performs a case insensitive redaction: if 'the' is among the sensitive words, the words
    'THE', 'THe', 'The', 'tHE' and 'thE' will all be redacted
- to perform such a case insensitive redaction, regex is used
- in the sensitive file, each line must contain only one sensitive word
- if all files are opened correctly, the program creates a new redacted file with a name specified by the user
"""

import re
from pathlib import Path

data_folder = Path("../files")
inf_name = input('enter the name of the file to redact: ')
inf = open(data_folder / inf_name, 'r')

sen_name = input('enter the name of the file with sensitive words inside it: ')
sen = open(data_folder / sen_name, 'r')

# all sensitive words will go into a list called words
words = []
line = sen.readline()
while line != "":
    line = line.rstrip()
    words.append(line)

    line = sen.readline()

sen.close()

# opening/creating redacted file
outf_name = input('enter the name of the new redacted file: ')
outf = open(data_folder / outf_name, 'w')

# reading each line of the input file and replacing the sensitive words occurrences with asterisks
line = inf.readline()
while line != '':
    # each time a new line is read, the line gets redacted for all words, before reading the next line
    for word in words:
        # the current word case gets ignored
        src_str = re.compile(word, re.IGNORECASE)
        # if current line contains case insensitive occurrences of current word, it will be updated with more redactions
        redacted_line = src_str.sub('*' * len(word), line)
        # I must update the line according to redactions during the words loop
        line = redacted_line

    # after all words get checked against the current line, the redacted line gets pushed to the redacted file
    outf.write(redacted_line)
    # before starting a new words loop, a new line gets read
    line = inf.readline()

inf.close()
outf.close()


# ---- add possibility to use a sensitive file with all words on the same line
