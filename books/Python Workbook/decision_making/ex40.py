# exercise 40: Sound Levels

sound = int(input("enter sound level in decibel: "))

if sound < 40:
    print("below quiet room")
elif sound == 40:
    print("quiet room")
elif 40 < sound < 70:
    print("between quiet room and alarm clock")
elif sound == 70:
    print("alarm clock")
elif 70 < sound < 106:
    print("between alarm clock and gas lawnmower")
elif sound == 106:
    print("gas lawnmower")
elif 106 < sound < 130:
    print("between gas lawnmower and jackhammer")
elif sound == 130:
    print("jackhammer")
else:
    print("above jackhammer")
