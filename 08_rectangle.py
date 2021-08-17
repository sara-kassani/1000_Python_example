'''
Write a script that will ask for the sides of a rectangle and print out the area.
Provide error messsages if either of the sides is negative.
'''

def main():
    length = input('Length: ')
    width = input('Width: ')

    if float(length) <= 0:
        print('Error: Length can\'t be zero or negative.')
        return

    if float(width) <= 0:
        print('Error: Width can\'t be zero or negative.')
        return

    area = float(length) * float(width)
    print('The area is ',area)

if __name__ == '__main__':
    main()


