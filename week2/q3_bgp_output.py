#!/usr/bin/env python

entry1 = "*  1.0.192.0/18   157.130.10.233     0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233     0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233     0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233     0 701 6762 6762 6762 6762 38040 9737 i"

entry1_list = entry1.split()
entry1_output = [entry1_list[1], entry1_list[3:-1]]
entry2_list = entry2.split()
entry2_output = [entry2_list[1], entry2_list[3:-1]]
entry3_list = entry3.split()
entry3_output = [entry3_list[1], entry3_list[3:-1]]
entry4_list = entry4.split()
entry4_output = [entry4_list[1], entry4_list[3:-1]]

print("%-20s%-60s" % ("IP Prefix", "AS Path"))
print("%-20s%-60s" % (entry1_output[0], entry1_output[1]))
print("%-20s%-60s" % (entry2_output[0], entry2_output[1]))
print("%-20s%-60s" % (entry3_output[0], entry3_output[1]))
print("%-20s%-60s" % (entry4_output[0], entry4_output[1]))
