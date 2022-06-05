# exercise 129: Tokenizing a String


def tokenizing_str(mathexp):
    tokens = ['(', ')', '*', '/', '^']
    tokens_cond = ['+', '-']

    # first thing is deleting all spaces
    s = mathexp.replace(" ", "")
    str_to_token = []
    i = 0

    # using a while loop because a for loop here would make it hard to correctly increment the loop variable
    while i < len(s):
        # handling case when the element is a single character
        if s[i] in tokens:
            str_to_token.append(s[i])
            i = i + 1

        # handling case when a + or - is encountered
        elif s[i] in tokens_cond:

            # if there is a previous element, and that element is a number or parentheses
            if i > 0 and (s[i - 1] >= '0' and s[i - 1] <= '9' or s[i - 1] == ')'):
                # then the + or - refers to an operator
                str_to_token.append(s[i])
                i = i + 1

            # otherwise,the + o - is part of a number (e.g. +5) but I have to understand how long it is
            # e.g. if the previous element is ( then the following + is of course part of a number (e.g. +5)
            else:
                # first thing is adding + or - to the num variable and incrementing the loop variable by 1
                num = s[i]
                i = i + 1

                # as long as I see numbers ahead, I keep pushing those numbers tonum, incrementing the loop variable
                while i < len(s) and s[i] >= '0' and s[i] <= '9':
                    num = num + s[i]
                    i = i + 1
                    # once exiting the loop, the number is finished: I can push the num in the token list
                str_to_token.append(num)

        # handling case when a number (without leading + or -) is encountered
        # as before, I start by pushing the first digit but I have to check how many other digits are inside the number
        elif '0' <= s[i] <= '9':
            num = ""
            while i < len(s) and s[i] >= '0' and s[i] <= '9':
                num += s[i]
                i += 1
            str_to_token.append(num)

        # in any other case there will be a not valid element inside the expression
        else:
            return 'error: invalid math expression'

    return str_to_token


def main():
    my_mathexp = input('enter a math expression: ')
    print(tokenizing_str(my_mathexp))


if __name__ == '__main__':
    main()
