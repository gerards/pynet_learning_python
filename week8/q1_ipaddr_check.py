#!/usr/bin/env python3
'''

Pynet Learning Python
 - Week 6, Question 3

'''

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
    if len(ip_address_octets) == 4:
        try:
            return int(ip_address_octets[0]) >= 1 and \
                    int(ip_address_octets[0]) <= 223 and \
                    int(ip_address_octets[0]) != 127 and \
                    int(ip_address_octets[1]) >= 0 and \
                    int(ip_address_octets[1]) <= 255 and \
                    int(ip_address_octets[2]) >= 0 and \
                    int(ip_address_octets[2]) <= 255 and \
                    int(ip_address_octets[3]) >= 0 and \
                    int(ip_address_octets[3]) <= 255
        except ValueError:
            return False


def ip_addr_not_169_254_check(ip_address_octets):
    " Check IP address for specific numbering "
    return ip_address_octets[0] != "169" and ip_address_octets[1] != "254"

def main():
    " main one "

    test_ip_addresses = {
        '192.168.1' : False,
        '10.1.1.' : False,
        '10.1.1.x' : False,
        '0.77.22.19' : False,
        '-1.88.99.17' : False,
        '241.17.17.9' : False,
        '127.0.0.1' : False,
        '169.254.1.9' : False,
        '192.256.7.7' : False,
        '192.168.-1.7' : False,
        '10.1.1.256' : False,
        '1.1.1.1' : True,
        '223.255.255.255' : True,
        '223.0.0.0' : True,
        '10.200.255.1' : True,
        '192.168.17.1' : True,
    }

    for key, value in test_ip_addresses.items():
        print()
        print("Testing " + key + " ; Test case is " + str(value) + " ; Result is : "
              + str(ip_isvalid(key)))
        if ip_isvalid(key) == value:
            print("succeeded")
        else:
            print("failed")


if __name__ == "__main__":
    main()
