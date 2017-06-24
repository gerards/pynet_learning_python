#!/usr/bin/env python
"""

ch3q1

"""

import sys


def main():
    " MAIN! "
    try:
        ip_address = sys.argv[1]
    except IndexError:
        sys.exit(sys.argv[0] + " <ip_address>")

    octets = ip_address.split(".")

    if len(octets) == 4:
        ip_address_bin_list = []

        for octet_cnt, octet in enumerate(octets):
            octet_cnt = octet_cnt + 1
            octet_bin = bin(int(octet))[2:]
            octet_bin_len = len(octet_bin)

            if len(octet_bin) > 8:
                sys.exit("IP Address invalid: octet number " + str(octet_cnt) +
                         " has length " + str(octet_bin_len))
            else:
                octet_bin = ((8 - len(octet_bin)) * "0") + str(octet_bin)

            ip_address_bin_list.append(octet_bin)
        ip_address_bin = ".".join(ip_address_bin_list)

        ip_address_hex_list = []
        for octet in octets:
            octet_hex = hex(int(octet))[2:]
            octet_hex = ((2 - len(octet_hex)) * "0") + str(octet_hex)
            ip_address_hex_list.append(octet_hex)
        ip_address_hex = ".".join(ip_address_hex_list)

        print()
        print("%-20s%-40s%-20s" % ("IP Subnet Decimal",
                                   "IP Subnet Binary",
                                   "IP Subnet Hexidecmial"))
        print("%-20s%-40s%-20s" % (ip_address,
                                   ip_address_bin,
                                   ip_address_hex))
        print()
    else:
        sys.exit("IP Address invalid: Incorrect ammount of subnets: " +
                 str(len(octets)))



if __name__ == "__main__":
    main()
