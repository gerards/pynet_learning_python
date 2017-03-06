#!/usr/bin/env python

show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0        unassigned      YES     unset       up          up
FastEthernet1        unassigned      YES     unset       up          up
FastEthernet2        unassigned      YES     unset       down        down
FastEthernet3        unassigned      YES     unset       up          up
FastEthernet4        6.9.4.10        YES     NVRAM       up          up
NVI0                 6.9.4.10        YES     unset       up          up
Tunnel1              16.25.253.2     YES     NVRAM       up          down
Tunnel2              16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES     NVRAM       down        down
Vlan10               10.220.88.1     YES     NVRAM       up          up
Vlan20               192.168.0.1     YES     NVRAM       down        down
Vlan100              10.220.84.1     YES     NVRAM       up          up
'''

# break into lines and remove blank first and last line and header line
# create empty list to append interesting lines
show_ip_lines = show_ip_int_brief.split("\n")
show_ip_lines = show_ip_lines[2:-1]
interfaces_upup = []

for line in show_ip_lines:
    # break into words
    line_split = line.split()

    # keep interfaces in up/up state
    if(line_split[4] == "up" and line_split[5] == "up"):
        interfaces_upup.append((line_split[0], line_split[1], line_split[4], line_split[5]))

# print
print("%-25s %-15s %-10s %-10s" % ("Interface", "IP-Address", "Status", "Protocol"))

for line in interfaces_upup:
    print("%-25s %-15s %-10s %-10s" % (line[0], line[1], line[2], line[3]))
