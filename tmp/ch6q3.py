#!/usr/bin/env python
'''

ch6q3.py

Convert the IP address validation code (Class4, exercise1) into a function, take one variable 'ip_address' and
return either True or False (depending on whether 'ip_address' is a valid IP). Only include IP address checking
in the function--no prompting for input, no printing to standard output.

Import this IP address validation function into the Python interpreter shell and test it (use both 'import x'
and 'from x import y').
---
Python 3.5.2 (default, Nov 13 2016, 21:41:46)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ch6q3
>>> help(ch6q3)
>>> ch6q3.valid_ip('asdf')
False
>>> ch6q3.valid_ip('192.1.1.1')
True
>>> from ch6q3 import valid_ip
>>> valid_ip('asdf')
False
>>> valid_ip('192.168.1.1')
True
>>> from ch6q3 import valid_ip as ipcheck
>>> ipcheck('192.168.1.1')
True
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'ch6q3', 'ipcheck', 'valid_ip']
---

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
        elif int(octets[1]) == 127:
            ip_valid = False
        elif (int(octets[0]) == 169) and (int(octets[1]) == 254):
            ip_valid = False

        cnt = 2
        for octet in (octets[1], octets[2], octets[3]):
            if (int(octet) < 1) or (int(octet) > 255):
                ip_valid = False
            cnt = cnt + 1

    except ValueError:
        ip_valid = False
    except IndexError:
        ip_valid = False

    return ip_valid


def convert_ipaddr(ip_addr, number_type):
    ' convert ip from dec to bin '

    octets = ip_addr.split('.')
    ip_address_list = []

    for octet in octets:
        if number_type == 'bin':
            octet_conversion = bin(int(octet))[2:]
            octet_conversion = ((8 - len(octet_conversion)) * '0') + str(octet_conversion)
        elif number_type == 'hex':
            octet_conversion = hex(int(octet))[2:]
            octet_conversion = ((2 - len(octet_conversion)) * '0') + str(octet_conversion)
        ip_address_list.append(octet_conversion)
    ip_address_converted = '.'.join(ip_address_list)

    return ip_address_converted


def main():
    ' MAIN! '

    ip_valid = False
    while not ip_valid:
        ip_address = input('\nEnter IP address: ')
        ip_valid = valid_ip(ip_address)

        if ip_valid:
            ip_address_bin = convert_ipaddr(ip_address, 'bin')
            ip_address_hex = convert_ipaddr(ip_address, 'hex')

    print()
    print('%-20s%-40s%-20s' % ('IP Subnet Decimal', 'IP Subnet Binary', 'IP Subnet Hexidecmial'))
    print('%-20s%-40s%-20s' % (ip_address, ip_address_bin, ip_address_hex))
    print()


if __name__ == '__main__':
    main()
