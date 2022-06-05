# exercise 31: Units of Pressure

pressure_KPa = float(input('enter pressure in kilopascals: '))

KPa_to_psi = 0.145038
KPa_to_Torr = 7.50062
KPa_to_atm = 0.00986923

pressure_psi = pressure_KPa * KPa_to_psi
pressure_Torr = pressure_KPa * KPa_to_Torr
pressure_atm = pressure_KPa * KPa_to_atm

print('a pressure of %.4f kilopascals equals a pressure of %.4f pounds per square inch, %.4f millimeters\
 of mercury and %.4f atmospheres' % (pressure_KPa, pressure_psi, pressure_Torr, pressure_atm))

