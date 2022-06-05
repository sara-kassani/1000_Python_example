# exercise 139: Morse Code

# creating list with all letters A-Z and numbers 0-0 (using two loops)
lett_and_num = []

for i in range(65, 91):
    lett_and_num.append(chr(i))

for i in range(10):
    lett_and_num.append(i)

# creating ist of morse codes that I will associate, in order, to the list of letters-numbers
codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.',
         '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----',
         '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

# starting from two lists (letter-numbers, morse codes) a dictionary is created
# using zip() I am able to associate elements within two lists following the same order
morse_dict = dict(zip(lett_and_num, codes))
print(morse_dict)


def main():
    message = input('enter a message: ')
    # empty list where I will push each letter of the message which is converted in morse code
    morse_el = []
    # for each character of the message, if present (uppercase) in the dictionary as key, I push its value in the list
    for c in message:
        if c.upper() in morse_dict:
            morse_el.append(morse_dict[c.upper()])
    # gathering all elements of the list in a unique string separating them with a space
    message_in_morse = ' '.join(morse_el)
    print(message_in_morse)


if __name__ == '__main__':
    main()