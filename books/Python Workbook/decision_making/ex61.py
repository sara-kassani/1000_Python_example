# exercise 61: Is a License Plate Valid?

# older style AAA 000
# new style 0000 AAA

plate = input('enter license plate: ')
# error checking
# if I have less than 6 elements or more than 7, it is not a valid plate
if len(plate) < 6 or len(plate) > 7:
    print('please enter a valid license plate')
    exit()

# function ord allows to convert the letter/number into a numeric code
# e.g. A = 65 and Z = 90 then 0 = 48 and 9 = 57
first = ord(plate[0])
second = ord(plate[1])
third = ord(plate[2])
fourth = ord(plate[3])
fifth = ord(plate[4])
sixth = ord(plate[5])

license = ''

# if the string is 6 elements, then it can only be an old style license
if len(plate) == 6:
    if 65 <= first <= 90 and 65 <= second <= 90 and 65 <= third <= 90:
        if 48 <= fourth <= 57 and 48 <= fifth <= 57 and 48 <= sixth <= 57:
            license_type = 'an old style'

# if the string is 7 elements, it can only be a new style license
elif len(plate) == 7:
    # adding the seventh element as numeric code for that letter/number
    seventh = ord(plate[6])
    if 48 <= first <= 57 and 48 <= second <= 57 and 48 <= third <= 57 and 48 <= fourth <= 57:
        if 65 <= fifth <= 90 and 65 <= sixth <= 90 and 65 <= seventh <= 90:
            license_type = 'a new style'

if license:
    print("{} is valid for {}".format(plate, license_type))
else:
    print("license plate is not valid.")
