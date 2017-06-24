#!/usr/bin/env python3
'''

Pynet Learning Python
 - Week 6, Question 3

'''

import sys



def ip_isvalid(ip_addr):
    " Run checks over IP address "

    ip_addr_octets = ip_addr.split(".")

    # perform checks
    valid_ip_addr = ip_addr_octet_check(ip_addr_octets) and \
                    ip_addr_octet_range_check(ip_addr_octets) and \
                    ip_addr_not_169_254_check(ip_addr_octets)

    return valid_ip_addr


def ip_addr_octet_check(ip_address_octets):
    " Check the IP address number of octets is 4 "
    return len(ip_address_octets) == 4

def ip_addr_octet_range_check(ip_address_octets):
    " Check the IP address octet range is valid "
    return int(ip_address_octets[0]) >= 1 and \
       int(ip_address_octets[0]) <= 223 and \
       int(ip_address_octets[0]) != 127 and \
       int(ip_address_octets[1]) >= 1 and \
       int(ip_address_octets[1]) <= 255 and \
       int(ip_address_octets[2]) >= 1 and \
       int(ip_address_octets[2]) <= 255 and \
       int(ip_address_octets[3]) >= 1 and \
       int(ip_address_octets[3]) <= 255

def ip_addr_not_169_254_check(ip_address_octets):
    " Check IP address for specific numbering "
    return ip_address_octets[0] != 169 and ip_address_octets[1] != 254

def main():
    " main one "
    if len(sys.argv) != 1:
        sys.exit("Usage: " + sys.argv[0])

    ip_addr = ""

    while ip_isvalid(ip_addr) is False:
        ip_addr = input("\n%-20s : " % "Enter IP Address")

        if ip_isvalid(ip_addr):
            print("%-20s : %-20s" % ("Valid IP address", "True"))
        else:
            print("%-20s : %-20s" % ("Valid IP address", "False"))

if __name__ == "__main__":
    main()
