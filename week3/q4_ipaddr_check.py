#!/usr/bin/env python

import sys

ip_addr = sys.argv[1]
ip_addr_octets = ip_addr.split(".")

if len(sys.argv) != 2:
    sys.exit("Usage: " + sys.argv[0] + " <ip_address>")


def ip_addr_octet_check(ip_address_octets):
    if(len(ip_address_octets) == 4):
        return True
    else:
        return False

def ip_addr_octet_range_check(ip_address_octets):
    if(int(ip_address_octets[0]) >= 1 and
       int(ip_address_octets[0]) <= 223 and
       int(ip_address_octets[0]) != 127 and
       int(ip_address_octets[1]) >= 1 and
       int(ip_address_octets[1]) <= 255 and
       int(ip_address_octets[2]) >= 1 and
       int(ip_address_octets[2]) <= 255 and
       int(ip_address_octets[3]) >= 1 and
       int(ip_address_octets[3]) <= 255):
        return True
    else:
        return False

def ip_addr_not_169_254_check(ip_address_octets):
    if(ip_address_octets[0] != 169 and ip_address_octets[1] != 254):
        return True
    else:
        return False


# perform checks
print("%-20s : %-20s" % ("IP Address entered", ip_addr))

if(ip_addr_octet_check(ip_addr_octets) and
   ip_addr_octet_range_check(ip_addr_octets) and
   ip_addr_not_169_254_check(ip_addr_octets)):
    print("%-20s : %-20s" % ("Valid IP address", "True"))
else:
    print("%-20s : %-20s" % ("Valid IP address", "False"))

