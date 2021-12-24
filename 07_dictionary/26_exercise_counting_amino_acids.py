# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:23:06 2021

@author: sarak
"""
# Count Amino Acid
# Generate random DNA sequence
# import sys
# import random

# if len(sys.argv) != 2:
#     exit("Need a number")
# count = int(sys.argv[1])

# dna = []
# for _ in range(count):
#     dna.append(random.choice(['A', 'C', 'T', 'G']))
# print(''.join(dna))

###############################################################################
dna = 'CACCCATGAGATGTCTTAACGCTGCTTTCATTATAGCCG'

aa_by_codon = {
'ACG' : '?',
'CAC' : 'Histidin',
'CAU' : 'Histidin',
'CCA' : 'Proline',
'CCG' : 'Proline',
'GAT' : '?',
'GTC' : '?',
'TGA' : '?',
'TTA' : '?',
'CTG' : '?',
'CTT' : '?',
'TCA' : '?',
'TAG' : '?',
#...
}

count = {}

for i in range(0, len(dna)-2, 3):
    codon = dna[i:i+3]
    print(codon)
                # CAC
                # CCA
                # TGA
                # GAT
                # GTC
                # TTA
                # ACG
                # CTG
                # CTT
                # TCA
                # TTA
                # TAG
                # CCG

    aa = aa_by_codon[codon]
    if aa not in count:
        count[aa] = 0
    count[aa] += 1

for aa in sorted(count.keys()):
    print("{}: {}".format(aa, count[aa]))

                # ?: 10
                # Histidin: 1
                # Proline: 2







