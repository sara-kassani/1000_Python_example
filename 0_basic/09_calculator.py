'''
Create a script that accepts 2 numbers and an operator (+, -, *, /), and prints the result of the operation
'''
def main():
    operand1 = float(input('Enter the first operand: '))
    operand2 = float(input('Enter the second operand: '))
    operator = input('Enter the operator (+-*/): ')

    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    else:
        print('Error: invalid operator')

    print(result)

if __name__ == '__main__':
    main()