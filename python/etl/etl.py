#!/usr/bin/env python
#encoding=utf8

def transform(legacy_data):
    return {ch.lower(): [n for n in legacy_data if ch in legacy_data[n]][0] for chars in legacy_data.values() for ch in chars}
