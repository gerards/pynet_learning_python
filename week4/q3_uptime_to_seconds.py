#!/usr/bin/env python
'''
Pynet - Learning Python - Week 4

Question 3:
    - From the provided uptime strings process the string to obtain the
    uptime in seconds
'''


UPTIME1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
UPTIME2 = '3750RJ UPTIME is 1 hour, 29 minutes'
UPTIME3 = 'CATS3560 UPTIME is 8 weeks, 4 days, 18 hours, 16 minutes'
UPTIME4 = 'rtr1 UPTIME is 5 years, 18 weeks, 8 hours, 23 minutes'

SECONDS_PER_WEEK = 604800
SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

DEVICE_DETAILS = []

for uptime in (UPTIME1, UPTIME2, UPTIME3, UPTIME4):
    uptime_list = uptime.split(", ")
    temp_list = uptime_list[0].split()
    device_name = temp_list[0]
    uptime_list[0] = " ".join(temp_list[-2:])
    DEVICE_DETAILS.append({"device_name": device_name, "uptime": uptime_list})

for device in DEVICE_DETAILS:
    for time in device["uptime"]:
        total_seconds = 0
        if "week" in time:
            weeks = int(time.split()[0])
            total_seconds += weeks * SECONDS_PER_WEEK
        elif "day" in time:
            days = int(time.split()[0])
            total_seconds += days * SECONDS_PER_DAY
        elif "hour" in time:
            hours = int(time.split()[0])
            total_seconds += hours * SECONDS_PER_HOUR
        elif "minute" in time:
            minutes = int(time.split()[0])
            total_seconds += minutes * SECONDS_PER_MINUTE
        elif "second" in time:
            seconds = int(time.split()[0])
            total_seconds += seconds

        device["uptime_in_seconds"] = total_seconds

    print("\n%-20s : %-40s" % ("Device", device["device_name"]))
    print("%-20s : %-40s" % ("Uptime in seconds", device["uptime_in_seconds"]))
print("")
