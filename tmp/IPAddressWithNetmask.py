#!/usr/bin/env python
'''

IPAddressWithNetmask.py

'''

from IPAddress import IPAddress


class IPAddressWithNetmask(IPAddress):

    def __init__(self, ipaddress_cidr):
        ipaddr, subnet = ipaddress_cidr.split("/")

        IPAddress.__init__(self, ipaddr)
        self.subnet = subnet
