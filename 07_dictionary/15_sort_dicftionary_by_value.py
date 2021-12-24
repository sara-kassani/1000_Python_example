# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 02:04:48 2021

@author: sarak
"""
def main():
    scores = {
        'Foo': 10,
        'Bar': 23,
        'Miu': 84,
        }

    print(scores)    #  {'Foo': 10, 'Bar': 23, 'Miu': 84}

    sorted_names = sorted(scores)
    print(sorted_names)    #  ['Bar', 'Foo', 'Miu']

    for s in sorted_names:
        print('{}:  {}'.format(s, scores[s]))

                # Bar  23
                # Foo  10
                # Miu  84

    # sort the values but we cannot get the keys back
    print(sorted(scores.values()))    #  [10, 23, 84]

    print('')

    # sort using a lambda expression
    sorted_names = sorted(scores, key= lambda x: scores[x])

    for k in sorted_names:
        print('{}:  {}'.format(k, scores[k]))

            # Foo:  10
            # Bar:  23
            # Miu:  84

    print('')

    # sort the keys according to the values
    sorted_names = sorted(scores, key= scores.__getitem__)

    for k in sorted_names:
        print('{}: {}'.format(k, scores[k]))

            # Foo: 10
            # Bar: 23
            # Miu: 84

if __name__ == '__main__':
    main()