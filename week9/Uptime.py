#!/usr/bin/env python
'''

PyNet : Learning Python
 - Week 9, Question 2

Example of the uptime string:
'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
'3750RJ uptime is 1 hour, 29 minutes'
'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

'''

def process_uptime_string(uptime):
    '''
    Check for and process uptime variable
    '''
    uptime_list = uptime.split(", ")
    output = {}

    output["years"] = 0
    output["weeks"] = 0
    output["days"] = 0
    output["hours"] = 0
    output["minutes"] = 0

    for element in uptime_list:
        if "year" in element:
            output["years"] = element.split(" ")[0]
        if "week" in element:
            output["weeks"] = element.split(" ")[0]
        if "day" in element:
            output["days"] = element.split(" ")[0]
        if "hour" in element:
            output["hours"] = element.split(" ")[0]
        if "minute" in element:
            output["minutes"] = element.split(" ")[0]

    print(output)
    return output


class Uptime(object):
    " Uptime class "


    def __init__(self, uptime):
        " Creates Uptime object, takes uptime String as input "

        uptime_str = uptime.split("uptime is ")[1]
        uptime_dict = process_uptime_string(uptime_str)

        self.years = uptime_dict["years"]
        self.weeks = uptime_dict["weeks"]
        self.days = uptime_dict["days"]
        self.hours = uptime_dict["hours"]
        self.minutes = uptime_dict["minutes"]

    def uptime_in_seconds(self):
        " Return uptime in seconds "

        s_in_minute = 60
        s_in_hour = 60 * s_in_minute
        s_in_day = 24 * s_in_hour
        s_in_week = 7 * s_in_day
        s_in_year = 52 * s_in_week

        uptime_in_seconds = int(self.minutes) * s_in_minute + \
                            int(self.hours) * s_in_hour + \
                            int(self.days) * s_in_day + \
                            int(self.weeks) * s_in_week + \
                            int(self.years) * s_in_year

        print(str(uptime_in_seconds))
