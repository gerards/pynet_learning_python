#!/usr/bin/env python
'''

Pynet : Learning Python
 - Class 7, Question 4

'''

from glob import glob

def main():
    ' main one '

    cdp_files = glob('CDP_DATA/*_cdp.txt')

    for file in cdp_files:
        with open(file) as a_file:
            for line in a_file:
                #print(line.strip('\n'))
                if "show cdp neighbors detail" in line:
                    local_host = line.split(">")[0]
                    print(local_host)

                if "Device ID" in line:
                    remote_host = line.split(" ID: ")[1]
                    remote_host = remote_host.strip()
                    print(' -> ' + remote_host)


main()
