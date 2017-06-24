#!/usr/bin/env python
'''

Pynet - Learning Python
 - Week6, Question 5

'''

import sys
from q3_ipaddr_check import ip_isvalid
from q4_ipaddr_converter import convert_to_binary

if len(sys.argv) != 2:
    sys.exit("Usage: " + sys.argv[0] + " <ip_address>")

IP_INPUT = sys.argv.pop()

def main():
    " main one "

    if ip_isvalid(IP_INPUT):
        bin_ip_addr = convert_to_binary(IP_INPUT)

        # print the output
        print("IP is valid\n")
        print("\n%-15s %-45s" % ("IP Address", "Binary"))
        print("%-15s %-45s\n\n" % (IP_INPUT, bin_ip_addr))
    else:
        print("IP is not valid\n")


main()
