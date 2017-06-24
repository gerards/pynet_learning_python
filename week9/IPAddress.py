#!/usr/bin/env python
'''

Pynet : Learning Python
 - Week9, Question 1

'''

class IPAddress(object):
    " IP address class "

    def __init__(self, ip_address):
        " Create IPAddress object, takes an IP address string input "

        self.ip_address = ip_address


    def get_ip(self):
        " Returns the IP address "

        return self.ip_address

    def display_in_binary(self):
        " Returns IP address in binary "

        octets = self.ip_address.split(".")
        binary_octets = []

        for octet in octets:
            binary_octets.append(bin(int(octet)))
            binary_octets[-1] = binary_octets[-1][2:]
            # OR binary_octets[-1] = binary_octets[-1].split("0b")[1]
            binary_octets[-1] = binary_octets[-1].rjust(8, "0")


        return ".".join(binary_octets)

    def display_in_hex(self):
        " Returns IP address in hexidecimal "

        octets = self.ip_address.split(".")
        hex_octets = []

        for octet in octets:
            hex_octets.append(hex(int(octet)))
            hex_octets[-1] = hex_octets[-1][2:]
            # OR binary_octets[-1] = binary_octets[-1].split("0b")[1]
            hex_octets[-1] = hex_octets[-1].rjust(2, "0")


        return ".".join(hex_octets)


    def ip_isvalid(self):
        " Run checks over IP address "


        ip_address_octets = self.ip_address.split(".")

        '''
        Check the IP address number of octets is 4
        '''
        if len(ip_address_octets) != 4:
            return False

        '''
        Check the IP address octet range is valid
        '''
        if len(ip_address_octets) == 4:
            try:
                if int(ip_address_octets[0]) < 1 and \
                   int(ip_address_octets[0]) > 223 and \
                   int(ip_address_octets[0]) == 127:
                    return False

                for octet in ip_address_octets[1:]:
                    if int(octet) < 0 and int(octet) > 255:
                        return False

            except ValueError:
                return False


        '''
        Check IP address for specific numbering
        '''
        if not ip_address_octets[0] != "169" and ip_address_octets[1] != "254":
            return False

        return True
