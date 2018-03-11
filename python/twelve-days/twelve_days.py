#!/usr/bin/env python
#encoding=utf8

START = "On the {order} day of Christmas my true love gave to me, "
END = "a Partridge in a Pear Tree."
PARTS = {
    12: "twelve Drummers Drumming",
    11: "eleven Pipers Piping",
    10: "ten Lords-a-Leaping",
    9: "nine Ladies Dancing",
    8: "eight Maids-a-Milking",
    7: "seven Swans-a-Swimming",
    6: "six Geese-a-Laying",
    5: "five Gold Rings",
    4: "four Calling Birds",
    3: "three French Hens",
    2: "two Turtle Doves",
}

ORDERS = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
}


def recite(start_verse, end_verse):
    lyrics = []
    for i in range(start_verse, end_verse+1):
        start = START.format(order=ORDERS[i])
        end = END
        parts = ", ".join(PARTS[j] for j in range(i, 1, -1))
        if parts:
            parts += ", and "
        lyrics.append(start + parts + end)
    return lyrics
