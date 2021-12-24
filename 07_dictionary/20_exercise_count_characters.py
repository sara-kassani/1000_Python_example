# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:36:40 2021

@author: sarak
"""
# Exercise:count characters
# Given a long text, count how many times each character appears?
#%%%%
def main():

    text = """
    This is a vey long text.
    Ok, maybe this is not that long after all.
    """
    count = {}
    for char in text:
        if char == '\n':
            continue
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    for key in sorted(count.keys()):
        print(" '{}' {}".format(key, count[key]))


    # We need to store the counter somewhere. We could use two lists for that, but that would give a complex solution that runs in O(n**2) time.

#%%%%
    from collections import defaultdict

    count = defaultdict(int)

    for char in text:
        if char == '\n':
            continue
        count[char] += 1

    for key in sorted(count.keys()):
        print("'{}', {}".format, key, count[key])





#%%%%
if __name__ == '__main__':
    main()