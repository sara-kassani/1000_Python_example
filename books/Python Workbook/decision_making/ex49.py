# exercise 49: Chinese Zodiac

year = int(input('enter year: '))

if year % 12 == 0:
    animal = 'Monkey'
elif year % 12 == 1:
    animal = 'Rooster'
elif year % 12 == 2:
    animal = 'Dog'
elif year % 12 == 3:
    animal = 'Pig'
elif year % 12 == 4:
    animal = 'Rat'
elif year % 12 == 5:
    animal = 'Ox'
elif year % 12 == 6:
    animal = 'Tiger'
elif year % 12 == 7:
    animal = 'Hare'
elif year % 12 == 8:
    animal = 'Dragon'
elif year % 12 == 9:
    animal = 'Snake'
elif year % 12 == 10:
    animal = 'Horse'
elif year % 12 == 11:
    animal = 'Sheep'

if year > 2020:
    print('%d will be the year of the %s' % (year, animal))
else:
    print('%d was the year of the %s' % (year, animal))


"""details:
the program divides the entered year by 12 and, based on the remainder, it says which animal
it corresponds to. 
The cycle is 12, thus year is always divided by 12. 
I start from the year that can be divided by 12, namely 2004 (2004 % 12 == 0), that corresponds to Monkey.
Then based on each additional remainder, the program stores the corresponding animal, until getting 
to the year when the remainder will be zero again (e.g. 2004, it will be 2004 + 12 = 2016), and so on.
"""