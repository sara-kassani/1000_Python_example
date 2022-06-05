# exercise 28: Body Mass Index

"""
this exercise computes the body mass index which correlates height and weight and is obtained
by dividing the weight (in kg) by the height (in mt) squared. If height is in inches (pollici)
and weight in pounds (libbre), just use the same formula multiplied by 703
"""

mt = float(input("insert height in meters: "))
kg = float(input("insert weight in kilograms: "))

inches = mt * 39.37
pounds = kg * 2.20462

BMI = kg / (mt * mt)
print("a height of %.2f meters (or %.2f inches) and a weight of %.2f kg (or %.2f lbs) lead to a BMI of %.2f" \
      % (mt, inches, kg, pounds, BMI))



