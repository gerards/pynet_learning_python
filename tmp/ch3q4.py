#!/usr/bin/env python
"""

ch3q1

"""

import sys


def main():
    " MAIN! "
    if len(sys.argv) != 2:
        sys.exit("Usage: ./" + sys.argv[0] + " <ip_address>")

    ip_address = sys.argv.pop()
    octets = ip_address.split(".")

    if len(octets) != 4:
        sys.exit("IP Address is NOT VALID: Address must contain four octets")

    ip_address_bin_list = []
    try:
        if (int(octets[0]) < 1) or (int(octets[0]) > 223):
            sys.exit("\nIP Address is NOT VALID: First octet must be " \
                     "between 1 - 223.\n")
        elif int(octets[1]) == 127:
            sys.exit("\nIP Address is NOT VALID: First octet must not " \
                     "equal 127.\n")
        elif (int(octets[0]) == 169) and (int(octets[1]) == 254):
            sys.exit("\nIP Address is NOT VALID: Cannot use 169.254.x.x " \
                     " address space\n")
        elif (int(octets[1]) < 1) or (int(octets[1]) > 255):
            sys.exit("\nIP Address is NOT VALID: Second octect must be between" \
                     " 1 - 255.\n")
        elif (int(octets[2]) < 1) or (int(octets[2]) > 255):
            sys.exit("\nIP Address is NOT VALID: Third octect must be between" \
                     " 1 - 255.\n")
        elif (int(octets[3]) < 1) or (int(octets[3]) > 255):
            sys.exit("\nIP Address is NOT VALID: Forth octect must be between" \
                     " 1 - 255.\n")
    except ValueError:
        sys.exit("\nIP Address is NOT VALID: Must use Integers")

    for octet in octets:
        octet_bin = bin(int(octet))[2:]

        ip_address_bin_list = []
        for octet in octets:
            octet_bin = bin(int(octet))[2:]
            octet_bin = ((8 - len(octet_bin)) * "0") + str(octet_bin)
            ip_address_bin_list.append(octet_bin)
        '''
        ip_address_bin = ".".join(ip_address_bin_list)
        '''

        ip_address_hex_list = []
        for octet in octets:
            octet_hex = hex(int(octet))[2:]
            octet_hex = ((2 - len(octet_hex)) * "0") + str(octet_hex)
            ip_address_hex_list.append(octet_hex)
        '''
        ip_address_hex = ".".join(ip_address_hex_list)
        '''



    print()
    print("IP Address is VALID")
    print()
    '''
    print("%-20s%-40s%-20s" % ("IP Subnet Decimal",
                               "IP Subnet Binary",
                               "IP Subnet Hexidecmial"))
    print("%-20s%-40s%-20s" % (ip_address,
                               ip_address_bin,
                               ip_address_hex))
    print()
    '''

if __name__ == "__main__":
    main()
