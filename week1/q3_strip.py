#!/usr/bin/env python

import fileinput

for line in fileinput.input():
        ip_addr = []
        for octet in line.split("."):
            ip_addr.append(octet.strip())
        print(ip_addr)
