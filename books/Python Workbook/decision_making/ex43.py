# exercise 43: Frequency to Note

freq = float(input('please enter a frequency in Hz: '))

if abs(freq - 261.63) <= 1:
    note = 'C4'
elif abs(freq - 293.66) <= 1:
    note = 'D4'
elif abs(freq - 329.63) <= 1:
    note = 'E4'
elif abs(freq - 349.23) <= 1:
    note = 'F4'
elif abs(freq - 392) <= 1:
    note = 'G4'
elif abs(freq - 440) <= 1:
    note = 'A4'
elif abs(freq - 493.88) <= 1:
    note = 'B4'
else:
    note = None

# here I use a conditional expression
print(note) if note else print('that frequency does not correspond to any notes')

