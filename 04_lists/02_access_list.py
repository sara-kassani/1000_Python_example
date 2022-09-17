"""
- Access single elements
- Access a sublist: [start:end]
- Creates a copy of that sublist
"""
def main():

    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
    print(planets)

    print(planets[0])     # Mercury
    print(type(planets[0]))    # <class 'str'>

    print(planets[0:1])    # Mercury
    print(type(planets[0:1]))    # <class 'list'>
    
    
    
    print(planets[0:2])
    print(planets[1:3])

    print(planets[2:])
    print(planets[:3])

    print(planets[:])


if __name__ == '__main__':
    main()
