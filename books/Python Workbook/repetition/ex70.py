# exercise 40: Parity Bits

line = input('enter 8 bits: ')

while line != '':
    if line.count('0') + line.count('1') != 8 or len(line) != 8:
        print('that wasn\'t 8 bits. Try again.')
    else:
        ones = line.count('1')

        if ones % 2 == 0:
            print('the parity bit should be 0')
        else:
            print('the parity bit should be 1')

    line = input('enter 8 bits: ')


""" explanation
parity bit is the number between 0 and 1 that added to the amount of 1 that are present in the
previous group of 8 bits, results in an even number (even parity case as this exercise) or in an
odd number (odd parity).
Thus, 8 bits have to be entered in the input, all of them have to be either 0 or 1, then among these
8 bits only the 1 are added and the resulting value gets checked. Then a value is chosen, namely the 
value that added to the previous value, makes the resulting value either even (even parity) or odd (odd parity). 
"""
