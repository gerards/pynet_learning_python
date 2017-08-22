#!/usr/bin/env python
"""

ch2q2

"""

def main():
    " MAIN! "

    entries = {
        "entry1" : "*  1.0.192.0/18   157.130.10.233     0 701 38040 9737 i",
        "entry2" : "*  1.1.1.0/24       157.130.10.233     0 701 1299 15169 i",
        "entry3" : "*  1.1.42.0/24     157.130.10.233     0 701 9505 174082 1465 i",
        "entry4" : "*  1.0.192.0/19   157.130.10.233     0 701 6762 6762 6762 6762 38040 9737 i"
    }

    output = {}
    for key in entries:
        ip_prefix = entries[key].split()[1]
        as_path = entries[key].split()[4:-1]
        output[ip_prefix] = as_path

    print("%-20s%-60s" % ("ip_prefix", "as_path"))

    for key, value in output.items():
        print("%-20s%-60s" % (key, value))


if __name__ == "__main__":
    main()
