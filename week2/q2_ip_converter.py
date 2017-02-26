#!/usr/bin/env python

input = input("Enter IP address: ")
octets = input.split(".")
first_octet = bin(int(octets[0]))
second_octet = bin(int(octets[1]))
third_octet = bin(int(octets[2]))
forth_octet = bin(int(octets[3]))

print("%-20s%-20s%-20s%-20s" % ("First Octet", "Second Octet",
                                "Third Octet", "Forth Octet"))
print("%-20s%-20s%-20s%-20s" % (first_octet, second_octet,
                                third_octet, forth_octet))
