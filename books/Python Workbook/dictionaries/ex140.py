# exercise 140: Postal Codes

first_ch_letters = ['A', 'B', 'C', 'E', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'X', 'Y']

provinces = ['Newfoundland', 'Nova Scotia', 'Prince Edward Island', 'New Brunswick', 'Quebec', 'Quebec',
             'Quebec', 'Ontario', 'Ontario', 'Ontario', 'Ontario', 'Ontario', 'Manitoba', 'Saskatchewan',
             'Alberta', 'British Columbia', 'Nunavut or Northwest Territories', 'Yukon']

rural = 0

# dictionary where key are letters and values are provinces
postal_dict = dict(zip(first_ch_letters, provinces))
print(postal_dict)


def main():
    postalcode = input('enter a Canadian postal code: ')
    # checking that first letter of the postal code is among the allowed ones, if so, a province is assigned
    if postalcode[0].upper() not in first_ch_letters:
        print('error: that first character is not allowed')
        exit()
    else:
        province = postal_dict[postalcode[0].upper()]
    # checking that second characters is a number 0-9, if so, checking if it is rural or urban area
    if not postalcode[1].isnumeric():
        print('error: that second character is not allowed')
        exit()
    else:
        if int(postalcode[1]) == rural:
            area = 'a rural'
        else:
            area = 'an urban'

    print('the postal code is for %s address in %s' % (area, province))


if __name__ == '__main__':
    main()
