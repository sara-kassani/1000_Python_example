# exercise 134: Generate All Sublists of a List

def allSublists(data):
    # there will be at least an empy list as sublist
    sublists = [[]]
    # generate all of the sublists from length 1 to length 4
    # length will assume values between 1 and 4 included
    for length in range(1, len(data)+1):
        # generate the sublists starting at each index
        # i will assume values between 0 and 3 included
        for i in range(0, len(data) - length + 1):
            sublists.append(data[i : i + length])
    return sublists


if __name__ == '__main__':
    data = [1, 2, 3, 4]
    print(allSublists(data))


"""
Example with parameter data = [1, 2, 3, 4]
in the first iteration I will have to 'extract' sublists of length 1, thus with one elemeny only. 
Looping each index from 0 to 3 adding each single element as sublist.
When passing to length 2, I will be extracting sublists of length 2 and by looping each index I
will make it possible to push all possible combinations of two elements.
Same logic until getting to length 4, when I will extract the only 4-element sublist:
in that case i will range from 0 to 1 (4-4+1), therefore in that single final loop I will extract
the sublist that comes from data[0 : 0 + 4] namely data [0:4] namely a sublist of the first 3 elements,
in other words the entire passed list.
"""