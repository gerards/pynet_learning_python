#!/usr/bin/env python
'''

ch6q2.py


Write a function that converts a list to a dictionary where the index of the
list is used as the key to the new dictionary (the function should return the
new dictionary).

'''

import pprint

def list_to_dictionary(a_list):
    ' list to dict '
    a_dict = {}

    for cnt, value in enumerate(a_list):
        a_dict[cnt] = value

    return a_dict


def main():
    ' main! '

    test_list = ['a', 'b', 99, (1, 2, 3)]

    print()
    pprint.pprint(test_list)
    print()
    pprint.pprint(list_to_dictionary(test_list))
    print()


if __name__ == '__main__':
    main()
