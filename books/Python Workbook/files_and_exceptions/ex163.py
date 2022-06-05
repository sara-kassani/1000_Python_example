# exercise 163: Names that Reached Number One

from pathlib import Path

FIRST_YEAR = 1900
LAST_YEAR = 2012


def LoadAndAdd(fname, names):
    inf = open(fname, 'r')
    line = inf.readline()
    inf.close()
    parts = line.split()
    name = parts[0]

    if name not in names:
        names.append(name)


def main():
    girls = []
    boys = []

    data_folder = Path("../files/baby_names/BabyNames/")

    for year in range(FIRST_YEAR, LAST_YEAR + 1):
        f_to_open_g = data_folder / (str(year) + "_GirlsNames.txt")
        f_to_open_b = data_folder / (str(year) + "_BoysNames.txt")

        LoadAndAdd(f_to_open_g, girls)
        LoadAndAdd(f_to_open_b, boys)

    print('Girls\' names that reached #1:')
    for name in girls:
        print(' ', name)
    print()
    print('Boys\' names that reached #1:')
    for name in boys:
        print(' ', name)


if __name__ == '__main__':
    main()
