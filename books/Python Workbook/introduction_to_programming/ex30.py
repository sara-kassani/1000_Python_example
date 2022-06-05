# exercise 30: Celsius to Fahreneit and Kelvin

T_celsius = float(input("enter temperature in degree celsius: "))

T_fahreneit = T_celsius * (9/5) + 32
T_kelvin = T_celsius + 273.15

print("%.2f degree celsius equal %.2f degree fahreneit and %.2f degree kelvin" % (T_celsius, T_fahreneit, T_kelvin))
