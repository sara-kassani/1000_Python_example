# exercise 149: Display the Head of a File

from pathlib import Path


data_folder = Path("../files")
file_to_open = data_folder / "elements.txt"

fin = open(file_to_open, 'r')
for i in range(10):
    print(fin.readline())

"""
readline() reads one single line keeping track of where it left: if I call it
10 times, it will read 10 consecutive lines
"""

""" if importing os.path:
file_to_open = os.path.join("..", "files", "elements.txt")
"""
