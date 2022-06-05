# exercise 130: Unary and Binary Operators

def tokenlist(s):
    """
    :param s: a math expression as string
    :return: a list of tokens (without indicating if the + and - are unary or binary operators)
    """
    op = ['(', ')', '*', '/', '^', '+', '-']
    s = s.replace(" ", "")
    tokens = []

    i = 0
    while i < len(s):
        # handling case when an operator is encountered
        if s[i] in op:
            tokens.append(s[i])
            i = i+1

        # handling case when a digit is encountered
        elif s[i] >= '0' and s[i] <= '9':
            # I have to check how long is the number (how many more digits)
            num = ''
            while i < len(s) and s[i] >= '0' and s[i] <= '9':
                num = num + s[i]
                i =  i + 1
            # when exiting the loop, the number is pushed as a new token
            tokens.append(num)

        # in any other case there is a not valid element
        else:
            return []

    return tokens


def identify_unary(tokens):
    """
    the function will indicate if the + and - operators are unary, by adding an 'u' in that case
    :param tokens: starting list of tokens without indication of unary operators
    :return: the new list of token with such indication
    """
    length = len(tokens)
    new_tokens = []

    i = 0
    while i < length:
        # if no element comes before + or -, it is for sure a unary operator
        if i == 0 and (tokens[i] == '+' or tokens[i] == '-'):
            new_tokens.append('u' + tokens[i])
            i += 1

        # if the previous element is an operator itself or an open parentheses, + or - is a unary operator
        # in case of close parentheses before the + or -, it is not a unary (e.g. ((7x) + 5))
        elif i > 0 and (tokens[i] == '+' or tokens[i] == '-') and \
                (tokens[i-1] == '*' or tokens[i-1] == '+' or tokens[i-1] == '-'\
                        or tokens[i-1] == '/' or tokens[i-1] == '('):
            new_tokens.append('u' + tokens[i])
            i += 1

        # in any other case the + or - are binary operators: nothing changes, no "u" added before it
        else:
            new_tokens.append(tokens[i])
            i += 1

    return new_tokens



def main():
    expression = input('exp: ')
    tokens = tokenlist(expression)
    print('here are your tokens:')
    print(tokens)
    precise_tokens = identify_unary(tokens)
    print('here are your tokens with details about unary operators:')
    print(precise_tokens)


if __name__ == '__main__':
    main()
