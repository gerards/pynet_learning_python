#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    # exit the script
    sys.exit("Usage: sys.argv[0] <ip_addr>")

ip_addr = sys.argv.pop()
octets = ip_addr.split(".")

# create blank list to allow .append() to use in method below
ip_addr_bin = []

if len(octets) == 4:
    for octet in octets:
        bin_octet = bin(int(octet))
        bin_octet = bin_octet[2:]

        padding_cnt = 8 - len(bin_octet)
        while padding_cnt != 0:
            bin_octet = '0' + bin_octet
            padding_cnt -= 1

        ip_addr_bin.append(bin_octet)

    # join binary elements into dotted-binary format
    ip_addr_bin = ".".join(ip_addr_bin)

    # print the output
    print("\n%-15s %-45s" % ("IP Address", "Binary"))
    print("%-15s %-45s\n\n" % (ip_addr, ip_addr_bin))
else:
    sys.exit("Invalid IP Address")

