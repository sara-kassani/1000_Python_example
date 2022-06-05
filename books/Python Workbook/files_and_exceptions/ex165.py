# exercise 165: Most Births in a Given Time Period

import os.path


year1 = input('enter the starting year: ')
year2 = input('enter the closing year: ')

data_folder = os.path.join('..', 'files', 'baby_names', 'BabyNames')
girl_names = []
boy_names = []

for y in range(int(year1), int(year2) + 1):
    file_to_open_g = os.path.join(data_folder, f"{y}_GirlsNames.txt")
    file_to_open_b = os.path.join(data_folder, f"{y}_BoysNames.txt")

    girl_fname = open(file_to_open_g, 'r')
    boy_fname = open(file_to_open_b, 'r')

    girl_name = girl_fname.readline().split()[0]
    boy_name = boy_fname.readline().split()[0]

    if girl_name not in girl_names:
        girl_names.append(girl_name)
    if boy_name not in boy_names:
        boy_names.append(boy_name)


def main():
    print(f"here are the most common girl names between {year1} and {year2}:")
    for name in girl_names:
        print(name, end ='  ')

    print()

    print(f"here are the most common boy names between {year1} and {year2}:")
    for name in boy_names:
        print(name, end='  ')


if __name__ == '__main__':
    main()