#!/usr/bin/env python
'''

Testing Paramiko SSH connection to Cisco device

'''

import time
import paramiko


def disable_paging(remote_conn, command="terminal length 0\n", delay=1):
    ' Stop terminal paging, allow output to continue to completion '
    remote_conn.send("\n")
    remote_conn.send(command)

    # Wait for the command to complete
    time.sleep(delay)

    output = remote_conn.recv(65535)

    return output


def main():
    ' MAIN '

    ipaddr = '172.16.63.101'
    username = 'cisco'
    password = 'cisco'

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ipaddr, username=username, password=password)

    remote_conn = remote_conn_pre.invoke_shell()

    disable_paging(remote_conn)

    remote_conn.send("\n")
    remote_conn.send("show version\n")

    # Wait for the command to complete - terminal was design for human interaction
    time.sleep(1)

    output = remote_conn.recv(65535)
    print(output)


if __name__ == '__main__':
    main()
