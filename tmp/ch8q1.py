#!/usr/bin/env python
'''

ch8q1.py

'''


def valid_ip(ip_addr):
    ' is ip_addr valid '

    ip_valid = True
    octets = ip_addr.split('.')

    try:
        if len(octets) != 4:
            ip_valid = False
        elif (int(octets[0]) < 1) or (int(octets[0]) > 223):
            ip_valid = False
        elif int(octets[0]) == 127:
            ip_valid = False
        elif (int(octets[0]) == 169) and (int(octets[1]) == 254):
            ip_valid = False

        for octet in (octets[1], octets[2], octets[3]):
            if (int(octet) < 0) or (int(octet) > 255):
                ip_valid = False

    except ValueError:
        ip_valid = False
    except IndexError:
        ip_valid = False

    return ip_valid


def main():
    ' MAIN! '

    test_ip_addresses = {
        '192.168.1': False,
        '10.1.1.': False,
        '10.1.1.x': False,
        '0.77.22.19': False,
        '-1.88.99.17': False,
        '241.17.17.9': False,
        '127.0.0.1': False,
        '169.254.1.9': False,
        '192.256.7.7': False,
        '192.168.-1.7': False,
        '10.1.1.256': False,
        '1.1.1.1': True,
        '223.255.255.255': True,
        '223.0.0.0': True,
        '10.200.255.1': True,
        '192.168.17.1': True,
    }

    for key, value in test_ip_addresses.items():
        if valid_ip(key) == value:
            print("IP %s test passed" % (key))
        else:
            print("IP %s test did not pass. Expected Result: %s, Test Result: %s"
                  % (key, value, valid_ip(key)))

if __name__ == '__main__':
    main()
