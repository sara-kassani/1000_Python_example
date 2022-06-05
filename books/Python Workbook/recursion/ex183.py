# exercise 183: Element Sequences

elements = []
inf = open('../files/elements.txt', 'r')
all_lines = inf.readlines()

for el in all_lines:
    element = el.split(',')[2].strip()
    elements.append(element)

elements.sort()
print(elements)


def longestSequence(start, words):
    if start == '':
        return []

    best = []
    last_letter = start[len(start) - 1].lower()

    for i in range(0, len(words)):
        first_letter = words[i][0].lower()

        if first_letter == last_letter:
            candidate = longestSequence(words[i], words[0:i] + words[i+1:len(words)])

            if len(candidate) > len(best):
                best = candidate

    return [start] + best


if __name__ == '__main__':
    print(longestSequence('Manganese', elements))
