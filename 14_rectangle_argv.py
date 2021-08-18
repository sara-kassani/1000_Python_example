# Area of rectangle (argv)
import sys

def main():
    if len(sys.argv) != 3:
        exit('Error: Needs 2 argumentd: width length')

    width = int(sys.argv[1])
    length = int(sys.argv[2])

    if length <= 0:
        exit('length is not positive')

    if width <= 0:
        exit('width is not positive')

    area = length * width
    print(area)

if __name__ == '__main__':
    main()