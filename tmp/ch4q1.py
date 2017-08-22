#!/usr/bin/env python
"""

ch4q1

"""


def main():
    " MAIN! "

    ip_valid = False

    while not ip_valid:
        ip_valid = True
        ip_address = input("\nEnter IP address: ")
        octets = ip_address.split(".")
        print(octets)

        try:
            if len(octets) != 4:
                ip_valid = False
                print("len check %s" % (len(octets)))

            ip_address_bin_list = []
            if (int(octets[0]) < 1) or (int(octets[0]) > 223):
                ip_valid = False
                print("\nIP Address is NOT VALID: Octet 1  must be " \
                         "between 1 - 223.\n")
            elif int(octets[1]) == 127:
                ip_valid = False
                print("\nIP Address is NOT VALID: Octet 1  must not " \
                         "equal 127.\n")
            elif (int(octets[0]) == 169) and (int(octets[1]) == 254):
                ip_valid = False
                print("\nIP Address is NOT VALID: Cannot use 169.254.x.x " \
                         " address space\n")

            cnt = 2
            for octet in (octets[1], octets[2], octets[3]):
                if (int(octet) < 1) or (int(octet) > 255):
                    ip_valid = False
                    print("\nIP Address is NOT VALID: Octect " + str(cnt) + " must be between" \
                         " 1 - 255.\n")
                cnt = cnt + 1

        except ValueError:
            ip_valid = False
            print("\nIP Address is NOT VALID: Must use Integers")
        except IndexError:
            ip_valid = False
            print("\nIP Address is NOT VALID: Address must contain " \
                      "four octets\n")
        if ip_valid:
            for octet in octets:
                octet_bin = bin(int(octet))[2:]

                ip_address_bin_list = []
                for octet in octets:
                    octet_bin = bin(int(octet))[2:]
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


if __name__ == "__main__":
    main()
