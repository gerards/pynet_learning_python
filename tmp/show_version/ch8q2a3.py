#!/usr/bin/env python
'''

ch8q2a3.py

Function3 = obtain_model -- process the show version output and return the
model (881) else return None.

Example of line:
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.

'''

def obtain_model(show_ver_file):
    ' return model of None '

    model = None

    show_ver_list = show_ver_file.split("\n")

    for line in show_ver_list:
        if 'bytes of memory' in line:
            model = line.split()[1]
            return model

    return model
