# exercise 20: Ideal Gas Law

pressure = float(input('insert pressure in pascals: '))
volume = float(input('insert volume in liters: '))
# constant in J/mol*K
R_constant = 8314
temperature_celsius = float(input('insert temperature in celsius: '))
temperature_kelvin = temperature_celsius + 273.15

n_moles = (pressure * volume) / (R_constant * temperature_kelvin)

print("the number of moles of gas in a SCUBA tank is about %.2f" % n_moles)
