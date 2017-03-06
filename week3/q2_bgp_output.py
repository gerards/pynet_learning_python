#!/usr/bin/env python

entries = ["*  1.0.192.0/18   157.130.10.233     0 701 38040 9737 i",
           "*  1.1.1.0/24     157.130.10.233     0 701 1299 15169 i",
           "*  1.1.42.0/24    157.130.10.233     0 701 9505 17408 2.1465 i",
           "*  1.0.192.0/19   157.130.10.233     0 701 6762 6762 6762 6762 38040 9737 i"
           ]

def format_entry(entry):
    entry_split = entry.split()
    ip_prefix = entry_split[1]
    as_path = entry_split[3:-1]
    return ip_prefix, as_path

print("%-20s%-60s" % ("IP Prefix", "AS Path"))

for entry in entries:
    ip_prefix, as_path = format_entry(entry)
    print("%-20s%-60s" % (ip_prefix, as_path))
