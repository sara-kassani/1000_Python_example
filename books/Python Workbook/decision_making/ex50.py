# exercise 50: Richter Scale

magnitude = float(input("enter magnitude: "))

if magnitude >= 10:
    level = "meteoric"
elif magnitude >= 8:
    level = "great"
elif magnitude >= 7:
    level = "major"
elif magnitude >= 6:
    level = "strong"
elif magnitude >= 5:
    level = "moderate"
elif magnitude >= 4:
    level = "light"
elif magnitude >= 3:
    level = "minor"
elif magnitude >= 2:
    level = "very minor"
else:
    level = "micro"

print("an earthquake with magnitude {} is a {} one".format(magnitude, level))
