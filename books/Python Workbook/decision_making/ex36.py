# exercise 36: Dog Years

human_age = int(input("enter a human age: "))

if human_age == 1:
    dog_age = 10.5
if human_age == 2:
    dog_age = 21
# from third human year, each year corresponds to four dog years
if human_age >= 3:
    dog_age = 21 + (human_age - 2) * 4
else:
    print("please enter a valid age")
    exit()


print("a human age of {} equals a dog age of {}".format(human_age, dog_age))


