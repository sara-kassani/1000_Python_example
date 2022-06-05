# exercise 73: Caesar Cipher

message = input('enter a message: ')
shift = int(input('enter a shift: '))

new_message = ""

for ch in message:
    # if the character is a lowercase letter
    if "a" <= ch <= "z":
        # first I find its position in the alphabet
        pos = ord(ch) - ord('a')
        # then I find its new position based on the shift
        # note that if left side of the modulo operator is less than right (but positive), the result is left side
        # the modulo operator also handles negative shifting
        # the modulo operator makes it possible to handle shifting which goes beyond the alphabet
        pos = (pos + shift) % 26
        new_message += chr(ord('a') + pos)

    elif "A" <= ch <= "Z":
        pos = ord(ch) - ord('A')
        pos = (pos + shift) % 26
        new_message += chr(ord('A') + pos)
    else:
        new_message += ch

print('the shifted message is %s' % new_message)


# note: how does the modulo operator work for negative integers