#!/usr/bin/env python
'''

Pynet : Learning Python
 - Class 8, Question 2

This module get the devices uptime from the show version output

'''

def get_uptime(output):
    ' Get devices uptime from show version output '
    lines = output.split("\n")
    for line in lines:
        if "uptime is" in line:
            uptime = line.split("uptime is ")[1]
            return "uptime is " + uptime

def main():
    ' main one '
    file_show_ver = open('show_version.txt')
    show_ver_output = file_show_ver.read()
    print(get_uptime(show_ver_output))

if __name__ == '__main__':
    main()
