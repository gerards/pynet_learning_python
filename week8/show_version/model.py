#!/usr/bin/env python
'''

Pynet : Learning Python
 - Class 8, Question 2

This module get device model from the show version output

'''

def get_model(output):
    ' Get software version from show version output '
    lines = output.split("\n")
    for line in lines:
        if "bytes of memory" in line:
            return line.split(" ")[1]

def main():
    ' main one '
    file_show_ver = open('show_version.txt')
    show_ver_output = file_show_ver.read()
    print(get_model(show_ver_output))

if __name__ == '__main__':
    main()
