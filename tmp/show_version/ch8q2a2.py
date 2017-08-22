#!/usr/bin/env python
'''

ch8q2a2.py

Function2 = obtain_uptime -- process the show version output and return the
network device's uptime string (uptime is 12 weeks, 5 days, 1 hour, 4 minutes)
else return None.

Exmaple line:
twb-sf-881 uptime is 12 weeks, 5 days, 1 hour, 4 minutes

'''

def obtain_uptime(show_ver_file):
    ' Return uptime or None '

    uptime = None

    show_ver_list = show_ver_file.split('\n')

    for line in show_ver_list:
        line = line.strip()
        if 'uptime' in line:
            uptime = "uptime is" + line.split('uptime is')[1]
            return uptime

    return uptime
