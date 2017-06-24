#!/usr/bin/env python
'''

Pynet Learning Python
 - Week6, Question 2

'''

import pprint

def convert_list_to_dict(a_list):
    " list the function says! "
    a_dict = {}
    for cnt, value in enumerate(a_list):
        a_dict[cnt] = value
    return a_dict

def main():
    " main stuff "
    list_1 = [0, 1, 2, 3, 4, 5]
    dict_1 = convert_list_to_dict(list_1)

    # Display the results
    print("List: %s" % str(list_1))
    print("Dict: %s" % str(dict_1))


if __name__ == "__main__":
    main()
