#!/usr/bin/env python
#encoding=utf8

RECORD = {
    1: ("lay in", "the house that Jack built."),
    2: ("ate", "the malt"),
    3: ("killed", "the rat"),
    4: ("worried", "the cat"),
    5: ("tossed", "the dog"),
    6: ("milked", "the cow with the crumpled horn"),
    7: ("kissed", "the maiden all forlorn"),
    8: ("married", "the man all tattered and torn"),
    9: ("woke", "the priest all shaven and shorn"),
    10:("kept", "the rooster that crowed in the morn"),
    11:("belonged to", "the farmer sowing his corn"),
    12:("", "the horse and the hound and the horn"),
}


def recite_single(i):
    verse = ["This is " + RECORD[i][1]]
    count = 1
    while i > 1:
        verse.insert(1, " ".join([
            "that", RECORD[count][0], RECORD[count][1]
        ]))
        count +=1
        i -= 1

    return verse


def recite(start_verse, end_verse):
    verses = []
    for i in range(start_verse, end_verse+1):
        if verses:
            verses.append("")
        verses += recite_single(i)
    return verses
