# exercise 73: Caesar Cipher

""" info:
the program converts in lowercase caesar cipher string
codes:
A = 65 e Z = 90 poi 0 = 48 e 9 = 57
a = 97 e z = 122
"""

message = input('enter message: ')
message = message.lower()
shift = int(input('enter shift amount: '))

if shift > 26 or shift < -26:
    print('enter a shift between -26 and 26')
    exit()

res = ''

# case of positive shift
if shift > 0:
    for c_of_message in message:
        if 97 <= ord(c_of_message) <= 122:  # case of lowercase letters
            if ord(c_of_message) + shift > 122:  # case of going beyond letter z
                # subtracting 26 and start counting the shift again from letter a
                res += chr(ord(c_of_message) - 26 + shift)
            else:
                res += chr(ord(c_of_message) + shift)  # if not beyond z, add the shift directly
        else:
            res += c_of_message

# case of negative shift
if shift < 0:
    for c_of_message in message:
        if 97 <= ord(c_of_message) <= 122:  # case of lowercase letters
            if ord(c_of_message) + shift < 97:  # in this case when subtracting I go beyond letter a
                # subtracting 26 and start counting the shift again from letter a
                res += chr(ord(c_of_message) + 26 + shift)
            else:

                res += chr(ord(c_of_message) + shift)  # if not beyond a, subtract the shift directly
        else:
            res += c_of_message

print(res)
