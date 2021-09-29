"""
Exercise: color selector menu
• In a script have a list of colors. Write a script that will display a menu (a list of numbers and
the corresponding color) and prompts the user for a number. The user needs to type in one of
the numbers. That’s the selected color.
    1. blue
    2. green
    3. yellow
    4. white
• For extra credit make sure the system is user-proof and it won’t blow up on various incorrect
input values. (e.g Floating point number. Number that is out of range, non-number)
"""


def main():
    colors = ['blue', 'yellow', 'black', 'purple']

    # for ix in range(len(colors)):
    #     print('{}) {}'.format(ix+1, colors[ix]))

    for i, color in enumerate(colors):
       print('{}) {}'.format(i + 1, color))

    selection = input('Select color: ')
    if not selection.isdecimal():
        exit(f'We need a number between 1 and {len(colors)}')

    if int(selection) < 1 or int(selection) > len (colors):
        exit(f'The number must be between 1 and {len(colors)}')

    col = int(selection) - 1
    print(colors[col])


if __name__ == '__main__':
    main()

    
