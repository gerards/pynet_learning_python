#!/usr/bin/env python
'''

Paramiko example from Kirk Byers

'''

import time
import paramiko


def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''

    remote_conn.send("terminal length 0\n")
    time.sleep(1)

    # Clear the buffer on the screen
    output = remote_conn.recv(1000)

    return output


def main():
    ' MAIN! '
    # VARIABLES THAT NEED CHANGED
    ipaddr = '172.16.63.101'
    username = 'cisco'
    password = 'cisco'

    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts
    # (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(
        ipaddr,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )
    print("SSH connection established to %s" % ipaddr)

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print("Interactive SSH session established")

    # Stripaddr the initial router prompt
    output = remote_conn.recv(1000)

    # See what we have
    print(output.decode())

    # Turn off paging
    disable_paging(remote_conn)

    # Now let's try to send the router a command
    remote_conn.send("\n")
    remote_conn.send("show ver\n")

    # Wait for the command to complete
    time.sleep(1)

    output = remote_conn.recv(65535)
    print(output.decode())


if __name__ == '__main__':
    main()
