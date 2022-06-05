# exercise 157: Both Letter Grades and Grade Points

from decision_making.ex52_bis import lett_to_point
from decision_making.ex53_bis import point_to_lett


def grade_converter(value):
    try:
        res = point_to_lett(value)
        return res
    except:
        try:
            res = lett_to_point(value)
            return res
        except:
            raise ValueError('the supplied input is not valid.')


def main():
    mygrade = input('enter either a letter or point grade: ')
    while mygrade != '':
        try:
            print(grade_converter(mygrade))
            mygrade = input('enter either a letter or point grade: ')
        except:
            print('invalid input, retry')
            mygrade = input('enter either a letter or point grade: ')


if __name__ == '__main__':
    main()
