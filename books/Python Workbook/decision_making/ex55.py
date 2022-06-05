# exercise 55: Wavelengths of Visible Light

wavelength = float(input("enter wavelength in nanometers: "))

if wavelength < 380 or wavelength > 750:
    color = ""
elif wavelength >= 620:
    color = "red"
elif wavelength >= 590:
    color = "orange"
elif wavelength >= 570:
    color = "yellow"
elif wavelength >= 495:
    color = "green"
elif wavelength >= 450:
    color = "blue"
elif wavelength >= 380:
    color = "violet"

if color:
    print(color)
else:
    print('invalid wavelength')
