# exercise 69: Admission Price

standard_fee = 23
over_fee = 18
under_fee = 14
group_charge = 0

while True:
    age = input('age of the guest: ')
    if age == '':
        print("total charge for the group is $ %d" % group_charge)
        break
    else:
        age = int(age)
        if age <= 2:
            print('free ticket')
        elif 3 <= age <= 12:
            group_charge += under_fee
            print('$ %d' % under_fee)
        elif age >= 65:
            group_charge += over_fee
            print('$ %d' % over_fee)
        else:
            group_charge += standard_fee
            print('$ %d' % standard_fee)
