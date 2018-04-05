#!/usr/bin/env python
#encoding=utf8



class Scale(object):
    USE_SHARPS = "G D A E B F# C a e b f# c# g# d#".split()
    USE_FLATS = "F Bb Eb Ab Db Gb d g c f bb eb".split()

    JUMP = {
        'A': 3,
        'M': 2,
        'm': 1,
    }

    def __init__(self, tonic, intervals=None):
        self.tonic = tonic
        self.intervals = intervals
        if self.intervals and sum(self.JUMP[i] for i in intervals) != 12:
            raise ValueError("Invalid intervals")

    @property
    def scale(self):
        if self.tonic in self.USE_SHARPS:
            _scale = "A A# B C C# D D# E F F# G G#".split()
        else:
            _scale = "A Bb B C Db D Eb E F Gb G Ab".split()

        index = _scale.index(self.tonic.title())
        return _scale[index:] + _scale[:index]

    @property
    def pitches(self):
        if not self.intervals:
            return self.scale
        _pitches = []
        index = 0
        for ch in self.intervals:
            _pitches.append(self.scale[index])
            index += self.JUMP[ch]
        return _pitches
