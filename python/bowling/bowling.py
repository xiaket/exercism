#!/usr/bin/env python
#encoding=utf8


class BowlingGame(object):
    def __init__(self):
        self.frames = []
        self.current_frame = []
        self.max_pin = 10

    @property
    def items(self):
        return len(self.current_frame)

    @property
    def sums(self):
        return sum(self.current_frame)

    @property
    def is_fill(self):
        return sum(self.current_frame[:2]) % 10 == 0 and self.first

    @property
    def is_strike(self):
        return self.first == 10

    @property
    def first(self):
        return self.current_frame[0]

    def roll(self, pins):
        if pins > self.max_pin or pins < 0:
            raise ValueError("Bad pins number")

        if len(self.frames) == 10:
            raise IndexError("No more pins please")

        if not self.current_frame:
            self.current_frame.append(pins)
            if pins == 10 and len(self.frames) != 9:
                self.frames.append(self.current_frame)
                self.current_frame = []
            elif pins != 10:
                self.max_pin = 10 - pins
            return

        if len(self.frames) != 9:
            self.current_frame.append(pins)
            self.frames.append(self.current_frame)
            self.current_frame = []
            self.max_pin = 10
            return

        # If we can reach here, then it is the final frame and we already have
        # one or more items in self.current_frame.
        if self.items == 2 and not (self.is_strike or self.is_fill):
            raise IndexError("No more pins please")

        if self.items == 3:
            raise IndexError("No more pins please")

        self.current_frame.append(pins)
        if self.sums != 10 and pins != 10:
            self.max_pin = 10 - pins
        else:
            self.max_pin = 10

        if self.items == 2 and (not (self.is_strike or self.is_fill) or self.sums < 10):
            self.frames.append(self.current_frame)
            self.current_frame = []
        elif self.items == 3 and (self.is_strike or self.is_fill):
            self.frames.append(self.current_frame)
            self.current_frame = []

    def score(self):
        _score = 0
        if len(self.frames) != 10:
            raise IndexError("Not enough frames")

        for i, frame in enumerate(self.frames):
            if i == 9:
                if len(frame) == 2:
                    _score += sum(frame)
                elif frame[0] == 10 and sum(frame[1:]) == 10:
                    # strike and fill
                    _score += 20
                elif frame[0] == 10 and frame[1] == 10:
                    _score += (20 + frame[-1])
                elif sum(frame[:-1]) == 10:
                    _score += (10 + frame[-1])
                elif frame[0] == 10 and sum(frame[1:]) != 10:
                    _score += 10 + sum(frame[1:])
            elif sum(frame) < 10:
                _score += sum(frame)
            elif sum(frame) == 10 and len(frame) == 2:
                _score += (10 + self.frames[i+1][0])
            elif frame[0] == 10:
                if i < 8:
                    frames = self.frames[i + 1] + self.frames[i + 2]
                else:
                    frames = self.frames[i + 1]
                _score += (10 + sum(frames[:2]))


        return _score
