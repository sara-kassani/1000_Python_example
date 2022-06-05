# exercise 169: Redacting Text in a File

"""
- the program performs a case insensitive redaction
- if 'the' is among the sensitive words, the word 'The' will be redacted
- however the redacted text will be all lowercase due to originary text getting converted to lowercase pre-manipulation
- the program will create a new file with a name specified by the user
"""

from pathlib import Path


def redactFile(myfile, sensitiveFile, redactedFile):
    sensitive_words = []
    sens_f = open(sensitiveFile, 'r')
    for line in sens_f:
        for word in line.split():
            sensitive_words.append(word)
    # I have just created a list of sensitive words based on a sensitive words file.txt

    inf = open(myfile, 'r')
    # I convert my file.txt in a whole string by joining all the lines of the list created through readlines()
    file_as_string = ''.join(inf.readlines()).lower()
    # at this point I have the whole text as a string
    # I have to replace all the words in the list that occurr in the string, with asterisks

    for word in sensitive_words:
        # for each word, I update the string, replacing that word with as many * as the number of characters to redact
        file_as_string = file_as_string.replace(word, '*' * len(word))

    # when I have my final redacted string, I will add the whole string in a new file.txt that I create (or overwrite)
    outf = open(redactedFile, 'w')
    outf.write(file_as_string)

    inf.close()
    sens_f.close()
    outf.close()

    return outf


def main():
    data_folder = Path("../files")
    original_text_file = input('enter file to read: ')
    sensitive_words_file = input('enter a file with sensitive words: ')
    redacted_file = input('enter the name of the redacted output file: ')
    redactFile(data_folder / original_text_file, data_folder / sensitive_words_file, data_folder / redacted_file)


if __name__ == '__main__':
    main()