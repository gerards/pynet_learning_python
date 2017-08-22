#!/usr/bin/env python
"""

ch3q3


show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

From this output, create a list where each element in the list is a tuple consisting of (interface_name, ip_address, status, protocol).  Only include interfaces that are in the up/up state.

Print this list to standard output.

"""

import pprint


def main():
    " MAIN! "

    output = {}
    show_ip_int_brief = \
'''Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up'''

    interfaces = show_ip_int_brief.split("\n")[1:]

    for interface in interfaces:
        interface_name = interface.split()[0]
        ip_address = interface.split()[1]
        status = interface.split()[4]
        protocol = interface.split()[5]

        if (status == "up") and (protocol == "up"):
            output[interface_name] = [ip_address, status, protocol]

    pprint.pprint(output)
'''
    for key, value in output.items():
        print("%20s : %-30s" % (key, value))
'''

if __name__ == "__main__":
    main()
