#!/usr/bin/env python
#encoding=utf8


class Clock(object):
    def __init__(self, hour, minute):
        self.minutes = (hour * 60 + minute + 9999 * 1440) % 1440

    @property
    def hour(self):
        return divmod(self.minutes, 60)[0]

    @property
    def minute(self):
        return divmod(self.minutes, 60)[1]

    def __repr__(self):
        return '{0:02d}:{1:02d}'.format(self.hour, self.minute)

    def __eq__(self, other):
        return self.minutes == other.minutes

    def __add__(self, minutes):
        minutes = self.minutes + minutes
        self.minutes = (minutes + 9999 * 1440) % 1440
        return self

    def __sub__(self, minutes):
        minutes = self.minutes - minutes
        self.minutes = (minutes + 9999 * 1440) % 1440
        return self

    def __str__(self):
        return repr(self)
