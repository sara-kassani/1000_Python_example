# exercise 56: Frequency to Name

frequency = float(input('enter frequency of radiation: '))

if frequency >= 3 * 10**19:
    name = 'gamma rays'
elif frequency >= 3 * 10**17:
    name = 'X-rays'
elif frequency >= 7.5 * 10**14:
    name = 'Ultraviolet light'
elif frequency >= 4.3 * 10**14:
    name = 'Visible light'
elif frequency >= 3 * 10**12:
    name = 'Infrared light'
elif frequency >= 3 * 10**9:
    name = 'microwaves'
else:
    name = 'radio waves'

print('that frequency corresponds to %s' % name)
