# exercise 45: Date to Holiday Name

month = input("enter month: ")
day = input("enter day: ")

if month.lower() == "january" or month.lower() == "jan" or month == "1" or month == "01":
    if day == "1" or day == "01":
        holiday = "New year's day"
elif month.lower() == "july" or month.lower() == "jul" or month == "7" or month == "07":
    if day == "1" or day == "01":
        holiday = "Canada day"
elif month.lower() == "december" or month.lower() == "dec" or month == "12":
    if day == "25":
        holiday = "Christmas day"
else:
    holiday = "the entered date doesn't correspond to any holiday"

print(holiday)
