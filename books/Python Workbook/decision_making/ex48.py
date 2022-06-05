# exercise 48: Birth Date to Astrological Sign

month = input('enter a month: ').lower()
day = int(input('enter a day: '))

if month == 'january':
    if day <= 19:
        sign = 'capricorn'
    else:
        sign = 'aquarius'
elif month == 'february':
    if day <= 18:
        sign = 'aquarius'
    else:
        sign = 'pisces'
elif month == 'march':
    if day <= 20:
        sign = 'pisces'
    else:
        sign = 'aries'
elif month == 'april':
    if day <= 19:
        sign = 'aries'
    else:
        sign = 'taurus'
elif month == 'may':
    if day <= 20:
        sign = 'taurus'
    else:
        sign = 'gemini'
elif month == 'june':
    if day <= 20:
        sign = 'gemini'
    else:
        sign = 'cancer'
elif month == 'july':
    if day <= 22:
        sign = 'cancer'
    else:
        sign = 'leo'
elif month == 'august':
    if day <= 22:
        sign = 'leo'
    else:
        sign = 'virgo'
elif month == 'september':
    if day <= 23:
        sign = 'virgo'
    else:
        sign = 'libra'
elif month == 'october':
    if day <= 22:
        sign = 'libra'
    else:
        sign = 'scorpio'
elif month == 'november':
    if day <= 21:
        sign = 'scorpio'
    else:
        sign = 'sagittarius'
elif month == 'december':
    if day <= 21:
        sign = 'sagittarius'
    else:
        sign = 'capricorn'
else:
    print('error: check month spelling')
    exit()

print('zodiacal sign: {}'.format(sign))


