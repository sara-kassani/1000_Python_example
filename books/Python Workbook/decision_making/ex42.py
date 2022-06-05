# exercise 42: Note to Frequency

note = input("enter note: ")

if note[0] + '4' == "C4":
    freq_fourth = 261.63
elif note[0] + '4' == "D4":
    freq_fourth = 293.66
elif note[0] + '4' == "E4":
    freq_fourth = 329.63
elif note[0] + '4' == "F4":
    freq_fourth = 349.23
elif note[0] + '4' == "G4":
    freq_fourth = 392.00
elif note[0] + '4' == "A4":
    freq_fourth = 440.00
elif note[0] + '4' == "B4":
    freq_fourth = 493.88


if note[1] == '4':
    print(freq_fourth)
else:
    octave_n = int(note[1])
    frequency = freq_fourth / (2**(4 - octave_n))
    print(frequency)

