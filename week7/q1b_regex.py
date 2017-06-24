#!/usr/bin/env python
'''

Pynet : Learning Python
 - Week 7, Question 1

a. Create a program that opens the 'r1_cdp.txt' file and using regular expressions
extracts the remote hostname, remote IP address, model, vendor, and device_type.

b. Create a program that opens the 'sw1_cdp.txt' file and finds all of the remote
hostnames, remote IP addresses, and remote remote_platforms.  Your output should look
similar to the following:

 remote_hosts: ['R1', 'R2', 'R3', 'R4', 'R5']
          ip_addresses: ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5']
     remote_platform: ['Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881']

'''

import re

def main():
    " main one "

    remote_hosts = []
    ip_addresses = []
    remote_platform = []

    with open("sw1_cdp.txt") as file_sw1_cdp:
        for line in file_sw1_cdp:
            #print(line.strip('\n'))

            remote_hostname = re.findall(r"Device ID: (.+)", line)
            if remote_hostname:
                remote_hosts.append(remote_hostname[0])

            remote_ip_addr = re.findall(r"IP address: (.+)", line)
            if remote_ip_addr:
                ip_addresses.append(remote_ip_addr[0])

            remote_platform_capabilities = \
                    re.findall(r"Platform: (.+),\s*Capabilities: (.+) ", line)
            if remote_platform_capabilities:
                vendor, model = remote_platform_capabilities[0][0].split()
                #device_type = remote_platform_capabilities[0][1]
                remote_platform.append(vendor + ' ' + model)


    print('%20s : %-60s' % ('remote_hosts', remote_hosts))
    print('%20s : %-60s' % ('ip_addresses', ip_addresses))
    print('%20s : %-60s' % ('remote_platform', remote_platform))

main()
