# exercise 176: The NATO Phonetic Alphabet

def phonetic_spelling(s):
    """
    :param s: a word or a sentence (string)
    :return: a string which represents a series of words that do the spelling for the passed string
    """
    spelling = ''

    d = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',\
         'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet',\
         'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',\
         'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',\
         'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee',\
         'Z': 'Zulu'}

    # BASE CASE
    # when the passed string has become empty, the spelling is done
    if s == '':
        return ''

    # RECURSIVE CASE
    # at each recursion, the program checks if the element is inside the dictionary
    # if so, the spelling variable gets new content
    element = s[0].upper()
    if element in d:
        spelling += d[element] + ' '

    # each recursion takes the previous spelling content and invoke the function again from the following element
    return spelling + phonetic_spelling(s[1:])


def main():
    word = input('enter a word to spell: ')
    print(phonetic_spelling(word))


if __name__ == '__main__':
    main()