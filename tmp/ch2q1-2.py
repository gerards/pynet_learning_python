#!/usr/bin/env python
"""

Q2

"""

def main():
    " MAIN! "

    ip_subnet = input("Enter IP Network: ")

    octets = ip_subnet.split(".")
    octets = octets[:3]
    octets.append("0")

    ip_subnet_bin_list = []
    for octet in octets:
        octet_bin = bin(int(octet))[2:]
        octet_bin = ((8 - len(octet_bin)) * "0") + str(octet_bin)
        ip_subnet_bin_list.append(octet_bin)
    ip_subnet_bin = ".".join(ip_subnet_bin_list)

    ip_subnet_hex_list = []
    for octet in octets:
        octet_hex = hex(int(octet))[2:]
        octet_hex = ((2 - len(octet_hex)) * "0") + str(octet_hex)
        ip_subnet_hex_list.append(octet_hex)
    ip_subnet_hex = ".".join(ip_subnet_hex_list)

    print()
    print("%-20s%-40s%-20s" % ("IP Subnet Decimal",
                               "IP Subnet Binary",
                               "IP Subnet Hexidecmial"))
    print("%-20s%-40s%-20s" % (ip_subnet,
                               ip_subnet_bin,
                               ip_subnet_hex))


if __name__ == "__main__":
    main()
