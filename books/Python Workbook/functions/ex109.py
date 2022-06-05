# exercise 109: Magic Date

from functions.ex106 import isLeap, daysInMonth


def isMagicDate(day, month, year):
    two_digit_year = int(str(year)[2] + str(year)[3])
    if day * month == two_digit_year:
        return True
    else:
        #print('not magic date')
        return False


def main():
    #list_of_magic_dates = []
    for yyyy in range(1900, 2000):
        for mm in range(1, 13):
            for dd in range(1, daysInMonth(mm, yyyy)):
                if isMagicDate(dd, mm, yyyy):
                    print("%.2d-%.2d-%.4d"%(dd, mm, yyyy))
                    #list_of_magic_dates.append('%.2d-%.2d-%.4d'%(dd,mm,yyyy))
    #print(list_of_magic_dates)


if __name__ == '__main__':
    main()
