#!/usr/bin/env python
'''

Login to a network device and collect device info from show version output

Create a script that can login to a network device (using either telnet or SSH) and
retrieve 'show version' from the device.

Process the 'show version' output and store the below attributes in a NetworkDevice object:

NetworkObject
    hostname
    ip
    username
    password
    device_type            # router, switch, firewall, etc.
    vendor
    model
    os_version
    uptime                        # seconds
    serial_number

This object should be stored to a file using pickle.

'''

import time
import pickle
import paramiko


class NetworkDevice():
    ' Network Device class '

    def __init__(self, ipaddr, username, password):
        self.ipaddr = ipaddr
        self.username = username
        self.password = password
        self.device_details = {
            'hostname': '',
            'ip': self.ipaddr,
            'username': self.username,
            'password': self.password,
            'vendor': '',
            'model': '',
            'os_version': '', 'uptime': 0,
            'serial_number': '',
        }

    def _connect(self, disable_paging=True):
        ' Setup connect to network device '
        # Create instance of SSHClient object
        remote_conn_pre = paramiko.SSHClient()

        # Automatically add untrusted hosts
        # (make sure okay for security policy in your environment)
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # initiate SSH connection
        remote_conn_pre.connect(
            self.ipaddr,
            username=self.username,
            password=self.password,
            look_for_keys=False,
            allow_agent=False,
        )

        # Use invoke_shell to establish an 'interactive session'
        remote_conn = remote_conn_pre.invoke_shell()

        if disable_paging:
            # Turn off paging
            remote_conn.send("terminal length 0\n")
            time.sleep(1)

        # Clear the buffer on the screen
        remote_conn.recv(1000)

        return remote_conn

    def send_command(self, command):
        ' Send command to network device and return output '
        remote_conn = self._connect()
        remote_conn.send("\n" + command + '\n')

        time.sleep(2)

        output = remote_conn.recv(65535)
        output = output.decode()
        remote_conn.close()

        return output

    def get_device_details(self):
        ' Return device details pulled from show version '
        show_version = self.send_command('show version')
        show_version_lines = show_version.split('\n')

        for line in show_version_lines:
            if 'Cisco IOS Software' in line:
                vendor_line = line.split(", ")
                self.device_details['vendor'] = vendor_line[0].split()[0]
                self.device_details['model'] = vendor_line[1].split()[0]
                self.device_details['os_version'] = vendor_line[2].split()[1]

            if " uptime is " in line:
                self.device_details['hostname'], uptime_line = line.split(" uptime is ")
                uptime_line = uptime_line.split(", ")
                seconds_per_minute = 60
                seconds_per_hour = 60 * seconds_per_minute
                seconds_per_day = 24 * seconds_per_hour
                seconds_per_week = 7 * seconds_per_day
                seconds_per_year = 52 * seconds_per_week

                for time_period in uptime_line:
                    if 'year' in time_period:
                        self.device_details['uptime'] = seconds_per_year * int(
                            time_period.split()[0])
                    if 'week' in time_period:
                        self.device_details['uptime'] += seconds_per_week * int(
                            time_period.split()[0])
                    if 'day' in time_period:
                        self.device_details['uptime'] += seconds_per_day * int(
                            time_period.split()[0])
                    if 'hour' in time_period:
                        self.device_details['uptime'] += seconds_per_hour * int(
                            time_period.split()[0])
                    if 'minute' in time_period:
                        self.device_details['uptime'] += seconds_per_minute * int(
                            time_period.split()[0])

            if "Processor board ID " in line:
                serial_line = line.split("Processor board ID ")
                self.device_details['serial_number'] = serial_line[1].strip()

        return self.device_details


def main():
    ' MAIN! '
    SW1 = NetworkDevice('172.16.63.100', 'cisco', 'cisco')
    R1 = NetworkDevice('172.16.63.101', 'cisco', 'cisco')
    R2 = NetworkDevice('172.16.63.102', 'cisco', 'cisco')
    network_devices = [SW1, R1, R2]

    for device in network_devices:
        print()
        device.get_device_details()
        for key, value in device.device_details.items():
            print("%15s : %-30s" % (key, value))

    pickle.dump(network_devices, open('foo.pickle', 'wb'))

    print("\n")
    print("Reading objects from pickle files:")
    with open('foo.pickle', 'rb') as f:
        netdev_objects = pickle.load(f)
        for netdev_obj in netdev_objects:
            print(50 * '-')
            for key, value in netdev_obj.device_details.items():
                print("%15s : %-30s" % (key, value))
        print(50 * '-')


if __name__ == '__main__':
    main()
