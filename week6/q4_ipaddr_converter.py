#!/usr/bin/env python
'''

Pynet Learning Python
 - Week6, Question 4

'''

import sys

def convert_to_binary(dec_ip_addr):
    " Convert decimal IP address to binary IP address "

    octets = dec_ip_addr.split(".")

    # create blank list to allow .append() to use in method below
    bin_ip_addr_list = []

    if len(octets) == 4:
        for octet in octets:
            bin_octet = bin(int(octet))
            bin_octet = bin_octet[2:]

            padding_cnt = 8 - len(bin_octet)
            while padding_cnt != 0:
                bin_octet = '0' + bin_octet
                padding_cnt -= 1

            bin_ip_addr_list.append(bin_octet)

        # join binary elements into dotted-binary format
        return ".".join(bin_ip_addr_list)

def main():
    " main one "

    if len(sys.argv) != 2:
        # exit the script
        sys.exit("Usage: " + sys.argv[0] + " <ip_input>")

    ip_input = sys.argv.pop()

    bin_ip_addr = convert_to_binary(ip_input)

    # print the output
    print("\n%-15s %-45s" % ("IP Address", "Binary"))
    print("%-15s %-45s\n\n" % (ip_input, bin_ip_addr))

if __name__ == '__main__':
    main()
