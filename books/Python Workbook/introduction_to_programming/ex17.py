# exercise 17: Heat Capacity
"""
the heat capacity is the amount of energy required to increase the temperature of one
gram of a material by one degree Celsius.
The total amount of energy q required to raise m grams of material by ẟT cann be computed as:
q = mCẟT
"""

# heat capacity of water: 4186 joule
C_water = 4186 #
m = float(input('enter mass of material: '))
delta_T = float(input('enter temperature change: '))
energy_j = m * C_water * delta_T

print("the amount of energy required to change by %.2f degree the temperature of %.2f ml of water\
 is %.2f joule" % (delta_T, m, energy_j))

""" part 2 of exercise: computing cost of heating a mass of water which is necessary for a cup of coffee,
assuming that electricity price is 8.9 cent / kw-h """

# using 75 g as input in m (mass of water) and 100 degree as input in delta_T
# then converting the energy result from joul to kw-h (kilowattora) because cost is in kw-h

joule_to_kwh = 2.7777e-7
energy_kwh = energy_j * joule_to_kwh

# 8.9 cent per kw-h is the price of electricity
electricity_price = 8.9
cost = electricity_price * energy_kwh

print("and this amount of energy will cost %.2f cent" % cost)

if m == float(75) and delta_T == float(100):
    print("for example, the cost of heating 75 g of water necessary for a cup of coffee is %.2f cent" % cost)


