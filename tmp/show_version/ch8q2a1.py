#!/usr/bin/env python
'''

ch8q2a1.py

Function1 = obtain_os_version -- process the show version output and return the OS version (Version 15.0(1)M4) else return None.

Looking for line such as:
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)

'''

def obtain_os_version(show_ver_file):
    ' Return OS Version or None '

    os_version = None

    show_ver_list = show_ver_file.split('\n')

    for line in show_ver_list:
        if "Cisco IOS Software" in line:
            os_version = line.split(', ')[2]
            return os_version

    return os_version
