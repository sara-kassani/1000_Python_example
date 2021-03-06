"""
Exercise: Count words
"""


def main():
    celestial_objects = [
        'Moon', 'Gas', 'Asteriod', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
    ]

    names = []
    counter = []

    for name in celestial_objects:
        if name in names:
            idx = names.index(name)
            counter[idx] +=1
        else:
            names.append(name)
            counter.append(1)

    for i in range(len(names)):
        print("{:12}   {}". format(names[i], counter[i]))


if __name__ == '__main__':
    main()
