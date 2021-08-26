"""
Sort
"""

def main():
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
    print(planets)                  # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']

    planets.sort()
    print(planets)                  # ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Saturn', 'Venus']

    planets.sort(reverse= True)
    print(planets)                  # ['Venus', 'Saturn', 'Mercury', 'Mars', 'Jupiter', 'Earth']


if __name__ == '__main__':
    main()