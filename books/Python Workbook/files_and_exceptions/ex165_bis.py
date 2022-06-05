# exercise 165: Most Births in a Given Time Period

from pathlib import Path


year1 = input('enter the starting year: ')
year2 = input('enter the closing year: ')

# entering in a variable the base path to the folder of files
data_folder = Path("../files/baby_names/BabyNames/")
girl_names = []
boy_names = []

for y in range(int(year1), int(year2) + 1):
    # specifying the variable paths for girls and boys
    file_to_open_g = data_folder / (str(y) + "_GirlsNames.txt")
    file_to_open_b = data_folder / (str(y) + "_BoysNames.txt")
    # once specified the complete path for a given year, the program opens the relative files in read mode
    girl_fname = open(file_to_open_g, 'r')
    boy_fname = open(file_to_open_b, 'r')

    # opening the file for that year and gender, reading first line and dividing it in two elements, extracting name
    girl_name = girl_fname.readline().split()[0]
    boy_name = boy_fname.readline().split()[0]

    # pushing the most common name for that year inside the output list, if not present
    if girl_name not in girl_names:
        girl_names.append(girl_name)
    if boy_name not in boy_names:
        boy_names.append(boy_name)

    girl_fname.close()
    boy_fname.close()


def main():
    print('here are the most common girl names between %s and %s:'%(year1, year2))
    for name in girl_names:
        print(name, end= '  ')

    print()

    print('here are the most common boy names between %s and %s:'%(year1, year2))
    for name in boy_names:
        print(name, end='  ')


if __name__ == '__main__':
    main()


"""
possibility to add way to say in that years which is the single most frequent name
"""
