# exercise 44: Faces on Money

banknote = int(input("enter a $ banknote amount: "))

if banknote == 1:
    image = "George Washington"
elif banknote == 2:
    image = "Thomas Jefferson"
elif banknote == 5:
    image = "Abraham Lincoln"
elif banknote == 10:
    image = "Alexander Hamilton"
elif banknote == 20:
    image = "Andrew Jackson"
elif banknote == 50:
    image = "Ulysses S. Grant"
elif banknote == 100:
    image = "Benjamin Franklin"
else:
    print('that banknote does not exist')
    quit()

print(image)
