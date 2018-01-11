#!/usr/bin/env python
#encoding=utf8

# Globals for the bearings
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y

    def advance(self):
        self.x += self.bearing[0]
        self.y += self.bearing[1]

    def turn_right(self):
        self.bearing = (
            self.bearing[0] * 0 + self.bearing[1] * 1,
            self.bearing[0] * -1 + self.bearing[1] * 0,
        )

    def turn_left(self):
        self.bearing = (
            self.bearing[0] * 0 + self.bearing[1] * -1,
            self.bearing[0] * 1 + self.bearing[1] * 0,
        )

    def simulate(self, actions):
        for action in actions:
            if action == "L":
                self.turn_left()
            elif action == "R":
                self.turn_right()
            elif action == "A":
                self.advance()

    @property
    def coordinates(self):
        return (self.x, self.y)
