#!/usr/bin/env python

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"
cisco_ios_split = cisco_ios.split(",")
cisco_ios_version = cisco_ios_split[2][9:]

print(cisco_ios_version)
