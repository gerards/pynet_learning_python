#!/usr/bin/env python
"""

ch2q4

"""

def main():
    " MAIN! "
    cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), "\
                "Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

    cisco_version = cisco_ios.split(", ")[2]
    cisco_version = cisco_version.split()[1]
    print(cisco_version)

if __name__ == "__main__":
    main()
