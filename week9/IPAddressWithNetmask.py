#!/usr/bin/env python
'''

Pynet : Learning Python
    - Week 9, Question 3

'''

from IPAddress import IPAddress

class IPAddressWithNetmask(IPAddress):
    " IPAddressWithNetmask class which inherits IPAddress class "

    def __init__(self, ip_cidr):
        self.ip_address, self.subnet_bits = ip_cidr.split("/")
        self.netmask = "/" + self.subnet_bits
        IPAddress.__init__(self, self.ip_address)

    def mask_in_bits(self):
        " blah "

        netmask_bits = self.subnet_bits
        netmask_bits = "1" * int(netmask_bits)
        while len(netmask_bits) < 32:
            netmask_bits = netmask_bits + "0"

        return netmask_bits


def main():
    " Main! "

    test_ip = IPAddressWithNetmask("192.168.1.1/24")

    print(test_ip.ip_address)
    print(test_ip.subnet_bits)
    print(test_ip.netmask)
    print(test_ip.display_in_binary())
    print(test_ip.mask_in_bits())

if __name__ == "__main__":
    main()
