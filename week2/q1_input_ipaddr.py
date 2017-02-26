#!/usr/bin/env python

input = input("Enter IP address: ")

octets = input.split(".")
octets = octets[:3]
octets.append("0")

network = ".".join(octets)
first_octet_bin = bin(int(octets[0]))
first_octet_hex = hex(int(octets[0]))

print("%-20s%-20s%-20s" % ("NETWORK_NUMBER", "FIRST_OCTET_BINARY", "FIRST_OCTET_HEX"))
print("%-20s%-20s%-20s" % (network, first_octet_bin, first_octet_hex))
