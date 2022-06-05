# exercise 37: Vowel or Consonant

letter = input("enter a letter of the alphabet: ")

letter = letter.lower()

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("{} is a vowel".format(letter))
elif letter == "y":
    print("{} is sometimes a vowel and sometimes a consonant".format(letter))
else:
    print("{} is a consonant".format(letter))
