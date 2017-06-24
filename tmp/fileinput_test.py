#!/usr/bin/env python
"""

Testing

"""

import fileinput

def main():
    " Main! "
    for line in fileinput.input():
        for word in line.split(" "):
            print(word.strip())



if __name__ == "__main__":
    main()
