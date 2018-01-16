#!/usr/bin/env python
#encoding=utf8

PLANETS = {
    'earth': 1,
    'mercury': 0.2408467,
    'venus': 0.61519726,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132,
}

SECONDS_IN_A_YEAR = 31557600


class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth = seconds / 1. / SECONDS_IN_A_YEAR

    def __getattr__(self, name):
        if name.startswith("on_") and name.split("_")[1] in PLANETS:
            result = round(self.earth / PLANETS[name.split("_")[1]], 2)
            return lambda : result
