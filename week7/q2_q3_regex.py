#!/usr/bin/env python
'''

Pynet : Learning Python
 - Class 7, Question 2

Open the regular file ospf_data.txt and use regular expressions extract the:
    - interface
    - IP address
    - area
    - type
    - cost
    - hello timer
    - dead timer

Your output should look similar to the following:

Int:        GigabitEthernet0/1
IP:        172.16.13.150/29
Area:    30395
Type:    BROADCAST
Cost:    1
Hello:   10
Dead:   40

'''

import re

def main():
    ' main one '
    with open("ospf_data.txt") as file_ospf_data:
        for line in file_ospf_data:
            #print(line.strip("\n"))

            re_interface_line = re.search(r'^(\w+\d+/?\d*\.?\d*) is up', line)
            if re_interface_line:
                print()
                interface = re_interface_line.group(1)
                print('%-10s : %-60s' % ("Int", interface))

            re_ip_address_line = re.search(r'^\s+Internet Address (.*?), Area (\d+),', line)
            if re_ip_address_line:
                ip_address = re_ip_address_line.group(1)
                area = re_ip_address_line.group(2)
                print('%-10s : %-60s' % ("IP", ip_address))
                print('%-10s : %-60s' % ("Area", area))

            re_process_id_line = \
              re.search(r'Process ID (\d+), Router ID (.*?), Network Type (.*?), Cost: (\d+)', line)
            if re_process_id_line:
                network_type = re_process_id_line.group(3)
                cost = re_process_id_line.group(4)
                print('%-10s : %-60s' % ("Type", network_type))
                print('%-10s : %-60s' % ("Cost", cost))

            re_timer_line = \
              re.search(r'Hello (\d+), Dead (\d+), Wait (\d+), Retransmit (\d+)', line)
            if re_timer_line:
                hello_timer = re_timer_line.group(1)
                dead_timer = re_timer_line.group(2)
                print('%-10s : %-60s' % ("Hello", hello_timer))
                print('%-10s : %-60s' % ("Dead", dead_timer))

    print()




main()
