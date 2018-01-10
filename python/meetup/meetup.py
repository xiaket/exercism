#!/usr/bin/env python
#encoding=utf8

import calendar


WEEKDAYS = [
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday",
]

WHICHES = {
    'first': 0,
    '1st': 0,
    'second': 1,
    '2nd': 1,
    'third': 2,
    '3rd': 2,
    'fourth': 3,
    '4th': 3,
    'fifth': 4,
    '5th': 4,
    'last': -1,
}


def meetup_day(year, month, day_of_the_week, which):
    cal = calendar.Calendar()
    iterator = cal.itermonthdates(year, month)
    dates = [d for d in iterator if WEEKDAYS.index(day_of_the_week) == d.weekday() and d.month == month]
    if which != 'teenth':
        return dates[WHICHES[which]]
    return [d for d in dates if 20 > d.day >= 10][-1]
