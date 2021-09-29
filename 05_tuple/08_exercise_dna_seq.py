"""
Exercise: DNA sequencing
- A, C, T, G are called bases or nucleotides
- Given a sequence like 'ACCGXXCXXGTTACTGGGCXTTGTXX' (nucleotide mixed up with other elements)
- First return the sequences containing only ACTG. The above string will ve changed to [[‘ACCG’, ‘C’, ‘GTTACTGGGC’, ‘TTGT’].
- Then sort them by length. Expected result: [‘GTTACTGGGC’, ‘ACCG’, ‘TTGT’, ‘C’]
- What if the original string contains more than on type of forming elements? e.g. ‘ACCGXXCXXYYGTTQRACQQTGGGCXTTGTXX’. Can you do the same?
"""


def main():
    ##########################################################
    # dna = 'ACCGXXCXXGTTACTGGGCXTTGT'
    # sequences = dna.split('X')
    # sequences.sort(key = len, reverse = True)
    #
    # new_seq = []
    # for w in sequences:
    #     if len(w) > 0:
    #         new_seq.append(w)
    #
    # print(sequences)
    # print(new_seq)
    ##########################################################
    # Solution: DNA sequencing with filter
    # dna = 'ACCGXXCXXGTTACTGGGCXTTGT'
    # sequences = dna.split('X')
    # sequences.sort(key = len, reverse = True)
    #
    # def not_empty(x):
    #     return len(x) > 0
    #
    # print(sequences)
    # sequences = list(filter(not_empty, sequences))
    # print(sequences)
    ##########################################################
    # Solution: DNA sequencing with filter and lambda
    dna = 'ACCGXXCXXGTTACTGGGCXTTGT'
    sequences = dna.split('X')
    sequences.sort(key = len, reverse = True)

    print(sequences)
    sequences = list(filter(lambda x: len(x) > 0, sequences))
    print(sequences)


if __name__ == '__main__':
    main()
