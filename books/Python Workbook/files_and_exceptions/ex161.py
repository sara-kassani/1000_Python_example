# Exercise 161: What's that Element Again?

import os.path

file_of_elements = os.path.join("../files/elements.txt")
try:
    inf = open(file_of_elements, 'r')

except:
    print('file not found')
    quit()

d_elements = dict()
d_symbols = dict()
d_protons = dict()

for line in inf:
    line = line.strip()
    # I split the line in three elements: the first one contains protons, the second one symbol and the first one name
    el_info = line.split(',')
    # creating three different dictionaries for when I will use the user input to search for elements' info
    # each dictionary has a key corresponding to one of the three information and a tuple of the other two info as value
    d_protons[el_info[0]] = (el_info[1], el_info[2])
    d_symbols[el_info[1]] = (el_info[0], el_info[2])
    d_elements[el_info[2]] = (el_info[0], el_info[1])

inf.close()

if __name__ == '__main__':
    user_input = input('enter a number of protons, a symbol ora full element name: ')
    # capitalizing the input will make me it possible to ignore case in user input
    user_input = user_input.capitalize()

    # before entering the loop, these information will be still empty
    element = None
    protons = None
    symbol = None

    while user_input != '':
        # I check which dictionary contains the user input as a key
        # Then I assign the three info to three variables for later printing
        if user_input in d_protons:
            protons = user_input
            symbol = d_protons[protons][0]
            element = d_protons[protons][1]
        elif user_input in d_symbols:
            symbol = user_input
            protons = d_symbols[symbol][0]
            element = d_symbols[symbol][1]
        elif user_input in d_elements:
            element = user_input
            protons = d_elements[element][0]
            symbol = d_elements[element][1]
        # if the input is not present in any dictionary, then the input is not valid
        else:
            print('the input is not valid. Enter a valid number of protons, element or symbol.')

        # if the three variables were filled with a value in the loop, it means I can print them because I found info
        if element and protons and symbol:
            print("element: %s"%element)
            print("symbol: %s"%symbol)
            print("protons: %s"%protons)

        # at the end of each loop I will always have to empty the three variables
        # I do that because otherwise, in case of a later invalid input, the three variables might still store a value
        element = None
        protons = None
        symbol = None

        # at the end of the loop, I ask again to type an input and capitalize it
        user_input = input('enter a number of protons, a symbol ora full element name: ')
        user_input = user_input.capitalize()