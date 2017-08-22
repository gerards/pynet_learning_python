#!/usr/bin/env python
'''

ch4q2.py

II. Parse the below 'show version' data and obtain the following items
(vendor, model, os_version, uptime, and serial_number).  Try to make your
string parsing generic i.e. it would work for other Cisco IOS devices.

The following are reasonable strings to look for:

'Cisco IOS Software' for vendor and os_version
'bytes of memory' for model
'Processor board ID' for serial_number
' uptime is ' for uptime

Store these variables (vendor, model, os_version, uptime, and serial_number) in
a dictionary.  Print the dictionary to standard output when done.

Note, "Cisco IOS Software...Version 15.0(1)M4...(fc1)" is one line.

'''

import pprint


def main():
    " MAIN! "
    device_details = {
        'vendor' : '',
        'model' : '',
        'os_version' : '',
        'uptime' : 0,
        'serial_number' : '', }

    show_version_data = \
'''
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support:
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102
'''

    show_version_lines = show_version_data.split('\n')
    for line in show_version_lines:
        if 'Cisco IOS Software' in line:
            vendor_line = line.split(", ")
            device_details['vendor'] = vendor_line[0].split()[0]
            device_details['model'] = vendor_line[1].split()[0]
            device_details['os_version'] = vendor_line[2].split()[1]

        if " uptime is " in line:
            uptime_line = line.split(" uptime is ")
            uptime_line = uptime_line[1].split(", ")
            seconds_per_minute = 60
            seconds_per_hour = 60 * seconds_per_minute
            seconds_per_day = 24 * seconds_per_hour
            seconds_per_week = 7 * seconds_per_day
            seconds_per_year = 52 * seconds_per_week

            for time in uptime_line:
                if 'year' in time:
                    device_details['uptime'] = seconds_per_year * int(time.split()[0])
                if 'week' in time:
                    device_details['uptime'] += seconds_per_week * int(time.split()[0])
                if 'day' in time:
                    device_details['uptime'] += seconds_per_day * int(time.split()[0])
                if 'hour' in time:
                    device_details['uptime'] += seconds_per_hour * int(time.split()[0])
                if 'minute' in time:
                    device_details['uptime'] += seconds_per_minute * int(time.split()[0])

        if "Processor board ID " in line:
            serial_line = line.split("Processor board ID ")
            device_details['serial_number'] = serial_line[1]

            pprint.pprint(device_details)

if __name__ == "__main__":
    main()
