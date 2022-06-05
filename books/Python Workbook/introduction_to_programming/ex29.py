# exercise 29: Wind Chill

T_celsius = float(input('enter temperature in degree Celsius: '))
wind_speed = float(input('enter wind speed km/h: '))

# the wind chill index
wci = 13.12 + 0.6125 * T_celsius - 11.37 * (wind_speed**0.16) + 0.3965 * T_celsius * (wind_speed**0.16)

print("the wind chill index is {}".format(round(wci)))
