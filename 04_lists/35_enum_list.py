"""
Enumerate lists
"""


def main():
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']

    for idx, planet in enumerate(planets):
        print(idx, planet)

    print('')                             # create an empty line
    enu = enumerate(planet)
    print(enu.__class__.__name__)
    print(enu)


if __name__ == '__main__':
    main()

# 0 Mercury
# 1 Venus
# 2 Earth
# 3 Mars
# 4 Jupiter
# 5 Saturn

# enumerate
# <enumerate object at 0x00000144130DBA98>
