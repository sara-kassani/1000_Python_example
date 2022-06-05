# exercise 131: Infix to Postfix

# info: infix expression: 3 + 4 ; postfix expression: 3 4 +
# check conversions at https://www.mathblog.dk/tools/infix-postfix-converter/

from lists.ex129 import tokenizing_str
from functions.ex96 import isInteger
from functions.ex97 import precedence


def infix_to_postfix(t):
    all_op = ['+', '-', '*', '/', '**', '^']
    operators = []
    postfix = []
    for token in t:
        if isInteger(token):
            # print(token)
            postfix.append(token)
        if token in all_op:
            # note: I edited the sign of the precedence from < to <= with respect to the proposed solution of the book
            # basically, I have to move in postfix the operators even when they have the same precedence of the current
            while operators != [] and operators[-1] != '(' and precedence(token) <= precedence(operators[-1]):
                postfix.append(operators.pop())
            operators.append(token)
        if token == '(':
            operators.append(token)
        if token == ')':
            while operators[-1] != '(':
                postfix.append(operators.pop())
            operators.remove('(')

    while len(operators) > 0:
        # in ordet to remove from operators, I use pop() to avoid an infinite loop
        postfix.append(operators.pop())

    print(''.join(postfix))
    return postfix


def main():
    myexpression = input('enter math expression: ')
    infix_to_postfix(tokenizing_str(myexpression))


if __name__ == '__main__':
    main()