#!/usr/bin/env python
#encoding=utf8


def grep(pattern, files, flags=''):
    flags = [f for f in flags.split()]
    flag_i = '-i' in flags
    flag_l = '-l' in flags
    flag_n = '-n' in flags
    flag_v = '-v' in flags
    flag_x = '-x' in flags
    flag_m = len(files) > 1

    if flag_i:
        pattern = pattern.lower()

    def filter(line_):
        line = line_.lower() if flag_i else line_
        match = pattern == line.strip() if flag_x else pattern in line
        return not match if flag_v else match

    matches = []
    for name in files:
        with open(name) as fobj:
            for i, line in enumerate(fobj.readlines()):
                if not filter(line):
                    continue
                if flag_n:
                    line = "{}:{}".format(i + 1, line)
                if flag_l:
                    if name not in matches:
                        matches.append(name)
                    continue
                if flag_m:
                    matches.append("{}:{}".format(name, line))
                else:
                    matches.append(line)

    if flag_l:
        matches = [m + "\n" for m in matches]
    return ''.join(matches)
