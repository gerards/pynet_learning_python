#!/usr/bin/env python
'''

ch9q1.py

'''


class IPAddress():
    ' IPAddress class '

    def __init__(self, ipaddr):
        self.ipaddr = ipaddr

    def display_in_binary(self):
        ' Convert IP address from decimal to binary '
        octets = self.ipaddr.split('.')
        bin_octets = []

        for octet in octets:
            octet = int(octet)
            bin_octet = bin(octet)[2:]
            bin_octet = bin_octet.rjust(8, '0')
            bin_octets.append(bin_octet)

        bin_addr = ".".join(bin_octets)
        return bin_addr

    def display_in_hex(self):
        ' Convert IP address from decimal to hexidecimal '
        octets = self.ipaddr.split('.')
        hex_octets = []

        for octet in octets:
            octet = int(octet)
            hex_octet = hex(octet)[2:]
            hex_octet = hex_octet.rjust(2, '0')
            hex_octets.append(hex_octet)

        hex_addr = ".".join(hex_octets)
        return hex_addr

    def is_valid(self):
        ' Check IP address is valid. Returns True of False '

        ip_valid = True
        octets = self.ipaddr.split('.')

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


class IPAddressWithNetmask(IPAddress):
    ' IPAddress with Netmask using CIDR format '

    def __init__(self, ipaddress_cidr):
        ipaddr, subnet = ipaddress_cidr.split("/")

        IPAddress.__init__(self, ipaddr)
        self.netmask = "/" + subnet

    def display_netmask(self):
        ' Print subnet mask in binary '

        netmask = self.netmask.strip('/')
        netmask_dotdecimal = ''
        netmask_dotdecimal_octets = []
        netmask_bin = int(netmask) * "1" + (32 - int(netmask)) * "0"
        netmask_bin_octets = []

        cnt = 8
        while cnt <= 32:
            netmask_bin_octets.append(netmask_bin[(cnt - 8):cnt])
            cnt += 8

        for octet in netmask_bin_octets:
            netmask_dotdecimal_octets.append(str(int(octet, 2)))

        netmask_dotdecimal = ".".join(netmask_dotdecimal_octets)

        return netmask_dotdecimal


def main():
    ' MAIN '
    cidr = IPAddressWithNetmask('192.168.1.1/24')

    print()
    print("%20s: %-40s" % ("IP", cidr.ipaddr))
    print("%20s: %-40s" % ("Netmask", cidr.display_netmask()))
    print("%20s: %-40s" % ("IP - Binary", cidr.display_in_binary()))
    print("%20s: %-40s" % ("IP - Hexidecimal", cidr.display_in_hex()))
    print("%20s: %-40s" % ("Valid IP Address", cidr.is_valid()))
    print()


if __name__ == '__main__':
    main()
