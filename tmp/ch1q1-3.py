#!/usr/bin/env python
"""

q1

"""

def main():
    " MAIN! "

    ipv6_addr = "FE80:0000:0000:0000:0101:A3EF:EE1E:1719"

    ipv6_split = ipv6_addr.split(":")

    print()
    print("IPv6 address split:")
    print(ipv6_split)
    print()

    ipv6_joined = ":".join(ipv6_split)

    print("IPv6 addresses joined:")
    print(ipv6_joined)
    print()


if __name__ == "__main__":
    main()
