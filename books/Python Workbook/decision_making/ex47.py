# exercise 47: Season From Month and Day

month = input("enter month: ")
day = int(input("enter day: "))

month = month.lower()
season = ''

if month == "march":
    if day < 20:
        season = "winter"
    elif day <= 31:
        season = "spring"
if month == "june":
    if day < 21:
        season = "spring"
    elif day <= 30:
        season = "summer"
if month == "september":
    if day < 22:
        season = "summer"
    elif day <= 30:
        season = "fall"
if month == "december":
    if day < 21:
        season = "fall"
    elif day <= 31:
        season = "winter"
elif (month == "april" and day <= 30) or (month == "may" and day <= 31):
    season = "spring"
elif (month == "july" and day <= 31) or (month == "august" and day <= 31):
    season = "summer"
elif (month == "october" and day <= 31) or (month == "november" and day <= 30):
    season = "fall"
elif (month == "january" and day <= 31) or (month == "february" and day <= 29):
    season = "winter"
else:
    print('not valid. Check month spelling and make sure number of days is within range.')
    quit()

print('{} {} is {}'.format(month, day, season))

# a way to minimize the if statement is making them more complex
