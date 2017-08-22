#!/usr/bin/env python
'''

ch9q1.py

'''

class IPAddress(object):
    ' IPAddress class '

    def __init__(self, ip_address):
        ' initialise IPAdress class '

        self.ip_addr = ip_address


    def display_in_binary(self):
        ' convert ip from dec to bin '

        octets = self.ip_addr.split('.')
        ip_address_list = []

        for octet in octets:
            octet_conversion = bin(int(octet))[2:]
            octet_conversion = ((8 - len(octet_conversion)) * '0') + str(octet_conversion)
            ip_address_list.append(octet_conversion)
        ip_address_converted = '.'.join(ip_address_list)

        return ip_address_converted


    def display_in_hex(self):
        ' convert ip from dec to hex '

        octets = self.ip_addr.split('.')
        ip_address_list = []

        for octet in octets:
            octet_conversion = hex(int(octet))[2:]
            octet_conversion = ((2 - len(octet_conversion)) * '0') + str(octet_conversion)
            ip_address_list.append(octet_conversion)
        ip_address_converted = '.'.join(ip_address_list)

        return ip_address_converted


    def ip_valid(self):
        ' is ip_addr valid '

        ip_valid = True
        octets = self.ip_addr.split('.')

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
