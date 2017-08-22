#!/usr/bin/env python
'''

ch9q2.py

II. Create an Uptime class that takes in a Cisco IOS uptime string and parses the string
into years, weeks, days, hours, minutes (assigning these as attributes of the object).  For example:

>>> test_obj = Uptime('twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes')
>>> test_obj.years
0
>>> test_obj.weeks
6
>>> test_obj.days
4
>>> test_obj.hours
2
>>> test_obj.minutes
25



You class should be able to process the following four uptime strings:

'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
'3750RJ uptime is 1 hour, 29 minutes'
'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'


    A. Create a method for this class that returns the uptime in seconds.

>>> test_obj.uptime_seconds()
3983100

'''

import re


def find_uptime_field(a_pattern, uptime_str):
    '''
    If there is a match return the match group(1)

    Else return 0
    '''

    a_check = re.search(a_pattern, uptime_str)

    if a_check:
        return int(a_check.group(1))


class Uptime(object):
    '''
    Create an Uptime object for Cisco uptime strings
    '''

    def __init__(self, uptime_str):
        '''
        Initialise uptime object

        Questions about this code:
            1. Unsure here is best to have uptime_str a self.uptime_str as it is
        unique to the object?
            2. If self.uptime_str then the find_uptime_field needs to be
            updated to be a object method with self.uptime_str attribute passed
            instead?
        '''

        # [years, weeks, days, hours, minutes]
        uptime_list = [0, 0, 0, 0, 0]

        pattern_list = [
            r" ([0-9]+) year",
            r" ([0-9]+) week",
            r" ([0-9]+) day",
            r" ([0-9]+) hour",
            r" ([0-9]+) minute",
        ]

        for i, a_pattern in enumerate(pattern_list):
            uptime_list[i] = find_uptime_field(a_pattern, uptime_str)

        (self.years, self.weeks, self.days, self.hours, self.minutes) = uptime_list

    def uptime_seconds(self):
        '''
        Return uptime in seconds
        '''

        seconds_per_minute = 60
        seconds_per_hour = 60 * seconds_per_minute
        seconds_per_day = 24 * seconds_per_hour
        seconds_per_week = 7 * seconds_per_day
        seconds_per_year = 52 * seconds_per_week

        uptime_in_seconds = (
            seconds_per_year * self.years +
            seconds_per_week * self.weeks +
            seconds_per_day * self.days +
            seconds_per_hour * self.hours +
            seconds_per_minute * self.minutes
        )

        return uptime_in_seconds


def main():
    '''
    Test various uptime strings
    '''

    uptime_strings = [
        'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes',
        '3750RJ uptime is 1 hour, 29 minutes',
        'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes',
        'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes',
    ]

    for uptime_str in uptime_strings:

        test_obj = Uptime(uptime_str)

        print()
        print("> " + uptime_str)
        print("%-20s: %s" % ('years', test_obj.years))
        print("%-20s: %s" % ('weeks', test_obj.weeks))
        print("%-20s: %s" % ('days', test_obj.days))
        print("%-20s: %s" % ('hours', test_obj.hours))
        print("%-20s: %s" % ('minutes', test_obj.minutes))

        print("%-20s: %s" % ('Uptime in seconds: ', test_obj.uptime_seconds()))

    print()


if __name__ == "__main__":
    main()
