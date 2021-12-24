# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:43:01 2021

@author: sarak
"""

# Exercise: Count words
def main():
    words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']

#%%%% Soultion 1
    counter = {}
    for word in words:
        if word not in counter:
            counter[word] = 0
        counter[word] += 1


    for word in counter:
        print("{}: {}".format(word, counter[word]))
#%%%% Solustion 2

    from collections import Counter
    cnt = Counter()

    for word in words:
        cnt[word] += 1

    print(cnt)

    for w in cnt.keys():
        print("{} {}".format(w, cnt[w]))
#%%%% Solution 3
    from collections import defaultdict

    dd = defaultdict(lambda: 0)
    for word in words:
        dd[word] += 1
    print(dd)

    for word in dd.keys():
        print("{}: {}".format(word, dd[word]))

#%%%%
if __name__ == "__main__":
    main()