# exercise 39: Month Name to Number of Days

month = input("enter a month in lowercase: ")
month = month.lower()
num_of_days = ""

if month == "november" or month == "april"\
    or month == "june" or month == "september":
    num_of_days = 30
elif month == "february":
    # in this case I will have a string, not an integer
    num_of_days = "28 or 29"
elif month == "january" or month == "march" or month == "may" or month == "july" or month == "august"\
        or month == 'october' or month == 'december':
    num_of_days = 31
else:
    print('month is not valid. Please spell it correctly.')
    exit()

print("month: {}".format(month.capitalize()))
print("number of days: {}".format(num_of_days))


