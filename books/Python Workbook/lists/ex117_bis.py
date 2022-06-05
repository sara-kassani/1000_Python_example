# exercise 117: Only the Words


# in this version I also ignore _ and ' and - and ` (from sides) and I replace -- and - with spaces

def words_in_string(s):
    # replacing all -- with spaces and then split the string based on spaces
    s_draft = s.replace('--', ' ')
    s_draft = s_draft.replace('-', ' ')
    base_list = s_draft.replace('\'', ' ').split()
    # print(base_list)

    res_list = []

    for el in base_list:
        el = el.strip(", .?!-;:\"()_`")
        if el:
            res_list.append(el.lower())

    return res_list


def main():
    string = input('enter a string: ')
    print(words_in_string(string))


if __name__ == "__main__":
    main()
