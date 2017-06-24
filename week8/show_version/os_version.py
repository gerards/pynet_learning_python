#!/usr/bin/env python
'''

Pynet : Learning Python
 - Class 8, Question 2

This module get the OS version from the show version output

'''

def get_version(output):
    ' Get software version from show version output '
    lines = output.split("\n")
    for line in lines:
        if "Cisco IOS Software" in line:
            return line.split(", ")[2]

def main():
    ' main one '
    file_show_ver = open('show_version.txt')
    show_ver_output = file_show_ver.read()
    print(get_version(show_ver_output))

if __name__ == '__main__':
    main()
