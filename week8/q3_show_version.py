#!/usr/bin/env python
'''

Pynet : Learning Python
 - Class 8, Question 3

Import and use show_version package

'''
import show_version

def main():
    ' main stuff '
    a_file = open("./show_version/show_version.txt")
    file_guts = a_file.read()

    model = show_version.get_model(file_guts)
    os_version = show_version.get_version(file_guts)
    uptime = show_version.get_uptime(file_guts)

    print("%10s : %-30s" % ("model", model))
    print("%10s : %-30s" % ("os_version", os_version))
    print("%10s : %-30s" % ("uptime", uptime))


if __name__ == '__main__':
    main()
